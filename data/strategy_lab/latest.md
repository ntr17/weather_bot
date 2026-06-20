# Strategy Lab
Generated: 2026-06-20T04:43:02.573546+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 39
  - need >=30 post-activation resolved trades, have 21
  - need post-activation ROI after drag >=3%, have 1.35%
  - need positive bootstrap lower bound, have -4.92%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 39 | 35/4 | 8.75% | 6.84% | -4.92% | 0.768 | 0.0292 |
| 2 | d2_ev15 | 39 | 35/4 | 8.75% | 6.84% | -4.92% | 0.768 | 0.0292 |
| 3 | d2_ecmwf_only | 39 | 35/4 | 8.75% | 6.84% | -4.92% | 0.768 | 0.0292 |
| 4 | ev15_mixed | 50 | 41/9 | 6.29% | 4.38% | -6.42% | 0.765 | 0.0213 |
| 5 | d2_ev18 | 37 | 33/4 | 8.37% | 6.46% | -7.25% | 0.768 | 0.0132 |
| 6 | ev18_mixed | 44 | 36/8 | 4.54% | 2.63% | -10.15% | 0.764 | -0.0212 |
| 7 | ecmwf_only | 45 | 39/6 | 4.06% | 2.17% | -9.66% | 0.770 | -0.0221 |
| 8 | d2_only | 42 | 37/5 | 4.46% | 2.57% | -10.40% | 0.771 | -0.0267 |
| 9 | entry_70_80 | 47 | 38/9 | 2.90% | 0.99% | -12.44% | 0.759 | -0.0396 |
| 10 | d2_entry_72_85 | 40 | 35/5 | 3.81% | 1.93% | -11.89% | 0.774 | -0.0423 |
| 11 | entry_72_82 | 49 | 39/10 | 0.61% | -1.28% | -13.92% | 0.769 | -0.0635 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 21 | 18/3 | 3.21% | 1.35% | -16.30% | 0.778 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 55 | 50/5 | 8.69% | 0.22% | 0.752 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 62 | 55/7 | 6.08% | -2.55% | 0.753 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
