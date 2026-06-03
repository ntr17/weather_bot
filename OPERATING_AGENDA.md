# WeatherBot Operating Agenda

Source of truth for project leadership, agent handoffs, and paper-to-live
decisions. This document should be read before changing strategy, deployment,
or money controls.

Last updated: 2026-06-03

## Mission

Make the bot profitable without confusing activity for progress.

The near-term goal is not "trade more." The near-term goal is to prove one
small, repeatable weather-market edge after fees, spread, failed fills, and
operational downtime. Until that is true, the bot stays small.

## Current State

- GitHub Actions is intentionally forced to `PAPER_TRADING=true`.
- Hosted GitHub runners are not a live deployment target because live CLOB
  order placement was blocked by geographic restrictions.
- The live candidate is narrow: NO-only weather positions, real D+1/D+2
  horizons, entry range around 0.70 to 0.85, with strict exposure caps.
- Current paper history suggests a possible V3 edge, but the sample is still
  small enough that it must be treated as promising, not proven.
- The wallet bankroll is about 50 USDC, so fixed costs, fees, spread, and bad
  fills matter more than elegance.

## Operating Principles

1. Money is controlled by deterministic code and explicit caps, not by an LLM.
2. Live trading is forbidden when preflight, region, credentials, or risk caps
   are unclear.
3. Paper trading continues whenever live trading is blocked, because data is
   the asset we can compound safely.
4. Strategy changes must be tied to an audit result or a specific observed bug.
5. No scaling after a lucky run. Scaling requires resolved-trade evidence.
6. The leader raises a blocker clearly when blocked; no guessing, no pretending.

## Agent Roles

These roles can be one person, one Codex session, or several sub-agents. They
exist to keep the thinking clean.

| Role | Owns | Output |
| --- | --- | --- |
| Lead | Agenda, decisions, integration, final calls | Decision memo and next actions |
| Risk Manager | Bankroll, caps, live gates, kill switch | Go/no-go verdict |
| Data Scientist | Edge audit, fee/spread impact, sample quality | Evidence memo |
| Deployment/SRE | Runner, schedule, logs, geoblock, recovery | Deployment status |
| Strategy Researcher | New hypotheses and market niches | Backtestable proposal |
| Code Maintainer | Tests, refactors, bug fixes | Patch plus verification |

## Agent Dialog Protocol

Each agent reports in this shape:

```text
Role:
Question:
Evidence:
Risk:
Recommendation:
Blocked:
```

The Lead then writes a decision memo:

```text
Decision:
Why:
Commands run:
Files changed:
Money impact:
Next check:
```

No agent is allowed to say "go live" without evidence from the Risk Manager and
Data Scientist roles.

## Daily Agenda

Run these checks when opening a new working session:

```powershell
git fetch github master
git status --short --branch
python scripts/autonomy_report.py
python scripts/edge_audit.py
python scripts/verify.py --local
```

Interpretation:

- If local is behind GitHub, inspect and fast-forward before making decisions.
- If the bot has not run recently, fix deployment before strategy.
- If no new paper positions appear for 24h, decide whether that is expected
  from exposure caps or a real scanner/blocking bug.
- If open exposure exceeds the live cap, do not launch live until paper
  positions are reset or closed.
- If edge audit weakens after resolved trades, stop thinking about live launch
  and work on strategy quality.

## Weekly Agenda

1. Re-run `scripts/edge_audit.py` and record the V3 actual-strategy metrics.
2. Separate D+1 from D+2 results.
3. Estimate fee and spread drag using realistic entry prices.
4. Review every full-cost loss manually.
5. Decide whether to keep, tighten, or retire the current strategy.
6. Update this document if the operating thesis changes.

## Live Launch Gates

All gates must be true before live trading:

- Actual runner is not geoblocked and complies with Polymarket restrictions.
- `PAPER_TRADING=false` only on the live runner, never on hosted Actions.
- `PK` and `FUNDER` are present on the live runner and never committed.
- `max_bet <= 5`.
- `max_total_open_cost <= 20`.
- `max_new_positions_per_run <= 2`.
- `enable_yes_trading=false`.
- `min_ev >= 0.12`.
- `min_no_entry >= 0.70`.
- `max_no_entry <= 0.85`.
- No open paper exposure is being mistaken for live exposure.
- `python -m pytest tests` passes.
- The Lead writes a decision memo before the first live order.

## Initial Live Plan

If the gates pass, launch with:

- One tiny allowed runner, preferably a low-cost VPS only if it is compliant and
  not geoblocked.
- NO-only strategy.
- 5 USDC max order size.
- 20 USDC max total open exposure.
- No scaling for at least 20 resolved live trades.
- Manual review after every loss during the first week.

## Scaling Rules

Do not increase size unless all are true:

- At least 20 resolved live trades.
- Positive net PnL after fees and spread.
- No unresolved deployment or fill-quality problems.
- Drawdown stayed within the planned cap.
- The same filters that produced the edge are still active.

First scale step is from 5 USDC to 7.50 USDC max order size, not to a large
bankroll fraction.

## Known Blockers

- Hosted GitHub Actions cannot be trusted for live execution because CLOB order
  placement hit geographic restrictions.
- The current paper state includes old historical artifacts, so status balance
  and total return must be interpreted carefully.
- Some older docs are stale and still describe previous workflows or outdated
  test counts. Prefer this file plus current code and `data/status.md`.

## What To Build Next

1. Add or harden a live-runner preflight command that prints readiness without
   exposing secrets.
2. Add a VPS/systemd deployment path for live mode.
3. Keep hosted GitHub Actions paper-only.
4. Make edge audit explicitly fee/spread-aware.
5. Add a simple daily report artifact that agents can read before working.
6. Improve docs so stale historical instructions are clearly marked.

