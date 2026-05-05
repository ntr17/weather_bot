"""One-time state reset: set starting_balance=$5000 and recompute balance from positions."""
from core.storage import load_all_markets, load_state, save_state

mkts = load_all_markets()
state = load_state(5000)

# Compute from actual positions
open_cost = 0
closed_pnl = 0
total_opened = 0
wins = 0
losses = 0

for m in mkts:
    for pid, p in m.get("positions", {}).items():
        total_opened += 1
        if p.get("status") == "open":
            open_cost += p.get("cost", 0)
        else:
            pnl = p.get("pnl", 0)
            closed_pnl += pnl
            if pnl >= 0:
                wins += 1
            else:
                losses += 1

starting = 5000.0
balance = round(starting - open_cost + closed_pnl, 2)

print(f"Starting:     ${starting:.2f}")
print(f"Open cost:    ${open_cost:.2f}")
print(f"Closed PnL:   ${closed_pnl:.2f}")
print(f"New balance:  ${balance:.2f}")
print(f"Positions:    {total_opened} total ({total_opened - wins - losses} open, {wins + losses} closed)")
print(f"Win/Loss:     {wins}/{losses}")

state["balance"] = balance
state["starting_balance"] = starting
state["total_trades"] = total_opened
state["wins"] = wins
state["losses"] = losses
state["peak_balance"] = max(state.get("peak_balance", 0), balance)

save_state(state)
print(f"\nState reset to: {state}")
