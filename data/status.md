# WeatherBot Status
_Auto-generated 2026-04-30 02:45 UTC_

## Summary
| Metric | Value |
|--------|-------|
| Mode | PAPER |
| Balance | $645.62 |
| Starting | $1,000.00 |
| Return | -35.4% |
| Total trades | 325 |
| Win rate | 5/325 (2%) |
| Open positions | 9 |
| Markets tracked | 41 |
| Calibration keys | 112 |

## Open Positions (9)
| City | Date | Bucket | Side | Entry | Source | Horizon |
|------|------|--------|------|-------|--------|---------|
| Paris | 2026-04-30 | 22–22°C | YES | $0.090 | ECMWF | D+0 |
| Munich | 2026-04-30 | -999–8°C | YES | $0.006 | METAR | D+0 |
| Ankara | 2026-04-30 | 19–19°C | YES | $0.050 | ECMWF | D+0 |
| Shanghai | 2026-04-30 | 17–17°C | YES | $0.044 | ECMWF | D+0 |
| Singapore | 2026-04-30 | 32–32°C | YES | $0.120 | METAR | D+0 |
| Buenos Aires | 2026-04-30 | 23–23°C | YES | $0.270 | ECMWF | D+0 |
| Paris | 2026-05-01 | 24–24°C | YES | $0.140 | ECMWF | D+1 |
| Ankara | 2026-05-01 | 14–14°C | YES | $0.069 | ECMWF | D+1 |
| Tokyo | 2026-05-01 | 21–999°C | YES | $0.350 | ECMWF | D+1 |

## Recent Trades (last 6)
| City | Date | Bucket | Side | Entry | PnL | Outcome | Source |
|------|------|--------|------|-------|-----|---------|--------|
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | loss | ECMWF |
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | win | ECMWF |
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | loss | ECMWF |
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | win | ECMWF |
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | loss | ECMWF |
| New York City | 2025-05-01 | 80–83°F | NO | $0.380 | +0.00 | win | ECMWF |

## City Performance
| City | Trades | Wins | WR | PnL | Avg PnL |
|------|--------|------|-----|-----|---------|
| New York City | 6 | 3 | 50% | +0.00 | +0.00 |

## City Health (last 20 runs)
| City | OK | Fails | Rate | Streak | Status | Last Error |
|------|----|-------|------|--------|--------|------------|
| Ankara | 7 | 0 | 0% | 0 | ok |  |
| Atlanta | 7 | 0 | 0% | 0 | ok |  |
| Buenos Aires | 7 | 0 | 0% | 0 | ok |  |
| Chicago | 7 | 0 | 0% | 0 | ok |  |
| Dallas | 7 | 0 | 0% | 0 | ok |  |
| London | 7 | 0 | 0% | 0 | ok |  |
| Lucknow | 7 | 0 | 0% | 0 | ok |  |
| Miami | 7 | 0 | 0% | 0 | ok |  |
| Munich | 7 | 0 | 0% | 0 | ok |  |
| New York City | 7 | 0 | 0% | 0 | ok |  |
| Paris | 7 | 0 | 0% | 0 | ok |  |
| Sao Paulo | 7 | 0 | 0% | 0 | ok |  |
| Seattle | 7 | 0 | 0% | 0 | ok |  |
| Seoul | 7 | 0 | 0% | 0 | ok |  |
| Shanghai | 7 | 0 | 0% | 0 | ok |  |
| Singapore | 7 | 0 | 0% | 0 | ok |  |
| Tel Aviv | 7 | 0 | 0% | 0 | ok |  |
| Tokyo | 7 | 0 | 0% | 0 | ok |  |
| Toronto | 7 | 0 | 0% | 0 | ok |  |
| Wellington | 7 | 0 | 0% | 0 | ok |  |

## Calibration (112 keys)
| City | ECMWF D+1 σ | GFS D+1 σ | Source | Samples |
|------|-------------|-----------|--------|---------|
| Ankara | 2.708 | 2.708 | bootstrap_persistence | 89 |
| Atlanta | 7.985 | 7.985 | bootstrap_persistence | 89 |
| Chicago | 11.293 | 11.293 | bootstrap_persistence | 89 |
| Dallas | 8.026 | 8.026 | bootstrap_persistence | 89 |
| London | 2.414 | 2.414 | bootstrap_persistence | 89 |
| Lucknow | 1.676 | 1.676 | bootstrap_persistence | 89 |
| Miami | 3.859 | 3.859 | bootstrap_persistence | 89 |
| New York City | 8.746 | 8.746 | bootstrap_persistence | 89 |
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
| max_price | 0.7 |
| max_no_price | 0.985 |
| kelly_fraction | 0.25 |
| stop_loss_pct | 0.8 |
| no_stop_loss_floor | 0.85 |
| trailing_activation | 1.2 |
| no_pyes_threshold | 0.25 |
| min_hours | 2.0 |
| max_hours | 168.0 |
