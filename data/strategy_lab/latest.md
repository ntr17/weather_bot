# Strategy Lab
Generated: 2026-09-24T17:17:20.804539+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `unknown`
- Live blockers:
  - need >=30 post-activation resolved trades, have 0
  - need >=3% ROI after fee/spread drag, have 0.39%
  - need positive bootstrap lower bound, have -6.10%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 158 | 126/32 | 2.29% | 0.39% | -6.10% | 0.762 | -0.0175 |
| 2 | d2_ev18 | 158 | 126/32 | 2.29% | 0.39% | -6.10% | 0.762 | -0.0175 |
| 3 | d2_ev15 | 183 | 146/37 | 1.86% | -0.02% | -6.05% | 0.769 | -0.0214 |
| 4 | d2_ecmwf_only | 183 | 146/37 | 1.86% | -0.02% | -6.05% | 0.769 | -0.0214 |
| 5 | ev15_mixed | 194 | 152/42 | 1.23% | -0.66% | -6.39% | 0.768 | -0.0290 |
| 6 | ev18_mixed | 165 | 129/36 | 0.75% | -1.16% | -7.56% | 0.761 | -0.0381 |
| 7 | ecmwf_only | 189 | 150/39 | 0.25% | -1.64% | -7.71% | 0.770 | -0.0434 |
| 8 | d2_only | 186 | 148/38 | 0.33% | -1.56% | -7.96% | 0.770 | -0.0435 |
| 9 | d2_entry_72_85 | 170 | 136/34 | 0.00% | -1.87% | -8.77% | 0.776 | -0.0494 |
| 10 | entry_72_82 | 157 | 123/34 | -0.64% | -2.53% | -9.67% | 0.765 | -0.0591 |
| 11 | entry_70_80 | 155 | 118/37 | -0.75% | -2.67% | -9.99% | 0.752 | -0.0617 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 199 | 161/38 | 2.69% | -2.35% | 0.765 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 206 | 166/40 | 1.55% | -3.71% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
