"""Tests for bankroll/exposure risk helpers."""

from dataclasses import dataclass

from core.risk import can_open_more, cfg_with_remaining_open_budget, total_open_cost


@dataclass(frozen=True)
class DummyConfig:
    max_bet: float = 5.0
    max_total_open_cost: float = 20.0
    max_new_positions_per_run: int = 2


def test_total_open_cost_counts_only_open_positions():
    markets = [
        {
            "positions": {
                "a": {"status": "open", "cost": 5.5},
                "b": {"status": "closed", "cost": 99.0},
            }
        },
        {"positions": {"c": {"status": "open", "cost": 4.25}}},
    ]

    assert total_open_cost(markets) == 9.75


def test_can_open_more_blocks_per_run_cap():
    ok, reason = can_open_more(DummyConfig(), new_positions_this_run=2, open_cost=0.0)

    assert not ok
    assert "new-position cap" in reason


def test_can_open_more_blocks_when_remaining_below_min_order():
    ok, reason = can_open_more(DummyConfig(), new_positions_this_run=0, open_cost=16.25)

    assert not ok
    assert "open exposure cap" in reason


def test_can_open_more_allows_inside_caps():
    ok, reason = can_open_more(DummyConfig(), new_positions_this_run=1, open_cost=10.0)

    assert ok
    assert reason == ""


def test_cfg_with_remaining_open_budget_caps_max_bet():
    cfg = cfg_with_remaining_open_budget(DummyConfig(max_bet=7.0), open_cost=14.5)

    assert cfg.max_bet == 5.5


def test_cfg_with_remaining_open_budget_keeps_uncapped_config():
    cfg = DummyConfig(max_bet=7.0, max_total_open_cost=0.0)

    assert cfg_with_remaining_open_budget(cfg, open_cost=100.0) is cfg
