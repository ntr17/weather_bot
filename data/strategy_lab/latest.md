# Strategy Lab
Generated: 2026-07-13T19:52:30.271133+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 81
  - need post-activation ROI after drag >=3%, have 1.25%
  - need positive bootstrap lower bound, have -3.47%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 81 | 69/12 | 7.11% | 5.21% | -3.47% | 0.767 | 0.0400 |
| 2 | d2_ev15 | 81 | 69/12 | 7.11% | 5.21% | -3.47% | 0.767 | 0.0400 |
| 3 | d2_ecmwf_only | 81 | 69/12 | 7.11% | 5.21% | -3.47% | 0.767 | 0.0400 |
| 4 | d2_ev18 | 76 | 64/12 | 6.52% | 4.61% | -5.58% | 0.764 | 0.0266 |
| 5 | ev15_mixed | 92 | 75/17 | 5.47% | 3.57% | -4.65% | 0.765 | 0.0194 |
| 6 | d2_only | 84 | 71/13 | 4.10% | 2.21% | -7.19% | 0.768 | -0.0031 |
| 7 | ecmwf_only | 87 | 73/14 | 3.81% | 1.92% | -7.57% | 0.768 | -0.0073 |
| 8 | ev18_mixed | 83 | 67/16 | 3.86% | 1.95% | -7.90% | 0.762 | -0.0081 |
| 9 | d2_entry_72_85 | 75 | 64/11 | 3.74% | 1.86% | -8.72% | 0.776 | -0.0119 |
| 10 | entry_70_80 | 79 | 63/16 | 2.67% | 0.75% | -9.39% | 0.753 | -0.0254 |
| 11 | entry_72_82 | 76 | 61/15 | 1.13% | -0.76% | -10.76% | 0.765 | -0.0453 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 63 | 52/11 | 3.12% | 1.25% | -9.35% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 97 | 84/13 | 7.30% | 0.22% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 104 | 89/15 | 5.25% | -1.98% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
