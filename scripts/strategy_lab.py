#!/usr/bin/env python3
"""Rank paper strategy variants from the WeatherBot SQLite history.

The lab is intentionally dependency-free. It reconstructs closed positions from
the markets table because that preserves real horizon at entry better than the
flat trades table.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "weatherbot.db"
PAPER_CONFIG_PATH = ROOT / "config.paper.json"
OUT_DIR = ROOT / "data" / "strategy_lab"
LATEST_JSON = OUT_DIR / "latest.json"
LATEST_MD = OUT_DIR / "latest.md"
V3_START = "2026-05-14"
RNG_SEED = 29
TAKER_FEE_RATE = 0.05
SPREAD_DRAG_RATE = 0.01


@dataclass(frozen=True)
class Candidate:
    name: str
    min_ev: float
    min_entry: float
    max_entry: float
    min_horizon: int
    max_horizon: int
    sources: tuple[str, ...] = ()
    max_spread: float = 0.15


CANDIDATES = [
    Candidate("d2_ev15", 0.15, 0.70, 0.85, 2, 2),
    Candidate("d2_ev18", 0.18, 0.70, 0.85, 2, 2),
    Candidate("d2_only", 0.12, 0.70, 0.85, 2, 2),
    Candidate("d2_entry_72_85", 0.12, 0.72, 0.85, 2, 2),
    Candidate("d2_ecmwf_only", 0.15, 0.70, 0.85, 2, 2, sources=("ecmwf",)),
    Candidate("d2_ensemble_only", 0.15, 0.70, 0.85, 2, 2, sources=("ensemble",)),
    Candidate("d2_gfs_only", 0.15, 0.70, 0.85, 2, 2, sources=("gfs",)),
    Candidate("d1_only", 0.12, 0.70, 0.85, 1, 1),
    Candidate("ev15_mixed", 0.15, 0.70, 0.85, 1, 2),
    Candidate("ev18_mixed", 0.18, 0.70, 0.85, 1, 2),
    Candidate("entry_70_80", 0.12, 0.70, 0.80, 1, 2),
    Candidate("entry_72_82", 0.12, 0.72, 0.82, 1, 2),
    Candidate("ecmwf_only", 0.12, 0.70, 0.85, 1, 2, sources=("ecmwf",)),
    Candidate("ensemble_only", 0.12, 0.70, 0.85, 1, 2, sources=("ensemble",)),
]


def load_paper_candidate() -> Candidate:
    try:
        raw = json.loads(PAPER_CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return Candidate("current_paper", 0.12, 0.70, 0.85, 1, 2)

    return Candidate(
        "current_paper",
        float(raw.get("min_ev", 0.12)),
        float(raw.get("min_no_entry", 0.70)),
        float(raw.get("max_no_entry", 0.85)),
        int(raw.get("min_horizon_days", 1)),
        int(raw.get("max_horizon_days", 2)),
        max_spread=float(raw.get("max_slippage", 0.15)),
    )


def load_paper_activation() -> str | None:
    try:
        raw = json.loads(PAPER_CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None
    activated = raw.get("_activated_at")
    return str(activated) if activated else None


def parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        ts = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return ts.astimezone(timezone.utc)


def wilson_interval(wins: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return 0.0, 0.0
    phat = wins / n
    denom = 1 + z * z / n
    center = (phat + z * z / (2 * n)) / denom
    radius = z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n) / denom
    return center - radius, center + radius


def bootstrap_roi(trades: list[dict[str, Any]], draws: int = 5000) -> tuple[float, float]:
    if not trades:
        return 0.0, 0.0
    rng = random.Random(RNG_SEED)
    values = []
    for _ in range(draws):
        sample = [trades[rng.randrange(len(trades))] for __ in range(len(trades))]
        cost = sum(t["cost"] for t in sample)
        pnl = sum(t["pnl"] for t in sample)
        values.append(pnl / cost if cost else 0.0)
    values.sort()
    return values[int(draws * 0.025)], values[int(draws * 0.975) - 1]


def load_closed_positions() -> list[dict[str, Any]]:
    if not DB_PATH.exists():
        return []
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT city, date, json_data FROM markets").fetchall()
    conn.close()

    out: list[dict[str, Any]] = []
    for row in rows:
        try:
            market = json.loads(row["json_data"])
        except Exception:
            continue
        market_date = market.get("date") or row["date"]
        for pos in market.get("positions", {}).values():
            if pos.get("status") != "closed":
                continue
            if pos.get("close_reason") == "paper_cancelled":
                continue
            if pos.get("pnl") is None:
                continue
            opened_at = pos.get("opened_at") or ""
            if opened_at < V3_START:
                continue
            opened = parse_ts(opened_at)
            if not opened:
                continue
            try:
                real_horizon = (
                    datetime.strptime(market_date, "%Y-%m-%d").date()
                    - opened.date()
                ).days
            except Exception:
                continue
            out.append(
                {
                    "city": market.get("city") or row["city"],
                    "city_name": market.get("city_name") or row["city"],
                    "date": market_date,
                    "side": str(pos.get("side", "")).lower(),
                    "entry": float(pos.get("entry_price") or 0.0),
                    "ev": float(pos.get("ev") or 0.0),
                    "spread": float(pos.get("spread") or 0.0),
                    "cost": float(pos.get("cost") or 0.0),
                    "pnl": float(pos.get("pnl") or 0.0),
                    "source": str(pos.get("forecast_source") or "").lower(),
                    "reason": str(pos.get("close_reason") or ""),
                    "opened_at": opened_at,
                    "real_horizon": real_horizon,
                }
            )
    return out


def filter_candidate(trades: list[dict[str, Any]], cand: Candidate) -> list[dict[str, Any]]:
    subset = []
    for trade in trades:
        if trade["side"] != "no":
            continue
        if trade["real_horizon"] < cand.min_horizon or trade["real_horizon"] > cand.max_horizon:
            continue
        if trade["entry"] < cand.min_entry or trade["entry"] > cand.max_entry:
            continue
        if trade["ev"] < cand.min_ev:
            continue
        if trade["spread"] > cand.max_spread:
            continue
        if cand.sources and trade["source"] not in cand.sources:
            continue
        subset.append(trade)
    return subset


def since(trades: list[dict[str, Any]], activated_at: str | None) -> list[dict[str, Any]]:
    if not activated_at:
        return []
    activated = parse_ts(activated_at)
    if not activated:
        return []
    return [
        trade for trade in trades
        if parse_ts(trade.get("opened_at")) and parse_ts(trade.get("opened_at")) >= activated
    ]


def metrics(trades: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(trades)
    wins = sum(1 for t in trades if t["pnl"] > 0)
    losses = n - wins
    pnl = sum(t["pnl"] for t in trades)
    cost = sum(t["cost"] for t in trades)
    avg_entry = sum(t["entry"] for t in trades) / n if n else 0.0
    avg_ev = sum(t["ev"] for t in trades) / n if n else 0.0
    avg_spread = sum(t["spread"] for t in trades) / n if n else 0.0
    fee_est = sum(t["cost"] * TAKER_FEE_RATE * t["entry"] * (1 - t["entry"]) for t in trades)
    spread_est = sum(t["cost"] * SPREAD_DRAG_RATE for t in trades)
    pnl_after_drag = pnl - fee_est - spread_est
    wr_lo, wr_hi = wilson_interval(wins, n)
    roi_lo, roi_hi = bootstrap_roi(trades)
    loss_pnl = [t["pnl"] for t in trades if t["pnl"] < 0]
    reasons: dict[str, int] = {}
    for t in trades:
        reasons[t["reason"]] = reasons.get(t["reason"], 0) + 1

    return {
        "n": n,
        "wins": wins,
        "losses": losses,
        "win_rate": round(wins / n, 4) if n else 0.0,
        "win_rate_wilson_low": round(wr_lo, 4),
        "win_rate_wilson_high": round(wr_hi, 4),
        "avg_entry": round(avg_entry, 4),
        "avg_ev": round(avg_ev, 4),
        "avg_spread": round(avg_spread, 4),
        "pnl": round(pnl, 2),
        "cost": round(cost, 2),
        "roi": round(pnl / cost, 4) if cost else 0.0,
        "fee_est": round(fee_est, 2),
        "spread_est": round(spread_est, 2),
        "pnl_after_drag": round(pnl_after_drag, 2),
        "roi_after_drag": round(pnl_after_drag / cost, 4) if cost else 0.0,
        "bootstrap_roi_low": round(roi_lo, 4),
        "bootstrap_roi_high": round(roi_hi, 4),
        "max_loss": round(min(loss_pnl), 2) if loss_pnl else 0.0,
        "reasons": dict(sorted(reasons.items())),
    }


def score(row: dict[str, Any]) -> float:
    m = row["metrics"]
    if m["n"] == 0:
        return -999.0
    sample_penalty = max(0, 50 - m["n"]) * 0.002
    downside_penalty = max(0.0, -m["bootstrap_roi_low"]) * 0.35
    return round(m["roi_after_drag"] - sample_penalty - downside_penalty, 5)


def candidate_to_overlay(cand: Candidate) -> dict[str, Any]:
    return {
        "_note": f"Auto-selected paper-only overlay from strategy_lab candidate {cand.name}.",
        "enable_yes_trading": False,
        "max_bet": 5.0,
        "min_ev": cand.min_ev,
        "max_slippage": cand.max_spread,
        "max_no_positions": 1,
        "min_no_entry": cand.min_entry,
        "max_no_entry": cand.max_entry,
        "min_horizon_days": cand.min_horizon,
        "max_horizon_days": cand.max_horizon,
        "max_total_open_cost": 20.0,
        "max_new_positions_per_run": 2,
        "no_stop_enabled": False,
        "no_forecast_exit": False,
    }


def breakdown(trades: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for trade in trades:
        groups.setdefault(str(trade.get(key) or "unknown"), []).append(trade)
    rows = []
    for value, subset in sorted(groups.items()):
        rows.append({"value": value, "metrics": metrics(subset)})
    rows.sort(key=lambda r: (r["metrics"]["roi_after_drag"], r["metrics"]["n"]), reverse=True)
    return rows


def materially_bad_d1(trades: list[dict[str, Any]]) -> bool:
    d1 = [t for t in trades if t["side"] == "no" and t["real_horizon"] == 1]
    if len(d1) < 10:
        return False
    return metrics(d1)["roi_after_drag"] <= 0


def sample_floor(cand: Candidate) -> int:
    return 15 if cand.min_horizon == 2 and cand.max_horizon == 2 else 20


def same_filter(left: Candidate, right: Candidate) -> bool:
    return (
        left.min_ev == right.min_ev
        and left.min_entry == right.min_entry
        and left.max_entry == right.max_entry
        and left.min_horizon == right.min_horizon
        and left.max_horizon == right.max_horizon
        and left.sources == right.sources
        and left.max_spread == right.max_spread
    )


def build_report() -> dict[str, Any]:
    closed = load_closed_positions()
    current_candidate = load_paper_candidate()
    activated_at = load_paper_activation()
    rows = []
    current_row: dict[str, Any] | None = None
    candidate_names = {c.name for c in CANDIDATES}
    candidates = [current_candidate] + [c for c in CANDIDATES if c.name not in {current_candidate.name}]
    if current_candidate.name in candidate_names:
        candidates = [current_candidate] + CANDIDATES

    for cand in candidates:
        subset = filter_candidate(closed, cand)
        row = {
            "candidate": cand.__dict__,
            "metrics": metrics(subset),
        }
        row["score"] = score(row)
        rows.append(row)
        if cand.name == "current_paper":
            current_row = row

    rows.sort(key=lambda r: (r["score"], r["metrics"]["n"]), reverse=True)
    best = rows[0] if rows else None
    current = current_row or best
    d2_ev15_row = next((r for r in rows if r["candidate"]["name"] == "d2_ev15"), None)

    action = "observe"
    reason = "Not enough evidence to change paper strategy."
    overlay = None
    if best and current:
        best_m = best["metrics"]
        current_m = current["metrics"]
        best_cand = Candidate(**best["candidate"])
        current_cand = Candidate(**current["candidate"])
        best_is_safe_sample = best_m["n"] >= sample_floor(best_cand) and best_m["roi_after_drag"] > 0
        beats_current = best["score"] >= current["score"] + 0.015
        current_bad = current_m["n"] >= 20 and current_m["roi_after_drag"] <= 0
        d1_bad = materially_bad_d1(closed)
        if best["candidate"]["name"] == "current_paper" or same_filter(best_cand, current_cand):
            action = "keep"
            reason = "Current paper strategy remains the best risk-adjusted live-applicable candidate."
        elif (
            d2_ev15_row
            and d1_bad
            and d2_ev15_row["metrics"]["n"] >= 15
            and d2_ev15_row["metrics"]["roi_after_drag"] > current_m["roi_after_drag"]
            and not same_filter(Candidate(**d2_ev15_row["candidate"]), current_cand)
        ):
            action = "adapt_paper"
            reason = "D+1 is negative and D+2 ev15 is the strongest live-applicable thesis for paper testing."
            overlay = candidate_to_overlay(Candidate(**d2_ev15_row["candidate"]))
        elif best_is_safe_sample and (beats_current or current_bad):
            action = "adapt_paper"
            reason = "Best candidate beats current risk-adjusted score enough for paper testing."
            overlay = candidate_to_overlay(Candidate(**best["candidate"]))
        else:
            action = "keep"
            reason = "A variant ranks higher, but the improvement is too weak for automatic adaptation."

    live_ready = False
    live_reasons = []
    post_activation_metrics: dict[str, Any] | None = None
    if current:
        m = current["metrics"]
        current_cand = Candidate(**current["candidate"])
        d2_only_live = current_cand.min_horizon == 2 and current_cand.max_horizon == 2
        post_activation = since(filter_candidate(closed, current_cand), activated_at)
        post_activation_metrics = metrics(post_activation)
        live_checks = [
            (m["n"] >= 100, f"need >=100 resolved trades, have {m['n']}"),
            (
                post_activation_metrics["n"] >= 30,
                f"need >=30 post-activation resolved trades, have {post_activation_metrics['n']}",
            ),
            (m["roi_after_drag"] >= 0.03, f"need >=3% ROI after fee/spread drag, have {m['roi_after_drag'] * 100:.2f}%"),
            (
                post_activation_metrics["n"] == 0 or post_activation_metrics["roi_after_drag"] >= 0.03,
                f"need post-activation ROI after drag >=3%, have {post_activation_metrics['roi_after_drag'] * 100:.2f}%",
            ),
            (m["bootstrap_roi_low"] > 0, f"need positive bootstrap lower bound, have {m['bootstrap_roi_low'] * 100:.2f}%"),
            (m["win_rate"] > m["avg_entry"] + 0.03, "need win rate at least 3 points over avg NO breakeven"),
            (d2_only_live, "current paper strategy must be D+2-only before live review"),
        ]
        live_ready = all(ok for ok, _ in live_checks)
        live_reasons = [msg for ok, msg in live_checks if not ok]

    no_v3 = [t for t in closed if t["side"] == "no" and t["real_horizon"] >= 1]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_db": str(DB_PATH.relative_to(ROOT)),
        "closed_positions_loaded": len(closed),
        "paper_activation": {
            "activated_at": activated_at,
            "current_post_activation_metrics": post_activation_metrics or metrics([]),
        },
        "rows": rows,
        "diagnostics": {
            "by_horizon": breakdown(no_v3, "real_horizon"),
            "by_source": breakdown(no_v3, "source"),
        },
        "recommendation": {
            "action": action,
            "reason": reason,
            "best_candidate": best["candidate"]["name"] if best else None,
            "current_score": current["score"] if current else None,
            "best_score": best["score"] if best else None,
            "paper_overlay": overlay,
        },
        "live_gate": {
            "ready_for_user_review": live_ready,
            "reasons_not_ready": live_reasons,
        },
    }


def markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Strategy Lab",
        f"Generated: {report['generated_at']}",
        "",
        "## Recommendation",
        "",
        f"- Action: `{report['recommendation']['action']}`",
        f"- Best candidate: `{report['recommendation']['best_candidate']}`",
        f"- Reason: {report['recommendation']['reason']}",
        f"- Ready for live user review: `{report['live_gate']['ready_for_user_review']}`",
        f"- Paper policy activated at: `{report['paper_activation']['activated_at'] or 'unknown'}`",
    ]
    if report["live_gate"]["reasons_not_ready"]:
        lines.append("- Live blockers:")
        for reason in report["live_gate"]["reasons_not_ready"]:
            lines.append(f"  - {reason}")

    lines.extend(
        [
            "",
            "## Ranked Candidates",
            "",
            "| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for i, row in enumerate(report["rows"], 1):
        m = row["metrics"]
        lines.append(
            f"| {i} | {row['candidate']['name']} | {m['n']} | "
            f"{m['wins']}/{m['losses']} | {m['roi'] * 100:.2f}% | "
            f"{m['roi_after_drag'] * 100:.2f}% | {m['bootstrap_roi_low'] * 100:.2f}% | "
            f"{m['avg_entry']:.3f} | {row['score']:.4f} |"
        )

    post = report["paper_activation"]["current_post_activation_metrics"]
    lines.extend(
        [
            "",
            "## Post-Activation Current Paper",
            "",
            "| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
            (
                f"| {post['n']} | {post['wins']}/{post['losses']} | "
                f"{post['roi'] * 100:.2f}% | {post['roi_after_drag'] * 100:.2f}% | "
                f"{post['bootstrap_roi_low'] * 100:.2f}% | {post['avg_entry']:.3f} |"
            ),
        ]
    )

    lines.extend(
        [
            "",
            "## Diagnostics By Horizon",
            "",
            "| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in report["diagnostics"]["by_horizon"]:
        m = row["metrics"]
        lines.append(
            f"| D+{row['value']} | {m['n']} | {m['wins']}/{m['losses']} | "
            f"{m['roi_after_drag'] * 100:.2f}% | {m['bootstrap_roi_low'] * 100:.2f}% | "
            f"{m['avg_entry']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## Diagnostics By Source",
            "",
            "| Source | N | W/L | ROI after drag | Boot ROI low | Entry |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in report["diagnostics"]["by_source"]:
        m = row["metrics"]
        lines.append(
            f"| {row['value'].upper()} | {m['n']} | {m['wins']}/{m['losses']} | "
            f"{m['roi_after_drag'] * 100:.2f}% | {m['bootstrap_roi_low'] * 100:.2f}% | "
            f"{m['avg_entry']:.3f} |"
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank WeatherBot paper strategy variants.")
    parser.add_argument("--write", action="store_true", help="Write latest reports to data/strategy_lab.")
    args = parser.parse_args()

    report = build_report()
    text = markdown(report)
    if args.write:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        LATEST_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        LATEST_MD.write_text(text, encoding="utf-8")
        print(f"Wrote {LATEST_MD.relative_to(ROOT)}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
