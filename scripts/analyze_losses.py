"""Analyze recent major losses — find what opened $0.001 positions."""
from core.storage import load_trades

trades = load_trades()

print("=== WORST LOSSES ===")
for t in sorted(trades, key=lambda x: x.get("pnl", 0))[:15]:
    city = t.get("city", "?")
    date = t.get("date", "?")
    side = t.get("side", "?")
    entry = t.get("entry_price", 0)
    pnl = t.get("pnl", 0)
    reason = t.get("reason", "?")
    print(f"{city:15s} {date} {side:3s} entry=${entry:.3f} pnl=${pnl:+.2f} reason={reason}")

print("\n=== LONGSHOT YES (<0.05) ===")
yes_longshots = [t for t in trades if t.get("side") == "yes" and t.get("entry_price", 1) < 0.05]
print(f"Found {len(yes_longshots)} YES longshots")
for t in yes_longshots[-10:]:
    city = t.get("city", "?")
    date = t.get("date", "?")
    entry = t.get("entry_price", 0)
    pnl = t.get("pnl", 0)
    reason = t.get("reason", "?")
    print(f"  {city:15s} {date} entry=${entry:.4f} pnl=${pnl:+.2f}")

print("\n=== IMPOSSIBLE NO (<0.001) ===")
no_impossible = [t for t in trades if t.get("side") == "no" and t.get("entry_price", 1) < 0.002]
print(f"Found {len(no_impossible)} impossible NOs")
for t in no_impossible[-10:]:
    city = t.get("city", "?")
    date = t.get("date", "?")
    entry = t.get("entry_price", 0)
    pnl = t.get("pnl", 0)
    print(f"  {city:15s} {date} entry=${entry:.4f} pnl=${pnl:+.2f}")

print("\n=== SUMMARY ===")
print(f"Total trades: {len(trades)}")
print(f"Wins: {sum(1 for t in trades if t.get('pnl', 0) > 0)}")
print(f"Losses: {sum(1 for t in trades if t.get('pnl', 0) < 0)}")
total_pnl = sum(t.get("pnl", 0) for t in trades)
print(f"Total PnL: ${total_pnl:.2f}")
