# Strategy Lab
Generated: 2026-07-11T03:45:57.832389+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 74
  - need post-activation ROI after drag >=3%, have -1.50%
  - need positive bootstrap lower bound, have -5.14%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 74 | 62/12 | 6.20% | 4.30% | -5.14% | 0.767 | 0.0250 |
| 2 | d2_ev15 | 74 | 62/12 | 6.20% | 4.30% | -5.14% | 0.767 | 0.0250 |
| 3 | d2_ecmwf_only | 74 | 62/12 | 6.20% | 4.30% | -5.14% | 0.767 | 0.0250 |
| 4 | d2_ev18 | 69 | 57/12 | 5.48% | 3.57% | -6.57% | 0.763 | 0.0127 |
| 5 | ev15_mixed | 85 | 68/17 | 4.60% | 2.69% | -6.33% | 0.765 | 0.0047 |
| 6 | d2_only | 77 | 64/13 | 3.14% | 1.25% | -8.91% | 0.768 | -0.0187 |
| 7 | ecmwf_only | 80 | 66/14 | 2.88% | 0.99% | -8.73% | 0.768 | -0.0207 |
| 8 | d2_entry_72_85 | 69 | 58/11 | 2.94% | 1.07% | -9.78% | 0.775 | -0.0235 |
| 9 | ev18_mixed | 76 | 60/16 | 2.73% | 0.82% | -9.10% | 0.761 | -0.0237 |
| 10 | entry_70_80 | 75 | 59/16 | 2.01% | 0.09% | -10.66% | 0.754 | -0.0364 |
| 11 | entry_72_82 | 72 | 57/15 | 0.52% | -1.38% | -12.28% | 0.766 | -0.0568 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 56 | 45/11 | 0.38% | -1.50% | -13.34% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 90 | 77/13 | 6.78% | -0.43% | 0.757 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 97 | 82/15 | 4.73% | -3.24% | 0.757 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
