"""
gopfan2_analyzer.py
-------------------
Reverse-engineers the trading strategy of gopfan2 on Polymarket.
Wallet: 0xf2f6af4f27ec2dcf4072095ab804016e14cd5817

Steps:
  1. Pull full trade history from Polymarket Data API (paginated, up to API limit)
  2. Filter to weather markets only (strict compound-phrase matching)
  3. Print a strategy summary report + what they actually trade
  4. Flag anomalies
"""

import json
import time
import sys
import io
import re
from datetime import datetime, timezone
from collections import defaultdict, Counter
from pathlib import Path

# Force UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

try:
    import requests
except ImportError:
    sys.exit("requests is not installed. Run: pip install requests")

# ─── Constants ───────────────────────────────────────────────────────────────

WALLET = "0xf2f6af4f27ec2dcf4072095ab804016e14cd5817"
BASE_URL = "https://data-api.polymarket.com/activity"
PAGE_LIMIT = 500
SLEEP_BETWEEN_PAGES = 0.5

DATA_DIR = Path(__file__).parent / "data"
RAW_PATH = DATA_DIR / "gopfan2_raw_trades.json"
WEATHER_PATH = DATA_DIR / "gopfan2_weather_trades.json"

# Strict compound patterns — avoids "high" in "higher", "heat" in "Heat" (NBA team)
# These match actual Polymarket temperature bucket market titles.
WEATHER_PATTERNS = [
    r"\btemperature\b",
    r"°[fc]\b",
    r"\bdegrees [fc]\b",
    r"\bdaily high\b",
    r"\bhigh temperature\b",
    r"\bwill the high\b",
    r"\blow temperature\b",
    r"\bdaily low\b",
    r"\bwill the low\b",
    r"\brainfall\b",
    r"\bprecipitation\b",
    r"\bsnowfall\b",
    r"\bsnow accumulation\b",
    r"\bwind speed\b",
    r"\bwind gust\b",
    r"\bhumidity\b",
    r"\bfrost\b",
    r"\bheat index\b",
    r"\bweather (market|forecast|condition)\b",
    r"\bmax temp\b",
    r"\bmin temp\b",
    r"\bhigh of \d",       # "high of 72" style
    r"\bwill it (rain|snow)\b",
    r"\binches of (rain|snow)\b",
    r"mph wind",
]

CITIES = {
    "NYC":           ["new york", "nyc", "laguardia", "klga"],
    "Chicago":       ["chicago", "kord"],
    "Dallas":        ["dallas", "kdal", "love field"],
    "Miami":         ["miami", "kmia"],
    "Seattle":       ["seattle", "ksea", "sea-tac"],
    "Atlanta":       ["atlanta", "katl"],
    "London":        ["london", "eglc"],
    "Tokyo":         ["tokyo", "rjtt", "haneda"],
    "Los Angeles":   ["los angeles", "l.a.", "lax"],
    "Phoenix":       ["phoenix", "phx"],
    "Houston":       ["houston", "hou"],
    "Denver":        ["denver", "den"],
    "Boston":        ["boston", "bos"],
    "San Francisco": ["san francisco", "sfo"],
    "Minneapolis":   ["minneapolis", "msp"],
    "Las Vegas":     ["las vegas", "lvs"],
}

PRICE_BUCKETS = [
    (0.00, 0.15, "$0.00–$0.15 (tail)"),
    (0.15, 0.30, "$0.15–$0.30"),
    (0.30, 0.50, "$0.30–$0.50"),
    (0.50, 0.70, "$0.50–$0.70"),
    (0.70, 0.85, "$0.70–$0.85"),
    (0.85, 1.00, "$0.85–$1.00 (near-certain)"),
]

_WEATHER_RE = [re.compile(p, re.IGNORECASE) for p in WEATHER_PATTERNS]


# ─── Step 1: Fetch ───────────────────────────────────────────────────────────

def fetch_all_trades() -> list:
    all_trades = []
    offset = 0
    page = 1

    print(f"[fetch] Pulling trade history for {WALLET}")

    while True:
        url = f"{BASE_URL}?user={WALLET}&limit={PAGE_LIMIT}&offset={offset}"
        print(f"[fetch] Page {page} (offset={offset}) ...", end=" ", flush=True)

        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 400:
                print("API offset limit reached — stopping.")
                break
            resp.raise_for_status()
        except requests.RequestException as exc:
            print(f"\n[fetch] Request error: {exc}")
            break

        try:
            data = resp.json()
        except ValueError:
            print(f"\n[fetch] Non-JSON response:\n{resp.text[:500]}")
            break

        if not isinstance(data, list):
            print(f"\n[fetch] Unexpected structure:\n{json.dumps(data)[:500]}")
            break

        count = len(data)
        print(f"{count} records")
        all_trades.extend(data)

        if count < PAGE_LIMIT:
            break

        offset += PAGE_LIMIT
        page += 1
        time.sleep(SLEEP_BETWEEN_PAGES)

    print(f"[fetch] Total: {len(all_trades)} records\n")
    return all_trades


# ─── Step 2: Filter ──────────────────────────────────────────────────────────

def is_weather_market(trade: dict) -> bool:
    title = (trade.get("title") or "").lower()
    slug  = (trade.get("slug") or "").lower()
    event = (trade.get("eventSlug") or "").lower()
    text  = f"{title} {slug} {event}"
    return any(rx.search(text) for rx in _WEATHER_RE)


def filter_weather(trades: list) -> list:
    return [t for t in trades if t.get("type") == "TRADE" and is_weather_market(t)]


# ─── Helpers ─────────────────────────────────────────────────────────────────

def extract_city(trade: dict) -> str:
    title = (trade.get("title") or "").lower()
    slug  = (trade.get("slug") or "").lower()
    text  = f"{title} {slug}"
    for city, keywords in CITIES.items():
        if any(kw in text for kw in keywords):
            return city
    return "Unknown"


def price_bucket(price: float) -> str:
    for lo, hi, label in PRICE_BUCKETS:
        if lo <= price <= hi:
            return label
    return "unknown"


def parse_dt(ts) -> datetime | None:
    if ts is None:
        return None
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc)
    except (ValueError, OSError):
        return None


def usdc_size(trade: dict) -> float:
    v = trade.get("usdcSize") or trade.get("size") or 0
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def trade_price(trade: dict) -> float:
    v = trade.get("price") or 0
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def trade_side(trade: dict) -> str:
    return "SELL" if (trade.get("side") or "").upper() == "SELL" else "BUY"


def trade_outcome(trade: dict) -> str:
    o = trade.get("outcome") or ""
    if o:
        return o
    idx = trade.get("outcomeIndex")
    if idx == 0:
        return "Yes"
    if idx == 1:
        return "No"
    return "?"


def bar(n: int, max_n: int, width: int = 40) -> str:
    if max_n == 0:
        return ""
    return "█" * max(1, int(n / max_n * width)) if n > 0 else ""


# ─── Step 3: Report ──────────────────────────────────────────────────────────

def print_report(all_trades: list, weather: list):
    sep = "=" * 68
    trades_only = [t for t in all_trades if t.get("type") == "TRADE"]
    n = len(weather)

    print(sep)
    print("  GOPFAN2 STRATEGY REPORT — Polymarket")
    print(f"  Wallet : {WALLET}")
    print(f"  Run at : {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(sep)

    # ── 1. Overview ──────────────────────────────────────────────────────────
    print(f"\n[1] TRADE COUNTS")
    print(f"    Activity records (all types) : {len(all_trades)}")
    print(f"    TRADE records                : {len(trades_only)}")
    print(f"    ⚠  API caps at 3500 records  — full history may be longer")

    # ── What does gopfan2 actually trade? ────────────────────────────────────
    print(f"\n[1b] WHAT GOPFAN2 ACTUALLY TRADES (top market categories)")
    event_ctr: Counter = Counter()
    for t in trades_only:
        slug = (t.get("eventSlug") or "unknown")[:55]
        event_ctr[slug] += 1
    max_e = event_ctr.most_common(1)[0][1] if event_ctr else 1
    for slug, cnt in event_ctr.most_common(15):
        print(f"    {cnt:4d}  {bar(cnt, max_e, 25)}  {slug}")

    print(f"\n    Top market titles:")
    title_ctr: Counter = Counter()
    for t in trades_only:
        title_ctr[(t.get("title") or "")[:60]] += 1
    for title, cnt in title_ctr.most_common(10):
        print(f"    {cnt:4d}  {title}")

    # ── Weather section ───────────────────────────────────────────────────────
    print(f"\n[2] WEATHER MARKET TRADES")
    print(f"    Weather trades found : {n}")
    if n == 0:
        print()
        print("    ┌─────────────────────────────────────────────────────────────┐")
        print("    │  FINDING: gopfan2 has NO weather bucket trades in the       │")
        print("    │  3,500 records returned by the API. This wallet is a        │")
        print("    │  political/sports prediction specialist, not a weather       │")
        print("    │  trader. Check a different wallet or use the Polymarket      │")
        print("    │  leaderboard to find the actual top weather traders.        │")
        print("    └─────────────────────────────────────────────────────────────┘")
        print()
        _print_what_to_do_next()
        return

    print(f"    (weather share: {n/len(trades_only)*100:.1f}% of trade records)")

    # Win rate
    print(f"\n[3] WIN RATE")
    yes_buys = [t for t in weather if trade_side(t) == "BUY" and trade_outcome(t).lower() == "yes"]
    no_buys  = [t for t in weather if trade_side(t) == "BUY" and trade_outcome(t).lower() == "no"]
    print(f"    YES buys : {len(yes_buys)}")
    print(f"    NO buys  : {len(no_buys)}")
    print(f"    NOTE: 'outcome' = outcome token traded, not resolution result.")
    print(f"          True win rate needs resolution data (separate endpoint).")

    # Price distribution
    print(f"\n[4] ENTRY PRICE DISTRIBUTION")
    bucket_ctr: dict[str, int] = defaultdict(int)
    prices = []
    for t in weather:
        p = trade_price(t)
        prices.append(p)
        bucket_ctr[price_bucket(p)] += 1
    max_b = max(bucket_ctr.values()) if bucket_ctr else 1
    for lo, hi, label in PRICE_BUCKETS:
        cnt = bucket_ctr.get(label, 0)
        print(f"    {label:27s} {cnt:4d}  {bar(cnt, max_b)}")
    if prices:
        print(f"\n    Avg: ${sum(prices)/len(prices):.3f}  "
              f"Min: ${min(prices):.3f}  Max: ${max(prices):.3f}")

    # City breakdown
    print(f"\n[5] TRADES BY CITY")
    city_ctr: Counter = Counter(extract_city(t) for t in weather)
    max_c = city_ctr.most_common(1)[0][1] if city_ctr else 1
    for city, cnt in city_ctr.most_common(15):
        print(f"    {city:<18s} {cnt:4d}  {bar(cnt, max_c, 25)}")

    # Position size
    print(f"\n[6] POSITION SIZE (USDC)")
    sizes = sorted([usdc_size(t) for t in weather if usdc_size(t) > 0])
    if sizes:
        avg_sz = sum(sizes) / len(sizes)
        median = sizes[len(sizes) // 2]
        print(f"    Count    : {len(sizes)}")
        print(f"    Average  : ${avg_sz:.2f}")
        print(f"    Median   : ${median:.2f}")
        print(f"    Max      : ${max(sizes):.2f}")
        print(f"    Total    : ${sum(sizes):,.2f}")

    # Hour distribution
    print(f"\n[7] ENTRY HOUR DISTRIBUTION (UTC)")
    print(f"    ECMWF publishes ~06:00 & 18:00 UTC | HRRR every hour")
    hour_ctr: Counter = Counter()
    for t in weather:
        dt = parse_dt(t.get("timestamp"))
        if dt:
            hour_ctr[dt.hour] += 1
    max_h = max(hour_ctr.values()) if hour_ctr else 1
    for h in range(24):
        cnt = hour_ctr.get(h, 0)
        marker = " ← ECMWF" if h in (6, 7, 18, 19) else ""
        print(f"    {h:02d}:00  {cnt:4d}  {bar(cnt, max_h, 25)}{marker}")

    # Side preference
    print(f"\n[8] SIDE / OUTCOME PREFERENCE")
    buys  = sum(1 for t in weather if trade_side(t) == "BUY")
    sells = sum(1 for t in weather if trade_side(t) == "SELL")
    print(f"    BUY  : {buys} ({buys/n*100:.1f}%)")
    print(f"    SELL : {sells} ({sells/n*100:.1f}%)")
    if yes_buys or no_buys:
        total_buys = len(yes_buys) + len(no_buys)
        print(f"    YES buys : {len(yes_buys)} ({len(yes_buys)/total_buys*100:.1f}%)")
        print(f"    NO buys  : {len(no_buys)} ({len(no_buys)/total_buys*100:.1f}%)")

    # Resolution horizon
    print(f"\n[9] RESOLUTION HORIZON")
    unique_cids = {t.get("conditionId") for t in weather if t.get("conditionId")}
    print(f"    Unique weather markets : {len(unique_cids)}")
    print(f"    Resolution data        : needs per-market API call")

    # ── Step 4: Anomalies ─────────────────────────────────────────────────────
    print(f"\n[10] ANOMALIES")
    anomalies = []
    for t in weather:
        p = trade_price(t)
        sz = usdc_size(t)
        flags = []
        if p < 0.05:
            flags.append(f"extreme tail price={p:.3f}")
        if p > 0.90:
            flags.append(f"near-certain price={p:.3f}")
        if sz > 500:
            flags.append(f"large bet ${sz:.0f}")
        if flags:
            dt = parse_dt(t.get("timestamp"))
            dt_str = dt.strftime("%Y-%m-%d %H:%M UTC") if dt else "?"
            title = (t.get("title") or "")[:60]
            print(f"\n    [{dt_str}]  {title}")
            print(f"    {trade_side(t)} {trade_outcome(t)}  ${sz:.2f}  @ ${p:.3f}")
            print(f"    Flags: {' | '.join(flags)}")
            anomalies.append(t)
    if not anomalies:
        print("    None found.")
    print(f"\n    Total anomalies: {len(anomalies)}")

    # ── Strategy fingerprint ──────────────────────────────────────────────────
    print(f"\n{sep}")
    print("  STRATEGY FINGERPRINT")
    print(sep)
    if prices:
        modal = max(bucket_ctr, key=bucket_ctr.get)
        print(f"  Preferred price range  : {modal}")
    if city_ctr:
        top = city_ctr.most_common(1)[0]
        print(f"  Most traded city       : {top[0]} ({top[1]} trades)")
    if hour_ctr:
        ph = hour_ctr.most_common(1)[0]
        print(f"  Peak trading hour      : {ph[0]:02d}:00 UTC ({ph[1]} trades)")
    if sizes:
        print(f"  Avg position size      : ${avg_sz:.2f} USDC")
    print(f"  Buy/Sell               : {buys}/{sells}")
    print(sep)


def _print_what_to_do_next():
    print("[NEXT STEPS] To find the real top weather trader:")
    print()
    print("  1. Check the Polymarket leaderboard filtered to Weather markets:")
    print("     https://polymarket.com/leaderboard?category=weather")
    print()
    print("  2. Use the Polymarket Gamma API to find top weather markets:")
    print("     GET https://gamma-api.polymarket.com/markets?tag=weather&limit=100")
    print("     Then check which wallets appear most in the trade history.")
    print()
    print("  3. Search the activity API with a weather conditionId first:")
    print("     Find a resolved weather market -> GET activity?conditionId=...")
    print("     -> identify wallets with large profitable positions.")
    print()
    print("  4. gopfan2's actual specialty: Peruvian elections + FIFA + Hungary")
    print("     That's where their 3500 recorded trades are concentrated.")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_trades = fetch_all_trades()
    with open(RAW_PATH, "w") as f:
        json.dump(all_trades, f, indent=2)
    print(f"[save] Raw   -> {RAW_PATH}  ({len(all_trades)} records)")

    weather = filter_weather(all_trades)
    with open(WEATHER_PATH, "w") as f:
        json.dump(weather, f, indent=2)
    print(f"[save] Weather -> {WEATHER_PATH}  ({len(weather)} records)")
    print()

    print_report(all_trades, weather)


if __name__ == "__main__":
    main()
