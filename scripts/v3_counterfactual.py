"""
V3 Counterfactual Analysis

V3 disables forecast_changed exits and stop_loss for NO positions.
Under V3, every D+1/D+2 NO position either:
  A) Hits take_profit at entry*1.10 (40% of trades historically), OR
  B) Holds to resolution (wins if NO is correct, loses entire cost if not)

We need to estimate what happens to the 60% that DON'T hit TP.
"""
import sqlite3
import json

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()

# For trades closed via forecast_changed or stop_loss,
# can we determine whether the market eventually resolved in our favor?
# We need to match trades to their market resolution.

# First, check what data markets table has
print("=== MARKET TABLE STRUCTURE ===")
markets = c.execute("SELECT city, date, json_data FROM markets LIMIT 1").fetchone()
if markets:
    data = json.loads(markets["json_data"])
    print(f"Fields: {list(data.keys())}")
    print(f"Status: {data.get('status')}")
    print(f"Actual temp: {data.get('actual_temp')}")
    print(f"Resolved outcome: {data.get('resolved_outcome')}")

# Get all markets that have resolved (have actual_temp)
print("\n=== RESOLVED MARKETS WITH ACTUAL TEMP ===")
resolved_markets = c.execute("""
SELECT city, date, json_data FROM markets
WHERE json_data LIKE '%actual_temp%'
ORDER BY date DESC
""").fetchall()
print(f"Total markets with actual_temp: {len(resolved_markets)}")

# Build lookup: city+date -> actual_temp
temp_lookup = {}
for m in resolved_markets:
    data = json.loads(m["json_data"])
    at = data.get("actual_temp")
    if at is not None:
        temp_lookup[(m["city"], m["date"])] = at

print(f"Markets with actual temp values: {len(temp_lookup)}")
if temp_lookup:
    for k, v in list(temp_lookup.items())[:5]:
        print(f"  {k}: {v}F")

# Now get all D+1/D+2 NO trades that were NOT take_profit
print("\n=== NON-TP TRADES COUNTERFACTUAL ===")
non_tp = c.execute("""
SELECT city, date, entry_price, exit_price, cost, pnl, horizon,
       reason, bucket_low, bucket_high, opened_at
FROM trades
WHERE side='no' AND horizon IN ('D+1','D+2')
  AND pnl IS NOT NULL
  AND reason != 'take_profit'
ORDER BY opened_at
""").fetchall()

would_win = 0
would_lose = 0
unknown = 0
v3_pnl_sum = 0
v3_cost_sum = 0
results = []

for r in non_tp:
    key = (r["city"], r["date"])
    actual = temp_lookup.get(key)
    bl = r["bucket_low"]
    bh = r["bucket_high"]
    entry = r["entry_price"]
    cost = r["cost"]
    shares = cost / entry if entry > 0 else 0

    if actual is not None:
        # NO wins if actual temp is NOT in the bucket
        in_bucket = (bl <= actual <= bh)
        # Handle edge buckets
        if bl == -999:
            in_bucket = actual <= bh
        if bh == 999:
            in_bucket = actual >= bl

        if not in_bucket:
            # NO wins - payout $1/share
            v3_exit = 1.0
            v3_pnl = (v3_exit - entry) * shares
            would_win += 1
            status = "WIN"
        else:
            # NO loses - payout $0
            v3_exit = 0.0
            v3_pnl = -cost  # lose everything
            would_lose += 1
            status = "LOSS"

        v3_pnl_sum += v3_pnl
        v3_cost_sum += cost
        actual_pnl_str = f"actual={actual:.0f}F bucket=[{bl},{bh}] -> {status} v3_pnl={v3_pnl:+.2f}"
    else:
        unknown += 1
        actual_pnl_str = "NO ACTUAL TEMP DATA"
        v3_cost_sum += cost

    results.append((r["city"], r["date"], r["horizon"], r["reason"],
                    entry, cost, r["pnl"], actual_pnl_str))

print(f"Total non-TP trades: {len(non_tp)}")
print(f"Would WIN at resolution: {would_win}")
print(f"Would LOSE at resolution: {would_lose}")
print(f"Unknown (no actual temp): {unknown}")
if would_win + would_lose > 0:
    res_wr = would_win / (would_win + would_lose)
    print(f"Resolution WR: {res_wr:.1%}")
    print(f"V3 PnL for held-to-resolution: ${v3_pnl_sum:.2f}")

# Show some examples
print("\nExamples (first 30):")
for city, date, h, reason, entry, cost, old_pnl, result in results[:30]:
    print(f"  {city:15} {date} {h} {reason:20} entry={entry:.3f} "
          f"cost={cost:.2f} paper_pnl={old_pnl:+.2f} | {result}")

# Now calculate FULL V3 scenario
print("\n" + "="*60)
print("FULL V3 SCENARIO: TP exits + resolution hold")
print("="*60)

# TP trades (same as before)
tp = c.execute("""
SELECT SUM(pnl) as tp_pnl, SUM(cost) as tp_cost, COUNT(*) as n
FROM trades WHERE side='no' AND horizon IN ('D+1','D+2')
  AND pnl IS NOT NULL AND reason='take_profit'
""").fetchone()
tp_pnl = tp["tp_pnl"]
tp_cost = tp["tp_cost"]
tp_n = tp["n"]

total_v3_pnl = tp_pnl + v3_pnl_sum
total_v3_cost = tp_cost + v3_cost_sum
total_v3_n = tp_n + len(non_tp)

print(f"Take-profit exits: n={tp_n}, pnl={tp_pnl:+.2f}, cost={tp_cost:.2f}")
print(f"Resolution holds:  n={would_win+would_lose}, pnl={v3_pnl_sum:+.2f}")
print(f"Unknown:           n={unknown}")
print(f"TOTAL:             n={total_v3_n}, pnl={total_v3_pnl:+.2f}, cost={total_v3_cost:.2f}")
if total_v3_cost > 0:
    print(f"V3 ROI: {total_v3_pnl/total_v3_cost*100:+.1f}%")
    print(f"V3 WR: {(tp_n + would_win)}/{total_v3_n - unknown} = "
          f"{(tp_n + would_win)/(total_v3_n - unknown)*100:.1f}%")

# Fee impact on V3
print(f"\n--- Fee impact ---")
avg_entry = 0.741
avg_shares = 25 / avg_entry
fee_rate = 0.05
# Only TP exits incur exit fees (resolution pays out from contract, no CLOB)
# Entry fee on ALL trades
entry_fee = avg_shares * fee_rate * avg_entry * (1 - avg_entry)
# Exit fee only on TP trades (sell on CLOB)
avg_tp_exit = 0.834  # from the data
exit_fee = avg_shares * fee_rate * avg_tp_exit * (1 - avg_tp_exit)
total_fees_all = entry_fee * total_v3_n + exit_fee * tp_n
print(f"Entry fee per trade: ${entry_fee:.2f}")
print(f"Exit fee (TP only): ${exit_fee:.2f}")
print(f"Total fees ({total_v3_n} entries + {tp_n} TP exits): ${total_fees_all:.2f}")
if total_v3_cost > 0:
    net_v3_pnl = total_v3_pnl - total_fees_all
    print(f"Net V3 PnL after fees: ${net_v3_pnl:+.2f}")
    print(f"Net V3 ROI after fees: {net_v3_pnl/total_v3_cost*100:+.1f}%")

conn.close()
