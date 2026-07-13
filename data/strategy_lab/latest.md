# Strategy Lab
Generated: 2026-07-13T15:14:38.034208+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 80
  - need post-activation ROI after drag >=3%, have 0.92%
  - need positive bootstrap lower bound, have -3.87%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 80 | 68/12 | 6.99% | 5.09% | -3.87% | 0.766 | 0.0374 |
| 2 | d2_ev15 | 80 | 68/12 | 6.99% | 5.09% | -3.87% | 0.766 | 0.0374 |
| 3 | d2_ecmwf_only | 80 | 68/12 | 6.99% | 5.09% | -3.87% | 0.766 | 0.0374 |
| 4 | d2_ev18 | 75 | 63/12 | 6.39% | 4.48% | -5.59% | 0.763 | 0.0252 |
| 5 | ev15_mixed | 91 | 74/17 | 5.36% | 3.46% | -5.04% | 0.765 | 0.0170 |
| 6 | d2_only | 83 | 70/13 | 3.98% | 2.09% | -8.07% | 0.768 | -0.0073 |
| 7 | ecmwf_only | 86 | 72/14 | 3.69% | 1.80% | -7.62% | 0.767 | -0.0087 |
| 8 | ev18_mixed | 82 | 66/16 | 3.71% | 1.80% | -7.97% | 0.762 | -0.0099 |
| 9 | d2_entry_72_85 | 74 | 63/11 | 3.61% | 1.73% | -8.90% | 0.775 | -0.0138 |
| 10 | entry_70_80 | 79 | 63/16 | 2.67% | 0.75% | -9.39% | 0.753 | -0.0254 |
| 11 | entry_72_82 | 75 | 60/15 | 0.99% | -0.91% | -11.74% | 0.765 | -0.0502 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 62 | 51/11 | 2.80% | 0.92% | -9.71% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 96 | 83/13 | 7.23% | 0.03% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 103 | 88/15 | 5.19% | -2.27% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
