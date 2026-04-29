"""Append resolved trades to logs/paper_trades.jsonl for later analysis."""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

LOGS_DIR = Path(__file__).parent.parent / "logs"
TRADE_LOG = LOGS_DIR / "paper_trades.jsonl"


def append_trade(mkt: dict[str, Any]) -> None:
    """Append one resolved market to the trade log. No-op if position missing."""
    pos = mkt.get("position")
    if not pos:
        return

    LOGS_DIR.mkdir(exist_ok=True)

    record = {
        "ts":              datetime.now(timezone.utc).isoformat(),
        "city":            mkt.get("city"),
        "city_name":       mkt.get("city_name"),
        "date":            mkt.get("date"),
        "unit":            mkt.get("unit"),
        "station":         mkt.get("station"),
        "horizon":         mkt.get("current_horizon"),
        "side":            pos.get("side", "yes"),
        "bucket_low":      pos.get("bucket_low"),
        "bucket_high":     pos.get("bucket_high"),
        "entry_price":     pos.get("entry_price"),
        "exit_price":      pos.get("exit_price"),
        "shares":          pos.get("shares"),
        "cost":            pos.get("cost"),
        "pnl":             pos.get("pnl"),
        "p":               pos.get("p"),
        "ev":              pos.get("ev"),
        "sigma":           pos.get("sigma"),
        "forecast_temp":   pos.get("forecast_temp"),
        "forecast_source": pos.get("forecast_source"),
        "actual_temp":     mkt.get("actual_temp"),
        "outcome":         mkt.get("resolved_outcome"),
        "reason":          pos.get("close_reason"),
        "opened_at":       pos.get("opened_at"),
        "closed_at":       pos.get("closed_at"),
    }

    with TRADE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
