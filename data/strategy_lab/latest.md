# Strategy Lab
Generated: 2026-08-17T07:18:59.365953+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.92%
  - need post-activation ROI after drag >=3%, have -0.45%
  - need positive bootstrap lower bound, have -3.24%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 148 | 122/26 | 4.82% | 2.92% | -3.24% | 0.765 | 0.0179 |
| 2 | d2_ev15 | 148 | 122/26 | 4.82% | 2.92% | -3.24% | 0.765 | 0.0179 |
| 3 | d2_ecmwf_only | 148 | 122/26 | 4.82% | 2.92% | -3.24% | 0.765 | 0.0179 |
| 4 | d2_ev18 | 129 | 106/23 | 4.96% | 3.04% | -4.56% | 0.758 | 0.0144 |
| 5 | ev15_mixed | 159 | 128/31 | 3.85% | 1.94% | -4.44% | 0.764 | 0.0039 |
| 6 | ev18_mixed | 136 | 109/27 | 3.09% | 1.17% | -5.93% | 0.757 | -0.0091 |
| 7 | ecmwf_only | 154 | 126/28 | 2.68% | 0.79% | -6.08% | 0.765 | -0.0134 |
| 8 | d2_only | 151 | 124/27 | 2.85% | 0.96% | -6.62% | 0.765 | -0.0136 |
| 9 | d2_entry_72_85 | 135 | 112/23 | 2.71% | 0.84% | -6.64% | 0.772 | -0.0148 |
| 10 | entry_70_80 | 134 | 106/28 | 1.97% | 0.05% | -7.68% | 0.751 | -0.0264 |
| 11 | entry_72_82 | 130 | 105/25 | 1.53% | -0.37% | -8.55% | 0.763 | -0.0336 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 130 | 105/25 | 1.44% | -0.45% | -7.53% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 164 | 137/27 | 5.15% | -0.34% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 171 | 142/29 | 3.70% | -2.14% | 0.760 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
