#!/usr/bin/env python3
"""
verify.py — Independent bot health & liveness monitor.

Run this anytime to get a definitive answer:
  - Is the bot running?
  - Is it in LIVE or PAPER mode?
  - Has it placed any real CLOB orders?
  - Is it opening new positions or is it stuck?
  - What's the recent P&L?

Usage:
    python scripts/verify.py           # full check (pulls latest from github)
    python scripts/verify.py --local   # skip git pull, use local DB only
    python scripts/verify.py --watch   # pull + check every 30 min

This script trusts NOTHING. It reads raw data and draws its own conclusions.
"""

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "weatherbot.db"
STATUS_PATH = ROOT / "data" / "status.md"
SAFETY_PATH = ROOT / "data" / "safety.json"

# ─── Colors (works on Windows Terminal / modern terminals) ───────────────────
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


def ok(msg: str) -> str:
    return f"{GREEN}✓{RESET} {msg}"


def warn(msg: str) -> str:
    return f"{YELLOW}⚠{RESET} {msg}"


def fail(msg: str) -> str:
    return f"{RED}✗{RESET} {msg}"


# ─── Git operations ─────────────────────────────────────────────────────────

def pull_latest() -> bool:
    """Pull latest DB from GitHub. Returns True if successful."""
    try:
        # Stash local changes, pull remote, restore DB from remote
        subprocess.run(["git", "fetch", "github", "master"],
                       cwd=ROOT, capture_output=True, timeout=30)
        subprocess.run(
            ["git", "checkout", "github/master", "--",
             "data/weatherbot.db", "data/status.md", "data/safety.json"],
            cwd=ROOT, capture_output=True, timeout=10
        )
        return True
    except Exception as e:
        print(warn(f"Could not pull latest: {e}"))
        return False


def get_last_commit_time() -> datetime | None:
    """Get timestamp of latest 'bot: update state' commit."""
    try:
        result = subprocess.run(
            ["git", "log", "github/master", "--oneline", "--format=%aI", "-1"],
            cwd=ROOT, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            return datetime.fromisoformat(result.stdout.strip())
    except Exception:
        pass
    return None


def get_recent_commits(n: int = 5) -> list[str]:
    """Get last N commit messages."""
    try:
        result = subprocess.run(
            ["git", "log", "github/master", "--oneline", f"-{n}"],
            cwd=ROOT, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip().splitlines()
    except Exception:
        pass
    return []


# ─── Database queries ────────────────────────────────────────────────────────

def get_db() -> sqlite3.Connection:
    if not DB_PATH.exists():
        print(fail("Database not found at data/weatherbot.db"))
        sys.exit(1)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def check_mode(conn: sqlite3.Connection) -> dict:
    """Determine trading mode from evidence in the database."""
    cur = conn.cursor()

    # Check for ANY live_order_id in trades
    cur.execute("SELECT COUNT(*) FROM trades WHERE json_extract(json_data, '$.live_order_id') IS NOT NULL")
    live_trades = cur.fetchone()[0]

    # Check for live_order_id in market positions (json_data column)
    cur.execute("""
        SELECT COUNT(*) FROM markets
        WHERE json_extract(json_data, '$.positions') LIKE '%live_order_id%'
        AND json_extract(json_data, '$.positions') NOT LIKE '%"live_order_id": null%'
        AND json_extract(json_data, '$.positions') NOT LIKE '%"live_order_id": "NONE"%'
    """)
    live_positions = cur.fetchone()[0]

    return {
        "live_trades_in_log": live_trades,
        "live_positions_in_markets": live_positions,
        "has_any_live_evidence": live_trades > 0 or live_positions > 0,
    }


def check_activity(conn: sqlite3.Connection) -> dict:
    """Check recent bot activity."""
    cur = conn.cursor()
    now = datetime.now(timezone.utc)

    # Last run_log entry
    cur.execute("SELECT ts, city, status, new_pos, closed, resolved, error FROM run_log ORDER BY id DESC LIMIT 1")
    last_run = cur.fetchone()

    # Runs in last hour
    one_hour_ago = (now - timedelta(hours=1)).isoformat()
    cur.execute("SELECT COUNT(*) FROM run_log WHERE ts >= ?", (one_hour_ago,))
    runs_last_hour = cur.fetchone()[0]

    # Runs in last 24h
    one_day_ago = (now - timedelta(hours=24)).isoformat()
    cur.execute("SELECT COUNT(*) FROM run_log WHERE ts >= ?", (one_day_ago,))
    runs_last_24h = cur.fetchone()[0]

    # New positions in last 24h
    cur.execute("SELECT SUM(new_pos) FROM run_log WHERE ts >= ?", (one_day_ago,))
    new_pos_24h = cur.fetchone()[0] or 0

    # Errors in last 24h
    cur.execute("SELECT COUNT(*) FROM run_log WHERE ts >= ? AND error IS NOT NULL", (one_day_ago,))
    errors_24h = cur.fetchone()[0]

    # Last time a new position was opened
    cur.execute("SELECT MAX(opened_at) FROM trades")
    last_opened = cur.fetchone()[0]

    return {
        "last_run_ts": last_run["ts"] if last_run else None,
        "last_run_city": last_run["city"] if last_run else None,
        "last_run_status": last_run["status"] if last_run else None,
        "runs_last_hour": runs_last_hour,
        "runs_last_24h": runs_last_24h,
        "new_positions_24h": new_pos_24h,
        "errors_24h": errors_24h,
        "last_position_opened": last_opened,
    }


def check_performance(conn: sqlite3.Connection) -> dict:
    """Check trading performance."""
    cur = conn.cursor()

    # V3 trades (after May 14 cutover)
    cur.execute("""
        SELECT COUNT(*) as n,
               SUM(CASE WHEN pnl > 0 THEN 1 ELSE 0 END) as wins,
               SUM(CASE WHEN pnl < 0 THEN 1 ELSE 0 END) as losses,
               SUM(pnl) as total_pnl
        FROM trades
        WHERE opened_at >= '2026-05-14' AND reason != 'paper_cancelled'
    """)
    r = cur.fetchone()

    # Open positions count (from markets json)
    cur.execute("SELECT json_data FROM markets WHERE status = 'open'")
    open_count = 0
    for row in cur.fetchall():
        mkt = json.loads(row["json_data"])
        for pos in mkt.get("positions", {}).values():
            if pos.get("status") == "open":
                open_count += 1

    # State balance
    cur.execute("SELECT json_data FROM state LIMIT 1")
    state_row = cur.fetchone()
    balance = 54.0
    if state_row:
        state = json.loads(state_row["json_data"])
        balance = state.get("balance", 54.0)

    return {
        "v3_trades": r["n"] or 0,
        "v3_wins": r["wins"] or 0,
        "v3_losses": r["losses"] or 0,
        "v3_pnl": r["total_pnl"] or 0.0,
        "open_positions": open_count,
        "balance": balance,
    }


def check_blockers(conn: sqlite3.Connection) -> list[str]:
    """Check for known failure patterns. Returns list of problems."""
    problems = []
    cur = conn.cursor()
    now = datetime.now(timezone.utc)

    # 1. Bot not running (no runs in 2 hours)
    two_hours_ago = (now - timedelta(hours=2)).isoformat()
    cur.execute("SELECT COUNT(*) FROM run_log WHERE ts >= ?", (two_hours_ago,))
    if cur.fetchone()[0] == 0:
        problems.append("Bot has not run in 2+ hours")

    # 2. No new positions in 24h (was the re-entry blocking bug)
    one_day_ago = (now - timedelta(hours=24)).isoformat()
    cur.execute("SELECT SUM(new_pos) FROM run_log WHERE ts >= ?", (one_day_ago,))
    new_24h = cur.fetchone()[0] or 0
    if new_24h == 0:
        problems.append("Zero new positions opened in 24 hours — bot may be stuck")

    # 3. All recent errors
    cur.execute("SELECT COUNT(*), COUNT(DISTINCT city) FROM run_log WHERE ts >= ? AND error IS NOT NULL", (one_day_ago,))
    r = cur.fetchone()
    if r[0] > 10:
        problems.append(f"{r[0]} errors across {r[1]} cities in last 24h")

    # 4. Balance at zero or below reserve
    cur.execute("SELECT json_data FROM state LIMIT 1")
    state_row = cur.fetchone()
    if state_row:
        state = json.loads(state_row["json_data"])
        bal = state.get("balance", 0)
        if bal < 5:
            problems.append(f"Balance critically low: ${bal:.2f}")

    # 5. Safety kill switch active
    if SAFETY_PATH.exists():
        safety = json.loads(SAFETY_PATH.read_text())
        if safety.get("kill_switch"):
            problems.append("KILL SWITCH IS ACTIVE — all trading halted")

    # 6. paper_cancelled positions still blocking (the bug we just fixed)
    cur.execute("SELECT json_data FROM markets WHERE status = 'open'")
    blocked_markets = 0
    for row in cur.fetchall():
        mkt = json.loads(row["json_data"])
        positions = mkt.get("positions", {})
        cancelled = sum(1 for p in positions.values() if p.get("close_reason") == "paper_cancelled")
        if cancelled > 0:
            blocked_markets += 1
    if blocked_markets > 0:
        problems.append(f"{blocked_markets} markets still have paper_cancelled positions blocking re-entry")

    return problems


# ─── Main report ─────────────────────────────────────────────────────────────

def run_report(skip_pull: bool = False) -> None:
    now = datetime.now(timezone.utc)
    print(f"\n{BOLD}{'═' * 60}{RESET}")
    print(f"{BOLD}  WEATHERBOT VERIFICATION — {now.strftime('%Y-%m-%d %H:%M UTC')}{RESET}")
    print(f"{BOLD}{'═' * 60}{RESET}\n")

    # 1. Pull latest
    if not skip_pull:
        print("  Pulling latest from GitHub...", end=" ", flush=True)
        if pull_latest():
            print("done")
        else:
            print("failed (using local data)")

    # 2. Git commit activity
    print(f"\n{BOLD}── GIT ACTIVITY ──{RESET}")
    last_commit = get_last_commit_time()
    if last_commit:
        age = now - last_commit
        age_str = f"{int(age.total_seconds() // 60)} min ago"
        ts_str = last_commit.strftime("%H:%M UTC")
        msg = f"Last commit: {ts_str} ({age_str})"
        if age < timedelta(hours=1):
            print(f"  {ok(msg)}")
        elif age < timedelta(hours=2):
            print(f"  {warn(msg)}")
        else:
            print(f"  {fail(msg + ' — BOT MAY BE DOWN')}")
    else:
        print(f"  {warn('Could not determine last commit time')}")

    commits = get_recent_commits(5)
    if commits:
        print(f"  Recent commits:")
        for c in commits:
            print(f"    {c}")

    # 3. Database checks
    conn = get_db()

    print(f"\n{BOLD}── TRADING MODE ──{RESET}")
    mode = check_mode(conn)
    if mode["has_any_live_evidence"]:
        n_live = mode['live_trades_in_log']
        print(f"  {ok(f'LIVE MODE CONFIRMED — {n_live} live trades in log')}")
    else:
        print(f"  {fail('NO LIVE EVIDENCE — zero live_order_id found anywhere in DB')}")
        print(f"  This means either:")
        print(f"    a) PAPER_TRADING secret is not set to 'false'")
        print(f"    b) Bot is in live mode but hasn't found any eligible trades yet")
        print(f"    c) Live orders failed (check Actions logs for [ERROR])")

    print(f"\n{BOLD}── BOT ACTIVITY ──{RESET}")
    activity = check_activity(conn)
    if activity["last_run_ts"]:
        last_run = datetime.fromisoformat(activity["last_run_ts"])
        run_age = now - last_run
        run_age_str = f"{int(run_age.total_seconds() // 60)} min ago"
        run_msg = f"Last run: {activity['last_run_ts'][:19]} ({run_age_str})"
        if run_age < timedelta(hours=1):
            print(f"  {ok(run_msg)}")
        else:
            print(f"  {fail(run_msg)}")
    print(f"  Runs last hour: {activity['runs_last_hour']}")
    print(f"  Runs last 24h: {activity['runs_last_24h']}")
    print(f"  New positions (24h): {activity['new_positions_24h']}")
    print(f"  Errors (24h): {activity['errors_24h']}")
    print(f"  Last position opened: {activity['last_position_opened'] or 'never'}")

    print(f"\n{BOLD}── PERFORMANCE (V3, since May 14) ──{RESET}")
    perf = check_performance(conn)
    print(f"  Balance: ${perf['balance']:.2f}")
    print(f"  Open positions: {perf['open_positions']}")
    print(f"  Closed trades: {perf['v3_trades']} ({perf['v3_wins']}W / {perf['v3_losses']}L)")
    if perf["v3_wins"] + perf["v3_losses"] > 0:
        wr = perf["v3_wins"] / (perf["v3_wins"] + perf["v3_losses"]) * 100
        print(f"  Win rate: {wr:.1f}%")
    print(f"  P&L: ${perf['v3_pnl']:+.2f}")

    print(f"\n{BOLD}── BLOCKERS ──{RESET}")
    blockers = check_blockers(conn)
    if blockers:
        for b in blockers:
            print(f"  {fail(b)}")
    else:
        print(f"  {ok('No known blockers detected')}")

    # Final verdict
    print(f"\n{BOLD}{'─' * 60}{RESET}")
    all_good = (
        mode["has_any_live_evidence"]
        and activity["runs_last_hour"] > 0
        and activity["new_positions_24h"] > 0
        and len(blockers) == 0
    )
    if all_good:
        print(f"  {GREEN}{BOLD}VERDICT: BOT IS LIVE AND HEALTHY{RESET}")
    elif mode["has_any_live_evidence"]:
        print(f"  {YELLOW}{BOLD}VERDICT: LIVE BUT HAS ISSUES — check blockers above{RESET}")
    elif activity["runs_last_hour"] > 0:
        print(f"  {YELLOW}{BOLD}VERDICT: BOT IS RUNNING BUT NO LIVE TRADES YET{RESET}")
        print(f"  → Check GitHub Actions logs for the 'Run bot' step")
        print(f"  → Look for: 'WEATHERBOT — single cycle (LIVE)' vs '(PAPER)'")
        print(f"  → If it says PAPER: your PAPER_TRADING secret is wrong")
        print(f"  → If it says LIVE but no trades: no eligible markets right now (normal)")
    else:
        print(f"  {RED}{BOLD}VERDICT: BOT IS NOT RUNNING{RESET}")

    print(f"\n  {BOLD}To check Actions logs:{RESET}")
    print(f"  https://github.com/ntr17/weather_bot/actions")
    print(f"  Click latest run → 'Run bot (single cycle)' → read output\n")

    conn.close()


# ─── Entry point ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Verify weatherbot health & liveness")
    parser.add_argument("--local", action="store_true", help="Skip git pull, use local DB")
    parser.add_argument("--watch", action="store_true", help="Re-check every 30 minutes")
    args = parser.parse_args()

    if args.watch:
        while True:
            run_report(skip_pull=args.local)
            print(f"\n  Next check in 30 minutes... (Ctrl+C to stop)\n")
            time.sleep(1800)
    else:
        run_report(skip_pull=args.local)


if __name__ == "__main__":
    main()
