"""Audit whether the current WeatherBot strategy has a measurable edge.

This is intentionally dependency-free so it can run on GitHub Actions, Windows,
or a small self-hosted runner without adding pandas/numpy.
"""

from __future__ import annotations

import json
import math
import random
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "weatherbot.db"
RNG_SEED = 11


def wilson_interval(wins: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return 0.0, 0.0
    phat = wins / n
    denom = 1.0 + z * z / n
    center = (phat + z * z / (2 * n)) / denom
    radius = z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n) / denom
    return center - radius, center + radius


def metrics(trades: list[dict]) -> dict:
    n = len(trades)
    wins = sum(1 for t in trades if t["pnl"] > 0)
    pnl = sum(t["pnl"] for t in trades)
    cost = sum(t["cost"] for t in trades)
    avg_entry = sum(t["entry_price"] for t in trades) / n if n else 0.0
    wr_lo, wr_hi = wilson_interval(wins, n)

    roi_boot = []
    if n:
        random.seed(RNG_SEED)
        for _ in range(10_000):
            sample = [trades[random.randrange(n)] for __ in range(n)]
            sample_cost = sum(t["cost"] for t in sample)
            sample_pnl = sum(t["pnl"] for t in sample)
            roi_boot.append(sample_pnl / sample_cost if sample_cost else 0.0)
        roi_boot.sort()
        roi_lo = roi_boot[250]
        roi_hi = roi_boot[9749]
    else:
        roi_lo = roi_hi = 0.0

    return {
        "n": n,
        "wins": wins,
        "losses": n - wins,
        "wr": wins / n if n else 0.0,
        "wr_lo": wr_lo,
        "wr_hi": wr_hi,
        "avg_entry": avg_entry,
        "pnl": pnl,
        "cost": cost,
        "roi": pnl / cost if cost else 0.0,
        "roi_lo": roi_lo,
        "roi_hi": roi_hi,
    }


def print_metrics(label: str, m: dict) -> None:
    print(
        f"{label:18s} n={m['n']:3d} W/L={m['wins']:3d}/{m['losses']:<3d} "
        f"WR={m['wr'] * 100:5.1f}% [{m['wr_lo'] * 100:4.1f},{m['wr_hi'] * 100:4.1f}] "
        f"entry={m['avg_entry']:.3f} pnl=${m['pnl']:7.2f} "
        f"ROI={m['roi'] * 100:6.2f}% bootROI95=[{m['roi_lo'] * 100:6.2f},{m['roi_hi'] * 100:6.2f}]"
    )


def load_closed_trades(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute("SELECT * FROM trades ORDER BY opened_at").fetchall()
    trades = []
    for row in rows:
        t = dict(row)
        if t.get("pnl") is None:
            continue
        if t.get("reason") == "paper_cancelled":
            continue
        if not t.get("opened_at"):
            continue
        trades.append(t)
    return trades


def window(trades: list[dict], start: str | None, end: str | None, side: str | None = None) -> list[dict]:
    out = []
    for t in trades:
        opened = t["opened_at"]
        if start and opened < start:
            continue
        if end and opened >= end:
            continue
        if side and t.get("side") != side:
            continue
        out.append(t)
    return out


def load_real_horizon_v3(conn: sqlite3.Connection) -> list[dict]:
    """Return V3 NO trades whose market date was at least D+1 at entry."""
    v3 = []
    rows = conn.execute("SELECT city, date, json_data FROM markets").fetchall()
    for row in rows:
        market = json.loads(row["json_data"])
        for pos in market.get("positions", {}).values():
            if pos.get("status") != "closed":
                continue
            if pos.get("side") != "no":
                continue
            if pos.get("opened_at", "") < "2026-05-14":
                continue
            if pos.get("close_reason") == "paper_cancelled" or pos.get("pnl") is None:
                continue
            try:
                horizon = (
                    datetime.strptime(market["date"], "%Y-%m-%d").date()
                    - datetime.fromisoformat(pos["opened_at"]).date()
                ).days
            except Exception:
                continue
            if horizon >= 1:
                v3.append(
                    {
                        **pos,
                        "city": market.get("city_name", market.get("city", "?")),
                        "date": market.get("date"),
                        "real_horizon": horizon,
                    }
                )
    return v3


def bayes_prob_wr_above_breakeven(wins: int, losses: int, breakeven: float, draws: int = 100_000) -> float:
    """Beta(wins+1, losses+1) posterior probability that true WR exceeds breakeven."""
    random.seed(12)
    above = 0
    for _ in range(draws):
        x = random.gammavariate(wins + 1, 1)
        y = random.gammavariate(losses + 1, 1)
        if x / (x + y) > breakeven:
            above += 1
    return above / draws


def current_open_positions(conn: sqlite3.Connection) -> list[dict]:
    positions = []
    for row in conn.execute("SELECT city, date, json_data FROM markets").fetchall():
        market = json.loads(row["json_data"])
        for pos in market.get("positions", {}).values():
            if pos.get("status") != "open":
                continue
            positions.append(
                {
                    "city": market.get("city_name", market.get("city", "?")),
                    "date": market.get("date"),
                    "horizon": market.get("current_horizon", "?"),
                    **pos,
                }
            )
    return positions


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    trades = load_closed_trades(conn)
    print("=== Strategy Windows (NO only) ===")
    for label, start, end in [
        ("all_no", None, None),
        ("pre_v2_no", None, "2026-05-06"),
        ("v2_no_hold", "2026-05-06", "2026-05-14"),
        ("v3_no_raw", "2026-05-14", None),
    ]:
        print_metrics(label, metrics(window(trades, start, end, side="no")))

    print("\n=== V3 Actual Strategy: NO, Real D+1 or Later ===")
    v3 = load_real_horizon_v3(conn)
    v3m = metrics(v3)
    print_metrics("v3_actual", v3m)
    if v3:
        prob = bayes_prob_wr_above_breakeven(v3m["wins"], v3m["losses"], v3m["avg_entry"])
        print(f"Bayes P(true WR > avg entry breakeven): {prob:.3f}")

    print("\nBy real horizon:")
    by_horizon: dict[int, list[dict]] = defaultdict(list)
    for t in v3:
        by_horizon[t["real_horizon"]].append(t)
    for horizon in sorted(by_horizon):
        print_metrics(f"D+{horizon}", metrics(by_horizon[horizon]))

    print("\nBy exit reason:")
    by_reason: dict[str, list[dict]] = defaultdict(list)
    for t in v3:
        by_reason[t.get("close_reason", "?")].append(t)
    for reason, subset in sorted(by_reason.items()):
        print_metrics(reason, metrics(subset))

    print("\n=== Current Open Paper Exposure ===")
    open_pos = current_open_positions(conn)
    exposure = sum(p.get("cost", 0.0) or 0.0 for p in open_pos)
    print(f"Open positions: {len(open_pos)}")
    print(f"Open cost: ${exposure:.2f}")
    for p in sorted(open_pos, key=lambda x: (x["date"], x["city"], x.get("bucket_low", 0))):
        print(
            f"  {p['city']:16s} {p['date']} {p.get('side', '?').upper():3s} "
            f"{p.get('bucket_low', 0):.0f}-{p.get('bucket_high', 0):.0f} "
            f"entry={p.get('entry_price', 0):.3f} cost=${p.get('cost', 0):.2f} "
            f"src={str(p.get('forecast_source', '?')).upper():8s} horizon={p['horizon']}"
        )

    print("\n=== $50 Live Launch Readiness ===")
    print("Verify active config before launch; global exposure controls should be enabled.")
    print("Initial live caps: max_bet=$5, max_total_open_cost=$15-$20, max_new_positions_per_run=2.")
    print("Candidate filter: NO only, real D+2, entry 0.70-0.85, min_ev >= 0.15.")

    conn.close()


if __name__ == "__main__":
    main()
