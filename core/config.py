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
    max_price: float
    min_volume: float
    min_hours: float
    max_hours: float
    kelly_fraction: float
    max_slippage: float
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
        min_volume=float(raw.get("min_volume", 500)),
        min_hours=float(raw.get("min_hours", 2.0)),
        max_hours=float(raw.get("max_hours", 72.0)),
        kelly_fraction=float(raw.get("kelly_fraction", 0.25)),
        max_slippage=float(raw.get("max_slippage", 0.03)),
        scan_interval=int(raw.get("scan_interval", 3600)),
        monitor_interval=int(raw.get("monitor_interval", 600)),
        calibration_min=int(raw.get("calibration_min", 30)),
        vc_key=vc_key,
        polygon_private_key=os.environ.get("POLYGON_PRIVATE_KEY", ""),
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY", ""),
        paper_trading=os.environ.get("PAPER_TRADING", "true").lower() != "false",
    )


# Default sigma before calibration kicks in (requires 30+ resolved trades)
DEFAULT_SIGMA_F: float = 2.0   # Fahrenheit markets
DEFAULT_SIGMA_C: float = 1.2   # Celsius markets
