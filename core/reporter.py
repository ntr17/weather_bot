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
    load_all_markets,
    load_calibration,
    load_state,
    load_trades,
)

STATUS_PATH = Path(__file__).parent.parent / "data" / "status.md"


def generate_status(cfg) -> str:
    """Build full status report and write to data/status.md."""
    now = datetime.now(timezone.utc)
    state = load_state(cfg.balance)
    all_mkts = load_all_markets()
    trades = load_trades()
    cal = load_calibration()
    health = get_city_health(lookback=20)

    open_pos = [m for m in all_mkts if m.get("position") and m["position"].get("status") == "open"]
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
        lines.append(f"## Open Positions ({len(open_pos)})")
        lines.append(f"| City | Date | Bucket | Side | Entry | Source | Horizon |")
        lines.append(f"|------|------|--------|------|-------|--------|---------|")
        for m in sorted(open_pos, key=lambda x: x["date"]):
            pos = m["position"]
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
                  "stop_loss_pct", "no_stop_loss_floor", "trailing_activation",
                  "no_pyes_threshold", "min_hours", "max_hours"):
        val = getattr(cfg, field, "?")
        lines.append(f"| {field} | {val} |")
    lines.append("")

    report = "\n".join(lines)
    STATUS_PATH.parent.mkdir(exist_ok=True)
    STATUS_PATH.write_text(report, encoding="utf-8")
    return report
