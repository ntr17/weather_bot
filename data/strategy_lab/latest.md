# Strategy Lab
Generated: 2026-08-10T08:07:16.242869+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.59%
  - need post-activation ROI after drag >=3%, have -1.52%
  - need positive bootstrap lower bound, have -4.33%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 114 | 93/21 | 4.80% | 2.88% | -5.10% | 0.759 | 0.0109 |
| 2 | current_paper | 131 | 107/24 | 4.49% | 2.59% | -4.33% | 0.765 | 0.0107 |
| 3 | d2_ev15 | 131 | 107/24 | 4.49% | 2.59% | -4.33% | 0.765 | 0.0107 |
| 4 | d2_ecmwf_only | 131 | 107/24 | 4.49% | 2.59% | -4.33% | 0.765 | 0.0107 |
| 5 | ev15_mixed | 142 | 113/29 | 3.47% | 1.57% | -5.21% | 0.764 | -0.0025 |
| 6 | ev18_mixed | 121 | 96/25 | 2.77% | 0.86% | -7.06% | 0.758 | -0.0161 |
| 7 | d2_only | 134 | 109/25 | 2.38% | 0.49% | -7.43% | 0.766 | -0.0211 |
| 8 | ecmwf_only | 137 | 111/26 | 2.22% | 0.33% | -7.20% | 0.766 | -0.0219 |
| 9 | d2_entry_72_85 | 120 | 98/22 | 1.86% | -0.02% | -8.64% | 0.773 | -0.0304 |
| 10 | entry_70_80 | 119 | 93/26 | 1.50% | -0.42% | -8.87% | 0.751 | -0.0352 |
| 11 | entry_72_82 | 116 | 92/24 | 0.63% | -1.26% | -9.48% | 0.764 | -0.0458 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 113 | 90/23 | 0.37% | -1.52% | -9.45% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 147 | 122/25 | 5.06% | -0.92% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 154 | 127/27 | 3.53% | -2.71% | 0.760 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
