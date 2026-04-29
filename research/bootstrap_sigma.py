"""
Bootstrap sigma calibration from 90 days of ERA5 historical data.

Uses a PERSISTENCE forecast as a proxy for NWP forecast error:
  - D+1 "forecast" = today's actual temperature
  - D+2 "forecast" = today's actual temperature
  - etc.
  - Error = |actual(day + H) - actual(day)|

Persistence consistently OVERESTIMATES NWP model error (ECMWF beats persistence
by a wide margin), so the resulting sigma values are conservative:
  → smaller Kelly bets → safer trading until real calibration kicks in.

Uses ONLY the free Open-Meteo ERA5 archive API. No paid endpoints.

Run ONCE on the personal machine before starting the bot:
    python research/bootstrap_sigma.py

No API keys needed — ERA5 archive (archive-api.open-meteo.com) is free.
Requires: requests, python >= 3.10

Once 30+ trades resolve, the live calibrator (core/calibrator.py) will
automatically replace these bootstrap values with real forecast errors.
"""

import json
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

# ── Path setup ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from core.locations import LOCATIONS, TIMEZONES
from core.storage import load_calibration, save_calibration

# ── Config ────────────────────────────────────────────────────────────────────
LOOKBACK_DAYS = 90       # How many past days to analyze
MIN_SAMPLES   = 20       # Minimum samples before writing a sigma value
BACKOFF       = 0.5      # Seconds between API calls (Open-Meteo is free but polite)

# Horizons to calibrate.  D+0 is omitted — METAR handles D+0 live.
HORIZONS = [1, 2, 3]


# ── API helpers ───────────────────────────────────────────────────────────────

def _get(url: str, params: dict) -> dict:
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, timeout=(8, 15))
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            if attempt < 2:
                time.sleep(BACKOFF * (attempt + 1))
            else:
                raise
    return {}


def fetch_actual(lat: float, lon: float, start: str, end: str,
                 unit: str, timezone: str) -> dict[str, float]:
    """
    Actual daily max temperature from ERA5 reanalysis (what really happened).
    ERA5 is available via Open-Meteo historical API, free.
    Returns {date_str: temp}.
    """
    temp_unit = "fahrenheit" if unit == "F" else "celsius"
    data = _get("https://archive-api.open-meteo.com/v1/archive", {
        "latitude":         lat,
        "longitude":        lon,
        "start_date":       start,
        "end_date":         end,
        "daily":            "temperature_2m_max",
        "temperature_unit": temp_unit,
        "timezone":         timezone,
    })
    result: dict[str, float] = {}
    for d, t in zip(
        data.get("daily", {}).get("time", []),
        data.get("daily", {}).get("temperature_2m_max", []),
    ):
        if t is not None:
            result[d] = round(float(t), 1) if unit == "C" else round(float(t))
    return result


def compute_persistence_errors(actuals: dict[str, float], horizon: int) -> list[float]:
    """
    Compute forecast errors using persistence as a proxy for NWP.

    Persistence forecast: "tomorrow will be the same as today."
    Error at horizon H = |actual(day + H) - actual(day)|

    This overestimates NWP error (ECMWF beats persistence), making sigma values
    conservative. Bets will be smaller than optimal until the live calibrator
    accumulates 30+ resolved trades and replaces these values.
    """
    errors: list[float] = []
    for day_str, today_temp in sorted(actuals.items()):
        target_str = (date.fromisoformat(day_str) + timedelta(days=horizon)).isoformat()
        actual_target = actuals.get(target_str)
        if actual_target is not None:
            errors.append(abs(actual_target - today_temp))
    return errors


# ── Main calibration loop ─────────────────────────────────────────────────────

def bootstrap(cities: list[str] | None = None) -> None:
    today = date.today()
    # Leave a 2-day buffer — ERA5 reanalysis has ~2-day lag
    end_date   = today - timedelta(days=3)
    start_date = end_date - timedelta(days=LOOKBACK_DAYS - 1)

    target_cities = cities or list(LOCATIONS.keys())
    cal = load_calibration()

    total_cities = len(target_cities)
    for ci, city_slug in enumerate(target_cities, 1):
        loc = LOCATIONS[city_slug]
        tz  = TIMEZONES.get(city_slug, "UTC")
        print(f"\n[{ci}/{total_cities}] {loc.name} ({loc.unit})")

        # Fetch actuals once for this city+period
        print("  fetching ERA5 actuals...", end=" ", flush=True)
        try:
            actuals = fetch_actual(
                loc.lat, loc.lon,
                start_date.isoformat(),
                end_date.isoformat(),
                loc.unit,
                tz,
            )
            time.sleep(BACKOFF)
        except Exception as exc:
            print(f"FAIL ({exc}) — skipping")
            continue
        print(f"{len(actuals)} days")

        for horizon in HORIZONS:
            errors = compute_persistence_errors(actuals, horizon)
            print(f"  persistence D+{horizon}:", end=" ", flush=True)

            if len(errors) < MIN_SAMPLES:
                print(f"only {len(errors)} samples — skip")
                continue

            mae = round(sum(errors) / len(errors), 3)
            # Convert MAE to std dev: for a normal distribution, σ = MAE × √(π/2) ≈ 1.2533
            sigma = round(mae * 1.2533, 3)

            # Write for both ecmwf and gfs (persistence is model-agnostic;
            # live calibrator will refine these after 30+ real resolved trades)
            for source_name in ("ecmwf", "gfs"):
                key = f"{city_slug}_{source_name}_D+{horizon}"
                existing = cal.get(key, {})
                old_sigma = existing.get("sigma", 0)
                change = f" (was {old_sigma:.2f})" if old_sigma else " (new)"
                cal[key] = {
                    "sigma":      sigma,
                    "mae":        mae,
                    "n":          len(errors),
                    "source":     "bootstrap_persistence",
                    "updated_at": datetime.now(timezone.utc).isoformat(),
                }
            print(f"MAE={mae:.2f}°{loc.unit} → σ={sigma:.2f}{change}")

        # Write flat ecmwf key (D+1 proxy) for get_sigma() fallback
        d1_key = f"{city_slug}_ecmwf_D+1"
        if d1_key in cal:
            flat_key = f"{city_slug}_ecmwf"
            if flat_key not in cal or cal[flat_key].get("source", "").startswith("bootstrap"):
                cal[flat_key] = {**cal[d1_key], "horizon": "D+1_proxy"}

        save_calibration(cal)  # save after each city — safe to interrupt

    print(f"\n✓ Bootstrap complete. {len(cal)} calibration entries in data/calibration.json")
    _print_summary(cal)


def _print_summary(cal: dict) -> None:
    print("\n── Summary ──────────────────────────────────────────────────")
    from core.config import DEFAULT_SIGMA_F, DEFAULT_SIGMA_C
    cities_done = sorted({k.split("_")[0] for k in cal if "_ecmwf_" in k})
    for city in cities_done:
        loc = LOCATIONS.get(city)
        if not loc:
            continue
        default = DEFAULT_SIGMA_F if loc.unit == "F" else DEFAULT_SIGMA_C
        row = f"  {loc.name:<18}"
        for src in ("ecmwf", "gfs"):
            for h in HORIZONS:
                k = f"{city}_{src}_D+{h}"
                if k in cal:
                    row += f"  {src}/D+{h}={cal[k]['sigma']:.1f}"
        print(row + f"  (default was {default}°{loc.unit})")
    print("─────────────────────────────────────────────────────────────\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Bootstrap sigma from historical forecasts")
    parser.add_argument(
        "--cities", nargs="*", default=None,
        help="City slugs to process (default: all). E.g. --cities nyc chicago miami"
    )
    parser.add_argument(
        "--days", type=int, default=LOOKBACK_DAYS,
        help=f"Days of history to use (default: {LOOKBACK_DAYS})"
    )
    args = parser.parse_args()
    LOOKBACK_DAYS = args.days
    bootstrap(cities=args.cities)
