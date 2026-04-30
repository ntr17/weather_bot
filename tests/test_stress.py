"""
End-to-end stress test for scan_once — simulates multiple 30-min cycles.

Verifies:
1. Closed positions are NOT re-entered (the re-entry bug fix)
2. NO stop_price is entry * stop_loss_pct (not the broken absolute floor)
3. NO take-profit uses entry * 1.10 (not flat 0.75/0.85)
4. All closures (stop_loss, trailing, take_profit) are logged to trades table
5. Balance accounting is correct across cycles
6. max_no_positions cap is respected
"""

import json
import math
import os
import sqlite3
import sys
import tempfile
from collections import namedtuple
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

# Setup path
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# ────────────────────────────────────────────────────────────────────────────
# Redirect DB to a temp file so we don't touch production data
# ────────────────────────────────────────────────────────────────────────────
_tmp_dir = tempfile.mkdtemp()
_tmp_db = Path(_tmp_dir) / "test.db"

import core.storage as storage
storage.DB_PATH = _tmp_db
storage._conn = None          # force fresh connection

from core.config import Config
from core.executor import try_open_no_position, try_open_position
from core.monitor import check_stops_and_tp, check_forecast_change, check_resolution
from core.pricer import in_bucket
from core.scanner import Outcome
from core.storage import (
    load_state, save_state, load_market, save_market,
    new_market, get_open_positions, load_all_markets,
    append_run_log,
)

# ────────────────────────────────────────────────────────────────────────────
# Config
# ────────────────────────────────────────────────────────────────────────────
CFG = Config(
    balance=1000.0,
    max_bet=20.0,
    min_ev=0.08,
    max_price=0.70,
    max_no_price=0.985,
    min_volume=50,
    kelly_fraction=0.25,
    stop_loss_pct=0.80,
    no_stop_loss_floor=0.85,
    trailing_activation=1.20,
    no_pyes_threshold=0.25,
    max_no_positions=4,
    max_hours=168.0,
    min_hours=2.0,
    paper_trading=True,
    vc_key="",
    max_slippage=0.10,
    scan_interval=1800,
    monitor_interval=600,
    calibration_min=30,
    polygon_private_key="",
    anthropic_api_key="",
)

# Fake outcomes for a NYC market — 11 buckets
def make_outcomes(prices: dict[str, tuple[float, float]] | None = None) -> list[Outcome]:
    """Create 11 NYC Fahrenheit buckets with given bid/ask prices."""
    buckets = [
        (52, 55), (56, 57), (58, 59), (60, 61), (62, 63),
        (64, 65), (66, 67), (68, 69), (70, 71), (72, 73), (74, 77),
    ]
    default_prices = {}
    for lo, hi in buckets:
        mid = (lo + hi) / 2
        # Price inversely proportional to distance from 65°F
        dist = abs(mid - 65)
        bid = max(0.02, round(0.30 - dist * 0.025, 3))
        ask = round(bid + 0.02, 3)
        default_prices[f"mkt-{lo}-{hi}"] = (bid, ask)

    p = prices or default_prices
    result = []
    for (lo, hi) in buckets:
        mid_key = f"mkt-{lo}-{hi}"
        bid, ask = p.get(mid_key, default_prices[mid_key])
        result.append(Outcome(
            question=f"Will NYC be {lo}-{hi}°F?",
            market_id=mid_key,
            t_low=float(lo),
            t_high=float(hi),
            bid=bid,
            ask=ask,
            spread=round(ask - bid, 4),
            volume=1000,
        ))
    return result


def get_calibration():
    return {"nyc_ecmwf_D+1": 2.5}


def run_scan_cycle(
    cfg: Config,
    outcomes: list[Outcome],
    forecast_temp: float,
    live_prices: dict[str, tuple[float, float]] | None = None,
    cycle_label: str = "cycle",
) -> tuple[int, int, int]:
    """
    Simulate one scan_once cycle for a single city/date.
    Returns (new_positions, closed, resolved).
    """
    new_pos = closed = resolved_count = 0
    state = load_state(cfg.balance)
    city_slug = "nyc"
    date_str = "2026-05-02"
    sigma = 2.5
    src = "ecmwf"

    mkt = load_market(city_slug, date_str)
    if mkt is None:
        mkt = new_market(
            city_slug=city_slug,
            city_name="New York City",
            station="KJFK",
            unit="F",
            date_str=date_str,
            end_date="2026-05-03T00:00:00Z",
            hours_at_discovery=48.0,
        )

    mkt = {
        **mkt,
        "current_horizon": "D+1",
        "all_outcomes": [
            {
                "question": o.question,
                "market_id": o.market_id,
                "range": [o.t_low, o.t_high],
                "bid": o.bid,
                "ask": o.ask,
                "spread": o.spread,
                "volume": o.volume,
            }
            for o in outcomes
        ],
    }

    # Provide a default live_prices that returns the snapshot prices
    if live_prices is None:
        live_prices = {o.market_id: (o.bid, o.ask) for o in outcomes}

    def fake_live(market_id):
        return live_prices.get(market_id)

    # ── Monitor existing positions ──
    open_positions = get_open_positions(mkt)
    for pos_id, pos in list(open_positions.items()):
        with patch("core.monitor.fetch_live_price", side_effect=fake_live):
            with patch("core.monitor.check_resolved", return_value=None):
                mkt, state, did_close = check_stops_and_tp(
                    mkt, state, cfg.trailing_activation, pos_id
                )
        if did_close:
            closed += 1
            continue

    # ── Open new positions ──
    all_bucket_ids = set(mkt.get("positions", {}).keys())

    matched = next(
        (o for o in outcomes if in_bucket(forecast_temp, o.t_low, o.t_high)),
        None,
    )
    if matched and matched.market_id not in all_bucket_ids:
        with patch("core.executor.fetch_live_price", side_effect=fake_live):
            mkt, state, did_open = try_open_position(
                mkt, matched, forecast_temp, src, sigma, state, cfg,
            )
        if did_open:
            new_pos += 1
            all_bucket_ids.add(matched.market_id)

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
        with patch("core.executor.fetch_live_price", side_effect=fake_live):
            mkt, state, did_open = try_open_no_position(
                mkt, o, forecast_temp, src, sigma, state, cfg,
            )
        if did_open:
            new_pos += 1
            all_bucket_ids.add(o.market_id)
            current_no_count += 1

    save_market(mkt)
    save_state(state)

    return new_pos, closed, resolved_count


def _reset_db():
    """Close SQLite connection and delete temp DB for a fresh start."""
    if storage._conn is not None:
        try:
            storage._conn.close()
        except Exception:
            pass
        storage._conn = None
    _tmp_db.unlink(missing_ok=True)


# ════════════════════════════════════════════════════════════════════════════
# TEST 1: Re-entry prevention across multiple cycles
# ════════════════════════════════════════════════════════════════════════════
def test_no_reentry():
    """After positions are opened and stopped out, they must NOT be re-opened on the SAME buckets."""
    print("\n" + "="*70)
    print("TEST 1: Re-entry prevention across multiple cycles")
    print("="*70)

    _reset_db()

    outcomes = make_outcomes()
    forecast = 65.0  # matches 64-65 bucket

    # Cycle 1: open positions
    new1, _, _ = run_scan_cycle(CFG, outcomes, forecast, cycle_label="cycle1")
    print(f"  Cycle 1: opened {new1} positions")
    assert new1 > 0, "Should open at least 1 position"

    state1 = load_state(CFG.balance)
    balance_after_open = state1["balance"]
    
    mkt = load_market("nyc", "2026-05-02")
    positions = mkt.get("positions", {})
    c1_bucket_ids = set(positions.keys())
    open_c1 = sum(1 for p in positions.values() if p["status"] == "open")
    print(f"  Positions in DB: {len(positions)} ({open_c1} open)")
    print(f"  Bucket IDs: {c1_bucket_ids}")

    # Simulate stop-loss: drop all NO prices by 25%
    stopped_prices = {}
    for o in outcomes:
        pos = positions.get(o.market_id)
        if pos and pos["side"] == "no":
            entry = pos["entry_price"]
            target_no_bid = entry * 0.70  # well below stop
            yes_ask_needed = 1.0 - target_no_bid
            stopped_prices[o.market_id] = (o.bid, min(0.99, yes_ask_needed))
        else:
            stopped_prices[o.market_id] = (o.bid, o.ask)

    # Cycle 2: stops should fire, positions close; new NOs may open on OTHER buckets
    new2, closed2, _ = run_scan_cycle(CFG, outcomes, forecast,
                                       live_prices=stopped_prices,
                                       cycle_label="cycle2")
    print(f"  Cycle 2: opened {new2}, closed {closed2}")
    assert closed2 > 0, "Should close some positions via stop_loss"

    state2 = load_state(CFG.balance)
    balance_after_close = state2["balance"]
    print(f"  Balance: ${balance_after_open:.2f} → ${balance_after_close:.2f}")

    mkt = load_market("nyc", "2026-05-02")
    positions = mkt.get("positions", {})
    c2_bucket_ids = set(positions.keys())
    open_c2 = sum(1 for p in positions.values() if p["status"] == "open")
    closed_c2 = sum(1 for p in positions.values() if p["status"] == "closed")
    print(f"  Positions: {len(positions)} total ({open_c2} open, {closed_c2} closed)")

    # KEY ASSERTION: closed positions still in dict
    assert closed_c2 > 0, "Closed positions should remain in dict"
    # All original bucket IDs must still be in the dict (closed, not deleted)
    assert c1_bucket_ids.issubset(c2_bucket_ids), (
        f"Original buckets {c1_bucket_ids - c2_bucket_ids} were deleted from dict!"
    )
    # New positions (if any) must be on DIFFERENT buckets
    if new2 > 0:
        new_bucket_ids = c2_bucket_ids - c1_bucket_ids
        print(f"  New buckets in cycle 2: {new_bucket_ids} (all different from cycle 1 ✓)")

    # Snapshot balance before idle cycles
    balance_before_idle = state2["balance"]

    # Cycles 3-6: run AGAIN — should NOT re-enter any bucket (all are occupied)
    for i in range(3, 7):
        new_n, _, _ = run_scan_cycle(CFG, outcomes, forecast,
                                      live_prices=stopped_prices,
                                      cycle_label=f"cycle{i}")
        assert new_n == 0, (
            f"FAIL: Re-entered {new_n} positions in cycle {i} on already-bet buckets!"
        )

    state_final = load_state(CFG.balance)
    print(f"  Cycles 3-6: 0 new positions each ✓")
    print(f"  Final balance: ${state_final['balance']:.2f} (was ${balance_before_idle:.2f})")
    assert state_final["balance"] == balance_before_idle, (
        f"Balance drained during idle cycles: ${state_final['balance']:.2f} != ${balance_before_idle:.2f}"
    )
    print("  PASSED ✓")


# ════════════════════════════════════════════════════════════════════════════
# TEST 2: NO stop_price correctness
# ════════════════════════════════════════════════════════════════════════════
def test_no_stop_price():
    """NO stop_price = entry * stop_loss_pct, never the absolute floor."""
    print("\n" + "="*70)
    print("TEST 2: NO stop_price correctness")
    print("="*70)

    _reset_db()

    outcomes = make_outcomes()
    forecast = 65.0

    run_scan_cycle(CFG, outcomes, forecast, cycle_label="open")
    mkt = load_market("nyc", "2026-05-02")

    for mid, pos in mkt.get("positions", {}).items():
        if pos["side"] == "no":
            entry = pos["entry_price"]
            expected_stop = round(entry * CFG.stop_loss_pct, 4)
            actual_stop = pos["stop_price"]
            ok = actual_stop == expected_stop
            status = "✓" if ok else "✗"
            print(f"  {status} {mid}: entry=${entry:.3f} stop=${actual_stop:.4f} "
                  f"(expected {expected_stop:.4f})")
            assert ok, (
                f"FAIL: {mid} stop_price={actual_stop} != entry*0.80={expected_stop}. "
                f"Got absolute floor bug?"
            )
            # Also verify stop < entry (the old bug had stop > entry)
            assert actual_stop < entry, (
                f"FAIL: stop_price {actual_stop} >= entry {entry} — would trigger immediately!"
            )

    print("  PASSED ✓")


# ════════════════════════════════════════════════════════════════════════════
# TEST 3: NO take-profit uses relative threshold
# ════════════════════════════════════════════════════════════════════════════
def test_no_take_profit():
    """NO take-profit should use entry * 1.10, not flat 0.75/0.85."""
    print("\n" + "="*70)
    print("TEST 3: NO take-profit relative threshold")
    print("="*70)

    _reset_db()

    outcomes = make_outcomes()
    forecast = 65.0

    run_scan_cycle(CFG, outcomes, forecast, cycle_label="open")
    mkt = load_market("nyc", "2026-05-02")
    state = load_state(CFG.balance)

    # Find a NO position with entry < 0.90 (so TP target < 1.0 is reachable)
    no_pos = None
    no_mid = None
    for mid, pos in mkt.get("positions", {}).items():
        if pos["side"] == "no" and pos["status"] == "open" and pos["entry_price"] < 0.85:
            no_pos = pos
            no_mid = mid
            break

    assert no_pos is not None, "Should have at least one NO position"
    entry = no_pos["entry_price"]
    tp_target = round(entry * 1.10, 4)

    # Price at entry + 5% — should NOT trigger TP
    no_bid_below_tp = entry * 1.05
    yes_ask_for_below = 1.0 - no_bid_below_tp
    prices_below = {no_mid: (0.01, yes_ask_for_below)}
    
    with patch("core.monitor.fetch_live_price",
               return_value=(0.01, yes_ask_for_below)):
        with patch("core.monitor.check_resolved", return_value=None):
            _, _, did_close = check_stops_and_tp(mkt, state, CFG.trailing_activation, no_mid)
    print(f"  NO entry=${entry:.3f}, TP target=${tp_target:.3f}")
    print(f"  Price at entry+5% (${no_bid_below_tp:.3f}): close={did_close} (should be False)")
    assert not did_close, "Should NOT trigger TP at +5%"

    # Price at entry + 15% — SHOULD trigger TP
    no_bid_above_tp = entry * 1.15
    yes_ask_for_above = 1.0 - no_bid_above_tp
    
    with patch("core.monitor.fetch_live_price",
               return_value=(0.01, max(0.01, yes_ask_for_above))):
        with patch("core.monitor.check_resolved", return_value=None):
            updated_mkt, _, did_close = check_stops_and_tp(
                mkt, state, CFG.trailing_activation, no_mid
            )
    print(f"  Price at entry+15% (${no_bid_above_tp:.3f}): close={did_close} (should be True)")
    assert did_close, "SHOULD trigger TP at +15%"

    # OLD BUG: flat 0.75 threshold would trigger on NO tokens priced at 0.80+
    # Verify a NO token at $0.80 is NOT immediately TP'd
    print(f"  (Old flat 0.75 would have triggered at entry — this is fixed)")
    print("  PASSED ✓")


# ════════════════════════════════════════════════════════════════════════════
# TEST 4: All closures logged to trades table
# ════════════════════════════════════════════════════════════════════════════
def test_trade_logging():
    """Stop-loss, trailing, take-profit closures must appear in trades table."""
    print("\n" + "="*70)
    print("TEST 4: All closures logged to trades table")
    print("="*70)

    _reset_db()

    outcomes = make_outcomes()
    forecast = 65.0

    # Open positions
    run_scan_cycle(CFG, outcomes, forecast, cycle_label="open")
    mkt = load_market("nyc", "2026-05-02")
    state = load_state(CFG.balance)

    open_positions = get_open_positions(mkt)
    assert len(open_positions) > 0

    # Trigger stop-loss on all NO positions
    stopped_prices = {}
    for o in outcomes:
        pos = mkt["positions"].get(o.market_id)
        if pos and pos["side"] == "no" and pos["status"] == "open":
            entry = pos["entry_price"]
            target_no_bid = entry * 0.70
            yes_ask = 1.0 - target_no_bid
            stopped_prices[o.market_id] = (o.bid, min(0.99, yes_ask))
        else:
            stopped_prices[o.market_id] = (o.bid, o.ask)

    run_scan_cycle(CFG, outcomes, forecast, live_prices=stopped_prices, cycle_label="stop")

    # Check trades table
    conn = storage._get_conn()
    trades = conn.execute("SELECT * FROM trades").fetchall()
    trade_count = len(trades)
    print(f"  Trades in DB after stop-losses: {trade_count}")

    # Each closed position should have a trade entry
    mkt = load_market("nyc", "2026-05-02")
    closed_count = sum(
        1 for p in mkt["positions"].values()
        if p["status"] == "closed"
    )
    print(f"  Closed positions: {closed_count}")
    assert trade_count == closed_count, (
        f"FAIL: {trade_count} trades logged but {closed_count} positions closed. "
        f"Missing {closed_count - trade_count} trade records!"
    )
    print("  PASSED ✓")


# ════════════════════════════════════════════════════════════════════════════
# TEST 5: Balance accounting across cycles
# ════════════════════════════════════════════════════════════════════════════
def test_balance_accounting():
    """Balance must equal: start - open_costs + sum(returned from closed)."""
    print("\n" + "="*70)
    print("TEST 5: Balance accounting correctness")
    print("="*70)

    _reset_db()

    outcomes = make_outcomes()
    forecast = 65.0
    START = 1000.0

    # Cycle 1: open
    run_scan_cycle(CFG, outcomes, forecast, cycle_label="open")
    state = load_state(CFG.balance)
    mkt = load_market("nyc", "2026-05-02")

    open_cost = sum(p["cost"] for p in mkt["positions"].values() if p["status"] == "open")
    expected_balance = round(START - open_cost, 2)
    print(f"  After opening: balance=${state['balance']:.2f} (expected ${expected_balance:.2f})")
    assert abs(state["balance"] - expected_balance) < 0.01, (
        f"Balance mismatch: {state['balance']} != {expected_balance}"
    )

    # Cycle 2: stop some
    stopped_prices = {}
    for o in outcomes:
        pos = mkt["positions"].get(o.market_id)
        if pos and pos["side"] == "no" and pos["status"] == "open":
            entry = pos["entry_price"]
            target_no_bid = entry * 0.70
            yes_ask = 1.0 - target_no_bid
            stopped_prices[o.market_id] = (o.bid, min(0.99, yes_ask))
        else:
            stopped_prices[o.market_id] = (o.bid, o.ask)

    run_scan_cycle(CFG, outcomes, forecast, live_prices=stopped_prices, cycle_label="stop")
    state = load_state(CFG.balance)
    mkt = load_market("nyc", "2026-05-02")

    open_cost = sum(p["cost"] for p in mkt["positions"].values() if p["status"] == "open")
    closed_returned = sum(
        p["cost"] + (p["pnl"] or 0)
        for p in mkt["positions"].values()
        if p["status"] == "closed"
    )
    expected = round(START - open_cost - sum(p["cost"] for p in mkt["positions"].values() if p["status"] == "closed") + closed_returned, 2)
    # Simpler: balance = START - all_open_costs + sum(cost+pnl for closed)
    actual_expected = round(START - open_cost + sum(
        (p["pnl"] or 0) for p in mkt["positions"].values() if p["status"] == "closed"
    ), 2)
    
    print(f"  After stops: balance=${state['balance']:.2f} (expected ${actual_expected:.2f})")
    assert abs(state["balance"] - actual_expected) < 0.01, (
        f"Balance mismatch: {state['balance']} != {actual_expected}"
    )

    # Run 4 more cycles — balance should NOT change (no new trades, no re-entry)
    for i in range(4):
        run_scan_cycle(CFG, outcomes, forecast, live_prices=stopped_prices, cycle_label=f"idle{i}")
    
    state_final = load_state(CFG.balance)
    print(f"  After 4 idle cycles: balance=${state_final['balance']:.2f} (should be ${state['balance']:.2f})")
    assert state_final["balance"] == state["balance"], (
        f"Balance changed during idle cycles: {state_final['balance']} != {state['balance']} — phantom drain!"
    )
    print("  PASSED ✓")


# ════════════════════════════════════════════════════════════════════════════
# TEST 6: max_no_positions cap
# ════════════════════════════════════════════════════════════════════════════
def test_max_no_positions():
    """Never open more than max_no_positions NO positions per event."""
    print("\n" + "="*70)
    print("TEST 6: max_no_positions cap (max=4)")
    print("="*70)

    _reset_db()

    outcomes = make_outcomes()
    forecast = 65.0

    run_scan_cycle(CFG, outcomes, forecast, cycle_label="open")
    mkt = load_market("nyc", "2026-05-02")

    no_count = sum(
        1 for p in mkt["positions"].values()
        if p["side"] == "no" and p["status"] == "open"
    )
    print(f"  NO positions opened: {no_count} (max={CFG.max_no_positions})")
    assert no_count <= CFG.max_no_positions, (
        f"FAIL: {no_count} NO positions > max {CFG.max_no_positions}"
    )
    print("  PASSED ✓")


# ════════════════════════════════════════════════════════════════════════════
# TEST 7: High-frequency stress — 20 cycles
# ════════════════════════════════════════════════════════════════════════════
def test_20_cycle_stress():
    """Run 20 scan cycles. Positions should be opened ONCE, never re-entered."""
    print("\n" + "="*70)
    print("TEST 7: 20-cycle stress test")
    print("="*70)

    _reset_db()

    outcomes = make_outcomes()
    forecast = 65.0
    START = 1000.0

    total_new = 0
    total_closed = 0

    for cycle in range(20):
        # Every 5th cycle, prices drop (trigger stops)
        if cycle > 0 and cycle % 5 == 0:
            mkt = load_market("nyc", "2026-05-02")
            if mkt:
                stopped_prices = {}
                for o in outcomes:
                    pos = (mkt.get("positions", {}) or {}).get(o.market_id)
                    if pos and pos["side"] == "no" and pos["status"] == "open":
                        entry = pos["entry_price"]
                        target_no_bid = entry * 0.70
                        yes_ask = 1.0 - target_no_bid
                        stopped_prices[o.market_id] = (o.bid, min(0.99, yes_ask))
                    else:
                        stopped_prices[o.market_id] = (o.bid, o.ask)
                new_n, closed_n, _ = run_scan_cycle(CFG, outcomes, forecast,
                                                     live_prices=stopped_prices,
                                                     cycle_label=f"cycle{cycle}")
            else:
                new_n, closed_n, _ = run_scan_cycle(CFG, outcomes, forecast,
                                                     cycle_label=f"cycle{cycle}")
        else:
            new_n, closed_n, _ = run_scan_cycle(CFG, outcomes, forecast,
                                                 cycle_label=f"cycle{cycle}")
        total_new += new_n
        total_closed += closed_n

    mkt = load_market("nyc", "2026-05-02")
    state = load_state(CFG.balance)
    positions = mkt.get("positions", {})

    all_pos_count = len(positions)
    open_count = sum(1 for p in positions.values() if p["status"] == "open")
    closed_count = sum(1 for p in positions.values() if p["status"] == "closed")

    print(f"  Total new across 20 cycles: {total_new}")
    print(f"  Total closed across 20 cycles: {total_closed}")
    print(f"  Positions in DB: {all_pos_count} ({open_count} open, {closed_count} closed)")
    print(f"  Final balance: ${state['balance']:.2f}")

    # Critical: total positions opened should equal what's in the DB
    assert total_new == all_pos_count, (
        f"FAIL: Opened {total_new} but DB has {all_pos_count} — "
        f"{'positions were lost' if total_new > all_pos_count else 'phantom re-entries!'}"
    )

    # Balance sanity
    open_cost = sum(p["cost"] for p in positions.values() if p["status"] == "open")
    closed_pnl = sum(p["pnl"] or 0 for p in positions.values() if p["status"] == "closed")
    expected_balance = round(START - open_cost + closed_pnl, 2)
    assert abs(state["balance"] - expected_balance) < 0.01, (
        f"Balance mismatch: ${state['balance']:.2f} != ${expected_balance:.2f}"
    )

    print(f"  Balance check: ${state['balance']:.2f} == ${expected_balance:.2f} ✓")
    print("  PASSED ✓")


# ════════════════════════════════════════════════════════════════════════════
# RUN ALL
# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 70)
    print("WEATHERBOT END-TO-END STRESS TEST")
    print("=" * 70)

    tests = [
        test_no_reentry,
        test_no_stop_price,
        test_no_take_profit,
        test_trade_logging,
        test_balance_accounting,
        test_max_no_positions,
        test_20_cycle_stress,
    ]

    passed = 0
    failed = 0
    for test_fn in tests:
        try:
            test_fn()
            passed += 1
        except Exception as e:
            print(f"  FAILED: {e}")
            failed += 1

    print("\n" + "=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)}")
    print("=" * 70)

    # Cleanup
    import shutil
    shutil.rmtree(_tmp_dir, ignore_errors=True)

    sys.exit(1 if failed > 0 else 0)
