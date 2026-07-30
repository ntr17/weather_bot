# Strategy Lab
Generated: 2026-07-30T09:06:20.837215+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 1.00%
  - need positive bootstrap lower bound, have -3.09%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 112 | 94/18 | 6.28% | 4.38% | -3.09% | 0.765 | 0.0330 |
| 2 | d2_ev15 | 112 | 94/18 | 6.28% | 4.38% | -3.09% | 0.765 | 0.0330 |
| 3 | d2_ecmwf_only | 112 | 94/18 | 6.28% | 4.38% | -3.09% | 0.765 | 0.0330 |
| 4 | d2_ev18 | 101 | 84/17 | 6.02% | 4.11% | -4.47% | 0.759 | 0.0255 |
| 5 | ev15_mixed | 123 | 100/23 | 4.99% | 3.08% | -3.74% | 0.764 | 0.0177 |
| 6 | d2_only | 115 | 96/19 | 3.83% | 1.93% | -6.31% | 0.766 | -0.0028 |
| 7 | ev18_mixed | 108 | 87/21 | 3.78% | 1.87% | -6.46% | 0.758 | -0.0039 |
| 8 | ecmwf_only | 118 | 98/20 | 3.59% | 1.70% | -6.14% | 0.765 | -0.0045 |
| 9 | d2_entry_72_85 | 102 | 86/16 | 3.62% | 1.74% | -6.77% | 0.773 | -0.0063 |
| 10 | entry_70_80 | 104 | 83/21 | 2.67% | 0.75% | -7.82% | 0.751 | -0.0199 |
| 11 | entry_72_82 | 100 | 81/19 | 1.78% | -0.12% | -9.08% | 0.764 | -0.0330 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 94 | 77/17 | 2.89% | 1.00% | -7.19% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 128 | 109/19 | 6.47% | 0.04% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 135 | 114/21 | 4.73% | -1.79% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
