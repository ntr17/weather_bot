# Strategy Lab
Generated: 2026-07-11T13:57:23.260859+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 76
  - need post-activation ROI after drag >=3%, have -0.84%
  - need positive bootstrap lower bound, have -4.73%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 76 | 64/12 | 6.38% | 4.49% | -4.73% | 0.768 | 0.0284 |
| 2 | d2_ev15 | 76 | 64/12 | 6.38% | 4.49% | -4.73% | 0.768 | 0.0284 |
| 3 | d2_ecmwf_only | 76 | 64/12 | 6.38% | 4.49% | -4.73% | 0.768 | 0.0284 |
| 4 | d2_ev18 | 71 | 59/12 | 5.70% | 3.80% | -6.61% | 0.765 | 0.0149 |
| 5 | ev15_mixed | 87 | 70/17 | 4.78% | 2.88% | -5.75% | 0.766 | 0.0087 |
| 6 | d2_only | 79 | 66/13 | 3.35% | 1.46% | -8.90% | 0.769 | -0.0165 |
| 7 | ecmwf_only | 82 | 68/14 | 3.09% | 1.20% | -8.52% | 0.769 | -0.0178 |
| 8 | d2_entry_72_85 | 71 | 60/11 | 3.17% | 1.30% | -9.34% | 0.777 | -0.0197 |
| 9 | ev18_mixed | 78 | 62/16 | 2.98% | 1.07% | -9.08% | 0.763 | -0.0211 |
| 10 | entry_70_80 | 75 | 59/16 | 2.01% | 0.09% | -10.66% | 0.754 | -0.0364 |
| 11 | entry_72_82 | 72 | 57/15 | 0.52% | -1.38% | -12.28% | 0.766 | -0.0568 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 58 | 47/11 | 1.03% | -0.84% | -12.09% | 0.772 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 92 | 79/13 | 6.88% | -0.47% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 99 | 84/15 | 4.84% | -2.86% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
