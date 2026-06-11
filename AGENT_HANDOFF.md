# Agent Handoff

This repo is a Polymarket weather trading bot. It is currently paper-only. Do not enable live trading, change wallet secrets, or raise risk without explicit user approval.

## Current Branch

- Use `master`.
- GitHub remote is `github`, repo `ntr17/weather_bot`.
- Latest known remote commit when this file was written: `466e0bf bot: update state 2026-06-11T07:00:52Z`.

## Read First

1. `BRAIN.md` - current strategy decision and live blockers.
2. `data/strategy_lab/latest.md` - strategy rankings and evidence.
3. `data/autonomy_report.md` - deployment, mode, risk gates, activity.
4. `data/status.md` - current paper positions and bot status.
5. `config.paper.json` - only config the brain is allowed to modify.
6. `.github/workflows/bot.yml` and `.github/workflows/brain.yml` - scheduled paper trading and brain review.

## Operating Rules

- Hosted GitHub Actions must remain paper-only.
- Live mode requires user approval.
- Brain scripts may tune `config.paper.json` only.
- Current live gate requires:
  - at least 100 resolved current-strategy trades,
  - at least 30 post-activation resolved trades,
  - positive bootstrap lower bound,
  - fee/spread-adjusted ROI above threshold.

## Current Thesis

The only promising shape so far is buying NO on exact-temperature weather buckets around D+2 when model forecasts make the bucket look overpriced. D+1 has been weak. Ensemble trades have been weak. The current paper config is intentionally narrow: NO-only, D+2-only, small order size, limited exposure.

## Current Status

- Paper policy activated at `2026-06-09T18:23:01Z`.
- Current strategy evidence: 17 resolved trades, 16 wins / 1 loss, ROI after drag about 8.05%.
- Post-activation current-strategy evidence: 0 resolved trades.
- Not ready for live review.
- Latest status shows paper mode, 3 open positions, 15 USDC open cost.

## What To Improve Next

1. Verify the scheduled paper bot is still running and collecting D+2 data.
2. Explain why post-activation current-strategy resolved count is still 0.
3. Audit whether `data/status.md` return math is misleading because paper balance started from older larger test sizing.
4. Build stronger edge analysis by city, source, horizon, bucket distance, forecast error, liquidity/spread, and time-to-resolution.
5. Stress test real-trading feasibility with 5 USDC orders, fees, spread, fills, geoblock constraints, and CLOB failures.
6. Propose strategy changes only if they are live-executable, measurable, and reversible.

## Useful Commands

```powershell
git fetch github master
git pull --rebase --autostash github master
.\.venv\Scripts\python.exe scripts\apply_paper_strategy.py
.\.venv\Scripts\python.exe scripts\autonomy_report.py --write
.\.venv\Scripts\python.exe scripts\strategy_lab.py --write
.\.venv\Scripts\python.exe scripts\paper_brain.py --apply
.\.venv\Scripts\python.exe -m pytest tests
```

## Prompt For The Next Model

You are taking over as lead engineer, quant researcher, and risk manager for this paper-only Polymarket weather bot. First read `AGENT_HANDOFF.md`, `BRAIN.md`, `data/strategy_lab/latest.md`, `data/autonomy_report.md`, `data/status.md`, and `config.paper.json`. Do not enable live trading. Do not touch secrets. Your job is to verify data collection, diagnose blockers, improve edge research, and propose or implement only paper-mode strategy changes that could later execute live with 5 USDC order sizes. Be skeptical. Separate historical evidence from post-activation evidence. If blocked, say exactly what is missing and what command or file proves it.
