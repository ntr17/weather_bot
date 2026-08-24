# Strategy Lab
Generated: 2026-08-24T02:00:12.844893+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.34%
  - need post-activation ROI after drag >=3%, have -4.30%
  - need positive bootstrap lower bound, have -5.94%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 135 | 108/27 | 2.91% | 1.00% | -6.29% | 0.759 | -0.0120 |
| 2 | current_paper | 158 | 126/32 | 2.23% | 0.34% | -5.94% | 0.767 | -0.0174 |
| 3 | d2_ev15 | 158 | 126/32 | 2.23% | 0.34% | -5.94% | 0.767 | -0.0174 |
| 4 | d2_ecmwf_only | 158 | 126/32 | 2.23% | 0.34% | -5.94% | 0.767 | -0.0174 |
| 5 | ev15_mixed | 169 | 132/37 | 1.50% | -0.39% | -6.80% | 0.766 | -0.0277 |
| 6 | ev18_mixed | 142 | 111/31 | 1.17% | -0.74% | -7.85% | 0.759 | -0.0349 |
| 7 | ecmwf_only | 164 | 130/34 | 0.41% | -1.47% | -8.05% | 0.768 | -0.0429 |
| 8 | d2_only | 161 | 128/33 | 0.51% | -1.38% | -8.67% | 0.768 | -0.0441 |
| 9 | d2_entry_72_85 | 145 | 116/29 | 0.16% | -1.71% | -9.33% | 0.775 | -0.0498 |
| 10 | entry_70_80 | 138 | 106/32 | 0.10% | -1.82% | -9.77% | 0.751 | -0.0524 |
| 11 | entry_72_82 | 134 | 105/29 | -0.40% | -2.30% | -10.06% | 0.763 | -0.0582 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 140 | 109/31 | -2.42% | -4.30% | -11.50% | 0.768 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 174 | 141/33 | 3.18% | -2.52% | 0.762 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 181 | 146/35 | 1.92% | -3.80% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
