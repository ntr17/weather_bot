# Strategy Lab
Generated: 2026-06-09T20:22:04.848079+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Live blockers:
  - need >=100 resolved trades, have 17
  - need positive bootstrap lower bound, have -6.35%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 17 | 16/1 | 9.96% | 8.05% | -6.35% | 0.756 | -0.0077 |
| 2 | d2_ev15 | 17 | 16/1 | 9.96% | 8.05% | -6.35% | 0.756 | -0.0077 |
| 3 | d2_ecmwf_only | 17 | 16/1 | 9.96% | 8.05% | -6.35% | 0.756 | -0.0077 |
| 4 | d2_ev18 | 15 | 14/1 | 9.64% | 7.71% | -8.69% | 0.753 | -0.0233 |
| 5 | ev15_mixed | 25 | 20/5 | 7.32% | 5.40% | -7.89% | 0.754 | -0.0236 |
| 6 | ecmwf_only | 23 | 20/3 | 4.01% | 2.11% | -12.52% | 0.762 | -0.0767 |
| 7 | ev18_mixed | 19 | 15/4 | 5.28% | 3.36% | -14.70% | 0.750 | -0.0799 |
| 8 | d2_only | 20 | 18/2 | 4.50% | 2.61% | -13.45% | 0.762 | -0.0810 |
| 9 | entry_70_80 | 28 | 22/6 | 2.81% | 0.90% | -14.82% | 0.757 | -0.0869 |
| 10 | d2_entry_72_85 | 19 | 17/2 | 4.12% | 2.23% | -14.90% | 0.766 | -0.0919 |
| 11 | entry_72_82 | 27 | 21/6 | 0.91% | -0.98% | -16.50% | 0.764 | -0.1135 |
| 12 | d1_only | 10 | 6/4 | 1.87% | -0.03% | -42.20% | 0.760 | -0.2280 |
| 13 | ensemble_only | 6 | 3/3 | -15.05% | -16.88% | -80.41% | 0.770 | -0.5382 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 33 | 31/2 | 9.55% | -0.77% | 0.735 |
| D+1 | 17 | 11/6 | -7.65% | -40.17% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 1 | 1/0 | 40.79% | 42.84% | 0.700 |
| ECMWF | 40 | 36/4 | 6.52% | -3.16% | 0.739 |
| ENSEMBLE | 9 | 5/4 | -13.47% | -64.94% | 0.755 |
