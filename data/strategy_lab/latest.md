# Strategy Lab
Generated: 2026-07-20T19:58:55.425745+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 94
  - need post-activation ROI after drag >=3%, have 2.23%
  - need positive bootstrap lower bound, have -2.70%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 94 | 80/14 | 7.26% | 5.36% | -2.70% | 0.765 | 0.0442 |
| 2 | d2_ev15 | 94 | 80/14 | 7.26% | 5.36% | -2.70% | 0.765 | 0.0442 |
| 3 | d2_ecmwf_only | 94 | 80/14 | 7.26% | 5.36% | -2.70% | 0.765 | 0.0442 |
| 4 | d2_ev18 | 87 | 73/14 | 6.52% | 4.61% | -4.52% | 0.761 | 0.0303 |
| 5 | ev15_mixed | 105 | 86/19 | 5.72% | 3.82% | -3.51% | 0.764 | 0.0259 |
| 6 | d2_only | 97 | 82/15 | 4.46% | 2.57% | -6.35% | 0.766 | 0.0035 |
| 7 | ecmwf_only | 100 | 84/16 | 4.18% | 2.29% | -6.24% | 0.766 | 0.0011 |
| 8 | d2_entry_72_85 | 85 | 73/12 | 4.34% | 2.47% | -7.21% | 0.775 | -0.0005 |
| 9 | ev18_mixed | 94 | 76/18 | 4.05% | 2.14% | -6.99% | 0.760 | -0.0031 |
| 10 | entry_70_80 | 89 | 71/18 | 2.81% | 0.89% | -9.06% | 0.751 | -0.0228 |
| 11 | entry_72_82 | 85 | 69/16 | 1.76% | -0.13% | -10.15% | 0.765 | -0.0368 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 76 | 63/13 | 4.12% | 2.23% | -6.83% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 110 | 95/15 | 7.28% | 0.48% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 117 | 100/17 | 5.34% | -1.65% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
