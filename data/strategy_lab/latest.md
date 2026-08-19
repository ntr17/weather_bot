# Strategy Lab
Generated: 2026-08-19T13:13:00.475650+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 1.05%
  - need post-activation ROI after drag >=3%, have -3.33%
  - need positive bootstrap lower bound, have -5.44%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 132 | 107/25 | 3.91% | 2.00% | -5.48% | 0.758 | 0.0008 |
| 2 | current_paper | 153 | 123/30 | 2.95% | 1.05% | -5.44% | 0.765 | -0.0085 |
| 3 | d2_ev15 | 153 | 123/30 | 2.95% | 1.05% | -5.44% | 0.765 | -0.0085 |
| 4 | d2_ecmwf_only | 153 | 123/30 | 2.95% | 1.05% | -5.44% | 0.765 | -0.0085 |
| 5 | ev15_mixed | 164 | 129/35 | 2.15% | 0.25% | -6.43% | 0.764 | -0.0200 |
| 6 | ev18_mixed | 139 | 110/29 | 2.11% | 0.19% | -7.07% | 0.758 | -0.0228 |
| 7 | d2_only | 156 | 125/31 | 1.14% | -0.75% | -8.12% | 0.766 | -0.0359 |
| 8 | ecmwf_only | 159 | 127/32 | 1.03% | -0.86% | -7.90% | 0.766 | -0.0362 |
| 9 | d2_entry_72_85 | 140 | 113/27 | 0.85% | -1.03% | -8.65% | 0.773 | -0.0406 |
| 10 | entry_70_80 | 137 | 106/31 | 0.56% | -1.36% | -8.99% | 0.751 | -0.0451 |
| 11 | entry_72_82 | 133 | 105/28 | 0.07% | -1.82% | -9.46% | 0.763 | -0.0513 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 135 | 106/29 | -1.44% | -3.33% | -10.55% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 169 | 138/31 | 3.75% | -1.79% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 176 | 143/33 | 2.42% | -3.39% | 0.760 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
