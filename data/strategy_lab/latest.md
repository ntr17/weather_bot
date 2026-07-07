# Strategy Lab
Generated: 2026-07-07T20:17:46.825987+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 67
  - need post-activation ROI after drag >=3%, have 2.07%
  - need positive bootstrap lower bound, have -3.77%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 67 | 58/9 | 7.84% | 5.94% | -3.77% | 0.770 | 0.0462 |
| 2 | d2_ev15 | 67 | 58/9 | 7.84% | 5.94% | -3.77% | 0.770 | 0.0462 |
| 3 | d2_ecmwf_only | 67 | 58/9 | 7.84% | 5.94% | -3.77% | 0.770 | 0.0462 |
| 4 | d2_ev18 | 62 | 53/9 | 7.26% | 5.36% | -5.57% | 0.767 | 0.0341 |
| 5 | ev15_mixed | 78 | 64/14 | 5.95% | 4.05% | -4.58% | 0.768 | 0.0245 |
| 6 | d2_only | 70 | 60/10 | 4.46% | 2.58% | -7.78% | 0.772 | -0.0014 |
| 7 | ecmwf_only | 73 | 62/11 | 4.13% | 2.25% | -7.85% | 0.771 | -0.0050 |
| 8 | ev18_mixed | 69 | 56/13 | 4.26% | 2.35% | -8.30% | 0.764 | -0.0056 |
| 9 | entry_70_80 | 68 | 55/13 | 3.26% | 1.35% | -9.96% | 0.757 | -0.0214 |
| 10 | d2_entry_72_85 | 65 | 55/10 | 3.12% | 1.24% | -9.75% | 0.777 | -0.0217 |
| 11 | entry_72_82 | 68 | 54/14 | 0.62% | -1.27% | -12.18% | 0.767 | -0.0553 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 49 | 41/8 | 3.93% | 2.07% | -9.75% | 0.775 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 83 | 73/10 | 7.89% | 0.42% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 90 | 78/12 | 5.67% | -2.17% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
