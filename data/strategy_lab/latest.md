# Strategy Lab
Generated: 2026-07-12T08:32:40.096474+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 77
  - need post-activation ROI after drag >=3%, have -0.48%
  - need positive bootstrap lower bound, have -4.49%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 77 | 65/12 | 6.50% | 4.60% | -4.49% | 0.768 | 0.0303 |
| 2 | d2_ev15 | 77 | 65/12 | 6.50% | 4.60% | -4.49% | 0.768 | 0.0303 |
| 3 | d2_ecmwf_only | 77 | 65/12 | 6.50% | 4.60% | -4.49% | 0.768 | 0.0303 |
| 4 | d2_ev18 | 72 | 60/12 | 5.83% | 3.92% | -6.60% | 0.764 | 0.0161 |
| 5 | ev15_mixed | 88 | 71/17 | 4.89% | 2.99% | -5.62% | 0.766 | 0.0102 |
| 6 | d2_only | 80 | 67/13 | 3.47% | 1.58% | -8.18% | 0.769 | -0.0128 |
| 7 | ecmwf_only | 83 | 69/14 | 3.20% | 1.31% | -8.31% | 0.769 | -0.0160 |
| 8 | d2_entry_72_85 | 72 | 61/11 | 3.31% | 1.43% | -9.07% | 0.776 | -0.0175 |
| 9 | ev18_mixed | 79 | 63/16 | 3.12% | 1.21% | -8.61% | 0.762 | -0.0180 |
| 10 | entry_70_80 | 76 | 60/16 | 2.14% | 0.22% | -10.17% | 0.754 | -0.0334 |
| 11 | entry_72_82 | 73 | 58/15 | 0.66% | -1.23% | -12.18% | 0.765 | -0.0549 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 59 | 48/11 | 1.39% | -0.48% | -11.58% | 0.771 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 93 | 80/13 | 6.94% | -0.24% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 100 | 85/15 | 4.90% | -2.72% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
