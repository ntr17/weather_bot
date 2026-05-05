"""Check how Tokyo NO $0.001 was opened."""
import sqlite3
import json

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Get the trade
cur.execute("""
SELECT * FROM trades
WHERE city = 'tokyo' AND side = 'no' AND entry_price < 0.01
""")

trade = cur.fetchone()
if trade:
    print("=== Tokyo NO Trade Details ===")
    print(f"opened_at: {trade['opened_at']}")
    print(f"entry_price: ${trade['entry_price']:.4f}")
    print(f"exit_price: ${trade['exit_price']:.4f}")
    print(f"shares: {trade['shares']}")
    print(f"cost: ${trade['cost']:.2f}")
    print(f"pnl: ${trade['pnl']:.2f}")
    print(f"outcome: {trade['outcome']}")
    print(f"forecast_temp: {trade['forecast_temp']}")
    print(f"forecast_source: {trade['forecast_source']}")
    print(f"ev: {trade['ev']:.4f}")
    print(f"p: {trade['p']:.4f}")
    print(f"reason: {trade['reason']}")
    
    if trade['json_data']:
        try:
            data = json.loads(trade['json_data'])
            print(f"\njson_data keys: {data.keys()}")
        except:
            pass
else:
    print("Trade not found")

conn.close()
