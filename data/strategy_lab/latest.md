# Strategy Lab
Generated: 2026-08-02T08:38:49.464678+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have -0.24%
  - need positive bootstrap lower bound, have -3.78%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 117 | 97/20 | 5.51% | 3.61% | -3.78% | 0.764 | 0.0229 |
| 2 | d2_ev15 | 117 | 97/20 | 5.51% | 3.61% | -3.78% | 0.764 | 0.0229 |
| 3 | d2_ecmwf_only | 117 | 97/20 | 5.51% | 3.61% | -3.78% | 0.764 | 0.0229 |
| 4 | d2_ev18 | 104 | 85/19 | 4.86% | 2.95% | -5.73% | 0.759 | 0.0095 |
| 5 | ev15_mixed | 128 | 103/25 | 4.32% | 2.42% | -4.86% | 0.763 | 0.0072 |
| 6 | d2_only | 120 | 99/21 | 3.18% | 1.28% | -6.68% | 0.765 | -0.0106 |
| 7 | ecmwf_only | 123 | 101/22 | 2.97% | 1.08% | -6.95% | 0.765 | -0.0135 |
| 8 | d2_entry_72_85 | 107 | 89/18 | 2.91% | 1.04% | -7.62% | 0.772 | -0.0163 |
| 9 | ev18_mixed | 111 | 88/23 | 2.72% | 0.80% | -7.61% | 0.758 | -0.0186 |
| 10 | entry_70_80 | 109 | 86/23 | 2.03% | 0.11% | -8.44% | 0.751 | -0.0284 |
| 11 | entry_72_82 | 105 | 84/21 | 1.13% | -0.77% | -9.31% | 0.763 | -0.0403 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 99 | 80/19 | 1.65% | -0.24% | -8.41% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 133 | 112/21 | 5.90% | -0.24% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 140 | 117/23 | 4.23% | -2.33% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
