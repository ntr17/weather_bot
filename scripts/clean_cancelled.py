"""Remove paper_cancelled positions from market records.
Run once to clean up after reset_for_live.py.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.storage import load_all_markets, save_market


def main():
    markets = load_all_markets()
    total_removed = 0
    markets_touched = 0

    for mkt in markets:
        positions = mkt.get("positions", {})
        to_remove = [
            pid for pid, pos in positions.items()
            if pos.get("close_reason") == "paper_cancelled"
        ]
        if to_remove:
            for pid in to_remove:
                del positions[pid]
            save_market({**mkt, "positions": positions})
            total_removed += len(to_remove)
            markets_touched += 1

    print(f"Removed {total_removed} paper_cancelled positions from {markets_touched} markets")


if __name__ == "__main__":
    main()
