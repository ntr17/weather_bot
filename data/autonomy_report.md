# WeatherBot Autonomy Report
Generated: 2026-06-15 05:30 UTC

## Git

- Local HEAD: `368a699 bot: update state 2026-06-15T02:02:37Z`
- Remote master: `368a699 bot: update state 2026-06-15T02:02:37Z`
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

- Last run age: `208.1` minutes
- Runs last 1h / 2h / 24h: `0` / `0` / `200`
- New positions last 24h: `4`
- Errors last 24h: `0`
- State balance: `$34.69`
- Open positions: `2`
- Open cost: `$10.00`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Open positions after activation: `2`
- Legacy open positions: `0`

## V3 Actual Edge

- Trades: `63` (53W / 10L)
- Avg entry: `0.748`
- PnL: `$+83.60` on `$1080.19` cost
- ROI: `7.74%`

## Gates

| Gate | Status | Detail |
| --- | --- | --- |
| Actions paper-only | OK | Hosted Actions must not be live. |
| Recent bot activity | BLOCK | 0 runs in last 2h. |
| New data flow | OK | 4 new positions in last 24h; caps may explain zero. |
| Live max bet | OK | max_bet=5.00; target <= 5. |
| Live total exposure cap | OK | max_total_open_cost=20.00; target <= 20. |
| Current open exposure | OK | open_cost=10.00; reset/wait before live if above cap. |
| Per-run position cap | OK | max_new_positions_per_run=2; target <= 2. |
| NO-only strategy | OK | enable_yes_trading=False. |
| Entry and EV filters | OK | min_ev=0.15, min_no_entry=0.70, max_no_entry=0.85. |
| Resolved edge sample | OK | v3_actual n=63; keep small while sample is limited. |

## Agenda

- Fix paper deployment or scheduler before discussing strategy.
- Prepare compliant non-Actions live runner only after geoblock preflight passes.
- Run fee/spread-aware edge audit before first live order.
- Keep live launch capped at 5 USDC orders and 20 USDC total exposure.
