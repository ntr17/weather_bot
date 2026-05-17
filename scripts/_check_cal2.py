"""Check why live calibration never ran."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.storage import load_all_markets

markets = load_all_markets()
resolved = [m for m in markets if m.get("status") == "resolved"]
print(f"Total resolved markets: {len(resolved)}")

# Check how many have actual_temp
with_actual = [m for m in resolved if m.get("actual_temp") is not None]
print(f"Resolved with actual_temp: {len(with_actual)}")
print(f"Resolved WITHOUT actual_temp: {len(resolved) - len(with_actual)}")

# Check forecast sources in snapshots
from collections import Counter
sources = Counter()
for m in with_actual:
    for snap in m.get("forecast_snapshots", []):
        src = snap.get("best_source", "none")
        sources[src] += 1
print(f"\nForecast sources in snapshots (resolved markets with actual temp):")
for src, cnt in sources.most_common():
    print(f"  {src}: {cnt}")

# Check per-city resolved counts
from collections import defaultdict
city_resolved = defaultdict(int)
for m in with_actual:
    city_resolved[m.get("city", "?")] += 1
print(f"\nResolved markets per city (with actual_temp):")
for city in sorted(city_resolved.keys()):
    status = "OK (>=30)" if city_resolved[city] >= 30 else "BELOW 30"
    print(f"  {city:20s}: {city_resolved[city]:3d} - {status}")

# Check how many have ecmwf/gfs-specific snapshots
ecmwf_match = 0
ensemble_match = 0
for m in with_actual:
    has_ecmwf = any(s.get("best_source") == "ecmwf" for s in m.get("forecast_snapshots", []))
    has_ensemble = any(s.get("best_source") == "ensemble" for s in m.get("forecast_snapshots", []))
    if has_ecmwf: ecmwf_match += 1
    if has_ensemble: ensemble_match += 1
print(f"\nMarkets with at least one 'ecmwf' snapshot: {ecmwf_match}")
print(f"Markets with at least one 'ensemble' snapshot: {ensemble_match}")
