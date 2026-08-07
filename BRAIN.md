# WeatherBot Brain
Last review: 2026-08-07 13:42 UTC

## Decision

- Paper action: `keep`
- Best candidate: `d2_ev18`
- Paper config changed: `False`
- Action result: No paper config change requested.
- Ready for live user review: `False`

## Evidence

- Closed positions loaded: `167`
- Current strategy: n=124, ROI after drag=2.54%, bootstrap low=-4.57%
- Best strategy: n=109, ROI after drag=3.03%, bootstrap low=-5.41%
- Post-activation current strategy: n=106, ROI after drag=-1.88%, bootstrap low=-10.04%
- Paper policy activated at: `2026-06-09T18:23:01Z`

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

- need >=3% ROI after fee/spread drag, have 2.54%
- need post-activation ROI after drag >=3%, have -1.88%
- need positive bootstrap lower bound, have -4.57%

## Operating Rule

The brain may change `config.paper.json` only. It may not set `PAPER_TRADING=false`, modify wallet secrets, or increase live risk. When ready, it writes the live-review case here and waits for the user.
