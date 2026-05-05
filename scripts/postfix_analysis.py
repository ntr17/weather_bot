"""Post-fix analysis: what happened in the 3 runs since the bugfix?"""
import sqlite3, json
from datetime import datetime

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row

# State
state = json.loads(conn.execute("SELECT json_data FROM state WHERE id=1").fetchone()["json_data"])
print(f"Balance: ${state['balance']:.2f}")
print(f"Total trades: {state['total_trades']}")
print(f"Wins: {state.get('wins',0)}, Losses: {state.get('losses',0)}")
print()

# Run log — how many runs since the fix?
runs = conn.execute(
    "SELECT ts, city, status, new_pos, closed, resolved, duration_s, error "
    "FROM run_log ORDER BY ts"
).fetchall()

# The fix was pushed around 06:00 UTC, so post-fix runs start after that
fix_time = "2026-04-30T07:00"
post_fix = [r for r in runs if r["ts"] >= fix_time]
pre_fix = [r for r in runs if r["ts"] < fix_time]

print(f"Pre-fix runs: {len(pre_fix)}")
print(f"Post-fix runs: {len(post_fix)}")
print()

# Post-fix summary
post_new = sum(r["new_pos"] or 0 for r in post_fix)
post_closed = sum(r["closed"] or 0 for r in post_fix)
post_resolved = sum(r["resolved"] or 0 for r in post_fix)
post_errors = sum(1 for r in post_fix if r["status"] != "ok")
print(f"Post-fix: {post_new} opened, {post_closed} closed, {post_resolved} resolved, {post_errors} errors")
print()

# All positions — current state
mkts = conn.execute("SELECT json_data FROM markets").fetchall()
total_open = 0
total_closed = 0
total_cost_open = 0
total_pnl_closed = 0
total_cost_closed = 0

no_positions = []
yes_positions = []
closed_positions = []

for row in mkts:
    m = json.loads(row["json_data"])
    for mid, p in m.get("positions", {}).items():
        if p["status"] == "open":
            total_open += 1
            total_cost_open += p.get("cost", 0) or 0
            entry = {"city": m["city_name"], "side": p["side"], "entry": p["entry_price"],
                     "cost": p["cost"], "bucket": f"{p['bucket_low']}-{p['bucket_high']}",
                     "date": m["date"], "horizon": m.get("current_horizon", "?")}
            if p["side"] == "no":
                no_positions.append(entry)
            else:
                yes_positions.append(entry)
        else:
            total_closed += 1
            pnl = p.get("pnl", 0) or 0
            total_pnl_closed += pnl
            total_cost_closed += p.get("cost", 0) or 0
            closed_positions.append({
                "city": m["city_name"], "side": p["side"],
                "entry": p["entry_price"], "exit": p.get("exit_price", 0),
                "cost": p["cost"], "pnl": pnl,
                "reason": p.get("close_reason", ""),
                "date": m["date"],
                "opened": (p.get("opened_at") or "")[:16],
                "closed": (p.get("closed_at") or "")[:16],
            })

print(f"POSITIONS SUMMARY:")
print(f"  Open: {total_open} (cost: ${total_cost_open:.2f})")
print(f"  Closed: {total_closed} (PnL: ${total_pnl_closed:.2f})")
print(f"  YES open: {len(yes_positions)}, NO open: {len(no_positions)}")
print()

print(f"BALANCE RECONCILIATION:")
print(f"  Balance: ${state['balance']:.2f}")
print(f"  Open cost: ${total_cost_open:.2f}")
print(f"  Closed PnL: ${total_pnl_closed:.2f}")
print(f"  Expected balance = 812.33 - open_cost + closed_pnl")
# We reset to 812.33 but then state got overwritten by Actions?
# Check what balance was before the 3 runs
start_bal = 812.33
expected = round(start_bal - total_cost_open + total_pnl_closed, 2)
print(f"  Expected (from $812.33): ${expected:.2f}")
print(f"  Actual: ${state['balance']:.2f}")
print(f"  GAP: ${state['balance'] - expected:.2f}")
print()

# Check: did Actions start from the corrected balance or the old one?
# The config.template.json sets the initial balance — check that
print("CONFIG TEMPLATE BALANCE:")
import os
if os.path.exists("config.template.json"):
    with open("config.template.json") as f:
        tmpl = json.load(f)
    print(f"  config.template.json balance: ${tmpl.get('balance', 'N/A')}")
print()

# Show the closed positions sorted by PnL
print("CLOSED POSITIONS (sorted by PnL):")
for p in sorted(closed_positions, key=lambda x: x["pnl"]):
    print(f"  {p['city']:16s} {p['date']} {p['side']:3s} "
          f"entry=${p['entry']:.3f} exit=${p['exit']:.3f} "
          f"cost=${p['cost']:6.2f} pnl={p['pnl']:+7.2f} [{p['reason']}] "
          f"opened={p['opened']} closed={p['closed']}")

# Check: is the balance ALSO being re-loaded from state that has the OLD
# corrupted balance? The fix_state.py set it to 812.33, but if Actions
# ran with `config.template.json` balance=10000, it would use the state 
# in the DB which we fixed...
# BUT WAIT: load_state() uses the DB state, not config balance, unless
# there's no state yet.
# Let's check: when did the balance first get modified by post-fix runs?

print()
print("OPEN YES POSITIONS:")
for p in sorted(yes_positions, key=lambda x: x["cost"], reverse=True):
    print(f"  {p['city']:16s} {p['date']} {p['horizon']} "
          f"bucket={p['bucket']} entry=${p['entry']:.3f} cost=${p['cost']:.2f}")

print()
print(f"OPEN NO POSITIONS ({len(no_positions)}):")
for p in sorted(no_positions, key=lambda x: x["cost"], reverse=True):
    print(f"  {p['city']:16s} {p['date']} {p['horizon']} "
          f"bucket={p['bucket']} entry=${p['entry']:.3f} cost=${p['cost']:.2f}")

conn.close()
