# Strategy Lab
Generated: 2026-08-15T01:52:30.676119+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.68%
  - need post-activation ROI after drag >=3%, have -0.91%
  - need positive bootstrap lower bound, have -3.94%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 145 | 119/26 | 4.58% | 2.68% | -3.94% | 0.764 | 0.0130 |
| 2 | d2_ev15 | 145 | 119/26 | 4.58% | 2.68% | -3.94% | 0.764 | 0.0130 |
| 3 | d2_ecmwf_only | 145 | 119/26 | 4.58% | 2.68% | -3.94% | 0.764 | 0.0130 |
| 4 | d2_ev18 | 126 | 103/23 | 4.69% | 2.77% | -5.21% | 0.758 | 0.0095 |
| 5 | ev15_mixed | 156 | 125/31 | 3.62% | 1.71% | -4.85% | 0.763 | 0.0001 |
| 6 | ev18_mixed | 133 | 106/27 | 2.80% | 0.88% | -6.69% | 0.757 | -0.0146 |
| 7 | d2_only | 148 | 121/27 | 2.60% | 0.71% | -6.77% | 0.765 | -0.0166 |
| 8 | ecmwf_only | 151 | 123/28 | 2.44% | 0.55% | -6.39% | 0.765 | -0.0169 |
| 9 | d2_entry_72_85 | 132 | 109/23 | 2.44% | 0.56% | -7.19% | 0.772 | -0.0196 |
| 10 | entry_70_80 | 131 | 103/28 | 1.70% | -0.23% | -8.13% | 0.750 | -0.0307 |
| 11 | entry_72_82 | 127 | 102/25 | 1.24% | -0.66% | -8.51% | 0.763 | -0.0364 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 127 | 102/25 | 0.97% | -0.91% | -7.97% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 161 | 134/27 | 5.01% | -0.79% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 168 | 139/29 | 3.55% | -2.42% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
