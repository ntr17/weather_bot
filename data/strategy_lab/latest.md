# Strategy Lab
Generated: 2026-07-23T14:35:55.481331+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 2.32%
  - need positive bootstrap lower bound, have -2.45%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 101 | 86/15 | 7.17% | 5.27% | -2.45% | 0.765 | 0.0441 |
| 2 | d2_ev15 | 101 | 86/15 | 7.17% | 5.27% | -2.45% | 0.765 | 0.0441 |
| 3 | d2_ecmwf_only | 101 | 86/15 | 7.17% | 5.27% | -2.45% | 0.765 | 0.0441 |
| 4 | d2_ev18 | 92 | 77/15 | 6.34% | 4.43% | -4.31% | 0.760 | 0.0292 |
| 5 | ev15_mixed | 112 | 92/20 | 5.70% | 3.80% | -3.34% | 0.764 | 0.0263 |
| 6 | d2_only | 104 | 88/16 | 4.49% | 2.60% | -5.98% | 0.766 | 0.0051 |
| 7 | ecmwf_only | 107 | 90/17 | 4.22% | 2.32% | -5.84% | 0.766 | 0.0028 |
| 8 | d2_entry_72_85 | 91 | 78/13 | 4.34% | 2.46% | -6.91% | 0.774 | 0.0004 |
| 9 | ev18_mixed | 99 | 80/19 | 3.96% | 2.04% | -6.62% | 0.759 | -0.0028 |
| 10 | entry_70_80 | 94 | 75/19 | 2.69% | 0.77% | -8.68% | 0.750 | -0.0227 |
| 11 | entry_72_82 | 90 | 73/17 | 1.74% | -0.15% | -9.52% | 0.765 | -0.0348 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 83 | 69/14 | 4.20% | 2.32% | -6.43% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 117 | 101/16 | 7.16% | 0.76% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 124 | 106/18 | 5.29% | -1.42% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
