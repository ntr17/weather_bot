# Strategy Lab
Generated: 2026-06-11T11:00:06.131029+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 17
  - need >=30 post-activation resolved trades, have 0
  - need positive bootstrap lower bound, have -6.35%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 17 | 16/1 | 9.96% | 8.05% | -6.35% | 0.756 | -0.0077 |
| 2 | d2_ev15 | 17 | 16/1 | 9.96% | 8.05% | -6.35% | 0.756 | -0.0077 |
| 3 | d2_ecmwf_only | 17 | 16/1 | 9.96% | 8.05% | -6.35% | 0.756 | -0.0077 |
| 4 | ev15_mixed | 28 | 22/6 | 6.73% | 4.81% | -7.68% | 0.754 | -0.0228 |
| 5 | d2_ev18 | 15 | 14/1 | 9.64% | 7.71% | -8.69% | 0.753 | -0.0233 |
| 6 | ecmwf_only | 23 | 20/3 | 4.01% | 2.11% | -12.52% | 0.762 | -0.0767 |
| 7 | d2_only | 20 | 18/2 | 4.50% | 2.61% | -13.45% | 0.762 | -0.0810 |
| 8 | ev18_mixed | 22 | 17/5 | 4.61% | 2.68% | -14.92% | 0.751 | -0.0814 |
| 9 | entry_70_80 | 31 | 24/7 | 2.40% | 0.49% | -15.10% | 0.757 | -0.0859 |
| 10 | d2_entry_72_85 | 19 | 17/2 | 4.12% | 2.23% | -14.90% | 0.766 | -0.0919 |
| 11 | entry_72_82 | 30 | 23/7 | 0.54% | -1.36% | -16.24% | 0.763 | -0.1104 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 33 | 31/2 | 9.55% | -0.77% | 0.735 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 40 | 36/4 | 6.52% | -3.16% | 0.739 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
