"""
Polymarket market discovery and parsing.

Finds temperature bucket markets for a given city + date, parses
bucket ranges from question text, and fetches live order-book prices.
"""

import json
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone

import requests

from core.locations import MONTHS


@dataclass
class Outcome:
    question: str
    market_id: str
    t_low: float    # -999 = "or below" edge bucket
    t_high: float   # +999 = "or higher" edge bucket
    bid: float
    ask: float
    spread: float
    volume: float


def _get_json(url: str, retries: int = 3) -> dict | list:
    for attempt in range(retries):
        try:
            resp = requests.get(url, timeout=(5, 8))
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
            else:
                raise exc
    return {}


def get_event(city_slug: str, month: int, day: int, year: int) -> dict | None:
    """
    Fetch the Polymarket event for highest daily temperature in a city.
    Slug format: highest-temperature-in-{city}-on-{month}-{day}-{year}
    """
    month_name = MONTHS[month - 1]
    slug = f"highest-temperature-in-{city_slug}-on-{month_name}-{day}-{year}"
    try:
        data = _get_json(f"https://gamma-api.polymarket.com/events?slug={slug}")
        if data and isinstance(data, list) and len(data) > 0:
            return data[0]
    except Exception:
        pass
    return None


def parse_temp_range(question: str) -> tuple[float, float] | None:
    """
    Extract (t_low, t_high) from a temperature bucket question.

    Handles:
      "between 45-46°F"  → (45.0, 46.0)
      "40°F or below"    → (-999.0, 40.0)
      "90°F or higher"   → (90.0, 999.0)
      "be 45°F on"       → (45.0, 45.0)  exact single-degree
    """
    if not question:
        return None
    num = r"(-?\d+(?:\.\d+)?)"

    if re.search(r"or below", question, re.IGNORECASE):
        m = re.search(num + r"[°]?[FC] or below", question, re.IGNORECASE)
        if m:
            return (-999.0, float(m.group(1)))

    if re.search(r"or higher", question, re.IGNORECASE):
        m = re.search(num + r"[°]?[FC] or higher", question, re.IGNORECASE)
        if m:
            return (float(m.group(1)), 999.0)

    m = re.search(r"between " + num + r"-" + num + r"[°]?[FC]", question, re.IGNORECASE)
    if m:
        return (float(m.group(1)), float(m.group(2)))

    m = re.search(r"be " + num + r"[°]?[FC] on", question, re.IGNORECASE)
    if m:
        v = float(m.group(1))
        return (v, v)

    return None


def hours_to_resolution(end_date_str: str) -> float:
    """Hours remaining until market closes."""
    if not end_date_str:
        return 999.0
    try:
        end = datetime.fromisoformat(end_date_str.replace("Z", "+00:00"))
        return max(0.0, (end - datetime.now(timezone.utc)).total_seconds() / 3600)
    except Exception:
        return 999.0


def parse_outcomes(event: dict) -> list[Outcome]:
    """Extract all temperature bucket outcomes from a Polymarket event."""
    outcomes: list[Outcome] = []
    for market in event.get("markets", []):
        question = market.get("question", "")
        rng = parse_temp_range(question)
        if not rng:
            continue
        try:
            prices = json.loads(market.get("outcomePrices", "[0.5,0.5]"))
            bid = float(prices[0])
            ask = float(prices[1]) if len(prices) > 1 else bid
        except Exception:
            continue

        outcomes.append(Outcome(
            question=question,
            market_id=str(market.get("id", "")),
            t_low=rng[0],
            t_high=rng[1],
            bid=round(bid, 4),
            ask=round(ask, 4),
            spread=round(ask - bid, 4),
            volume=float(market.get("volume", 0)),
        ))

    outcomes.sort(key=lambda o: o.t_low)
    return outcomes


def fetch_live_price(market_id: str) -> tuple[float, float] | None:
    """
    Fetch real-time bestBid / bestAsk directly from the market endpoint.
    Returns (bid, ask) or None on failure.

    Bug fix vs v2: v2 used outcomePrices[0/1] in some places and bestBid/bestAsk
    in others, causing inconsistency. This function always uses bestBid/bestAsk.
    """
    try:
        data = _get_json(f"https://gamma-api.polymarket.com/markets/{market_id}", retries=2)
        best_bid = data.get("bestBid")
        best_ask = data.get("bestAsk")
        if best_bid is not None and best_ask is not None:
            return (float(best_bid), float(best_ask))
    except Exception:
        pass
    return None


def check_resolved(market_id: str) -> bool | None:
    """
    Check if a market has resolved.
    Returns True (YES won), False (NO won), None (still open / undetermined).
    """
    try:
        data = _get_json(f"https://gamma-api.polymarket.com/markets/{market_id}", retries=2)
        if not data.get("closed", False):
            return None
        prices = json.loads(data.get("outcomePrices", "[0.5,0.5]"))
        yes_price = float(prices[0])
        if yes_price >= 0.95:
            return True
        if yes_price <= 0.05:
            return False
    except Exception:
        pass
    return None
