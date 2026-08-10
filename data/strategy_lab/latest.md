# Strategy Lab
Generated: 2026-08-10T02:37:21.758659+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.39%
  - need post-activation ROI after drag >=3%, have -1.95%
  - need positive bootstrap lower bound, have -4.75%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 129 | 105/24 | 4.29% | 2.39% | -4.75% | 0.765 | 0.0073 |
| 2 | d2_ev15 | 129 | 105/24 | 4.29% | 2.39% | -4.75% | 0.765 | 0.0073 |
| 3 | d2_ecmwf_only | 129 | 105/24 | 4.29% | 2.39% | -4.75% | 0.765 | 0.0073 |
| 4 | d2_ev18 | 112 | 91/21 | 4.56% | 2.65% | -5.65% | 0.759 | 0.0067 |
| 5 | ev15_mixed | 140 | 111/29 | 3.27% | 1.37% | -5.49% | 0.764 | -0.0055 |
| 6 | ev18_mixed | 119 | 94/25 | 2.53% | 0.61% | -7.45% | 0.758 | -0.0200 |
| 7 | d2_only | 132 | 107/25 | 2.17% | 0.28% | -7.72% | 0.766 | -0.0242 |
| 8 | ecmwf_only | 135 | 109/26 | 2.01% | 0.12% | -7.39% | 0.766 | -0.0247 |
| 9 | d2_entry_72_85 | 118 | 96/22 | 1.62% | -0.25% | -8.57% | 0.774 | -0.0325 |
| 10 | entry_70_80 | 117 | 91/26 | 1.27% | -0.65% | -9.34% | 0.751 | -0.0392 |
| 11 | entry_72_82 | 114 | 90/24 | 0.38% | -1.51% | -9.93% | 0.764 | -0.0498 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 111 | 88/23 | -0.06% | -1.95% | -9.86% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 145 | 120/25 | 4.93% | -0.61% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 152 | 125/27 | 3.41% | -2.86% | 0.760 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
