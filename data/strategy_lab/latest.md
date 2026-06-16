# Strategy Lab
Generated: 2026-06-16T21:22:06.895146+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 32
  - need >=30 post-activation resolved trades, have 14
  - need post-activation ROI after drag >=3%, have 2.86%
  - need positive bootstrap lower bound, have -5.05%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 32 | 29/3 | 9.38% | 7.46% | -5.05% | 0.760 | 0.0209 |
| 2 | d2_ev15 | 32 | 29/3 | 9.38% | 7.46% | -5.05% | 0.760 | 0.0209 |
| 3 | d2_ecmwf_only | 32 | 29/3 | 9.38% | 7.46% | -5.05% | 0.760 | 0.0209 |
| 4 | ev15_mixed | 43 | 35/8 | 6.67% | 4.75% | -6.36% | 0.758 | 0.0112 |
| 5 | d2_ev18 | 30 | 27/3 | 9.04% | 7.12% | -7.59% | 0.759 | 0.0046 |
| 6 | ev18_mixed | 37 | 30/7 | 4.87% | 2.95% | -10.94% | 0.756 | -0.0348 |
| 7 | entry_70_80 | 44 | 36/8 | 3.59% | 1.68% | -11.69% | 0.757 | -0.0361 |
| 8 | ecmwf_only | 38 | 33/5 | 4.29% | 2.39% | -10.48% | 0.763 | -0.0368 |
| 9 | d2_only | 35 | 31/4 | 4.73% | 2.84% | -11.01% | 0.763 | -0.0401 |
| 10 | d2_entry_72_85 | 33 | 29/4 | 4.05% | 2.16% | -12.38% | 0.767 | -0.0557 |
| 11 | entry_72_82 | 44 | 35/9 | 0.89% | -1.00% | -14.29% | 0.765 | -0.0720 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 14 | 12/2 | 4.76% | 2.86% | -22.14% | 0.763 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 48 | 44/4 | 9.11% | 0.02% | 0.744 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 55 | 49/6 | 6.35% | -2.69% | 0.746 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
