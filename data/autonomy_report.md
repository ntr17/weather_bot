# WeatherBot Autonomy Report
Generated: 2026-08-27 22:19 UTC

## Git

- Local HEAD: `20623f4 bot: update state 2026-08-27T20:43:00Z`
- Remote master: `20623f4 bot: update state 2026-08-27T20:43:00Z`
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

- Last run age: `96.8` minutes
- Runs last 1h / 2h / 24h: `0` / `20` / `60`
- New positions last 24h: `2`
- Errors last 24h: `0`
- State balance: `$16.16`
- Open positions: `2`
- Open cost: `$10.00`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Open positions after activation: `2`
- Legacy open positions: `0`

## V3 Actual Edge

- Trades: `196` (156W / 40L)
- Avg entry: `0.762`
- PnL: `$+65.07` on `$1745.19` cost
- ROI: `3.73%`

## Gates

| Gate | Status | Detail |
| --- | --- | --- |
| Actions paper-only | OK | Hosted Actions must not be live. |
| Recent bot activity | OK | 20 runs in last 2h. |
| New data flow | OK | 2 new positions in last 24h; caps may explain zero. |
| Live max bet | OK | max_bet=5.00; target <= 5. |
| Live total exposure cap | OK | max_total_open_cost=20.00; target <= 20. |
| Current open exposure | OK | open_cost=10.00; reset/wait before live if above cap. |
| Per-run position cap | OK | max_new_positions_per_run=2; target <= 2. |
| NO-only strategy | OK | enable_yes_trading=False. |
| Entry and EV filters | OK | min_ev=0.15, min_no_entry=0.70, max_no_entry=0.85. |
| Resolved edge sample | OK | v3_actual n=196; keep small while sample is limited. |

## Agenda

- Prepare compliant non-Actions live runner only after geoblock preflight passes.
- Run fee/spread-aware edge audit before first live order.
- Keep live launch capped at 5 USDC orders and 20 USDC total exposure.
