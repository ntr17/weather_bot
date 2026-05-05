"""Deep analysis of what went wrong."""
import sqlite3
import json

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row

mkts = conn.execute("SELECT json_data FROM markets").fetchall()

total_pos = 0
open_pos = 0
closed_pos = 0
total_open_cost = 0.0
total_closed_cost = 0.0
side_counts = {"yes_open": 0, "no_open": 0, "yes_closed": 0, "no_closed": 0}
multi_pos_markets = []

for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos_legacy = m.get("position")
    if pos_legacy and not positions:
        positions = {pos_legacy.get("market_id", "legacy"): pos_legacy}
    
    open_in_mkt = []
    for mid, p in positions.items():
        total_pos += 1
        status = p.get("status", "unknown")
        side = p.get("side", "yes")
        cost = p.get("cost", 0) or 0
        
        if status == "open":
            open_pos += 1
            total_open_cost += cost
            side_counts[f"{side}_open"] += 1
            open_in_mkt.append(p)
        else:
            closed_pos += 1
            total_closed_cost += cost
            side_counts[f"{side}_closed"] += 1
    
    if len(open_in_mkt) > 1:
        multi_pos_markets.append((m, open_in_mkt))

print("=" * 60)
print("  POSITION INVENTORY")
print("=" * 60)
print(f"  Total positions: {total_pos}")
print(f"  Open: {open_pos}  (YES: {side_counts['yes_open']}, NO: {side_counts['no_open']})")
print(f"  Closed: {closed_pos}  (YES: {side_counts['yes_closed']}, NO: {side_counts['no_closed']})")
print(f"  Open cost: ${total_open_cost:.2f}")
print(f"  Closed cost: ${total_closed_cost:.2f}")
print(f"  Balance: $559.11")
print(f"  Balance + open cost = ${559.11 + total_open_cost:.2f}")
print(f"  Missing from $1000: ${1000 - 559.11 - total_open_cost:.2f}")

if multi_pos_markets:
    print(f"\n  Markets with multiple open positions: {len(multi_pos_markets)}")
    for m, positions in multi_pos_markets:
        city = m.get("city_name", "?")
        date = m.get("date", "?")
        print(f"\n  {city} {date} ({len(positions)} open):")
        for p in positions:
            bucket = f"{p.get('bucket_low', 0):.0f}-{p.get('bucket_high', 0):.0f}"
            print(f"    {p['side']:3s} {bucket:10s} entry=${p['entry_price']:.3f} cost=${p['cost']:.2f}")

# Most importantly — show ALL open positions grouped by date
print(f"\n{'=' * 60}")
print(f"  ALL OPEN POSITIONS BY DATE")
print(f"{'=' * 60}")
by_date = {}
for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos_legacy = m.get("position")
    if pos_legacy and not positions:
        positions = {pos_legacy.get("market_id", "legacy"): pos_legacy}
    
    for mid, p in positions.items():
        if p.get("status") == "open":
            date = m.get("date", "?")
            by_date.setdefault(date, []).append((m, p))

for date in sorted(by_date.keys()):
    items = by_date[date]
    total = sum(p.get("cost", 0) for _, p in items)
    print(f"\n  {date} — {len(items)} positions, ${total:.2f} deployed")
    for m, p in items:
        city = m.get("city_name", "?")
        unit = m.get("unit", "F")
        blo = p.get("bucket_low", 0)
        bhi = p.get("bucket_high", 0)
        if blo == -999:
            bucket = f"<={bhi:.0f}°{unit}"
        elif bhi == 999:
            bucket = f">={blo:.0f}°{unit}"
        else:
            bucket = f"{blo:.0f}-{bhi:.0f}°{unit}"
        print(f"    {city:18s} {p['side']:3s} {bucket:12s} entry=${p['entry_price']:.3f} "
              f"cost=${p['cost']:.2f} src={p.get('forecast_source', '?')}")

# Check closed positions to understand PnL flow
print(f"\n{'=' * 60}")
print(f"  ALL CLOSED POSITIONS")
print(f"{'=' * 60}")
for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos_legacy = m.get("position")
    if pos_legacy and not positions:
        positions = {pos_legacy.get("market_id", "legacy"): pos_legacy}
    
    for mid, p in positions.items():
        if p.get("status") != "open" and p.get("status") is not None:
            city = m.get("city_name", "?")
            pnl = p.get("pnl", 0) or 0
            reason = p.get("close_reason", "?")
            print(f"  {city:18s} {m.get('date','?')} {p['side']:3s} "
                  f"entry=${p.get('entry_price', 0):.3f} exit=${p.get('exit_price', 0):.3f} "
                  f"cost=${p.get('cost', 0):.2f} pnl={pnl:+.2f} [{reason}]")

conn.close()
