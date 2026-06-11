# Strategy Lab
Generated: 2026-06-11T16:31:46.725886+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 18
  - need >=30 post-activation resolved trades, have 1
  - need positive bootstrap lower bound, have -6.06%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 18 | 17/1 | 10.03% | 8.12% | -6.06% | 0.756 | -0.0040 |
| 2 | d2_ev15 | 18 | 17/1 | 10.03% | 8.12% | -6.06% | 0.756 | -0.0040 |
| 3 | d2_ecmwf_only | 18 | 17/1 | 10.03% | 8.12% | -6.06% | 0.756 | -0.0040 |
| 4 | ev15_mixed | 29 | 23/6 | 6.82% | 4.90% | -7.49% | 0.754 | -0.0192 |
| 5 | d2_ev18 | 16 | 15/1 | 9.72% | 7.80% | -9.08% | 0.754 | -0.0218 |
| 6 | ecmwf_only | 24 | 21/3 | 4.12% | 2.23% | -12.58% | 0.762 | -0.0737 |
| 7 | ev18_mixed | 23 | 18/5 | 4.75% | 2.83% | -14.11% | 0.751 | -0.0751 |
| 8 | d2_only | 21 | 19/2 | 4.62% | 2.72% | -12.85% | 0.762 | -0.0758 |
| 9 | entry_70_80 | 32 | 25/7 | 2.52% | 0.61% | -15.01% | 0.757 | -0.0824 |
| 10 | d2_entry_72_85 | 20 | 18/2 | 4.25% | 2.36% | -14.28% | 0.765 | -0.0864 |
| 11 | entry_72_82 | 31 | 24/7 | 0.68% | -1.21% | -15.51% | 0.763 | -0.1044 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1/0 | 15.80% | 13.89% | 15.80% | 0.760 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 34 | 32/2 | 9.58% | -0.28% | 0.736 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 41 | 37/4 | 6.56% | -3.16% | 0.740 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
