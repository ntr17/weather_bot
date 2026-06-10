# Strategy Lab
Generated: 2026-06-10T20:47:50.443910+00:00

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
| 4 | d2_ev18 | 15 | 14/1 | 9.64% | 7.71% | -8.69% | 0.753 | -0.0233 |
| 5 | ev15_mixed | 27 | 21/6 | 6.47% | 4.54% | -8.70% | 0.754 | -0.0311 |
| 6 | ecmwf_only | 23 | 20/3 | 4.01% | 2.11% | -12.52% | 0.762 | -0.0767 |
| 7 | d2_only | 20 | 18/2 | 4.50% | 2.61% | -13.45% | 0.762 | -0.0810 |
| 8 | ev18_mixed | 21 | 16/5 | 4.24% | 2.31% | -15.86% | 0.751 | -0.0904 |
| 9 | entry_70_80 | 30 | 23/7 | 2.12% | 0.21% | -15.24% | 0.758 | -0.0912 |
| 10 | d2_entry_72_85 | 19 | 17/2 | 4.12% | 2.23% | -14.90% | 0.766 | -0.0919 |
| 11 | entry_72_82 | 29 | 22/7 | 0.22% | -1.67% | -16.82% | 0.764 | -0.1176 |
| 12 | d1_only | 12 | 7/5 | -1.18% | -3.09% | -42.88% | 0.760 | -0.2570 |
| 13 | ensemble_only | 7 | 4/3 | -11.05% | -12.88% | -66.34% | 0.770 | -0.4470 |
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
| D+1 | 19 | 12/7 | -8.99% | -40.69% | 0.754 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 40 | 36/4 | 6.52% | -3.16% | 0.739 |
| ENSEMBLE | 10 | 6/4 | -10.69% | -56.23% | 0.756 |
