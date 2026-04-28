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
from core.pricer import in_bucket
from core.scanner import check_resolved, fetch_live_price
from core.storage import load_all_markets, save_market


def check_stops_and_tp(
    mkt: dict[str, Any],
    state: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Check stop-loss, trailing stop, and take-profit on a single open position.

    Returns (updated_mkt, updated_state, did_close).
    """
    pos = mkt["position"]
    mid = pos["market_id"]

    live = fetch_live_price(mid)
    if live is None:
        return mkt, state, False

    current_bid, _ = live
    entry = pos["entry_price"]
    stop = pos.get("stop_price", round(entry * 0.80, 4))

    # Trailing stop: move to breakeven when up 20%
    if current_bid >= entry * 1.20 and not pos.get("trailing_activated", False):
        updated_pos = {**pos, "stop_price": entry, "trailing_activated": True}
        updated_mkt = {**mkt, "position": updated_pos}
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

    return close_position(mkt, current_bid, reason, state) + (True,)


def check_forecast_change(
    mkt: dict[str, Any],
    state: dict[str, Any],
    new_forecast: float,
    unit: str,
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Close position if forecast has moved significantly outside the bucket.

    Bug fix vs v2: midpoint is now computed from the bucket itself, not from
    forecast_temp (which caused exits to never trigger on edge buckets).

    Buffer: 2°F / 1°C — prevents thrashing on small forecast wiggles.
    """
    pos = mkt["position"]
    t_low = pos["bucket_low"]
    t_high = pos["bucket_high"]
    buffer = 2.0 if unit == "F" else 1.0

    # Already in bucket — no action
    if in_bucket(new_forecast, t_low, t_high):
        return mkt, state, False

    # Compute bucket midpoint for edge buckets
    if t_low == -999.0:
        midpoint = t_high - buffer
    elif t_high == 999.0:
        midpoint = t_low + buffer
    else:
        midpoint = (t_low + t_high) / 2.0

    # Only close if forecast is beyond midpoint + buffer from the bucket
    forecast_far = abs(new_forecast - midpoint) > (abs(midpoint - t_low) + buffer)
    if not forecast_far:
        return mkt, state, False

    live = fetch_live_price(pos["market_id"])
    if live is None:
        return mkt, state, False

    current_bid, _ = live
    return close_position(mkt, current_bid, "forecast_changed", state) + (True,)


def check_resolution(
    mkt: dict[str, Any],
    state: dict[str, Any],
    vc_key: str,
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Check if a market has resolved on Polymarket and record the outcome.
    Also fetches actual temperature from Visual Crossing for calibration.

    Returns (updated_mkt, updated_state, did_resolve).
    """
    pos = mkt.get("position")
    if not pos or pos.get("status") != "open":
        return mkt, state, False

    won = check_resolved(pos["market_id"])
    if won is None:
        return mkt, state, False

    exit_price = 1.0 if won else 0.0
    reason = "resolved_win" if won else "resolved_loss"

    updated_mkt, updated_state = close_position(mkt, exit_price, reason, state)

    # Update win/loss counter
    if won:
        updated_state = {**updated_state, "wins": updated_state.get("wins", 0) + 1}
    else:
        updated_state = {**updated_state, "losses": updated_state.get("losses", 0) + 1}

    # Fetch actual temperature for calibration (non-blocking)
    actual_temp = get_actual_temp(mkt["city"], mkt["date"], vc_key)
    resolved_mkt = {
        **updated_mkt,
        "status":           "resolved",
        "resolved_outcome": "win" if won else "loss",
        "pnl":              updated_mkt["position"]["pnl"],
        "actual_temp":      actual_temp,
    }

    save_market(resolved_mkt)
    return resolved_mkt, updated_state, True


def _hours_left(end_date_str: str) -> float:
    if not end_date_str:
        return 999.0
    try:
        end = datetime.fromisoformat(end_date_str.replace("Z", "+00:00"))
        return max(0.0, (end - datetime.now(timezone.utc)).total_seconds() / 3600)
    except Exception:
        return 999.0
