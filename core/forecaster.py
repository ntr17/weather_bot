"""
Weather data fetching from three sources:
  - ECMWF via Open-Meteo     (all cities, 7-day, bias-corrected, free)
  - GFS seamless via Open-Meteo (US cities, 3-day, hourly updates, free)
  - METAR via aviationweather.gov (real-time D+0 actual, free)
  - Visual Crossing          (actual resolved temp, ~$0.0001/call)

Bug fixes vs bot_v2:
  - Source was labelled "hrrr" but was actually gfs_seamless; now labelled correctly.
  - All fetches have retry logic with exponential backoff.
  - Snapshot selection uses consistent source priority logic.
"""

import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import requests

from core.config import Config
from core.locations import LOCATIONS, TIMEZONES


@dataclass
class ForecastSnapshot:
    ts: str
    ecmwf: float | None
    gfs: float | None     # was labelled "hrrr" in v1/v2 — it's actually GFS seamless
    metar: float | None
    best: float | None
    best_source: str | None
    model_spread: float | None = None  # abs(ecmwf - gfs) when both models available; used for sigma inflation


def _get_json(url: str, retries: int = 3, backoff: float = 3.0) -> dict:
    """GET with retries and exponential backoff."""
    for attempt in range(retries):
        try:
            resp = requests.get(url, timeout=(5, 10))
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            if attempt < retries - 1:
                time.sleep(backoff * (attempt + 1))
            else:
                raise exc
    return {}


def get_ecmwf(city_slug: str, dates: list[str]) -> dict[str, float]:
    """
    ECMWF IFS 0.25° daily max via Open-Meteo, bias-corrected.
    Updates at ~06:00 and 18:00 UTC with a ~6h lag.
    Returns {date_str: temp}.
    """
    loc = LOCATIONS[city_slug]
    temp_unit = "fahrenheit" if loc.unit == "F" else "celsius"
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={loc.lat}&longitude={loc.lon}"
        f"&daily=temperature_2m_max&temperature_unit={temp_unit}"
        f"&forecast_days=7&timezone={TIMEZONES.get(city_slug, 'UTC')}"
        f"&models=ecmwf_ifs025&bias_correction=true"
    )
    try:
        data = _get_json(url)
    except Exception as exc:
        print(f"  [ECMWF] {city_slug}: {exc}")
        return {}

    result: dict[str, float] = {}
    for date, temp in zip(
        data.get("daily", {}).get("time", []),
        data.get("daily", {}).get("temperature_2m_max", []),
    ):
        if date in dates and temp is not None:
            result[date] = round(float(temp), 1) if loc.unit == "C" else round(float(temp))
    return result


def get_gfs(city_slug: str, dates: list[str]) -> dict[str, float]:
    """
    GFS seamless (HRRR+GFS blend) daily max via Open-Meteo.
    US cities only; horizon limited to 3 days (most accurate within 48h).
    Updates hourly — most responsive model for short-range US.
    """
    loc = LOCATIONS[city_slug]
    if loc.region != "us":
        return {}

    temp_unit = "fahrenheit" if loc.unit == "F" else "celsius"
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={loc.lat}&longitude={loc.lon}"
        f"&daily=temperature_2m_max&temperature_unit={temp_unit}"
        f"&forecast_days=3&timezone={TIMEZONES.get(city_slug, 'UTC')}"
        f"&models=gfs_seamless"
    )
    try:
        data = _get_json(url)
    except Exception as exc:
        print(f"  [GFS] {city_slug}: {exc}")
        return {}

    result: dict[str, float] = {}
    for date, temp in zip(
        data.get("daily", {}).get("time", []),
        data.get("daily", {}).get("temperature_2m_max", []),
    ):
        if date in dates and temp is not None:
            result[date] = round(float(temp))
    return result


def get_metar(city_slug: str) -> float | None:
    """
    Current observed temperature from the ICAO METAR station.
    Only valid for D+0 (today). Returns Fahrenheit or Celsius per location unit.
    """
    loc = LOCATIONS[city_slug]
    try:
        url = f"https://aviationweather.gov/api/data/metar?ids={loc.station}&format=json"
        data = _get_json(url, retries=2)
        if data and isinstance(data, list):
            temp_c = data[0].get("temp")
            if temp_c is not None:
                temp_c = float(temp_c)
                if loc.unit == "F":
                    return round(temp_c * 9 / 5 + 32)
                return round(temp_c, 1)
    except Exception as exc:
        print(f"  [METAR] {city_slug}: {exc}")
    return None


def get_actual_temp(city_slug: str, date_str: str, vc_key: str) -> float | None:
    """
    Actual maximum temperature for a past date via Visual Crossing.
    Queries the ICAO station code (airport) — this is what Polymarket resolves on.
    Cost: ~$0.0001/call on free tier.
    """
    loc = LOCATIONS[city_slug]
    vc_unit = "us" if loc.unit == "F" else "metric"
    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
        f"/{loc.station}/{date_str}/{date_str}"
        f"?unitGroup={vc_unit}&key={vc_key}&include=days&elements=tempmax"
    )
    try:
        data = _get_json(url, retries=2)
        days = data.get("days", [])
        if days and days[0].get("tempmax") is not None:
            return round(float(days[0]["tempmax"]), 1)
    except Exception as exc:
        print(f"  [VC] {city_slug} {date_str}: {exc}")
    return None


def take_snapshot(city_slug: str, dates: list[str]) -> dict[str, ForecastSnapshot]:
    """
    Fetch all sources and build a ForecastSnapshot per date.

    Source priority:
      - US D+0/D+1, both models: ensemble mean (ECMWF+GFS)/2; model_spread stored
      - US D+0/D+1, GFS only:   GFS
      - All others:             ECMWF
      - D+0 override:           METAR only if it EXCEEDS the model max (daily high achieved)
    """
    now_utc = datetime.now(timezone.utc)
    now_str = now_utc.isoformat()
    today = now_utc.strftime("%Y-%m-%d")
    d1 = (now_utc + timedelta(days=1)).strftime("%Y-%m-%d")

    ecmwf = get_ecmwf(city_slug, dates)
    gfs = get_gfs(city_slug, dates)   # empty for non-US

    loc = LOCATIONS[city_slug]
    snapshots: dict[str, ForecastSnapshot] = {}

    for date in dates:
        ecmwf_val = ecmwf.get(date)
        gfs_val = gfs.get(date) if date in (today, d1) else None
        metar_val = get_metar(city_slug) if date == today else None

        # Pick best forecast source / ensemble mean
        model_spread = None
        if loc.region == "us" and gfs_val is not None and ecmwf_val is not None:
            # Both models available — use ensemble mean and record their disagreement.
            # The spread is passed to the trading loop to inflate sigma proportionally.
            best = round((ecmwf_val + gfs_val) / 2.0)
            best_source = "ensemble"
            model_spread = round(abs(ecmwf_val - gfs_val), 1)
        elif loc.region == "us" and gfs_val is not None:
            best, best_source = gfs_val, "gfs"
        elif ecmwf_val is not None:
            best, best_source = ecmwf_val, "ecmwf"
        else:
            best, best_source = None, None

        # METAR overrides best for D+0 ONLY if it exceeds the model forecast.
        # METAR is the current observed temperature — NOT the daily maximum.
        # Overriding with METAR is valid only once the daily high has already occurred
        # (i.e., the observed temp beats the model's predicted max).
        if date == today and metar_val is not None:
            if best is None or metar_val > best:
                best, best_source = metar_val, "metar"
                model_spread = None  # direct observation; model disagreement irrelevant

        snapshots[date] = ForecastSnapshot(
            ts=now_str,
            ecmwf=ecmwf_val,
            gfs=gfs_val,
            metar=metar_val,
            best=best,
            best_source=best_source,
            model_spread=model_spread,
        )

    return snapshots
