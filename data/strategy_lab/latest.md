# Strategy Lab
Generated: 2026-07-30T19:55:17.780209+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have -0.08%
  - need positive bootstrap lower bound, have -3.94%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 113 | 94/19 | 5.68% | 3.78% | -3.94% | 0.764 | 0.0240 |
| 2 | d2_ev15 | 113 | 94/19 | 5.68% | 3.78% | -3.94% | 0.764 | 0.0240 |
| 3 | d2_ecmwf_only | 113 | 94/19 | 5.68% | 3.78% | -3.94% | 0.764 | 0.0240 |
| 4 | d2_ev18 | 102 | 84/18 | 5.35% | 3.43% | -5.15% | 0.759 | 0.0163 |
| 5 | ev15_mixed | 124 | 100/24 | 4.45% | 2.55% | -4.29% | 0.763 | 0.0105 |
| 6 | d2_only | 116 | 96/20 | 3.29% | 1.39% | -6.69% | 0.765 | -0.0095 |
| 7 | ecmwf_only | 119 | 98/21 | 3.07% | 1.18% | -6.77% | 0.765 | -0.0119 |
| 8 | ev18_mixed | 109 | 87/22 | 3.15% | 1.24% | -7.14% | 0.758 | -0.0126 |
| 9 | d2_entry_72_85 | 103 | 86/17 | 3.03% | 1.15% | -7.66% | 0.773 | -0.0153 |
| 10 | entry_70_80 | 105 | 83/22 | 2.12% | 0.20% | -8.78% | 0.751 | -0.0287 |
| 11 | entry_72_82 | 101 | 81/20 | 1.20% | -0.69% | -9.79% | 0.764 | -0.0412 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 95 | 77/18 | 1.81% | -0.08% | -8.25% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 129 | 109/20 | 6.05% | -0.15% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 136 | 114/22 | 4.35% | -2.37% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
