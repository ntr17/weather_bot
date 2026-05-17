import sqlite3, json
conn = sqlite3.connect('data/weatherbot.db')
conn.row_factory = sqlite3.Row
rows = conn.execute("SELECT key, json_data FROM calibration WHERE key LIKE '%ecmwf%' LIMIT 10").fetchall()
for r in rows:
    d = json.loads(r['json_data'])
    print(f"{r['key']:35s} source={d.get('source','?'):25s} n={d.get('n','?')}")
