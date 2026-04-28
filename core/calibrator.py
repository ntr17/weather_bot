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
) -> float:
    """
    Return calibrated sigma for this city+source pair.
    Falls back to default if not enough data yet.
    """
    key = f"{city_slug}_{source}"
    if key in calibration:
        return calibration[key]["sigma"]
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
            errors: list[float] = []

            for mkt in group:
                snap = next(
                    (s for s in reversed(mkt.get("forecast_snapshots", []))
                     if s.get("best_source") == source),
                    None,
                )
                if snap and snap.get("best") is not None:
                    errors.append(abs(snap["best"] - mkt["actual_temp"]))

            if len(errors) < calibration_min:
                continue

            mae = sum(errors) / len(errors)
            key = f"{city}_{source}"
            loc = LOCATIONS.get(city)
            old_default = DEFAULT_SIGMA_F if (loc and loc.unit == "F") else DEFAULT_SIGMA_C
            old_sigma = cal.get(key, {}).get("sigma", old_default)
            new_sigma = round(mae, 3)

            cal[key] = {
                "sigma":      new_sigma,
                "n":          len(errors),
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }

            if abs(new_sigma - old_sigma) > 0.05:
                city_name = LOCATIONS[city].name if city in LOCATIONS else city
                updated.append(f"{city_name}/{source}: {old_sigma:.2f}→{new_sigma:.2f}")

    save_calibration(cal)
    if updated:
        print(f"  [CAL] Updated: {', '.join(updated)}")
    return cal
