"""
Phase 0 — Empirical proof script.

Measures the historical temperature delta between:
  - Airport ICAO coordinates  (what Polymarket resolves on)
  - City-centre coordinates   (what most market participants price on)

For each city, fetches the past 90 days of daily max temps from Open-Meteo
at BOTH coordinate sets and computes:
  - Mean delta (airport − city-centre)
  - Std dev of delta
  - Fraction of days where delta crosses a 1°F / 1°C bucket boundary
  - Seasonal breakdown (summer vs winter)

Run with:
  python research/airport_offset.py

No API keys required — Open-Meteo is free.
Outputs a summary table + saves JSON to research/data/airport_offset.json.

INTERPRETING RESULTS:
  - Delta mean ≠ 0  →  systematic mispricing exists
  - |delta| ≥ 1°F on >20% of days  →  bucket-crossing is common
  - These two together = the edge is real; proceed to Phase 1
  - If delta mean ≈ 0 and bucket-crossing < 10% → revisit thesis
"""

import json
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import requests

# ── City-centre coordinates (what weather apps / market participants see) ─────
# These are approximate downtown / Central Park / city-center lat/lon.
CITY_CENTERS: dict[str, tuple[float, float]] = {
    "nyc":          (40.7128,  -74.0060),   # Manhattan
    "chicago":      (41.8781,  -87.6298),   # The Loop
    "miami":        (25.7617,  -80.1918),   # Downtown Miami
    "dallas":       (32.7767,  -96.7970),   # Downtown Dallas
    "seattle":      (47.6062, -122.3321),   # Downtown Seattle
    "atlanta":      (33.7490,  -84.3880),   # Downtown Atlanta
    "london":       (51.5074,   -0.1278),   # City of London
    "tokyo":        (35.6762,  139.6503),   # Shinjuku
}

# Airport (ICAO) coordinates — Polymarket resolves on these
AIRPORTS: dict[str, tuple[float, float, str]] = {
    "nyc":          (40.7772,  -73.8726,  "KLGA"),
    "chicago":      (41.9742,  -87.9073,  "KORD"),
    "miami":        (25.7959,  -80.2870,  "KMIA"),
    "dallas":       (32.8471,  -96.8518,  "KDAL"),
    "seattle":      (47.4502, -122.3088,  "KSEA"),
    "atlanta":      (33.6407,  -84.4277,  "KATL"),
    "london":       (51.5048,    0.0495,  "EGLC"),
    "tokyo":        (35.7647,  140.3864,  "RJTT"),
}

CITY_NAMES: dict[str, str] = {
    "nyc": "New York City", "chicago": "Chicago", "miami": "Miami",
    "dallas": "Dallas", "seattle": "Seattle", "atlanta": "Atlanta",
    "london": "London", "tokyo": "Tokyo",
}

UNITS: dict[str, str] = {
    "nyc": "F", "chicago": "F", "miami": "F", "dallas": "F",
    "seattle": "F", "atlanta": "F", "london": "C", "tokyo": "C",
}

TIMEZONES: dict[str, str] = {
    "nyc": "America/New_York", "chicago": "America/Chicago",
    "miami": "America/New_York", "dallas": "America/Chicago",
    "seattle": "America/Los_Angeles", "atlanta": "America/New_York",
    "london": "Europe/London", "tokyo": "Asia/Tokyo",
}


def fetch_daily_max(lat: float, lon: float, start: str, end: str, unit: str) -> list[float | None]:
    """Fetch 90 days of daily max temps from Open-Meteo (free, no auth)."""
    temp_unit = "fahrenheit" if unit == "F" else "celsius"
    url = (
        f"https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={lat}&longitude={lon}"
        f"&start_date={start}&end_date={end}"
        f"&daily=temperature_2m_max&temperature_unit={temp_unit}"
        f"&timezone=UTC"
    )
    for attempt in range(3):
        try:
            resp = requests.get(url, timeout=(5, 15))
            resp.raise_for_status()
            data = resp.json()
            return data.get("daily", {}).get("temperature_2m_max", [])
        except Exception as exc:
            if attempt < 2:
                time.sleep(3 * (attempt + 1))
            else:
                print(f"  ERROR fetching {lat},{lon}: {exc}", file=sys.stderr)
    return []


def analyse_city(city: str, days: int = 90) -> dict:
    """Run the offset analysis for one city."""
    end_dt = date.today() - timedelta(days=2)   # leave 2 days for data lag
    start_dt = end_dt - timedelta(days=days - 1)
    start_str = start_dt.isoformat()
    end_str = end_dt.isoformat()

    unit = UNITS[city]
    city_lat, city_lon = CITY_CENTERS[city]
    apt_lat, apt_lon, icao = AIRPORTS[city]

    print(f"  Fetching {CITY_NAMES[city]} ({days} days)...", end=" ", flush=True)

    city_temps = fetch_daily_max(city_lat, city_lon, start_str, end_str, unit)
    time.sleep(0.5)   # be polite to free API
    apt_temps = fetch_daily_max(apt_lat, apt_lon, start_str, end_str, unit)

    paired = [
        (c, a) for c, a in zip(city_temps, apt_temps)
        if c is not None and a is not None
    ]

    if len(paired) < 30:
        print(f"insufficient data ({len(paired)} days)")
        return {"city": city, "error": "insufficient_data"}

    deltas = [a - c for c, a in paired]   # positive = airport warmer
    n = len(deltas)
    mean_delta = sum(deltas) / n
    variance = sum((d - mean_delta) ** 2 for d in deltas) / n
    std_delta = variance ** 0.5

    bucket_size = 1.0   # 1°F or 1°C
    crossing_days = sum(1 for d in deltas if abs(d) >= bucket_size)
    crossing_pct = crossing_days / n * 100

    # Seasonal split (roughly: summer = months 5-9 in NH)
    summer_deltas = deltas[: n // 2]   # simplified — first half of window
    winter_deltas = deltas[n // 2:]

    result = {
        "city":             city,
        "city_name":        CITY_NAMES[city],
        "icao":             icao,
        "unit":             unit,
        "n_days":           n,
        "mean_delta":       round(mean_delta, 3),
        "std_delta":        round(std_delta, 3),
        "crossing_pct":     round(crossing_pct, 1),
        "min_delta":        round(min(deltas), 2),
        "max_delta":        round(max(deltas), 2),
        "summer_mean":      round(sum(summer_deltas) / len(summer_deltas), 3) if summer_deltas else None,
        "winter_mean":      round(sum(winter_deltas) / len(winter_deltas), 3) if winter_deltas else None,
    }

    verdict = (
        "STRONG EDGE" if abs(mean_delta) >= 1.0 and crossing_pct >= 20
        else "MODERATE EDGE" if abs(mean_delta) >= 0.5 or crossing_pct >= 15
        else "WEAK EDGE"
    )
    result["verdict"] = verdict

    print(
        f"delta={mean_delta:+.2f}°{unit} ±{std_delta:.2f} | "
        f"bucket-crossing {crossing_pct:.0f}% | {verdict}"
    )
    return result


def run() -> None:
    print("\n=== Airport vs City-Centre Temperature Offset Analysis ===")
    print("Fetching 90 days of historical data from Open-Meteo (free)...\n")

    results = []
    for city in CITY_CENTERS:
        result = analyse_city(city, days=90)
        results.append(result)
        time.sleep(0.3)

    # Save JSON
    out_dir = Path("research/data")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "airport_offset.json"
    out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    # Print summary table
    print(f"\n{'='*70}")
    print(f"  {'City':<16} {'ICAO':<6} {'Mean Δ':>8} {'StdDev':>8} {'Crossing%':>10}  Verdict")
    print(f"  {'-'*64}")
    for r in results:
        if "error" in r:
            print(f"  {r['city_name']:<16} {'ERR':<6}")
            continue
        print(
            f"  {r['city_name']:<16} {r['icao']:<6} "
            f"{r['mean_delta']:>+7.2f}° {r['std_delta']:>8.2f} "
            f"{r['crossing_pct']:>9.0f}%  {r['verdict']}"
        )
    print(f"{'='*70}")
    print(f"\nFull results saved to {out_path}")
    print("\nNEXT STEP:")
    print("  Mean Δ ≠ 0 AND crossing% ≥ 20% in ≥ 3 cities → proceed to Phase 1 (paper trading)")
    print("  Otherwise → revisit thesis before committing capital\n")


if __name__ == "__main__":
    run()
