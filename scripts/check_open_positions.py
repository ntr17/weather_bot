"""Check current open positions."""
import sqlite3

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Load all markets with positions
cur.execute("SELECT json_data FROM markets")
rows = cur.fetchall()

mkt = []
for row in rows:
    try:
        import json
        m = json.loads(row["json_data"])
        mkt.append(m)
    except:
        pass

print(f"=== Open Positions Across {len(mkt)} Markets ===\n")

total_open = 0
total_cost = 0

for m in mkt:
    city = m.get("city_name", "?")
    positions = m.get("positions", {})
    if not positions:
        continue
    
    open_count = sum(1 for p in positions.values() if p.get("status") == "open")
    if open_count == 0:
        continue
    
    total_open += open_count
    
    for pos_id, pos in positions.items():
        if pos.get("status") != "open":
            continue
        
        side = pos.get("side", "?")
        entry = pos.get("entry_price", 0)
        shares = pos.get("shares", 0)
        cost = pos.get("cost", 0)
        
        total_cost += cost
        
        print(f"{city:15s} {m['date']} {side:3s} "
              f"entry=${entry:.4f} shares={shares:7.0f} cost=${cost:.2f}")

print(f"\nTotal open positions: {total_open}")
print(f"Total deployed capital: ${total_cost:.2f}")

conn.close()
