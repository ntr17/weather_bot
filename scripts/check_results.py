"""Quick results analysis — run after pulling latest DB from Actions."""
import sqlite3
import json
from collections import defaultdict

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row

# State
r = conn.execute("SELECT json_data FROM state WHERE id=1").fetchone()
st = json.loads(r["json_data"])
print("=" * 60)
print("  STATE")
print("=" * 60)
for k, v in st.items():
    print(f"  {k}: {v}")

# All trades
rows = conn.execute("SELECT * FROM trades ORDER BY ts").fetchall()
print(f"\n{'=' * 60}")
print(f"  TRADES: {len(rows)} total")
print(f"{'=' * 60}")

by_side_outcome = defaultdict(lambda: {"count": 0, "pnl": 0.0, "cost": 0.0})
by_city = defaultdict(lambda: {"count": 0, "pnl": 0.0, "wins": 0})
by_reason = defaultdict(int)

for r in rows:
    key = f"{r['side']}_{r['outcome']}"
    by_side_outcome[key]["count"] += 1
    by_side_outcome[key]["pnl"] += r["pnl"] or 0
    by_side_outcome[key]["cost"] += r["cost"] or 0
    
    city = r["city_name"] or r["city"]
    by_city[city]["count"] += 1
    by_city[city]["pnl"] += r["pnl"] or 0
    if r["outcome"] == "win":
        by_city[city]["wins"] += 1
    
    by_reason[r["reason"] or "unknown"] += 1

print("\n  By side/outcome:")
for key, data in sorted(by_side_outcome.items()):
    print(f"    {key:20s} count={data['count']:4d}  pnl={data['pnl']:+8.2f}  cost={data['cost']:8.2f}")

total_pnl = sum(d["pnl"] for d in by_side_outcome.values())
total_cost = sum(d["cost"] for d in by_side_outcome.values())
print(f"    {'TOTAL':20s} count={len(rows):4d}  pnl={total_pnl:+8.2f}  cost={total_cost:8.2f}")

print("\n  By close reason:")
for reason, count in sorted(by_reason.items(), key=lambda x: -x[1]):
    print(f"    {reason:20s} {count}")

print("\n  By city:")
for city, data in sorted(by_city.items(), key=lambda x: x[1]["pnl"]):
    wr = f"{data['wins']}/{data['count']}" if data["count"] else "—"
    print(f"    {city:18s} trades={data['count']:3d}  pnl={data['pnl']:+8.2f}  WR={wr}")

# Open positions
print(f"\n{'=' * 60}")
print(f"  OPEN POSITIONS")
print(f"{'=' * 60}")
mkts = conn.execute("SELECT json_data FROM markets").fetchall()
open_cost = 0.0
for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    if not positions:
        # Legacy single position
        pos = m.get("position")
        if pos and pos.get("status") == "open":
            positions = {pos["market_id"]: pos}
    for mid, pos in positions.items():
        if pos.get("status") == "open":
            cost = pos.get("cost", 0)
            open_cost += cost
            unit = m.get("unit", "F")
            bucket = f"{pos.get('bucket_low', 0):.0f}-{pos.get('bucket_high', 0):.0f}°{unit}"
            print(f"    {m.get('city_name', '?'):18s} {m.get('date', '?')} {pos.get('side', '?'):3s} "
                  f"{bucket:14s} entry=${pos.get('entry_price', 0):.3f} cost=${cost:.2f} "
                  f"src={pos.get('forecast_source', '?')}")

print(f"\n  Total deployed: ${open_cost:.2f}")
print(f"  Balance: ${st['balance']:.2f}")
print(f"  Deployed + Balance = ${open_cost + st['balance']:.2f}")

# Recent trade details
print(f"\n{'=' * 60}")
print(f"  LAST 20 TRADES (detail)")
print(f"{'=' * 60}")
for r in rows[-20:]:
    print(f"    {r['ts'][:16]} {r['city_name'] or '?':14s} {r['date'] or '?'} "
          f"{r['side']:3s} {r['bucket_low']:.0f}-{r['bucket_high']:.0f} "
          f"entry=${r['entry_price']:.3f} exit=${r['exit_price']:.3f} "
          f"pnl={r['pnl']:+.2f} {r['outcome'] or '?'} [{r['reason'] or '?'}]")

# Run log — how many runs
run_count = conn.execute("SELECT COUNT(*) FROM run_log").fetchone()[0]
recent_runs = conn.execute("SELECT * FROM run_log ORDER BY ts DESC LIMIT 10").fetchall()
print(f"\n{'=' * 60}")
print(f"  RUN LOG: {run_count} total runs")
print(f"{'=' * 60}")
for r in recent_runs:
    print(f"    {r['ts'][:16]} {r['city'] or '?':14s} {r['status']:8s} "
          f"new={r['new_pos'] or 0} closed={r['closed'] or 0} "
          f"resolved={r['resolved'] or 0} {r['duration_s']:.1f}s")

conn.close()
