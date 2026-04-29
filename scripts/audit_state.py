"""Quick audit of bot state for strategy assessment."""
from core.storage import load_all_markets, load_calibration, load_state

mkts = load_all_markets()
state = load_state(1000)
cal = load_calibration()

open_pos = [m for m in mkts if m.get("position") and m["position"].get("status") == "open"]
closed_pos = [m for m in mkts if m.get("position") and m["position"].get("status") == "closed"]
resolved = [m for m in mkts if m.get("status") == "resolved"]
no_pos = [m for m in mkts if not m.get("position")]

print("=== STATE ===")
print(f"Balance: ${state['balance']:,.2f} (started ${state['starting_balance']:,.2f})")
print(f"Total trades: {state['total_trades']}")
print(f"Wins: {state['wins']} | Losses: {state['losses']}")
print(f"Total markets tracked: {len(mkts)}")
print(f"  Open positions: {len(open_pos)}")
print(f"  Closed positions (not resolved): {len(closed_pos)}")
print(f"  Resolved: {len(resolved)}")
print(f"  No position taken: {len(no_pos)}")
print(f"Calibration keys: {len(cal)}")
print()

# Capital deployed
total_deployed = sum(p["position"]["cost"] for p in open_pos)
print(f"Capital deployed in open positions: ${total_deployed:.2f}")
print(f"Capital available: ${state['balance']:,.2f}")
print(f"Total accounted: ${state['balance'] + total_deployed:.2f}")
print()

print("=== OPEN POSITIONS ===")
for m in open_pos:
    p = m["position"]
    side = p["side"].upper()
    print(f"  {m['city_name']:<18} {m['date']} | {side} | "
          f"entry=${p['entry_price']:.3f} | cost=${p['cost']:.2f} | "
          f"EV={p['ev']:+.3f} | {p['forecast_source']} | sigma={p['sigma']}")

print()
print("=== CLOSED POSITIONS (with P&L) ===")
all_closed = closed_pos + [m for m in resolved if m.get("position")]
total_pnl = 0
wins = losses = 0
for m in all_closed:
    p = m["position"]
    side = p["side"].upper()
    pnl = p.get("pnl")
    reason = p.get("close_reason", "?")
    exit_p = p.get("exit_price", "?")
    actual = m.get("actual_temp", "")
    actual_str = f" actual={actual}" if actual else ""
    pnl_str = f"${pnl:+.2f}" if pnl is not None else "N/A"
    if pnl is not None:
        total_pnl += pnl
        if pnl > 0:
            wins += 1
        else:
            losses += 1
    print(f"  {m['city_name']:<18} {m['date']} | {side} | "
          f"entry=${p['entry_price']:.3f} | exit={exit_p} | "
          f"pnl={pnl_str} | {reason}{actual_str}")

print()
print(f"=== P&L SUMMARY ===")
print(f"Realized P&L: ${total_pnl:+.2f}")
print(f"Wins: {wins} | Losses: {losses}")
if wins + losses > 0:
    print(f"Win rate: {wins/(wins+losses):.0%}")
print()

# Calibration data
if cal:
    print("=== CALIBRATION ===")
    for key, val in sorted(cal.items()):
        print(f"  {key}: sigma={val.get('sigma', '?'):.2f} (n={val.get('n', '?')})")
else:
    print("=== CALIBRATION: NONE (using defaults) ===")
    print("  Need 30+ resolved trades to calibrate. Currently at 0.")

# What fraction of scanned markets had tradeable opportunities?
print()
print("=== OPPORTUNITY RATE ===")
traded = len([m for m in mkts if m.get("position")])
print(f"Markets scanned: {len(mkts)}")
print(f"Positions taken: {traded}")
print(f"Hit rate: {traded/len(mkts):.0%}" if mkts else "N/A")
