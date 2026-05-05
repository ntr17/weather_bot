import sqlite3, json
conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row
mkts = conn.execute("SELECT json_data FROM markets").fetchall()

stop_losses = 0; stop_pnl = 0
trailing = 0; trailing_pnl = 0
take_profit = 0; tp_pnl = 0
resolved = 0; resolved_pnl = 0
total_no_closed = 0; total_yes_closed = 0

for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos = m.get("position")
    if pos and not positions:
        positions = {pos.get("market_id", "legacy"): pos}
    for mid, p in positions.items():
        if p.get("status") != "open" and p.get("status") is not None:
            reason = p.get("close_reason", "")
            pnl = p.get("pnl", 0) or 0
            if p.get("side") == "no":
                total_no_closed += 1
            else:
                total_yes_closed += 1
            if "stop_loss" in reason:
                stop_losses += 1
                stop_pnl += pnl
            elif "trailing" in reason:
                trailing += 1
                trailing_pnl += pnl
            elif "take_profit" in reason:
                take_profit += 1
                tp_pnl += pnl
            elif "resolved" in reason:
                resolved += 1
                resolved_pnl += pnl

print(f"Closed YES: {total_yes_closed}  Closed NO: {total_no_closed}")
print(f"Stop-losses:  {stop_losses:3d}  PnL: {stop_pnl:+8.2f}")
print(f"Trailing:     {trailing:3d}  PnL: {trailing_pnl:+8.2f}")
print(f"Take-profit:  {take_profit:3d}  PnL: {tp_pnl:+8.2f}")
print(f"Resolved:     {resolved:3d}  PnL: {resolved_pnl:+8.2f}")
total = stop_losses + trailing + take_profit + resolved
total_pnl = stop_pnl + trailing_pnl + tp_pnl + resolved_pnl
print(f"TOTAL closed: {total}  PnL: {total_pnl:+8.2f}")
print()

# The REAL damage — balance reconciliation
# Start: $1000
# Closed position costs returned: sum of (cost + pnl) for each closed
returned = 0
for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos = m.get("position")
    if pos and not positions:
        positions = {pos.get("market_id", "legacy"): pos}
    for mid, p in positions.items():
        if p.get("status") != "open" and p.get("status") is not None:
            returned += (p.get("cost", 0) or 0) + (p.get("pnl", 0) or 0)

open_cost = 0
for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos = m.get("position")
    if pos and not positions:
        positions = {pos.get("market_id", "legacy"): pos}
    for mid, p in positions.items():
        if p.get("status") == "open":
            open_cost += p.get("cost", 0) or 0

print("BALANCE RECONCILIATION:")
print(f"  Starting balance: $1,000.00")
print(f"  Current balance:  $559.11")
print(f"  Open positions:   ${open_cost:.2f}")
print(f"  Returned from closed: ${returned:.2f}")
print(f"  Accounted: ${559.11 + open_cost:.2f} + closed returned")
print(f"  Total PnL from closed: ${total_pnl:.2f}")
print(f"  Missing = 1000 - balance - open = ${1000 - 559.11 - open_cost:.2f}")
print()

# The KEY question: are stop-losses on NO positions killing us?
print("STOP-LOSS ANALYSIS ON NO POSITIONS:")
no_sl_count = 0
no_sl_pnl = 0
no_sl_entries = []
for row in mkts:
    m = json.loads(row["json_data"])
    positions = m.get("positions", {})
    pos = m.get("position")
    if pos and not positions:
        positions = {pos.get("market_id", "legacy"): pos}
    for mid, p in positions.items():
        if (p.get("side") == "no" and p.get("close_reason") == "stop_loss" 
            and p.get("status") != "open"):
            no_sl_count += 1
            pnl = p.get("pnl", 0) or 0
            no_sl_pnl += pnl
            entry = p.get("entry_price", 0)
            exit_p = p.get("exit_price", 0)
            cost = p.get("cost", 0)
            no_sl_entries.append((entry, exit_p, cost, pnl, m.get("city_name")))

print(f"  NO stop-losses: {no_sl_count}")
print(f"  Total NO SL PnL: ${no_sl_pnl:.2f}")
print(f"  Avg loss per NO SL: ${no_sl_pnl/no_sl_count:.2f}" if no_sl_count else "")
print()
print(f"  Entry prices of stopped-out NOs:")
for entry, exit_p, cost, pnl, city in sorted(no_sl_entries, key=lambda x: x[3]):
    pct_drop = (exit_p - entry) / entry * 100 if entry else 0
    print(f"    {city:16s} entry=${entry:.3f} exit=${exit_p:.3f} ({pct_drop:+.1f}%) "
          f"cost=${cost:.2f} pnl={pnl:+.2f}")

conn.close()
