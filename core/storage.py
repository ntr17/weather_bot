"""
JSON persistence layer. One file per market, one state file, one calibration file.

All functions return new dicts — never mutate the input.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent / "data"
MARKETS_DIR = DATA_DIR / "markets"
STATE_FILE = DATA_DIR / "state.json"
CALIBRATION_FILE = DATA_DIR / "calibration.json"


def ensure_dirs() -> None:
    """Create data directories if they don't exist."""
    DATA_DIR.mkdir(exist_ok=True)
    MARKETS_DIR.mkdir(exist_ok=True)


# ── State (balance + aggregate stats) ────────────────────────────────────────

def load_state(starting_balance: float = 10_000.0) -> dict[str, Any]:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {
        "balance":          starting_balance,
        "starting_balance": starting_balance,
        "total_trades":     0,
        "wins":             0,
        "losses":           0,
        "peak_balance":     starting_balance,
    }


def save_state(state: dict[str, Any]) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


# ── Per-market records ────────────────────────────────────────────────────────

def market_path(city_slug: str, date_str: str) -> Path:
    return MARKETS_DIR / f"{city_slug}_{date_str}.json"


def load_market(city_slug: str, date_str: str) -> dict[str, Any] | None:
    p = market_path(city_slug, date_str)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def save_market(market: dict[str, Any]) -> None:
    p = market_path(market["city"], market["date"])
    p.write_text(json.dumps(market, indent=2, ensure_ascii=False), encoding="utf-8")


def load_all_markets() -> list[dict[str, Any]]:
    markets = []
    for f in MARKETS_DIR.glob("*.json"):
        try:
            markets.append(json.loads(f.read_text(encoding="utf-8")))
        except Exception:
            pass
    return markets


def new_market(
    city_slug: str,
    city_name: str,
    station: str,
    unit: str,
    date_str: str,
    end_date: str,
    hours_at_discovery: float,
) -> dict[str, Any]:
    return {
        "city":               city_slug,
        "city_name":          city_name,
        "date":               date_str,
        "unit":               unit,
        "station":            station,
        "event_end_date":     end_date,
        "hours_at_discovery": round(hours_at_discovery, 1),
        "status":             "open",       # open | closed | resolved
        "positions":          [],           # list of open/closed bucket positions
        "actual_temp":        None,
        "resolved_outcome":   None,         # win | loss | no_position
        "pnl":                None,
        "forecast_snapshots": [],
        "market_snapshots":   [],
        "all_outcomes":       [],
        "created_at":         datetime.now(timezone.utc).isoformat(),
    }


# ── Calibration ───────────────────────────────────────────────────────────────

def load_calibration() -> dict[str, Any]:
    if CALIBRATION_FILE.exists():
        return json.loads(CALIBRATION_FILE.read_text(encoding="utf-8"))
    return {}


def save_calibration(cal: dict[str, Any]) -> None:
    CALIBRATION_FILE.write_text(json.dumps(cal, indent=2), encoding="utf-8")
