# Strategy Lab
Generated: 2026-07-27T10:11:24.068350+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 2.25%
  - need positive bootstrap lower bound, have -2.21%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 106 | 90/16 | 7.05% | 5.15% | -2.21% | 0.764 | 0.0438 |
| 2 | d2_ev15 | 106 | 90/16 | 7.05% | 5.15% | -2.21% | 0.764 | 0.0438 |
| 3 | d2_ecmwf_only | 106 | 90/16 | 7.05% | 5.15% | -2.21% | 0.764 | 0.0438 |
| 4 | d2_ev18 | 96 | 80/16 | 6.17% | 4.25% | -4.64% | 0.759 | 0.0263 |
| 5 | ev15_mixed | 117 | 96/21 | 5.63% | 3.73% | -3.43% | 0.763 | 0.0253 |
| 6 | d2_only | 109 | 92/17 | 4.45% | 2.56% | -5.65% | 0.765 | 0.0058 |
| 7 | ecmwf_only | 112 | 94/18 | 4.19% | 2.29% | -5.73% | 0.765 | 0.0029 |
| 8 | d2_entry_72_85 | 96 | 82/14 | 4.30% | 2.42% | -6.72% | 0.773 | 0.0007 |
| 9 | ev18_mixed | 103 | 83/20 | 3.85% | 1.94% | -6.39% | 0.758 | -0.0030 |
| 10 | entry_70_80 | 99 | 79/20 | 2.71% | 0.78% | -8.24% | 0.751 | -0.0210 |
| 11 | entry_72_82 | 95 | 77/18 | 1.78% | -0.11% | -9.16% | 0.764 | -0.0332 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 88 | 73/15 | 4.14% | 2.25% | -6.15% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 122 | 105/17 | 7.04% | 0.76% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 129 | 110/19 | 5.21% | -1.53% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
