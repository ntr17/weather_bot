# Strategy Lab
Generated: 2026-06-15T12:45:39.229679+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 27
  - need >=30 post-activation resolved trades, have 9
  - need positive bootstrap lower bound, have -5.27%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 27 | 25/2 | 9.94% | 8.03% | -5.27% | 0.764 | 0.0159 |
| 2 | d2_ev15 | 27 | 25/2 | 9.94% | 8.03% | -5.27% | 0.764 | 0.0159 |
| 3 | d2_ecmwf_only | 27 | 25/2 | 9.94% | 8.03% | -5.27% | 0.764 | 0.0159 |
| 4 | ev15_mixed | 38 | 31/7 | 7.01% | 5.09% | -6.83% | 0.761 | 0.0030 |
| 5 | d2_ev18 | 25 | 23/2 | 9.65% | 7.74% | -7.38% | 0.764 | 0.0016 |
| 6 | ev18_mixed | 32 | 26/6 | 5.19% | 3.28% | -10.83% | 0.760 | -0.0411 |
| 7 | ecmwf_only | 33 | 29/4 | 4.52% | 2.62% | -10.81% | 0.767 | -0.0456 |
| 8 | entry_70_80 | 39 | 32/7 | 3.78% | 1.86% | -12.39% | 0.760 | -0.0468 |
| 9 | d2_only | 30 | 27/3 | 5.00% | 3.10% | -11.23% | 0.768 | -0.0483 |
| 10 | d2_entry_72_85 | 28 | 25/3 | 4.30% | 2.41% | -12.66% | 0.773 | -0.0642 |
| 11 | entry_72_82 | 39 | 31/8 | 0.97% | -0.92% | -15.02% | 0.769 | -0.0838 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 9 | 8/1 | 7.89% | 6.03% | -21.71% | 0.778 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 43 | 40/3 | 9.46% | 0.31% | 0.745 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 50 | 45/5 | 6.59% | -2.37% | 0.747 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
