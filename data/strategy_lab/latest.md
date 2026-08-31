# Strategy Lab
Generated: 2026-08-31T22:54:46.629895+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.85%
  - need post-activation ROI after drag >=3%, have -3.34%
  - need positive bootstrap lower bound, have -5.49%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 140 | 113/27 | 3.49% | 1.58% | -5.31% | 0.760 | -0.0028 |
| 2 | current_paper | 163 | 131/32 | 2.74% | 0.85% | -5.49% | 0.767 | -0.0107 |
| 3 | d2_ev15 | 163 | 131/32 | 2.74% | 0.85% | -5.49% | 0.767 | -0.0107 |
| 4 | d2_ecmwf_only | 163 | 131/32 | 2.74% | 0.85% | -5.49% | 0.767 | -0.0107 |
| 5 | ev15_mixed | 174 | 137/37 | 1.99% | 0.09% | -6.17% | 0.767 | -0.0207 |
| 6 | ev18_mixed | 147 | 116/31 | 1.77% | -0.14% | -7.06% | 0.759 | -0.0261 |
| 7 | d2_only | 166 | 133/33 | 1.02% | -0.86% | -7.65% | 0.768 | -0.0354 |
| 8 | ecmwf_only | 169 | 135/34 | 0.92% | -0.97% | -7.47% | 0.768 | -0.0358 |
| 9 | d2_entry_72_85 | 150 | 121/29 | 0.73% | -1.14% | -8.25% | 0.775 | -0.0403 |
| 10 | entry_70_80 | 143 | 111/32 | 0.67% | -1.25% | -9.07% | 0.752 | -0.0442 |
| 11 | entry_72_82 | 139 | 110/29 | 0.20% | -1.69% | -9.33% | 0.764 | -0.0495 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 145 | 114/31 | -1.46% | -3.34% | -9.99% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 179 | 146/33 | 3.52% | -2.00% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 186 | 151/35 | 2.24% | -3.58% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
