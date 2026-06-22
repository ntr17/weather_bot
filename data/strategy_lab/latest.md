# Strategy Lab
Generated: 2026-06-22T12:28:07.556193+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 43
  - need >=30 post-activation resolved trades, have 25
  - need post-activation ROI after drag >=3%, have -10.67%
  - need positive bootstrap lower bound, have -8.09%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 43 | 36/7 | 5.73% | 3.83% | -8.09% | 0.772 | -0.0040 |
| 2 | d2_ev15 | 43 | 36/7 | 5.73% | 3.83% | -8.09% | 0.772 | -0.0040 |
| 3 | d2_ecmwf_only | 43 | 36/7 | 5.73% | 3.83% | -8.09% | 0.772 | -0.0040 |
| 4 | ev15_mixed | 54 | 42/12 | 3.81% | 1.90% | -8.97% | 0.768 | -0.0124 |
| 5 | d2_ev18 | 40 | 33/7 | 4.99% | 3.08% | -10.54% | 0.770 | -0.0261 |
| 6 | ecmwf_only | 49 | 40/9 | 1.70% | -0.19% | -12.46% | 0.773 | -0.0475 |
| 7 | d2_only | 46 | 38/8 | 1.95% | 0.07% | -12.48% | 0.774 | -0.0510 |
| 8 | entry_70_80 | 49 | 38/11 | 1.31% | -0.60% | -13.67% | 0.760 | -0.0558 |
| 9 | ev18_mixed | 47 | 36/11 | 1.50% | -0.41% | -13.60% | 0.767 | -0.0577 |
| 10 | d2_entry_72_85 | 44 | 36/8 | 1.19% | -0.68% | -14.19% | 0.777 | -0.0685 |
| 11 | entry_72_82 | 51 | 39/12 | -0.98% | -2.86% | -15.80% | 0.769 | -0.0839 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 25 | 19/6 | -8.82% | -10.67% | -30.13% | 0.782 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 59 | 51/8 | 6.93% | -1.71% | 0.756 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 66 | 56/10 | 4.56% | -4.58% | 0.756 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
