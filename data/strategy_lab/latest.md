# Strategy Lab
Generated: 2026-08-01T19:37:15.083306+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need post-activation ROI after drag >=3%, have 0.80%
  - need positive bootstrap lower bound, have -3.27%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 116 | 97/19 | 6.10% | 4.20% | -3.27% | 0.765 | 0.0306 |
| 2 | d2_ev15 | 116 | 97/19 | 6.10% | 4.20% | -3.27% | 0.765 | 0.0306 |
| 3 | d2_ecmwf_only | 116 | 97/19 | 6.10% | 4.20% | -3.27% | 0.765 | 0.0306 |
| 4 | d2_ev18 | 103 | 85/18 | 5.52% | 3.61% | -4.87% | 0.759 | 0.0191 |
| 5 | ev15_mixed | 127 | 103/24 | 4.84% | 2.94% | -4.26% | 0.763 | 0.0145 |
| 6 | d2_only | 119 | 99/20 | 3.71% | 1.81% | -6.21% | 0.765 | -0.0036 |
| 7 | ecmwf_only | 122 | 101/21 | 3.48% | 1.59% | -5.96% | 0.765 | -0.0050 |
| 8 | d2_entry_72_85 | 106 | 89/17 | 3.49% | 1.61% | -7.20% | 0.773 | -0.0091 |
| 9 | ev18_mixed | 110 | 88/22 | 3.33% | 1.42% | -6.78% | 0.758 | -0.0095 |
| 10 | entry_70_80 | 108 | 86/22 | 2.57% | 0.65% | -7.81% | 0.751 | -0.0208 |
| 11 | entry_72_82 | 104 | 84/20 | 1.69% | -0.20% | -8.55% | 0.764 | -0.0319 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 98 | 80/18 | 2.69% | 0.80% | -7.18% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 132 | 112/20 | 6.31% | 0.03% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 139 | 117/22 | 4.60% | -2.02% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
