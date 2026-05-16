"""
Tests for core/monitor.py — check_forecast_change and check_stops_and_tp.

All external I/O (fetch_live_price, close_position, save_market) is mocked.
"""

import pytest
from unittest.mock import patch, MagicMock

from core.monitor import check_forecast_change, check_stops_and_tp


# ── Helpers ───────────────────────────────────────────────────────────────────

def _state(balance: float = 9_980.0) -> dict:
    return {
        "balance":          balance,
        "starting_balance": 10_000.0,
        "total_trades":     1,
        "wins":             0,
        "losses":           0,
        "peak_balance":     10_000.0,
    }


def _mkt(
    bucket_low: float = 70.0,
    bucket_high: float = 73.0,
    entry_price: float = 0.30,
    shares: float = 66.67,
    cost: float = 20.0,
    stop_price: float | None = None,
    trailing_activated: bool = False,
    event_end_date: str = "2099-01-01T00:00:00Z",  # far future = hours > 48
) -> dict:
    if stop_price is None:
        stop_price = round(entry_price * 0.80, 4)
    pos = {
        "market_id":          "mkt-001",
        "question":           "Will NYC be 70-73°F?",
        "bucket_low":         bucket_low,
        "bucket_high":        bucket_high,
        "entry_price":        entry_price,
        "bid_at_entry":       round(entry_price - 0.02, 4),
        "spread":             0.02,
        "shares":             shares,
        "cost":               cost,
        "p":                  0.50,
        "ev":                 0.20,
        "kelly":              0.25,
        "forecast_temp":      71.5,
        "forecast_source":    "ecmwf",
        "sigma":              1.0,
        "stop_price":         stop_price,
        "trailing_activated": trailing_activated,
        "opened_at":          "2025-05-01T10:00:00+00:00",
        "status":             "open",
        "exit_price":         None,
        "close_reason":       None,
        "closed_at":          None,
        "pnl":                None,
    }
    return {
        "city":             "nyc",
        "city_name":        "New York City",
        "date":             "2025-05-01",
        "unit":             "F",
        "status":           "open",
        "event_end_date":   event_end_date,
        "all_outcomes":     [],
        "forecast_snapshots": [],
        "positions": {"mkt-001": pos},
    }


def _fake_close(mkt, exit_price, reason, state, position_id=None, cfg=None):
    """Minimal close_position stand-in used by monitor tests."""
    pos_id = position_id or "mkt-001"
    pos = mkt["positions"][pos_id]
    updated_pos = {**pos, "status": "closed",
                   "exit_price": exit_price, "close_reason": reason, "pnl": 0.0}
    updated_positions = {**mkt["positions"], pos_id: updated_pos}
    return {**mkt, "positions": updated_positions}, state


# ── check_forecast_change ──────────────────────────────────────────────────────

class TestCheckForecastChange:
    """
    Bucket (70, 73), midpoint = 71.5.
    abs(midpoint - t_low) = 1.5, so buffer threshold = 1.5 + 2.0 = 3.5.
    Forecast needs abs(forecast - 71.5) > 3.5 to trigger a close
    (i.e., forecast < 68.0 or forecast > 75.0).
    """

    def test_no_close_when_forecast_in_bucket(self):
        mkt = _mkt()
        state = _state()
        _, _, did_close = check_forecast_change(mkt, state, 72.0, "F")
        assert not did_close

    @patch("core.monitor.fetch_live_price", return_value=(0.30, 0.32))
    def test_no_close_at_exact_bucket_boundary(self, mock_live):
        mkt = _mkt()
        state = _state()
        # 75.0 is exactly at threshold — not strictly greater, so no close
        _, _, did_close = check_forecast_change(mkt, state, 75.0, "F")
        assert not did_close

    @patch("core.monitor.fetch_live_price", return_value=(0.30, 0.32))
    def test_no_close_within_buffer(self, mock_live):
        mkt = _mkt()
        state = _state()
        # 74.9 — outside bucket, close to boundary, still within buffer
        _, _, did_close = check_forecast_change(mkt, state, 74.9, "F")
        assert not did_close

    @patch("core.monitor.close_position", side_effect=_fake_close)
    @patch("core.monitor.fetch_live_price", return_value=(0.18, 0.22))
    def test_close_when_forecast_high(self, mock_live, mock_close):
        mkt = _mkt()
        state = _state()
        # 76 > 75.0 (threshold) → should close
        _, _, did_close = check_forecast_change(mkt, state, 76.0, "F")
        assert did_close

    @patch("core.monitor.close_position", side_effect=_fake_close)
    @patch("core.monitor.fetch_live_price", return_value=(0.18, 0.22))
    def test_close_when_forecast_low(self, mock_live, mock_close):
        mkt = _mkt()
        state = _state()
        # 67 < 68.0 (threshold) → should close
        _, _, did_close = check_forecast_change(mkt, state, 67.0, "F")
        assert did_close

    def test_no_close_when_no_live_price(self):
        mkt = _mkt()
        state = _state()
        with patch("core.monitor.fetch_live_price", return_value=None):
            _, _, did_close = check_forecast_change(mkt, state, 80.0, "F")
        assert not did_close

    @patch("core.monitor.close_position", side_effect=_fake_close)
    @patch("core.monitor.fetch_live_price", return_value=(0.18, 0.22))
    def test_celsius_buffer_is_one_degree(self, mock_live, mock_close):
        """Celsius buffer is 1°C, not 2°F."""
        # Bucket (10, 13), midpoint=11.5, abs(midpoint - t_low)=1.5, threshold=1.5+1.0=2.5
        # close when abs(forecast - 11.5) > 2.5, i.e., forecast > 14 or < 9
        mkt = _mkt(bucket_low=10.0, bucket_high=13.0)
        state = _state()
        _, _, did_close = check_forecast_change(mkt, state, 15.0, "C")
        assert did_close

    def test_edge_bucket_low_closes_when_forecast_clearly_above_ceiling(self):
        """
        Edge bucket (-999, 40): forecast_far = new_forecast > t_high + buffer = 42.
        A forecast of 43°F is clearly above the "or below 40°F" ceiling → close.
        """
        mkt = _mkt(bucket_low=-999.0, bucket_high=40.0)
        state = _state()
        with patch("core.monitor.fetch_live_price", return_value=(0.10, 0.15)):
            with patch("core.monitor.close_position", side_effect=_fake_close):
                _, _, did_close = check_forecast_change(mkt, state, 43.0, "F")
        assert did_close

    def test_edge_bucket_low_no_close_within_buffer(self):
        """
        Edge bucket (-999, 40): forecast = 41°F is above ceiling but within 2°F buffer → hold.
        """
        mkt = _mkt(bucket_low=-999.0, bucket_high=40.0)
        state = _state()
        with patch("core.monitor.fetch_live_price", return_value=(0.10, 0.15)):
            with patch("core.monitor.close_position", side_effect=_fake_close):
                _, _, did_close = check_forecast_change(mkt, state, 41.0, "F")
        assert not did_close

    def test_edge_bucket_high_closes_when_forecast_clearly_below_floor(self):
        """
        Edge bucket (90, 999): forecast_far = new_forecast < t_low - buffer = 88.
        A forecast of 87°F is clearly below the "or above 90°F" floor → close.
        """
        mkt = _mkt(bucket_low=90.0, bucket_high=999.0)
        state = _state()
        with patch("core.monitor.fetch_live_price", return_value=(0.10, 0.15)):
            with patch("core.monitor.close_position", side_effect=_fake_close):
                _, _, did_close = check_forecast_change(mkt, state, 87.0, "F")
        assert did_close


# ── check_stops_and_tp ─────────────────────────────────────────────────────────

class TestCheckStopsAndTp:

    def test_returns_false_when_no_live_price(self):
        mkt = _mkt()
        with patch("core.monitor.fetch_live_price", return_value=None):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert not did_close

    def test_returns_false_when_price_ok(self):
        """Price above stop, below TP — nothing triggered."""
        mkt = _mkt(entry_price=0.30, stop_price=0.24)
        # current_bid=0.50 — above stop (0.24), below TP (0.75, hours>48)
        with patch("core.monitor.fetch_live_price", return_value=(0.50, 0.55)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert not did_close

    @patch("core.monitor.close_position", side_effect=_fake_close)
    def test_stop_loss_triggered(self, mock_close):
        mkt = _mkt(entry_price=0.30, stop_price=0.24)
        with patch("core.monitor.fetch_live_price", return_value=(0.20, 0.22)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close
        _, call_exit, call_reason, _, _ = mock_close.call_args[0]
        assert call_exit == 0.20
        assert call_reason == "stop_loss"

    @patch("core.monitor.save_market")
    def test_trailing_stop_activates_at_20_percent(self, mock_sm):
        """When current_bid >= entry * 1.20, trailing stop moves to breakeven."""
        entry = 0.30
        mkt = _mkt(entry_price=entry, stop_price=round(entry * 0.80, 4))
        # current_bid = 0.36 = entry * 1.20 — exactly at threshold
        with patch("core.monitor.fetch_live_price", return_value=(0.36, 0.38)):
            updated_mkt, _, did_close = check_stops_and_tp(mkt, _state())
        # Trailing activates but price is above new stop (entry=0.30) → no close
        assert not did_close
        mock_sm.assert_called_once()
        assert updated_mkt["positions"]["mkt-001"]["trailing_activated"] is True
        assert updated_mkt["positions"]["mkt-001"]["stop_price"] == pytest.approx(entry, abs=0.0001)

    @patch("core.monitor.close_position", side_effect=_fake_close)
    def test_take_profit_triggered_far_from_resolution(self, mock_close):
        """TP threshold is 0.75 when >48h to resolution (far-future date)."""
        mkt = _mkt(entry_price=0.30, event_end_date="2099-01-01T00:00:00Z")
        with patch("core.monitor.fetch_live_price", return_value=(0.76, 0.78)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close
        _, call_exit, call_reason, _, _ = mock_close.call_args[0]
        assert call_reason == "take_profit"

    @patch("core.monitor.close_position", side_effect=_fake_close)
    def test_take_profit_threshold_48h(self, mock_close):
        """TP threshold is 0.85 when 24-48h to resolution."""
        from datetime import datetime, timedelta, timezone
        # Set end_date to ~36h from now
        future = (datetime.now(timezone.utc) + timedelta(hours=36)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        mkt = _mkt(entry_price=0.30, event_end_date=future)
        # 0.86 >= 0.85 → take profit triggered
        with patch("core.monitor.fetch_live_price", return_value=(0.86, 0.88)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close

    def test_no_take_profit_under_24h(self):
        """Within last 24h, hold to resolution — TP disabled."""
        from datetime import datetime, timedelta, timezone
        future = (datetime.now(timezone.utc) + timedelta(hours=12)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        mkt = _mkt(entry_price=0.30, stop_price=0.24, event_end_date=future)
        # Price at 0.90 — would normally trigger TP but not in final 24h
        with patch("core.monitor.fetch_live_price", return_value=(0.90, 0.92)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert not did_close

    @patch("core.monitor.close_position", side_effect=_fake_close)
    def test_trailing_stop_reason_at_breakeven(self, mock_close):
        """If trailing is activated and price drops to stop (=entry), reason=trailing_stop."""
        entry = 0.30
        mkt = _mkt(entry_price=entry, stop_price=entry, trailing_activated=True)
        # current_bid = entry exactly — stop triggered, but current_bid >= entry → trailing_stop
        with patch("core.monitor.fetch_live_price", return_value=(entry, entry + 0.01)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close
        _, call_exit, call_reason, _, _ = mock_close.call_args[0]
        assert call_reason == "trailing_stop"


# ── NO side tests ──────────────────────────────────────────────────────────────

def _no_mkt(
    bucket_low: float = 80.0,
    bucket_high: float = 83.0,
    entry_price: float = 0.38,   # NO ask = 1 - YES_bid(0.62)
    shares: float = 50.0,
    cost: float = 19.0,
) -> dict:
    """Market record with an open NO position."""
    pos = {
        "market_id":          "mkt-no-001",
        "question":           "Will NYC be 80-83°F?",
        "side":               "no",
        "bucket_low":         bucket_low,
        "bucket_high":        bucket_high,
        "entry_price":        entry_price,
        "bid_at_entry":       round(1.0 - 0.64, 4),
        "spread":             0.02,
        "shares":             shares,
        "cost":               cost,
        "p":                  1.0,
        "ev":                 1.63,
        "kelly":              0.25,
        "forecast_temp":      72.0,
        "forecast_source":    "ecmwf",
        "sigma":              1.0,
        "stop_price":         round(entry_price * 0.30, 4),
        "trailing_activated": False,
        "opened_at":          "2025-05-01T10:00:00+00:00",
        "status":             "open",
        "exit_price":         None,
        "close_reason":       None,
        "closed_at":          None,
        "pnl":                None,
    }
    return {
        "city":             "nyc",
        "city_name":        "New York City",
        "date":             "2025-05-01",
        "unit":             "F",
        "status":           "open",
        "event_end_date":   "2099-01-01T00:00:00Z",
        "all_outcomes":     [],
        "forecast_snapshots": [],
        "positions": {"mkt-no-001": pos},
    }


class TestNoSideMonitor:

    # ── check_stops_and_tp with NO ─────────────────────────────────────────────

    def test_no_stop_loss_uses_no_bid(self):
        """
        For NO, current effective bid = 1 - YES_ask.
        Stop triggers when that falls below stop_price.
        """
        mkt = _no_mkt(entry_price=0.38)
        # stop_price = 0.38 * 0.30 = 0.114
        # YES_ask = 0.90 → NO_bid = 0.10 < stop_price
        with patch("core.monitor.fetch_live_price", return_value=(0.88, 0.90)):
            with patch("core.monitor.close_position", side_effect=_fake_close) as mc:
                _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close
        _, call_exit, call_reason, _, _ = mc.call_args[0]
        assert call_exit == pytest.approx(0.10, abs=0.001)
        assert call_reason == "stop_loss"

    def test_no_take_profit_uses_no_bid(self):
        """TP for NO fires when NO_bid (1 - YES_ask) >= 0.75."""
        mkt = _no_mkt(entry_price=0.38)
        # YES_ask = 0.22 → NO_bid = 0.78 >= TP=0.75
        with patch("core.monitor.fetch_live_price", return_value=(0.20, 0.22)):
            with patch("core.monitor.close_position", side_effect=_fake_close) as mc:
                _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close
        _, call_exit, call_reason, _, _ = mc.call_args[0]
        assert call_reason == "take_profit"

    def test_no_no_action_when_price_mid_range(self):
        """NO_bid in mid-range: above stop (entry*0.30), below TP (entry*1.10) → no action."""
        mkt = _no_mkt(entry_price=0.38)
        # NO_bid = 1 - YES_ask = 1 - 0.65 = 0.35; stop=0.114, TP=0.418
        with patch("core.monitor.fetch_live_price", return_value=(0.33, 0.65)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert not did_close

    # ── check_forecast_change with NO ─────────────────────────────────────────

    def test_no_closes_when_forecast_enters_bucket(self):
        """NO thesis: forecast not in bucket. If it enters, close."""
        mkt = _no_mkt(bucket_low=80.0, bucket_high=83.0)
        # Forecast moves to 81 — now inside the bucket
        with patch("core.monitor.fetch_live_price", return_value=(0.60, 0.62)):
            with patch("core.monitor.close_position", side_effect=_fake_close):
                _, _, did_close = check_forecast_change(mkt, _state(), 81.0, "F")
        assert did_close

    def test_no_stays_when_forecast_outside_bucket(self):
        """Forecast remains far from bucket → keep the NO position."""
        mkt = _no_mkt(bucket_low=80.0, bucket_high=83.0)
        with patch("core.monitor.fetch_live_price", return_value=(0.60, 0.62)):
            _, _, did_close = check_forecast_change(mkt, _state(), 72.0, "F")
        assert not did_close

    # ── check_resolution with NO ──────────────────────────────────────────────

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_no_wins_when_yes_resolves_false(self, mock_sm, mock_ss):
        """YES resolves NO (price→0) → our NO position wins."""
        from core.monitor import check_resolution
        mkt = _no_mkt()
        with patch("core.monitor.check_resolved", return_value=False), \
             patch("core.monitor.get_actual_temp", return_value=None), \
             patch("core.monitor.close_position", side_effect=_fake_close) as mc:
            _, updated_state, did_resolve = check_resolution(mkt, _state(), "key")
        assert did_resolve
        _, call_exit, call_reason, _, _ = mc.call_args[0]
        assert call_exit == 1.0
        assert call_reason == "resolved_win"

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_no_loses_when_yes_resolves_true(self, mock_ss, mock_sm):
        """YES resolves YES (price→1) → our NO position loses."""
        from core.monitor import check_resolution
        mkt = _no_mkt()
        with patch("core.monitor.check_resolved", return_value=True), \
             patch("core.monitor.get_actual_temp", return_value=None), \
             patch("core.monitor.close_position", side_effect=_fake_close) as mc:
            _, updated_state, did_resolve = check_resolution(mkt, _state(), "key")
        assert did_resolve
        _, call_exit, call_reason, _, _ = mc.call_args[0]
        assert call_exit == 0.0
        assert call_reason == "resolved_loss"


class TestAuditBugFixes:
    """Regression tests for bugs found by audit (2026-04-30)."""

    def test_no_tp_capped_at_099(self):
        """C1: NO TP should be capped at 0.99 when entry * 1.10 > 1.0."""
        # entry=0.95 → raw TP = 1.045, should cap to 0.99
        mkt = _no_mkt(entry_price=0.95)
        mkt["positions"]["mkt-no-001"]["stop_price"] = round(0.95 * 0.30, 4)
        # NO_bid = 1 - YES_ask = 1 - 0.02 = 0.98 < 0.99 → no trigger
        with patch("core.monitor.fetch_live_price", return_value=(0.01, 0.02)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert not did_close  # 0.98 < 0.99

    def test_no_tp_fires_at_099(self):
        """C1: NO TP at 0.99 should fire when NO_bid >= 0.99."""
        mkt = _no_mkt(entry_price=0.95)
        mkt["positions"]["mkt-no-001"]["stop_price"] = round(0.95 * 0.30, 4)
        # NO_bid = 1 - YES_ask = 1 - 0.005 = 0.995 >= 0.99 → trigger
        with patch("core.monitor.fetch_live_price", return_value=(0.003, 0.005)):
            with patch("core.monitor.close_position", side_effect=_fake_close) as mc:
                _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close
        _, _, call_reason, _, _ = mc.call_args[0]
        assert call_reason == "take_profit"

    def test_double_close_prevented(self):
        """M2: Closing an already-closed position should be a no-op."""
        mkt = _no_mkt()
        # Manually close the position
        mkt["positions"]["mkt-no-001"]["status"] = "closed"
        mkt["positions"]["mkt-no-001"]["pnl"] = 5.0
        mkt["positions"]["mkt-no-001"]["exit_price"] = 1.0
        # Try to close again via stops — should be skipped
        with patch("core.monitor.fetch_live_price", return_value=(0.95, 0.97)):
            _, _, did_close = check_stops_and_tp(mkt, _state(), position_id="mkt-no-001")
        assert not did_close
