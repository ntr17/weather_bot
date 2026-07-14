# Strategy Lab
Generated: 2026-07-14T03:39:22.596048+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 82
  - need post-activation ROI after drag >=3%, have 1.54%
  - need positive bootstrap lower bound, have -3.22%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 82 | 70/12 | 7.21% | 5.31% | -3.22% | 0.768 | 0.0418 |
| 2 | d2_ev15 | 82 | 70/12 | 7.21% | 5.31% | -3.22% | 0.768 | 0.0418 |
| 3 | d2_ecmwf_only | 82 | 70/12 | 7.21% | 5.31% | -3.22% | 0.768 | 0.0418 |
| 4 | d2_ev18 | 77 | 65/12 | 6.64% | 4.73% | -5.30% | 0.764 | 0.0288 |
| 5 | ev15_mixed | 93 | 76/17 | 5.57% | 3.67% | -4.50% | 0.766 | 0.0209 |
| 6 | d2_only | 85 | 72/13 | 4.21% | 2.32% | -7.39% | 0.769 | -0.0027 |
| 7 | ecmwf_only | 88 | 74/14 | 3.92% | 2.03% | -7.23% | 0.768 | -0.0050 |
| 8 | ev18_mixed | 84 | 68/16 | 3.99% | 2.08% | -7.93% | 0.763 | -0.0069 |
| 9 | d2_entry_72_85 | 76 | 65/11 | 3.86% | 1.99% | -7.96% | 0.776 | -0.0080 |
| 10 | entry_70_80 | 79 | 63/16 | 2.67% | 0.75% | -9.39% | 0.753 | -0.0254 |
| 11 | entry_72_82 | 77 | 62/15 | 1.27% | -0.62% | -10.85% | 0.766 | -0.0442 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 64 | 53/11 | 3.42% | 1.54% | -8.38% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 98 | 85/13 | 7.35% | 0.45% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 105 | 90/15 | 5.31% | -1.93% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
