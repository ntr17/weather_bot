"""
Diagnostic: For a live weather market, compare what Gamma shows vs what CLOB has.
This answers: are the token IDs valid? Does CLOB have books for them?
Run this ONLY on personal machine (hits APIs).
"""
import json
import requests

# Pick a current weather market — tomorrow's NYC or São Paulo
# Let's find what's live right now
print("=" * 60)
print("STEP 1: Find live weather events from Gamma API")
print("=" * 60)

# Try a few cities for tomorrow (May 20, 2026)
cities = ["new-york-city", "sao-paulo", "chicago", "miami"]
months = ["january","february","march","april","may","june",
          "july","august","september","october","november","december"]

found_event = None
for city in cities:
    slug = f"highest-temperature-in-{city}-on-may-20-2026"
    url = f"https://gamma-api.polymarket.com/events?slug={slug}"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if data and len(data) > 0:
            found_event = data[0]
            print(f"\n✓ Found event: {city} May 20")
            print(f"  Title: {found_event.get('title', 'N/A')}")
            break
    except:
        pass

if not found_event:
    # Try May 21
    for city in cities:
        slug = f"highest-temperature-in-{city}-on-may-21-2026"
        url = f"https://gamma-api.polymarket.com/events?slug={slug}"
        try:
            resp = requests.get(url, timeout=10)
            data = resp.json()
            if data and len(data) > 0:
                found_event = data[0]
                print(f"\n✓ Found event: {city} May 21")
                print(f"  Title: {found_event.get('title', 'N/A')}")
                break
        except:
            pass

if not found_event:
    print("\n✗ No live weather events found. Try different dates.")
    exit(1)

print("\n" + "=" * 60)
print("STEP 2: Check each market's CLOB token IDs")
print("=" * 60)

markets = found_event.get("markets", [])
print(f"\nEvent has {len(markets)} markets (temperature buckets)")

results = []
for i, mkt in enumerate(markets[:8]):  # Check first 8
    question = mkt.get("question", "???")
    market_id = mkt.get("id", "")
    best_bid = mkt.get("bestBid", "N/A")
    best_ask = mkt.get("bestAsk", "N/A")
    
    # Get token IDs
    try:
        token_ids = json.loads(mkt.get("clobTokenIds", "[]"))
    except:
        token_ids = []
    
    clob_yes = token_ids[0] if len(token_ids) >= 1 else ""
    clob_no = token_ids[1] if len(token_ids) >= 2 else ""
    
    print(f"\n--- Market {i+1}: {question}")
    print(f"    Gamma bid/ask: {best_bid} / {best_ask}")
    print(f"    market_id: {market_id}")
    print(f"    clobTokenId YES: {clob_yes[:30]}...")
    print(f"    clobTokenId NO:  {clob_no[:30]}...")
    
    # Now hit the CLOB directly (NO AUTH NEEDED for order book)
    for label, token_id in [("YES", clob_yes), ("NO", clob_no)]:
        if not token_id:
            print(f"    CLOB {label}: NO TOKEN ID")
            continue
        
        clob_url = f"https://clob.polymarket.com/book?token_id={token_id}"
        try:
            r = requests.get(clob_url, timeout=10)
            if r.status_code == 200:
                book = r.json()
                bids = book.get("bids", [])
                asks = book.get("asks", [])
                print(f"    CLOB {label}: ✓ BOOK EXISTS | {len(bids)} bids, {len(asks)} asks")
                if asks:
                    print(f"         Best ask: ${float(asks[0]['price']):.3f} x {asks[0]['size']}")
                if bids:
                    print(f"         Best bid: ${float(bids[0]['price']):.3f} x {bids[0]['size']}")
                results.append({"q": question, "side": label, "status": "OK", "bids": len(bids), "asks": len(asks)})
            elif r.status_code == 404:
                print(f"    CLOB {label}: ✗ 404 — NO ORDER BOOK")
                results.append({"q": question, "side": label, "status": "404"})
            else:
                print(f"    CLOB {label}: ✗ HTTP {r.status_code} — {r.text[:100]}")
                results.append({"q": question, "side": label, "status": f"HTTP {r.status_code}"})
        except Exception as e:
            print(f"    CLOB {label}: ✗ ERROR — {e}")
            results.append({"q": question, "side": label, "status": "error"})

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
ok_count = sum(1 for r in results if r["status"] == "OK")
fail_count = sum(1 for r in results if r["status"] != "OK")
print(f"  Books found: {ok_count}")
print(f"  Books missing: {fail_count}")

if fail_count > 0:
    print("\n  FAILED tokens:")
    for r in results:
        if r["status"] != "OK":
            print(f"    {r['side']} — {r['q'][:50]} — {r['status']}")

if ok_count > 0:
    print("\n  WORKING tokens with liquidity:")
    for r in results:
        if r["status"] == "OK" and (r.get("bids", 0) > 0 or r.get("asks", 0) > 0):
            print(f"    {r['side']} — {r['q'][:50]} — {r['bids']}b/{r['asks']}a")
