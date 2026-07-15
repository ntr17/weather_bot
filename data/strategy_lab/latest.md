# Strategy Lab
Generated: 2026-07-15T14:13:46.875540+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 85
  - need post-activation ROI after drag >=3%, have 2.13%
  - need positive bootstrap lower bound, have -3.08%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 85 | 73/12 | 7.39% | 5.50% | -3.08% | 0.768 | 0.0442 |
| 2 | d2_ev15 | 85 | 73/12 | 7.39% | 5.50% | -3.08% | 0.768 | 0.0442 |
| 3 | d2_ecmwf_only | 85 | 73/12 | 7.39% | 5.50% | -3.08% | 0.768 | 0.0442 |
| 4 | d2_ev18 | 79 | 67/12 | 6.73% | 4.82% | -4.34% | 0.765 | 0.0330 |
| 5 | ev15_mixed | 96 | 79/17 | 5.76% | 3.86% | -4.45% | 0.766 | 0.0230 |
| 6 | d2_only | 88 | 75/13 | 4.43% | 2.55% | -6.91% | 0.769 | 0.0013 |
| 7 | ecmwf_only | 91 | 77/14 | 4.14% | 2.25% | -6.88% | 0.769 | -0.0016 |
| 8 | ev18_mixed | 86 | 70/16 | 4.11% | 2.20% | -7.25% | 0.763 | -0.0034 |
| 9 | d2_entry_72_85 | 79 | 68/11 | 4.11% | 2.24% | -7.85% | 0.777 | -0.0051 |
| 10 | entry_70_80 | 81 | 65/16 | 2.80% | 0.88% | -9.61% | 0.754 | -0.0248 |
| 11 | entry_72_82 | 80 | 65/15 | 1.56% | -0.33% | -10.65% | 0.767 | -0.0406 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 67 | 56/11 | 4.00% | 2.13% | -7.76% | 0.771 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 101 | 88/13 | 7.45% | 0.70% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 108 | 93/15 | 5.42% | -1.65% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
