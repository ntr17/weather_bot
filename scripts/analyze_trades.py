"""One-time analysis of convergence trade data."""
import sqlite3

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()

# 1) ALL NO trades since May 6
print("=== ALL NO TRADES since May 6 ===")
rows = c.execute("""
SELECT city, date, entry_price, exit_price, cost, pnl, horizon,
       opened_at, closed_at, outcome, reason
FROM trades
WHERE opened_at >= '2026-05-06' AND side='no'
ORDER BY opened_at
""").fetchall()
print(f"Total NO trades: {len(rows)}")
resolved = [r for r in rows if r["outcome"] is not None]
pending = [r for r in rows if r["outcome"] is None]
wins = [r for r in resolved if r["outcome"] == "win"]
losses = [r for r in resolved if r["outcome"] == "loss"]
print(f"Resolved: {len(resolved)} (W:{len(wins)} L:{len(losses)}), Open: {len(pending)}")
if resolved:
    total_pnl = sum(r["pnl"] for r in resolved)
    total_cost = sum(r["cost"] for r in resolved)
    print(f"Total PnL: {total_pnl:.2f}, Total Cost: {total_cost:.2f}, ROI: {total_pnl/total_cost*100:.1f}%")

# 2) By horizon
print("\n=== ALL NO BY HORIZON ===")
for row in c.execute("""
SELECT horizon, COUNT(*) as n,
  SUM(CASE WHEN outcome='win' THEN 1 ELSE 0 END) as w,
  SUM(CASE WHEN outcome='loss' THEN 1 ELSE 0 END) as l,
  SUM(CASE WHEN outcome IS NULL THEN 1 ELSE 0 END) as pending,
  SUM(CASE WHEN outcome IS NOT NULL THEN pnl ELSE 0 END) as total_pnl,
  SUM(CASE WHEN outcome IS NOT NULL THEN cost ELSE 0 END) as total_cost,
  AVG(entry_price) as avg_entry
FROM trades WHERE opened_at >= '2026-05-06' AND side='no'
GROUP BY horizon ORDER BY horizon
"""):
    roi = row[5] / row[6] * 100 if row[6] > 0 else 0
    print(f"  {row[0]}: total={row[1]}, W={row[2]}, L={row[3]}, open={row[4]}, "
          f"pnl={row[5]:.2f}, cost={row[6]:.2f}, ROI={roi:.1f}%, avg_entry={row[7]:.3f}")

# 3) By close reason
print("\n=== ALL NO BY CLOSE REASON ===")
for row in c.execute("""
SELECT reason, horizon, COUNT(*) as n, SUM(pnl) as total_pnl, AVG(pnl) as avg_pnl,
       AVG(entry_price) as avg_entry, AVG(exit_price) as avg_exit
FROM trades WHERE opened_at >= '2026-05-06' AND side='no' AND outcome IS NOT NULL
GROUP BY reason, horizon ORDER BY reason, horizon
"""):
    print(f"  {row[0]} ({row[1]}): n={row[2]}, pnl={row[3]:.2f}, avg_pnl={row[4]:.2f}, "
          f"entry={row[5]:.3f}, exit={row[6]:.3f}")

# 4) Take-profit convergence subset
print("\n=== CONVERGENCE: take_profit at D+1/D+2 ===")
conv = c.execute("""
SELECT city, date, entry_price, exit_price, cost, pnl, horizon, opened_at, closed_at
FROM trades WHERE opened_at >= '2026-05-06' AND side='no'
  AND horizon IN ('D+1','D+2') AND reason='take_profit'
ORDER BY opened_at
""").fetchall()
print(f"Count: {len(conv)}")
for r in conv:
    roi_pct = r["pnl"] / r["cost"] * 100 if r["cost"] > 0 else 0
    print(f"  {r['city']:15} {r['date']} {r['horizon']} "
          f"entry={r['entry_price']:.3f} exit={r['exit_price']:.3f} "
          f"cost={r['cost']:.2f} pnl={r['pnl']:.2f} ({roi_pct:+.1f}%)")

# 5) Resolved wins (held to maturity)
print("\n=== RESOLVED WINS at D+1/D+2 ===")
rw = c.execute("""
SELECT city, date, entry_price, exit_price, cost, pnl, horizon, reason
FROM trades WHERE opened_at >= '2026-05-06' AND side='no'
  AND horizon IN ('D+1','D+2') AND reason='resolved_win'
ORDER BY opened_at
""").fetchall()
print(f"Count: {len(rw)}")
for r in rw:
    roi_pct = r["pnl"] / r["cost"] * 100 if r["cost"] > 0 else 0
    print(f"  {r['city']:15} {r['date']} {r['horizon']} "
          f"entry={r['entry_price']:.3f} exit={r['exit_price']:.3f} "
          f"cost={r['cost']:.2f} pnl={r['pnl']:.2f} ({roi_pct:+.1f}%)")

# 6) Losses
print("\n=== LOSSES at D+1/D+2 ===")
ls = c.execute("""
SELECT city, date, entry_price, exit_price, cost, pnl, horizon, reason
FROM trades WHERE opened_at >= '2026-05-06' AND side='no'
  AND horizon IN ('D+1','D+2') AND outcome='loss'
ORDER BY opened_at
""").fetchall()
print(f"Count: {len(ls)}")
for r in ls:
    print(f"  {r['city']:15} {r['date']} {r['horizon']} "
          f"entry={r['entry_price']:.3f} exit={r['exit_price']:.3f} "
          f"cost={r['cost']:.2f} pnl={r['pnl']:.2f} reason={r['reason']}")

# 7) Entry price distribution for convergence
print("\n=== ENTRY PRICE DISTRIBUTION (all resolved NO D+1/D+2) ===")
for row in c.execute("""
SELECT
  CASE WHEN entry_price < 0.70 THEN '0.65-0.70'
       WHEN entry_price < 0.75 THEN '0.70-0.75'
       WHEN entry_price < 0.80 THEN '0.75-0.80'
       WHEN entry_price < 0.85 THEN '0.80-0.85'
       ELSE '0.85-0.90' END as bucket,
  COUNT(*) as n, SUM(pnl) as total_pnl, AVG(pnl) as avg_pnl
FROM trades WHERE opened_at >= '2026-05-06' AND side='no'
  AND horizon IN ('D+1','D+2') AND outcome IS NOT NULL
GROUP BY bucket ORDER BY bucket
"""):
    print(f"  {row[0]}: n={row[1]}, total_pnl={row[2]:.2f}, avg_pnl={row[3]:.2f}")

# 8) All open positions right now
print("\n=== CURRENTLY OPEN POSITIONS ===")
for row in c.execute("""
SELECT city, date, side, horizon, entry_price, cost, opened_at, bucket_low, bucket_high
FROM trades WHERE outcome IS NULL AND closed_at IS NULL
ORDER BY opened_at
"""):
    print(f"  {row['city']:15} {row['date']} {row['side']:3} {row['horizon']} "
          f"entry={row['entry_price']:.3f} cost={row['cost']:.2f} "
          f"bucket=[{row['bucket_low']},{row['bucket_high']}] opened={row['opened_at']}")

# 9) Overall state
print("\n=== ACCOUNT STATE ===")
state = c.execute("SELECT * FROM state").fetchone()
if state:
    print(dict(state))

# 10) Total trades in DB
total = c.execute("SELECT COUNT(*) FROM trades").fetchone()[0]
print(f"\nTotal trades in DB: {total}")

# 11) All unique horizons and counts
print("\n=== ALL HORIZONS (full DB) ===")
for row in c.execute("""
SELECT horizon, side, COUNT(*) as n,
  SUM(CASE WHEN outcome='win' THEN 1 ELSE 0 END) as w,
  SUM(CASE WHEN outcome='loss' THEN 1 ELSE 0 END) as l,
  SUM(CASE WHEN outcome IS NULL THEN 1 ELSE 0 END) as pending
FROM trades GROUP BY horizon, side ORDER BY horizon, side
"""):
    print(f"  {row[0]} {row[1]}: n={row[2]}, W={row[3]}, L={row[4]}, open={row[5]}")

conn.close()
