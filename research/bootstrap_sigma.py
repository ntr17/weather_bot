"""
Bootstrap sigma calibration from REAL historical model forecast errors.

Primary source — Open-Meteo Previous Runs API (free):
  https://previous-runs-api.open-meteo.com/v1/forecast
  `temperature_2m_previous_dayN` is the temperature that the model predicted
  N days in advance for each hour. We take the daily max per lead time and
  compare it with the ERA5 archive actual daily max. That is the true
  forecast error at horizon D+N — exactly what bucket_prob() needs.

Fallback — persistence error |actual(d+H) - actual(d)|. Persistence
substantially OVERESTIMATES NWP error. The v1 bootstrap used persistence for
everything, which produced sigmas up to 17°F; for a NO-selling strategy
inflated sigma is NOT conservative — it deflates p(YES) on near-forecast
buckets and made the bot systematically buy NO on likely buckets.
Fallback entries are labelled `bootstrap_persistence_fallback` and are
clamped at read time by core/calibrator.get_sigma().

Run on the personal machine (or CI) — re-run safe, never overwrites
calibration entries learned from live resolved trades:
    python research/bootstrap_sigma.py
"""

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from core.locations import LOCATIONS, TIMEZONES
from core.storage import load_calibration, save_calibration

LOOKBACK_DAYS = 90       # Previous Runs API supports up to 92 past days
MIN_SAMPLES   = 20       # Minimum samples before writing a sigma value
BACKOFF       = 0.5      # Seconds between API calls

HORIZONS = [1, 2, 3]     # D+0 is handled live by METAR

# calibration source name -> Open-Meteo model id
MODELS = {"ecmwf": "ecmwf_ifs025", "gfs": "gfs_seamless"}


def _get(url: str, params: dict) -> dict:
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, timeout=(8, 30))
            resp.raise_for_status()
            return resp.json()
        except Exception:
            if attempt < 2:
                time.sleep(BACKOFF * (attempt + 1))
            else:
                raise
    return {}


def fetch_actual(lat: float, lon: float, start: str, end: str,
                 unit: str, tz: str) -> dict[str, float]:
    """Actual daily max temperature from ERA5 reanalysis. {date_str: temp}."""
    temp_unit = "fahrenheit" if unit == "F" else "celsius"
    data = _get("https://archive-api.open-meteo.com/v1/archive", {
        "latitude":         lat,
        "longitude":        lon,
        "start_date":       start,
        "end_date":         end,
        "daily":            "temperature_2m_max",
        "temperature_unit": temp_unit,
        "timezone":         tz,
    })
    result: dict[str, float] = {}
    for d, t in zip(
        data.get("daily", {}).get("time", []),
        data.get("daily", {}).get("temperature_2m_max", []),
    ):
        if t is not None:
            result[d] = round(float(t), 1) if unit == "C" else round(float(t))
    return result


def fetch_model_daily_max(lat: float, lon: float, model_id: str,
                          unit: str, tz: str) -> dict[int, dict[str, float]]:
    """
    Daily max per forecast lead time from the Previous Runs API.

    Returns {horizon: {date_str: forecast_daily_max}} where the forecast was
    issued `horizon` days before the date.
    """
    temp_unit = "fahrenheit" if unit == "F" else "celsius"
    hourly_vars = [f"temperature_2m_previous_day{h}" for h in HORIZONS]
    data = _get("https://previous-runs-api.open-meteo.com/v1/forecast", {
        "latitude":         lat,
        "longitude":        lon,
        "hourly":           ",".join(hourly_vars),
        "models":           model_id,
        "past_days":        LOOKBACK_DAYS,
        "forecast_days":    1,
        "temperature_unit": temp_unit,
        "timezone":         tz,
    })

    hourly = data.get("hourly", {})
    times = hourly.get("time", [])
    out: dict[int, dict[str, float]] = {}

    for h in HORIZONS:
        # With a single model the key is plain; with multiple it gets a suffix.
        prefix = f"temperature_2m_previous_day{h}"
        key = next((k for k in hourly if k == prefix or k.startswith(prefix + "_")), None)
        if key is None:
            continue
        daily_max: dict[str, float] = {}
        for ts, temp in zip(times, hourly.get(key, [])):
            if temp is None:
                continue
            day = ts[:10]
            if day not in daily_max or temp > daily_max[day]:
                daily_max[day] = float(temp)
        out[h] = {
            d: (round(t, 1) if unit == "C" else round(t))
            for d, t in daily_max.items()
        }
    return out


def compute_persistence_errors(actuals: dict[str, float], horizon: int) -> list[float]:
    """Fallback proxy: error of the 'tomorrow = today' forecast at horizon H."""
    errors: list[float] = []
    for day_str, today_temp in sorted(actuals.items()):
        target_str = (date.fromisoformat(day_str) + timedelta(days=horizon)).isoformat()
        actual_target = actuals.get(target_str)
        if actual_target is not None:
            errors.append(abs(actual_target - today_temp))
    return errors


def _write_key(cal: dict, key: str, errors: list[float], source_label: str,
               unit: str) -> str | None:
    """Write one calibration entry from an error list. Never clobbers live data."""
    if len(errors) < MIN_SAMPLES:
        return None
    if cal.get(key, {}).get("source") == "live":
        return None   # live calibration from resolved trades wins
    mae = round(sum(errors) / len(errors), 3)
    # MAE -> std dev for a normal distribution: σ = MAE × √(π/2)
    sigma = round(mae * 1.2533, 3)
    cal[key] = {
        "sigma":      sigma,
        "mae":        mae,
        "n":          len(errors),
        "source":     source_label,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    return f"{key}: MAE={mae:.2f}°{unit} σ={sigma:.2f}"


def bootstrap(cities: list[str] | None = None) -> None:
    today = date.today()
    end_date = today - timedelta(days=3)            # ERA5 has ~2-day lag
    start_date = end_date - timedelta(days=LOOKBACK_DAYS - 1)

    target_cities = cities or list(LOCATIONS.keys())
    cal = load_calibration()

    for ci, city_slug in enumerate(target_cities, 1):
        loc = LOCATIONS[city_slug]
        tz = TIMEZONES.get(city_slug, "UTC")
        print(f"\n[{ci}/{len(target_cities)}] {loc.name} ({loc.unit})")

        try:
            actuals = fetch_actual(loc.lat, loc.lon, start_date.isoformat(),
                                   end_date.isoformat(), loc.unit, tz)
            time.sleep(BACKOFF)
        except Exception as exc:
            print(f"  ERA5 actuals FAILED ({exc}) — skipping city")
            continue
        print(f"  ERA5 actuals: {len(actuals)} days")

        for source_name, model_id in MODELS.items():
            if source_name == "gfs" and loc.region != "us":
                continue

            model_ok = False
            try:
                forecasts = fetch_model_daily_max(loc.lat, loc.lon, model_id,
                                                  loc.unit, tz)
                time.sleep(BACKOFF)
                for h in HORIZONS:
                    errors = [
                        abs(fc - actuals[d])
                        for d, fc in forecasts.get(h, {}).items()
                        if d in actuals
                    ]
                    msg = _write_key(cal, f"{city_slug}_{source_name}_D+{h}",
                                     errors, "bootstrap_model", loc.unit)
                    if msg:
                        model_ok = True
                        print(f"  {msg}")
            except Exception as exc:
                print(f"  {source_name} previous-runs FAILED ({exc})")

            if not model_ok:
                # Persistence fallback — clamped at read time by get_sigma()
                for h in HORIZONS:
                    errors = compute_persistence_errors(actuals, h)
                    msg = _write_key(cal, f"{city_slug}_{source_name}_D+{h}",
                                     errors, "bootstrap_persistence_fallback",
                                     loc.unit)
                    if msg:
                        print(f"  {msg} (persistence fallback)")

        # Flat key for get_sigma() fallback when no horizon-specific entry
        d1_key = f"{city_slug}_ecmwf_D+1"
        flat_key = f"{city_slug}_ecmwf"
        if d1_key in cal and cal.get(flat_key, {}).get("source") != "live":
            cal[flat_key] = {**cal[d1_key], "horizon": "D+1_proxy"}

        save_calibration(cal)   # save per city — safe to interrupt

    # Relabel any v1 persistence keys we didn't regenerate (e.g. gfs keys the
    # old script wrote for non-US cities). Values are clamped at read time;
    # the relabel stops CI from re-running the bootstrap forever.
    relabeled = 0
    for key, entry in cal.items():
        slug = key.split("_")[0]
        if entry.get("source") == "bootstrap_persistence" and slug in target_cities:
            entry["source"] = "bootstrap_persistence_fallback"
            relabeled += 1
    if relabeled:
        save_calibration(cal)
        print(f"  relabeled {relabeled} leftover persistence keys")

    print(f"\n✓ Bootstrap complete. {len(cal)} calibration entries.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Bootstrap sigma from real historical model forecast errors")
    parser.add_argument("--cities", nargs="*", default=None,
                        help="City slugs (default: all)")
    parser.add_argument("--days", type=int, default=LOOKBACK_DAYS,
                        help=f"Days of history (default {LOOKBACK_DAYS}, max 92)")
    args = parser.parse_args()
    LOOKBACK_DAYS = min(args.days, 92)
    bootstrap(cities=args.cities)
