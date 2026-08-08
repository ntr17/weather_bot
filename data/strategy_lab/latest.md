# Strategy Lab
Generated: 2026-08-08T19:02:43.897019+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.75%
  - need post-activation ROI after drag >=3%, have -1.43%
  - need positive bootstrap lower bound, have -4.59%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 110 | 90/20 | 5.07% | 3.16% | -5.27% | 0.759 | 0.0132 |
| 2 | current_paper | 126 | 103/23 | 4.65% | 2.75% | -4.59% | 0.765 | 0.0114 |
| 3 | d2_ev15 | 126 | 103/23 | 4.65% | 2.75% | -4.59% | 0.765 | 0.0114 |
| 4 | d2_ecmwf_only | 126 | 103/23 | 4.65% | 2.75% | -4.59% | 0.765 | 0.0114 |
| 5 | ev15_mixed | 137 | 109/28 | 3.59% | 1.69% | -5.38% | 0.764 | -0.0019 |
| 6 | ev18_mixed | 117 | 93/24 | 2.99% | 1.08% | -7.22% | 0.758 | -0.0145 |
| 7 | d2_only | 129 | 105/24 | 2.48% | 0.59% | -7.49% | 0.766 | -0.0203 |
| 8 | ecmwf_only | 132 | 107/25 | 2.31% | 0.41% | -7.15% | 0.766 | -0.0209 |
| 9 | d2_entry_72_85 | 115 | 94/21 | 1.95% | 0.07% | -8.38% | 0.773 | -0.0286 |
| 10 | entry_70_80 | 115 | 90/25 | 1.67% | -0.25% | -8.85% | 0.751 | -0.0335 |
| 11 | entry_72_82 | 112 | 89/23 | 0.78% | -1.11% | -9.80% | 0.764 | -0.0454 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 108 | 86/22 | 0.46% | -1.43% | -9.45% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 142 | 118/24 | 5.22% | -0.86% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 149 | 123/26 | 3.65% | -2.58% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
