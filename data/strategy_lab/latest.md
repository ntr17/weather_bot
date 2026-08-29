# Strategy Lab
Generated: 2026-08-29T20:58:46.317650+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.63%
  - need post-activation ROI after drag >=3%, have -3.74%
  - need positive bootstrap lower bound, have -5.70%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 138 | 111/27 | 3.24% | 1.33% | -5.89% | 0.760 | -0.0073 |
| 2 | current_paper | 161 | 129/32 | 2.52% | 0.63% | -5.70% | 0.767 | -0.0137 |
| 3 | d2_ev15 | 161 | 129/32 | 2.52% | 0.63% | -5.70% | 0.767 | -0.0137 |
| 4 | d2_ecmwf_only | 161 | 129/32 | 2.52% | 0.63% | -5.70% | 0.767 | -0.0137 |
| 5 | ev15_mixed | 172 | 135/37 | 1.78% | -0.11% | -6.64% | 0.766 | -0.0243 |
| 6 | ev18_mixed | 145 | 114/31 | 1.51% | -0.40% | -7.49% | 0.759 | -0.0302 |
| 7 | d2_only | 164 | 131/33 | 0.80% | -1.08% | -8.08% | 0.768 | -0.0391 |
| 8 | ecmwf_only | 167 | 133/34 | 0.70% | -1.18% | -7.97% | 0.768 | -0.0397 |
| 9 | d2_entry_72_85 | 148 | 119/29 | 0.49% | -1.38% | -8.99% | 0.775 | -0.0453 |
| 10 | entry_70_80 | 141 | 109/32 | 0.43% | -1.49% | -9.10% | 0.751 | -0.0467 |
| 11 | entry_72_82 | 137 | 108/29 | -0.05% | -1.95% | -9.73% | 0.763 | -0.0536 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 143 | 112/31 | -1.86% | -3.74% | -11.01% | 0.768 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 177 | 144/33 | 3.37% | -2.29% | 0.762 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 184 | 149/35 | 2.10% | -3.61% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
