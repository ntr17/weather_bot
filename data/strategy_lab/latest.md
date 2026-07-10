# Strategy Lab
Generated: 2026-07-10T15:04:52.472785+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 71
  - need positive bootstrap lower bound, have -2.48%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 71 | 62/9 | 8.55% | 6.66% | -2.48% | 0.769 | 0.0579 |
| 2 | d2_ev15 | 71 | 62/9 | 8.55% | 6.66% | -2.48% | 0.769 | 0.0579 |
| 3 | d2_ecmwf_only | 71 | 62/9 | 8.55% | 6.66% | -2.48% | 0.769 | 0.0579 |
| 4 | d2_ev18 | 66 | 57/9 | 8.07% | 6.17% | -4.00% | 0.765 | 0.0477 |
| 5 | ev15_mixed | 82 | 68/14 | 6.63% | 4.73% | -4.14% | 0.766 | 0.0328 |
| 6 | d2_only | 74 | 64/10 | 5.20% | 3.31% | -6.72% | 0.770 | 0.0096 |
| 7 | ev18_mixed | 73 | 60/13 | 5.12% | 3.21% | -7.02% | 0.763 | 0.0075 |
| 8 | ecmwf_only | 77 | 66/11 | 4.85% | 2.96% | -6.89% | 0.770 | 0.0055 |
| 9 | entry_70_80 | 72 | 59/13 | 4.02% | 2.11% | -8.62% | 0.756 | -0.0091 |
| 10 | d2_entry_72_85 | 68 | 58/10 | 3.68% | 1.80% | -8.87% | 0.776 | -0.0131 |
| 11 | entry_72_82 | 71 | 57/14 | 1.20% | -0.69% | -11.69% | 0.766 | -0.0478 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 53 | 45/8 | 6.06% | 4.19% | -7.11% | 0.772 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 87 | 77/10 | 8.30% | 0.95% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 94 | 82/12 | 6.08% | -1.57% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
