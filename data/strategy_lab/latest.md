# Strategy Lab
Generated: 2026-06-24T20:13:29.730063+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 45
  - need >=30 post-activation resolved trades, have 27
  - need post-activation ROI after drag >=3%, have -7.08%
  - need positive bootstrap lower bound, have -7.32%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 45 | 38/7 | 6.36% | 4.46% | -7.32% | 0.770 | 0.0090 |
| 2 | d2_ev15 | 45 | 38/7 | 6.36% | 4.46% | -7.32% | 0.770 | 0.0090 |
| 3 | d2_ecmwf_only | 45 | 38/7 | 6.36% | 4.46% | -7.32% | 0.770 | 0.0090 |
| 4 | ev15_mixed | 56 | 44/12 | 4.37% | 2.46% | -8.35% | 0.766 | -0.0046 |
| 5 | d2_ev18 | 42 | 35/7 | 5.70% | 3.79% | -9.36% | 0.768 | -0.0109 |
| 6 | ecmwf_only | 51 | 42/9 | 2.28% | 0.39% | -11.53% | 0.771 | -0.0365 |
| 7 | d2_only | 48 | 40/8 | 2.56% | 0.68% | -11.94% | 0.771 | -0.0390 |
| 8 | ev18_mixed | 49 | 38/11 | 2.23% | 0.32% | -12.58% | 0.764 | -0.0428 |
| 9 | entry_70_80 | 51 | 40/11 | 1.89% | -0.02% | -12.97% | 0.758 | -0.0456 |
| 10 | d2_entry_72_85 | 45 | 37/8 | 1.52% | -0.36% | -13.63% | 0.776 | -0.0613 |
| 11 | entry_72_82 | 52 | 40/12 | -0.67% | -2.55% | -15.01% | 0.768 | -0.0780 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 27 | 21/6 | -5.22% | -7.08% | -25.26% | 0.777 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 61 | 53/8 | 7.26% | -1.61% | 0.755 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 68 | 58/10 | 4.87% | -3.77% | 0.755 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
