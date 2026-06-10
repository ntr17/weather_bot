# WeatherBot Autonomy Report
Generated: 2026-06-10 10:39 UTC

## Git

- Local HEAD: `61e3779 brain: update paper strategy review 2026-06-10T10:36:06Z`
- Remote master: `61e3779 brain: update paper strategy review 2026-06-10T10:36:06Z`
```text
## master...github/master
M  .env.example
M  articles/expected_value.txt
M  articles/niche.txt
M  articles/patents.txt
M  articles/polymarket_explained.txt
M  config.paper.json
M  scripts/autonomy_report.py
M  scripts/paper_brain.py
M  scripts/strategy_lab.py
?? scripts/_check_state.py
?? scripts/run_local.ps1
?? scripts/setup_task.ps1
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

- Last run age: `163.4` minutes
- Runs last 1h / 2h / 24h: `0` / `0` / `160`
- New positions last 24h: `0`
- Errors last 24h: `0`
- State balance: `$28.14`
- Open positions: `3`
- Open cost: `$15.00`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Open positions after activation: `0`
- Legacy open positions: `3`

## V3 Actual Edge

- Trades: `51` (43W / 8L)
- Avg entry: `0.742`
- PnL: `$+82.05` on `$1020.19` cost
- ROI: `8.04%`

## Gates

| Gate | Status | Detail |
| --- | --- | --- |
| Actions paper-only | OK | Hosted Actions must not be live. |
| Recent bot activity | BLOCK | 0 runs in last 2h. |
| New data flow | WARN | 0 new positions in last 24h; caps may explain zero. |
| Live max bet | OK | max_bet=5.00; target <= 5. |
| Live total exposure cap | OK | max_total_open_cost=20.00; target <= 20. |
| Current open exposure | OK | open_cost=15.00; reset/wait before live if above cap. |
| Per-run position cap | OK | max_new_positions_per_run=2; target <= 2. |
| NO-only strategy | OK | enable_yes_trading=False. |
| Entry and EV filters | OK | min_ev=0.15, min_no_entry=0.70, max_no_entry=0.85. |
| Resolved edge sample | OK | v3_actual n=51; keep small while sample is limited. |

## Agenda

- Fix paper deployment or scheduler before discussing strategy.
- Prepare compliant non-Actions live runner only after geoblock preflight passes.
- Run fee/spread-aware edge audit before first live order.
- Keep live launch capped at 5 USDC orders and 20 USDC total exposure.
