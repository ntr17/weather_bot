# Strategy Lab
Generated: 2026-06-18T20:40:41.288437+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 34
  - need >=30 post-activation resolved trades, have 16
  - need positive bootstrap lower bound, have -4.73%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 34 | 31/3 | 9.54% | 7.63% | -4.73% | 0.763 | 0.0278 |
| 2 | d2_ev15 | 34 | 31/3 | 9.54% | 7.63% | -4.73% | 0.763 | 0.0278 |
| 3 | d2_ecmwf_only | 34 | 31/3 | 9.54% | 7.63% | -4.73% | 0.763 | 0.0278 |
| 4 | ev15_mixed | 45 | 37/8 | 6.85% | 4.93% | -5.84% | 0.760 | 0.0189 |
| 5 | d2_ev18 | 32 | 29/3 | 9.23% | 7.31% | -6.53% | 0.762 | 0.0142 |
| 6 | ev18_mixed | 39 | 32/7 | 5.13% | 3.21% | -10.06% | 0.759 | -0.0251 |
| 7 | ecmwf_only | 40 | 35/5 | 4.51% | 2.61% | -10.04% | 0.765 | -0.0290 |
| 8 | d2_only | 37 | 33/4 | 4.95% | 3.06% | -10.56% | 0.766 | -0.0324 |
| 9 | entry_70_80 | 45 | 37/8 | 3.66% | 1.75% | -11.97% | 0.758 | -0.0344 |
| 10 | d2_entry_72_85 | 35 | 31/4 | 4.30% | 2.41% | -11.86% | 0.770 | -0.0474 |
| 11 | entry_72_82 | 46 | 37/9 | 1.16% | -0.73% | -13.59% | 0.767 | -0.0629 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 14/2 | 6.31% | 4.43% | -17.00% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 50 | 46/4 | 9.18% | 0.05% | 0.747 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 57 | 51/6 | 6.44% | -2.45% | 0.748 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
