# Strategy Lab
Generated: 2026-07-22T14:27:07.824239+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 98
  - need post-activation ROI after drag >=3%, have 1.60%
  - need positive bootstrap lower bound, have -2.85%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 98 | 83/15 | 6.87% | 4.97% | -2.85% | 0.765 | 0.0397 |
| 2 | d2_ev15 | 98 | 83/15 | 6.87% | 4.97% | -2.85% | 0.765 | 0.0397 |
| 3 | d2_ecmwf_only | 98 | 83/15 | 6.87% | 4.97% | -2.85% | 0.765 | 0.0397 |
| 4 | d2_ev18 | 91 | 76/15 | 6.12% | 4.21% | -4.88% | 0.760 | 0.0250 |
| 5 | ev15_mixed | 109 | 89/20 | 5.41% | 3.51% | -4.14% | 0.763 | 0.0206 |
| 6 | d2_only | 101 | 85/16 | 4.17% | 2.28% | -6.53% | 0.766 | -0.0001 |
| 7 | ecmwf_only | 104 | 87/17 | 3.91% | 2.01% | -6.39% | 0.765 | -0.0023 |
| 8 | d2_entry_72_85 | 88 | 75/13 | 3.98% | 2.11% | -7.57% | 0.775 | -0.0054 |
| 9 | ev18_mixed | 98 | 79/19 | 3.73% | 1.82% | -6.93% | 0.759 | -0.0060 |
| 10 | entry_70_80 | 92 | 73/19 | 2.43% | 0.51% | -8.81% | 0.750 | -0.0257 |
| 11 | entry_72_82 | 88 | 71/17 | 1.46% | -0.43% | -10.11% | 0.765 | -0.0397 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 80 | 66/14 | 3.49% | 1.60% | -7.57% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 114 | 98/16 | 6.99% | 0.45% | 0.757 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 121 | 103/18 | 5.10% | -1.90% | 0.757 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
