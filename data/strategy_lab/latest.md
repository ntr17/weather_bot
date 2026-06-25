# Strategy Lab
Generated: 2026-06-25T15:18:56.938853+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 47
  - need >=30 post-activation resolved trades, have 29
  - need post-activation ROI after drag >=3%, have -9.19%
  - need positive bootstrap lower bound, have -8.32%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 47 | 39/8 | 5.59% | 3.70% | -8.32% | 0.770 | 0.0019 |
| 2 | d2_ev15 | 47 | 39/8 | 5.59% | 3.70% | -8.32% | 0.770 | 0.0019 |
| 3 | d2_ecmwf_only | 47 | 39/8 | 5.59% | 3.70% | -8.32% | 0.770 | 0.0019 |
| 4 | ev15_mixed | 58 | 45/13 | 3.75% | 1.85% | -8.58% | 0.767 | -0.0115 |
| 5 | d2_ev18 | 44 | 36/8 | 4.86% | 2.96% | -10.12% | 0.769 | -0.0178 |
| 6 | d2_only | 50 | 41/9 | 1.95% | 0.07% | -12.34% | 0.772 | -0.0425 |
| 7 | ecmwf_only | 53 | 43/10 | 1.71% | -0.18% | -12.40% | 0.771 | -0.0452 |
| 8 | ev18_mixed | 51 | 39/12 | 1.52% | -0.39% | -12.91% | 0.765 | -0.0491 |
| 9 | entry_70_80 | 53 | 41/12 | 1.33% | -0.59% | -13.74% | 0.759 | -0.0540 |
| 10 | d2_entry_72_85 | 47 | 38/9 | 0.89% | -0.99% | -14.34% | 0.777 | -0.0661 |
| 11 | entry_72_82 | 54 | 41/13 | -1.21% | -3.09% | -15.35% | 0.769 | -0.0846 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 29 | 22/7 | -7.34% | -9.19% | -27.59% | 0.778 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 63 | 54/9 | 6.79% | -1.89% | 0.756 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 70 | 59/11 | 4.48% | -4.29% | 0.756 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
