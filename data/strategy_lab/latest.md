# Strategy Lab
Generated: 2026-06-15T21:26:37.066493+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 28
  - need >=30 post-activation resolved trades, have 10
  - need positive bootstrap lower bound, have -4.87%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 28 | 26/2 | 10.03% | 8.12% | -4.87% | 0.764 | 0.0202 |
| 2 | d2_ev15 | 28 | 26/2 | 10.03% | 8.12% | -4.87% | 0.764 | 0.0202 |
| 3 | d2_ecmwf_only | 28 | 26/2 | 10.03% | 8.12% | -4.87% | 0.764 | 0.0202 |
| 4 | ev15_mixed | 39 | 32/7 | 7.11% | 5.20% | -6.67% | 0.760 | 0.0067 |
| 5 | d2_ev18 | 26 | 24/2 | 9.76% | 7.85% | -7.17% | 0.763 | 0.0054 |
| 6 | ev18_mixed | 33 | 27/6 | 5.34% | 3.43% | -10.85% | 0.759 | -0.0377 |
| 7 | entry_70_80 | 40 | 33/7 | 3.90% | 1.99% | -11.77% | 0.759 | -0.0413 |
| 8 | ecmwf_only | 34 | 30/4 | 4.64% | 2.75% | -10.66% | 0.767 | -0.0418 |
| 9 | d2_only | 31 | 28/3 | 5.13% | 3.23% | -10.87% | 0.767 | -0.0437 |
| 10 | d2_entry_72_85 | 29 | 26/3 | 4.44% | 2.56% | -12.22% | 0.772 | -0.0592 |
| 11 | entry_72_82 | 40 | 32/8 | 1.12% | -0.77% | -14.85% | 0.768 | -0.0797 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 9/1 | 8.96% | 7.09% | -17.06% | 0.775 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 44 | 41/3 | 9.50% | 0.24% | 0.746 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 51 | 46/5 | 6.64% | -2.59% | 0.747 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
