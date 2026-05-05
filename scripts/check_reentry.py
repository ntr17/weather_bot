"""Check if the same buckets are being bet on repeatedly."""
import sqlite3, json
from collections import Counter
conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row

# Look at run_log to see how many new positions per run
runs = conn.execute(
    "SELECT ts, city, new_pos, closed, resolved FROM run_log "
    "WHERE new_pos > 0 ORDER BY ts"
).fetchall()

print("HIGH VOLUME RUNS (new_pos > 2):")
for r in runs:
    if r["new_pos"] > 2:
        print(f"  {r['ts'][:16]} {r['city']:14s} new={r['new_pos']} "
              f"closed={r['closed'] or 0} resolved={r['resolved'] or 0}")

# Count total by city
by_city = Counter()
for r in runs:
    by_city[r["city"]] += r["new_pos"]

print("\nTOTAL POSITIONS OPENED BY CITY:")
for city, count in by_city.most_common():
    print(f"  {city:18s} {count:3d}")

# Check: each run opens new positions even though the same buckets are open
# This means the "clear closed positions" code is letting them re-enter
# Let's look at a specific city to see the pattern
target = "nyc"
nyc_runs = conn.execute(
    "SELECT ts, new_pos, closed, resolved FROM run_log "
    "WHERE city = ? ORDER BY ts", (target,)
).fetchall()
print(f"\nNYC RUN HISTORY:")
for r in nyc_runs:
    print(f"  {r['ts'][:16]} new={r['new_pos'] or 0} closed={r['closed'] or 0} "
          f"resolved={r['resolved'] or 0}")

# Check how many positions NYC has right now
for row in conn.execute("SELECT json_data FROM markets WHERE city = ?", (target,)).fetchall():
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    print(f"\n  NYC {m['date']}: {len(positions)} positions")
    for mid, p in positions.items():
        print(f"    {p['side']:3s} {p.get('bucket_low',0):.0f}-{p.get('bucket_high',0):.0f} "
              f"status={p['status']} cost=${p.get('cost',0):.2f}")

# THE BIG QUESTION: count total positions opened vs total in DB
total_opened = sum(r["new_pos"] for r in conn.execute(
    "SELECT new_pos FROM run_log WHERE new_pos > 0"
).fetchall())
print(f"\nSUMMARY:")
print(f"  Total positions opened (run_log): {total_opened}")
print(f"  Positions in DB: 56")
print(f"  Lost: {total_opened - 56}")
print(f"  Cost per lost position (avg): ${(total_opened - 56) * 20 / max(total_opened - 56, 1):.2f}")

# The issue is clear: positions are being OVERWRITTEN.
# When scan runs again for the same city/date, the new positions dict
# replaces the old one. If a position was closed and cleared, a new one
# can be opened on the same bucket_id. The balance keeps getting drained.

conn.close()
