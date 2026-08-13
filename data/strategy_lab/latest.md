# Strategy Lab
Generated: 2026-08-13T19:28:39.066292+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 0.10%
  - need positive bootstrap lower bound, have -3.16%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 123 | 102/21 | 5.68% | 3.76% | -3.96% | 0.758 | 0.0237 |
| 2 | current_paper | 140 | 116/24 | 5.28% | 3.38% | -3.16% | 0.764 | 0.0227 |
| 3 | d2_ev15 | 140 | 116/24 | 5.28% | 3.38% | -3.16% | 0.764 | 0.0227 |
| 4 | d2_ecmwf_only | 140 | 116/24 | 5.28% | 3.38% | -3.16% | 0.764 | 0.0227 |
| 5 | ev15_mixed | 151 | 122/29 | 4.23% | 2.33% | -4.22% | 0.764 | 0.0085 |
| 6 | ev18_mixed | 130 | 105/25 | 3.72% | 1.80% | -5.24% | 0.757 | -0.0003 |
| 7 | d2_only | 143 | 118/25 | 3.20% | 1.31% | -6.33% | 0.765 | -0.0091 |
| 8 | ecmwf_only | 146 | 120/26 | 3.02% | 1.13% | -5.98% | 0.765 | -0.0096 |
| 9 | d2_entry_72_85 | 128 | 106/22 | 2.59% | 0.71% | -7.51% | 0.772 | -0.0192 |
| 10 | entry_70_80 | 127 | 101/26 | 2.36% | 0.43% | -7.52% | 0.751 | -0.0220 |
| 11 | entry_72_82 | 124 | 100/24 | 1.41% | -0.49% | -8.49% | 0.763 | -0.0346 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 122 | 99/23 | 1.99% | 0.10% | -7.15% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 156 | 131/25 | 5.55% | -0.20% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 163 | 136/27 | 4.03% | -2.16% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
