"""Full audit from SQLite for strategy assessment."""
import sqlite3
import json

db = sqlite3.connect("data/weatherbot.db")
db.row_factory = sqlite3.Row

# State
row = db.execute("SELECT * FROM state WHERE id=1").fetchone()
state = json.loads(row["json_data"])
print("=== STATE ===")
for k, v in state.items():
    print(f"  {k}: {v}")
print()

# All markets
rows = db.execute("SELECT city, date, status, json_data FROM markets").fetchall()
markets = []
for r in rows:
    m = json.loads(r["json_data"])
    m["_status_col"] = r["status"]
    markets.append(m)

with_pos = [m for m in markets if m.get("position")]
without_pos = [m for m in markets if not m.get("position")]

print(f"Total markets tracked: {len(markets)}")
print(f"  With position: {len(with_pos)}")
print(f"  Without position: {len(without_pos)}")
print()

# Positions by status
open_pos = [m for m in with_pos if m["position"].get("status") == "open"]
closed_pos = [m for m in with_pos if m["position"].get("status") == "closed"]
other_pos = [m for m in with_pos if m["position"].get("status") not in ("open", "closed")]

print(f"=== OPEN POSITIONS ({len(open_pos)}) ===")
total_deployed = 0
for m in open_pos:
    p = m["position"]
    cost = p.get("cost", 0)
    total_deployed += cost
    print(f"  {m.get('city_name','?'):<18} {m.get('date','?')} | "
          f"{p['side'].upper():>3} @ ${p['entry_price']:.3f} | "
          f"cost=${cost:.2f} | EV={p.get('ev',0):+.3f} | "
          f"sigma={p.get('sigma','?')} | {p.get('forecast_source','?')}")
print(f"  Total deployed: ${total_deployed:.2f}")
print()

print(f"=== CLOSED POSITIONS ({len(closed_pos)}) ===")
total_pnl = 0
wins = losses = breakeven = 0
for m in closed_pos:
    p = m["position"]
    pnl = p.get("pnl")
    reason = p.get("close_reason", "?")
    actual = m.get("actual_temp", "")
    if pnl is not None:
        total_pnl += pnl
        if pnl > 0: wins += 1
        elif pnl < 0: losses += 1
        else: breakeven += 1
    pnl_s = f"pnl=${pnl:+.2f}" if pnl is not None else "pnl=N/A"
    actual_s = f" actual={actual}" if actual else ""
    print(f"  {m.get('city_name','?'):<18} {m.get('date','?')} | "
          f"{p['side'].upper():>3} @ ${p['entry_price']:.3f} | "
          f"exit=${p.get('exit_price',0):.3f} | {pnl_s} | {reason}{actual_s}")
print(f"  Realized P&L: ${total_pnl:+.2f}")
print(f"  W/L/BE: {wins}/{losses}/{breakeven}")
print()

# Balance reconciliation
print("=== BALANCE CHECK ===")
print(f"  Starting: ${state['starting_balance']:.2f}")
print(f"  Current:  ${state['balance']:.2f}")
print(f"  Deployed: ${total_deployed:.2f}")
print(f"  Realized: ${total_pnl:+.2f}")
accounted = state["balance"] + total_deployed - total_pnl
print(f"  Balance + deployed - realized = ${accounted:.2f}")
gap = state["starting_balance"] - accounted
if abs(gap) > 0.01:
    print(f"  GAP: ${gap:.2f} unaccounted")
else:
    print(f"  OK: fully reconciled")
print()

# No-position markets status
print(f"=== MARKETS WITHOUT POSITION ({len(without_pos)}) ===")
statuses = {}
for m in without_pos:
    s = m.get("_status_col", "?")
    statuses[s] = statuses.get(s, 0) + 1
for s, c in sorted(statuses.items()):
    print(f"  {s}: {c}")
print()

# Calibration
cal_rows = db.execute("SELECT * FROM calibration").fetchall()
if cal_rows:
    print(f"=== CALIBRATION ({len(cal_rows)} keys) ===")
    for r in cal_rows:
        print(f"  {r['key']}: sigma={r['sigma']:.2f} n={r['n']}")
else:
    print("=== CALIBRATION: NONE ===")
    print("  Using defaults (2.0F / 1.2C). Need resolved trades to calibrate.")
print()

# Trades table (resolved)
trades = db.execute("SELECT * FROM trades ORDER BY ts").fetchall()
print(f"=== TRADES LOG ({len(trades)} entries) ===")
for t in trades:
    d = dict(t)
    print(f"  {d.get('city_name','?'):<18} {d.get('date','?')} | "
          f"{d.get('side','?'):>3} @ ${d.get('entry_price',0):.3f} | "
          f"pnl=${d.get('pnl',0):+.2f} | {d.get('reason','?')}")
print()

# Run log stats
runs = db.execute(
    "SELECT status, COUNT(*) as cnt FROM run_log GROUP BY status"
).fetchall()
print("=== RUN LOG ===")
for r in runs:
    print(f"  {r['status']}: {r['cnt']}")
total_runs = sum(r["cnt"] for r in runs)
print(f"  Total: {total_runs}")
print()

# Opportunity rate
print("=== SUMMARY FOR STRATEGY ASSESSMENT ===")
print(f"Markets scanned: {len(markets)}")
print(f"Positions taken: {len(with_pos)} ({len(with_pos)/len(markets)*100:.0f}%)")
print(f"Open: {len(open_pos)} | Closed: {len(closed_pos)}")
print(f"Win rate: {wins}/{wins+losses} = {wins/(wins+losses)*100:.0f}%" if wins+losses > 0 else "Win rate: N/A (no resolved)")
print(f"Deployed capital: ${total_deployed:.2f} / ${state['balance']:.2f} available")
avg_cost = total_deployed / len(open_pos) if open_pos else 0
print(f"Avg position size: ${avg_cost:.2f}")
