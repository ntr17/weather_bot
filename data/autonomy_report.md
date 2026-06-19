# WeatherBot Autonomy Report
Generated: 2026-06-19 20:06 UTC

## Git

- Local HEAD: `82fad59 bot: update state 2026-06-19T19:49:42Z`
- Remote master: `82fad59 bot: update state 2026-06-19T19:49:42Z`
```text
## master...origin/master
```

## Mode

- Hosted Actions forced paper: `True`
- Local `PAPER_TRADING`: `(unset: code defaults to paper)`
- Live evidence in DB: `False` (0 trades, 0 markets)

## Config Caps

| Field | Value |
| --- | ---: |
| balance | 50.00 |
| max_bet | 5.00 |
| min_ev | 0.15 |
| min_no_entry | 0.70 |
| max_no_entry | 0.85 |
| max_total_open_cost | 20.00 |
| max_new_positions_per_run | 2 |
| enable_yes_trading | False |

## Activity

- Last run age: `16.3` minutes
- Runs last 1h / 2h / 24h: `20` / `20` / `160`
- New positions last 24h: `4`
- Errors last 24h: `0`
- State balance: `$23.91`
- Open positions: `4`
- Open cost: `$20.00`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Open positions after activation: `4`
- Legacy open positions: `0`

## V3 Actual Edge

- Trades: `74` (62W / 12L)
- Avg entry: `0.752`
- PnL: `$+82.82` on `$1135.19` cost
- ROI: `7.30%`

## Gates

| Gate | Status | Detail |
| --- | --- | --- |
| Actions paper-only | OK | Hosted Actions must not be live. |
| Recent bot activity | OK | 20 runs in last 2h. |
| New data flow | OK | 4 new positions in last 24h; caps may explain zero. |
| Live max bet | OK | max_bet=5.00; target <= 5. |
| Live total exposure cap | OK | max_total_open_cost=20.00; target <= 20. |
| Current open exposure | OK | open_cost=20.00; reset/wait before live if above cap. |
| Per-run position cap | OK | max_new_positions_per_run=2; target <= 2. |
| NO-only strategy | OK | enable_yes_trading=False. |
| Entry and EV filters | OK | min_ev=0.15, min_no_entry=0.70, max_no_entry=0.85. |
| Resolved edge sample | OK | v3_actual n=74; keep small while sample is limited. |

## Agenda

- Prepare compliant non-Actions live runner only after geoblock preflight passes.
- Run fee/spread-aware edge audit before first live order.
- Keep live launch capped at 5 USDC orders and 20 USDC total exposure.
