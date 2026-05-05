"""
Order execution — paper trading and live trading.

Paper mode: deducts cost from balance in state.json, records position.
Live mode: calls the Polymarket CLOB API (not yet implemented — Phase 2).

All state mutations go through storage helpers (immutable update pattern).
"""

from datetime import datetime, timezone
from typing import Any

from core.config import Config
from core.notifier import trade_closed, trade_opened
from core.pricer import bet_size, calc_ev, calc_kelly, bucket_prob
from core.storage import save_market, save_state, append_trade
from core.scanner import Outcome, fetch_live_price


def try_open_position(
    mkt: dict[str, Any],
    outcome: Outcome,
    forecast_temp: float,
    forecast_source: str,
    sigma: float,
    state: dict[str, Any],
    cfg: Config,
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Attempt to open a YES position on the given outcome.

    Returns (updated_market, updated_state, did_open).

    Steps:
      1. Calculate probability, EV, Kelly from snapshot price.
      2. Apply all filters (EV, price, volume, slippage).
      3. Fetch live bestAsk / bestBid from Polymarket API.
      4. Re-check filters with live price.
      5. Open position (deduct from balance).
    """
    p = bucket_prob(forecast_temp, outcome.t_low, outcome.t_high, sigma)
    ev = calc_ev(p, outcome.ask)

    if ev < cfg.min_ev:
        return mkt, state, False
    if outcome.ask >= cfg.max_price:
        return mkt, state, False
    if outcome.ask < cfg.min_yes_price:
        return mkt, state, False
    if outcome.volume < cfg.min_volume:
        return mkt, state, False
    if outcome.spread > cfg.max_slippage:
        return mkt, state, False

    kelly = calc_kelly(p, outcome.ask, cfg.kelly_fraction)
    size = bet_size(kelly, state["balance"], cfg.max_bet)
    if size < 0.50:
        return mkt, state, False

    # Fetch live price — re-check with real market data
    live = fetch_live_price(outcome.market_id)
    if live is None:
        print(f"  [WARN] Could not fetch live price for {outcome.market_id}")
        live = (outcome.bid, outcome.ask)

    real_bid, real_ask = live
    real_spread = round(real_ask - real_bid, 4)

    if real_ask >= cfg.max_price or real_ask < cfg.min_yes_price or real_spread > cfg.max_slippage:
        unit_sym = mkt.get("unit", "F")
        print(
            f"  [SKIP] {mkt['city_name']} {mkt['date']} — "
            f"live ask ${real_ask:.3f} spread ${real_spread:.3f}"
        )
        return mkt, state, False

    # Recalculate EV and Kelly with live price
    real_ev = calc_ev(p, real_ask)
    if real_ev < cfg.min_ev:
        return mkt, state, False

    real_kelly = calc_kelly(p, real_ask, cfg.kelly_fraction)
    real_size = bet_size(real_kelly, state["balance"], cfg.max_bet)
    real_shares = round(real_size / real_ask, 4)

    unit_sym = mkt.get("unit", "F")
    bucket_label = _bucket_label(outcome.t_low, outcome.t_high, unit_sym)
    horizon = mkt.get("current_horizon", "D+?")

    print(
        f"  [BUY]  {mkt['city_name']} {horizon} {mkt['date']} | "
        f"{bucket_label} | ${real_ask:.3f} | EV {real_ev:+.2f} | "
        f"${real_size:.2f} ({forecast_source.upper()})"
    )

    position = {
        "market_id":          outcome.market_id,
        "question":           outcome.question,
        "side":               "yes",
        "bucket_low":         outcome.t_low,
        "bucket_high":        outcome.t_high,
        "entry_price":        real_ask,
        "bid_at_entry":       real_bid,
        "spread":             real_spread,
        "shares":             real_shares,
        "cost":               real_size,
        "p":                  round(p, 4),
        "ev":                 round(real_ev, 4),
        "kelly":              round(real_kelly, 4),
        "forecast_temp":      forecast_temp,
        "forecast_source":    forecast_source,
        "sigma":              sigma,
        "stop_price":         round(real_ask * cfg.stop_loss_pct, 4),
        "trailing_activated": False,
        "opened_at":          datetime.now(timezone.utc).isoformat(),
        "status":             "open",
        "exit_price":         None,
        "close_reason":       None,
        "closed_at":          None,
        "pnl":                None,
    }

    new_positions = {**mkt.get("positions", {}), outcome.market_id: position}
    updated_mkt = {**mkt, "positions": new_positions}
    updated_state = {
        **state,
        "balance":      round(state["balance"] - real_size, 2),
        "total_trades": state["total_trades"] + 1,
    }

    if not cfg.paper_trading:
        _execute_live_order(outcome.market_id, real_size, cfg)

    save_market(updated_mkt)
    save_state(updated_state)
    trade_opened(mkt["city_name"], mkt["date"], bucket_label,
                 real_ask, real_ev, real_size, forecast_source)
    return updated_mkt, updated_state, True


def try_open_no_position(
    mkt: dict[str, Any],
    outcome: Outcome,
    forecast_temp: float,
    forecast_source: str,
    sigma: float,
    state: dict[str, Any],
    cfg: Config,
) -> tuple[dict[str, Any], dict[str, Any], bool]:
    """
    Attempt to open a NO position on a bucket the forecast says is unlikely.

    We buy NO when the market overprices a bucket our airport forecast says
    is clearly wrong — the mirror image of the YES edge.

    NO token cost  = 1 - YES_bid
    NO token pays  = $1.00 if YES resolves NO (i.e. that bucket didn't hit)
    """
    p_yes = bucket_prob(forecast_temp, outcome.t_low, outcome.t_high, sigma)
    p_no = round(1.0 - p_yes, 4)

    # Only bet NO when we're very confident YES is wrong
    if p_yes > cfg.no_pyes_threshold:
        return mkt, state, False

    # NO ask = 1 - YES_bid (cost to acquire the NO token)
    no_ask_snapshot = round(1.0 - outcome.bid, 4)
    ev_no = calc_ev(p_no, no_ask_snapshot)

    if ev_no < cfg.min_ev:
        return mkt, state, False
    if no_ask_snapshot >= cfg.max_no_price:   # NO tokens are inherently priced near 1.0
        return mkt, state, False
    if outcome.volume < cfg.min_volume:
        return mkt, state, False
    if outcome.spread > cfg.max_slippage:
        return mkt, state, False

    kelly = calc_kelly(p_no, no_ask_snapshot, cfg.kelly_fraction)
    size = bet_size(kelly, state["balance"], cfg.max_bet)
    if size < 0.50:
        return mkt, state, False

    # Fetch live price — re-check with real market data
    live = fetch_live_price(outcome.market_id)
    if live is None:
        print(f"  [WARN] Could not fetch live price for {outcome.market_id}")
        live = (outcome.bid, outcome.ask)

    real_yes_bid, real_yes_ask = live
    real_no_ask = round(1.0 - real_yes_bid, 4)
    real_no_bid = round(1.0 - real_yes_ask, 4)
    real_spread = round(real_yes_ask - real_yes_bid, 4)

    if real_no_ask >= cfg.max_no_price or real_spread > cfg.max_slippage:
        return mkt, state, False

    # Entry band filter — only trade NOs in the profitable range
    if real_no_ask < cfg.min_no_entry or real_no_ask > cfg.max_no_entry:
        return mkt, state, False

    real_ev_no = calc_ev(p_no, real_no_ask)
    if real_ev_no < cfg.min_ev:
        return mkt, state, False

    real_kelly = calc_kelly(p_no, real_no_ask, cfg.kelly_fraction)
    real_size = bet_size(real_kelly, state["balance"], cfg.max_bet)
    real_shares = round(real_size / real_no_ask, 4)

    unit_sym = mkt.get("unit", "F")
    bucket_label = _bucket_label(outcome.t_low, outcome.t_high, unit_sym)
    horizon = mkt.get("current_horizon", "D+?")

    print(
        f"  [SELL] {mkt['city_name']} {horizon} {mkt['date']} | "
        f"NO {bucket_label} | ${real_no_ask:.3f} | EV {real_ev_no:+.2f} | "
        f"${real_size:.2f} ({forecast_source.upper()})"
    )

    position = {
        "market_id":          outcome.market_id,
        "question":           outcome.question,
        "side":               "no",
        "bucket_low":         outcome.t_low,
        "bucket_high":        outcome.t_high,
        "entry_price":        real_no_ask,
        "bid_at_entry":       real_no_bid,
        "spread":             real_spread,
        "shares":             real_shares,
        "cost":               real_size,
        "p":                  p_no,
        "ev":                 round(real_ev_no, 4),
        "kelly":              round(real_kelly, 4),
        "forecast_temp":      forecast_temp,
        "forecast_source":    forecast_source,
        "sigma":              sigma,
        "stop_price":         round(real_no_ask * cfg.no_stop_loss_pct, 4),
        "trailing_activated": False,
        "opened_at":          datetime.now(timezone.utc).isoformat(),
        "status":             "open",
        "exit_price":         None,
        "close_reason":       None,
        "closed_at":          None,
        "pnl":                None,
    }

    new_positions = {**mkt.get("positions", {}), outcome.market_id: position}
    updated_mkt = {**mkt, "positions": new_positions}
    updated_state = {
        **state,
        "balance":      round(state["balance"] - real_size, 2),
        "total_trades": state["total_trades"] + 1,
    }

    if not cfg.paper_trading:
        _execute_live_order(outcome.market_id, real_size, cfg)

    save_market(updated_mkt)
    save_state(updated_state)
    trade_opened(mkt["city_name"], mkt["date"], f"NO {bucket_label}",
                 real_no_ask, real_ev_no, real_size, forecast_source)
    return updated_mkt, updated_state, True


def close_position(
    mkt: dict[str, Any],
    exit_price: float,
    reason: str,
    state: dict[str, Any],
    position_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """
    Close an open position and update balance + market record.
    If position_id is given, close that specific position from positions dict.
    Returns (updated_market, updated_state).
    """
    positions = mkt.get("positions", {})
    if position_id and position_id in positions:
        pos = positions[position_id]
    elif position_id is None and positions:
        # Close first open position (backward compat)
        open_pos = {k: v for k, v in positions.items() if v.get("status") == "open"}
        if not open_pos:
            return mkt, state
        position_id, pos = next(iter(open_pos.items()))
    else:
        return mkt, state

    if pos.get("status") != "open":
        return mkt, state

    pnl = round((exit_price - pos["entry_price"]) * pos["shares"], 2)
    now = datetime.now(timezone.utc).isoformat()

    reason_label = {
        "stop_loss":      "STOP",
        "trailing_stop":  "TRAILING",
        "take_profit":    "TAKE",
        "forecast_changed": "CLOSE",
        "resolved_win":   "WIN",
        "resolved_loss":  "LOSS",
    }.get(reason, reason.upper())

    print(
        f"  [{reason_label}] {mkt['city_name']} {mkt['date']} | "
        f"entry ${pos['entry_price']:.3f} → ${exit_price:.3f} | "
        f"PnL: {'+'if pnl>=0 else ''}{pnl:.2f}"
    )

    updated_pos = {
        **pos,
        "exit_price":   exit_price,
        "pnl":          pnl,
        "close_reason": reason,
        "closed_at":    now,
        "status":       "closed",
    }
    updated_positions = {**positions, position_id: updated_pos}
    updated_mkt = {**mkt, "positions": updated_positions}
    updated_state = {
        **state,
        "balance": round(state["balance"] + pos["cost"] + pnl, 2),
        "peak_balance": max(state.get("peak_balance", 0), state["balance"] + pos["cost"] + pnl),
    }

    # Update win/loss counters for ALL close reasons (not just resolution)
    if pnl >= 0:
        updated_state = {**updated_state, "wins": updated_state.get("wins", 0) + 1}
    else:
        updated_state = {**updated_state, "losses": updated_state.get("losses", 0) + 1}

    save_market(updated_mkt)
    save_state(updated_state)
    append_trade(updated_mkt, pos=updated_positions[position_id])
    trade_closed(
        mkt["city_name"], mkt["date"],
        _bucket_label(pos["bucket_low"], pos["bucket_high"], mkt.get("unit", "F")),
        pos["entry_price"], exit_price, pnl, reason,
    )
    return updated_mkt, updated_state


def _bucket_label(t_low: float, t_high: float, unit: str) -> str:
    if t_low == -999.0:
        return f"≤{t_high:.0f}°{unit}"
    if t_high == 999.0:
        return f"≥{t_low:.0f}°{unit}"
    return f"{t_low:.0f}–{t_high:.0f}°{unit}"


def _execute_live_order(market_id: str, size: float, cfg: Config) -> None:
    """
    Live order execution placeholder — Phase 2.
    Will call polymarket-live-executor skill or CLOB API directly.
    """
    raise NotImplementedError(
        "Live trading not yet implemented. Set PAPER_TRADING=true in .env "
        "or implement CLOB integration in Phase 2."
    )
