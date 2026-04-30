"""
Position monitoring: stop-loss, trailing stop, take-profit, forecast exits, resolution.

Bug fixes vs bot_v2:
  - Consistent price fetching: always uses bestBid/bestAsk (never outcomePrices).
  - Edge-bucket forecast-change exit fixed: uses bucket midpoint, not forecast_temp itself.
  - Stop price always re-fetched live before triggering.
  - Take-profit thresholds applied based on hours remaining.
"""

from datetime import datetime, timezone
from typing import Any

from core.executor import close_position
from core.forecaster import get_actual_temp
from core.trade_log import append_trade
from core.pricer import in_bucket
from core.scanner import check_resolved, fetch_live_price
from core.storage import load_all_markets, save_market


def check_stops_and_tp(
    mkt: dict[str, Any],
    state: dict[str, Any],
    trailing_activation: float = 1.20,
    position_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Check stop-loss, trailing stop, and take-profit on a single open position.
    Handles both YES and NO sides.

    Returns (updated_mkt, updated_state, did_close).
    """
    positions = mkt.get("positions", {})
    if position_id and position_id in positions:
        pos = positions[position_id]
    elif position_id is None and positions:
        open_pos = {k: v for k, v in positions.items() if v.get("status") == "open"}
        if not open_pos:
            return mkt, state, False
        position_id, pos = next(iter(open_pos.items()))
    else:
        return mkt, state, False

    mid = pos["market_id"]
    side = pos.get("side", "yes")

    live = fetch_live_price(mid)
    if live is None:
        return mkt, state, False

    yes_bid, yes_ask = live
    # For YES: sell at bid. For NO: sell NO = buy YES at ask → NO_bid = 1 - YES_ask
    current_bid = yes_bid if side == "yes" else round(1.0 - yes_ask, 4)
    entry = pos["entry_price"]
    stop = pos.get("stop_price", round(entry * 0.80, 4))

    # Trailing stop: move to breakeven when up sufficiently
    if current_bid >= entry * trailing_activation and not pos.get("trailing_activated", False):
        updated_pos = {**pos, "stop_price": entry, "trailing_activated": True}
        updated_positions = {**mkt.get("positions", {}), position_id: updated_pos}
        updated_mkt = {**mkt, "positions": updated_positions}
        save_market(updated_mkt)
        print(
            f"  [TRAILING] {mkt['city_name']} {mkt['date']} "
            f"— stop moved to breakeven ${entry:.3f}"
        )
        # Re-bind for further checks this call
        mkt = updated_mkt
        pos = updated_pos
        stop = entry

    # Take-profit threshold based on hours to resolution
    end_date = mkt.get("event_end_date", "")
    hours_left = _hours_left(end_date)

    if side == "no":
        # NO tokens resolve to $1.00; take profit relative to entry
        if hours_left < 24:
            take_profit = None      # hold to resolution
        else:
            take_profit = round(entry * 1.10, 4)   # 10% gain on NO cost
    else:
        if hours_left < 24:
            take_profit = None          # hold to resolution
        elif hours_left < 48:
            take_profit = 0.85
        else:
            take_profit = 0.75

    take_triggered = take_profit is not None and current_bid >= take_profit
    stop_triggered = current_bid <= stop

    if not (take_triggered or stop_triggered):
        return mkt, state, False

    if take_triggered:
        reason = "take_profit"
    elif current_bid < entry:
        reason = "stop_loss"
    else:
        reason = "trailing_stop"

    updated_mkt, updated_state = close_position(mkt, current_bid, reason, state, position_id)
    return updated_mkt, updated_state, True


def check_forecast_change(
    mkt: dict[str, Any],
    state: dict[str, Any],
    new_forecast: float,
    unit: str,
    position_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Close position if forecast has invalidated our thesis.
    """
    positions = mkt.get("positions", {})
    if position_id and position_id in positions:
        pos = positions[position_id]
    elif position_id is None and positions:
        open_pos = {k: v for k, v in positions.items() if v.get("status") == "open"}
        if not open_pos:
            return mkt, state, False
        position_id, pos = next(iter(open_pos.items()))
    else:
        return mkt, state, False

    side = pos.get("side", "yes")
    t_low = pos["bucket_low"]
    t_high = pos["bucket_high"]
    buffer = 2.0 if unit == "F" else 1.0

    live = fetch_live_price(pos["market_id"])
    if live is None:
        return mkt, state, False
    yes_bid, yes_ask = live

    if side == "no":
        # Thesis: forecast is NOT in this bucket. Exit if it moves in.
        if not in_bucket(new_forecast, t_low, t_high):
            return mkt, state, False
        current_no_bid = round(1.0 - yes_ask, 4)
        updated_mkt, updated_state = close_position(
            mkt, current_no_bid, "forecast_changed", state, position_id
        )
        return updated_mkt, updated_state, True

    # YES side ────────────────────────────────────────────────────────────────
    # Already in bucket — no action
    if in_bucket(new_forecast, t_low, t_high):
        return mkt, state, False

    # Determine whether the forecast has moved far enough outside the bucket to warrant exit.
    if t_low == -999.0:
        # "X°F or below" — close YES if forecast is clearly ABOVE the upper bound
        forecast_far = new_forecast > t_high + buffer
    elif t_high == 999.0:
        # "X°F or higher" — close YES if forecast is clearly BELOW the lower bound
        forecast_far = new_forecast < t_low - buffer
    else:
        # Middle bucket — close if forecast drifts beyond half-width + buffer from centre
        midpoint = (t_low + t_high) / 2.0
        half_width = (t_high - t_low) / 2.0
        forecast_far = abs(new_forecast - midpoint) > half_width + buffer

    if not forecast_far:
        return mkt, state, False

    updated_mkt, updated_state = close_position(mkt, yes_bid, "forecast_changed", state, position_id)
    return updated_mkt, updated_state, True


def check_resolution(
    mkt: dict[str, Any],
    state: dict[str, Any],
    vc_key: str,
    position_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Check if a market has resolved on Polymarket and record the outcome.
    Also fetches actual temperature from Visual Crossing for calibration.

    Returns (updated_mkt, updated_state, did_resolve).
    """
    positions = mkt.get("positions", {})
    if position_id and position_id in positions:
        pos = positions[position_id]
    elif position_id is None and positions:
        open_pos = {k: v for k, v in positions.items() if v.get("status") == "open"}
        if not open_pos:
            return mkt, state, False
        position_id, pos = next(iter(open_pos.items()))
    else:
        return mkt, state, False

    if pos.get("status") != "open":
        return mkt, state, False

    side = pos.get("side", "yes")
    yes_won = check_resolved(pos["market_id"])
    if yes_won is None:
        return mkt, state, False

    # For NO positions, winning = YES resolved at 0 (NO token pays out)
    won = yes_won if side == "yes" else not yes_won
    exit_price = 1.0 if won else 0.0
    reason = "resolved_win" if won else "resolved_loss"

    updated_mkt, updated_state = close_position(mkt, exit_price, reason, state, position_id)

    # Fetch actual temperature for calibration (non-blocking)
    actual_temp = get_actual_temp(mkt["city"], mkt["date"], vc_key)

    # Check if ALL positions on this market are now closed → mark market resolved
    all_closed = all(
        p.get("status") != "open"
        for p in updated_mkt.get("positions", {}).values()
    )
    if all_closed:
        resolved_mkt = {
            **updated_mkt,
            "status":           "resolved",
            "resolved_outcome": "win" if won else "loss",
            "pnl":              sum(
                p.get("pnl", 0) or 0 for p in updated_mkt["positions"].values()
            ),
            "actual_temp":      actual_temp,
        }
    else:
        resolved_mkt = {**updated_mkt, "actual_temp": actual_temp}

    save_market(resolved_mkt)
    append_trade(resolved_mkt, pos=updated_mkt["positions"][position_id])
    return resolved_mkt, updated_state, True


def _hours_left(end_date_str: str) -> float:
    if not end_date_str:
        return 999.0
    try:
        end = datetime.fromisoformat(end_date_str.replace("Z", "+00:00"))
        return max(0.0, (end - datetime.now(timezone.utc)).total_seconds() / 3600)
    except Exception:
        return 999.0
