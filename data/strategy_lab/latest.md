# Strategy Lab
Generated: 2026-07-09T09:59:24.423209+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 70
  - need positive bootstrap lower bound, have -2.90%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 70 | 61/9 | 8.37% | 6.47% | -2.90% | 0.769 | 0.0546 |
| 2 | d2_ev15 | 70 | 61/9 | 8.37% | 6.47% | -2.90% | 0.769 | 0.0546 |
| 3 | d2_ecmwf_only | 70 | 61/9 | 8.37% | 6.47% | -2.90% | 0.769 | 0.0546 |
| 4 | d2_ev18 | 65 | 56/9 | 7.86% | 5.96% | -4.74% | 0.765 | 0.0430 |
| 5 | ev15_mixed | 81 | 67/14 | 6.46% | 4.55% | -4.05% | 0.767 | 0.0313 |
| 6 | d2_only | 73 | 63/10 | 5.01% | 3.12% | -6.99% | 0.770 | 0.0067 |
| 7 | ecmwf_only | 76 | 65/11 | 4.66% | 2.78% | -6.79% | 0.770 | 0.0040 |
| 8 | ev18_mixed | 72 | 59/13 | 4.90% | 2.99% | -7.46% | 0.763 | 0.0038 |
| 9 | entry_70_80 | 71 | 58/13 | 3.83% | 1.91% | -8.98% | 0.756 | -0.0123 |
| 10 | d2_entry_72_85 | 67 | 57/10 | 3.46% | 1.59% | -9.47% | 0.776 | -0.0172 |
| 11 | entry_72_82 | 70 | 56/14 | 0.98% | -0.91% | -12.02% | 0.766 | -0.0512 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 52 | 44/8 | 5.53% | 3.67% | -7.90% | 0.773 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 86 | 76/10 | 8.19% | 0.84% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 93 | 81/12 | 5.97% | -1.80% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
