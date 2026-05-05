"""Deep diagnostic of current bot state — scans positions directly, not trades table."""
from core.storage import load_all_markets, load_state, load_trades

mkts = load_all_markets()
state = load_state(5000)  # Don't trigger top-up
trades = load_trades()

print("=== STATE ===")
for k, v in state.items():
    print(f"  {k}: {v}")

# Scan ALL positions from markets
open_yes = []
open_no = []
closed_yes = []
closed_no = []
for m in mkts:
    for pid, p in m.get("positions", {}).items():
        p_info = {**p, "_city": m.get("city"), "_date": m.get("date")}
        if p.get("status") == "open":
            (open_no if p.get("side") == "no" else open_yes).append(p_info)
        else:
            (closed_no if p.get("side") == "no" else closed_yes).append(p_info)

print(f"\n=== ALL POSITIONS (from markets) ===")
print(f"Open  YES: {len(open_yes)}, cost ${sum(p.get('cost',0) for p in open_yes):.2f}")
print(f"Open  NO:  {len(open_no)}, cost ${sum(p.get('cost',0) for p in open_no):.2f}")
print(f"Closed YES: {len(closed_yes)}, PnL ${sum(p.get('pnl',0) for p in closed_yes):.2f}")
print(f"Closed NO:  {len(closed_no)}, PnL ${sum(p.get('pnl',0) for p in closed_no):.2f}")
total_open = len(open_yes) + len(open_no)
total_closed = len(closed_yes) + len(closed_no)
total_positions = total_open + total_closed
open_cost = sum(p.get("cost", 0) for p in open_yes + open_no)
closed_pnl = sum(p.get("pnl", 0) for p in closed_yes + closed_no)
closed_cost = sum(p.get("cost", 0) for p in closed_yes + closed_no)
print(f"Total: {total_positions} positions ({total_open} open, {total_closed} closed)")
print(f"Trades table has: {len(trades)} records (vs {total_closed} closures)")

# Balance reconciliation
print(f"\n=== BALANCE RECONCILIATION ===")
all_costs = sum(p.get("cost", 0) for p in open_yes + open_no + closed_yes + closed_no)
all_returns = sum(p.get("cost", 0) + p.get("pnl", 0) for p in closed_yes + closed_no)
print(f"All costs ever:   ${all_costs:.2f}")
print(f"All returns:      ${all_returns:.2f}")
print(f"Open deployed:    ${open_cost:.2f}")
print(f"Net closed PnL:   ${closed_pnl:.2f}")
print(f"Implied balance (from $10k): ${10000 - open_cost + closed_pnl:.2f}")
print(f"Implied balance (from $5k):  ${5000 - open_cost + closed_pnl:.2f}")
print(f"Actual balance:   ${state['balance']:.2f}")

# Closed position details
print(f"\n=== CLOSED POSITIONS (from markets, all {total_closed}) ===")
for p in sorted(closed_yes + closed_no, key=lambda x: x.get("pnl", 0)):
    city = p.get("_city", "?")
    side = p.get("side", "?")
    entry = p.get("entry_price", 0)
    exit_p = p.get("exit_price", 0)
    cost = p.get("cost", 0)
    pnl = p.get("pnl", 0)
    reason = p.get("close_reason", "?")
    print(f"  {city:15s} {side:3s} entry=${entry:.3f} exit=${exit_p:.3f} cost=${cost:.2f} pnl=${pnl:+.2f} reason={reason}")

# Open position details — entry prices
print(f"\n=== OPEN YES POSITIONS ({len(open_yes)}) ===")
for p in sorted(open_yes, key=lambda x: x.get("cost", 0), reverse=True):
    city = p.get("_city", "?")
    entry = p.get("entry_price", 0)
    cost = p.get("cost", 0)
    print(f"  {city:15s} entry=${entry:.3f} cost=${cost:.2f}")

