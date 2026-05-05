import sqlite3, json
from collections import Counter
conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row

mkts = conn.execute("SELECT json_data FROM markets").fetchall()

postfix_opened = []
all_open_cost = 0
by_event = Counter()

for row in mkts:
    m = json.loads(row["json_data"])
    for mid, p in m.get("positions", {}).items():
        if p["status"] == "open":
            all_open_cost += p.get("cost", 0)
            by_event[f"{m['city_name']} {m['date']}"] += 1
            opened = p.get("opened_at") or ""
            if opened >= "2026-04-30T08:":
                postfix_opened.append((m["city_name"], m["date"], p["side"], p["cost"]))

print(f"Post-fix open positions: {len(postfix_opened)}")
print(f"Post-fix cost: ${sum(x[3] for x in postfix_opened):.2f}")
print()
print(f"Total open cost: ${all_open_cost:.2f}")
print(f"Balance: $71.71")
print(f"Total capital accounted: ${71.71 + all_open_cost:.2f}")
print()
print("Open positions per event (city+date):")
for event, count in by_event.most_common(20):
    print(f"  {event:35s}: {count}")
print(f"\nTotal events: {len(by_event)}")
print(f"Total open: {sum(by_event.values())}")
print(f"Deployed: ${all_open_cost:.2f} on $812 = {all_open_cost/812*100:.0f}%")

# Pre-fix vs post-fix open positions
pre = sum(1 for x in postfix_opened if False)
post = len(postfix_opened)
pre_count = sum(by_event.values()) - post
print(f"\nPre-fix still-open: {pre_count}")
print(f"Post-fix opened (still open): {post}")

conn.close()
