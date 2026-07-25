# Strategy Lab
Generated: 2026-07-25T08:26:35.135396+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 1.61%
  - need positive bootstrap lower bound, have -3.01%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 104 | 88/16 | 6.75% | 4.85% | -3.01% | 0.764 | 0.0380 |
| 2 | d2_ev15 | 104 | 88/16 | 6.75% | 4.85% | -3.01% | 0.764 | 0.0380 |
| 3 | d2_ecmwf_only | 104 | 88/16 | 6.75% | 4.85% | -3.01% | 0.764 | 0.0380 |
| 4 | d2_ev18 | 94 | 78/16 | 5.82% | 3.91% | -5.07% | 0.759 | 0.0214 |
| 5 | ev15_mixed | 115 | 94/21 | 5.35% | 3.45% | -3.94% | 0.763 | 0.0207 |
| 6 | d2_only | 107 | 90/17 | 4.15% | 2.26% | -6.20% | 0.765 | 0.0009 |
| 7 | ecmwf_only | 110 | 92/18 | 3.90% | 2.00% | -6.36% | 0.765 | -0.0023 |
| 8 | d2_entry_72_85 | 94 | 80/14 | 3.97% | 2.09% | -7.41% | 0.774 | -0.0050 |
| 9 | ev18_mixed | 101 | 81/20 | 3.49% | 1.58% | -6.97% | 0.758 | -0.0086 |
| 10 | entry_70_80 | 97 | 77/20 | 2.38% | 0.45% | -8.79% | 0.750 | -0.0263 |
| 11 | entry_72_82 | 93 | 75/18 | 1.43% | -0.47% | -9.82% | 0.764 | -0.0391 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 86 | 71/15 | 3.49% | 1.61% | -7.08% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 120 | 103/17 | 6.86% | 0.42% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 127 | 108/19 | 5.03% | -1.52% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
