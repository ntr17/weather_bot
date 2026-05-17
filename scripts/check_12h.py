"""Check what happened in the last 12 hours specifically."""
import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.storage import load_all_markets

markets = load_all_markets()
cutoff = (datetime.now(timezone.utc) - timedelta(hours=12)).isoformat()

# All trades closed in last 12 hours
recent = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        if p.get("status") != "closed":
            continue
        if (p.get("closed_at") or "") < cutoff:
            continue
        try:
            mkt_dt = datetime.strptime(m.get("date", ""), "%Y-%m-%d")
            open_dt = datetime.fromisoformat(p["opened_at"])
            real_horizon = (mkt_dt.date() - open_dt.date()).days
        except:
            real_horizon = -1
        p["real_horizon"] = real_horizon
        p["city"] = m.get("city_name", "?")
        p["mkt_date"] = m.get("date", "")
        recent.append(p)

print(f"Trades closed in last 12 hours: {len(recent)}")
print()

# Split by side
no_trades = [p for p in recent if p.get("side") == "no"]
yes_trades = [p for p in recent if p.get("side") == "yes"]

print(f"NO trades: {len(no_trades)}")
if no_trades:
    wins = [p for p in no_trades if (p.get("pnl") or 0) > 0]
    losses = [p for p in no_trades if (p.get("pnl") or 0) < 0]
    pnl = sum(p.get("pnl", 0) or 0 for p in no_trades)
    cost = sum(p.get("cost", 0) or 0 for p in no_trades)
    print(f"  Record: {len(wins)}W / {len(losses)}L = {len(wins)/(len(wins)+len(losses))*100:.1f}% WR")
    print(f"  PnL: ${pnl:+.2f}")
    print(f"  ROI: {pnl/cost*100:+.1f}%")
    
    # By reason
    reasons = {}
    for p in no_trades:
        r = p.get("close_reason", "?")
        reasons.setdefault(r, []).append(p)
    print()
    for r, ps in sorted(reasons.items()):
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in ps if (p.get("pnl", 0) or 0) < 0)
        pnl_r = sum(p.get("pnl", 0) or 0 for p in ps)
        print(f"  {r:18s}: {len(ps):3d} ({w}W/{l}L) PnL ${pnl_r:+.2f}")
    
    # By real horizon
    print()
    for h in [-1, 0, 1, 2, 3]:
        subset = [p for p in no_trades if p["real_horizon"] == h]
        if not subset:
            continue
        w = sum(1 for p in subset if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in subset if (p.get("pnl", 0) or 0) < 0)
        pnl_h = sum(p.get("pnl", 0) or 0 for p in subset)
        print(f"  D+{h}: {len(subset)} trades, {w}W/{l}L, PnL ${pnl_h:+.2f}")

    # Show the losses in detail
    if losses:
        print("\n  LOSSES:")
        for p in losses:
            print(f"    {p['city']:15s} {p['mkt_date']} D+{p['real_horizon']} "
                  f"entry ${p['entry_price']:.3f} → ${p.get('exit_price',0):.3f} "
                  f"PnL ${p.get('pnl',0):+.2f} ({p.get('close_reason','?')})")

if yes_trades:
    print(f"\nYES trades: {len(yes_trades)}")
    pnl_y = sum(p.get("pnl", 0) or 0 for p in yes_trades)
    print(f"  PnL: ${pnl_y:+.2f}")

# Check currently open positions
open_pos = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        if p.get("status") == "open":
            try:
                mkt_dt = datetime.strptime(m.get("date", ""), "%Y-%m-%d")
                open_dt = datetime.fromisoformat(p["opened_at"])
                real_horizon = (mkt_dt.date() - open_dt.date()).days
            except:
                real_horizon = -1
            p["real_horizon"] = real_horizon
            p["city"] = m.get("city_name", "?")
            p["mkt_date"] = m.get("date", "")
            open_pos.append(p)

print(f"\n=== OPEN POSITIONS: {len(open_pos)} ===")
no_open = [p for p in open_pos if p.get("side") == "no"]
yes_open = [p for p in open_pos if p.get("side") == "yes"]
print(f"  NO: {len(no_open)}, YES: {len(yes_open)}")

# Unrealized PnL
total_cost_open = sum(p.get("cost", 0) or 0 for p in open_pos)
print(f"  Capital deployed: ${total_cost_open:.2f}")

# Open by horizon
for h in [0, 1, 2]:
    subset = [p for p in no_open if p["real_horizon"] == h]
    if subset:
        cost = sum(p.get("cost", 0) or 0 for p in subset)
        print(f"  D+{h}: {len(subset)} positions, ${cost:.2f} deployed")
