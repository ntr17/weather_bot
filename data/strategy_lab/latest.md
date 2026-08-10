# Strategy Lab
Generated: 2026-08-10T19:21:02.602263+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.83%
  - need post-activation ROI after drag >=3%, have -1.00%
  - need positive bootstrap lower bound, have -4.21%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 117 | 96/21 | 5.06% | 3.15% | -4.79% | 0.759 | 0.0147 |
| 2 | current_paper | 134 | 110/24 | 4.73% | 2.83% | -4.21% | 0.766 | 0.0136 |
| 3 | d2_ev15 | 134 | 110/24 | 4.73% | 2.83% | -4.21% | 0.766 | 0.0136 |
| 4 | d2_ecmwf_only | 134 | 110/24 | 4.73% | 2.83% | -4.21% | 0.766 | 0.0136 |
| 5 | ev15_mixed | 145 | 116/29 | 3.70% | 1.80% | -5.05% | 0.765 | 0.0003 |
| 6 | ev18_mixed | 124 | 99/25 | 3.06% | 1.15% | -6.37% | 0.758 | -0.0108 |
| 7 | d2_only | 137 | 112/25 | 2.64% | 0.75% | -7.05% | 0.766 | -0.0172 |
| 8 | ecmwf_only | 140 | 114/26 | 2.47% | 0.57% | -6.77% | 0.766 | -0.0180 |
| 9 | d2_entry_72_85 | 123 | 101/22 | 2.14% | 0.27% | -8.21% | 0.773 | -0.0260 |
| 10 | entry_70_80 | 121 | 95/26 | 1.73% | -0.19% | -8.72% | 0.751 | -0.0324 |
| 11 | entry_72_82 | 119 | 95/24 | 0.93% | -0.96% | -9.24% | 0.764 | -0.0419 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 116 | 93/23 | 0.88% | -1.00% | -8.87% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 150 | 125/25 | 5.21% | -0.54% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 157 | 130/27 | 3.68% | -2.48% | 0.760 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
