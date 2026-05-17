"""Check live market liquidity on Polymarket weather markets right now."""
import requests
import json
from datetime import datetime, timedelta

GAMMA = "https://gamma-api.polymarket.com"

cities = [
    "chicago", "nyc", "miami", "atlanta", "dallas",
    "london", "paris", "munich", "tokyo", "seoul",
    "singapore", "shanghai", "toronto", "seattle",
    "wellington", "buenos-aires", "ankara", "tel-aviv",
    "sao-paulo", "lucknow"
]

# Check D+1 and D+2 markets
now = datetime.utcnow()
dates_to_check = [
    (now + timedelta(days=1)).strftime("%Y-%m-%d"),
    (now + timedelta(days=2)).strftime("%Y-%m-%d"),
]

print(f"Current UTC: {now.isoformat()}")
print(f"Checking dates: {dates_to_check}")
print()

total_markets = 0
total_outcomes = 0
markets_with_volume = 0

for target_date in dates_to_check:
    dt = datetime.strptime(target_date, "%Y-%m-%d")
    month_name = dt.strftime("%B").lower()
    day = dt.day
    year = dt.year

    print(f"=== {target_date} (D+{(dt.date() - now.date()).days}) ===")

    for city in cities[:10]:  # check first 10 cities
        slug = f"highest-temperature-in-{city}-on-{month_name}-{day}-{year}"
        try:
            r = requests.get(f"{GAMMA}/events", params={"slug": slug}, timeout=10)
            if r.status_code != 200:
                continue
            events = r.json()
            if not events:
                continue
            event = events[0]
            mkts = event.get("markets", [])
            if not mkts:
                continue

            total_markets += 1
            # Analyze each outcome (temperature bucket)
            no_entry_candidates = 0
            for m in mkts:
                total_outcomes += 1
                yes_price = float(m.get("outcomePrices", "0.5").split(",")[0]) if isinstance(m.get("outcomePrices"), str) else 0.5
                no_price = 1 - yes_price
                bid = float(m.get("bestBid", 0))
                ask = float(m.get("bestAsk", 0))
                vol = float(m.get("volume", 0))
                spread = ask - bid if ask and bid else 0
                no_ask = 1 - bid  # cost to buy NO
                no_bid = 1 - ask  # what we get selling NO

                # Is this a valid NO entry? (0.65 <= no_ask <= 0.90)
                if 0.65 <= no_ask <= 0.90 and vol > 0:
                    no_entry_candidates += 1
                    q = m.get("question", "")[:60]
                    print(f"  {city:15} {q}")
                    print(f"    YES: bid={bid:.3f} ask={ask:.3f} spread={spread:.3f} vol=${vol:.0f}")
                    print(f"    NO:  ask={no_ask:.3f} bid={no_bid:.3f}")
                    if vol > 0:
                        markets_with_volume += 1

        except Exception as e:
            pass

print(f"\n=== SUMMARY ===")
print(f"Events found: {total_markets}")
print(f"Total outcomes: {total_outcomes}")
print(f"Markets with volume: {markets_with_volume}")
print(f"NO entry candidates (0.65-0.90): shown above")
