# Strategy Lab
Generated: 2026-07-14T08:29:56.490568+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 83
  - need post-activation ROI after drag >=3%, have 1.70%
  - need positive bootstrap lower bound, have -3.28%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 83 | 71/12 | 7.25% | 5.36% | -3.28% | 0.768 | 0.0421 |
| 2 | d2_ev15 | 83 | 71/12 | 7.25% | 5.36% | -3.28% | 0.768 | 0.0421 |
| 3 | d2_ecmwf_only | 83 | 71/12 | 7.25% | 5.36% | -3.28% | 0.768 | 0.0421 |
| 4 | d2_ev18 | 78 | 66/12 | 6.69% | 4.79% | -5.23% | 0.765 | 0.0296 |
| 5 | ev15_mixed | 94 | 77/17 | 5.62% | 3.72% | -4.49% | 0.766 | 0.0215 |
| 6 | d2_only | 86 | 73/13 | 4.27% | 2.38% | -7.23% | 0.769 | -0.0015 |
| 7 | ecmwf_only | 89 | 75/14 | 3.98% | 2.09% | -7.06% | 0.769 | -0.0038 |
| 8 | ev18_mixed | 85 | 69/16 | 4.05% | 2.15% | -7.73% | 0.763 | -0.0056 |
| 9 | d2_entry_72_85 | 77 | 66/11 | 3.93% | 2.06% | -7.98% | 0.776 | -0.0073 |
| 10 | entry_70_80 | 80 | 64/16 | 2.74% | 0.82% | -9.61% | 0.754 | -0.0254 |
| 11 | entry_72_82 | 78 | 63/15 | 1.35% | -0.54% | -10.93% | 0.766 | -0.0437 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 65 | 54/11 | 3.58% | 1.70% | -8.21% | 0.771 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 99 | 86/13 | 7.37% | 0.28% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 106 | 91/15 | 5.34% | -2.20% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
