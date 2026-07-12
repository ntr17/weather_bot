# Strategy Lab
Generated: 2026-07-12T19:33:38.035221+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 78
  - need post-activation ROI after drag >=3%, have 0.17%
  - need positive bootstrap lower bound, have -3.95%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 78 | 66/12 | 6.74% | 4.84% | -3.95% | 0.767 | 0.0346 |
| 2 | d2_ev15 | 78 | 66/12 | 6.74% | 4.84% | -3.95% | 0.767 | 0.0346 |
| 3 | d2_ecmwf_only | 78 | 66/12 | 6.74% | 4.84% | -3.95% | 0.767 | 0.0346 |
| 4 | d2_ev18 | 73 | 61/12 | 6.10% | 4.19% | -6.19% | 0.763 | 0.0202 |
| 5 | ev15_mixed | 89 | 72/17 | 5.11% | 3.21% | -5.31% | 0.765 | 0.0135 |
| 6 | d2_only | 81 | 68/13 | 3.71% | 1.82% | -8.52% | 0.768 | -0.0116 |
| 7 | ecmwf_only | 84 | 70/14 | 3.43% | 1.54% | -8.09% | 0.768 | -0.0129 |
| 8 | ev18_mixed | 80 | 64/16 | 3.40% | 1.49% | -8.31% | 0.762 | -0.0142 |
| 9 | d2_entry_72_85 | 72 | 61/11 | 3.31% | 1.43% | -9.07% | 0.776 | -0.0175 |
| 10 | entry_70_80 | 77 | 61/16 | 2.39% | 0.47% | -9.98% | 0.753 | -0.0302 |
| 11 | entry_72_82 | 73 | 58/15 | 0.66% | -1.23% | -12.18% | 0.765 | -0.0549 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 60 | 49/11 | 2.05% | 0.17% | -10.57% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 94 | 81/13 | 7.09% | 0.10% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 101 | 86/15 | 5.04% | -2.68% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
