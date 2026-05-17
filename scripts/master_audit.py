"""Master audit script — deep-dive into the trade database for orchestrator analysis."""
import sys
import sqlite3
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

DB_PATH = ROOT / "data" / "weatherbot.db"

if not DB_PATH.exists():
    print(f"ERROR: Database not found at {DB_PATH}")
    sys.exit(1)

conn = sqlite3.connect(str(DB_PATH))
conn.row_factory = sqlite3.Row

print("=" * 70)
print("  MASTER AUDIT — WeatherBot Database Analysis")
print("=" * 70)

# ── 1. Database overview ─────────────────────────────────────────────────
print("\n## 1. DATABASE OVERVIEW")
for table in ['markets', 'trades', 'state', 'calibration', 'run_log']:
    cnt = conn.execute(f"SELECT COUNT(*) as c FROM {table}").fetchone()['c']
    print(f"  {table}: {cnt} rows")

# ── 2. ALL positions from markets (source of truth) ──────────────────────
print("\n## 2. ALL POSITIONS (from markets table)")
rows = conn.execute("SELECT json_data FROM markets").fetchall()
markets = [json.loads(r['json_data']) for r in rows]

all_positions = []
for m in markets:
    for pid, p in m.get("positions", {}).items():
        # Calculate REAL horizon
        try:
            mkt_dt = datetime.strptime(m.get("date", ""), "%Y-%m-%d")
            open_dt = datetime.fromisoformat(p["opened_at"])
            real_horizon = (mkt_dt.date() - open_dt.date()).days
        except:
            real_horizon = -1
        p["_real_horizon"] = real_horizon
        p["_city"] = m.get("city_name", "?")
        p["_city_slug"] = m.get("city", "?")
        p["_mkt_date"] = m.get("date", "")
        p["_unit"] = m.get("unit", "F")
        all_positions.append(p)

open_pos = [p for p in all_positions if p.get("status") == "open"]
closed_pos = [p for p in all_positions if p.get("status") == "closed"]

print(f"  Total positions: {len(all_positions)}")
print(f"  Open: {len(open_pos)}")
print(f"  Closed: {len(closed_pos)}")
print(f"  YES positions: {sum(1 for p in all_positions if p.get('side') == 'yes')}")
print(f"  NO positions: {sum(1 for p in all_positions if p.get('side') == 'no')}")

# ── 3. V3 NO trades (May 14+) — the actual strategy ─────────────────────
print("\n## 3. V3 NO STRATEGY (opened_at >= 2026-05-14)")
v3_no = [p for p in closed_pos if p.get("side") == "no" and p.get("opened_at", "") >= "2026-05-14"]
v3_no_d1plus = [p for p in v3_no if p["_real_horizon"] >= 1]
v3_no_d0 = [p for p in v3_no if p["_real_horizon"] == 0]

print(f"  Total V3 NO (closed): {len(v3_no)}")
print(f"  D+0 (should be 0 with min_horizon_days=1): {len(v3_no_d0)}")
print(f"  D+1+ (actual V3): {len(v3_no_d1plus)}")

if v3_no_d1plus:
    wins = [p for p in v3_no_d1plus if (p.get("pnl") or 0) > 0]
    losses = [p for p in v3_no_d1plus if (p.get("pnl") or 0) < 0]
    zeros = [p for p in v3_no_d1plus if (p.get("pnl") or 0) == 0]
    total_pnl = sum(p.get("pnl", 0) or 0 for p in v3_no_d1plus)
    total_cost = sum(p.get("cost", 0) or 0 for p in v3_no_d1plus)
    print(f"  Record: {len(wins)}W / {len(losses)}L / {len(zeros)} break-even")
    print(f"  Win rate: {len(wins)/(len(wins)+len(losses))*100:.1f}%" if wins or losses else "")
    print(f"  Total PnL: ${total_pnl:+.2f}")
    print(f"  Total wagered: ${total_cost:.2f}")
    print(f"  ROI: {total_pnl/total_cost*100:+.1f}%" if total_cost else "")

    # By exit reason
    print("\n  By exit reason:")
    by_reason = defaultdict(list)
    for p in v3_no_d1plus:
        by_reason[p.get("close_reason", "unknown")].append(p)
    for r, ps in sorted(by_reason.items()):
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in ps if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        cost = sum(p.get("cost", 0) or 0 for p in ps)
        roi = pnl/cost*100 if cost else 0
        print(f"    {r:20s}: {len(ps):3d} ({w}W/{l}L) PnL ${pnl:+.2f} ROI {roi:+.1f}%")

    # By real horizon
    print("\n  By real horizon:")
    for h in range(0, 7):
        subset = [p for p in v3_no_d1plus if p["_real_horizon"] == h]
        if not subset:
            continue
        w = sum(1 for p in subset if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in subset if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in subset)
        cost = sum(p.get("cost", 0) or 0 for p in subset)
        roi = pnl/cost*100 if cost else 0
        print(f"    D+{h}: {len(subset):3d} trades, {w}W/{l}L = {w/(w+l)*100:.0f}% WR, PnL ${pnl:+.2f}, ROI {roi:+.1f}%")

# ── 4. By city ────────────────────────────────────────────────────────────
print("\n## 4. BY CITY (V3 NO, D+1+)")
if v3_no_d1plus:
    by_city = defaultdict(list)
    for p in v3_no_d1plus:
        by_city[p["_city"]].append(p)
    for city in sorted(by_city.keys()):
        ps = by_city[city]
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in ps if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        cost = sum(p.get("cost", 0) or 0 for p in ps)
        roi = pnl/cost*100 if cost else 0
        unit = ps[0]["_unit"]
        print(f"    {city:20s} ({unit}): {len(ps):3d} trades, {w}W/{l}L, PnL ${pnl:+.2f}, ROI {roi:+.1f}%")

# ── 5. Entry price analysis ──────────────────────────────────────────────
print("\n## 5. ENTRY PRICE ANALYSIS (V3 NO, D+1+)")
if v3_no_d1plus:
    # By price band
    bands = [(0.60, 0.70), (0.70, 0.75), (0.75, 0.80), (0.80, 0.85), (0.85, 0.90), (0.90, 0.95)]
    for lo, hi in bands:
        subset = [p for p in v3_no_d1plus if lo <= (p.get("entry_price") or 0) < hi]
        if not subset:
            continue
        w = sum(1 for p in subset if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in subset if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in subset)
        cost = sum(p.get("cost", 0) or 0 for p in subset)
        roi = pnl/cost*100 if cost else 0
        avg_entry = sum(p.get("entry_price", 0) for p in subset) / len(subset)
        print(f"    ${lo:.2f}-${hi:.2f}: {len(subset):3d} trades, {w}W/{l}L, avg entry ${avg_entry:.3f}, PnL ${pnl:+.2f}, ROI {roi:+.1f}%")

    # Win/loss amounts
    win_amts = [p.get("pnl", 0) or 0 for p in v3_no_d1plus if (p.get("pnl", 0) or 0) > 0]
    loss_amts = [p.get("pnl", 0) or 0 for p in v3_no_d1plus if (p.get("pnl", 0) or 0) < 0]
    print(f"\n  Avg win: ${sum(win_amts)/len(win_amts):+.2f}" if win_amts else "")
    print(f"  Avg loss: ${sum(loss_amts)/len(loss_amts):+.2f}" if loss_amts else "")
    print(f"  Max single loss: ${min(loss_amts):.2f}" if loss_amts else "")
    print(f"  Max single win: ${max(win_amts):+.2f}" if win_amts else "")

# ── 6. Resolution-only analysis (remove take-profit to see true edge) ────
print("\n## 6. RESOLUTION-ONLY ANALYSIS (what if we held everything?)")
if v3_no_d1plus:
    resolution_only = [p for p in v3_no_d1plus if p.get("close_reason") in ("resolved_win", "resolved_loss")]
    tp_exits = [p for p in v3_no_d1plus if p.get("close_reason") == "take_profit"]
    print(f"  Resolution-only: {len(resolution_only)} trades")
    if resolution_only:
        w = sum(1 for p in resolution_only if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in resolution_only if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in resolution_only)
        cost = sum(p.get("cost", 0) or 0 for p in resolution_only)
        print(f"  Record: {w}W/{l}L = {w/(w+l)*100:.0f}% WR")
        print(f"  PnL: ${pnl:+.2f}, ROI: {pnl/cost*100:+.1f}%")
    print(f"  Take-profit exits: {len(tp_exits)}")
    if tp_exits:
        tp_pnl = sum(p.get("pnl", 0) or 0 for p in tp_exits)
        tp_cost = sum(p.get("cost", 0) or 0 for p in tp_exits)
        print(f"  TP PnL: ${tp_pnl:+.2f}, avg: ${tp_pnl/len(tp_exits):+.2f}")

# ── 7. All losses deep-dive ──────────────────────────────────────────────
print("\n## 7. ALL V3 LOSSES (deep-dive)")
if v3_no_d1plus:
    for p in [x for x in v3_no_d1plus if (x.get("pnl", 0) or 0) < 0]:
        bkt = f"{p.get('bucket_low', 0):.0f}-{p.get('bucket_high', 0):.0f}°{p['_unit']}"
        print(f"  {p['_city']:15s} {p['_mkt_date']} D+{p['_real_horizon']} | "
              f"NO {bkt} | entry ${p.get('entry_price', 0):.3f} | "
              f"PnL ${p.get('pnl', 0):+.2f} | reason: {p.get('close_reason', '?')} | "
              f"forecast: {p.get('forecast_temp', '?')}°{p['_unit']} sigma={p.get('sigma', '?')}")

# ── 8. Open positions risk ──────────────────────────────────────────────
print(f"\n## 8. OPEN POSITIONS RISK ({len(open_pos)} positions)")
if open_pos:
    total_at_risk = sum(p.get("cost", 0) or 0 for p in open_pos)
    by_side = defaultdict(list)
    for p in open_pos:
        by_side[p.get("side", "?")].append(p)
    for side, ps in by_side.items():
        cost = sum(p.get("cost", 0) or 0 for p in ps)
        print(f"  {side.upper()}: {len(ps)} positions, ${cost:.2f} at risk")
    
    # Open by city
    open_by_city = defaultdict(list)
    for p in open_pos:
        open_by_city[p["_city"]].append(p)
    print(f"\n  Open by city:")
    for city in sorted(open_by_city.keys()):
        ps = open_by_city[city]
        cost = sum(p.get("cost", 0) or 0 for p in ps)
        print(f"    {city:20s}: {len(ps)} positions, ${cost:.2f}")

    # Worst case: all open positions lose
    print(f"\n  WORST CASE: all open positions resolve to $0")
    print(f"  Total at risk: ${total_at_risk:.2f}")

    # By horizon
    open_by_hz = defaultdict(list)
    for p in open_pos:
        open_by_hz[p["_real_horizon"]].append(p)
    print(f"\n  Open by real horizon:")
    for h in sorted(open_by_hz.keys()):
        ps = open_by_hz[h]
        cost = sum(p.get("cost", 0) or 0 for p in ps)
        print(f"    D+{h}: {len(ps)} positions, ${cost:.2f}")

# ── 9. Forecast source analysis ──────────────────────────────────────────
print("\n## 9. FORECAST SOURCE ANALYSIS (V3 NO, D+1+)")
if v3_no_d1plus:
    by_src = defaultdict(list)
    for p in v3_no_d1plus:
        by_src[p.get("forecast_source", "?")].append(p)
    for src, ps in sorted(by_src.items()):
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in ps if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        cost = sum(p.get("cost", 0) or 0 for p in ps)
        roi = pnl/cost*100 if cost else 0
        print(f"    {src:12s}: {len(ps):3d} trades, {w}W/{l}L, PnL ${pnl:+.2f}, ROI {roi:+.1f}%")

# ── 10. Correlation analysis ─────────────────────────────────────────────
print("\n## 10. LOSS CORRELATION")
if v3_no_d1plus:
    loss_dates = defaultdict(list)
    for p in [x for x in v3_no_d1plus if (x.get("pnl", 0) or 0) < 0]:
        loss_dates[p.get("_mkt_date", "?")].append(p)
    if loss_dates:
        print(f"  Losses grouped by market date:")
        for d in sorted(loss_dates.keys()):
            ps = loss_dates[d]
            cities = [p["_city"] for p in ps]
            total_loss = sum(p.get("pnl", 0) or 0 for p in ps)
            print(f"    {d}: {len(ps)} losses ({', '.join(cities)}), total ${total_loss:.2f}")

# ── 11. Calibration data ────────────────────────────────────────────────
print("\n## 11. CALIBRATION DATA")
cal_rows = conn.execute("SELECT key, sigma, mae, n FROM calibration ORDER BY key").fetchall()
if cal_rows:
    for r in cal_rows:
        print(f"    {r['key']:30s}: sigma={r['sigma']:.3f}, MAE={r['mae']}, n={r['n']}")
else:
    print("  No calibration data yet")

# ── 12. State ────────────────────────────────────────────────────────────
print("\n## 12. CURRENT STATE")
state_row = conn.execute("SELECT json_data FROM state WHERE id=1").fetchone()
if state_row:
    state = json.loads(state_row['json_data'])
    for k, v in state.items():
        print(f"    {k}: {v}")

# ── 13. Bucket width analysis ───────────────────────────────────────────
print("\n## 13. BUCKET WIDTH vs OUTCOME (V3 NO)")
if v3_no_d1plus:
    for p in v3_no_d1plus:
        lo = p.get("bucket_low", 0)
        hi = p.get("bucket_high", 0)
        if lo == -999 or hi == 999:
            p["_bucket_width"] = "edge"
        else:
            p["_bucket_width"] = f"{hi - lo:.0f}°"
    
    by_width = defaultdict(list)
    for p in v3_no_d1plus:
        by_width[p["_bucket_width"]].append(p)
    
    for width in sorted(by_width.keys()):
        ps = by_width[width]
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in ps if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        cost = sum(p.get("cost", 0) or 0 for p in ps)
        roi = pnl/cost*100 if cost else 0
        print(f"    width={width:5s}: {len(ps):3d} trades, {w}W/{l}L, PnL ${pnl:+.2f}, ROI {roi:+.1f}%")

# ── 14. Time-of-day analysis ────────────────────────────────────────────
print("\n## 14. TIME-OF-DAY (hour UTC) — V3 NO")
if v3_no_d1plus:
    by_hour = defaultdict(list)
    for p in v3_no_d1plus:
        try:
            h = datetime.fromisoformat(p["opened_at"]).hour
            by_hour[h].append(p)
        except:
            pass
    for h in sorted(by_hour.keys()):
        ps = by_hour[h]
        w = sum(1 for p in ps if (p.get("pnl", 0) or 0) > 0)
        l = sum(1 for p in ps if (p.get("pnl", 0) or 0) < 0)
        pnl = sum(p.get("pnl", 0) or 0 for p in ps)
        print(f"    {h:02d}:00 UTC: {len(ps):3d} trades, {w}W/{l}L, PnL ${pnl:+.2f}")

# ── 15. P-value vs breakeven ────────────────────────────────────────────
print("\n## 15. STATISTICAL SIGNIFICANCE")
if v3_no_d1plus:
    wins = [p for p in v3_no_d1plus if (p.get("pnl", 0) or 0) > 0]
    losses = [p for p in v3_no_d1plus if (p.get("pnl", 0) or 0) < 0]
    n = len(wins) + len(losses)
    w = len(wins)
    if n > 0:
        wr = w / n
        # Average entry price to compute breakeven WR
        avg_entry = sum(p.get("entry_price", 0) for p in v3_no_d1plus) / len(v3_no_d1plus)
        # NO resolves to $1.00. Profit = 1 - entry. Loss = entry.
        # Breakeven: WR * (1-entry) = (1-WR) * entry → WR = entry / 1 = entry
        be_wr = avg_entry  # For a $1 payout NO token, breakeven WR = entry_price
        
        # Binomial test p-value (one-tailed: is WR > breakeven?)
        from math import comb, log
        p_value = 0
        for k in range(w, n+1):
            p_value += comb(n, k) * (be_wr ** k) * ((1 - be_wr) ** (n - k))
        
        print(f"  n={n}, wins={w}, WR={wr*100:.1f}%")
        print(f"  Avg NO entry: ${avg_entry:.3f}")
        print(f"  Breakeven WR: {be_wr*100:.1f}%")
        print(f"  Observed WR: {wr*100:.1f}%")
        print(f"  One-tailed p-value: {p_value:.4f}")
        print(f"  Significant at 5%? {'YES' if p_value < 0.05 else 'NO'}")
        print(f"  Significant at 10%? {'YES' if p_value < 0.10 else 'NO'}")

# ── 16. Trades table summary ────────────────────────────────────────────
print("\n## 16. TRADES TABLE SUMMARY")
trade_cnt = conn.execute("SELECT COUNT(*) as c FROM trades").fetchone()['c']
print(f"  Total trade records: {trade_cnt}")
if trade_cnt > 0:
    # Recent trades
    recent = conn.execute("SELECT city_name, date, side, entry_price, exit_price, pnl, reason, opened_at FROM trades ORDER BY ts DESC LIMIT 10").fetchall()
    print(f"\n  Last 10 trades:")
    for t in recent:
        print(f"    {t['city_name']:15s} {t['date']} {t['side']:3s} entry=${t['entry_price']:.3f} pnl=${t['pnl']:+.2f} reason={t['reason']}")

conn.close()
print("\n" + "=" * 70)
print("  AUDIT COMPLETE")
print("=" * 70)
