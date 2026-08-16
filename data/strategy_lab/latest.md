# Strategy Lab
Generated: 2026-08-16T07:02:37.748237+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.71%
  - need post-activation ROI after drag >=3%, have -0.84%
  - need positive bootstrap lower bound, have -3.59%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 146 | 120/26 | 4.61% | 2.71% | -3.59% | 0.764 | 0.0145 |
| 2 | d2_ev15 | 146 | 120/26 | 4.61% | 2.71% | -3.59% | 0.764 | 0.0145 |
| 3 | d2_ecmwf_only | 146 | 120/26 | 4.61% | 2.71% | -3.59% | 0.764 | 0.0145 |
| 4 | d2_ev18 | 127 | 104/23 | 4.72% | 2.81% | -5.07% | 0.757 | 0.0103 |
| 5 | ev15_mixed | 157 | 126/31 | 3.65% | 1.74% | -4.73% | 0.763 | 0.0008 |
| 6 | ev18_mixed | 134 | 107/27 | 2.84% | 0.92% | -6.53% | 0.757 | -0.0137 |
| 7 | d2_only | 149 | 122/27 | 2.64% | 0.74% | -6.67% | 0.765 | -0.0159 |
| 8 | ecmwf_only | 152 | 124/28 | 2.48% | 0.58% | -6.35% | 0.765 | -0.0164 |
| 9 | d2_entry_72_85 | 133 | 110/23 | 2.48% | 0.60% | -7.00% | 0.772 | -0.0185 |
| 10 | entry_70_80 | 132 | 104/28 | 1.74% | -0.19% | -8.04% | 0.750 | -0.0300 |
| 11 | entry_72_82 | 128 | 103/25 | 1.28% | -0.61% | -8.79% | 0.763 | -0.0369 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 128 | 103/25 | 1.05% | -0.84% | -8.03% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 162 | 135/27 | 5.02% | -0.45% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 169 | 140/29 | 3.57% | -2.35% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
