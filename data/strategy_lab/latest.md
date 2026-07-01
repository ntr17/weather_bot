# Strategy Lab
Generated: 2026-07-01T20:17:05.869137+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 56
  - need post-activation ROI after drag >=3%, have -4.46%
  - need positive bootstrap lower bound, have -6.18%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 56 | 47/9 | 6.12% | 4.23% | -6.18% | 0.771 | 0.0207 |
| 2 | d2_ev15 | 56 | 47/9 | 6.12% | 4.23% | -6.18% | 0.771 | 0.0207 |
| 3 | d2_ecmwf_only | 56 | 47/9 | 6.12% | 4.23% | -6.18% | 0.771 | 0.0207 |
| 4 | d2_ev18 | 53 | 44/9 | 5.51% | 3.61% | -8.46% | 0.770 | 0.0065 |
| 5 | ev15_mixed | 67 | 53/14 | 4.33% | 2.43% | -7.34% | 0.768 | -0.0014 |
| 6 | d2_only | 59 | 49/10 | 2.67% | 0.78% | -10.62% | 0.772 | -0.0294 |
| 7 | ecmwf_only | 62 | 51/11 | 2.40% | 0.51% | -10.47% | 0.772 | -0.0315 |
| 8 | ev18_mixed | 60 | 47/13 | 2.38% | 0.47% | -10.57% | 0.767 | -0.0323 |
| 9 | entry_70_80 | 61 | 48/13 | 1.91% | 0.00% | -12.16% | 0.760 | -0.0426 |
| 10 | d2_entry_72_85 | 56 | 46/10 | 1.71% | -0.16% | -12.88% | 0.776 | -0.0467 |
| 11 | entry_72_82 | 62 | 48/14 | -0.46% | -2.35% | -14.21% | 0.768 | -0.0732 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 38 | 30/8 | -2.60% | -4.46% | -19.64% | 0.777 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 72 | 62/10 | 6.97% | -1.04% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 79 | 67/12 | 4.73% | -3.85% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
