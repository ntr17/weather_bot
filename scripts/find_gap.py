"""Find the $314 gap — where did the money go?"""
import sqlite3, json
conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row

# Full accounting of every position ever created
mkts = conn.execute("SELECT json_data FROM markets").fetchall()

all_costs_ever = 0  # total cost of all positions ever opened
all_returned = 0    # cost + pnl returned for closed positions
all_open_cost = 0   # cost still locked in open positions

overwritten_cost = 0  # positions that were cleared (position set to None/overwritten)

for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos = m.get("position")
    if pos and not positions:
        positions = {pos.get("market_id", "legacy"): pos}
    
    for mid, p in positions.items():
        cost = p.get("cost", 0) or 0
        pnl = p.get("pnl", 0) or 0
        status = p.get("status")
        
        all_costs_ever += cost
        if status == "open":
            all_open_cost += cost
        elif status == "closed":
            all_returned += cost + pnl

# Check state total_trades
state_row = conn.execute("SELECT json_data FROM state WHERE id=1").fetchone()
state = json.loads(state_row["json_data"])

print("FULL ACCOUNTING:")
print(f"  State total_trades: {state['total_trades']}")
print(f"  Positions found in DB: {sum(len(json.loads(r['json_data']).get('positions', {})) for r in mkts)}")
print(f"  Legacy positions: {sum(1 for r in mkts if json.loads(r['json_data']).get('position'))}")
print()
print(f"  All position costs in DB: ${all_costs_ever:.2f}")
print(f"  Open position costs:      ${all_open_cost:.2f}")
print(f"  Closed returned:          ${all_returned:.2f}")
print(f"  Sum (open + returned):    ${all_open_cost + all_returned:.2f}")
print()
print(f"  Balance: ${state['balance']:.2f}")
print(f"  Balance + open + (costs-returned for closed): ${state['balance'] + all_open_cost:.2f}")
print()

# The issue: state['total_trades'] = 380 but we only have 56 positions
# That means 380 - 56 = 324 positions were LOST (overwritten/cleared)
# Each one deducted from balance but never returned
lost_trades = state["total_trades"] - sum(
    len(json.loads(r["json_data"]).get("positions", {})) 
    for r in mkts
)
# Also count legacy position entries
for row in mkts:
    m = json.loads(row["json_data"])
    if m.get("position") and not m.get("positions"):
        lost_trades -= 1

print(f"DIAGNOSIS:")
print(f"  State says {state['total_trades']} trades opened")
print(f"  DB has 56 positions (47 closed + 9 open)")
print(f"  MISSING POSITIONS: {lost_trades}")
print(f"  These were opened (balance deducted) but their records were lost")
print()

# HOW were they lost? Check if the 'positions' dict cleanup code is the culprit
# In main.py we have:
#   positions = {k: v for k, v in positions.items() if v.get("status") == "open"}
#   mkt = {**mkt, "positions": positions}
# This CLEARS closed positions every scan cycle! When they close via stop_loss,
# the closed record stays for one cycle, then gets wiped.
# BUT close_position does save_market with the closed status.
# The issue is the NEXT scan cycle re-clears it.
# Let's verify: how many positions have status='closed' vs open?

closed_in_db = 0
open_in_db = 0
for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos = m.get("position")
    if pos and not positions:
        positions = {pos.get("market_id", "legacy"): pos}
    for mid, p in positions.items():
        if p.get("status") == "open":
            open_in_db += 1
        else:
            closed_in_db += 1

print(f"  Positions in DB with status=open: {open_in_db}")
print(f"  Positions in DB with status=closed: {closed_in_db}")
print(f"  Total: {open_in_db + closed_in_db}")
print()

# What about per-run new_pos counts from run_log?
runs = conn.execute("SELECT city, new_pos FROM run_log WHERE new_pos > 0").fetchall()
total_new = sum(r["new_pos"] for r in runs)
print(f"  Run log says {total_new} positions opened across {len(runs)} city-runs")
print(f"  But state says {state['total_trades']}")
print(f"  Difference: {state['total_trades'] - total_new}")

conn.close()
