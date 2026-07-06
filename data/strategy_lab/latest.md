# Strategy Lab
Generated: 2026-07-06T04:44:00.173025+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 64
  - need post-activation ROI after drag >=3%, have 0.85%
  - need positive bootstrap lower bound, have -4.23%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 64 | 55/9 | 7.49% | 5.59% | -4.23% | 0.770 | 0.0411 |
| 2 | d2_ev15 | 64 | 55/9 | 7.49% | 5.59% | -4.23% | 0.770 | 0.0411 |
| 3 | d2_ecmwf_only | 64 | 55/9 | 7.49% | 5.59% | -4.23% | 0.770 | 0.0411 |
| 4 | d2_ev18 | 60 | 51/9 | 6.95% | 5.05% | -5.59% | 0.768 | 0.0309 |
| 5 | ev15_mixed | 75 | 61/14 | 5.61% | 3.71% | -5.26% | 0.768 | 0.0187 |
| 6 | d2_only | 67 | 57/10 | 4.08% | 2.19% | -8.77% | 0.772 | -0.0088 |
| 7 | ecmwf_only | 70 | 59/11 | 3.76% | 1.88% | -8.36% | 0.771 | -0.0105 |
| 8 | ev18_mixed | 67 | 54/13 | 3.91% | 2.01% | -9.04% | 0.765 | -0.0115 |
| 9 | entry_70_80 | 66 | 53/13 | 2.96% | 1.05% | -10.43% | 0.758 | -0.0260 |
| 10 | d2_entry_72_85 | 62 | 52/10 | 2.68% | 0.81% | -10.50% | 0.777 | -0.0286 |
| 11 | entry_72_82 | 66 | 52/14 | 0.27% | -1.62% | -13.00% | 0.768 | -0.0617 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 46 | 38/8 | 2.71% | 0.85% | -11.97% | 0.775 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 80 | 70/10 | 7.70% | 0.11% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 87 | 75/12 | 5.47% | -2.55% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
