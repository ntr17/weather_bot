# WeatherBot Status
_Auto-generated 2026-04-29 13:12 UTC_

## Summary
| Metric | Value |
|--------|-------|
| Mode | PAPER |
| Balance | $830.50 |
| Starting | $1,000.00 |
| Return | -17.0% |
| Total trades | 20 |
| Win rate | 2/20 (10%) |
| Open positions | 7 |
| Markets tracked | 41 |
| Calibration keys | 119 |

## Open Positions (7)
| City | Date | Bucket | Side | Entry | Source | Horizon |
|------|------|--------|------|-------|--------|---------|
| Atlanta | 2026-04-30 | -999–67°F | YES | $0.035 | GFS | D+1 |
| Paris | 2026-04-30 | 22–22°C | YES | $0.190 | ECMWF | D+1 |
| Lucknow | 2026-04-30 | 36–36°C | YES | $0.056 | ECMWF | D+1 |
| Buenos Aires | 2026-04-30 | 22–22°C | YES | $0.180 | ECMWF | D+1 |
| Paris | 2026-05-01 | 24–24°C | YES | $0.120 | ECMWF | D+2 |
| Munich | 2026-05-01 | 18–18°C | YES | $0.120 | ECMWF | D+2 |
| Tokyo | 2026-05-01 | 21–999°C | YES | $0.379 | ECMWF | D+2 |

## Recent Trades (last 2)
| City | Date | Bucket | Side | Entry | PnL | Outcome | Source |
|------|------|--------|------|-------|-----|---------|--------|
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | loss | ECMWF |
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | win | ECMWF |

## City Performance
| City | Trades | Wins | WR | PnL | Avg PnL |
|------|--------|------|-----|-----|---------|
| New York City | 2 | 1 | 50% | +0.00 | +0.00 |

## City Health (last 20 runs)
| City | OK | Fails | Rate | Streak | Status | Last Error |
|------|----|-------|------|--------|--------|------------|
| Ankara | 1 | 0 | 0% | 0 | ok |  |
| Atlanta | 1 | 0 | 0% | 0 | ok |  |
| Buenos Aires | 1 | 0 | 0% | 0 | ok |  |
| Chicago | 1 | 0 | 0% | 0 | ok |  |
| Dallas | 1 | 0 | 0% | 0 | ok |  |
| London | 1 | 0 | 0% | 0 | ok |  |
| Lucknow | 1 | 0 | 0% | 0 | ok |  |
| Miami | 1 | 0 | 0% | 0 | ok |  |
| Munich | 1 | 0 | 0% | 0 | ok |  |
| New York City | 1 | 0 | 0% | 0 | ok |  |
| Paris | 1 | 0 | 0% | 0 | ok |  |
| Sao Paulo | 1 | 0 | 0% | 0 | ok |  |
| Seattle | 1 | 0 | 0% | 0 | ok |  |
| Seoul | 1 | 0 | 0% | 0 | ok |  |
| Shanghai | 1 | 0 | 0% | 0 | ok |  |
| Singapore | 1 | 0 | 0% | 0 | ok |  |
| Tel Aviv | 1 | 0 | 0% | 0 | ok |  |
| Tokyo | 1 | 0 | 0% | 0 | ok |  |
| Toronto | 1 | 0 | 0% | 0 | ok |  |
| Wellington | 1 | 0 | 0% | 0 | ok |  |

## Calibration (119 keys)
| City | ECMWF D+1 σ | GFS D+1 σ | Source | Samples |
|------|-------------|-----------|--------|---------|
| Ankara | 2.708 | 2.708 | bootstrap_persistence | 89 |
| Atlanta | 7.985 | 7.985 | bootstrap_persistence | 89 |
| Buenos Aires | 2.464 | 2.464 | bootstrap_persistence | 89 |
| Chicago | 11.293 | 11.293 | bootstrap_persistence | 89 |
| Dallas | 8.026 | 8.026 | bootstrap_persistence | 89 |
| London | 2.414 | 2.414 | bootstrap_persistence | 89 |
| Miami | 3.859 | 3.859 | bootstrap_persistence | 89 |
| New York City | 8.746 | 8.746 | bootstrap_persistence | 89 |
| Sao Paulo | 2.03 | 2.03 | bootstrap_persistence | 89 |
| Seattle | 5.154 | 5.154 | bootstrap_persistence | 89 |
| Seoul | 3.136 | 3.136 | bootstrap_persistence | 89 |
| Shanghai | 2.999 | 2.999 | bootstrap_persistence | 89 |
| Singapore | 0.945 | 0.945 | bootstrap_persistence | 89 |
| Tel Aviv | 3.101 | 3.101 | bootstrap_persistence | 89 |
| Tokyo | 3.215 | 3.215 | bootstrap_persistence | 89 |
| Toronto | 5.878 | 5.878 | bootstrap_persistence | 89 |
| Wellington | 2.143 | 2.143 | bootstrap_persistence | 89 |

## Active Config
| Param | Value |
|-------|-------|
| max_bet | 20.0 |
| min_ev | 0.08 |
| max_price | 0.6 |
| max_no_price | 0.97 |
| kelly_fraction | 0.25 |
| stop_loss_pct | 0.8 |
| no_stop_loss_floor | 0.85 |
| trailing_activation | 1.2 |
| no_pyes_threshold | 0.15 |
| min_hours | 2.0 |
| max_hours | 168.0 |
