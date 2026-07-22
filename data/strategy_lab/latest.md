# Strategy Lab
Generated: 2026-07-22T19:47:13.776909+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 99
  - need post-activation ROI after drag >=3%, have 2.04%
  - need positive bootstrap lower bound, have -2.49%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 99 | 84/15 | 7.07% | 5.16% | -2.49% | 0.764 | 0.0429 |
| 2 | d2_ev15 | 99 | 84/15 | 7.07% | 5.16% | -2.49% | 0.764 | 0.0429 |
| 3 | d2_ecmwf_only | 99 | 84/15 | 7.07% | 5.16% | -2.49% | 0.764 | 0.0429 |
| 4 | d2_ev18 | 92 | 77/15 | 6.34% | 4.43% | -4.31% | 0.760 | 0.0292 |
| 5 | ev15_mixed | 110 | 90/20 | 5.60% | 3.69% | -3.68% | 0.763 | 0.0240 |
| 6 | d2_only | 102 | 86/16 | 4.36% | 2.47% | -6.24% | 0.765 | 0.0029 |
| 7 | ecmwf_only | 105 | 88/17 | 4.10% | 2.20% | -6.39% | 0.765 | -0.0004 |
| 8 | d2_entry_72_85 | 89 | 76/13 | 4.20% | 2.32% | -7.12% | 0.774 | -0.0017 |
| 9 | ev18_mixed | 99 | 80/19 | 3.96% | 2.04% | -6.62% | 0.759 | -0.0028 |
| 10 | entry_70_80 | 93 | 74/19 | 2.64% | 0.72% | -8.43% | 0.750 | -0.0223 |
| 11 | entry_72_82 | 89 | 72/17 | 1.68% | -0.21% | -9.88% | 0.765 | -0.0367 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 81 | 67/14 | 3.93% | 2.04% | -7.06% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 115 | 99/16 | 7.11% | 0.58% | 0.757 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 122 | 104/18 | 5.22% | -1.65% | 0.757 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
