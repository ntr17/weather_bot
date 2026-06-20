# Strategy Lab
Generated: 2026-06-20T14:34:09.532384+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 40
  - need >=30 post-activation resolved trades, have 22
  - need post-activation ROI after drag >=3%, have 1.76%
  - need positive bootstrap lower bound, have -5.02%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 40 | 36/4 | 8.78% | 6.88% | -5.02% | 0.770 | 0.0312 |
| 2 | d2_ev15 | 40 | 36/4 | 8.78% | 6.88% | -5.02% | 0.770 | 0.0312 |
| 3 | d2_ecmwf_only | 40 | 36/4 | 8.78% | 6.88% | -5.02% | 0.770 | 0.0312 |
| 4 | ev15_mixed | 51 | 42/9 | 6.34% | 4.43% | -5.89% | 0.766 | 0.0237 |
| 5 | d2_ev18 | 37 | 33/4 | 8.37% | 6.46% | -7.25% | 0.768 | 0.0132 |
| 6 | ecmwf_only | 46 | 40/6 | 4.12% | 2.23% | -10.04% | 0.771 | -0.0208 |
| 7 | ev18_mixed | 44 | 36/8 | 4.54% | 2.63% | -10.15% | 0.764 | -0.0212 |
| 8 | d2_only | 43 | 38/5 | 4.52% | 2.64% | -10.32% | 0.772 | -0.0237 |
| 9 | d2_entry_72_85 | 41 | 36/5 | 3.88% | 2.00% | -11.32% | 0.776 | -0.0376 |
| 10 | entry_70_80 | 47 | 38/9 | 2.90% | 0.99% | -12.44% | 0.759 | -0.0396 |
| 11 | entry_72_82 | 49 | 39/10 | 0.61% | -1.28% | -13.92% | 0.769 | -0.0635 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 22 | 19/3 | 3.61% | 1.76% | -15.35% | 0.780 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 56 | 51/5 | 8.70% | -0.07% | 0.754 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 63 | 56/7 | 6.10% | -2.46% | 0.754 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
