#!/usr/bin/env python3
"""Generate an operating report for WeatherBot agent sessions.

The report is intentionally deterministic and secret-safe. It does not place
orders, does not require API keys, and does not call live trading endpoints.
Use it as the first command in a project session.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "weatherbot.db"
CONFIG_PATH = ROOT / "config.json"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "bot.yml"
REPORT_PATH = ROOT / "data" / "autonomy_report.md"
V3_START = "2026-05-14"


def run_git(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception as exc:
        return f"git error: {exc}"
    output = (result.stdout or result.stderr).strip()
    return output or "(no output)"


def git_ref_exists(ref: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", ref],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.returncode == 0


def best_remote_ref() -> str | None:
    for ref in ("github/master", "origin/master"):
        if git_ref_exists(ref):
            return ref
    return None


def parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        clean = value.replace("Z", "+00:00")
        ts = datetime.fromisoformat(clean)
    except ValueError:
        return None
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return ts.astimezone(timezone.utc)


def read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def workflow_forces_paper() -> bool:
    try:
        text = WORKFLOW_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return False
    return 'PAPER_TRADING: "true"' in text or "PAPER_TRADING: 'true'" in text


def connect_db() -> sqlite3.Connection | None:
    if not DB_PATH.exists():
        return None
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def table_exists(conn: sqlite3.Connection, name: str) -> bool:
    row = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (name,),
    ).fetchone()
    return row is not None


def get_state(conn: sqlite3.Connection) -> dict[str, Any]:
    if not table_exists(conn, "state"):
        return {}
    row = conn.execute("SELECT json_data FROM state LIMIT 1").fetchone()
    if not row:
        return {}
    try:
        return json.loads(row["json_data"])
    except Exception:
        return {}


def get_activity(conn: sqlite3.Connection) -> dict[str, Any]:
    if not table_exists(conn, "run_log"):
        return {}

    now = datetime.now(timezone.utc)
    one_hour = (now - timedelta(hours=1)).isoformat()
    two_hours = (now - timedelta(hours=2)).isoformat()
    one_day = (now - timedelta(days=1)).isoformat()

    last = conn.execute(
        "SELECT ts, city, status, new_pos, closed, resolved, error "
        "FROM run_log ORDER BY id DESC LIMIT 1"
    ).fetchone()
    runs_1h = conn.execute("SELECT COUNT(*) FROM run_log WHERE ts >= ?", (one_hour,)).fetchone()[0]
    runs_2h = conn.execute("SELECT COUNT(*) FROM run_log WHERE ts >= ?", (two_hours,)).fetchone()[0]
    runs_24h = conn.execute("SELECT COUNT(*) FROM run_log WHERE ts >= ?", (one_day,)).fetchone()[0]
    new_24h = conn.execute("SELECT SUM(new_pos) FROM run_log WHERE ts >= ?", (one_day,)).fetchone()[0] or 0
    errors_24h = conn.execute(
        "SELECT COUNT(*) FROM run_log WHERE ts >= ? AND error IS NOT NULL",
        (one_day,),
    ).fetchone()[0]

    last_ts = parse_ts(last["ts"]) if last else None
    age_min = None
    if last_ts:
        age_min = round((now - last_ts).total_seconds() / 60, 1)

    return {
        "last": dict(last) if last else None,
        "last_age_min": age_min,
        "runs_1h": runs_1h,
        "runs_2h": runs_2h,
        "runs_24h": runs_24h,
        "new_24h": int(new_24h),
        "errors_24h": errors_24h,
    }


def get_open_positions(conn: sqlite3.Connection) -> dict[str, Any]:
    if not table_exists(conn, "markets"):
        return {"count": 0, "cost": 0.0, "positions": []}

    positions: list[dict[str, Any]] = []
    rows = conn.execute("SELECT city, date, json_data FROM markets").fetchall()
    for row in rows:
        try:
            market = json.loads(row["json_data"])
        except Exception:
            continue
        for pos in market.get("positions", {}).values():
            if pos.get("status") != "open":
                continue
            positions.append(
                {
                    "city": market.get("city_name") or market.get("city") or row["city"],
                    "date": market.get("date") or row["date"],
                    "side": str(pos.get("side", "?")).upper(),
                    "entry": float(pos.get("entry_price") or 0.0),
                    "cost": float(pos.get("cost") or 0.0),
                    "source": str(pos.get("forecast_source") or "?").upper(),
                    "horizon": market.get("current_horizon", "?"),
                }
            )

    return {
        "count": len(positions),
        "cost": round(sum(p["cost"] for p in positions), 2),
        "positions": sorted(positions, key=lambda p: (p["date"], p["city"], p["entry"])),
    }


def get_live_evidence(conn: sqlite3.Connection) -> dict[str, int | bool]:
    if not table_exists(conn, "trades") or not table_exists(conn, "markets"):
        return {"live_trades": 0, "live_positions": 0, "has_live_evidence": False}

    live_trades = conn.execute(
        "SELECT COUNT(*) FROM trades "
        "WHERE json_extract(json_data, '$.live_order_id') IS NOT NULL"
    ).fetchone()[0]
    live_positions = conn.execute(
        "SELECT COUNT(*) FROM markets "
        "WHERE json_extract(json_data, '$.positions') LIKE '%live_order_id%' "
        "AND json_extract(json_data, '$.positions') NOT LIKE '%\"live_order_id\": null%' "
        "AND json_extract(json_data, '$.positions') NOT LIKE '%\"live_order_id\": \"NONE\"%'"
    ).fetchone()[0]
    return {
        "live_trades": live_trades,
        "live_positions": live_positions,
        "has_live_evidence": live_trades > 0 or live_positions > 0,
    }


def get_v3_actual(conn: sqlite3.Connection) -> dict[str, Any]:
    if not table_exists(conn, "markets"):
        return {"n": 0, "wins": 0, "losses": 0, "pnl": 0.0, "cost": 0.0, "roi": 0.0}

    trades: list[dict[str, Any]] = []
    rows = conn.execute("SELECT city, date, json_data FROM markets").fetchall()
    for row in rows:
        try:
            market = json.loads(row["json_data"])
        except Exception:
            continue
        market_date = market.get("date") or row["date"]
        for pos in market.get("positions", {}).values():
            if pos.get("status") != "closed":
                continue
            if pos.get("side") != "no":
                continue
            if (pos.get("opened_at") or "") < V3_START:
                continue
            if pos.get("close_reason") == "paper_cancelled" or pos.get("pnl") is None:
                continue
            opened = parse_ts(pos.get("opened_at"))
            if not opened:
                continue
            try:
                horizon = (
                    datetime.strptime(market_date, "%Y-%m-%d").date()
                    - opened.date()
                ).days
            except Exception:
                continue
            if horizon < 1:
                continue
            trades.append(pos)

    pnl = sum(float(t.get("pnl") or 0.0) for t in trades)
    cost = sum(float(t.get("cost") or 0.0) for t in trades)
    wins = sum(1 for t in trades if float(t.get("pnl") or 0.0) > 0)
    losses = len(trades) - wins
    avg_entry = (
        sum(float(t.get("entry_price") or 0.0) for t in trades) / len(trades)
        if trades
        else 0.0
    )
    return {
        "n": len(trades),
        "wins": wins,
        "losses": losses,
        "pnl": round(pnl, 2),
        "cost": round(cost, 2),
        "roi": round(pnl / cost, 4) if cost else 0.0,
        "avg_entry": round(avg_entry, 3),
    }


def status_label(ok: bool, hard: bool = False) -> str:
    if ok:
        return "OK"
    return "BLOCK" if hard else "WARN"


def build_gate_rows(
    cfg: dict[str, Any],
    activity: dict[str, Any],
    open_pos: dict[str, Any],
    edge: dict[str, Any],
) -> list[tuple[str, str, str]]:
    max_bet = float(cfg.get("max_bet", 0.0) or 0.0)
    max_open = float(cfg.get("max_total_open_cost", 0.0) or 0.0)
    max_new = int(cfg.get("max_new_positions_per_run", 0) or 0)
    min_ev = float(cfg.get("min_ev", 0.0) or 0.0)
    min_no = float(cfg.get("min_no_entry", 0.0) or 0.0)
    max_no = float(cfg.get("max_no_entry", 1.0) or 1.0)

    rows = [
        (
            "Actions paper-only",
            status_label(workflow_forces_paper(), hard=True),
            "Hosted Actions must not be live.",
        ),
        (
            "Recent bot activity",
            status_label(activity.get("runs_2h", 0) > 0, hard=True),
            f"{activity.get('runs_2h', 0)} runs in last 2h.",
        ),
        (
            "New data flow",
            status_label(activity.get("new_24h", 0) > 0),
            f"{activity.get('new_24h', 0)} new positions in last 24h; caps may explain zero.",
        ),
        (
            "Live max bet",
            status_label(0 < max_bet <= 5, hard=True),
            f"max_bet={max_bet:.2f}; target <= 5.",
        ),
        (
            "Live total exposure cap",
            status_label(0 < max_open <= 20, hard=True),
            f"max_total_open_cost={max_open:.2f}; target <= 20.",
        ),
        (
            "Current open exposure",
            status_label(max_open > 0 and open_pos["cost"] <= max_open),
            f"open_cost={open_pos['cost']:.2f}; reset/wait before live if above cap.",
        ),
        (
            "Per-run position cap",
            status_label(0 < max_new <= 2, hard=True),
            f"max_new_positions_per_run={max_new}; target <= 2.",
        ),
        (
            "NO-only strategy",
            status_label(cfg.get("enable_yes_trading") is False, hard=True),
            f"enable_yes_trading={cfg.get('enable_yes_trading')}.",
        ),
        (
            "Entry and EV filters",
            status_label(min_ev >= 0.12 and min_no >= 0.70 and max_no <= 0.85, hard=True),
            f"min_ev={min_ev:.2f}, min_no_entry={min_no:.2f}, max_no_entry={max_no:.2f}.",
        ),
        (
            "Resolved edge sample",
            status_label(edge["n"] >= 50),
            f"v3_actual n={edge['n']}; keep small while sample is limited.",
        ),
    ]
    return rows


def markdown_report(fetch: bool = False) -> str:
    if fetch:
        run_git(["fetch", "github", "master"])

    now = datetime.now(timezone.utc)
    cfg = read_json(CONFIG_PATH, {})
    git_status = run_git(["status", "--short", "--branch"])
    last_commit = run_git(["log", "--oneline", "-1", "HEAD"])
    remote_ref = best_remote_ref()
    remote_commit = run_git(["log", "--oneline", "-1", remote_ref]) if remote_ref else "(remote ref unavailable)"
    env_mode = os.environ.get("PAPER_TRADING", "(unset: code defaults to paper)")

    conn = connect_db()
    if conn:
        state = get_state(conn)
        activity = get_activity(conn)
        open_pos = get_open_positions(conn)
        live = get_live_evidence(conn)
        edge = get_v3_actual(conn)
        conn.close()
    else:
        state = {}
        activity = {}
        open_pos = {"count": 0, "cost": 0.0, "positions": []}
        live = {"live_trades": 0, "live_positions": 0, "has_live_evidence": False}
        edge = {"n": 0, "wins": 0, "losses": 0, "pnl": 0.0, "cost": 0.0, "roi": 0.0}

    gate_rows = build_gate_rows(cfg, activity, open_pos, edge)

    agenda = []
    if "behind" in git_status:
        agenda.append("Fast-forward local master from github/master before editing.")
    if activity.get("runs_2h", 0) == 0:
        agenda.append("Fix paper deployment or scheduler before discussing strategy.")
    if open_pos["cost"] > float(cfg.get("max_total_open_cost", 0.0) or 0.0):
        agenda.append("Do not launch live until open paper exposure is closed or reset.")
    if edge["n"] < 50:
        agenda.append("Keep collecting resolved paper data; edge sample is still small.")
    agenda.extend(
        [
            "Prepare compliant non-Actions live runner only after geoblock preflight passes.",
            "Run fee/spread-aware edge audit before first live order.",
            "Keep live launch capped at 5 USDC orders and 20 USDC total exposure.",
        ]
    )

    lines = [
        "# WeatherBot Autonomy Report",
        f"Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Git",
        "",
        f"- Local HEAD: `{last_commit}`",
        f"- Remote master: `{remote_commit}`",
        "```text",
        git_status,
        "```",
        "",
        "## Mode",
        "",
        f"- Hosted Actions forced paper: `{workflow_forces_paper()}`",
        f"- Local `PAPER_TRADING`: `{env_mode}`",
        f"- Live evidence in DB: `{live['has_live_evidence']}` "
        f"({live['live_trades']} trades, {live['live_positions']} markets)",
        "",
        "## Config Caps",
        "",
        "| Field | Value |",
        "| --- | ---: |",
        f"| balance | {float(cfg.get('balance', 0.0) or 0.0):.2f} |",
        f"| max_bet | {float(cfg.get('max_bet', 0.0) or 0.0):.2f} |",
        f"| min_ev | {float(cfg.get('min_ev', 0.0) or 0.0):.2f} |",
        f"| min_no_entry | {float(cfg.get('min_no_entry', 0.0) or 0.0):.2f} |",
        f"| max_no_entry | {float(cfg.get('max_no_entry', 0.0) or 0.0):.2f} |",
        f"| max_total_open_cost | {float(cfg.get('max_total_open_cost', 0.0) or 0.0):.2f} |",
        f"| max_new_positions_per_run | {int(cfg.get('max_new_positions_per_run', 0) or 0)} |",
        f"| enable_yes_trading | {cfg.get('enable_yes_trading')} |",
        "",
        "## Activity",
        "",
        f"- Last run age: `{activity.get('last_age_min', 'unknown')}` minutes",
        f"- Runs last 1h / 2h / 24h: `{activity.get('runs_1h', 0)}` / "
        f"`{activity.get('runs_2h', 0)}` / `{activity.get('runs_24h', 0)}`",
        f"- New positions last 24h: `{activity.get('new_24h', 0)}`",
        f"- Errors last 24h: `{activity.get('errors_24h', 0)}`",
        f"- State balance: `${float(state.get('balance', 0.0) or 0.0):.2f}`",
        f"- Open positions: `{open_pos['count']}`",
        f"- Open cost: `${open_pos['cost']:.2f}`",
        "",
        "## V3 Actual Edge",
        "",
        f"- Trades: `{edge['n']}` ({edge['wins']}W / {edge['losses']}L)",
        f"- Avg entry: `{edge.get('avg_entry', 0.0):.3f}`",
        f"- PnL: `${edge['pnl']:+.2f}` on `${edge['cost']:.2f}` cost",
        f"- ROI: `{edge['roi'] * 100:.2f}%`",
        "",
        "## Gates",
        "",
        "| Gate | Status | Detail |",
        "| --- | --- | --- |",
    ]
    for name, status, detail in gate_rows:
        lines.append(f"| {name} | {status} | {detail} |")

    lines.extend(
        [
            "",
            "## Agenda",
            "",
        ]
    )
    for item in agenda:
        lines.append(f"- {item}")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate WeatherBot autonomy report.")
    parser.add_argument("--fetch", action="store_true", help="Fetch github/master before reporting.")
    parser.add_argument("--write", action="store_true", help="Write report to data/autonomy_report.md.")
    args = parser.parse_args()

    report = markdown_report(fetch=args.fetch)
    if args.write:
        REPORT_PATH.parent.mkdir(exist_ok=True)
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"Wrote {REPORT_PATH.relative_to(ROOT)}")
    else:
        print(report)


if __name__ == "__main__":
    main()
