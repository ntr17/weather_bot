# Strategy Lab
Generated: 2026-07-25T19:37:21.932487+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 2.01%
  - need positive bootstrap lower bound, have -2.66%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 105 | 89/16 | 6.94% | 5.04% | -2.66% | 0.764 | 0.0411 |
| 2 | d2_ev15 | 105 | 89/16 | 6.94% | 5.04% | -2.66% | 0.764 | 0.0411 |
| 3 | d2_ecmwf_only | 105 | 89/16 | 6.94% | 5.04% | -2.66% | 0.764 | 0.0411 |
| 4 | d2_ev18 | 95 | 79/16 | 6.04% | 4.13% | -4.89% | 0.759 | 0.0242 |
| 5 | ev15_mixed | 116 | 95/21 | 5.53% | 3.62% | -3.53% | 0.763 | 0.0238 |
| 6 | d2_only | 108 | 91/17 | 4.34% | 2.44% | -6.02% | 0.765 | 0.0033 |
| 7 | ecmwf_only | 111 | 93/18 | 4.08% | 2.18% | -6.30% | 0.765 | -0.0003 |
| 8 | d2_entry_72_85 | 95 | 81/14 | 4.17% | 2.30% | -6.90% | 0.773 | -0.0011 |
| 9 | ev18_mixed | 102 | 82/20 | 3.72% | 1.80% | -6.56% | 0.758 | -0.0050 |
| 10 | entry_70_80 | 98 | 78/20 | 2.58% | 0.66% | -8.70% | 0.750 | -0.0238 |
| 11 | entry_72_82 | 94 | 76/18 | 1.65% | -0.25% | -9.46% | 0.764 | -0.0356 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 87 | 72/15 | 3.90% | 2.01% | -6.20% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 121 | 104/17 | 6.98% | 0.81% | 0.757 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 128 | 109/19 | 5.14% | -1.73% | 0.757 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
