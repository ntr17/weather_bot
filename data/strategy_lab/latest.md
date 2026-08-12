# Strategy Lab
Generated: 2026-08-12T07:55:39.619956+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have -0.52%
  - need positive bootstrap lower bound, have -3.71%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 120 | 99/21 | 5.32% | 3.41% | -4.50% | 0.758 | 0.0184 |
| 2 | current_paper | 137 | 113/24 | 4.96% | 3.06% | -3.71% | 0.765 | 0.0176 |
| 3 | d2_ev15 | 137 | 113/24 | 4.96% | 3.06% | -3.71% | 0.765 | 0.0176 |
| 4 | d2_ecmwf_only | 137 | 113/24 | 4.96% | 3.06% | -3.71% | 0.765 | 0.0176 |
| 5 | ev15_mixed | 148 | 119/29 | 3.93% | 2.02% | -4.68% | 0.764 | 0.0038 |
| 6 | ev18_mixed | 127 | 102/25 | 3.34% | 1.43% | -6.13% | 0.758 | -0.0072 |
| 7 | d2_only | 140 | 115/25 | 2.88% | 0.99% | -6.74% | 0.766 | -0.0137 |
| 8 | ecmwf_only | 143 | 117/26 | 2.70% | 0.81% | -6.48% | 0.766 | -0.0146 |
| 9 | d2_entry_72_85 | 126 | 104/22 | 2.42% | 0.54% | -7.46% | 0.772 | -0.0207 |
| 10 | entry_70_80 | 124 | 98/26 | 2.00% | 0.08% | -8.03% | 0.751 | -0.0273 |
| 11 | entry_72_82 | 122 | 98/24 | 1.22% | -0.67% | -8.79% | 0.764 | -0.0375 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 119 | 96/23 | 1.37% | -0.52% | -7.90% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 153 | 128/25 | 5.34% | -0.48% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 160 | 133/27 | 3.83% | -2.27% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
