# WeatherBot — Agent State File

> **This file is the shared brain between the work machine (GitHub Copilot / VS Code)
> and the personal machine (Claude Code + claude-mem).
> Both agents READ and WRITE here. Always up to date in git.**

---

## Project in One Sentence
Automated paper/live trading bot for Polymarket weather markets.
Edge: Polymarket resolves on AIRPORT coordinates; most traders price on city center.
That 3–8°F delta = systematic mispricing we can exploit.

---

## Current Phase: Phase 1 — Paper Trading

### Phase Map
- [x] Phase 0 — Research: airport offset measured, gopfan2 competitor analyzed
- [ ] Phase 1 — Paper trading: architecture done, needs to run + calibrate (30 resolved trades minimum)
- [ ] Phase 2 — Live trading: CLOB API integration (executor.py placeholder exists)
- [ ] Phase 3 — All cities: expand from TIER1_CITIES to full LOCATIONS dict

### Paper Trading Status
- Bot fully built in `core/` (modular: forecaster, pricer, scanner, executor, calibrator, monitor)
- `PAPER_TRADING=true` default — no real money at risk
- Currently scans: TIER1_CITIES (NYC, Chicago, Miami, Dallas, Seattle, Atlanta)
- Calibration kicks in after 30 resolved trades per city (uses Visual Crossing actuals)
- Data persists in `data/` (gitignored — lives on personal machine only)

---

## Open TODOs

> Update this section on both machines when starting/finishing work.

### Work Machine (Copilot — build tasks)
- [ ] None queued. Waiting for personal machine TODOs to be pasted in.

### Personal Machine (Claude Code — run/debug tasks)
- [ ] UNKNOWN — paste todos from personal machine session here

### Shared / Next Up
- [ ] Verify Polymarket scanner actually finds weather events (API slug format may have changed)
- [ ] Run airport_offset.py on personal to confirm edge is still present
- [ ] Get paper trading running for 1 week and review state.json output
- [ ] Review gopfan2 analysis — what cities/prices does he favor?

---

## Architecture Decisions
- `config.json` — gitignored, machine-specific. Template: `config.template.json`
- `.env` — gitignored, never transferred. Secrets stay on each machine.
- `data/` — gitignored, lives on personal only. Work machine builds code, does not store trade data.
- `archive/` — old monolithic bot versions for reference only (bot_v1.py, bot_v2.py)
- Forecast sources: ECMWF (global, 6h lag) + HRRR/GFS (US only, hourly) + METAR (real-time)

## What Runs Where
| Task | Work machine | Personal machine |
|---|---|---|
| Edit code | YES | NO |
| Run tests (`pytest`) | YES | YES |
| `main.py probe` | NO — calls Polymarket API | YES |
| `main.py` (paper) | NO | YES |
| `main.py` (live) | NEVER | YES (future) |
| Research scripts | NO — call Polymarket | YES |

**IT rule: no Polymarket/crypto API calls from work machine.**

---

## Transfer Workflow (simplified)

### Code: Work → Personal
```
# Work machine (run once when you have changes to ship):
scripts\bundle.ps1
# Opens Desktop with WeatherBot_YYYYMMDD_HHMM.bundle
# Attach to Gmail manually and send to personal email
```
```
# Personal machine (after downloading .bundle from Gmail):
scripts\receive_bundle.ps1
# Auto-detects from Downloads, applies, pushes to GitHub
```

### Data: Personal → Work
Not needed in current phase. Data lives on personal machine.
If analysis is needed on work machine later: copy `data/` folder manually via USB or cloud sync.

---

## Key Files
- `main.py` — entry point: `probe` / `status` / `report` / (blank = trading loop)
- `core/scanner.py` — finds Polymarket events by slug pattern
- `core/forecaster.py` — fetches ECMWF + HRRR + METAR
- `core/pricer.py` — EV calculation, Kelly sizing
- `core/executor.py` — paper/live order execution
- `core/calibrator.py` — adjusts sigma from resolved trades
- `core/monitor.py` — checks stops, trailing stops, resolves closed markets
- `research/airport_offset.py` — Phase 0 proof script (no API key needed)
- `research/weather_intelligence.py` — competitor trade analysis (needs network)
- `research/gopfan2_analyzer.py` — deep analysis of top weather trader

## Config Reference (config.json)
- `min_ev: 0.1` — skip if expected value < 10%
- `kelly_fraction: 0.25` — quarter-Kelly sizing
- `max_price: 0.45` — never buy above 45 cents
- `max_slippage: 0.03` — skip if bid/ask spread > $0.03
- `scan_interval: 3600` — full scan every hour
- `monitor_interval: 600` — stop checks every 10 minutes