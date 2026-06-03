#!/usr/bin/env python3
"""WeatherBot paper supervisor.

This script is the repo-native "brain" for unattended paper trading. It reads
strategy_lab output, updates a project journal, and may adapt only the tracked
paper overlay. It cannot enable live trading.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from apply_paper_strategy import validate_overlay


ROOT = Path(__file__).resolve().parent.parent
LAB_JSON = ROOT / "data" / "strategy_lab" / "latest.json"
AUTONOMY_MD = ROOT / "data" / "autonomy_report.md"
PAPER_CONFIG = ROOT / "config.paper.json"
BRAIN_MD = ROOT / "BRAIN.md"
BRAIN_DIR = ROOT / "data" / "brain"
LATEST_MD = BRAIN_DIR / "latest.md"
STATE_JSON = BRAIN_DIR / "state.json"
LEDGER = BRAIN_DIR / "ledger.jsonl"


def read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def read_text(path: Path, default: str = "") -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return default


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_overlay(overlay: dict[str, Any]) -> dict[str, Any]:
    allowed = {
        key: value
        for key, value in overlay.items()
        if key.startswith("_") or key in {
            "enable_yes_trading",
            "max_bet",
            "min_ev",
            "max_slippage",
            "max_no_positions",
            "min_no_entry",
            "max_no_entry",
            "min_horizon_days",
            "max_horizon_days",
            "max_total_open_cost",
            "max_new_positions_per_run",
            "no_stop_enabled",
            "no_forecast_exit",
        }
    }
    return allowed


def maybe_apply_paper_overlay(lab: dict[str, Any], apply: bool) -> tuple[str, bool]:
    rec = lab.get("recommendation", {})
    if rec.get("action") != "adapt_paper":
        return "No paper config change requested.", False
    overlay = rec.get("paper_overlay")
    if not isinstance(overlay, dict):
        return "Strategy lab requested adaptation but did not provide an overlay.", False

    overlay = normalize_overlay(overlay)
    problems = validate_overlay(overlay)
    if problems:
        return "Paper overlay rejected: " + "; ".join(problems), False
    if not apply:
        return "Paper overlay would change, but --apply was not set.", False

    current = read_json(PAPER_CONFIG, {})
    comparable_current = {k: v for k, v in current.items() if not k.startswith("_")}
    comparable_next = {k: v for k, v in overlay.items() if not k.startswith("_")}
    if comparable_current == comparable_next:
        return "Recommended paper overlay already active.", False

    write_json(PAPER_CONFIG, overlay)
    return f"Updated {PAPER_CONFIG.name} to paper candidate `{rec.get('best_candidate')}`.", True


def best_row(lab: dict[str, Any]) -> dict[str, Any]:
    rows = lab.get("rows") or []
    return rows[0] if rows else {}


def current_row(lab: dict[str, Any]) -> dict[str, Any]:
    for row in lab.get("rows") or []:
        if row.get("candidate", {}).get("name") == "current_safe":
            return row
    return {}


def render(lab: dict[str, Any], action_result: str, changed: bool) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rec = lab.get("recommendation", {})
    live = lab.get("live_gate", {})
    best = best_row(lab)
    current = current_row(lab)
    best_m = best.get("metrics", {})
    current_m = current.get("metrics", {})

    lines = [
        "# WeatherBot Brain",
        f"Last review: {now}",
        "",
        "## Decision",
        "",
        f"- Paper action: `{rec.get('action', 'unknown')}`",
        f"- Best candidate: `{rec.get('best_candidate', 'unknown')}`",
        f"- Paper config changed: `{changed}`",
        f"- Action result: {action_result}",
        f"- Ready for live user review: `{live.get('ready_for_user_review', False)}`",
        "",
        "## Evidence",
        "",
        f"- Closed positions loaded: `{lab.get('closed_positions_loaded', 0)}`",
        f"- Current strategy: n={current_m.get('n', 0)}, "
        f"ROI after drag={current_m.get('roi_after_drag', 0) * 100:.2f}%, "
        f"bootstrap low={current_m.get('bootstrap_roi_low', 0) * 100:.2f}%",
        f"- Best strategy: n={best_m.get('n', 0)}, "
        f"ROI after drag={best_m.get('roi_after_drag', 0) * 100:.2f}%, "
        f"bootstrap low={best_m.get('bootstrap_roi_low', 0) * 100:.2f}%",
        "",
        "## Thesis",
        "",
        "- Main thesis: Polymarket exact-temperature weather buckets can overprice unlikely tails when market participants anchor on city-level intuition instead of airport-resolution forecasts.",
        "- Current exploitable shape: buy NO on non-forecast buckets, D+1/D+2, with entry and EV filters tight enough that one full-cost loss does not erase many weak wins.",
        "- The brain is currently optimizing paper filters only. Live mode remains locked behind user approval.",
        "",
        "## What I Am Watching",
        "",
        "- Whether D+2 continues to dominate D+1 after more resolved trades.",
        "- Whether take-profit exits are hiding unresolved full-loss risk.",
        "- Whether fee and spread drag turn the edge negative at 5 USDC order size.",
        "- Whether any city/source pair contributes repeated full-cost losses.",
        "- Whether deployment keeps producing fresh paper data every few hours.",
        "",
        "## Live Blockers",
        "",
    ]
    blockers = live.get("reasons_not_ready") or []
    if blockers:
        for blocker in blockers:
            lines.append(f"- {blocker}")
    else:
        lines.append("- Strategy evidence gate is clear; user review still required before live mode.")

    lines.extend(
        [
            "",
            "## Operating Rule",
            "",
            "The brain may change `config.paper.json` only. It may not set `PAPER_TRADING=false`, modify wallet secrets, or increase live risk. When ready, it writes the live-review case here and waits for the user.",
        ]
    )
    return "\n".join(lines) + "\n"


def append_ledger(lab: dict[str, Any], action_result: str, changed: bool) -> None:
    rec = lab.get("recommendation", {})
    row = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "action": rec.get("action"),
        "best_candidate": rec.get("best_candidate"),
        "changed": changed,
        "action_result": action_result,
        "ready_for_live_user_review": lab.get("live_gate", {}).get("ready_for_user_review", False),
        "current_score": rec.get("current_score"),
        "best_score": rec.get("best_score"),
    }
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the WeatherBot paper brain.")
    parser.add_argument("--apply", action="store_true", help="Allow safe paper overlay changes.")
    args = parser.parse_args()

    lab = read_json(LAB_JSON, {})
    if not lab:
        raise SystemExit("Missing strategy lab output. Run scripts/strategy_lab.py --write first.")

    action_result, changed = maybe_apply_paper_overlay(lab, apply=args.apply)
    report = render(lab, action_result, changed)
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    BRAIN_MD.write_text(report, encoding="utf-8")
    LATEST_MD.write_text(report, encoding="utf-8")
    write_json(
        STATE_JSON,
        {
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "last_action_result": action_result,
            "paper_config_changed": changed,
            "strategy_recommendation": lab.get("recommendation", {}),
            "live_gate": lab.get("live_gate", {}),
            "autonomy_report_present": AUTONOMY_MD.exists(),
        },
    )
    append_ledger(lab, action_result, changed)
    print(action_result)
    print(f"Wrote {BRAIN_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

