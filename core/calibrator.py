"""
Sigma calibrator: learns per-city, per-source forecast error from resolved markets.

After 30+ resolved trades, replaces the default sigma with the measured MAE.
This directly improves probability estimates and Kelly sizing.
"""

from datetime import datetime, timezone
from typing import Any

from core.config import DEFAULT_SIGMA_C, DEFAULT_SIGMA_F
from core.locations import LOCATIONS
from core.storage import load_calibration, save_calibration


def get_sigma(
    city_slug: str,
    source: str,
    calibration: dict[str, Any],
    horizon: str | None = None,
) -> float:
    """
    Return sigma (forecast std dev) for this city+source combination.

    Lookup priority:
      1. city_source_horizon  (e.g. "nyc_ecmwf_D+1")  — most specific
      2. city_source           (e.g. "nyc_ecmwf")      — flat calibrated
      3. unit default          (2.0°F / 1.2°C)

    Horizon-aware sigma significantly improves probability estimates:
      - D+1 ECMWF is much tighter than D+3 ECMWF
      - Bootstrap script pre-populates these from 90 days of history
    """
    if horizon:
        key_horizon = f"{city_slug}_{source}_{horizon}"
        if key_horizon in calibration:
            return calibration[key_horizon]["sigma"]

    key_flat = f"{city_slug}_{source}"
    if key_flat in calibration:
        return calibration[key_flat]["sigma"]

    loc = LOCATIONS.get(city_slug)
    return DEFAULT_SIGMA_F if (loc and loc.unit == "F") else DEFAULT_SIGMA_C


def run_calibration(
    markets: list[dict[str, Any]],
    calibration_min: int = 30,
) -> dict[str, Any]:
    """
    Recalculate sigma from resolved markets and persist.

    For each (city, source) pair:
      - Collect absolute errors |forecast_at_entry - actual_temp|
      - Compute MAE (mean absolute error)
      - Update calibration if MAE changed by >0.05

    Returns the updated calibration dict.
    """
    resolved = [
        m for m in markets
        if m.get("status") == "resolved" and m.get("actual_temp") is not None
    ]
    cal = load_calibration()
    updated: list[str] = []

    for source in ("ecmwf", "gfs", "metar"):
        cities = {m["city"] for m in resolved}
        for city in cities:
            group = [m for m in resolved if m["city"] == city]

            # Group errors by horizon (D+0, D+1, D+2, D+3) and flat (all)
            horizon_errors: dict[str, list[float]] = {}
            flat_errors: list[float] = []

            for mkt in group:
                snap = next(
                    (s for s in reversed(mkt.get("forecast_snapshots", []))
                     if s.get("best_source") == source),
                    None,
                )
                if snap is None or snap.get("best") is None:
                    continue
                err = abs(snap["best"] - mkt["actual_temp"])
                flat_errors.append(err)
                h = snap.get("horizon", "")
                if h:
                    horizon_errors.setdefault(h, []).append(err)

            loc = LOCATIONS.get(city)
            old_default = DEFAULT_SIGMA_F if (loc and loc.unit == "F") else DEFAULT_SIGMA_C
            city_name = LOCATIONS[city].name if city in LOCATIONS else city

            def _maybe_update(key: str, errors: list[float]) -> None:
                if len(errors) < calibration_min:
                    return
                mae = round(sum(errors) / len(errors), 3)
                old_sigma = cal.get(key, {}).get("sigma", old_default)
                cal[key] = {
                    "sigma":      mae,
                    "n":          len(errors),
                    "source":     "live",
                    "updated_at": datetime.now(timezone.utc).isoformat(),
                }
                if abs(mae - old_sigma) > 0.05:
                    updated.append(f"{city_name}/{source} {key.split('_')[-1]}: {old_sigma:.2f}→{mae:.2f}")

            _maybe_update(f"{city}_{source}", flat_errors)
            for horizon, h_errors in horizon_errors.items():
                _maybe_update(f"{city}_{source}_{horizon}", h_errors)

    save_calibration(cal)
    if updated:
        print(f"  [CAL] Updated: {', '.join(updated)}")
    return cal
