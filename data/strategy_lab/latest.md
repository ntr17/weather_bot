# Strategy Lab
Generated: 2026-08-18T07:08:00.038256+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 1.94%
  - need post-activation ROI after drag >=3%, have -1.98%
  - need positive bootstrap lower bound, have -4.65%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 150 | 122/28 | 3.84% | 1.94% | -4.65% | 0.764 | 0.0031 |
| 2 | d2_ev15 | 150 | 122/28 | 3.84% | 1.94% | -4.65% | 0.764 | 0.0031 |
| 3 | d2_ecmwf_only | 150 | 122/28 | 3.84% | 1.94% | -4.65% | 0.764 | 0.0031 |
| 4 | d2_ev18 | 131 | 106/25 | 3.84% | 1.92% | -5.50% | 0.757 | -0.0001 |
| 5 | ev15_mixed | 161 | 128/33 | 2.96% | 1.05% | -5.15% | 0.763 | -0.0075 |
| 6 | ev18_mixed | 138 | 109/29 | 2.03% | 0.11% | -6.89% | 0.757 | -0.0230 |
| 7 | ecmwf_only | 156 | 126/30 | 1.81% | -0.08% | -6.78% | 0.765 | -0.0245 |
| 8 | d2_only | 153 | 124/29 | 1.95% | 0.06% | -7.41% | 0.765 | -0.0253 |
| 9 | d2_entry_72_85 | 137 | 112/25 | 1.73% | -0.15% | -7.98% | 0.772 | -0.0294 |
| 10 | entry_70_80 | 136 | 106/30 | 1.03% | -0.90% | -8.51% | 0.751 | -0.0388 |
| 11 | entry_72_82 | 132 | 105/27 | 0.56% | -1.34% | -8.97% | 0.763 | -0.0448 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 132 | 105/27 | -0.09% | -1.98% | -9.19% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 166 | 137/29 | 4.43% | -1.10% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 173 | 142/31 | 3.04% | -2.79% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
