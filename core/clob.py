"""
Polymarket CLOB API integration for live order execution.

Uses py-clob-client-v2 for authenticated trading.
Handles: client initialization, order book analysis, limit order placement,
order tracking, and position exits.
"""

import json
import logging
import os
from typing import Optional

logger = logging.getLogger(__name__)

# Lazy import — only load when live trading is enabled
_client = None
_initialized = False


def _get_client():
    """
    Lazy-init the ClobClient. Only imported when live trading is active.
    Requires env vars: PK, FUNDER (proxy wallet address).
    """
    global _client, _initialized
    if _initialized:
        return _client

    _initialized = True

    pk = os.environ.get("PK", "")
    funder = os.environ.get("FUNDER", "")
    # SIGNATURE_TYPE controls the wallet flow:
    #   3 = POLY_1271 (deposit wallet — for new API wallets, e.g. MetaMask)
    #   1 = POLY_PROXY (old proxy wallet flow — only for legacy Google/email accounts)
    sig_type = int(os.environ.get("SIGNATURE_TYPE", "3"))

    if not pk or not funder:
        logger.warning("PK or FUNDER not set — live trading disabled")
        return None

    try:
        from py_clob_client_v2 import ApiCreds, ClobClient

        host = "https://clob.polymarket.com"
        chain_id = 137

        # Step 1: derive API credentials (L1 auth)
        # Note: create_or_derive_api_key() first tries CREATE (which 400s if
        # key already exists), then falls back to DERIVE. The library prints
        # a "[py_clob_client_v2] request error status=400" line — this is
        # EXPECTED on every run after the first. Not an error.
        temp_client = ClobClient(
            host=host,
            chain_id=chain_id,
            key=pk,
            signature_type=sig_type,
            funder=funder,
        )
        creds = temp_client.create_or_derive_api_key()
        if creds is None:
            logger.error("CLOB auth failed: could not create or derive API key. "
                         "Check PK, FUNDER, and SIGNATURE_TYPE.")
            return None
        logger.info("CLOB API credentials ready (sig_type=%d, funder=%s...%s)",
                    sig_type, funder[:6], funder[-4:])

        # Step 2: create fully authenticated client (L1+L2)
        _client = ClobClient(
            host=host,
            chain_id=chain_id,
            key=pk,
            creds=creds,
            signature_type=sig_type,
            funder=funder,
        )
        return _client

    except Exception as e:
        logger.error("Failed to initialize CLOB client: %s", e)
        _client = None
        return None


def get_order_book_depth(token_id: str, size_usdc: float = 15.0) -> Optional[dict]:
    """
    Analyze order book depth for a token. Returns None if client unavailable.

    Returns dict with: best_bid, best_ask, midpoint, spread,
                       vwap_buy (for buying `size_usdc` worth),
                       vwap_sell, slippage_pct
    """
    client = _get_client()
    if not client:
        return None

    try:
        book = client.get_order_book(token_id)
        if not book:
            return None

        # Handle both dict and object responses
        if isinstance(book, dict):
            bids = book.get("bids", [])
            asks = book.get("asks", [])
        else:
            bids = book.bids if hasattr(book, "bids") else []
            asks = book.asks if hasattr(book, "asks") else []

        # Return structured result even if one side is empty
        # (lets caller decide what to do with one-sided books)
        best_bid = 0.0
        best_ask = 0.0
        if bids:
            best_bid = float(bids[0]["price"] if isinstance(bids[0], dict) else bids[0].price)
        if asks:
            best_ask = float(asks[0]["price"] if isinstance(asks[0], dict) else asks[0].price)

        # VWAP calculation for buying
        vwap_buy = best_ask
        slippage = 0.0
        if asks and size_usdc > 0:
            filled = 0.0
            cost = 0.0
            for ask_level in asks:
                p = float(ask_level["price"] if isinstance(ask_level, dict) else ask_level.price)
                q = float(ask_level["size"] if isinstance(ask_level, dict) else ask_level.size)
                take = min(q, (size_usdc / p) - filled) if p > 0 else 0
                cost += take * p
                filled += take
                if cost >= size_usdc:
                    break
            vwap_buy = cost / filled if filled > 0 else best_ask
            slippage = (vwap_buy - best_ask) / best_ask * 100 if best_ask > 0 else 0

        return {
            "best_bid": best_bid,
            "best_ask": best_ask,
            "midpoint": (best_bid + best_ask) / 2 if (best_bid and best_ask) else 0.0,
            "spread": best_ask - best_bid if (best_bid and best_ask) else 0.0,
            "vwap_buy": vwap_buy,
            "slippage_pct": slippage,
            "book_depth_asks": len(asks),
            "book_depth_bids": len(bids),
        }

    except Exception as e:
        logger.error("Order book fetch failed for %s: %s", token_id, e)
        return None


def place_limit_buy(token_id: str, price: float, size_shares: float,
                    neg_risk: bool = True) -> Optional[dict]:
    """
    Place a GTC limit buy order (maker — zero fees).

    Args:
        token_id: the clobTokenId for the YES or NO outcome
        price: limit price (0.00-1.00)
        size_shares: number of shares to buy
        neg_risk: True for multi-outcome weather markets

    Returns: order response dict or None on failure
    """
    client = _get_client()
    if not client:
        return None

    try:
        from py_clob_client_v2 import OrderArgsV2, OrderType, PartialCreateOrderOptions, Side

        # Round price to 0.01 tick size (weather markets require this minimum)
        price = round(round(price / 0.01) * 0.01, 2)

        order_args = OrderArgsV2(
            token_id=token_id,
            price=price,
            size=size_shares,
            side=Side.BUY,
        )
        options = PartialCreateOrderOptions(
            tick_size="0.01",
            neg_risk=neg_risk,
        )

        resp = client.create_and_post_order(
            order_args=order_args,
            options=options,
            order_type=OrderType.GTC,
        )
        logger.info("Limit BUY placed: %s shares @ $%.2f token=%s resp=%s",
                     size_shares, price, token_id[:20], resp)
        return resp

    except Exception as e:
        logger.error("Limit BUY failed for %s: %s", token_id[:20], e)
        return None


def place_limit_sell(token_id: str, price: float, size_shares: float,
                     neg_risk: bool = True) -> Optional[dict]:
    """
    Place a GTC limit sell order (for take-profit exits — maker, zero fees).
    """
    client = _get_client()
    if not client:
        return None

    try:
        from py_clob_client_v2 import OrderArgsV2, OrderType, PartialCreateOrderOptions, Side

        # Round price to 0.01 tick size (weather markets require this minimum)
        price = round(round(price / 0.01) * 0.01, 2)

        order_args = OrderArgsV2(
            token_id=token_id,
            price=price,
            size=size_shares,
            side=Side.SELL,
        )
        options = PartialCreateOrderOptions(
            tick_size="0.01",
            neg_risk=neg_risk,
        )

        resp = client.create_and_post_order(
            order_args=order_args,
            options=options,
            order_type=OrderType.GTC,
        )
        logger.info("Limit SELL placed: %s shares @ $%.2f token=%s resp=%s",
                     size_shares, price, token_id[:20], resp)
        return resp

    except Exception as e:
        logger.error("Limit SELL failed for %s: %s", token_id[:20], e)
        return None


def place_market_buy(token_id: str, amount_usdc: float,
                     neg_risk: bool = True) -> Optional[dict]:
    """
    Place a FOK market buy order (taker — pays fees).
    Use only when speed matters more than fees.
    """
    client = _get_client()
    if not client:
        return None

    try:
        from py_clob_client_v2 import MarketOrderArgsV2, OrderType, PartialCreateOrderOptions, Side

        order_args = MarketOrderArgsV2(
            token_id=token_id,
            amount=amount_usdc,
            side=Side.BUY,
            order_type=OrderType.FOK,
        )
        options = PartialCreateOrderOptions(
            tick_size="0.001",
            neg_risk=neg_risk,
        )

        resp = client.create_and_post_market_order(
            order_args=order_args,
            options=options,
            order_type=OrderType.FOK,
        )
        logger.info("Market BUY placed: $%.2f on token=%s resp=%s",
                     amount_usdc, token_id[:20], resp)
        return resp

    except Exception as e:
        logger.error("Market BUY failed for %s: %s", token_id[:20], e)
        return None


def place_market_sell(token_id: str, size_shares: float,
                      neg_risk: bool = True) -> Optional[dict]:
    """
    Place a FOK market sell order (taker — pays fees).
    Used for exits where guaranteed fill matters more than fees.
    """
    client = _get_client()
    if not client:
        return None

    try:
        from py_clob_client_v2 import MarketOrderArgsV2, OrderType, PartialCreateOrderOptions, Side

        order_args = MarketOrderArgsV2(
            token_id=token_id,
            amount=size_shares,
            side=Side.SELL,
            order_type=OrderType.FOK,
        )
        options = PartialCreateOrderOptions(
            tick_size="0.001",
            neg_risk=neg_risk,
        )

        resp = client.create_and_post_market_order(
            order_args=order_args,
            options=options,
            order_type=OrderType.FOK,
        )
        logger.info("Market SELL placed: %.2f shares on token=%s resp=%s",
                     size_shares, token_id[:20], resp)
        return resp

    except Exception as e:
        logger.error("Market SELL failed for %s: %s", token_id[:20], e)
        return None


def cancel_all_orders() -> Optional[dict]:
    """Cancel all open orders."""
    client = _get_client()
    if not client:
        return None

    try:
        resp = client.cancel_all()
        logger.info("All orders cancelled: %s", resp)
        return resp
    except Exception as e:
        logger.error("Cancel all failed: %s", e)
        return None


def cancel_order(order_id: str) -> bool:
    """Cancel a specific order by ID. Returns True on success."""
    client = _get_client()
    if not client:
        return False

    try:
        resp = client.cancel(order_id=order_id)
        logger.info("Order cancelled: %s resp=%s", order_id[:16], resp)
        return True
    except Exception as e:
        logger.error("Cancel order %s failed: %s", order_id[:16], e)
        return False


def get_order(order_id: str) -> Optional[dict]:
    """Get a specific order's status by ID."""
    client = _get_client()
    if not client:
        return None

    try:
        resp = client.get_order(order_id)
        return resp if isinstance(resp, dict) else None
    except Exception as e:
        logger.error("Get order %s failed: %s", order_id[:16], e)
        return None


def get_open_orders() -> list:
    """Get all open orders."""
    client = _get_client()
    if not client:
        return []

    try:
        from py_clob_client_v2 import OpenOrderParams
        return client.get_orders(OpenOrderParams())
    except Exception as e:
        logger.error("Get orders failed: %s", e)
        return []


def get_trades() -> list:
    """Get trade history."""
    client = _get_client()
    if not client:
        return []

    try:
        return client.get_trades()
    except Exception as e:
        logger.error("Get trades failed: %s", e)
        return []


def reset_client():
    """Force re-initialization of the CLOB client (e.g. after credential rotation)."""
    global _client, _initialized
    _client = None
    _initialized = False
