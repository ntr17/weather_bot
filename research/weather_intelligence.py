#!/usr/bin/env python3
"""
weather_intelligence.py — Polymarket Weather Market Intelligence
=================================================================
Task 1: Pull the weather leaderboard
Task 2: Pull WeatherTraderBot's full trade history
Task 3: Analyze trades (price dist, position size, cities, UTC hours, YES/NO ratio)
Task 4: Print repo audit for bot_v1.py and bot_v2.py (weatherbet.py)

stdlib + requests only. Run from weatherbot-main/ root.
"""

import io
import sys
import re
import json
import time
import os
from datetime import datetime, timezone
from collections import Counter, defaultdict

import requests

# Force UTF-8 output on Windows
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

HEADERS = {"User-Agent": "weatherbot-research/1.0", "Accept": "application/json"}

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def get(url: str, params: dict = None, label: str = "") -> tuple[int, object]:
    """GET with graceful error handling. Returns (status_code, parsed_body)."""
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=30)
        try:
            body = r.json()
        except Exception:
            body = r.text
        return r.status_code, body
    except Exception as e:
        print(f"  [ERR] {label or url}: {e}")
        return 0, None

def bar(val: int, total: int, width: int = 30) -> str:
    filled = int(width * val / max(total, 1))
    return "#" * filled + "-" * (width - filled)

def section(title: str):
    print(f"\n{'=' * 65}")
    print(f"  {title}")
    print(f"{'=' * 65}")

# ─────────────────────────────────────────────────────────────────────────────
# TASK 1 — WEATHER LEADERBOARD
# ─────────────────────────────────────────────────────────────────────────────

LEADERBOARD_ENDPOINTS = [
    ("gamma leaderboard", "https://gamma-api.polymarket.com/leaderboard",
     {"category": "WEATHER", "timePeriod": "ALL", "orderBy": "PNL", "limit": 50}),
    ("data leaderboard", "https://data-api.polymarket.com/leaderboard",
     {"category": "WEATHER", "timePeriod": "ALL", "limit": 50}),
    ("gamma leaderboard no filter", "https://gamma-api.polymarket.com/leaderboard",
     {"timePeriod": "ALL", "orderBy": "PNL", "limit": 50}),
    ("data leaderboard no filter", "https://data-api.polymarket.com/leaderboard",
     {"timePeriod": "ALL", "limit": 50}),
    ("gamma top traders", "https://gamma-api.polymarket.com/users",
     {"orderBy": "profit", "ascending": "false", "limit": 50}),
]

def task1_leaderboard():
    section("TASK 1 — WEATHER LEADERBOARD")

    leaderboard = []
    target_wallet = None

    for label, url, params in LEADERBOARD_ENDPOINTS:
        print(f"\n  Trying: {label}")
        print(f"  URL:    {url}")
        print(f"  Params: {params}")
        status, body = get(url, params=params, label=label)
        print(f"  Status: {status}")

        if status == 0 or body is None:
            print("  Result: connection failed")
            continue

        # Print raw (truncated)
        raw = json.dumps(body, indent=2) if isinstance(body, (dict, list)) else str(body)
        print(f"  Raw ({len(raw)} chars):")
        print("  " + raw[:2000].replace("\n", "\n  "))
        if len(raw) > 2000:
            print(f"  ... [truncated, {len(raw)} total chars]")

        if isinstance(body, list) and len(body) > 0:
            leaderboard = body
            print(f"  -> Got {len(body)} entries")
            break
        elif isinstance(body, dict) and ("data" in body or "results" in body):
            rows = body.get("data") or body.get("results") or []
            if rows:
                leaderboard = rows
                print(f"  -> Got {len(rows)} entries via 'data'/'results' key")
                break

        time.sleep(0.5)

    if not leaderboard:
        print("\n  All leaderboard endpoints returned no usable data.")
        print("  Trying Gamma users endpoint to find WeatherTraderBot by name...")
        status, body = get(
            "https://gamma-api.polymarket.com/users",
            params={"search": "WeatherTraderBot", "limit": 10},
            label="user search"
        )
        print(f"  Status: {status}")
        if isinstance(body, (list, dict)):
            raw = json.dumps(body, indent=2)
            print("  " + raw[:1500].replace("\n", "\n  "))

        print("\n  Trying activity search by known weather slugs to find big traders...")
        # Pull activity for a well-known weather market and see who's trading
        status, body = get(
            "https://gamma-api.polymarket.com/markets",
            params={"tag": "weather", "limit": 5, "active": "true"},
            label="gamma markets weather tag"
        )
        print(f"\n  Gamma markets?tag=weather status: {status}")
        if isinstance(body, (list, dict)):
            print("  " + json.dumps(body, indent=2)[:1500].replace("\n", "\n  "))
        return target_wallet, leaderboard

    # Parse leaderboard
    print(f"\n  Leaderboard ({len(leaderboard)} entries):")
    print(f"  {'Username':<25} {'Wallet':<45} {'PnL':>12} {'Volume':>12}")
    print(f"  {'-'*25} {'-'*45} {'-'*12} {'-'*12}")

    for entry in leaderboard[:20]:
        username = (entry.get("name") or entry.get("username") or entry.get("displayName") or "?")[:24]
        wallet   = (entry.get("proxyWallet") or entry.get("address") or entry.get("wallet") or "?")[:44]
        pnl      = entry.get("pnl") or entry.get("profit") or entry.get("totalPnl") or 0
        volume   = entry.get("volume") or entry.get("totalVolume") or 0
        print(f"  {username:<25} {wallet:<45} {float(pnl):>12,.2f} {float(volume):>12,.0f}")

        if "weathertraderbot" in username.lower() or "weather" in username.lower():
            target_wallet = entry.get("proxyWallet") or entry.get("address") or entry.get("wallet")
            print(f"  *** FOUND weather trader: {username} -> {target_wallet}")

    # Save
    path = os.path.join(DATA_DIR, "weather_leaderboard.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, indent=2, ensure_ascii=False)
    print(f"\n  Saved to {path}")

    return target_wallet, leaderboard

# ─────────────────────────────────────────────────────────────────────────────
# FIND WEATHER TRADERS VIA GAMMA MARKETS
# ─────────────────────────────────────────────────────────────────────────────

def find_weather_markets():
    """Pull active weather markets from Gamma API to identify condition IDs."""
    print("\n  Scanning Gamma API for weather markets...")

    weather_slugs = []
    condition_ids = []

    endpoints = [
        ("gamma events tag=weather", "https://gamma-api.polymarket.com/events",
         {"tag": "weather", "active": "true", "limit": 10}),
        ("gamma events category search", "https://gamma-api.polymarket.com/events",
         {"_c": "weather", "limit": 10}),
        ("gamma markets label search", "https://gamma-api.polymarket.com/markets",
         {"_c": "temperature", "limit": 10}),
    ]

    found_markets = []
    for label, url, params in endpoints:
        status, body = get(url, params=params, label=label)
        print(f"  {label}: HTTP {status}")
        if status == 200 and isinstance(body, list) and len(body) > 0:
            print(f"  -> {len(body)} results")
            raw = json.dumps(body[:2], indent=2)
            print("  " + raw[:800].replace("\n", "\n  "))
            found_markets = body
            break
        elif status == 200 and isinstance(body, dict):
            rows = body.get("events") or body.get("markets") or body.get("data") or []
            if rows:
                found_markets = rows
                break
        time.sleep(0.4)

    # Try slug-based approach
    if not found_markets:
        print("  Trying slug lookup for a known weather event...")
        today = datetime.now(timezone.utc)
        test_slugs = [
            f"highest-temperature-in-nyc-on-april-{today.day}-{today.year}",
            f"highest-temperature-in-chicago-on-april-{today.day}-{today.year}",
            f"highest-temperature-in-miami-on-april-{today.day}-{today.year}",
        ]
        for slug in test_slugs:
            status, body = get(
                "https://gamma-api.polymarket.com/events",
                params={"slug": slug},
                label=slug
            )
            if status == 200 and isinstance(body, list) and len(body) > 0:
                print(f"  Found event for slug: {slug}")
                found_markets = body
                break
            time.sleep(0.3)

    for ev in found_markets[:5]:
        if isinstance(ev, dict):
            for mkt in ev.get("markets", [ev]):
                cid = mkt.get("conditionId") or mkt.get("condition_id")
                if cid:
                    condition_ids.append(cid)

    return condition_ids[:3]  # return at most 3 to query activity

def find_top_weather_traders(condition_ids: list) -> str | None:
    """Query activity by conditionId to find wallets trading weather markets."""
    if not condition_ids:
        return None

    print(f"\n  Looking up activity for {len(condition_ids)} weather market condition IDs...")
    wallet_pnl: dict[str, float] = defaultdict(float)
    wallet_names: dict[str, str] = {}

    for cid in condition_ids:
        print(f"  conditionId: {cid[:20]}...")
        status, body = get(
            "https://data-api.polymarket.com/activity",
            params={"conditionId": cid, "limit": 200},
            label=f"activity conditionId={cid[:12]}"
        )
        if status == 200 and isinstance(body, list):
            print(f"  -> {len(body)} trades")
            for trade in body:
                wallet = trade.get("proxyWallet") or trade.get("user") or ""
                name   = trade.get("name") or trade.get("username") or ""
                side   = trade.get("side") or ""
                price  = float(trade.get("price") or 0)
                size   = float(trade.get("usdcSize") or 0)
                if wallet:
                    wallet_pnl[wallet] += size
                    if name:
                        wallet_names[wallet] = name
        time.sleep(0.5)

    if not wallet_pnl:
        return None

    top = sorted(wallet_pnl.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"\n  Top wallets by volume on weather markets:")
    target = None
    for wallet, vol in top:
        name = wallet_names.get(wallet, "")
        label = f"{name} ({wallet[:12]}...)" if name else f"{wallet[:16]}..."
        print(f"    {label:<45} ${vol:>10,.2f}")
        if "weather" in name.lower() and not target:
            target = wallet

    return target

# ─────────────────────────────────────────────────────────────────────────────
# TASK 2 — FETCH TRADE HISTORY
# ─────────────────────────────────────────────────────────────────────────────

def task2_fetch_trades(wallet: str) -> list:
    section(f"TASK 2 — FETCH TRADE HISTORY")
    print(f"  Wallet: {wallet}")

    all_trades = []
    offset     = 0
    limit      = 500
    page       = 0

    while True:
        page += 1
        print(f"  Page {page} (offset={offset})...", end=" ", flush=True)
        status, body = get(
            "https://data-api.polymarket.com/activity",
            params={"user": wallet, "limit": limit, "offset": offset},
            label=f"page {page}"
        )

        if status == 400:
            print("API hard limit reached — stopping.")
            break
        if status != 200 or not isinstance(body, list):
            print(f"unexpected {status} — stopping.")
            if body:
                print(f"  Body: {str(body)[:300]}")
            break

        count = len(body)
        print(f"{count} trades")
        if count == 0:
            break

        all_trades.extend(body)
        offset += limit

        if count < limit:
            break

        time.sleep(0.5)

    print(f"\n  Total trades fetched: {len(all_trades)}")

    # Save raw
    path = os.path.join(DATA_DIR, "weathertraderbot_trades.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(all_trades, f, indent=2, ensure_ascii=False)
    print(f"  Saved to {path}")

    return all_trades

# ─────────────────────────────────────────────────────────────────────────────
# TASK 3 — ANALYZE TRADES
# ─────────────────────────────────────────────────────────────────────────────

WEATHER_PATTERNS = [
    r"\btemperature\b", r"°[fc]\b", r"\bdaily high\b", r"\bhigh temperature\b",
    r"\bwill the high\b", r"\blow temperature\b", r"\bwind speed\b",
    r"\bheat index\b", r"\bprecipitation\b", r"\bsnowfall\b", r"\brainfall\b",
    r"\bhumidity\b", r"\bwill it snow\b", r"\bwill it rain\b",
    r"\bhighest temp\b", r"\blowest temp\b", r"\bmax temp\b", r"\bmin temp\b",
    r"\bweather\b.*\bmarket\b", r"\bforecast\b.*\btemp\b",
]
_WEATHER_RE = [re.compile(p, re.IGNORECASE) for p in WEATHER_PATTERNS]

CITY_KEYWORDS = {
    "New York / NYC": ["new york", "nyc", "klga", "laguardia"],
    "Chicago":        ["chicago", "kord", "o'hare", "ohare"],
    "Miami":          ["miami", "kmia"],
    "Dallas":         ["dallas", "kdal", "love field"],
    "Seattle":        ["seattle", "ksea", "sea-tac"],
    "Atlanta":        ["atlanta", "katl", "hartsfield"],
    "London":         ["london", "eglc"],
    "Tokyo":          ["tokyo", "rjtt", "haneda"],
    "Paris":          ["paris", "lfpg"],
    "Chicago":        ["chicago"],
    "Singapore":      ["singapore", "wsss"],
    "Seoul":          ["seoul", "rksi"],
    "Shanghai":       ["shanghai", "zspd"],
}

def is_weather_trade(trade: dict) -> bool:
    text = " ".join(filter(None, [
        trade.get("title") or "",
        trade.get("slug") or "",
        trade.get("eventSlug") or "",
        trade.get("market") or "",
        trade.get("question") or "",
    ]))
    return any(rx.search(text) for rx in _WEATHER_RE)

def detect_city(trade: dict) -> str:
    text = " ".join(filter(None, [
        trade.get("title") or "",
        trade.get("slug") or "",
        trade.get("eventSlug") or "",
        trade.get("market") or "",
    ])).lower()
    for city, kws in CITY_KEYWORDS.items():
        if any(kw in text for kw in kws):
            return city
    return "Other"

def task3_analyze(trades: list, wallet: str):
    section("TASK 3 — TRADE ANALYSIS")

    if not trades:
        print("  No trades to analyze.")
        return

    print(f"  Wallet:      {wallet}")
    print(f"  Total records: {len(trades)}")

    # Filter to TRADE type only (skip YIELD / LP events)
    trade_records = [t for t in trades if t.get("type", "").upper() == "TRADE"]
    print(f"  TRADE records: {len(trade_records)}")

    # Separate weather vs all
    weather = [t for t in trade_records if is_weather_trade(t)]
    print(f"  Weather trades: {len(weather)}")

    if not weather:
        print("\n  No weather trades found in this wallet's history.")
        print("  Showing analysis of ALL trades instead.\n")
        weather = trade_records  # fall back to all

    if not weather:
        print("  No trades at all — nothing to analyze.")
        return

    # 1. Price distribution
    prices = [float(t.get("price") or 0) for t in weather if t.get("price") is not None]
    buckets = {
        "<0.15":        [p for p in prices if p < 0.15],
        "0.15–0.30":    [p for p in prices if 0.15 <= p < 0.30],
        "0.30–0.50":    [p for p in prices if 0.30 <= p < 0.50],
        "0.50–0.70":    [p for p in prices if 0.50 <= p < 0.70],
        ">0.70":        [p for p in prices if p >= 0.70],
    }
    total_trades = len(prices)

    print(f"\n  [1] PRICE DISTRIBUTION ({total_trades} trades with price data)")
    for label, group in buckets.items():
        pct = len(group) / max(total_trades, 1) * 100
        print(f"    {label:<12}  {len(group):>4}  ({pct:>5.1f}%)  [{bar(len(group), total_trades, 25)}]")

    # 2. Average position size
    sizes = [float(t.get("usdcSize") or 0) for t in weather if t.get("usdcSize") is not None]
    if sizes:
        avg_size  = sum(sizes) / len(sizes)
        max_size  = max(sizes)
        med_size  = sorted(sizes)[len(sizes) // 2]
        print(f"\n  [2] POSITION SIZE (USDC)")
        print(f"    Count:   {len(sizes)}")
        print(f"    Average: ${avg_size:>10,.2f}")
        print(f"    Median:  ${med_size:>10,.2f}")
        print(f"    Max:     ${max_size:>10,.2f}")

    # 3. Most traded cities
    city_counts = Counter(detect_city(t) for t in weather)
    print(f"\n  [3] CITIES (top 10)")
    for city, cnt in city_counts.most_common(10):
        pct = cnt / max(len(weather), 1) * 100
        print(f"    {city:<25}  {cnt:>4}  ({pct:>5.1f}%)  [{bar(cnt, len(weather), 20)}]")

    # 4. UTC hour distribution
    hour_counts: dict[int, int] = defaultdict(int)
    for t in weather:
        ts = t.get("timestamp")
        if ts:
            try:
                dt = datetime.fromtimestamp(int(ts), tz=timezone.utc)
                hour_counts[dt.hour] += 1
            except Exception:
                pass

    if hour_counts:
        peak_hour = max(hour_counts, key=hour_counts.get)
        print(f"\n  [4] UTC HOUR DISTRIBUTION (peak: {peak_hour:02d}:00 UTC)")
        max_h = max(hour_counts.values())
        for h in range(24):
            cnt = hour_counts.get(h, 0)
            bar_str = bar(cnt, max_h, 20)
            marker = " <-- peak" if h == peak_hour else ""
            print(f"    {h:02d}:00  {cnt:>4}  [{bar_str}]{marker}")

    # 5. YES vs NO ratio
    yes_trades = [t for t in weather if str(t.get("outcome") or "").upper() == "YES"
                  or str(t.get("side") or "").upper() in ("BUY", "")]
    no_trades  = [t for t in weather if str(t.get("outcome") or "").upper() == "NO"
                  or str(t.get("side") or "").upper() == "SELL"]

    # Better: use outcome field
    outcomes = Counter(str(t.get("outcome") or "unknown").upper() for t in weather)
    print(f"\n  [5] OUTCOME DISTRIBUTION")
    for outcome, cnt in outcomes.most_common():
        pct = cnt / max(len(weather), 1) * 100
        print(f"    {outcome:<10}  {cnt:>4}  ({pct:>5.1f}%)")

    sides = Counter(str(t.get("side") or "BUY").upper() for t in weather)
    print(f"\n  [5b] SIDE DISTRIBUTION")
    for side, cnt in sides.most_common():
        pct = cnt / max(len(weather), 1) * 100
        print(f"    {side:<10}  {cnt:>4}  ({pct:>5.1f}%)")

    # 6. Large trades (>$100)
    large = [t for t in weather if float(t.get("usdcSize") or 0) > 100]
    print(f"\n  [6] LARGE TRADES (>$100) — {len(large)} found")
    for t in large[:20]:
        title = (t.get("title") or t.get("slug") or "?")[:55]
        price = float(t.get("price") or 0)
        size  = float(t.get("usdcSize") or 0)
        side  = t.get("side") or "BUY"
        ts    = t.get("timestamp")
        dt    = datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d %H:%M") if ts else "?"
        print(f"    {dt}  ${size:>8,.2f}  @{price:.3f}  {side:<4}  {title}")

    # Sample raw trade for schema inspection
    print(f"\n  [sample] First weather trade raw fields:")
    if weather:
        sample = weather[0]
        for k, v in sample.items():
            print(f"    {k}: {v}")

# ─────────────────────────────────────────────────────────────────────────────
# TASK 4 — REPO AUDIT
# ─────────────────────────────────────────────────────────────────────────────

def task4_repo_audit():
    section("TASK 4 — REPO AUDIT: alteregoeth-ai/weatherbot")

    print("""
  FILES AUDITED
  -------------
  • bot_v1.py     — simple base bot
  • bot_v2.py     — production bot (weatherbet.py)

  ════════════════════════════════════════════════════════
  BOT V1 (bot_v1.py) — Simple Base
  ════════════════════════════════════════════════════════

  DATA SOURCE
    • NWS (api.weather.gov) — hourly gridpoint forecasts
    • NWS station observations (past 48h actuals via /stations/{ID}/observations)
    • Combines observed + forecast to get daily maximum

  ENTRY LOGIC
    • Find Polymarket event slug: "highest-temperature-in-{city}-on-{month}-{day}-{year}"
    • Parse temperature range from market question (regex: "between X-Y°F", "or below", "or higher")
    • Match forecast temp to bucket
    • Buy if market price < entry_threshold (default: 0.15)
    • Flat 5% of balance per trade — NO Kelly, NO EV calculation

  EXIT LOGIC
    • Sell if current price >= exit_threshold (default: 0.45)
    • No stop-loss, no time-based exit, no forecast-change exit

  MULTI-MODEL
    • NONE — single source (NWS only)

  CITIES
    • 6 US cities: NYC (KLGA), Chicago (KORD), Miami (KMIA),
      Dallas (KDAL), Seattle (KSEA), Atlanta (KATL)

  KNOWN GAPS / TODOs
    • Single data source (NWS) — no consensus, no EU/Asia
    • No EV or probability calculation — pure price threshold
    • No slippage or spread filter
    • No actual temperature verification after resolution
    • 5% flat sizing ignores edge probability → over-bets low-confidence trades
    • MAX_TRADES=5 cap can leave good signals on the table
    • No persistence of market metadata (no learning from history)

  ════════════════════════════════════════════════════════
  BOT V2 (bot_v2.py / weatherbet.py) — Production Bot
  ════════════════════════════════════════════════════════

  DATA SOURCES
    • ECMWF via Open-Meteo (all cities, 7-day, bias_correction=true)
    • HRRR+GFS seamless via Open-Meteo (US only, ≤48h horizon)
    • METAR via aviationweather.gov (real-time D+0 anchor)
    • Visual Crossing (paid API, for actual temp after resolution)
    Selection: HRRR for US D+0/D+1, ECMWF for everything else

  ENTRY LOGIC
    1. Pull ECMWF + HRRR + METAR forecasts
    2. Match forecast to temperature bucket (exact match for middle buckets,
       normal distribution for edge buckets using bucket_prob())
    3. Probability p = bucket_prob(forecast, t_low, t_high, sigma)
    4. EV = p * (1/price - 1) - (1-p) — must be >= min_ev (0.10)
    5. Kelly = (p*b - (1-p)) / b * kelly_fraction (0.25)
    6. Size  = min(kelly * balance, max_bet=$20)
    7. Verify real bestAsk/bestBid from Gamma API — re-check slippage (max 0.03) and price (max 0.45)
    8. Skip if spread > max_slippage or ask >= max_price

  EXIT LOGIC
    • Stop-loss: 20% below entry price
    • Trailing stop: if up 20%+, move stop to breakeven
    • Take-profit: $0.75 (>48h left), $0.85 (24-48h left), hold to resolution (<24h)
    • Forecast-change exit: if forecast shifts 2°F/1°C outside bucket with >buffer margin
    • Resolution: checks Polymarket market close (YES price ≥0.95 = win, ≤0.05 = loss)

  MULTI-MODEL
    • YES — 3 sources (ECMWF + HRRR + METAR)
    • Best-source logic: HRRR takes priority for US short-horizon, ECMWF for rest
    • Calibration: sigma updated from MAE of resolved markets (needs 30+ resolved)

  CITIES
    • 20 cities across US, EU, Asia, South America, Oceania
    • US: NYC, Chicago, Miami, Dallas, Seattle, Atlanta
    • EU: London, Paris, Munich, Ankara
    • Asia: Seoul, Tokyo, Shanghai, Singapore, Lucknow, Tel Aviv
    • Americas: Toronto, Sao Paulo, Buenos Aires
    • Oceania: Wellington

  KNOWN GAPS / TODOs
    1. sigma calibration inactive until 30+ resolved markets — using default sigma=2.0°F/1.2°C
       until enough history accumulates (could be weeks)
    2. Visual Crossing (VC_KEY) required for actual temp resolution but not set in config.json —
       resolved markets won't get actual_temp filled without it
    3. HRRR comment says "HRRR+GFS seamless" but model string is "gfs_seamless" (not "hrrr") —
       actually GFS, not true HRRR. Real HRRR would need Open-Meteo Pro plan
    4. No backtesting — can't validate strategy on historical data without 36GB dataset
    5. Gamma API event lookup has no retry on transient failures (single attempt, no back-off)
    6. Spread re-check at entry uses real ask but stop/take-profit exits use stale cached prices
       from all_outcomes (updated only on full scan, not monitor loop)
    7. monitor_positions() uses bestBid (correct for selling) but scan_and_update() uses
       outcomePrices[0] (less accurate) for stop-loss check — inconsistent
    8. No live execution — paper only (balance tracked in state.json, no Polymarket CLOB trades)
    9. forecast_changed exit logic checks abs(forecast - mid_bucket) > half_width + buffer,
       but mid_bucket calculation for edge buckets (-999 or 999) falls back to forecast_temp
       itself → edge-bucket positions almost never trigger forecast-change exit
   10. kelly_fraction=0.25 applied globally — no differentiation by horizon or city
    """)

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("  POLYMARKET WEATHER INTELLIGENCE")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 65)

    # ── TASK 1 ──────────────────────────────────────────────────────────────
    target_wallet, leaderboard = task1_leaderboard()

    # If leaderboard API gave nothing, try via weather market activity
    if not target_wallet:
        condition_ids = find_weather_markets()
        target_wallet = find_top_weather_traders(condition_ids)

    # Hard-code known WeatherTraderBot wallet if API is down
    # (can be updated once leaderboard API is confirmed)
    if not target_wallet:
        print("\n  Could not find WeatherTraderBot wallet via APIs.")
        print("  You can manually set the wallet address and re-run Task 2+3.")
        print("  Example: python research/weather_intelligence.py --wallet 0xABC...")

        # Check if passed as arg
        for i, arg in enumerate(sys.argv):
            if arg == "--wallet" and i + 1 < len(sys.argv):
                target_wallet = sys.argv[i + 1]
                print(f"  Using wallet from CLI: {target_wallet}")
                break

    # ── TASK 2 + 3 ──────────────────────────────────────────────────────────
    if target_wallet:
        trades = task2_fetch_trades(target_wallet)
        if trades:
            task3_analyze(trades, target_wallet)
        else:
            print("  No trades returned — skipping analysis.")
    else:
        print("\n  Skipping Tasks 2+3 — no wallet found.")
        print("  Re-run with: python research/weather_intelligence.py --wallet 0x...")

    # ── TASK 4 ──────────────────────────────────────────────────────────────
    task4_repo_audit()

    print("\n" + "=" * 65)
    print("  DONE")
    print("=" * 65)

if __name__ == "__main__":
    main()
