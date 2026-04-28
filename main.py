#!/usr/bin/env python3
"""
WeatherBot — Polymarket Weather Trading Bot
============================================
Usage:
    python main.py          # start trading loop
    python main.py status   # balance + open positions
    python main.py report   # full resolved-trade breakdown
    python main.py probe    # one scan, no positions opened (dry run)
"""

import sys
import time
from datetime import datetime, timedelta, timezone

from core.calibrator import get_sigma, run_calibration
from core.config import load_config
from core.executor import try_open_position
from core.forecaster import take_snapshot
from core.locations import LOCATIONS, MONTHS, TIER1_CITIES
from core.monitor import check_forecast_change, check_resolution, check_stops_and_tp
from core.scanner import get_event, hours_to_resolution, parse_outcomes
from core.storage import (
    ensure_dirs,
    load_all_markets,
    load_calibration,
    load_state,
    new_market,
    save_market,
    save_state,
)


def scan_once(cfg, calibration: dict, dry_run: bool = False) -> tuple[int, int, int]:
    """
    One full scan cycle across all active cities.
    Returns (new_positions, closed_positions, resolved_markets).
    """
    now = datetime.now(timezone.utc)
    state = load_state(cfg.balance)
    new_pos = closed = resolved = 0

    active_cities = TIER1_CITIES   # expand to all LOCATIONS keys in Phase 3

    for city_slug in active_cities:
        loc = LOCATIONS[city_slug]
        print(f"  → {loc.name}...", end=" ", flush=True)

        # Fetch all forecast sources once per city
        dates = [(now + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(4)]
        try:
            snapshots = take_snapshot(city_slug, dates)
            time.sleep(0.3)
        except Exception as exc:
            print(f"skip ({exc})")
            continue

        for i, date_str in enumerate(dates):
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            event = get_event(city_slug, dt.month, dt.day, dt.year)
            if not event:
                continue

            end_date = event.get("endDate", "")
            hours = hours_to_resolution(end_date)

            # Load or create market record
            from core.storage import load_market
            mkt = load_market(city_slug, date_str)
            if mkt is None:
                if hours < cfg.min_hours or hours > cfg.max_hours:
                    continue
                mkt = new_market(
                    city_slug=city_slug,
                    city_name=loc.name,
                    station=loc.station,
                    unit=loc.unit,
                    date_str=date_str,
                    end_date=end_date,
                    hours_at_discovery=hours,
                )

            if mkt["status"] == "resolved":
                continue

            # Update outcomes from live event data
            outcomes = parse_outcomes(event)
            snap = snapshots.get(date_str)
            forecast_temp = snap.best if snap else None
            forecast_source = snap.best_source if snap else None

            horizon = f"D+{i}"
            mkt = {
                **mkt,
                "current_horizon": horizon,
                "all_outcomes": [
                    {
                        "question":  o.question,
                        "market_id": o.market_id,
                        "range":     [o.t_low, o.t_high],
                        "bid":       o.bid,
                        "ask":       o.ask,
                        "spread":    o.spread,
                        "volume":    o.volume,
                    }
                    for o in outcomes
                ],
            }

            # Append forecast snapshot
            if snap:
                mkt["forecast_snapshots"].append({
                    "ts":          snap.ts,
                    "horizon":     horizon,
                    "hours_left":  round(hours, 1),
                    "ecmwf":       snap.ecmwf,
                    "gfs":         snap.gfs,
                    "metar":       snap.metar,
                    "best":        snap.best,
                    "best_source": snap.best_source,
                })

            # ── Monitor existing position ────────────────────────────────────
            if mkt.get("position") and mkt["position"].get("status") == "open":
                # 1. Resolution check
                mkt, state, did_resolve = check_resolution(mkt, state, cfg.vc_key)
                if did_resolve:
                    resolved += 1
                    continue

                # 2. Stop / take-profit
                mkt, state, did_close = check_stops_and_tp(mkt, state)
                if did_close:
                    closed += 1
                    continue

                # 3. Forecast change exit
                if forecast_temp is not None:
                    mkt, state, did_close = check_forecast_change(
                        mkt, state, forecast_temp, loc.unit
                    )
                    if did_close:
                        closed += 1
                        continue

            # ── Open new position ────────────────────────────────────────────
            if (
                not mkt.get("position")
                and forecast_temp is not None
                and hours >= cfg.min_hours
                and not dry_run
            ):
                sigma = get_sigma(city_slug, forecast_source or "ecmwf", calibration)

                # Find the one bucket that matches the forecast
                matched = next(
                    (o for o in outcomes
                     if _in_bucket(forecast_temp, o.t_low, o.t_high)),
                    None,
                )
                if matched:
                    mkt, state, did_open = try_open_position(
                        mkt, matched, forecast_temp, forecast_source or "ecmwf",
                        sigma, state, cfg,
                    )
                    if did_open:
                        new_pos += 1

            # Mark as closed by time
            if hours < 0.5 and mkt["status"] == "open":
                mkt = {**mkt, "status": "closed"}

            save_market(mkt)
            time.sleep(0.1)

        print("ok")

    save_state(state)

    # Recalibrate if enough resolved data
    all_mkts = load_all_markets()
    resolved_count = sum(1 for m in all_mkts if m.get("status") == "resolved")
    if resolved_count >= cfg.calibration_min:
        calibration.update(run_calibration(all_mkts, cfg.calibration_min))

    return new_pos, closed, resolved


def monitor_loop(cfg, calibration: dict) -> None:
    """Quick stop/TP check between full scans (runs every 10 min)."""
    all_mkts = load_all_markets()
    open_mkts = [
        m for m in all_mkts
        if m.get("position") and m["position"].get("status") == "open"
    ]
    if not open_mkts:
        return

    state = load_state(cfg.balance)
    for mkt in open_mkts:
        mkt, state, _ = check_stops_and_tp(mkt, state)
        mkt, state, _ = check_resolution(mkt, state, cfg.vc_key)
    save_state(state)


def run_loop() -> None:
    cfg = load_config()
    ensure_dirs()
    calibration = load_calibration()

    print(f"\n{'='*55}")
    print(f"  WEATHERBOT — STARTING")
    print(f"{'='*55}")
    print(f"  Mode:       {'PAPER' if cfg.paper_trading else 'LIVE'}")
    print(f"  Cities:     {', '.join(TIER1_CITIES)}")
    print(f"  Balance:    ${cfg.balance:,.0f} | Max bet: ${cfg.max_bet}")
    print(f"  Scan:       {cfg.scan_interval//60} min | Monitor: {cfg.monitor_interval//60} min")
    print(f"  Min EV:     {cfg.min_ev:.0%} | Max price: ${cfg.max_price}")
    print(f"  Ctrl+C to stop\n")

    last_full_scan = 0.0

    while True:
        now_ts = time.time()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if now_ts - last_full_scan >= cfg.scan_interval:
            print(f"\n[{now_str}] full scan...")
            try:
                new_pos, closed, res = scan_once(cfg, calibration)
                state = load_state(cfg.balance)
                print(
                    f"  balance: ${state['balance']:,.2f} | "
                    f"new: {new_pos} | closed: {closed} | resolved: {res}"
                )
                last_full_scan = time.time()
            except KeyboardInterrupt:
                print("\n  Stopping — state saved. Bye!")
                break
            except Exception as exc:
                print(f"  Scan error: {exc} — retrying in 60s")
                time.sleep(60)
                continue
        else:
            print(f"[{now_str}] monitoring positions...")
            try:
                monitor_loop(cfg, calibration)
            except Exception as exc:
                print(f"  Monitor error: {exc}")

        try:
            time.sleep(cfg.monitor_interval)
        except KeyboardInterrupt:
            print("\n  Stopping. Bye!")
            break


def print_status() -> None:
    cfg = load_config()
    state = load_state(cfg.balance)
    all_mkts = load_all_markets()

    open_pos = [m for m in all_mkts if m.get("position") and m["position"].get("status") == "open"]
    resolved = [m for m in all_mkts if m.get("status") == "resolved"]

    bal = state["balance"]
    start = state["starting_balance"]
    ret = (bal - start) / start * 100
    wins = state.get("wins", 0)
    losses = state.get("losses", 0)
    total = wins + losses

    print(f"\n{'='*55}")
    print(f"  WEATHERBOT — STATUS  ({'PAPER' if cfg.paper_trading else 'LIVE'})")
    print(f"{'='*55}")
    print(f"  Balance:  ${bal:,.2f}  (start ${start:,.2f}, {'+'if ret>=0 else ''}{ret:.1f}%)")
    if total:
        print(f"  Trades:   {total} | W: {wins} | L: {losses} | WR: {wins/total:.0%}")
    else:
        print(f"  Trades:   none yet")
    print(f"  Open:     {len(open_pos)} | Resolved: {len(resolved)}")

    if open_pos:
        print(f"\n  Open positions:")
        for m in open_pos:
            pos = m["position"]
            unit = m.get("unit", "F")
            label = f"{pos['bucket_low']:.0f}–{pos['bucket_high']:.0f}°{unit}"
            src = pos.get("forecast_source", "?").upper()
            print(f"    {m['city_name']:<16} {m['date']} | {label:<14} | "
                  f"entry ${pos['entry_price']:.3f} | {src}")
    print(f"{'='*55}\n")


def print_report() -> None:
    all_mkts = load_all_markets()
    resolved = [m for m in all_mkts if m.get("status") == "resolved" and m.get("pnl") is not None]

    print(f"\n{'='*55}")
    print(f"  WEATHERBOT — FULL REPORT")
    print(f"{'='*55}")

    if not resolved:
        print("  No resolved markets yet.\n")
        return

    total_pnl = sum(m["pnl"] for m in resolved)
    wins = [m for m in resolved if m.get("resolved_outcome") == "win"]

    print(f"\n  Resolved: {len(resolved)} | Wins: {len(wins)} | "
          f"WR: {len(wins)/len(resolved):.0%} | PnL: {'+'if total_pnl>=0 else ''}{total_pnl:.2f}")

    print(f"\n  By city:")
    for city in sorted({m["city"] for m in resolved}):
        group = [m for m in resolved if m["city"] == city]
        w = sum(1 for m in group if m.get("resolved_outcome") == "win")
        pnl = sum(m["pnl"] for m in group)
        name = LOCATIONS[city].name if city in LOCATIONS else city
        sign = "+" if pnl >= 0 else ""
        print(f"    {name:<16} {w}/{len(group)} ({w/len(group):.0%})  PnL: {sign}{pnl:.2f}")

    print(f"\n  Trades:")
    for m in sorted(resolved, key=lambda x: x["date"]):
        pos = m.get("position", {}) or {}
        snaps = m.get("forecast_snapshots", [])
        fc = snaps[-1].get("best") if snaps else None
        unit = m.get("unit", "F")
        bucket = f"{pos.get('bucket_low'):.0f}–{pos.get('bucket_high'):.0f}°{unit}" if pos else "—"
        outcome = m.get("resolved_outcome", "?").upper()
        pnl_str = f"{'+'if m['pnl']>=0 else ''}{m['pnl']:.2f}" if m.get("pnl") is not None else "—"
        actual = f"actual {m['actual_temp']}°{unit}" if m.get("actual_temp") else ""
        print(f"    {m['city_name']:<16} {m['date']} | {bucket:<14} | {outcome} {pnl_str} {actual}")

    print(f"{'='*55}\n")


def _in_bucket(forecast: float, t_low: float, t_high: float) -> bool:
    if t_low == t_high:
        return round(forecast) == round(t_low)
    return t_low <= forecast <= t_high


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd == "run":
        run_loop()
    elif cmd == "status":
        print_status()
    elif cmd == "report":
        print_report()
    elif cmd == "probe":
        _cfg = load_config()
        ensure_dirs()
        _cal = load_calibration()
        print("Dry-run scan (no positions will be opened)...")
        scan_once(_cfg, _cal, dry_run=True)
    else:
        print("Usage: python main.py [run|status|report|probe]")
