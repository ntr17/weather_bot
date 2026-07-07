# Strategy Lab
Generated: 2026-07-07T10:02:30.156950+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 66
  - need post-activation ROI after drag >=3%, have 1.78%
  - need positive bootstrap lower bound, have -4.07%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 66 | 57/9 | 7.76% | 5.86% | -4.07% | 0.769 | 0.0444 |
| 2 | d2_ev15 | 66 | 57/9 | 7.76% | 5.86% | -4.07% | 0.769 | 0.0444 |
| 3 | d2_ecmwf_only | 66 | 57/9 | 7.76% | 5.86% | -4.07% | 0.769 | 0.0444 |
| 4 | d2_ev18 | 62 | 53/9 | 7.26% | 5.36% | -5.57% | 0.767 | 0.0341 |
| 5 | ev15_mixed | 77 | 63/14 | 5.88% | 3.97% | -5.44% | 0.767 | 0.0207 |
| 6 | d2_only | 69 | 59/10 | 4.37% | 2.49% | -8.05% | 0.771 | -0.0033 |
| 7 | ev18_mixed | 69 | 56/13 | 4.26% | 2.35% | -8.30% | 0.764 | -0.0056 |
| 8 | ecmwf_only | 72 | 61/11 | 4.05% | 2.16% | -7.99% | 0.770 | -0.0064 |
| 9 | entry_70_80 | 68 | 55/13 | 3.26% | 1.35% | -9.96% | 0.757 | -0.0214 |
| 10 | d2_entry_72_85 | 64 | 54/10 | 3.01% | 1.14% | -10.18% | 0.776 | -0.0242 |
| 11 | entry_72_82 | 68 | 54/14 | 0.62% | -1.27% | -12.18% | 0.767 | -0.0553 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 48 | 40/8 | 3.65% | 1.78% | -10.08% | 0.773 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 82 | 72/10 | 7.85% | 0.14% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 89 | 77/12 | 5.62% | -2.59% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
