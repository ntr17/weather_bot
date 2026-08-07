# Strategy Lab
Generated: 2026-08-07T07:45:36.695469+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.54%
  - need post-activation ROI after drag >=3%, have -1.88%
  - need positive bootstrap lower bound, have -4.57%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 109 | 89/20 | 4.94% | 3.03% | -5.41% | 0.758 | 0.0114 |
| 2 | current_paper | 124 | 101/23 | 4.44% | 2.54% | -4.57% | 0.764 | 0.0094 |
| 3 | d2_ev15 | 124 | 101/23 | 4.44% | 2.54% | -4.57% | 0.764 | 0.0094 |
| 4 | d2_ecmwf_only | 124 | 101/23 | 4.44% | 2.54% | -4.57% | 0.764 | 0.0094 |
| 5 | ev15_mixed | 135 | 107/28 | 3.39% | 1.48% | -5.67% | 0.763 | -0.0050 |
| 6 | ev18_mixed | 116 | 92/24 | 2.85% | 0.94% | -7.17% | 0.758 | -0.0157 |
| 7 | d2_only | 127 | 103/24 | 2.26% | 0.37% | -7.29% | 0.765 | -0.0218 |
| 8 | ecmwf_only | 130 | 105/25 | 2.10% | 0.20% | -7.74% | 0.765 | -0.0251 |
| 9 | d2_entry_72_85 | 113 | 92/21 | 1.71% | -0.17% | -8.65% | 0.773 | -0.0320 |
| 10 | entry_70_80 | 114 | 89/25 | 1.54% | -0.38% | -9.07% | 0.751 | -0.0355 |
| 11 | entry_72_82 | 110 | 87/23 | 0.53% | -1.36% | -9.87% | 0.763 | -0.0481 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 106 | 84/22 | 0.01% | -1.88% | -10.04% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 140 | 116/24 | 5.09% | -1.22% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 147 | 121/26 | 3.52% | -2.90% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
