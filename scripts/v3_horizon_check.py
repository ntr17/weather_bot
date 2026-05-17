"""Check D+0 leak — were positions really opened at D+0 or is the label stale?"""
import sys
from pathlib import Path
from datetime import datetime
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.storage import load_all_markets

markets = load_all_markets()
all_pos = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        if p.get("status") == "closed" and p.get("side") == "no" and p.get("opened_at", "") >= "2026-05-14":
            all_pos.append({
                "city": m.get("city_name", "?"),
                "date": m.get("date", ""),
                "horizon": m.get("current_horizon", "?"),
                "opened": p.get("opened_at", "")[:16],
                "entry": p.get("entry_price", 0),
                "pnl": p.get("pnl", 0),
                "reason": p.get("close_reason", "?"),
            })

print("NO trades opened May 14+ — checking REAL horizon at entry time:")
print(f"{'City':15s} {'MktDate':12s} {'Opened':18s} {'DaysAhead':>9s} {'Label':>6s} {'PnL':>7s} {'Reason':>14s}")
print("-" * 90)

d0_count = 0
d1_count = 0
d2plus_count = 0

for p in sorted(all_pos, key=lambda x: x["opened"])[:40]:
    try:
        mkt_dt = datetime.strptime(p["date"], "%Y-%m-%d")
        open_dt = datetime.fromisoformat(p["opened"])
        days = (mkt_dt.date() - open_dt.date()).days
    except:
        days = -1
    if days == 0:
        d0_count += 1
    elif days == 1:
        d1_count += 1
    else:
        d2plus_count += 1
    print(f"{p['city']:15s} {p['date']:12s} {p['opened']:18s} {days:>9d} {p['horizon']:>6s} {p['pnl']:>+7.2f} {p['reason']:>14s}")

print()
print(f"REAL horizon distribution (first 40 trades opened May 14+):")
print(f"  Actual D+0 (opened same day as market): {d0_count}")
print(f"  Actual D+1 (opened 1 day before):       {d1_count}")
print(f"  Actual D+2+ (opened 2+ days before):    {d2plus_count}")

# Now do full count
all_d0 = 0
all_d1 = 0
all_d2 = 0
for p in all_pos:
    try:
        mkt_dt = datetime.strptime(p["date"], "%Y-%m-%d")
        open_dt = datetime.fromisoformat(p["opened"])
        days = (mkt_dt.date() - open_dt.date()).days
    except:
        days = -1
    if days == 0:
        all_d0 += 1
    elif days == 1:
        all_d1 += 1
    else:
        all_d2 += 1

print()
print(f"ALL NO trades opened May 14+ by REAL horizon:")
print(f"  D+0: {all_d0}")
print(f"  D+1: {all_d1}")
print(f"  D+2+: {all_d2}")
print(f"  Total: {all_d0 + all_d1 + all_d2}")
