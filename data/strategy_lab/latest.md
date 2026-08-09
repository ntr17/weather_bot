# Strategy Lab
Generated: 2026-08-09T07:25:51.304212+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.86%
  - need post-activation ROI after drag >=3%, have -1.21%
  - need positive bootstrap lower bound, have -4.28%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 111 | 91/20 | 5.19% | 3.28% | -4.66% | 0.759 | 0.0165 |
| 2 | current_paper | 127 | 104/23 | 4.75% | 2.86% | -4.28% | 0.765 | 0.0136 |
| 3 | d2_ev15 | 127 | 104/23 | 4.75% | 2.86% | -4.28% | 0.765 | 0.0136 |
| 4 | d2_ecmwf_only | 127 | 104/23 | 4.75% | 2.86% | -4.28% | 0.765 | 0.0136 |
| 5 | ev15_mixed | 138 | 110/28 | 3.69% | 1.79% | -5.24% | 0.764 | -0.0004 |
| 6 | ev18_mixed | 118 | 94/24 | 3.12% | 1.20% | -6.83% | 0.758 | -0.0119 |
| 7 | ecmwf_only | 133 | 108/25 | 2.41% | 0.52% | -6.61% | 0.766 | -0.0179 |
| 8 | d2_only | 130 | 106/24 | 2.59% | 0.70% | -7.68% | 0.766 | -0.0199 |
| 9 | d2_entry_72_85 | 116 | 95/21 | 2.07% | 0.19% | -8.32% | 0.773 | -0.0272 |
| 10 | entry_70_80 | 116 | 91/25 | 1.79% | -0.13% | -8.70% | 0.751 | -0.0318 |
| 11 | entry_72_82 | 113 | 90/23 | 0.91% | -0.98% | -9.54% | 0.764 | -0.0432 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 109 | 87/22 | 0.68% | -1.21% | -9.12% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 143 | 119/24 | 5.28% | -0.69% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 150 | 124/26 | 3.72% | -2.53% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
