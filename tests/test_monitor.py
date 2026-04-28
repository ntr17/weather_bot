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
    return {
        "city":             "nyc",
        "city_name":        "New York City",
        "date":             "2025-05-01",
        "unit":             "F",
        "status":           "open",
        "event_end_date":   event_end_date,
        "all_outcomes":     [],
        "forecast_snapshots": [],
        "position": {
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
        },
    }


def _fake_close(mkt, exit_price, reason, state):
    """Minimal close_position stand-in used by monitor tests."""
    updated_pos = {**mkt["position"], "status": "closed",
                   "exit_price": exit_price, "close_reason": reason, "pnl": 0.0}
    return {**mkt, "position": updated_pos}, state


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

    def test_no_close_at_exact_bucket_boundary(self):
        mkt = _mkt()
        state = _state()
        # 75.0 is exactly at threshold — not strictly greater, so no close
        _, _, did_close = check_forecast_change(mkt, state, 75.0, "F")
        assert not did_close

    def test_no_close_within_buffer(self):
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

    def test_edge_bucket_low_never_closes(self):
        """
        Edge bucket (-999, 40): midpoint = 40 - 2 = 38.
        abs(midpoint - t_low) = abs(38 - (-999)) ≈ 1037.
        Even a forecast of 999 doesn't exceed threshold 1039.
        This is intentional — edge buckets don't get forecast-change exits.
        """
        mkt = _mkt(bucket_low=-999.0, bucket_high=40.0)
        state = _state()
        with patch("core.monitor.fetch_live_price", return_value=(0.10, 0.15)):
            with patch("core.monitor.close_position", side_effect=_fake_close):
                _, _, did_close = check_forecast_change(mkt, state, 999.0, "F")
        assert not did_close


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
        _, call_exit, call_reason, _ = mock_close.call_args[0]
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
        assert updated_mkt["position"]["trailing_activated"] is True
        assert updated_mkt["position"]["stop_price"] == pytest.approx(entry, abs=0.0001)

    @patch("core.monitor.close_position", side_effect=_fake_close)
    def test_take_profit_triggered_far_from_resolution(self, mock_close):
        """TP threshold is 0.75 when >48h to resolution (far-future date)."""
        mkt = _mkt(entry_price=0.30, event_end_date="2099-01-01T00:00:00Z")
        with patch("core.monitor.fetch_live_price", return_value=(0.76, 0.78)):
            _, _, did_close = check_stops_and_tp(mkt, _state())
        assert did_close
        _, call_exit, call_reason, _ = mock_close.call_args[0]
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
        _, call_exit, call_reason, _ = mock_close.call_args[0]
        assert call_reason == "trailing_stop"
