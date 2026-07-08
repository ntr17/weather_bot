# Strategy Lab
Generated: 2026-07-08T03:48:49.165601+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 68
  - need post-activation ROI after drag >=3%, have 2.77%
  - need positive bootstrap lower bound, have -3.33%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 68 | 59/9 | 8.07% | 6.17% | -3.33% | 0.770 | 0.0500 |
| 2 | d2_ev15 | 68 | 59/9 | 8.07% | 6.17% | -3.33% | 0.770 | 0.0500 |
| 3 | d2_ecmwf_only | 68 | 59/9 | 8.07% | 6.17% | -3.33% | 0.770 | 0.0500 |
| 4 | d2_ev18 | 63 | 54/9 | 7.52% | 5.62% | -5.25% | 0.766 | 0.0378 |
| 5 | ev15_mixed | 79 | 65/14 | 6.17% | 4.27% | -4.72% | 0.767 | 0.0262 |
| 6 | d2_only | 71 | 61/10 | 4.70% | 2.81% | -7.80% | 0.771 | 0.0008 |
| 7 | ecmwf_only | 74 | 63/11 | 4.36% | 2.47% | -7.39% | 0.770 | -0.0012 |
| 8 | ev18_mixed | 70 | 57/13 | 4.53% | 2.62% | -8.24% | 0.764 | -0.0026 |
| 9 | entry_70_80 | 69 | 56/13 | 3.50% | 1.59% | -9.41% | 0.756 | -0.0170 |
| 10 | d2_entry_72_85 | 66 | 56/10 | 3.38% | 1.50% | -9.53% | 0.776 | -0.0184 |
| 11 | entry_72_82 | 69 | 55/14 | 0.88% | -1.01% | -11.81% | 0.766 | -0.0514 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 50 | 42/8 | 4.63% | 2.77% | -9.46% | 0.774 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 84 | 74/10 | 8.02% | 0.81% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 91 | 79/12 | 5.80% | -2.13% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
