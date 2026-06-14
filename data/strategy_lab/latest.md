# Strategy Lab
Generated: 2026-06-14T20:00:34.956640+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 25
  - need >=30 post-activation resolved trades, have 7
  - need positive bootstrap lower bound, have -6.03%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 25 | 23/2 | 9.89% | 7.98% | -6.03% | 0.763 | 0.0087 |
| 2 | d2_ev15 | 25 | 23/2 | 9.89% | 7.98% | -6.03% | 0.763 | 0.0087 |
| 3 | d2_ecmwf_only | 25 | 23/2 | 9.89% | 7.98% | -6.03% | 0.763 | 0.0087 |
| 4 | d2_ev18 | 23 | 21/2 | 9.59% | 7.67% | -7.43% | 0.762 | -0.0033 |
| 5 | ev15_mixed | 36 | 29/7 | 6.91% | 5.00% | -7.60% | 0.759 | -0.0046 |
| 6 | entry_70_80 | 37 | 30/7 | 3.63% | 1.72% | -12.06% | 0.758 | -0.0510 |
| 7 | ev18_mixed | 30 | 24/6 | 5.03% | 3.11% | -12.22% | 0.758 | -0.0517 |
| 8 | ecmwf_only | 31 | 27/4 | 4.38% | 2.49% | -11.09% | 0.766 | -0.0519 |
| 9 | d2_only | 28 | 25/3 | 4.86% | 2.97% | -11.72% | 0.767 | -0.0553 |
| 10 | d2_entry_72_85 | 26 | 23/3 | 4.14% | 2.25% | -13.43% | 0.772 | -0.0725 |
| 11 | entry_72_82 | 37 | 29/8 | 0.77% | -1.12% | -15.52% | 0.768 | -0.0915 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 6/1 | 6.69% | 4.82% | -30.40% | 0.776 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 41 | 38/3 | 9.45% | 0.13% | 0.743 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 48 | 43/5 | 6.55% | -2.97% | 0.746 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
