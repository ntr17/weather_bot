# Strategy Lab
Generated: 2026-08-30T21:12:21.367616+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.75%
  - need post-activation ROI after drag >=3%, have -3.52%
  - need positive bootstrap lower bound, have -5.56%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 139 | 112/27 | 3.38% | 1.46% | -5.62% | 0.760 | -0.0051 |
| 2 | current_paper | 162 | 130/32 | 2.64% | 0.75% | -5.56% | 0.767 | -0.0120 |
| 3 | d2_ev15 | 162 | 130/32 | 2.64% | 0.75% | -5.56% | 0.767 | -0.0120 |
| 4 | d2_ecmwf_only | 162 | 130/32 | 2.64% | 0.75% | -5.56% | 0.767 | -0.0120 |
| 5 | ev15_mixed | 173 | 136/37 | 1.90% | 0.00% | -6.21% | 0.766 | -0.0217 |
| 6 | ev18_mixed | 146 | 115/31 | 1.65% | -0.26% | -7.10% | 0.759 | -0.0274 |
| 7 | d2_only | 165 | 132/33 | 0.92% | -0.96% | -7.82% | 0.768 | -0.0370 |
| 8 | ecmwf_only | 168 | 134/34 | 0.82% | -1.07% | -7.74% | 0.768 | -0.0378 |
| 9 | d2_entry_72_85 | 149 | 120/29 | 0.63% | -1.25% | -8.66% | 0.775 | -0.0428 |
| 10 | entry_70_80 | 142 | 110/32 | 0.56% | -1.36% | -9.22% | 0.752 | -0.0459 |
| 11 | entry_72_82 | 138 | 109/29 | 0.08% | -1.81% | -9.44% | 0.763 | -0.0511 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 144 | 113/31 | -1.64% | -3.52% | -10.47% | 0.768 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 178 | 145/33 | 3.45% | -2.07% | 0.762 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 185 | 150/35 | 2.18% | -3.50% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
