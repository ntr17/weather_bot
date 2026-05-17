"""Quick V3 strategy analysis — May 6+ trades only."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.storage import load_all_markets

markets = load_all_markets()
all_pos = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        p["city"] = m.get("city_name", m.get("city", "?"))
        p["date"] = m.get("date", "")
        p["horizon"] = m.get("current_horizon", "?")
        all_pos.append(p)

closed = [p for p in all_pos if p.get("status") == "closed"]
opened = [p for p in all_pos if p.get("status") == "open"]

# V3 = after May 6
v3_closed = [p for p in closed if p.get("opened_at", "") >= "2026-05-06"]
v3_no = [p for p in v3_closed if p.get("side") == "no"]
v3_yes = [p for p in v3_closed if p.get("side") == "yes"]

print(f"Total positions in DB: {len(all_pos)}")
print(f"  Open:   {len(opened)}")
print(f"  Closed: {len(closed)}")
print()
print("=== V3 period (May 6+) closed trades ===")
print(f"  Total: {len(v3_closed)}")
print(f"  NO trades: {len(v3_no)}")
print(f"  YES trades: {len(v3_yes)}")
print()

if v3_no:
    wins = [p for p in v3_no if (p.get("pnl") or 0) > 0]
    losses = [p for p in v3_no if (p.get("pnl") or 0) < 0]
    flat = [p for p in v3_no if (p.get("pnl") or 0) == 0]
    total_pnl = sum(p.get("pnl", 0) or 0 for p in v3_no)
    total_cost = sum(p.get("cost", 0) or 0 for p in v3_no)
    print(f"  V3 NO: {len(wins)}W / {len(losses)}L / {len(flat)}flat")
    print(f"  Win rate: {len(wins)/len(v3_no)*100:.1f}%")
    print(f"  Total PnL: ${total_pnl:.2f}")
    print(f"  Total cost: ${total_cost:.2f}")
    if total_cost:
        print(f"  ROI: {total_pnl/total_cost*100:.1f}%")
    print()

    # By close reason
    reasons = {}
    for p in v3_no:
        r = p.get("close_reason", "?")
        reasons.setdefault(r, []).append(p)
    print("  By close reason:")
    for r, ps in sorted(reasons.items()):
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        print(f"    {r:20s}: {len(ps):3d} trades, {w}W, PnL ${pnl:+.2f}")
    print()

    # By horizon
    horizons = {}
    for p in v3_no:
        h = p.get("horizon", "?")
        horizons.setdefault(h, []).append(p)
    print("  By horizon:")
    for h, ps in sorted(horizons.items()):
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        wr = w / len(ps) * 100 if ps else 0
        print(f"    {h:5s}: {len(ps):3d} trades, {w}W/{len(ps)-w}L = {wr:.0f}% WR, PnL ${pnl:+.2f}")

    # D+0 vs D+1 vs D+2 split
    print()
    print("  === CRITICAL: D+0 trades (supposed to be DISABLED in V3) ===")
    d0 = [p for p in v3_no if p.get("horizon") == "D+0"]
    d1 = [p for p in v3_no if p.get("horizon") == "D+1"]
    d2 = [p for p in v3_no if p.get("horizon") == "D+2"]
    for label, subset in [("D+0", d0), ("D+1", d1), ("D+2", d2)]:
        if subset:
            w = sum(1 for p in subset if (p.get("pnl", 0) or 0) > 0)
            l = sum(1 for p in subset if (p.get("pnl", 0) or 0) < 0)
            pnl = sum(p.get("pnl", 0) or 0 for p in subset)
            cost = sum(p.get("cost", 0) or 0 for p in subset)
            roi = pnl/cost*100 if cost else 0
            print(f"    {label}: {len(subset)} trades, {w}W/{l}L = {w/(w+l)*100:.0f}% WR, PnL ${pnl:+.2f}, ROI {roi:+.1f}%")

if v3_yes:
    print()
    wins_y = [p for p in v3_yes if (p.get("pnl") or 0) > 0]
    losses_y = [p for p in v3_yes if (p.get("pnl") or 0) < 0]
    total_pnl_y = sum(p.get("pnl", 0) or 0 for p in v3_yes)
    total_cost_y = sum(p.get("cost", 0) or 0 for p in v3_yes)
    print(f"  V3 YES: {len(wins_y)}W / {len(losses_y)}L, PnL ${total_pnl_y:.2f}")
    if total_cost_y:
        print(f"  YES ROI: {total_pnl_y/total_cost_y*100:.1f}%")

# Check config state
print()
print("=== CONFIG CHECK ===")
import json
cfg = json.loads(open("config.json").read())
print(f"  enable_yes_trading: {cfg.get('enable_yes_trading')}")
print(f"  min_horizon_days: {cfg.get('min_horizon_days')}")
print(f"  max_horizon_days: {cfg.get('max_horizon_days')}")
print(f"  no_stop_enabled: {cfg.get('no_stop_enabled')}")
print(f"  no_forecast_exit: {cfg.get('no_forecast_exit')}")
print(f"  balance: {cfg.get('balance')}")
print(f"  max_bet: {cfg.get('max_bet')}")
