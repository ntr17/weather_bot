"""Risk helpers for bankroll and exposure limits."""

from __future__ import annotations

from dataclasses import replace
from typing import Any


MIN_ORDER_SIZE_USDC = 5.0


def total_open_cost(markets: list[dict[str, Any]]) -> float:
    """Return total cost currently deployed in open positions."""
    deployed = 0.0
    for market in markets:
        for pos in market.get("positions", {}).values():
            if pos.get("status") == "open":
                deployed += float(pos.get("cost") or 0.0)
    return round(deployed, 2)


def can_open_more(cfg: Any, new_positions_this_run: int, open_cost: float) -> tuple[bool, str]:
    """Check global per-run and exposure caps before opening another position."""
    max_new = int(getattr(cfg, "max_new_positions_per_run", 0) or 0)
    if max_new > 0 and new_positions_this_run >= max_new:
        return False, f"new-position cap hit: {new_positions_this_run}/{max_new}"

    max_open = float(getattr(cfg, "max_total_open_cost", 0.0) or 0.0)
    if max_open <= 0:
        return True, ""

    remaining = round(max_open - open_cost, 2)
    if remaining < MIN_ORDER_SIZE_USDC:
        return False, f"open exposure cap hit: ${open_cost:.2f}/${max_open:.2f}"

    return True, ""


def cfg_with_remaining_open_budget(cfg: Any, open_cost: float) -> Any:
    """
    Return cfg with max_bet capped to remaining open-exposure budget.

    The executor owns final sizing and min-order checks; this helper prevents a
    new trade from pushing total deployed capital above max_total_open_cost.
    """
    max_open = float(getattr(cfg, "max_total_open_cost", 0.0) or 0.0)
    if max_open <= 0:
        return cfg

    remaining = max(0.0, round(max_open - open_cost, 2))
    capped_max_bet = min(float(getattr(cfg, "max_bet")), remaining)
    if capped_max_bet == getattr(cfg, "max_bet"):
        return cfg
    return replace(cfg, max_bet=round(capped_max_bet, 2))
