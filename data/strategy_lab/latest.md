# Strategy Lab
Generated: 2026-08-19T18:56:17.752575+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.58%
  - need post-activation ROI after drag >=3%, have -4.05%
  - need positive bootstrap lower bound, have -6.00%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 133 | 107/26 | 3.36% | 1.45% | -6.12% | 0.759 | -0.0069 |
| 2 | current_paper | 154 | 123/31 | 2.47% | 0.58% | -6.00% | 0.766 | -0.0152 |
| 3 | d2_ev15 | 154 | 123/31 | 2.47% | 0.58% | -6.00% | 0.766 | -0.0152 |
| 4 | d2_ecmwf_only | 154 | 123/31 | 2.47% | 0.58% | -6.00% | 0.766 | -0.0152 |
| 5 | ev15_mixed | 165 | 129/36 | 1.72% | -0.18% | -6.90% | 0.765 | -0.0260 |
| 6 | ev18_mixed | 140 | 110/30 | 1.59% | -0.33% | -7.30% | 0.758 | -0.0289 |
| 7 | ecmwf_only | 160 | 127/33 | 0.61% | -1.28% | -7.95% | 0.766 | -0.0406 |
| 8 | d2_only | 157 | 125/32 | 0.71% | -1.18% | -8.69% | 0.766 | -0.0422 |
| 9 | entry_70_80 | 137 | 106/31 | 0.56% | -1.36% | -8.99% | 0.751 | -0.0451 |
| 10 | d2_entry_72_85 | 141 | 113/28 | 0.38% | -1.50% | -9.25% | 0.773 | -0.0474 |
| 11 | entry_72_82 | 133 | 105/28 | 0.07% | -1.82% | -9.46% | 0.763 | -0.0513 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 136 | 106/30 | -2.17% | -4.05% | -11.24% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 170 | 138/32 | 3.40% | -2.38% | 0.761 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 177 | 143/34 | 2.10% | -3.70% | 0.761 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
