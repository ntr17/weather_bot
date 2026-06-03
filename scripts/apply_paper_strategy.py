#!/usr/bin/env python3
"""Apply the paper-only strategy overlay to config.json.

This is used by scheduled paper runs. It deliberately accepts only a small
allowlist of non-secret strategy fields and enforces conservative rails.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.json"
PAPER_PATH = ROOT / "config.paper.json"

ALLOWED_FIELDS = {
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


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_overlay(overlay: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    unknown = sorted(k for k in overlay if not k.startswith("_") and k not in ALLOWED_FIELDS)
    if unknown:
        problems.append(f"unknown fields are not allowed: {', '.join(unknown)}")

    if overlay.get("enable_yes_trading") is not False:
        problems.append("paper brain must keep enable_yes_trading=false")
    if float(overlay.get("max_bet", 0)) > 5:
        problems.append("max_bet must be <= 5")
    if float(overlay.get("max_total_open_cost", 0)) > 20:
        problems.append("max_total_open_cost must be <= 20")
    if int(overlay.get("max_new_positions_per_run", 0)) > 2:
        problems.append("max_new_positions_per_run must be <= 2")
    if int(overlay.get("max_no_positions", 0)) > 2:
        problems.append("max_no_positions must be <= 2")
    if float(overlay.get("min_ev", 1)) < 0.10:
        problems.append("min_ev must be >= 0.10")
    if float(overlay.get("min_no_entry", 1)) < 0.65:
        problems.append("min_no_entry must be >= 0.65")
    if float(overlay.get("max_no_entry", 0)) > 0.90:
        problems.append("max_no_entry must be <= 0.90")
    if int(overlay.get("min_horizon_days", 99)) < 1:
        problems.append("min_horizon_days must be >= 1")
    if int(overlay.get("max_horizon_days", 0)) > 2:
        problems.append("max_horizon_days must be <= 2")
    if int(overlay.get("min_horizon_days", 1)) > int(overlay.get("max_horizon_days", 2)):
        problems.append("min_horizon_days cannot exceed max_horizon_days")
    if overlay.get("no_stop_enabled") is not False:
        problems.append("paper brain must keep no_stop_enabled=false")
    if overlay.get("no_forecast_exit") is not False:
        problems.append("paper brain must keep no_forecast_exit=false")

    return problems


def main() -> int:
    if not PAPER_PATH.exists():
        print("No config.paper.json overlay found; using config.json as-is.")
        return 0
    if not CONFIG_PATH.exists():
        print("config.json does not exist; copy config.template.json first.", file=sys.stderr)
        return 2

    config = load_json(CONFIG_PATH)
    overlay = load_json(PAPER_PATH)
    problems = validate_overlay(overlay)
    if problems:
        print("Unsafe paper overlay:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 2

    for key, value in overlay.items():
        if key.startswith("_"):
            continue
        config[key] = value

    CONFIG_PATH.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Applied paper strategy overlay from {PAPER_PATH.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

