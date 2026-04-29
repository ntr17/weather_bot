# WeatherBot — Polymarket Weather Trading Bot

**Edge**: Polymarket resolves on AIRPORT coordinates. Most traders price on city center.
That 3–8 °F delta = systematic mispricing on 1–2 °F bucket markets.

## State
Phase 1 — Paper trading. All bugs fixed. 106/106 tests green. Ready to deploy.

---

## Architecture (two-machine rule)

| Machine | Role |
|---------|------|
| **Work machine** | Edit code, run `pytest`, ship to GitHub. Never `main.py`. |
| **Personal machine** | Run the bot. Holds `.env`, `config.json`, `data/`. |

Secrets (API keys, wallet) live only in `.env` on personal machine — never transferred, never committed.
`data/` (markets, state, calibration) lives only on personal machine.

---

## Personal machine — first-time setup

```bash
git clone <repo-url>
cd weather_bot
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp config.template.json config.json
```

Create `.env` (never commit):
```
VISUAL_CROSSING_KEY=your_vc_key
PERSONAL_EMAIL=your@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
# Phase 2 only (leave blank for paper trading):
CLOB_API_KEY=
CLOB_API_SECRET=
CLOB_API_PASSPHRASE=
POLYGON_PRIVATE_KEY=
```

---

## Personal machine — step-by-step first run

### Step 1 — Verify slugs (one-time, ~1 min)

```bash
python scripts/verify_slugs.py
```

This checks which of the 20 cities have live Polymarket temperature markets today.
Expected: ~8–12 cities active at any time.

**If a city shows MISS:**
1. Open `https://gamma-api.polymarket.com/events?slug=highest-temperature-in-<city>-on-<month>-<day>-<year>` in a browser
2. Try slug variations (e.g., `new-york-city` vs `nyc`, `chicago-il` vs `chicago`)
3. If you find the right slug pattern, update `core/locations.py` → ship back to work machine (`scripts\ship.ps1`) → pull on personal machine
4. If Polymarket simply has no market for that city — the bot skips it silently (safe, no action needed)

### Step 2 — Bootstrap sigma (one-time, ~5–20 min)

```bash
python research/bootstrap_sigma.py
```

Fetches 90 days of historical Open-Meteo data for all 20 cities and computes calibrated sigma per city per forecast horizon. Writes `data/calibration.json`.

**Why**: Without this, the bot uses default sigma (2.0 °F for Fahrenheit cities). Bootstrap gives you city-specific, horizon-specific sigma immediately — so probabilities are accurate from trade 1.

Run once. Re-run only if you add new cities.

### Step 3 — Dry run (probe mode)

```bash
python main.py probe
```

Runs one full scan: fetches weather forecasts, prices all markets, computes EV and Kelly sizes — but places NO trades and writes NO state changes. Safe to run anytime.

Check the output for:
- Cities where markets are found
- Forecast temperatures and model spreads
- EV and suggested bet sizes
- Any errors (missing API keys, network issues)

### Step 4 — Start paper trading

```bash
python main.py
```

Runs the full loop: scan every 4 hours, monitor open positions every 15 min.
Trades are paper only (no real money moves) — all results logged to `data/state.json`.

---

## Daily operation

```bash
python main.py status          # balance, open positions, P&L summary
python main.py probe           # one-off scan, no trades
python main.py                 # start the full loop (leave running)
```

Check `data/state.json` for detailed position history.
Check `data/markets/` for individual market files.

---

## Data throughput — what to expect

| Metric | Value |
|--------|-------|
| Cities with active markets | ~8–12 at any time |
| Max open positions | ~80 (20 cities × D+0 through D+3) |
| Resolved trades per day | ~8–12 |
| Bootstrap sigma | Ready from day 1 |
| Global calibration update | ~3 days (30 total trades threshold) |
| Per-city calibration update | ~30 days (30 trades per city) |

You **cannot** increase throughput — each city has at most one market per date, and each date resolves once. More cities = more data; adding cities requires finding their Polymarket slugs.

---

## Monitoring — signs the bot is working

**Healthy signs:**
- `data/state.json` balance changes as positions open/close
- `data/markets/` files have `"status": "open"` positions
- Console shows forecast temperatures and EV values
- After ~3 days: `data/calibration.json` updates with live sigma values

**Warning signs:**
- Balance never changes → scanner finds no markets (check slugs)
- Only YES trades, no NO trades → check `max_no_price` in `config.json` (must be 0.97)
- All positions open but none close → check `config.json` stop-loss and TP settings
- `data/calibration.json` never updates → check Visual Crossing API key

---

## Shipping data back to work machine

You never need to. Code edits happen on work machine. Data stays on personal machine.

If you want to share a `data/state.json` snapshot for analysis, copy it manually.

---

## Config reference (`config.json`)

Key fields to know:

```json
{
  "paper_trading": true,        // MUST be true for Phase 1
  "starting_balance": 10000,    // virtual bankroll
  "max_bet": 50,                // max $ per trade
  "min_ev": 0.05,               // min edge required (5%)
  "max_price": 0.45,            // max YES token price to buy
  "max_no_price": 0.97,         // max NO token price to buy (NO tokens are ~0.85–0.97)
  "scan_interval_minutes": 240, // scan every 4 hours
  "monitor_interval_minutes": 15
}
```

---

## Git rules (strict)

- **Single branch: `master` only.** Never create `main`, `dev`, feature branches, or any other branch.
- **One remote that matters: `github`** (work machine) / **`origin`** (personal machine). Both point to `https://github.com/ntr17/weather_bot`.
- Work machine pushes: `scripts\ship.ps1` → commits + `git push github master`
- Personal machine pulls: `git pull origin master`
- Never `git merge` from remote into a feature branch — there is no feature branch.
- If a stray branch appears: change GitHub default to `master`, then `git push github --delete <branch>`.
- Commit the WIP marker `wip:` for uncommitted local changes before any merge.

## Workflow for code changes

**Work machine:**
1. Edit code
2. `pytest tests/` — must pass before shipping
3. `scripts\ship.ps1` — commits and pushes to GitHub (`master`)

**Personal machine:**
```bash
git pull origin master
```
Then restart `python main.py`. Data in `data/` is untouched by git (gitignored).

---

## Phase 2 — Live trading (future)

When ready to trade real money:
1. Set `"paper_trading": false` in `config.json`
2. Add Polymarket API keys + wallet key to `.env`
3. Implement `_execute_live_order()` stub in `core/executor.py`
4. Start small: lower `max_bet` significantly for first week

**Do not move to Phase 2 until you have at least 30 days of paper trading data showing positive EV.**

---

## Commands cheatsheet

```bash
# Personal machine
python scripts/verify_slugs.py       # check which cities have live markets
python research/bootstrap_sigma.py   # one-time sigma calibration
python main.py probe                 # dry run (safe)
python main.py status                # print P&L and positions
python main.py                       # start trading loop

# Work machine
pytest tests/                        # must pass before shipping
scripts\ship.ps1                     # commit + push to GitHub
```