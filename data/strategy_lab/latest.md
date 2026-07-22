# Strategy Lab
Generated: 2026-07-22T08:46:57.514829+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 97
  - need post-activation ROI after drag >=3%, have 1.51%
  - need positive bootstrap lower bound, have -2.83%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 97 | 82/15 | 6.84% | 4.94% | -2.83% | 0.765 | 0.0395 |
| 2 | d2_ev15 | 97 | 82/15 | 6.84% | 4.94% | -2.83% | 0.765 | 0.0395 |
| 3 | d2_ecmwf_only | 97 | 82/15 | 6.84% | 4.94% | -2.83% | 0.765 | 0.0395 |
| 4 | d2_ev18 | 90 | 75/15 | 6.08% | 4.17% | -4.86% | 0.761 | 0.0247 |
| 5 | ev15_mixed | 108 | 88/20 | 5.38% | 3.47% | -3.79% | 0.764 | 0.0214 |
| 6 | d2_only | 100 | 84/16 | 4.13% | 2.24% | -6.89% | 0.766 | -0.0017 |
| 7 | ecmwf_only | 103 | 86/17 | 3.87% | 1.97% | -6.63% | 0.766 | -0.0035 |
| 8 | d2_entry_72_85 | 88 | 75/13 | 3.98% | 2.11% | -7.57% | 0.775 | -0.0054 |
| 9 | ev18_mixed | 97 | 78/19 | 3.68% | 1.77% | -7.11% | 0.760 | -0.0072 |
| 10 | entry_70_80 | 91 | 72/19 | 2.38% | 0.46% | -9.02% | 0.751 | -0.0270 |
| 11 | entry_72_82 | 88 | 71/17 | 1.46% | -0.43% | -10.11% | 0.765 | -0.0397 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 79 | 65/14 | 3.39% | 1.51% | -7.78% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 113 | 97/16 | 6.98% | 0.53% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 120 | 102/18 | 5.09% | -1.92% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
