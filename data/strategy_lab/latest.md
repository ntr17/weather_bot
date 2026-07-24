# Strategy Lab
Generated: 2026-07-24T14:16:18.463478+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 2.46%
  - need positive bootstrap lower bound, have -2.36%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 102 | 87/15 | 7.22% | 5.32% | -2.36% | 0.765 | 0.0449 |
| 2 | d2_ev15 | 102 | 87/15 | 7.22% | 5.32% | -2.36% | 0.765 | 0.0449 |
| 3 | d2_ecmwf_only | 102 | 87/15 | 7.22% | 5.32% | -2.36% | 0.765 | 0.0449 |
| 4 | d2_ev18 | 92 | 77/15 | 6.34% | 4.43% | -4.31% | 0.760 | 0.0292 |
| 5 | ev15_mixed | 113 | 93/20 | 5.76% | 3.85% | -3.66% | 0.764 | 0.0257 |
| 6 | d2_only | 105 | 89/16 | 4.55% | 2.66% | -5.80% | 0.766 | 0.0063 |
| 7 | ecmwf_only | 108 | 91/17 | 4.28% | 2.39% | -5.94% | 0.766 | 0.0031 |
| 8 | d2_entry_72_85 | 92 | 79/13 | 4.41% | 2.53% | -6.75% | 0.775 | 0.0017 |
| 9 | ev18_mixed | 99 | 80/19 | 3.96% | 2.04% | -6.62% | 0.759 | -0.0028 |
| 10 | entry_70_80 | 95 | 76/19 | 2.77% | 0.85% | -8.80% | 0.751 | -0.0223 |
| 11 | entry_72_82 | 91 | 74/17 | 1.83% | -0.06% | -9.64% | 0.765 | -0.0343 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 84 | 70/14 | 4.35% | 2.46% | -6.12% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 118 | 102/16 | 7.19% | 0.77% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 125 | 107/18 | 5.32% | -1.47% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
