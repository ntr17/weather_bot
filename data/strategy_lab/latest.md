# Strategy Lab
Generated: 2026-09-04T04:40:54.283732+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.67%
  - need post-activation ROI after drag >=3%, have -3.51%
  - need positive bootstrap lower bound, have -5.35%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 144 | 116/28 | 3.26% | 1.35% | -5.45% | 0.760 | -0.0056 |
| 2 | current_paper | 167 | 134/33 | 2.56% | 0.67% | -5.35% | 0.768 | -0.0120 |
| 3 | d2_ev15 | 167 | 134/33 | 2.56% | 0.67% | -5.35% | 0.768 | -0.0120 |
| 4 | d2_ecmwf_only | 167 | 134/33 | 2.56% | 0.67% | -5.35% | 0.768 | -0.0120 |
| 5 | ev15_mixed | 178 | 140/38 | 1.83% | -0.06% | -6.14% | 0.767 | -0.0221 |
| 6 | ev18_mixed | 151 | 119/32 | 1.58% | -0.33% | -7.17% | 0.760 | -0.0284 |
| 7 | ecmwf_only | 173 | 138/35 | 0.78% | -1.11% | -7.52% | 0.768 | -0.0374 |
| 8 | d2_only | 170 | 136/34 | 0.88% | -1.01% | -8.08% | 0.768 | -0.0384 |
| 9 | d2_entry_72_85 | 154 | 124/30 | 0.58% | -1.29% | -8.49% | 0.775 | -0.0426 |
| 10 | entry_70_80 | 145 | 112/33 | 0.33% | -1.59% | -9.24% | 0.752 | -0.0482 |
| 11 | entry_72_82 | 143 | 113/30 | 0.05% | -1.84% | -9.43% | 0.764 | -0.0514 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 149 | 117/32 | -1.63% | -3.51% | -10.36% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 183 | 149/34 | 3.34% | -2.16% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 190 | 154/36 | 2.10% | -3.40% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
