# Strategy Lab
Generated: 2026-06-17T20:32:20.259083+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 33
  - need >=30 post-activation resolved trades, have 15
  - need positive bootstrap lower bound, have -4.95%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 33 | 30/3 | 9.51% | 7.60% | -4.95% | 0.762 | 0.0247 |
| 2 | d2_ev15 | 33 | 30/3 | 9.51% | 7.60% | -4.95% | 0.762 | 0.0247 |
| 3 | d2_ecmwf_only | 33 | 30/3 | 9.51% | 7.60% | -4.95% | 0.762 | 0.0247 |
| 4 | ev15_mixed | 44 | 36/8 | 6.80% | 4.88% | -6.49% | 0.759 | 0.0141 |
| 5 | d2_ev18 | 31 | 28/3 | 9.19% | 7.27% | -7.01% | 0.761 | 0.0102 |
| 6 | ev18_mixed | 38 | 31/7 | 5.05% | 3.13% | -10.56% | 0.758 | -0.0297 |
| 7 | ecmwf_only | 39 | 34/5 | 4.44% | 2.54% | -10.32% | 0.765 | -0.0327 |
| 8 | entry_70_80 | 44 | 36/8 | 3.59% | 1.68% | -11.67% | 0.757 | -0.0360 |
| 9 | d2_only | 36 | 32/4 | 4.89% | 2.99% | -11.04% | 0.765 | -0.0367 |
| 10 | d2_entry_72_85 | 34 | 30/4 | 4.22% | 2.33% | -12.12% | 0.769 | -0.0511 |
| 11 | entry_72_82 | 45 | 36/9 | 1.07% | -0.82% | -13.84% | 0.766 | -0.0666 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 15 | 13/2 | 5.91% | 4.02% | -18.39% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 49 | 45/4 | 9.17% | 0.23% | 0.746 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 56 | 50/6 | 6.42% | -2.44% | 0.748 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
