# Strategy Lab
Generated: 2026-08-05T09:09:42.449089+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.17%
  - need post-activation ROI after drag >=3%, have -2.63%
  - need positive bootstrap lower bound, have -5.30%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 107 | 87/20 | 4.52% | 2.61% | -5.84% | 0.759 | 0.0057 |
| 2 | current_paper | 122 | 99/23 | 4.07% | 2.17% | -5.30% | 0.765 | 0.0032 |
| 3 | d2_ev15 | 122 | 99/23 | 4.07% | 2.17% | -5.30% | 0.765 | 0.0032 |
| 4 | d2_ecmwf_only | 122 | 99/23 | 4.07% | 2.17% | -5.30% | 0.765 | 0.0032 |
| 5 | ev15_mixed | 133 | 105/28 | 3.04% | 1.14% | -6.17% | 0.764 | -0.0102 |
| 6 | ev18_mixed | 114 | 90/24 | 2.43% | 0.51% | -7.80% | 0.758 | -0.0222 |
| 7 | d2_only | 125 | 101/24 | 1.90% | 0.01% | -8.31% | 0.766 | -0.0290 |
| 8 | ecmwf_only | 128 | 103/25 | 1.74% | -0.15% | -8.09% | 0.766 | -0.0298 |
| 9 | d2_entry_72_85 | 112 | 91/21 | 1.53% | -0.35% | -9.08% | 0.773 | -0.0353 |
| 10 | entry_70_80 | 112 | 87/25 | 1.15% | -0.77% | -9.56% | 0.751 | -0.0412 |
| 11 | entry_72_82 | 109 | 86/23 | 0.34% | -1.55% | -9.97% | 0.764 | -0.0504 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 104 | 82/22 | -0.74% | -2.63% | -10.85% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 138 | 114/24 | 4.85% | -1.45% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 145 | 119/26 | 3.29% | -3.32% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
