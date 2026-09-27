# WeatherBot Autonomy Report
Generated: 2026-09-27 05:24 UTC

## Git

- Local HEAD: `f92ebec bot: update state 2026-09-27T00:14:24Z`
- Remote master: `f92ebec bot: update state 2026-09-27T00:14:24Z`
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
| min_ev | 0.18 |
| min_no_entry | 0.70 |
| max_no_entry | 0.85 |
| max_total_open_cost | 20.00 |
| max_new_positions_per_run | 2 |
| enable_yes_trading | False |

## Activity

- Last run age: `310.2` minutes
- Runs last 1h / 2h / 24h: `0` / `0` / `120`
- New positions last 24h: `0`
- Errors last 24h: `0`
- State balance: `$18.71`
- Open positions: `0`
- Open cost: `$0.00`
- Paper policy activated at: `unknown`
- Open positions after activation: `0`
- Legacy open positions: `0`

## V3 Actual Edge

- Trades: `221` (175W / 46L)
- Avg entry: `0.764`
- PnL: `$+57.62` on `$1870.19` cost
- ROI: `3.08%`

## Gates

| Gate | Status | Detail |
| --- | --- | --- |
| Actions paper-only | OK | Hosted Actions must not be live. |
| Recent bot activity | BLOCK | 0 runs in last 2h. |
| New data flow | WARN | 0 new positions in last 24h; caps may explain zero. |
| Live max bet | OK | max_bet=5.00; target <= 5. |
| Live total exposure cap | OK | max_total_open_cost=20.00; target <= 20. |
| Current open exposure | OK | open_cost=0.00; reset/wait before live if above cap. |
| Per-run position cap | OK | max_new_positions_per_run=2; target <= 2. |
| NO-only strategy | OK | enable_yes_trading=False. |
| Entry and EV filters | OK | min_ev=0.18, min_no_entry=0.70, max_no_entry=0.85. |
| Resolved edge sample | OK | v3_actual n=221; keep small while sample is limited. |

## Agenda

- Fix paper deployment or scheduler before discussing strategy.
- Prepare compliant non-Actions live runner only after geoblock preflight passes.
- Run fee/spread-aware edge audit before first live order.
- Keep live launch capped at 5 USDC orders and 20 USDC total exposure.
