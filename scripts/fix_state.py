"""
Reset state to correct the damage from the re-entry bug.

The bug caused ~319 phantom positions (opened, stopped out, record lost).
True losses from the 56 REAL positions: $60.96
Starting balance: $1000
Open position costs: $126.71

Corrected balance = 1000 - 126.71 (open) - 60.96 (real losses) = $812.33
"""
import sqlite3, json

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row

# Count real positions and losses
mkts = conn.execute("SELECT json_data FROM markets").fetchall()
total_real_positions = 0
real_pnl = 0
open_cost = 0

for row in mkts:
    m = json.loads(row["json_data"])
    for mid, p in m.get("positions", {}).items():
        total_real_positions += 1
        if p.get("status") == "open":
            open_cost += p.get("cost", 0) or 0
        else:
            real_pnl += p.get("pnl", 0) or 0

corrected_balance = round(1000 - open_cost + real_pnl, 2)

print(f"Real positions in DB: {total_real_positions}")
print(f"Open position costs: ${open_cost:.2f}")
print(f"Real closed PnL: ${real_pnl:.2f}")
print(f"Corrected balance: ${corrected_balance:.2f}")
print()

# Read current state
state_row = conn.execute("SELECT json_data FROM state WHERE id=1").fetchone()
state = json.loads(state_row["json_data"])
print(f"Current state: balance=${state['balance']:.2f}, total_trades={state['total_trades']}")
print(f"Correcting to: balance=${corrected_balance:.2f}, total_trades={total_real_positions}")

# Update
state["balance"] = corrected_balance
state["total_trades"] = total_real_positions
state["wins"] = 1  # Only Paris trailing stop was a win
state["losses"] = sum(
    1 for row in mkts
    for mid, p in json.loads(row["json_data"]).get("positions", {}).items()
    if p.get("status") != "open" and (p.get("pnl") or 0) < 0
)

conn.execute("UPDATE state SET json_data=? WHERE id=1", (json.dumps(state),))
conn.commit()
print(f"State updated. wins={state['wins']}, losses={state['losses']}")
conn.close()
