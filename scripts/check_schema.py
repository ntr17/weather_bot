"""Check schema."""
import sqlite3
conn = sqlite3.connect("data/weatherbot.db")
cur = conn.cursor()

cur.execute("PRAGMA table_info(trades)")
print("Trades table schema:")
for col in cur.fetchall():
    print(f"  {col}")

conn.close()
