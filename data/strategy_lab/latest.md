# Strategy Lab
Generated: 2026-06-16T11:37:29.639509+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 31
  - need >=30 post-activation resolved trades, have 13
  - need post-activation ROI after drag >=3%, have 0.25%
  - need positive bootstrap lower bound, have -6.07%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 31 | 28/3 | 9.07% | 7.16% | -6.07% | 0.761 | 0.0124 |
| 2 | d2_ev15 | 31 | 28/3 | 9.07% | 7.16% | -6.07% | 0.761 | 0.0124 |
| 3 | d2_ecmwf_only | 31 | 28/3 | 9.07% | 7.16% | -6.07% | 0.761 | 0.0124 |
| 4 | ev15_mixed | 42 | 34/8 | 6.39% | 4.47% | -7.12% | 0.759 | 0.0038 |
| 5 | d2_ev18 | 29 | 26/3 | 8.69% | 6.77% | -8.37% | 0.760 | -0.0036 |
| 6 | ev18_mixed | 36 | 29/7 | 4.50% | 2.58% | -10.91% | 0.757 | -0.0404 |
| 7 | entry_70_80 | 43 | 35/8 | 3.30% | 1.39% | -12.36% | 0.758 | -0.0434 |
| 8 | ecmwf_only | 37 | 32/5 | 4.00% | 2.10% | -11.29% | 0.764 | -0.0445 |
| 9 | d2_only | 34 | 30/4 | 4.42% | 2.53% | -11.79% | 0.765 | -0.0480 |
| 10 | d2_entry_72_85 | 32 | 28/4 | 3.72% | 1.83% | -12.74% | 0.769 | -0.0623 |
| 11 | entry_72_82 | 43 | 34/9 | 0.58% | -1.32% | -14.67% | 0.766 | -0.0785 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 11/2 | 2.14% | 0.25% | -25.80% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 47 | 43/4 | 8.95% | -0.30% | 0.745 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 54 | 48/6 | 6.20% | -2.55% | 0.747 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
