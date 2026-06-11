#!/usr/bin/env python3
"""
WeatherBot — Polymarket Weather Trading Bot
============================================
Usage:
    python main.py          # start trading loop
    python main.py once     # single scan+monitor cycle, then exit
    python main.py status   # balance + open positions
    python main.py report   # full resolved-trade breakdown
    python main.py probe    # one scan, no positions opened (dry run)
"""

import math
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from datetime import datetime, timedelta, timezone

from core.calibrator import get_sigma, run_calibration
from core.config import load_config
from core.executor import try_open_no_position, try_open_position
from core.forecaster import take_snapshot
from core.locations import LOCATIONS, MONTHS, TIER1_CITIES
from core.monitor import check_forecast_change, check_resolution, check_stops_and_tp
from core.pricer import in_bucket
from core.reporter import generate_status
from core.risk import can_open_more, cfg_with_remaining_open_budget, total_open_cost
from core.scanner import get_event, hours_to_resolution, parse_outcomes
from core.storage import (
    append_run_log,
    ensure_dirs,
    get_city_health,
    get_open_positions,
    has_any_open,
    load_all_markets,
    load_calibration,
    load_market,
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
    open_cost = total_open_cost(load_all_markets())
    new_pos = closed = resolved = 0

    active_cities = TIER1_CITIES   # all 20 cities; add/remove in core/locations.py

    for city_slug in active_cities:
        loc = LOCATIONS[city_slug]
        print(f"  → {loc.name}...", end=" ", flush=True)
        city_t0 = time.time()
        city_new = city_closed = city_resolved = 0

        # Fetch all forecast sources once per city
        dates = [(now + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
        try:
            snapshots = take_snapshot(city_slug, dates)
            time.sleep(0.3)
        except Exception as exc:
            err_msg = str(exc)[:200]
            is_timeout = "timeout" in err_msg.lower() or "timed out" in err_msg.lower()
            status = "timeout" if is_timeout else "error"
            print(f"{status} ({exc})")
            append_run_log(city_slug, status, error=err_msg,
                           duration_s=time.time() - city_t0)
            continue

        for i, date_str in enumerate(dates):
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            event = get_event(city_slug, dt.month, dt.day, dt.year)
            if not event:
                continue

            end_date = event.get("endDate", "")
            hours = hours_to_resolution(end_date)

            # Load or create market record
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
                    "ts":           snap.ts,
                    "horizon":      horizon,
                    "hours_left":   round(hours, 1),
                    "ecmwf":        snap.ecmwf,
                    "gfs":          snap.gfs,
                    "metar":        snap.metar,
                    "best":         snap.best,
                    "best_source":  snap.best_source,
                    "model_spread": snap.model_spread,
                })

            # ── Monitor existing positions ───────────────────────────────────
            open_positions = get_open_positions(mkt)
            for pos_id, pos in list(open_positions.items()):
                # 1. Resolution check
                mkt, state, did_resolve = check_resolution(mkt, state, cfg.vc_key, pos_id, cfg=cfg)
                if did_resolve:
                    resolved += 1
                    city_resolved += 1
                    continue

                # 2. Stop / take-profit
                mkt, state, did_close = check_stops_and_tp(
                    mkt, state, cfg.trailing_activation, pos_id,
                    no_stop_enabled=cfg.no_stop_enabled,
                    cfg=cfg,
                )
                if did_close:
                    closed += 1
                    city_closed += 1
                    continue

                # 3. Forecast change exit (only if enabled for this side)
                if forecast_temp is not None:
                    side = pos.get("side", "yes")
                    skip_fc = (side == "no" and not cfg.no_forecast_exit)
                    if not skip_fc:
                        mkt, state, did_close = check_forecast_change(
                            mkt, state, forecast_temp, loc.unit, pos_id, cfg=cfg
                        )
                        if did_close:
                            closed += 1
                            city_closed += 1
                            continue

            # ── Open new positions ────────────────────────────────────────────
            # Guard: don't open if balance is critically low (2% reserve)
            min_reserve = cfg.balance * 0.02
            if (
                forecast_temp is not None
                and hours >= cfg.min_hours
                and not dry_run
                and state["balance"] >= min_reserve
            ):
                # When ensemble is used, look up ECMWF sigma (the calibrated base model)
                # then inflate by model spread: σ_eff = √(σ² + (spread/2)²)
                sigma_source = "ecmwf" if forecast_source == "ensemble" else (forecast_source or "ecmwf")
                sigma = get_sigma(city_slug, sigma_source, calibration, horizon=horizon)
                if snap and snap.model_spread:
                    sigma = round(math.sqrt(sigma ** 2 + (snap.model_spread / 2.0) ** 2), 3)
                src = forecast_source or "ecmwf"

                # Bucket IDs with real positions (open or closed) — prevent re-entry
                # Exclude paper_cancelled: those were bulk-cancelled during paper→live reset
                all_bucket_ids = {
                    pid for pid, pos in mkt.get("positions", {}).items()
                    if pos.get("close_reason") != "paper_cancelled"
                }

                # 1. Try YES on the bucket that matches the forecast (if enabled)
                can_open, _ = can_open_more(cfg, new_pos, open_cost)
                if cfg.enable_yes_trading and can_open:
                    matched = next(
                        (o for o in outcomes
                         if in_bucket(forecast_temp, o.t_low, o.t_high)),
                        None,
                    )
                    if matched and matched.market_id not in all_bucket_ids:
                        trade_cfg = cfg_with_remaining_open_budget(cfg, open_cost)
                        mkt, state, did_open = try_open_position(
                            mkt, matched, forecast_temp, src, sigma, state, trade_cfg,
                        )
                        if did_open:
                            new_pos += 1
                            city_new += 1
                            all_bucket_ids.add(matched.market_id)
                            open_cost += mkt["positions"][matched.market_id].get("cost", 0.0)

                # 2. Try NO on ALL tail buckets (multi-NO strategy)
                # Cap to max_no_positions per event; respect horizon limits
                if i < cfg.min_horizon_days or i > cfg.max_horizon_days:
                    save_market(mkt)
                    time.sleep(0.1)
                    continue
                current_no_count = sum(
                    1 for p in get_open_positions(mkt).values()
                    if p.get("side") == "no"
                )
                other_outcomes = [
                    o for o in outcomes
                    if not in_bucket(forecast_temp, o.t_low, o.t_high)
                    and o.market_id not in all_bucket_ids
                ]
                for o in other_outcomes:
                    if current_no_count >= cfg.max_no_positions:
                        break
                    can_open, _ = can_open_more(cfg, new_pos, open_cost)
                    if not can_open:
                        break
                    trade_cfg = cfg_with_remaining_open_budget(cfg, open_cost)
                    mkt, state, did_open = try_open_no_position(
                        mkt, o, forecast_temp, src, sigma, state, trade_cfg,
                    )
                    if did_open:
                        new_pos += 1
                        city_new += 1
                        all_bucket_ids.add(o.market_id)
                        current_no_count += 1
                        open_cost += mkt["positions"][o.market_id].get("cost", 0.0)

            # Mark as closed by time
            if hours < 0.5 and mkt["status"] == "open":
                mkt = {**mkt, "status": "closed"}

            save_market(mkt)
            time.sleep(0.1)

        print("ok")
        append_run_log(city_slug, "ok", duration_s=time.time() - city_t0,
                       new_pos=city_new, closed=city_closed, resolved=city_resolved)

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
    open_mkts = [m for m in all_mkts if has_any_open(m)]
    if not open_mkts:
        return

    state = load_state(cfg.balance)
    for mkt in open_mkts:
        for pos_id in list(get_open_positions(mkt).keys()):
            mkt, state, _ = check_stops_and_tp(
                mkt, state, cfg.trailing_activation, pos_id,
                no_stop_enabled=cfg.no_stop_enabled,
                cfg=cfg,
            )
            mkt, state, _ = check_resolution(mkt, state, cfg.vc_key, pos_id, cfg=cfg)
    save_state(state)


def check_pending_orders(cfg) -> int:
    """
    Check if any GTC orders with status="live" have been filled since last cycle.
    Updates position records accordingly. Returns number of fills confirmed.

    For live mode only — paper trading doesn't track real orders.
    """
    if cfg.paper_trading:
        return 0

    from core.clob import cancel_order, get_order
    from core.executor import close_position

    live_order_ttl_hours = 12.0   # cancel GTC orders that haven't filled by then

    all_mkts = load_all_markets()
    state = load_state(cfg.balance)
    fills = 0
    now = datetime.now(timezone.utc)

    for mkt in all_mkts:
        changed = False

        for pos_id, pos in list(mkt.get("positions", {}).items()):
            if pos.get("status") != "open":
                continue
            if pos.get("order_status") != "live":
                continue

            order_id = pos.get("live_order_id", "")
            if not order_id:
                continue

            # Query CLOB for this order's current state
            order_info = get_order(order_id)
            if order_info is None:
                continue

            size_matched = float(order_info.get("size_matched", "0"))
            original_size = float(order_info.get("original_size", "0"))

            if original_size > 0 and size_matched / original_size >= 0.95:
                pos["order_status"] = "matched"
                pos["shares"] = size_matched  # Update to actual fill
                changed = True
                fills += 1
                print(f"  [FILL] Order {order_id[:16]}... filled: {size_matched:.2f} shares")
                continue

            try:
                opened = datetime.fromisoformat(pos.get("opened_at", ""))
                age_h = (now - opened).total_seconds() / 3600
            except ValueError:
                age_h = 0.0
            if age_h < live_order_ttl_hours:
                continue

            if size_matched > 0:
                # Partial fill, stale: cancel the remainder, keep what we own,
                # refund the unfilled cost so internal balance matches reality.
                cancel_order(order_id)
                old_cost = float(pos.get("cost", 0.0))
                new_cost = round(size_matched * pos["entry_price"], 2)
                pos["shares"] = size_matched
                pos["cost"] = new_cost
                pos["order_status"] = "matched"
                state["balance"] = round(state["balance"] + old_cost - new_cost, 2)
                save_state(state)
                changed = True
                print(f"  [PARTIAL] Order {order_id[:16]}... kept {size_matched:.2f} shares, "
                      f"refunded ${old_cost - new_cost:.2f}")
            else:
                # Never filled: cancel and refund full cost (handled by
                # close_position's unfilled_cancelled path).
                mkt, state = close_position(
                    mkt, pos["entry_price"], "unfilled_cancelled", state, pos_id, cfg=cfg
                )
                changed = False  # close_position already saved the market

        if changed:
            save_market(mkt)

    return fills


def live_preflight_ok(cfg) -> bool:
    """Return True if this process is allowed to attempt live CLOB trading."""
    if cfg.paper_trading:
        return True

    from core.clob import preflight_live_trading

    ok, reason = preflight_live_trading(check_geoblock=cfg.live_geoblock_check)
    if not ok:
        print(f"  [LIVE BLOCKED] {reason}")
        return False
    return True


def run_once() -> None:
    """Single scan + monitor cycle, then exit. For cron / GitHub Actions."""
    cfg = load_config()
    ensure_dirs()
    calibration = load_calibration()

    if not live_preflight_ok(cfg):
        generate_status(cfg)
        print("[once] live preflight failed; no scan attempted")
        return

    print(f"\n[once] WEATHERBOT — single cycle ({'PAPER' if cfg.paper_trading else 'LIVE'})")

    # Check if any pending GTC orders got filled since last cycle
    fills = check_pending_orders(cfg)
    if fills:
        print(f"[once] {fills} pending order(s) confirmed filled")

    new_pos, closed, res = scan_once(cfg, calibration)
    monitor_loop(cfg, calibration)

    state = load_state(cfg.balance)
    print(
        f"[once] done — balance: ${state['balance']:,.2f} | "
        f"new: {new_pos} | closed: {closed} | resolved: {res}"
    )

    # Health report — flag problem cities
    health = get_city_health(lookback=20)
    flagged = {c: h for c, h in health.items() if h["flagged"]}
    if flagged:
        print(f"\n⚠ FLAGGED CITIES ({len(flagged)}):")
        for city, h in sorted(flagged.items()):
            name = LOCATIONS[city].name if city in LOCATIONS else city
            print(f"  {name:<18} fails: {h['fails']}/{h['total_runs']} "
                  f"({h['fail_rate']:.0%}) | streak: {h['consec_fails']} | "
                  f"last: {h['last_error']}")
        print()

    # Write status report (committed by Actions for visibility)
    generate_status(cfg)
    print("[once] status.md written")


def run_loop() -> None:
    cfg = load_config()
    ensure_dirs()
    calibration = load_calibration()

    if not live_preflight_ok(cfg):
        generate_status(cfg)
        print("Live preflight failed; no scan attempted")
        return

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

    open_pos = [m for m in all_mkts if has_any_open(m)]
    total_open_positions = sum(len(get_open_positions(m)) for m in open_pos)
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
    print(f"  Open:     {total_open_positions} | Resolved: {len(resolved)}")

    if open_pos:
        print(f"\n  Open positions:")
        for m in open_pos:
            for pos in get_open_positions(m).values():
                unit = m.get("unit", "F")
                label = f"{pos['bucket_low']:.0f}–{pos['bucket_high']:.0f}°{unit}"
                src = pos.get("forecast_source", "?").upper()
                side = pos.get("side", "yes").upper()
                print(f"    {m['city_name']:<16} {m['date']} | {side} {label:<14} | "
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
        # Get first position from positions dict (legacy compat)
        positions = m.get("positions", {})
        pos = next(iter(positions.values()), {}) if positions else {}
        snaps = m.get("forecast_snapshots", [])
        fc = snaps[-1].get("best") if snaps else None
        unit = m.get("unit", "F")
        bucket = f"{pos.get('bucket_low'):.0f}–{pos.get('bucket_high'):.0f}°{unit}" if pos else "—"
        outcome = m.get("resolved_outcome", "?").upper()
        pnl_str = f"{'+'if m['pnl']>=0 else ''}{m['pnl']:.2f}" if m.get("pnl") is not None else "—"
        actual = f"actual {m['actual_temp']}°{unit}" if m.get("actual_temp") else ""
        print(f"    {m['city_name']:<16} {m['date']} | {bucket:<14} | {outcome} {pnl_str} {actual}")

    print(f"{'='*55}\n")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd == "run":
        run_loop()
    elif cmd == "once":
        run_once()
    elif cmd == "status":
        print_status()
    elif cmd == "report":
        print_report()
    elif cmd == "health":
        ensure_dirs()
        health = get_city_health(lookback=20)
        print(f"\n{'='*60}")
        print(f"  WEATHERBOT — CITY HEALTH (last 20 runs)")
        print(f"{'='*60}")
        for city in sorted(health):
            h = health[city]
            name = LOCATIONS[city].name if city in LOCATIONS else city
            flag = " ⚠ FLAGGED" if h["flagged"] else ""
            print(f"  {name:<18} ok: {h['total_runs']-h['fails']}/{h['total_runs']} "
                  f"({1-h['fail_rate']:.0%}) | streak_fail: {h['consec_fails']}{flag}")
            if h["last_error"]:
                print(f"    └─ last error: {h['last_error'][:80]}")
        print(f"{'='*60}\n")
    elif cmd == "probe":
        _cfg = load_config()
        ensure_dirs()
        _cal = load_calibration()
        print("Dry-run scan (no positions will be opened)...")
        scan_once(_cfg, _cal, dry_run=True)
    else:
        print("Usage: python main.py [run|once|status|report|health|probe]")
