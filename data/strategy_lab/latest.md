# Strategy Lab
Generated: 2026-07-03T04:12:08.938168+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 57
  - need post-activation ROI after drag >=3%, have -3.49%
  - need positive bootstrap lower bound, have -6.02%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 57 | 48/9 | 6.36% | 4.47% | -6.02% | 0.770 | 0.0236 |
| 2 | d2_ev15 | 57 | 48/9 | 6.36% | 4.47% | -6.02% | 0.770 | 0.0236 |
| 3 | d2_ecmwf_only | 57 | 48/9 | 6.36% | 4.47% | -6.02% | 0.770 | 0.0236 |
| 4 | d2_ev18 | 54 | 45/9 | 5.78% | 3.88% | -7.82% | 0.769 | 0.0114 |
| 5 | ev15_mixed | 68 | 54/14 | 4.55% | 2.65% | -7.24% | 0.767 | 0.0012 |
| 6 | d2_only | 60 | 50/10 | 2.91% | 1.02% | -10.13% | 0.772 | -0.0253 |
| 7 | ecmwf_only | 63 | 52/11 | 2.63% | 0.74% | -10.11% | 0.771 | -0.0280 |
| 8 | ev18_mixed | 61 | 48/13 | 2.66% | 0.75% | -10.45% | 0.766 | -0.0291 |
| 9 | entry_70_80 | 62 | 49/13 | 2.15% | 0.24% | -11.86% | 0.760 | -0.0391 |
| 10 | d2_entry_72_85 | 57 | 47/10 | 1.97% | 0.10% | -12.24% | 0.776 | -0.0418 |
| 11 | entry_72_82 | 63 | 49/14 | -0.20% | -2.09% | -13.78% | 0.768 | -0.0691 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 39 | 31/8 | -1.63% | -3.49% | -18.34% | 0.776 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 73 | 63/10 | 7.10% | -0.68% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 80 | 68/12 | 4.86% | -3.78% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
