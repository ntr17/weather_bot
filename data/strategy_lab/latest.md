# Strategy Lab
Generated: 2026-08-02T19:37:40.547577+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have -1.25%
  - need positive bootstrap lower bound, have -4.52%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 118 | 97/21 | 4.93% | 3.03% | -4.52% | 0.764 | 0.0145 |
| 2 | d2_ev15 | 118 | 97/21 | 4.93% | 3.03% | -4.52% | 0.764 | 0.0145 |
| 3 | d2_ecmwf_only | 118 | 97/21 | 4.93% | 3.03% | -4.52% | 0.764 | 0.0145 |
| 4 | d2_ev18 | 104 | 85/19 | 4.86% | 2.95% | -5.73% | 0.759 | 0.0095 |
| 5 | ev15_mixed | 129 | 103/26 | 3.80% | 1.90% | -5.45% | 0.763 | -0.0001 |
| 6 | d2_only | 121 | 99/22 | 2.65% | 0.76% | -7.23% | 0.765 | -0.0177 |
| 7 | ecmwf_only | 124 | 101/23 | 2.47% | 0.57% | -6.91% | 0.765 | -0.0185 |
| 8 | ev18_mixed | 111 | 88/23 | 2.72% | 0.80% | -7.61% | 0.758 | -0.0186 |
| 9 | d2_entry_72_85 | 108 | 89/19 | 2.34% | 0.46% | -8.32% | 0.773 | -0.0245 |
| 10 | entry_70_80 | 110 | 86/24 | 1.49% | -0.43% | -9.15% | 0.751 | -0.0363 |
| 11 | entry_72_82 | 106 | 84/22 | 0.57% | -1.32% | -9.86% | 0.764 | -0.0477 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 100 | 80/20 | 0.64% | -1.25% | -9.69% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 134 | 112/22 | 5.49% | -0.70% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 141 | 117/24 | 3.86% | -2.65% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
