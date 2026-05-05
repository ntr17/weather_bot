"""One-time: widen stop_price on existing open NO positions from 0.80 to 0.30 ratio."""
from core.storage import load_all_markets, save_market

mkts = load_all_markets()
updated = 0
for m in mkts:
    changed = False
    positions = m.get("positions", {})
    for pid, p in positions.items():
        if p.get("status") == "open" and p.get("side") == "no":
            old_stop = p.get("stop_price", 0)
            new_stop = round(p["entry_price"] * 0.30, 4)
            if abs(old_stop - new_stop) > 0.001:
                p["stop_price"] = new_stop
                changed = True
                updated += 1
                print(f"  {m.get('city'):15s} entry={p['entry_price']:.3f} stop {old_stop:.3f} -> {new_stop:.3f}")
    if changed:
        save_market(m)

print(f"\nUpdated {updated} NO position stop prices")
