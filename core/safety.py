"""
Safety controls for live trading.

Kill switch: stops all trading if daily losses exceed threshold.
Bankroll guard: prevents trades when balance is critically low.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

_SAFETY_PATH = Path(__file__).parent.parent / "data" / "safety.json"


def _load_safety() -> dict:
    if _SAFETY_PATH.exists():
        with open(_SAFETY_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"kill_switch": False, "daily_losses": {}, "reason": ""}


def _save_safety(data: dict) -> None:
    _SAFETY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(_SAFETY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def is_killed() -> tuple[bool, str]:
    """Check if the kill switch is active. Returns (is_killed, reason)."""
    data = _load_safety()
    if data.get("kill_switch", False):
        return True, data.get("reason", "Kill switch active")
    return False, ""


def activate_kill_switch(reason: str) -> None:
    """Activate the kill switch — stops all trading."""
    data = _load_safety()
    data["kill_switch"] = True
    data["reason"] = reason
    data["killed_at"] = datetime.now(timezone.utc).isoformat()
    _save_safety(data)
    print(f"  [KILL SWITCH] ACTIVATED: {reason}")


def deactivate_kill_switch() -> None:
    """Deactivate the kill switch."""
    data = _load_safety()
    data["kill_switch"] = False
    data["reason"] = ""
    _save_safety(data)
    print("  [KILL SWITCH] Deactivated")


def record_daily_loss(amount: float) -> None:
    """Record a loss for today."""
    data = _load_safety()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    daily = data.get("daily_losses", {})
    daily[today] = daily.get(today, 0.0) + amount
    data["daily_losses"] = daily
    _save_safety(data)


def check_daily_loss_limit(balance: float, max_daily_loss_pct: float = 0.20) -> bool:
    """
    Check if daily losses exceed the limit.
    Returns True if trading should continue, False if limit hit.
    
    max_daily_loss_pct: max % of initial balance we can lose per day (default 20%)
    """
    data = _load_safety()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    daily_loss = data.get("daily_losses", {}).get(today, 0.0)
    max_loss = balance * max_daily_loss_pct

    if daily_loss >= max_loss:
        activate_kill_switch(
            f"Daily loss limit hit: ${daily_loss:.2f} >= ${max_loss:.2f} ({max_daily_loss_pct*100:.0f}%)"
        )
        return False
    return True


def pre_trade_check(balance: float, bet_size: float) -> tuple[bool, str]:
    """
    Run all pre-trade safety checks.
    Returns (can_trade, reason_if_blocked).
    """
    # 1. Kill switch
    killed, reason = is_killed()
    if killed:
        return False, f"Kill switch: {reason}"

    # 2. Minimum balance
    if balance < 10.0:
        return False, f"Balance too low: ${balance:.2f} < $10.00"

    # 3. Bet size vs balance
    if bet_size > balance * 0.30:
        return False, f"Bet ${bet_size:.2f} > 30% of balance ${balance:.2f}"

    # 4. Daily loss limit
    if not check_daily_loss_limit(balance):
        return False, "Daily loss limit exceeded"

    return True, ""
