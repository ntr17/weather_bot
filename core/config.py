"""
Configuration loader. Non-secret settings come from config.json.
Secrets (API keys, wallet key) come exclusively from .env / environment variables.
"""

import json
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

_CONFIG_PATH = Path(__file__).parent.parent / "config.json"


@dataclass(frozen=True)
class Config:
    # Trading parameters
    balance: float
    max_bet: float
    min_ev: float
    max_price: float        # max YES token price (don't buy expensive YES)
    max_no_price: float     # max NO token price — must be high (NO tokens are ~0.85-0.97)
    min_volume: float
    min_hours: float
    max_hours: float
    kelly_fraction: float
    max_slippage: float
    # Position management
    stop_loss_pct: float         # YES stop: close when price drops to entry * this
    no_stop_loss_pct: float      # NO stop: close when NO bid drops to entry * this (wider than YES)
    no_stop_loss_floor: float    # DEPRECATED — kept for back-compat
    trailing_activation: float   # trailing stop activates when price >= entry * this
    no_pyes_threshold: float     # only sell NO when p_yes < this
    max_no_positions: int         # max simultaneous NO positions per market/event
    min_yes_price: float         # min YES token price (skip extreme longshots)
    # Strategy v2 — NO-HOLD
    enable_yes_trading: bool     # False = NO-only mode (data shows no YES edge)
    min_no_entry: float          # min NO entry price (avoid cheap volatile NOs)
    max_no_entry: float          # max NO entry price
    no_stop_enabled: bool        # False = hold to resolution, no stop-loss on NOs
    no_forecast_exit: bool       # False = never exit NO on forecast change
    max_horizon_days: int        # max D+N horizon to trade (2 = D+0, D+1, D+2)
    # Operational
    scan_interval: int
    monitor_interval: int
    calibration_min: int
    # Secrets (from env only)
    vc_key: str
    polygon_private_key: str
    anthropic_api_key: str
    paper_trading: bool


def load_config() -> Config:
    """Load config from config.json + environment variables."""
    with open(_CONFIG_PATH, encoding="utf-8") as f:
        raw = json.load(f)

    vc_key = os.environ.get("VC_KEY", "")
    if not vc_key:
        raise EnvironmentError(
            "VC_KEY is not set. Add it to .env — required for resolution tracking and calibration."
        )

    return Config(
        balance=float(raw.get("balance", 10_000.0)),
        max_bet=float(raw.get("max_bet", 20.0)),
        min_ev=float(raw.get("min_ev", 0.10)),
        max_price=float(raw.get("max_price", 0.45)),
        max_no_price=float(raw.get("max_no_price", 0.97)),
        min_volume=float(raw.get("min_volume", 500)),
        min_hours=float(raw.get("min_hours", 2.0)),
        max_hours=float(raw.get("max_hours", 72.0)),
        kelly_fraction=float(raw.get("kelly_fraction", 0.25)),
        max_slippage=float(raw.get("max_slippage", 0.03)),
        stop_loss_pct=float(raw.get("stop_loss_pct", 0.80)),
        no_stop_loss_pct=float(raw.get("no_stop_loss_pct", 0.30)),
        no_stop_loss_floor=float(raw.get("no_stop_loss_floor", 0.85)),
        trailing_activation=float(raw.get("trailing_activation", 1.20)),
        no_pyes_threshold=float(raw.get("no_pyes_threshold", 0.15)),
        max_no_positions=int(raw.get("max_no_positions", 4)),
        min_yes_price=float(raw.get("min_yes_price", 0.05)),
        enable_yes_trading=raw.get("enable_yes_trading", False),
        min_no_entry=float(raw.get("min_no_entry", 0.65)),
        max_no_entry=float(raw.get("max_no_entry", 0.90)),
        no_stop_enabled=raw.get("no_stop_enabled", False),
        no_forecast_exit=raw.get("no_forecast_exit", False),
        max_horizon_days=int(raw.get("max_horizon_days", 2)),
        scan_interval=int(raw.get("scan_interval", 3600)),
        monitor_interval=int(raw.get("monitor_interval", 600)),
        calibration_min=int(raw.get("calibration_min", 30)),
        vc_key=vc_key,
        polygon_private_key=os.environ.get("POLYGON_PRIVATE_KEY", ""),
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY", ""),
        paper_trading=os.environ.get("PAPER_TRADING", "true").lower() != "false",
    )


# Default sigma before calibration kicks in (requires 30+ resolved trades).
# Temporary prior — replaced by bootstrap_sigma.py measurements and then
# refined by the live calibrator as resolved trades accumulate.
DEFAULT_SIGMA_F: float = 2.0   # Fahrenheit markets
DEFAULT_SIGMA_C: float = 1.2   # Celsius markets
