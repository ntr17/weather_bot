# Strategy Lab
Generated: 2026-07-18T13:52:56.613403+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 90
  - need post-activation ROI after drag >=3%, have 2.24%
  - need positive bootstrap lower bound, have -2.82%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 90 | 77/13 | 7.34% | 5.44% | -2.82% | 0.767 | 0.0445 |
| 2 | d2_ev15 | 90 | 77/13 | 7.34% | 5.44% | -2.82% | 0.767 | 0.0445 |
| 3 | d2_ecmwf_only | 90 | 77/13 | 7.34% | 5.44% | -2.82% | 0.767 | 0.0445 |
| 4 | d2_ev18 | 83 | 70/13 | 6.59% | 4.69% | -4.90% | 0.763 | 0.0297 |
| 5 | ev15_mixed | 101 | 83/18 | 5.76% | 3.86% | -3.94% | 0.766 | 0.0248 |
| 6 | d2_only | 93 | 79/14 | 4.47% | 2.58% | -6.46% | 0.768 | 0.0032 |
| 7 | ecmwf_only | 96 | 81/15 | 4.18% | 2.29% | -6.51% | 0.768 | 0.0001 |
| 8 | ev18_mixed | 90 | 73/17 | 4.05% | 2.14% | -6.91% | 0.762 | -0.0028 |
| 9 | d2_entry_72_85 | 83 | 71/12 | 3.91% | 2.04% | -8.02% | 0.776 | -0.0077 |
| 10 | entry_70_80 | 85 | 68/17 | 2.78% | 0.86% | -9.19% | 0.753 | -0.0236 |
| 11 | entry_72_82 | 83 | 67/16 | 1.31% | -0.58% | -10.90% | 0.766 | -0.0440 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 72 | 60/12 | 4.11% | 2.24% | -7.28% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 106 | 92/14 | 7.37% | 0.44% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 113 | 97/16 | 5.39% | -1.71% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
