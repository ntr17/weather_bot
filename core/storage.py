"""
SQLite persistence layer — single data/weatherbot.db file.

Drop-in replacement for the old JSON-per-file storage.
Same public API: load_state, save_state, load_market, save_market, etc.

Schema:
  state        — single-row key/value (balance, wins, losses, etc.)
  markets      — one row per city+date, indexed city/date/status columns
                  + json_data column for the full nested dict
  calibration  — one row per calibration key (city_source_horizon)
  trades       — append-only resolved-trade log (replaces paper_trades.jsonl)
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent / "data"
DB_PATH = DATA_DIR / "weatherbot.db"

# Legacy paths — used only for one-time migration
_LEGACY_MARKETS_DIR = DATA_DIR / "markets"
_LEGACY_STATE_FILE = DATA_DIR / "state.json"
_LEGACY_CALIBRATION_FILE = DATA_DIR / "calibration.json"

# Module-level connection (reused within a single process)
_conn: sqlite3.Connection | None = None


def _get_conn() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        DATA_DIR.mkdir(exist_ok=True)
        _conn = sqlite3.connect(str(DB_PATH), timeout=10)
        _conn.execute("PRAGMA journal_mode=WAL")
        _conn.execute("PRAGMA foreign_keys=ON")
        _conn.row_factory = sqlite3.Row
        _init_schema(_conn)
        _migrate_legacy(_conn)
    return _conn


def _init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS state (
            id          INTEGER PRIMARY KEY CHECK (id = 1),
            json_data   TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS markets (
            city        TEXT NOT NULL,
            date        TEXT NOT NULL,
            status      TEXT NOT NULL DEFAULT 'open',
            json_data   TEXT NOT NULL,
            PRIMARY KEY (city, date)
        );
        CREATE INDEX IF NOT EXISTS idx_markets_status ON markets(status);

        CREATE TABLE IF NOT EXISTS calibration (
            key         TEXT PRIMARY KEY,
            sigma       REAL NOT NULL,
            mae         REAL,
            n           INTEGER,
            source      TEXT,
            updated_at  TEXT,
            json_data   TEXT
        );

        CREATE TABLE IF NOT EXISTS trades (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            ts              TEXT NOT NULL,
            city            TEXT,
            city_name       TEXT,
            date            TEXT,
            unit            TEXT,
            side            TEXT,
            bucket_low      REAL,
            bucket_high     REAL,
            entry_price     REAL,
            exit_price      REAL,
            shares          REAL,
            cost            REAL,
            pnl             REAL,
            p               REAL,
            ev              REAL,
            sigma           REAL,
            forecast_temp   REAL,
            forecast_source TEXT,
            actual_temp     REAL,
            outcome         TEXT,
            reason          TEXT,
            horizon         TEXT,
            opened_at       TEXT,
            closed_at       TEXT,
            json_data       TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_trades_city ON trades(city);
        CREATE INDEX IF NOT EXISTS idx_trades_date ON trades(date);

        CREATE TABLE IF NOT EXISTS run_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            ts          TEXT NOT NULL,
            city        TEXT NOT NULL,
            status      TEXT NOT NULL,   -- ok, timeout, error, skip
            error       TEXT,
            duration_s  REAL,
            new_pos     INTEGER DEFAULT 0,
            closed      INTEGER DEFAULT 0,
            resolved    INTEGER DEFAULT 0
        );
        CREATE INDEX IF NOT EXISTS idx_run_log_city ON run_log(city);
        CREATE INDEX IF NOT EXISTS idx_run_log_ts ON run_log(ts);
    """)
    conn.commit()


def _migrate_legacy(conn: sqlite3.Connection) -> None:
    """One-time migration: import existing JSON files into SQLite, then leave them."""
    # Skip if we already have data
    row = conn.execute("SELECT COUNT(*) AS cnt FROM markets").fetchone()
    if row["cnt"] > 0:
        return

    # Migrate state.json
    if _LEGACY_STATE_FILE.exists():
        try:
            state = json.loads(_LEGACY_STATE_FILE.read_text(encoding="utf-8"))
            conn.execute(
                "INSERT OR REPLACE INTO state (id, json_data) VALUES (1, ?)",
                (json.dumps(state, ensure_ascii=False),),
            )
        except Exception:
            pass

    # Migrate market JSON files
    if _LEGACY_MARKETS_DIR.exists():
        for f in _LEGACY_MARKETS_DIR.glob("*.json"):
            try:
                mkt = json.loads(f.read_text(encoding="utf-8"))
                conn.execute(
                    "INSERT OR REPLACE INTO markets (city, date, status, json_data) VALUES (?, ?, ?, ?)",
                    (mkt["city"], mkt["date"], mkt.get("status", "open"),
                     json.dumps(mkt, ensure_ascii=False)),
                )
            except Exception:
                pass

    # Migrate calibration.json
    if _LEGACY_CALIBRATION_FILE.exists():
        try:
            cal = json.loads(_LEGACY_CALIBRATION_FILE.read_text(encoding="utf-8"))
            for key, entry in cal.items():
                conn.execute(
                    """INSERT OR REPLACE INTO calibration
                       (key, sigma, mae, n, source, updated_at, json_data)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (key, entry.get("sigma", 0), entry.get("mae"),
                     entry.get("n"), entry.get("source"), entry.get("updated_at"),
                     json.dumps(entry, ensure_ascii=False)),
                )
        except Exception:
            pass

    conn.commit()


def ensure_dirs() -> None:
    """Create data directory and initialize DB."""
    DATA_DIR.mkdir(exist_ok=True)
    _get_conn()


def close_db() -> None:
    """Explicitly close the DB connection (for clean shutdown)."""
    global _conn
    if _conn is not None:
        _conn.close()
        _conn = None


# ── State (balance + aggregate stats) ────────────────────────────────────────

def load_state(starting_balance: float = 10_000.0) -> dict[str, Any]:
    conn = _get_conn()
    row = conn.execute("SELECT json_data FROM state WHERE id = 1").fetchone()
    if row:
        return json.loads(row["json_data"])
    return {
        "balance":          starting_balance,
        "starting_balance": starting_balance,
        "total_trades":     0,
        "wins":             0,
        "losses":           0,
        "peak_balance":     starting_balance,
    }


def save_state(state: dict[str, Any]) -> None:
    conn = _get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO state (id, json_data) VALUES (1, ?)",
        (json.dumps(state, ensure_ascii=False),),
    )
    conn.commit()


# ── Per-market records ────────────────────────────────────────────────────────

def load_market(city_slug: str, date_str: str) -> dict[str, Any] | None:
    conn = _get_conn()
    row = conn.execute(
        "SELECT json_data FROM markets WHERE city = ? AND date = ?",
        (city_slug, date_str),
    ).fetchone()
    return json.loads(row["json_data"]) if row else None


def save_market(market: dict[str, Any]) -> None:
    conn = _get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO markets (city, date, status, json_data) VALUES (?, ?, ?, ?)",
        (market["city"], market["date"], market.get("status", "open"),
         json.dumps(market, ensure_ascii=False)),
    )
    conn.commit()


def load_all_markets() -> list[dict[str, Any]]:
    conn = _get_conn()
    rows = conn.execute("SELECT json_data FROM markets").fetchall()
    return [json.loads(r["json_data"]) for r in rows]


def load_markets_by_status(status: str) -> list[dict[str, Any]]:
    """Load only markets with a given status — much faster than load_all + filter."""
    conn = _get_conn()
    rows = conn.execute(
        "SELECT json_data FROM markets WHERE status = ?", (status,)
    ).fetchall()
    return [json.loads(r["json_data"]) for r in rows]


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
        "status":             "open",
        "position":           None,
        "actual_temp":        None,
        "resolved_outcome":   None,
        "pnl":                None,
        "forecast_snapshots": [],
        "all_outcomes":       [],
        "created_at":         datetime.now(timezone.utc).isoformat(),
    }


# ── Calibration ───────────────────────────────────────────────────────────────

def load_calibration() -> dict[str, Any]:
    conn = _get_conn()
    rows = conn.execute("SELECT key, json_data FROM calibration").fetchall()
    return {r["key"]: json.loads(r["json_data"]) for r in rows}


def save_calibration(cal: dict[str, Any]) -> None:
    conn = _get_conn()
    for key, entry in cal.items():
        conn.execute(
            """INSERT OR REPLACE INTO calibration
               (key, sigma, mae, n, source, updated_at, json_data)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (key, entry.get("sigma", 0), entry.get("mae"),
             entry.get("n"), entry.get("source"), entry.get("updated_at"),
             json.dumps(entry, ensure_ascii=False)),
        )
    conn.commit()


# ── Trade log (replaces trade_log.py / paper_trades.jsonl) ────────────────────

def append_trade(mkt: dict[str, Any]) -> None:
    """Append one resolved market to the trades table."""
    pos = mkt.get("position")
    if not pos:
        return

    conn = _get_conn()
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

    conn.execute(
        """INSERT INTO trades
           (ts, city, city_name, date, unit, side, bucket_low, bucket_high,
            entry_price, exit_price, shares, cost, pnl, p, ev, sigma,
            forecast_temp, forecast_source, actual_temp, outcome, reason,
            horizon, opened_at, closed_at, json_data)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (record["ts"], record["city"], record["city_name"], record["date"],
         record["unit"], record["side"], record["bucket_low"], record["bucket_high"],
         record["entry_price"], record["exit_price"], record["shares"], record["cost"],
         record["pnl"], record["p"], record["ev"], record["sigma"],
         record["forecast_temp"], record["forecast_source"], record["actual_temp"],
         record["outcome"], record["reason"], record["horizon"],
         record["opened_at"], record["closed_at"],
         json.dumps(record, ensure_ascii=False)),
    )
    conn.commit()


def load_trades() -> list[dict[str, Any]]:
    """Load all trades — for analysis and reporting."""
    conn = _get_conn()
    rows = conn.execute("SELECT json_data FROM trades ORDER BY ts").fetchall()
    return [json.loads(r["json_data"]) for r in rows]


# ── Run log (per-city per-scan outcome tracking) ─────────────────────────────

def append_run_log(city: str, status: str, error: str | None = None,
                   duration_s: float = 0.0, new_pos: int = 0,
                   closed: int = 0, resolved: int = 0) -> None:
    """Log one city's outcome from a scan cycle."""
    conn = _get_conn()
    conn.execute(
        """INSERT INTO run_log (ts, city, status, error, duration_s, new_pos, closed, resolved)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (datetime.now(timezone.utc).isoformat(), city, status, error,
         round(duration_s, 2), new_pos, closed, resolved),
    )
    conn.commit()


def get_city_health(lookback: int = 20) -> dict[str, dict[str, Any]]:
    """
    Analyze last N runs per city. Returns dict of city -> health info.
    Flags cities with high failure rates or consecutive failures.
    """
    conn = _get_conn()
    rows = conn.execute(
        """SELECT city, status, error, ts
           FROM run_log
           WHERE id IN (
               SELECT id FROM run_log r2
               WHERE r2.city = run_log.city
               ORDER BY r2.id DESC
               LIMIT ?
           )
           ORDER BY city, id DESC""",
        (lookback,),
    ).fetchall()

    # Group by city
    from collections import defaultdict
    by_city: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_city[r["city"]].append({"status": r["status"], "error": r["error"], "ts": r["ts"]})

    health: dict[str, dict[str, Any]] = {}
    for city, runs in by_city.items():
        total = len(runs)
        fails = sum(1 for r in runs if r["status"] != "ok")
        # Count consecutive failures from most recent
        consec_fails = 0
        for r in runs:
            if r["status"] != "ok":
                consec_fails += 1
            else:
                break
        last_error = next((r["error"] for r in runs if r["error"]), None)
        fail_rate = fails / total if total else 0
        health[city] = {
            "total_runs":    total,
            "fails":         fails,
            "fail_rate":     round(fail_rate, 2),
            "consec_fails":  consec_fails,
            "last_error":    last_error,
            "flagged":       consec_fails >= 3 or fail_rate >= 0.5,
        }
    return health
