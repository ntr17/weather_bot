"""
Query and summarize paper trading results from logs/paper_trades.jsonl.

Usage:
    python scripts/query_trades.py           # full summary
    python scripts/query_trades.py --city nyc
    python scripts/query_trades.py --recent 20
    python scripts/query_trades.py --horizon D+1
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

TRADE_LOG = ROOT / "logs" / "paper_trades.jsonl"


def load_trades(city: str | None = None, horizon: str | None = None) -> list[dict]:
    if not TRADE_LOG.exists():
        return []
    trades = []
    with TRADE_LOG.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            t = json.loads(line)
            if city and t.get("city") != city:
                continue
            if horizon and t.get("horizon") != horizon:
                continue
            trades.append(t)
    return trades


def _pnl_str(v: float | None) -> str:
    if v is None:
        return "   ?"
    return f"{'+' if v >= 0 else ''}{v:6.2f}"


def print_summary(trades: list[dict]) -> None:
    if not trades:
        print("No trades in log yet.")
        return

    resolved = [t for t in trades if t.get("reason", "").startswith("resolved")]
    wins     = [t for t in resolved if t.get("outcome") == "win"]
    total_pnl = sum(t["pnl"] for t in trades if t.get("pnl") is not None)
    win_rate  = len(wins) / len(resolved) * 100 if resolved else 0.0

    print(f"\n{'='*60}")
    print(f"  PAPER TRADING RESULTS")
    print(f"{'='*60}")
    print(f"  Total trades:   {len(trades)}")
    print(f"  Resolved:       {len(resolved)}  (wins: {len(wins)}, losses: {len(resolved)-len(wins)})")
    print(f"  Win rate:       {win_rate:.1f}%")
    print(f"  Total PnL:      {_pnl_str(total_pnl)}")
    if resolved:
        avg = total_pnl / len(resolved)
        print(f"  Avg PnL/trade:  {_pnl_str(avg)}")

    # Per-city
    cities: dict[str, list] = {}
    for t in resolved:
        c = t.get("city_name", t.get("city", "?"))
        cities.setdefault(c, []).append(t)
    if cities:
        print(f"\n  By city:")
        for c, ts in sorted(cities.items()):
            w = sum(1 for t in ts if t.get("outcome") == "win")
            p = sum(t["pnl"] for t in ts if t.get("pnl") is not None)
            print(f"    {c:<18} {w}/{len(ts)} wins  PnL {_pnl_str(p)}")

    # Per-horizon
    horizons: dict[str, list] = {}
    for t in resolved:
        h = t.get("horizon", "?")
        horizons.setdefault(h, []).append(t)
    if horizons:
        print(f"\n  By horizon:")
        for h, ts in sorted(horizons.items()):
            w = sum(1 for t in ts if t.get("outcome") == "win")
            p = sum(t["pnl"] for t in ts if t.get("pnl") is not None)
            print(f"    {h:<8} {w}/{len(ts)} wins  PnL {_pnl_str(p)}")

    # Per-source
    sources: dict[str, list] = {}
    for t in resolved:
        s = t.get("forecast_source", "?")
        sources.setdefault(s, []).append(t)
    if sources:
        print(f"\n  By forecast source:")
        for s, ts in sorted(sources.items()):
            w = sum(1 for t in ts if t.get("outcome") == "win")
            p = sum(t["pnl"] for t in ts if t.get("pnl") is not None)
            print(f"    {s:<12} {w}/{len(ts)} wins  PnL {_pnl_str(p)}")

    print(f"{'='*60}\n")


def print_recent(trades: list[dict], n: int = 10) -> None:
    recent = trades[-n:]
    print(f"\n  Last {len(recent)} trades:")
    print(f"  {'Date':<12} {'City':<16} {'Bucket':<14} {'Side':<4} {'Entry':>6} {'Exit':>6} {'PnL':>7}  Outcome")
    print(f"  {'-'*80}")
    for t in recent:
        bl = t.get("bucket_low")
        bh = t.get("bucket_high")
        bl_s = f"{bl:.0f}" if bl is not None and bl > -900 else "?"
        bh_s = f"{bh:.0f}" if bh is not None and bh < 900 else "+"
        bucket = f"{bl_s}–{bh_s}°{t.get('unit','?')}"
        entry  = t.get("entry_price") or 0
        exit_p = t.get("exit_price")
        exit_s = f"{exit_p:.3f}" if exit_p is not None else "open"
        pnl_s  = _pnl_str(t.get("pnl"))
        outcome = t.get("outcome") or t.get("reason") or "?"
        print(f"  {t.get('date','?'):<12} {t.get('city_name','?'):<16} {bucket:<14} "
              f"{t.get('side','y'):<4} {entry:>6.3f} {exit_s:>6} {pnl_s}  {outcome}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--city",    default=None, help="Filter by city slug (e.g. nyc)")
    parser.add_argument("--horizon", default=None, help="Filter by horizon (e.g. D+1)")
    parser.add_argument("--recent",  type=int, default=None, help="Show N most recent trades")
    args = parser.parse_args()

    trades = load_trades(city=args.city, horizon=args.horizon)
    print_summary(trades)
    n = args.recent or min(20, len(trades))
    if trades:
        print_recent(trades, n)
