# Strategy Lab
Generated: 2026-08-04T20:00:35.444516+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.55%
  - need post-activation ROI after drag >=3%, have -2.03%
  - need positive bootstrap lower bound, have -4.68%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 120 | 98/22 | 4.45% | 2.55% | -4.68% | 0.765 | 0.0091 |
| 2 | d2_ev15 | 120 | 98/22 | 4.45% | 2.55% | -4.68% | 0.765 | 0.0091 |
| 3 | d2_ecmwf_only | 120 | 98/22 | 4.45% | 2.55% | -4.68% | 0.765 | 0.0091 |
| 4 | d2_ev18 | 106 | 86/20 | 4.32% | 2.41% | -5.70% | 0.759 | 0.0042 |
| 5 | ev15_mixed | 131 | 104/27 | 3.38% | 1.48% | -5.78% | 0.764 | -0.0054 |
| 6 | d2_only | 123 | 100/23 | 2.23% | 0.34% | -7.72% | 0.766 | -0.0236 |
| 7 | ecmwf_only | 126 | 102/24 | 2.07% | 0.17% | -7.29% | 0.765 | -0.0238 |
| 8 | ev18_mixed | 113 | 89/24 | 2.22% | 0.31% | -8.08% | 0.758 | -0.0252 |
| 9 | d2_entry_72_85 | 110 | 90/20 | 1.89% | 0.01% | -8.88% | 0.773 | -0.0310 |
| 10 | entry_70_80 | 111 | 86/25 | 0.96% | -0.96% | -9.71% | 0.751 | -0.0436 |
| 11 | entry_72_82 | 108 | 85/23 | 0.15% | -1.75% | -9.94% | 0.764 | -0.0523 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 102 | 81/21 | -0.14% | -2.03% | -10.30% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 136 | 113/23 | 5.14% | -1.22% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 143 | 118/25 | 3.55% | -3.11% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
