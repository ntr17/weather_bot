"""Check live market structure and liquidity."""
import requests
import json
from core.locations import MONTHS

month_name = MONTHS[5-1]  # May
slug = f"highest-temperature-in-chicago-on-{month_name}-15-2026"
print(f"Slug: {slug}")
url = f"https://gamma-api.polymarket.com/events?slug={slug}"
print(f"URL: {url}")

r = requests.get(url, timeout=10)
print(f"Status: {r.status_code}")
data = r.json()
print(f"Response length: {len(data)}")

if data:
    event = data[0]
    print(f"Event title: {event.get('title', 'N/A')[:80]}")
    mkts = event.get("markets", [])
    print(f"Markets (buckets): {len(mkts)}")

    no_candidates = []
    for m in mkts:
        q = m.get("question", "")
        bid = float(m.get("bestBid", 0) or 0)
        ask = float(m.get("bestAsk", 0) or 0)
        vol = float(m.get("volume", 0) or 0)
        spread = ask - bid
        no_ask = 1 - bid  # cost to buy NO
        no_bid = 1 - ask  # what you get selling NO
        clob_ids = m.get("clobTokenIds")

        if 0.65 <= no_ask <= 0.90:
            no_candidates.append({
                "q": q[:60],
                "bid": bid, "ask": ask, "spread": spread,
                "no_ask": no_ask, "no_bid": no_bid,
                "vol": vol,
                "market_id": m.get("id"),
                "clob_ids": clob_ids,
                "condition_id": m.get("conditionId"),
            })

    print(f"\nNO entry candidates (0.65-0.90):")
    for c in no_candidates:
        print(f"  {c['q']}")
        print(f"    YES bid={c['bid']:.3f} ask={c['ask']:.3f} spread={c['spread']:.3f} vol=${c['vol']:.0f}")
        print(f"    NO  ask={c['no_ask']:.3f} bid={c['no_bid']:.3f}")
        print(f"    market_id={c['market_id']}")
        print(f"    clobTokenIds={c['clob_ids']}")

    # Show ALL markets sorted by NO ask
    print(f"\nALL {len(mkts)} buckets sorted by YES price:")
    for m in sorted(mkts, key=lambda x: float(x.get("bestAsk", 0) or 0)):
        q = m.get("question", "")[:55]
        bid = float(m.get("bestBid", 0) or 0)
        ask = float(m.get("bestAsk", 0) or 0)
        vol = float(m.get("volume", 0) or 0)
        no_ask = 1 - bid
        print(f"  {q:55} YES={bid:.2f}/{ask:.2f} NO_ask={no_ask:.2f} vol=${vol:.0f}")

else:
    # Try different date/city combos
    print("No data for Chicago May 15. Trying other combos...")
    for city in ["nyc", "miami", "london", "tokyo"]:
        for day in [15, 16, 17]:
            slug = f"highest-temperature-in-{city}-on-{month_name}-{day}-2026"
            try:
                r = requests.get(f"https://gamma-api.polymarket.com/events?slug={slug}", timeout=5)
                d = r.json()
                if d:
                    print(f"  FOUND: {slug} -> {len(d[0].get('markets',[]))} markets")
            except:
                pass
