# Strategy Lab
Generated: 2026-06-13T19:56:12.768302+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 21
  - need >=30 post-activation resolved trades, have 3
  - need positive bootstrap lower bound, have -5.14%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 21 | 20/1 | 10.66% | 8.74% | -5.14% | 0.757 | 0.0114 |
| 2 | d2_ev15 | 21 | 20/1 | 10.66% | 8.74% | -5.14% | 0.757 | 0.0114 |
| 3 | d2_ecmwf_only | 21 | 20/1 | 10.66% | 8.74% | -5.14% | 0.757 | 0.0114 |
| 4 | ev15_mixed | 32 | 26/6 | 7.43% | 5.51% | -6.67% | 0.755 | -0.0042 |
| 5 | d2_ev18 | 19 | 18/1 | 10.45% | 8.52% | -7.85% | 0.755 | -0.0043 |
| 6 | ev18_mixed | 26 | 21/5 | 5.59% | 3.67% | -12.26% | 0.752 | -0.0542 |
| 7 | ecmwf_only | 27 | 24/3 | 4.79% | 2.89% | -11.47% | 0.762 | -0.0572 |
| 8 | d2_only | 24 | 22/2 | 5.31% | 3.42% | -11.81% | 0.762 | -0.0591 |
| 9 | entry_70_80 | 35 | 28/7 | 3.18% | 1.27% | -13.80% | 0.758 | -0.0656 |
| 10 | d2_entry_72_85 | 22 | 20/2 | 4.59% | 2.70% | -13.28% | 0.768 | -0.0755 |
| 11 | entry_72_82 | 33 | 26/7 | 1.04% | -0.85% | -15.19% | 0.765 | -0.0957 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 3/0 | 24.20% | 22.27% | 14.00% | 0.750 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 37 | 35/2 | 9.88% | 0.48% | 0.738 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 44 | 40/4 | 6.87% | -2.45% | 0.741 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
