# Strategy Lab
Generated: 2026-07-04T04:05:21.862584+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 59
  - need post-activation ROI after drag >=3%, have -1.92%
  - need positive bootstrap lower bound, have -5.45%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 59 | 50/9 | 6.76% | 4.86% | -5.45% | 0.770 | 0.0295 |
| 2 | d2_ev15 | 59 | 50/9 | 6.76% | 4.86% | -5.45% | 0.770 | 0.0295 |
| 3 | d2_ecmwf_only | 59 | 50/9 | 6.76% | 4.86% | -5.45% | 0.770 | 0.0295 |
| 4 | d2_ev18 | 56 | 47/9 | 6.22% | 4.32% | -7.11% | 0.769 | 0.0183 |
| 5 | ev15_mixed | 70 | 56/14 | 4.92% | 3.01% | -6.32% | 0.768 | 0.0080 |
| 6 | d2_only | 62 | 52/10 | 3.31% | 1.42% | -9.49% | 0.772 | -0.0190 |
| 7 | ev18_mixed | 63 | 50/13 | 3.13% | 1.22% | -10.03% | 0.766 | -0.0229 |
| 8 | ecmwf_only | 65 | 54/11 | 3.02% | 1.13% | -9.87% | 0.771 | -0.0232 |
| 9 | entry_70_80 | 63 | 50/13 | 2.42% | 0.51% | -11.50% | 0.759 | -0.0352 |
| 10 | d2_entry_72_85 | 58 | 48/10 | 2.12% | 0.24% | -11.59% | 0.777 | -0.0382 |
| 11 | entry_72_82 | 63 | 49/14 | -0.20% | -2.09% | -13.78% | 0.768 | -0.0691 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 41 | 33/8 | -0.06% | -1.92% | -16.19% | 0.776 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 75 | 65/10 | 7.31% | -0.42% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 82 | 70/12 | 5.07% | -3.33% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
