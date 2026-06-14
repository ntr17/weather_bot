# Strategy Lab
Generated: 2026-06-14T09:57:46.213477+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 24
  - need >=30 post-activation resolved trades, have 6
  - need positive bootstrap lower bound, have -6.13%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 24 | 22/2 | 9.84% | 7.92% | -6.13% | 0.760 | 0.0057 |
| 2 | d2_ev15 | 24 | 22/2 | 9.84% | 7.92% | -6.13% | 0.760 | 0.0057 |
| 3 | d2_ecmwf_only | 24 | 22/2 | 9.84% | 7.92% | -6.13% | 0.760 | 0.0057 |
| 4 | ev15_mixed | 35 | 28/7 | 6.84% | 4.92% | -7.25% | 0.758 | -0.0062 |
| 5 | d2_ev18 | 22 | 20/2 | 9.53% | 7.61% | -9.05% | 0.759 | -0.0116 |
| 6 | entry_70_80 | 37 | 30/7 | 3.63% | 1.72% | -12.06% | 0.758 | -0.0510 |
| 7 | ecmwf_only | 30 | 26/4 | 4.29% | 2.39% | -11.20% | 0.764 | -0.0553 |
| 8 | ev18_mixed | 29 | 23/6 | 4.92% | 3.00% | -13.39% | 0.756 | -0.0589 |
| 9 | d2_only | 27 | 24/3 | 4.77% | 2.87% | -11.96% | 0.765 | -0.0592 |
| 10 | d2_entry_72_85 | 25 | 22/3 | 4.03% | 2.15% | -13.37% | 0.770 | -0.0753 |
| 11 | entry_72_82 | 36 | 28/8 | 0.65% | -1.24% | -15.38% | 0.767 | -0.0942 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 6 | 5/1 | 5.37% | 3.48% | -37.90% | 0.768 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 40 | 37/3 | 9.43% | 0.05% | 0.742 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 47 | 42/5 | 6.52% | -2.93% | 0.744 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
