# Strategy Lab
Generated: 2026-07-21T08:48:43.976438+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 95
  - need post-activation ROI after drag >=3%, have 2.48%
  - need positive bootstrap lower bound, have -2.49%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 95 | 81/14 | 7.36% | 5.46% | -2.49% | 0.766 | 0.0459 |
| 2 | d2_ev15 | 95 | 81/14 | 7.36% | 5.46% | -2.49% | 0.766 | 0.0459 |
| 3 | d2_ecmwf_only | 95 | 81/14 | 7.36% | 5.46% | -2.49% | 0.766 | 0.0459 |
| 4 | d2_ev18 | 88 | 74/14 | 6.64% | 4.73% | -3.91% | 0.761 | 0.0336 |
| 5 | ev15_mixed | 106 | 87/19 | 5.82% | 3.92% | -3.47% | 0.764 | 0.0271 |
| 6 | d2_only | 98 | 83/15 | 4.57% | 2.68% | -5.92% | 0.767 | 0.0061 |
| 7 | ecmwf_only | 101 | 85/16 | 4.29% | 2.40% | -6.08% | 0.766 | 0.0027 |
| 8 | d2_entry_72_85 | 86 | 74/12 | 4.46% | 2.59% | -7.32% | 0.775 | 0.0003 |
| 9 | ev18_mixed | 95 | 77/18 | 4.18% | 2.27% | -6.82% | 0.760 | -0.0012 |
| 10 | entry_70_80 | 89 | 71/18 | 2.81% | 0.89% | -9.06% | 0.751 | -0.0228 |
| 11 | entry_72_82 | 86 | 70/16 | 1.90% | 0.01% | -9.68% | 0.766 | -0.0338 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 77 | 64/13 | 4.37% | 2.48% | -6.79% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 111 | 96/15 | 7.34% | 0.64% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 118 | 101/17 | 5.40% | -1.65% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
