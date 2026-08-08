# Strategy Lab
Generated: 2026-08-08T02:24:14.198927+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.63%
  - need post-activation ROI after drag >=3%, have -1.68%
  - need positive bootstrap lower bound, have -4.69%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 109 | 89/20 | 4.94% | 3.03% | -5.41% | 0.758 | 0.0114 |
| 2 | current_paper | 125 | 102/23 | 4.53% | 2.63% | -4.69% | 0.765 | 0.0099 |
| 3 | d2_ev15 | 125 | 102/23 | 4.53% | 2.63% | -4.69% | 0.765 | 0.0099 |
| 4 | d2_ecmwf_only | 125 | 102/23 | 4.53% | 2.63% | -4.69% | 0.765 | 0.0099 |
| 5 | ev15_mixed | 136 | 108/28 | 3.48% | 1.57% | -5.75% | 0.764 | -0.0044 |
| 6 | ev18_mixed | 116 | 92/24 | 2.85% | 0.94% | -7.17% | 0.758 | -0.0157 |
| 7 | d2_only | 128 | 104/24 | 2.36% | 0.47% | -7.84% | 0.766 | -0.0227 |
| 8 | ecmwf_only | 131 | 106/25 | 2.19% | 0.30% | -7.67% | 0.765 | -0.0238 |
| 9 | d2_entry_72_85 | 114 | 93/21 | 1.82% | -0.06% | -8.69% | 0.773 | -0.0310 |
| 10 | entry_70_80 | 114 | 89/25 | 1.54% | -0.38% | -9.07% | 0.751 | -0.0355 |
| 11 | entry_72_82 | 111 | 88/23 | 0.65% | -1.25% | -9.80% | 0.764 | -0.0468 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 107 | 85/22 | 0.21% | -1.68% | -9.84% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 141 | 117/24 | 5.14% | -0.93% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 148 | 122/26 | 3.58% | -2.97% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
