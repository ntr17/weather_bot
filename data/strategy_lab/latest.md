# Strategy Lab
Generated: 2026-07-17T19:35:21.230846+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 89
  - need post-activation ROI after drag >=3%, have 2.01%
  - need positive bootstrap lower bound, have -2.77%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 89 | 76/13 | 7.25% | 5.35% | -2.77% | 0.767 | 0.0438 |
| 2 | d2_ev15 | 89 | 76/13 | 7.25% | 5.35% | -2.77% | 0.767 | 0.0438 |
| 3 | d2_ecmwf_only | 89 | 76/13 | 7.25% | 5.35% | -2.77% | 0.767 | 0.0438 |
| 4 | d2_ev18 | 83 | 70/13 | 6.59% | 4.69% | -4.90% | 0.763 | 0.0297 |
| 5 | ev15_mixed | 100 | 82/18 | 5.68% | 3.77% | -4.03% | 0.765 | 0.0236 |
| 6 | d2_only | 92 | 78/14 | 4.37% | 2.48% | -6.47% | 0.768 | 0.0022 |
| 7 | ecmwf_only | 95 | 80/15 | 4.09% | 2.20% | -6.51% | 0.768 | -0.0008 |
| 8 | ev18_mixed | 90 | 73/17 | 4.05% | 2.14% | -6.91% | 0.762 | -0.0028 |
| 9 | d2_entry_72_85 | 82 | 70/12 | 3.80% | 1.93% | -7.84% | 0.775 | -0.0081 |
| 10 | entry_70_80 | 85 | 68/17 | 2.78% | 0.86% | -9.19% | 0.753 | -0.0236 |
| 11 | entry_72_82 | 83 | 67/16 | 1.31% | -0.58% | -10.90% | 0.766 | -0.0440 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 71 | 59/12 | 3.88% | 2.01% | -7.34% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 105 | 91/14 | 7.32% | 0.37% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 112 | 96/16 | 5.34% | -1.71% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
