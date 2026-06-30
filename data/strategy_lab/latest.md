# Strategy Lab
Generated: 2026-06-30T10:03:31.507962+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 52
  - need post-activation ROI after drag >=3%, have -7.75%
  - need positive bootstrap lower bound, have -7.58%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 52 | 43/9 | 5.46% | 3.56% | -7.58% | 0.771 | 0.0091 |
| 2 | d2_ev15 | 52 | 43/9 | 5.46% | 3.56% | -7.58% | 0.771 | 0.0091 |
| 3 | d2_ecmwf_only | 52 | 43/9 | 5.46% | 3.56% | -7.58% | 0.771 | 0.0091 |
| 4 | d2_ev18 | 49 | 40/9 | 4.75% | 2.85% | -9.76% | 0.770 | -0.0077 |
| 5 | ev15_mixed | 63 | 49/14 | 3.71% | 1.80% | -8.65% | 0.768 | -0.0123 |
| 6 | d2_only | 55 | 45/10 | 1.97% | 0.09% | -11.76% | 0.773 | -0.0403 |
| 7 | ecmwf_only | 58 | 47/11 | 1.73% | -0.15% | -11.31% | 0.772 | -0.0411 |
| 8 | ev18_mixed | 56 | 43/13 | 1.56% | -0.35% | -12.23% | 0.767 | -0.0463 |
| 9 | entry_70_80 | 57 | 44/13 | 1.23% | -0.68% | -13.51% | 0.760 | -0.0541 |
| 10 | d2_entry_72_85 | 52 | 42/10 | 0.95% | -0.93% | -13.55% | 0.777 | -0.0567 |
| 11 | entry_72_82 | 58 | 44/14 | -1.23% | -3.12% | -15.21% | 0.769 | -0.0844 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 34 | 26/8 | -5.90% | -7.75% | -24.38% | 0.779 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 68 | 58/10 | 6.63% | -1.61% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 75 | 63/12 | 4.39% | -4.40% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
