# Strategy Lab
Generated: 2026-07-31T19:57:08.061720+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 0.16%
  - need positive bootstrap lower bound, have -3.50%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 114 | 95/19 | 5.79% | 3.89% | -3.50% | 0.765 | 0.0267 |
| 2 | d2_ev15 | 114 | 95/19 | 5.79% | 3.89% | -3.50% | 0.765 | 0.0267 |
| 3 | d2_ecmwf_only | 114 | 95/19 | 5.79% | 3.89% | -3.50% | 0.765 | 0.0267 |
| 4 | d2_ev18 | 102 | 84/18 | 5.35% | 3.43% | -5.15% | 0.759 | 0.0163 |
| 5 | ev15_mixed | 125 | 101/24 | 4.56% | 2.65% | -4.25% | 0.764 | 0.0116 |
| 6 | d2_only | 117 | 97/20 | 3.40% | 1.51% | -6.67% | 0.766 | -0.0082 |
| 7 | ecmwf_only | 120 | 99/21 | 3.18% | 1.29% | -6.82% | 0.766 | -0.0110 |
| 8 | ev18_mixed | 109 | 87/22 | 3.15% | 1.24% | -7.14% | 0.758 | -0.0126 |
| 9 | d2_entry_72_85 | 104 | 87/17 | 3.15% | 1.27% | -7.43% | 0.773 | -0.0133 |
| 10 | entry_70_80 | 106 | 84/22 | 2.24% | 0.32% | -8.56% | 0.751 | -0.0268 |
| 11 | entry_72_82 | 102 | 82/20 | 1.34% | -0.56% | -9.36% | 0.764 | -0.0384 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 96 | 78/18 | 2.05% | 0.16% | -8.00% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 130 | 110/20 | 6.12% | -0.14% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 137 | 115/22 | 4.41% | -2.43% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
