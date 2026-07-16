# Strategy Lab
Generated: 2026-07-16T19:36:14.515696+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 88
  - need post-activation ROI after drag >=3%, have 1.64%
  - need positive bootstrap lower bound, have -2.97%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 88 | 75/13 | 7.10% | 5.21% | -2.97% | 0.767 | 0.0417 |
| 2 | d2_ev15 | 88 | 75/13 | 7.10% | 5.21% | -2.97% | 0.767 | 0.0417 |
| 3 | d2_ecmwf_only | 88 | 75/13 | 7.10% | 5.21% | -2.97% | 0.767 | 0.0417 |
| 4 | d2_ev18 | 82 | 69/13 | 6.42% | 4.52% | -5.04% | 0.763 | 0.0276 |
| 5 | ev15_mixed | 99 | 81/18 | 5.53% | 3.63% | -4.34% | 0.765 | 0.0211 |
| 6 | d2_only | 91 | 77/14 | 4.22% | 2.33% | -6.69% | 0.768 | -0.0001 |
| 7 | ecmwf_only | 94 | 79/15 | 3.94% | 2.05% | -6.76% | 0.768 | -0.0032 |
| 8 | ev18_mixed | 89 | 72/17 | 3.87% | 1.97% | -7.22% | 0.762 | -0.0056 |
| 9 | d2_entry_72_85 | 81 | 69/12 | 3.63% | 1.76% | -8.02% | 0.775 | -0.0105 |
| 10 | entry_70_80 | 84 | 67/17 | 2.62% | 0.70% | -9.70% | 0.753 | -0.0270 |
| 11 | entry_72_82 | 82 | 66/16 | 1.13% | -0.76% | -10.40% | 0.766 | -0.0440 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 70 | 58/12 | 3.51% | 1.64% | -8.00% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 104 | 90/14 | 7.23% | 0.45% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 111 | 95/16 | 5.25% | -2.00% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
