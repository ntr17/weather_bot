"""
Generate data/status.md — a full snapshot of bot state.

Committed to the repo after every Actions run so you (and Claude)
can see exactly what happened without running anything locally.
"""

from datetime import datetime, timezone
from pathlib import Path

from core.locations import LOCATIONS, TIER1_CITIES
from core.storage import (
    get_city_health,
    get_open_positions,
    has_any_open,
    load_all_markets,
    load_calibration,
    load_state,
    load_trades,
)

STATUS_PATH = Path(__file__).parent.parent / "data" / "status.md"


def generate_status(cfg) -> str:
    """Build full status report and write to data/status.md."""
    import json as _json
    _cfg_path = Path(__file__).parent.parent / "config.json"
    try:
        with open(_cfg_path, encoding="utf-8") as _f:
            cfg_dict = _json.load(_f)
    except Exception:
        cfg_dict = {}

    now = datetime.now(timezone.utc)
    state = load_state(cfg.balance)
    all_mkts = load_all_markets()
    trades = load_trades()
    cal = load_calibration()
    health = get_city_health(lookback=20)

    open_pos = [m for m in all_mkts if has_any_open(m)]
    resolved = [m for m in all_mkts if m.get("status") == "resolved"]

    bal = state["balance"]
    start = state["starting_balance"]
    ret = (bal - start) / start * 100
    wins = state.get("wins", 0)
    losses = state.get("losses", 0)
    total = wins + losses

    lines = []
    lines.append(f"# WeatherBot Status")
    lines.append(f"_Auto-generated {now.strftime('%Y-%m-%d %H:%M UTC')}_\n")

    # ── Summary ──────────────────────────────────────────────────────────────
    lines.append(f"## Summary")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Mode | {'PAPER' if cfg.paper_trading else '**LIVE**'} |")
    lines.append(f"| Balance | ${bal:,.2f} |")
    lines.append(f"| Starting | ${start:,.2f} |")
    lines.append(f"| Return | {'+' if ret >= 0 else ''}{ret:.1f}% |")
    lines.append(f"| Total trades | {total} |")
    if total:
        lines.append(f"| Win rate | {wins}/{total} ({wins/total:.0%}) |")
    lines.append(f"| Open positions | {len(open_pos)} |")
    lines.append(f"| Markets tracked | {len(all_mkts)} |")
    lines.append(f"| Calibration keys | {len(cal)} |")
    lines.append("")

    # ── Open Positions ───────────────────────────────────────────────────────
    if open_pos:
        # Count total open positions across all markets
        total_open = sum(len(get_open_positions(m)) for m in open_pos)
        lines.append(f"## Open Positions ({total_open})")
        lines.append(f"| City | Date | Bucket | Side | Entry | Source | Horizon |")
        lines.append(f"|------|------|--------|------|-------|--------|---------|")
        for m in sorted(open_pos, key=lambda x: x["date"]):
            for pos in get_open_positions(m).values():
                unit = m.get("unit", "F")
                bucket = f"{pos['bucket_low']:.0f}–{pos['bucket_high']:.0f}°{unit}"
                side = pos.get("side", "yes").upper()
                src = pos.get("forecast_source", "?").upper()
                hz = m.get("current_horizon", "?")
                lines.append(f"| {m['city_name']} | {m['date']} | {bucket} | {side} | "
                             f"${pos['entry_price']:.3f} | {src} | {hz} |")
        lines.append("")

    # ── Recent Trades ────────────────────────────────────────────────────────
    recent = sorted(trades, key=lambda t: t.get("ts", ""), reverse=True)[:20]
    if recent:
        lines.append(f"## Recent Trades (last {len(recent)})")
        lines.append(f"| City | Date | Bucket | Side | Entry | PnL | Outcome | Source |")
        lines.append(f"|------|------|--------|------|-------|-----|---------|--------|")
        for t in recent:
            unit = t.get("unit", "F")
            bucket = f"{t.get('bucket_low', 0):.0f}–{t.get('bucket_high', 0):.0f}°{unit}"
            side = t.get("side", "?").upper()
            pnl = t.get("pnl", 0)
            pnl_str = f"{'+'if pnl>=0 else ''}{pnl:.2f}" if pnl is not None else "—"
            outcome = t.get("outcome", "?")
            src = (t.get("forecast_source") or "?").upper()
            lines.append(f"| {t.get('city_name', '?')} | {t.get('date', '?')} | "
                         f"{bucket} | {side} | ${t.get('entry_price', 0):.3f} | "
                         f"{pnl_str} | {outcome} | {src} |")
        lines.append("")

    # ── City Performance ─────────────────────────────────────────────────────
    city_trades: dict[str, list] = {}
    for t in trades:
        city_trades.setdefault(t.get("city", "?"), []).append(t)

    if city_trades:
        lines.append(f"## City Performance")
        lines.append(f"| City | Trades | Wins | WR | PnL | Avg PnL |")
        lines.append(f"|------|--------|------|-----|-----|---------|")
        for city in sorted(city_trades):
            ct = city_trades[city]
            w = sum(1 for t in ct if t.get("outcome") == "win")
            pnl = sum(t.get("pnl", 0) for t in ct)
            avg = pnl / len(ct) if ct else 0
            name = LOCATIONS[city].name if city in LOCATIONS else city
            wr = f"{w/len(ct):.0%}" if ct else "—"
            lines.append(f"| {name} | {len(ct)} | {w} | {wr} | "
                         f"{'+'if pnl>=0 else ''}{pnl:.2f} | "
                         f"{'+'if avg>=0 else ''}{avg:.2f} |")
        lines.append("")

    # ── City Health (API reliability) ────────────────────────────────────────
    flagged = {c: h for c, h in health.items() if h["flagged"]}
    if health:
        lines.append(f"## City Health (last 20 runs)")
        if flagged:
            lines.append(f"\n**{len(flagged)} cities flagged** (>=3 consecutive failures or >=50% fail rate):\n")
        lines.append(f"| City | OK | Fails | Rate | Streak | Status | Last Error |")
        lines.append(f"|------|----|-------|------|--------|--------|------------|")
        for city in sorted(health):
            h = health[city]
            name = LOCATIONS[city].name if city in LOCATIONS else city
            ok = h["total_runs"] - h["fails"]
            status = "⚠ FLAGGED" if h["flagged"] else "ok"
            err = (h["last_error"] or "")[:60]
            lines.append(f"| {name} | {ok} | {h['fails']} | "
                         f"{h['fail_rate']:.0%} | {h['consec_fails']} | {status} | {err} |")
        lines.append("")

    # ── Calibration ──────────────────────────────────────────────────────────
    if cal:
        lines.append(f"## Calibration ({len(cal)} keys)")
        # Show per-city sigma summary
        cities_done = sorted({k.split("_")[0] for k in cal if "_ecmwf_" in k or "_gfs_" in k})
        if cities_done:
            lines.append(f"| City | ECMWF D+1 σ | GFS D+1 σ | Source | Samples |")
            lines.append(f"|------|-------------|-----------|--------|---------|")
            for city in cities_done:
                loc = LOCATIONS.get(city)
                if not loc:
                    continue
                e_key = f"{city}_ecmwf_D+1"
                g_key = f"{city}_gfs_D+1"
                e = cal.get(e_key, {})
                g = cal.get(g_key, {})
                lines.append(
                    f"| {loc.name} | {e.get('sigma', '—')} | {g.get('sigma', '—')} | "
                    f"{e.get('source', '—')} | {e.get('n', '—')} |"
                )
            lines.append("")

    # ── Strategy Parameters ──────────────────────────────────────────────────
    lines.append(f"## Active Config")
    lines.append(f"| Param | Value |")
    lines.append(f"|-------|-------|")
    for field in ("max_bet", "min_ev", "max_price", "max_no_price", "kelly_fraction",
                  "stop_loss_pct", "no_stop_loss_pct", "trailing_activation",
                  "no_pyes_threshold", "min_hours", "max_hours",
                  "enable_yes_trading", "min_no_entry", "max_no_entry",
                  "no_stop_enabled", "no_forecast_exit", "max_horizon_days",
                  "max_no_positions"):
        val = getattr(cfg, field, "?")
        lines.append(f"| {field} | {val} |")
    lines.append("")

    # ── Edge Tracker (v2 strategy) ───────────────────────────────────────────
    # Track only NO trades opened after the v2 strategy cutover
    v2_cutover = cfg_dict.get("v2_cutover", "2026-05-06T00:00:00")
    v2_trades = [t for t in trades
                 if t.get("side") == "no"
                 and (t.get("opened_at") or t.get("ts", "")) >= v2_cutover]
    if v2_trades:
        v2_n = len(v2_trades)
        v2_wins = sum(1 for t in v2_trades if (t.get("pnl") or 0) > 0)
        v2_losses = sum(1 for t in v2_trades if (t.get("pnl") or 0) < 0)
        v2_pnl = sum(t.get("pnl", 0) for t in v2_trades)
        v2_cost = sum(t.get("cost", 0) for t in v2_trades)
        v2_roi = (v2_pnl / v2_cost * 100) if v2_cost else 0
        v2_wr = v2_wins / v2_n * 100 if v2_n else 0

        # by close reason
        from collections import Counter
        v2_reasons = Counter(t.get("reason", "open") for t in v2_trades)

        # resolved-only subset
        v2_resolved = [t for t in v2_trades
                       if t.get("reason") in ("resolved_win", "resolved_loss")]
        v2_res_n = len(v2_resolved)
        v2_res_wins = sum(1 for t in v2_resolved if (t.get("pnl") or 0) > 0)
        v2_res_pnl = sum(t.get("pnl", 0) for t in v2_resolved)

        lines.append("## Edge Tracker (v2 NO-HOLD strategy)")
        lines.append(f"_Tracking NO trades opened after {v2_cutover[:10]}_\n")
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        lines.append(f"| Closed trades | {v2_n} |")
        lines.append(f"| Wins / Losses | {v2_wins} / {v2_losses} |")
        lines.append(f"| Win rate | {v2_wr:.1f}% |")
        lines.append(f"| Total PnL | ${v2_pnl:+.2f} |")
        lines.append(f"| ROI | {v2_roi:+.1f}% |")
        lines.append(f"| Resolved | {v2_res_n} ({v2_res_wins}W/{v2_res_n - v2_res_wins}L) |")
        if v2_res_n:
            lines.append(f"| Resolved WR | {v2_res_wins/v2_res_n*100:.1f}% |")
            lines.append(f"| Resolved PnL | ${v2_res_pnl:+.2f} |")
        lines.append(f"| Avg PnL/trade | ${v2_pnl/v2_n:+.2f} |")
        lines.append("")

        # close reason breakdown
        lines.append("### Close Reasons (v2)")
        lines.append("| Reason | Count | PnL |")
        lines.append("|--------|-------|-----|")
        for reason in ("resolved_win", "take_profit", "trailing_stop",
                       "forecast_changed", "stop_loss", "resolved_loss"):
            count = v2_reasons.get(reason, 0)
            if count == 0:
                continue
            rpnl = sum(t.get("pnl", 0) for t in v2_trades if t.get("reason") == reason)
            lines.append(f"| {reason} | {count} | ${rpnl:+.2f} |")
        lines.append("")
    else:
        lines.append("## Edge Tracker (v2 NO-HOLD strategy)")
        lines.append(f"_No v2 trades yet (cutover: {v2_cutover[:10]})_\n")

    # ── Edge Tracker (v3 convergence strategy) ───────────────────────────────
    v3_cutover = cfg_dict.get("v3_cutover", "2026-05-14T00:00:00")
    v3_trades = [t for t in trades
                 if t.get("side") == "no"
                 and (t.get("opened_at") or t.get("ts", "")) >= v3_cutover]
    if v3_trades:
        v3_n = len(v3_trades)
        v3_wins = sum(1 for t in v3_trades if (t.get("pnl") or 0) > 0)
        v3_losses = sum(1 for t in v3_trades if (t.get("pnl") or 0) < 0)
        v3_pnl = sum(t.get("pnl", 0) for t in v3_trades)
        v3_cost = sum(t.get("cost", 0) for t in v3_trades)
        v3_roi = (v3_pnl / v3_cost * 100) if v3_cost else 0
        v3_wr = v3_wins / v3_n * 100 if v3_n else 0

        from collections import Counter
        v3_reasons = Counter(t.get("reason", "open") for t in v3_trades)
        v3_tp = sum(1 for t in v3_trades if t.get("reason") == "take_profit")

        lines.append("## Edge Tracker (v3 CONVERGENCE strategy)")
        lines.append(f"_D+1/D+2 NO trades opened after {v3_cutover[:10]}_\n")
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        lines.append(f"| Trades | {v3_n} |")
        lines.append(f"| Wins / Losses | {v3_wins} / {v3_losses} |")
        lines.append(f"| Win rate | {v3_wr:.1f}% |")
        lines.append(f"| Total PnL | ${v3_pnl:+.2f} |")
        lines.append(f"| ROI | {v3_roi:+.1f}% |")
        lines.append(f"| Take-profit exits | {v3_tp} |")
        lines.append(f"| Avg PnL/trade | ${v3_pnl/v3_n:+.2f} |")
        lines.append("")
    else:
        lines.append("## Edge Tracker (v3 CONVERGENCE strategy)")
        lines.append(f"_No v3 trades yet (cutover: {v3_cutover[:10]})_\n")

    report = "\n".join(lines)
    STATUS_PATH.parent.mkdir(exist_ok=True)
    STATUS_PATH.write_text(report, encoding="utf-8")
    return report
