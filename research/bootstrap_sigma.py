"""
Bootstrap sigma calibration from 90 days of historical data.

For each city and forecast source (ECMWF, GFS), fetches what the model
predicted at D+1, D+2, and D+3 lag vs what actually happened at the airport.
Computes MAE (mean absolute error) per (city, source, horizon) triplet and
writes it to data/calibration.json in the same format the live calibrator uses.

This lets the bot trade with real sigma values from day 1, instead of the
hardcoded 2.0°F / 1.2°C fallback.

Run ONCE on the personal machine before starting the bot:
    python research/bootstrap_sigma.py

No API keys needed — Open-Meteo historical is free.
Requires: requests, python >= 3.10

HOW THE LAG SIMULATION WORKS:
  Open-Meteo's historical-forecast API lets you specify a `forecast_days`
  parameter with a past `start_date`. For example, requesting 3-day forecasts
  starting on 2025-01-01 gives you what the model *would have predicted* on
  that day for Jan 1, Jan 2, and Jan 3. Comparing that to the actual (from the
  reanalysis API) gives genuine forecast error at each horizon.

  We iterate over 90 past days, treating each as the "issue date" and collecting
  errors for the D+1, D+2, D+3 predictions issued on that day.
"""

import json
import sys
import time
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
BACKOFF       = 2.0      # Seconds between API calls (Open-Meteo is free but polite)

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


def fetch_historical_forecast(
    lat: float, lon: float,
    issue_date: str,
    horizon: int,
    unit: str,
    tz: str,
    model: str,
) -> float | None:
    """
    What did `model` predict on `issue_date` for `issue_date + horizon days`?
    Uses Open-Meteo's historical forecast API.

    The API accepts past start_date + forecast_days to reconstruct what was
    predicted at that issue time.
    Returns the predicted daily max temp or None.
    """
    temp_unit = "fahrenheit" if unit == "F" else "celsius"
    target_date = (date.fromisoformat(issue_date) + timedelta(days=horizon)).isoformat()
    forecast_days = horizon + 1   # need enough days to reach target

    try:
        data = _get("https://historical-forecast-api.open-meteo.com/v1/forecast", {
            "latitude":         lat,
            "longitude":        lon,
            "start_date":       issue_date,
            "end_date":         issue_date,
            "daily":            "temperature_2m_max",
            "temperature_unit": temp_unit,
            "timezone":         tz,
            "models":           model,
            "forecast_days":    forecast_days,
        })
    except Exception:
        return None

    for d, t in zip(
        data.get("daily", {}).get("time", []),
        data.get("daily", {}).get("temperature_2m_max", []),
    ):
        if d == target_date and t is not None:
            return round(float(t), 1) if unit == "C" else round(float(t))
    return None


# ── Main calibration loop ─────────────────────────────────────────────────────

def bootstrap(cities: list[str] | None = None) -> None:
    today = date.today()
    # Leave a 2-day buffer — ERA5 reanalysis has ~2-day lag
    end_date   = today - timedelta(days=3)
    start_date = end_date - timedelta(days=LOOKBACK_DAYS - 1)

    target_cities = cities or list(LOCATIONS.keys())
    cal = load_calibration()

    # model slug → calibration source name
    model_map = {
        "ecmwf_ifs025": "ecmwf",
        "gfs_seamless":  "gfs",
    }

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

        for model_slug, source_name in model_map.items():
            # GFS is US-only in reality, but we try it for all and skip if empty
            for horizon in HORIZONS:
                key = f"{city_slug}_{source_name}_D+{horizon}"
                errors: list[float] = []

                print(f"  {source_name} D+{horizon}:", end=" ", flush=True)

                # Iterate issue dates: for each past day, get the D+horizon forecast
                issue = start_date
                while issue <= end_date - timedelta(days=horizon):
                    issue_str  = issue.isoformat()
                    target_str = (issue + timedelta(days=horizon)).isoformat()
                    actual     = actuals.get(target_str)
                    if actual is None:
                        issue += timedelta(days=1)
                        continue

                    pred = fetch_historical_forecast(
                        loc.lat, loc.lon, issue_str, horizon,
                        loc.unit, tz, model_slug,
                    )
                    if pred is not None:
                        errors.append(abs(pred - actual))

                    time.sleep(0.5)   # polite to API
                    issue += timedelta(days=1)

                if len(errors) < MIN_SAMPLES:
                    print(f"only {len(errors)} samples — skip")
                    continue

                mae = round(sum(errors) / len(errors), 3)
                existing = cal.get(key, {})
                old_sigma = existing.get("sigma", 0)

                cal[key] = {
                    "sigma":        mae,
                    "n":            len(errors),
                    "source":       "bootstrap",
                    "updated_at":   datetime.now(timezone.utc).isoformat(),
                }
                change = f" (was {old_sigma:.2f})" if old_sigma else " (new)"
                print(f"MAE={mae:.2f}°{loc.unit}{change}")

        # Also write the flat (non-horizon) key so get_sigma() fallback works
        # Use the D+1 ECMWF value as the generic sigma for this city
        d1_key = f"{city_slug}_ecmwf_D+1"
        if d1_key in cal:
            flat_key = f"{city_slug}_ecmwf"
            if flat_key not in cal or cal[flat_key].get("source") == "bootstrap":
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
