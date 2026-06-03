"""
Reset state for live trading.

Run this ONCE before flipping PAPER_TRADING=false.
Resets balance to real bankroll, closes all paper positions,
preserves market history and calibration data.
"""
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.storage import load_state, save_state, load_all_markets, save_market


def main():
    parser = argparse.ArgumentParser(description="Reset paper state before live trading.")
    parser.add_argument("--balance", type=float, default=50.0, help="Real live bankroll in USDC.")
    args = parser.parse_args()

    live_balance = round(args.balance, 2)
    closed_at = datetime.now(timezone.utc).isoformat()

    state = load_state(live_balance)
    old_balance = state["balance"]

    # Close all open paper positions (mark as cancelled, not as losses)
    markets = load_all_markets()
    cancelled = 0
    for mkt in markets:
        positions = mkt.get("positions", {})
        changed = False
        for pid, pos in positions.items():
            if pos.get("status") == "open":
                positions[pid] = {
                    **pos,
                    "status": "closed",
                    "close_reason": "paper_cancelled",
                    "exit_price": pos["entry_price"],  # neutral — no PnL
                    "pnl": 0.0,
                    "closed_at": closed_at,
                }
                cancelled += 1
                changed = True
        if changed:
            save_market({**mkt, "positions": positions})

    # Reset state
    new_state = {
        **state,
        "balance": live_balance,
        "total_trades": state.get("total_trades", 0),
        "wins": state.get("wins", 0),
        "losses": state.get("losses", 0),
        "peak_balance": live_balance,
    }
    save_state(new_state)

    LIVE_BALANCE = live_balance
    print(f"State reset complete:")
    print(f"  Balance: ${old_balance:.2f} → ${LIVE_BALANCE:.2f}")
    print(f"  Cancelled {cancelled} open paper positions")
    print(f"  Market history and calibration preserved")
    print(f"\n  Ready for PAPER_TRADING=false")


if __name__ == "__main__":
    main()
