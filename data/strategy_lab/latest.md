# Strategy Lab
Generated: 2026-06-19T20:06:01.988915+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 38
  - need >=30 post-activation resolved trades, have 20
  - need post-activation ROI after drag >=3%, have 0.90%
  - need positive bootstrap lower bound, have -5.15%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 38 | 34/4 | 8.72% | 6.81% | -5.15% | 0.767 | 0.0261 |
| 2 | d2_ev15 | 38 | 34/4 | 8.72% | 6.81% | -5.15% | 0.767 | 0.0261 |
| 3 | d2_ecmwf_only | 38 | 34/4 | 8.72% | 6.81% | -5.15% | 0.767 | 0.0261 |
| 4 | ev15_mixed | 49 | 40/9 | 6.24% | 4.33% | -6.99% | 0.763 | 0.0168 |
| 5 | d2_ev18 | 36 | 32/4 | 8.33% | 6.42% | -6.91% | 0.766 | 0.0120 |
| 6 | ev18_mixed | 43 | 35/8 | 4.46% | 2.55% | -10.58% | 0.763 | -0.0255 |
| 7 | ecmwf_only | 44 | 38/6 | 3.99% | 2.10% | -10.26% | 0.769 | -0.0269 |
| 8 | d2_only | 41 | 36/5 | 4.40% | 2.50% | -10.46% | 0.769 | -0.0296 |
| 9 | entry_70_80 | 47 | 38/9 | 2.90% | 0.99% | -12.44% | 0.759 | -0.0396 |
| 10 | d2_entry_72_85 | 39 | 34/5 | 3.73% | 1.85% | -12.15% | 0.773 | -0.0460 |
| 11 | entry_72_82 | 49 | 39/10 | 0.61% | -1.28% | -13.92% | 0.769 | -0.0635 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 20 | 17/3 | 2.77% | 0.90% | -17.78% | 0.775 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 54 | 49/5 | 8.69% | 0.02% | 0.751 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 61 | 54/7 | 6.06% | -2.68% | 0.752 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
