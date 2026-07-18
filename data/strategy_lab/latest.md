# Strategy Lab
Generated: 2026-07-18T19:35:07.689681+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 91
  - need post-activation ROI after drag >=3%, have 2.69%
  - need positive bootstrap lower bound, have -2.62%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 91 | 78/13 | 7.53% | 5.63% | -2.62% | 0.767 | 0.0471 |
| 2 | d2_ev15 | 91 | 78/13 | 7.53% | 5.63% | -2.62% | 0.767 | 0.0471 |
| 3 | d2_ecmwf_only | 91 | 78/13 | 7.53% | 5.63% | -2.62% | 0.767 | 0.0471 |
| 4 | d2_ev18 | 84 | 71/13 | 6.81% | 4.90% | -4.83% | 0.763 | 0.0321 |
| 5 | ev15_mixed | 102 | 84/18 | 5.94% | 4.04% | -3.87% | 0.765 | 0.0269 |
| 6 | d2_only | 94 | 80/14 | 4.66% | 2.77% | -6.40% | 0.768 | 0.0053 |
| 7 | ecmwf_only | 97 | 82/15 | 4.37% | 2.48% | -6.12% | 0.768 | 0.0034 |
| 8 | ev18_mixed | 91 | 74/17 | 4.28% | 2.37% | -6.84% | 0.761 | -0.0002 |
| 9 | d2_entry_72_85 | 84 | 72/12 | 4.12% | 2.25% | -7.61% | 0.775 | -0.0041 |
| 10 | entry_70_80 | 86 | 69/17 | 2.99% | 1.07% | -9.00% | 0.753 | -0.0208 |
| 11 | entry_72_82 | 84 | 68/16 | 1.53% | -0.36% | -10.38% | 0.766 | -0.0399 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 73 | 61/12 | 4.56% | 2.69% | -6.52% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 107 | 93/14 | 7.48% | 0.59% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 114 | 98/16 | 5.50% | -1.47% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
