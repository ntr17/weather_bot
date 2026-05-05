"""Find impossible Tokyo trade."""
import sqlite3
conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Find Tokyo NOs with entry < 0.01
cur.execute("""
SELECT market_id, city, date, side, entry_price, exit_price, pnl, 
       reason, opened_at, closed_at
FROM trades
WHERE city = 'tokyo' AND side = 'no' AND entry_price < 0.01
ORDER BY opened_at DESC
""")

print("=== Tokyo NO Impossible Trades ===")
for row in cur.fetchall():
    print(f"opened={row['opened_at']}")
    print(f"  entry=${row['entry_price']:.4f} exit=${row['exit_price']:.4f}")
    print(f"  closed={row['closed_at']} reason={row['reason']}")
    print()

conn.close()
