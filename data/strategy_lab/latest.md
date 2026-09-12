# Strategy Lab
Generated: 2026-09-12T04:42:19.394026+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.24%
  - need post-activation ROI after drag >=3%, have -3.97%
  - need positive bootstrap lower bound, have -5.86%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 150 | 120/30 | 2.68% | 0.77% | -6.20% | 0.760 | -0.0140 |
| 2 | current_paper | 174 | 139/35 | 2.14% | 0.24% | -5.86% | 0.768 | -0.0181 |
| 3 | d2_ev15 | 174 | 139/35 | 2.14% | 0.24% | -5.86% | 0.768 | -0.0181 |
| 4 | d2_ecmwf_only | 174 | 139/35 | 2.14% | 0.24% | -5.86% | 0.768 | -0.0181 |
| 5 | ev15_mixed | 185 | 145/40 | 1.46% | -0.43% | -6.35% | 0.767 | -0.0265 |
| 6 | ev18_mixed | 157 | 123/34 | 1.07% | -0.84% | -7.46% | 0.760 | -0.0345 |
| 7 | ecmwf_only | 180 | 143/37 | 0.44% | -1.45% | -7.85% | 0.768 | -0.0420 |
| 8 | d2_only | 177 | 141/36 | 0.53% | -1.36% | -8.14% | 0.768 | -0.0421 |
| 9 | d2_entry_72_85 | 161 | 129/32 | 0.21% | -1.66% | -8.62% | 0.775 | -0.0468 |
| 10 | entry_70_80 | 150 | 115/35 | -0.21% | -2.14% | -9.72% | 0.752 | -0.0554 |
| 11 | entry_72_82 | 149 | 117/32 | -0.39% | -2.29% | -9.77% | 0.764 | -0.0571 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 156 | 122/34 | -2.09% | -3.97% | -10.51% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 190 | 154/36 | 2.97% | -2.43% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 197 | 159/38 | 1.78% | -3.75% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
