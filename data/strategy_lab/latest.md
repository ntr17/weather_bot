# Strategy Lab
Generated: 2026-07-27T19:58:30.214823+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 2.86%
  - need positive bootstrap lower bound, have -2.12%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 108 | 92/16 | 7.33% | 5.43% | -2.12% | 0.764 | 0.0469 |
| 2 | d2_ev15 | 108 | 92/16 | 7.33% | 5.43% | -2.12% | 0.764 | 0.0469 |
| 3 | d2_ecmwf_only | 108 | 92/16 | 7.33% | 5.43% | -2.12% | 0.764 | 0.0469 |
| 4 | d2_ev18 | 98 | 82/16 | 6.50% | 4.58% | -3.97% | 0.759 | 0.0319 |
| 5 | ev15_mixed | 119 | 98/21 | 5.90% | 4.00% | -3.07% | 0.763 | 0.0293 |
| 6 | d2_only | 111 | 94/17 | 4.74% | 2.85% | -5.59% | 0.765 | 0.0089 |
| 7 | ecmwf_only | 114 | 96/18 | 4.47% | 2.58% | -5.47% | 0.765 | 0.0067 |
| 8 | d2_entry_72_85 | 98 | 84/14 | 4.62% | 2.74% | -5.98% | 0.773 | 0.0065 |
| 9 | ev18_mixed | 105 | 85/20 | 4.20% | 2.28% | -6.09% | 0.759 | 0.0015 |
| 10 | entry_70_80 | 101 | 81/20 | 3.02% | 1.10% | -8.08% | 0.751 | -0.0173 |
| 11 | entry_72_82 | 97 | 79/18 | 2.13% | 0.23% | -8.84% | 0.764 | -0.0286 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 90 | 75/15 | 4.75% | 2.86% | -5.30% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 124 | 107/17 | 7.22% | 0.92% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 131 | 112/19 | 5.39% | -1.63% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
