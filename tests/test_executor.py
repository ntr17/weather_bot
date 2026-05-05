"""
Tests for core/executor.py â€” close_position, try_open_position, try_open_no_position.

All external I/O (save_market, save_state, fetch_live_price) is mocked.
"""

import pytest
from unittest.mock import patch, MagicMock

from core.config import Config
from core.executor import close_position, try_open_no_position, try_open_position
from core.scanner import Outcome


# â”€â”€ Helpers â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def _state(balance: float = 10_000.0, total_trades: int = 0) -> dict:
    return {
        "balance":          balance,
        "starting_balance": 10_000.0,
        "total_trades":     total_trades,
        "wins":             0,
        "losses":           0,
        "peak_balance":     balance,
    }


def _mkt(
    entry_price: float = 0.30,
    shares: float = 66.6667,
    cost: float = 20.0,
    stop_price: float = 0.24,
) -> dict:
    pos = {
        "market_id":          "mkt-001",
        "question":           "Will NYC be 70-71Â°F?",
        "bucket_low":         70.0,
        "bucket_high":        71.0,
        "entry_price":        entry_price,
        "bid_at_entry":       round(entry_price - 0.02, 4),
        "spread":             0.02,
        "shares":             shares,
        "cost":               cost,
        "p":                  0.45,
        "ev":                 0.15,
        "kelly":              0.25,
        "forecast_temp":      70.5,
        "forecast_source":    "ecmwf",
        "sigma":              3.0,
        "stop_price":         stop_price,
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
        "current_horizon":  "D+1",
        "event_end_date":   "2025-05-02T00:00:00Z",
        "all_outcomes":     [],
        "forecast_snapshots": [],
        "positions": {"mkt-001": pos},
    }


def _cfg(**overrides) -> Config:
    defaults = dict(
        balance=10_000.0,
        max_bet=20.0,
        min_ev=0.10,
        max_price=0.60,
        max_no_price=0.97,
        min_volume=500.0,
        min_hours=2.0,
        max_hours=72.0,
        kelly_fraction=0.25,
        max_slippage=0.05,
        stop_loss_pct=0.80,
        no_stop_loss_pct=0.30,
        no_stop_loss_floor=0.85,
        trailing_activation=1.20,
        no_pyes_threshold=0.15,
        max_no_positions=4,
        min_yes_price=0.05,
        enable_yes_trading=True,
        min_no_entry=0.10,
        max_no_entry=0.97,
        no_stop_enabled=True,
        no_forecast_exit=True,
        max_horizon_days=6,
        scan_interval=3600,
        monitor_interval=600,
        calibration_min=20,
        vc_key="test_key",
        polygon_private_key="",
        anthropic_api_key="",
        paper_trading=True,
    )
    defaults.update(overrides)
    return Config(**defaults)


def _outcome(**overrides) -> Outcome:
    """
    Baseline outcome: EV positive (pâ‰ˆ0.38 from sigma=1.0, ask=0.15).
    bucket (70, 73), forecast 72, sigma 1.0:
      bucket_prob â‰ˆ Phi((73-72)/1) - Phi((70-72)/1) â‰ˆ 0.841 - 0.023 = 0.818
      EV = 0.818 - 0.15 = 0.668 >> 0.10
    """
    defaults = dict(
        question="Will NYC be 70-73Â°F?",
        market_id="mkt-002",
        t_low=70.0,
        t_high=73.0,
        bid=0.13,
        ask=0.15,
        spread=0.02,
        volume=1000.0,
    )
    defaults.update(overrides)
    return Outcome(**defaults)


# â”€â”€ close_position â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

class TestClosePosition:

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_win_pnl(self, mock_sm, mock_ss):
        mkt = _mkt(entry_price=0.30, shares=66.6667, cost=20.0)
        state = _state(balance=9_980.0)

        updated_mkt, _ = close_position(mkt, 1.0, "resolved_win", state)

        pos = updated_mkt["positions"]["mkt-001"]
        # (1.0 - 0.30) * 66.6667 = 46.67
        assert pos["pnl"] == pytest.approx(46.67, abs=0.01)
        assert pos["exit_price"] == 1.0
        assert pos["status"] == "closed"
        assert pos["close_reason"] == "resolved_win"

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_loss_pnl(self, mock_sm, mock_ss):
        mkt = _mkt(entry_price=0.30, shares=66.6667, cost=20.0)
        state = _state(balance=9_980.0)

        updated_mkt, _ = close_position(mkt, 0.0, "resolved_loss", state)

        # (0.0 - 0.30) * 66.6667 = -20.0
        assert updated_mkt["positions"]["mkt-001"]["pnl"] == pytest.approx(-20.0, abs=0.01)

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_balance_restored_on_win(self, mock_sm, mock_ss):
        mkt = _mkt(entry_price=0.30, shares=66.6667, cost=20.0)
        state = _state(balance=9_980.0)

        _, updated_state = close_position(mkt, 1.0, "resolved_win", state)

        # balance + cost + pnl = 9980 + 20 + 46.67 = 10046.67
        assert updated_state["balance"] == pytest.approx(10046.67, abs=0.02)

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_balance_full_loss(self, mock_sm, mock_ss):
        mkt = _mkt(entry_price=0.30, shares=66.6667, cost=20.0)
        state = _state(balance=9_980.0)

        _, updated_state = close_position(mkt, 0.0, "resolved_loss", state)

        # balance + cost + pnl = 9980 + 20 + (-20) = 9980
        assert updated_state["balance"] == pytest.approx(9_980.0, abs=0.01)

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_partial_exit_pnl(self, mock_sm, mock_ss):
        mkt = _mkt(entry_price=0.30, shares=100.0, cost=30.0)
        state = _state(balance=9_970.0)

        updated_mkt, updated_state = close_position(mkt, 0.75, "take_profit", state)

        # (0.75 - 0.30) * 100 = 45.0
        assert updated_mkt["positions"]["mkt-001"]["pnl"] == pytest.approx(45.0, abs=0.01)
        # balance + cost + pnl = 9970 + 30 + 45 = 10045
        assert updated_state["balance"] == pytest.approx(10_045.0, abs=0.01)

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_saves_called(self, mock_sm, mock_ss):
        close_position(_mkt(), 0.5, "stop_loss", _state())
        mock_sm.assert_called_once()
        mock_ss.assert_called_once()

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_peak_balance_updated(self, mock_sm, mock_ss):
        mkt = _mkt(entry_price=0.30, shares=100.0, cost=30.0)
        state = _state(balance=9_970.0)
        state["peak_balance"] = 9_970.0

        _, updated_state = close_position(mkt, 1.0, "resolved_win", state)

        # balance after win = 9970 + 30 + 70 = 10070 â€” above old peak
        assert updated_state["peak_balance"] >= 10_070.0


# â”€â”€ try_open_position â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

class TestTryOpenPosition:

    def _run(self, outcome=None, cfg=None, forecast_temp=72.0, sigma=1.0,
             live_price=(0.13, 0.15)):
        """Helper: run try_open_position with mocked I/O."""
        outcome = outcome or _outcome()
        cfg = cfg or _cfg()
        state = _state()
        mkt = {
            "city":             "nyc",
            "city_name":        "New York City",
            "date":             "2025-05-01",
            "unit":             "F",
            "status":           "open",
            "current_horizon":  "D+1",
            "all_outcomes":     [],
            "forecast_snapshots": [],
        }
        with patch("core.executor.fetch_live_price", return_value=live_price), \
             patch("core.executor.save_market"), \
             patch("core.executor.save_state"):
            return try_open_position(
                mkt, outcome, forecast_temp, "ecmwf", sigma, state, cfg
            )

    def test_rejects_below_min_ev(self):
        # ask=0.80 with pâ‰ˆ0.82 â†’ EV = 0.02 < 0.10
        outcome = _outcome(ask=0.80, bid=0.78, spread=0.02)
        _, _, opened = self._run(outcome=outcome)
        assert not opened

    def test_rejects_above_max_price(self):
        # ask above max_price=0.60
        outcome = _outcome(ask=0.65, bid=0.63, spread=0.02)
        _, _, opened = self._run(outcome=outcome, live_price=(0.63, 0.65))
        assert not opened

    def test_rejects_below_min_volume(self):
        outcome = _outcome(volume=100.0)  # < min_volume=500
        _, _, opened = self._run(outcome=outcome)
        assert not opened

    def test_rejects_above_max_slippage(self):
        outcome = _outcome(bid=0.08, ask=0.15, spread=0.07)  # > max_slippage=0.05
        _, _, opened = self._run(outcome=outcome)
        assert not opened

    def test_rejects_live_price_too_high(self):
        # snapshot ok, but live ask is above max_price=0.60
        outcome = _outcome()
        _, _, opened = self._run(outcome=outcome, live_price=(0.58, 0.62))
        assert not opened

    def test_rejects_live_spread_too_wide(self):
        outcome = _outcome()
        _, _, opened = self._run(outcome=outcome, live_price=(0.08, 0.15))
        # spread = 0.15 - 0.08 = 0.07 > max_slippage=0.05
        assert not opened

    def test_opens_position_on_good_market(self):
        _, _, opened = self._run()
        assert opened

    def test_balance_debited_on_open(self):
        _, updated_state, opened = self._run()
        assert opened
        assert updated_state["balance"] < 10_000.0

    def test_trade_count_incremented(self):
        _, updated_state, opened = self._run()
        assert opened
        assert updated_state["total_trades"] == 1

    def test_position_fields_recorded(self):
        updated_mkt, _, opened = self._run(forecast_temp=72.0, sigma=1.0)
        assert opened
        pos = updated_mkt["positions"]["mkt-002"]
        assert pos["bucket_low"] == 70.0
        assert pos["bucket_high"] == 73.0
        assert pos["status"] == "open"
        assert pos["entry_price"] == pytest.approx(0.15, abs=0.001)
        assert pos["forecast_temp"] == 72.0
        assert pos["forecast_source"] == "ecmwf"
        assert pos["stop_price"] == pytest.approx(0.15 * 0.80, abs=0.001)

    def test_no_live_price_falls_back_to_snapshot(self):
        """When fetch_live_price returns None, uses snapshot ask â€” still may open."""
        outcome = _outcome()
        state = _state()
        mkt = {
            "city": "nyc", "city_name": "New York City",
            "date": "2025-05-01", "unit": "F",
            "status": "open", "current_horizon": "D+1",
            "all_outcomes": [], "forecast_snapshots": [],
        }
        with patch("core.executor.fetch_live_price", return_value=None), \
             patch("core.executor.save_market"), \
             patch("core.executor.save_state"):
            _, _, opened = try_open_position(
                mkt, outcome, 72.0, "ecmwf", 1.0, state, _cfg()
            )
        # Falls back to snapshot bid/ask â€” same values, so should open
        assert opened

    @patch("core.executor.save_state")
    @patch("core.executor.save_market")
    def test_yes_position_has_side_field(self, mock_sm, mock_ss):
        """YES positions must record side='yes' for monitor side-awareness."""
        outcome = _outcome()
        mkt = {
            "city": "nyc", "city_name": "New York City",
            "date": "2025-05-01", "unit": "F",
            "status": "open", "current_horizon": "D+1",
            "all_outcomes": [], "forecast_snapshots": [],
        }
        with patch("core.executor.fetch_live_price", return_value=(0.13, 0.15)):
            updated_mkt, _, opened = try_open_position(
                mkt, outcome, 72.0, "ecmwf", 1.0, _state(), _cfg()
            )
        assert opened
        assert updated_mkt["positions"]["mkt-002"]["side"] == "yes"


# â”€â”€ try_open_no_position â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

class TestTryOpenNoPosition:
    """
    Baseline NO scenario:
      Forecast = 72Â°F, bucket = 80â€“83Â°F (far away â†’ p_yes = 0, p_no = 1)
      YES_bid = 0.62 â†’ NO_ask = 1 - 0.62 = 0.38 < max_price=0.45
      EV_no = 1.0 * (1/0.38 - 1) - 0 = 1.63 >> min_ev=0.10
    """

    _NO_OUTCOME = dict(
        question="Will NYC be 80-83Â°F?",
        market_id="mkt-no-001",
        t_low=80.0,
        t_high=83.0,
        bid=0.62,   # YES_bid high â†’ market overpricing this bucket
        ask=0.64,
        spread=0.02,
        volume=1000.0,
    )

    def _base_mkt(self) -> dict:
        return {
            "city": "nyc", "city_name": "New York City",
            "date": "2025-05-01", "unit": "F",
            "status": "open", "current_horizon": "D+1",
            "all_outcomes": [], "forecast_snapshots": [],
        }

    def _run(self, outcome_kwargs=None, cfg=None, forecast_temp=72.0, sigma=1.0,
             live_price=(0.62, 0.64)):
        outcome = Outcome(**(self._NO_OUTCOME | (outcome_kwargs or {})))
        cfg = cfg or _cfg()
        with patch("core.executor.fetch_live_price", return_value=live_price), \
             patch("core.executor.save_market"), \
             patch("core.executor.save_state"):
            return try_open_no_position(
                self._base_mkt(), outcome, forecast_temp, "ecmwf", sigma, _state(), cfg
            )

    def test_opens_when_overpriced(self):
        _, _, opened = self._run()
        assert opened

    def test_side_is_no(self):
        updated_mkt, _, opened = self._run()
        assert opened
        assert updated_mkt["positions"]["mkt-no-001"]["side"] == "no"

    def test_entry_price_is_one_minus_yes_bid(self):
        # live YES_bid = 0.62 â†’ NO_ask = 0.38
        updated_mkt, _, opened = self._run(live_price=(0.62, 0.64))
        assert opened
        assert updated_mkt["positions"]["mkt-no-001"]["entry_price"] == pytest.approx(0.38, abs=0.001)

    def test_balance_debited(self):
        _, updated_state, opened = self._run()
        assert opened
        assert updated_state["balance"] < 10_000.0

    def test_rejects_when_p_yes_above_threshold(self):
        # Forecast 81Â°F â€” squarely in 80-83 bucket â†’ p_yes=1.0 > 0.15
        _, _, opened = self._run(forecast_temp=81.0)
        assert not opened

    def test_rejects_when_no_ask_above_max_no_price(self):
        # YES_bid = 0.02 â†’ NO_ask = 1 - 0.02 = 0.98 >= max_no_price=0.97
        _, _, opened = self._run(live_price=(0.02, 0.04))
        assert not opened

    def test_rejects_below_min_volume(self):
        _, _, opened = self._run(outcome_kwargs={"volume": 100.0})
        assert not opened

    def test_rejects_wide_spread(self):
        _, _, opened = self._run(outcome_kwargs={"bid": 0.55, "ask": 0.65, "spread": 0.10})
        assert not opened

    def test_no_ev_positive(self):
        # Sanity: with p_no=1.0 and NO_ask=0.38, EV should be very high
        updated_mkt, _, opened = self._run()
        assert opened
        assert updated_mkt["positions"]["mkt-no-001"]["ev"] > 0.10

    def test_no_stop_uses_entry_pct(self):
        """NO stop_price should use entry * no_stop_loss_pct (wider than YES)."""
        updated_mkt, _, opened = self._run()
        assert opened
        entry = updated_mkt["positions"]["mkt-no-001"]["entry_price"]
        expected = round(entry * 0.30, 4)
        assert updated_mkt["positions"]["mkt-no-001"]["stop_price"] == expected
