# Strategy Lab
Generated: 2026-08-19T01:55:19.505037+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 1.46%
  - need post-activation ROI after drag >=3%, have -2.73%
  - need positive bootstrap lower bound, have -5.03%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 131 | 106/25 | 3.84% | 1.92% | -5.50% | 0.757 | -0.0001 |
| 2 | current_paper | 151 | 122/29 | 3.36% | 1.46% | -5.03% | 0.764 | -0.0030 |
| 3 | d2_ev15 | 151 | 122/29 | 3.36% | 1.46% | -5.03% | 0.764 | -0.0030 |
| 4 | d2_ecmwf_only | 151 | 122/29 | 3.36% | 1.46% | -5.03% | 0.764 | -0.0030 |
| 5 | ev15_mixed | 162 | 128/34 | 2.52% | 0.61% | -5.74% | 0.763 | -0.0140 |
| 6 | ev18_mixed | 138 | 109/29 | 2.03% | 0.11% | -6.89% | 0.757 | -0.0230 |
| 7 | ecmwf_only | 157 | 126/31 | 1.38% | -0.51% | -7.36% | 0.765 | -0.0309 |
| 8 | d2_only | 154 | 124/30 | 1.51% | -0.39% | -7.86% | 0.765 | -0.0314 |
| 9 | d2_entry_72_85 | 138 | 112/26 | 1.25% | -0.63% | -8.25% | 0.772 | -0.0352 |
| 10 | entry_70_80 | 137 | 106/31 | 0.56% | -1.36% | -8.99% | 0.751 | -0.0451 |
| 11 | entry_72_82 | 133 | 105/28 | 0.07% | -1.82% | -9.46% | 0.763 | -0.0513 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 133 | 105/28 | -0.85% | -2.73% | -9.87% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 167 | 137/30 | 4.07% | -1.50% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 174 | 142/32 | 2.71% | -3.25% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
