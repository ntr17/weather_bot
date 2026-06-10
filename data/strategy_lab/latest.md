# Strategy Lab
Generated: 2026-06-10T10:39:28.738689+00:00

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
| 4 | ev15_mixed | 26 | 21/5 | 7.55% | 5.63% | -7.55% | 0.755 | -0.0181 |
| 5 | d2_ev18 | 15 | 14/1 | 9.64% | 7.71% | -8.69% | 0.753 | -0.0233 |
| 6 | ev18_mixed | 20 | 16/4 | 5.60% | 3.68% | -13.50% | 0.751 | -0.0704 |
| 7 | ecmwf_only | 23 | 20/3 | 4.01% | 2.11% | -12.52% | 0.762 | -0.0767 |
| 8 | d2_only | 20 | 18/2 | 4.50% | 2.61% | -13.45% | 0.762 | -0.0810 |
| 9 | entry_70_80 | 29 | 23/6 | 3.06% | 1.14% | -14.77% | 0.758 | -0.0823 |
| 10 | d2_entry_72_85 | 19 | 17/2 | 4.12% | 2.23% | -14.90% | 0.766 | -0.0919 |
| 11 | entry_72_82 | 28 | 22/6 | 1.19% | -0.71% | -15.81% | 0.764 | -0.1064 |
| 12 | d1_only | 11 | 7/4 | 3.08% | 1.18% | -36.52% | 0.761 | -0.1940 |
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
| D+1 | 18 | 12/6 | -6.83% | -37.18% | 0.754 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 1 | 1/0 | 40.79% | 42.84% | 0.700 |
| ECMWF | 40 | 36/4 | 6.52% | -3.16% | 0.739 |
| ENSEMBLE | 10 | 6/4 | -10.69% | -56.23% | 0.756 |
