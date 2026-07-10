# Strategy Lab
Generated: 2026-07-10T19:54:25.176348+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 72
  - need post-activation ROI after drag >=3%, have 2.22%
  - need positive bootstrap lower bound, have -3.63%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 72 | 62/10 | 7.76% | 5.86% | -3.63% | 0.768 | 0.0459 |
| 2 | d2_ev15 | 72 | 62/10 | 7.76% | 5.86% | -3.63% | 0.768 | 0.0459 |
| 3 | d2_ecmwf_only | 72 | 62/10 | 7.76% | 5.86% | -3.63% | 0.768 | 0.0459 |
| 4 | d2_ev18 | 67 | 57/10 | 7.20% | 5.29% | -5.31% | 0.765 | 0.0343 |
| 5 | ev15_mixed | 83 | 68/15 | 5.94% | 4.04% | -4.38% | 0.766 | 0.0251 |
| 6 | d2_only | 75 | 64/11 | 4.50% | 2.62% | -7.56% | 0.770 | -0.0003 |
| 7 | ev18_mixed | 74 | 60/14 | 4.31% | 2.40% | -7.85% | 0.763 | -0.0035 |
| 8 | ecmwf_only | 78 | 66/12 | 4.18% | 2.29% | -7.77% | 0.769 | -0.0043 |
| 9 | entry_70_80 | 73 | 59/14 | 3.34% | 1.43% | -9.65% | 0.756 | -0.0195 |
| 10 | d2_entry_72_85 | 69 | 58/11 | 2.94% | 1.07% | -9.78% | 0.775 | -0.0235 |
| 11 | entry_72_82 | 72 | 57/15 | 0.52% | -1.38% | -12.28% | 0.766 | -0.0568 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 54 | 45/9 | 4.10% | 2.22% | -8.93% | 0.772 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 88 | 77/11 | 7.79% | 0.44% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 95 | 82/13 | 5.62% | -2.16% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
