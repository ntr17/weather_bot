# WeatherBot Brain
Last review: 2026-06-08 16:31 UTC

## Decision

- Paper action: `adapt_paper`
- Best candidate: `ev15`
- Paper config changed: `False`
- Action result: Recommended paper overlay already active.
- Ready for live user review: `False`

## Evidence

- Closed positions loaded: `55`
- Current strategy: n=28, ROI after drag=3.90%, bootstrap low=-9.79%
- Best strategy: n=23, ROI after drag=7.65%, bootstrap low=-5.63%

## Thesis

- Main thesis: Polymarket exact-temperature weather buckets can overprice unlikely tails when market participants anchor on city-level intuition instead of airport-resolution forecasts.
- Current exploitable shape: buy NO on non-forecast buckets, D+1/D+2, with entry and EV filters tight enough that one full-cost loss does not erase many weak wins.
- The brain is currently optimizing paper filters only. Live mode remains locked behind user approval.

## What I Am Watching

- Whether D+2 continues to dominate D+1 after more resolved trades.
- Whether take-profit exits are hiding unresolved full-loss risk.
- Whether fee and spread drag turn the edge negative at 5 USDC order size.
- Whether any city/source pair contributes repeated full-cost losses.
- Whether deployment keeps producing fresh paper data every few hours.

## Live Blockers

- need >=100 resolved trades, have 28
- need positive bootstrap lower bound, have -9.79%

## Operating Rule

The brain may change `config.paper.json` only. It may not set `PAPER_TRADING=false`, modify wallet secrets, or increase live risk. When ready, it writes the live-review case here and waits for the user.
