"""One-time: reset state for v2 strategy launch.

Keeps all trade history (for comparison) but resets the balance
and win/loss counters so v2 starts clean at $5,000.
"""
import sqlite3
import json

DB = "data/weatherbot.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Load current state
cur.execute("SELECT json_data FROM state ORDER BY id DESC LIMIT 1")
row = cur.fetchone()
state = json.loads(row[0]) if row else {}

print("Before reset:")
print(f"  balance:          ${state.get('balance', 0):,.2f}")
print(f"  starting_balance: ${state.get('starting_balance', 0):,.2f}")
print(f"  total_trades:     {state.get('total_trades', 0)}")
print(f"  wins/losses:      {state.get('wins', 0)}/{state.get('losses', 0)}")

# Reset for v2
state["balance"] = 5000.0
state["starting_balance"] = 5000.0
state["total_trades"] = 0
state["wins"] = 0
state["losses"] = 0
state["peak_balance"] = 5000.0

cur.execute("INSERT OR REPLACE INTO state (id, json_data) VALUES (1, ?)",
            (json.dumps(state),))

# Close all existing open positions (legacy from v1)
cur.execute("SELECT rowid, json_data FROM markets")
closed_count = 0
for row in cur.fetchall():
    mkt = json.loads(row[1])
    positions = mkt.get("positions", {})
    changed = False
    for pos_id, pos in positions.items():
        if pos.get("status") == "open":
            pos["status"] = "closed"
            pos["close_reason"] = "v2_reset"
            pos["pnl"] = 0.0
            pos["exit_price"] = pos["entry_price"]
            changed = True
            closed_count += 1
    if changed:
        mkt["positions"] = positions
        cur.execute("UPDATE markets SET json_data = ? WHERE rowid = ?",
                    (json.dumps(mkt), row[0]))

conn.commit()
conn.close()

print(f"\nAfter reset:")
print(f"  balance:          $5,000.00")
print(f"  starting_balance: $5,000.00")
print(f"  counters:         0/0/0")
print(f"  closed {closed_count} legacy open positions")
print(f"\nv2 strategy ready to trade.")
