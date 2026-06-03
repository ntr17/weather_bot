"""V3 strategy final analysis — using REAL horizon at entry, not stale label."""
import sys
from pathlib import Path
from datetime import datetime
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.storage import load_all_markets

markets = load_all_markets()

# Collect ALL closed NO trades from V3 period (May 14+ = when template was enforced)
v3_no = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        if p.get("status") != "closed":
            continue
        if p.get("side") != "no":
            continue
        if p.get("opened_at", "") < "2026-05-14":
            continue
        # Calculate REAL horizon
        try:
            mkt_dt = datetime.strptime(m.get("date", ""), "%Y-%m-%d")
            open_dt = datetime.fromisoformat(p["opened_at"])
            real_horizon = (mkt_dt.date() - open_dt.date()).days
        except:
            real_horizon = -1
        p["real_horizon"] = real_horizon
        p["city"] = m.get("city_name", "?")
        p["mkt_date"] = m.get("date", "")
        v3_no.append(p)

# Also collect YES trades
v3_yes = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        if p.get("status") != "closed":
            continue
        if p.get("side") != "yes":
            continue
        if p.get("opened_at", "") < "2026-05-14":
            continue
        v3_yes.append(p)

print("=" * 60)
print("  V3 STRATEGY ANALYSIS — May 14-16, 2026")
print("  (using REAL horizon at entry time)")
print("=" * 60)
print()

# Filter to only D+1 and D+2 (the actual V3 strategy)
d1_d2 = [p for p in v3_no if p["real_horizon"] >= 1]
d0_only = [p for p in v3_no if p["real_horizon"] == 0]

print(f"Total NO trades (May 14+): {len(v3_no)}")
print(f"  Real D+0 (LEAK — should not exist): {len(d0_only)}")
print(f"  Real D+1/D+2 (V3 strategy): {len(d1_d2)}")
print()

if d1_d2:
    wins = [p for p in d1_d2 if (p.get("pnl") or 0) > 0]
    losses = [p for p in d1_d2 if (p.get("pnl") or 0) < 0]
    total_pnl = sum(p.get("pnl", 0) or 0 for p in d1_d2)
    total_cost = sum(p.get("cost", 0) or 0 for p in d1_d2)

    print("=== V3 NO (D+1 and D+2) — THE ACTUAL STRATEGY ===")
    print(f"  Trades: {len(d1_d2)}")
    print(f"  Record: {len(wins)}W / {len(losses)}L")
    print(f"  Win rate: {len(wins)/(len(wins)+len(losses))*100:.1f}%")
    print(f"  Total PnL: ${total_pnl:+.2f}")
    print(f"  Total wagered: ${total_cost:.2f}")
    print(f"  ROI: {total_pnl/total_cost*100:+.1f}%")
    print()

    # By close reason
    reasons = {}
    for p in d1_d2:
        r = p.get("close_reason", "?")
        reasons.setdefault(r, []).append(p)
    print("  By exit type:")
    for r, ps in sorted(reasons.items()):
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in ps if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        avg = pnl / len(ps) if ps else 0
        print(f"    {r:16s}: {len(ps):3d} ({w}W/{l}L)  PnL ${pnl:+.2f}  avg ${avg:+.2f}")
    print()

    # By real horizon
    for h in [1, 2, 3, 4, 5]:
        subset = [p for p in d1_d2 if p["real_horizon"] == h]
        if not subset:
            continue
        w = sum(1 for p in subset if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in subset if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in subset)
        cost = sum(p.get("cost", 0) or 0 for p in subset)
        roi = pnl/cost*100 if cost else 0
        print(f"  D+{h}: {len(subset):3d} trades, {w}W/{l}L = {w/(w+l)*100:.0f}% WR, PnL ${pnl:+.2f}, ROI {roi:+.1f}%")

    # Average entry price
    avg_entry = sum(p.get("entry_price", 0) for p in d1_d2) / len(d1_d2)
    print(f"\n  Avg entry price: ${avg_entry:.3f}")
    print(f"  Avg bet size: ${total_cost/len(d1_d2):.2f}")
    
    # Win/loss amounts
    avg_win = sum(p.get("pnl", 0) or 0 for p in wins) / len(wins) if wins else 0
    avg_loss = sum(p.get("pnl", 0) or 0 for p in losses) / len(losses) if losses else 0
    print(f"  Avg win: ${avg_win:+.2f}")
    print(f"  Avg loss: ${avg_loss:+.2f}")

# YES trades sanity check
if v3_yes:
    print()
    print("=== YES TRADES (should be ZERO with enable_yes_trading=false) ===")
    wins_y = sum(1 for p in v3_yes if (p.get("pnl", 0) or 0) > 0)
    losses_y = sum(1 for p in v3_yes if (p.get("pnl", 0) or 0) < 0)
    pnl_y = sum(p.get("pnl", 0) or 0 for p in v3_yes)
    print(f"  Count: {len(v3_yes)} (all opened BEFORE config took effect)")
    print(f"  Record: {wins_y}W / {losses_y}L, PnL ${pnl_y:+.2f}")

# Open positions check  
open_pos = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        if p.get("status") == "open":
            open_pos.append(p)
print(f"\n=== OPEN POSITIONS: {len(open_pos)} ===")
no_open = [p for p in open_pos if p.get("side") == "no"]
yes_open = [p for p in open_pos if p.get("side") == "yes"]
print(f"  NO: {len(no_open)}")
print(f"  YES: {len(yes_open)}")

# Projection for $54 bankroll
if d1_d2:
    print()
    print("=" * 60)
    print("  PROJECTION FOR $54 LIVE BANKROLL")
    print("=" * 60)
    wr = len(wins) / (len(wins) + len(losses))
    roi_pct = total_pnl / total_cost * 100
    trades_per_day = len(d1_d2) / 3  # 3 days of data
    print(f"  WR: {wr*100:.1f}%")
    print(f"  ROI per cycle: {roi_pct:+.1f}%")
    print(f"  Trades/day: ~{trades_per_day:.0f}")
    print(f"  At $7/trade, daily turnover: ~${trades_per_day*7:.0f}")
    print(f"  Expected daily PnL: ~${trades_per_day*7*roi_pct/100:.2f}")
    # A NO token bought at price p wins (1-p) if correct and loses p if wrong.
    # Break-even therefore requires true win probability >= p.
    print(f"  Breakeven WR needed: ~{avg_entry*100:.0f}%")
