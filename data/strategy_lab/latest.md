# Strategy Lab
Generated: 2026-06-21T20:06:26.142178+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 42
  - need >=30 post-activation resolved trades, have 24
  - need post-activation ROI after drag >=3%, have -6.87%
  - need positive bootstrap lower bound, have -7.25%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 42 | 36/6 | 6.73% | 4.83% | -7.25% | 0.772 | 0.0069 |
| 2 | d2_ev15 | 42 | 36/6 | 6.73% | 4.83% | -7.25% | 0.772 | 0.0069 |
| 3 | d2_ecmwf_only | 42 | 36/6 | 6.73% | 4.83% | -7.25% | 0.772 | 0.0069 |
| 4 | ev15_mixed | 53 | 42/11 | 4.64% | 2.73% | -8.01% | 0.768 | -0.0007 |
| 5 | d2_ev18 | 39 | 33/6 | 6.09% | 4.19% | -9.28% | 0.770 | -0.0126 |
| 6 | ecmwf_only | 48 | 40/8 | 2.49% | 0.61% | -11.48% | 0.773 | -0.0381 |
| 7 | d2_only | 45 | 38/7 | 2.80% | 0.91% | -11.82% | 0.774 | -0.0423 |
| 8 | ev18_mixed | 46 | 36/10 | 2.49% | 0.58% | -12.60% | 0.766 | -0.0463 |
| 9 | entry_70_80 | 48 | 38/10 | 2.10% | 0.19% | -12.79% | 0.759 | -0.0469 |
| 10 | d2_entry_72_85 | 43 | 36/7 | 2.07% | 0.20% | -13.61% | 0.777 | -0.0596 |
| 11 | entry_72_82 | 50 | 39/11 | -0.19% | -2.08% | -15.08% | 0.769 | -0.0736 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 24 | 19/5 | -5.03% | -6.87% | -25.66% | 0.782 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 58 | 51/7 | 7.52% | -1.14% | 0.756 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 65 | 56/9 | 5.07% | -3.59% | 0.756 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
