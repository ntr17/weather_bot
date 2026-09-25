# WeatherBot Brain
Last review: 2026-09-25 11:57 UTC

## Decision

- Paper action: `keep`
- Best candidate: `current_paper`
- Paper config changed: `False`
- Action result: No paper config change requested.
- Ready for live user review: `False`

## Evidence

- Closed positions loaded: `227`
- Current strategy: n=159, ROI after drag=0.49%, bootstrap low=-6.10%
- Best strategy: n=159, ROI after drag=0.49%, bootstrap low=-6.10%
- Post-activation current strategy: n=0, ROI after drag=0.00%, bootstrap low=0.00%
- Paper policy activated at: `unknown`

## Thesis

- Main thesis: Polymarket exact-temperature weather buckets can overprice unlikely tails when market participants anchor on city-level intuition instead of airport-resolution forecasts.
- Current exploitable shape: buy NO on non-forecast D+2 buckets with entry and EV filters tight enough that one full-cost loss does not erase many weak wins.
- The brain is currently optimizing paper filters only. Live mode remains locked behind user approval.

## What I Am Watching

- Whether D+2 continues to dominate after more resolved trades.
- Whether D+1 remains negative enough to keep excluded from live-applicable paper testing.
- Whether take-profit exits are hiding unresolved full-loss risk.
- Whether fee and spread drag turn the edge negative at 5 USDC order size.
- Whether any city/source pair contributes repeated full-cost losses.
- Whether deployment keeps producing fresh paper data every few hours.

## Live Blockers

- need >=30 post-activation resolved trades, have 0
- need >=3% ROI after fee/spread drag, have 0.49%
- need positive bootstrap lower bound, have -6.10%

## Operating Rule

The brain may change `config.paper.json` only. It may not set `PAPER_TRADING=false`, modify wallet secrets, or increase live risk. When ready, it writes the live-review case here and waits for the user.
