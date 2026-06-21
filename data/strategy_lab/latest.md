# Strategy Lab
Generated: 2026-06-21T14:35:07.936421+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 41
  - need >=30 post-activation resolved trades, have 23
  - need post-activation ROI after drag >=3%, have -2.75%
  - need positive bootstrap lower bound, have -5.56%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 41 | 36/5 | 7.74% | 5.84% | -5.56% | 0.770 | 0.0209 |
| 2 | d2_ev15 | 41 | 36/5 | 7.74% | 5.84% | -5.56% | 0.770 | 0.0209 |
| 3 | d2_ecmwf_only | 41 | 36/5 | 7.74% | 5.84% | -5.56% | 0.770 | 0.0209 |
| 4 | ev15_mixed | 52 | 42/10 | 5.48% | 3.57% | -7.25% | 0.766 | 0.0103 |
| 5 | d2_ev18 | 38 | 33/5 | 7.22% | 5.31% | -8.09% | 0.768 | 0.0008 |
| 6 | ecmwf_only | 47 | 40/7 | 3.30% | 1.41% | -10.78% | 0.771 | -0.0296 |
| 7 | d2_only | 44 | 38/6 | 3.65% | 1.76% | -11.07% | 0.772 | -0.0331 |
| 8 | ev18_mixed | 45 | 36/9 | 3.50% | 1.59% | -11.40% | 0.765 | -0.0340 |
| 9 | entry_70_80 | 48 | 38/10 | 2.10% | 0.19% | -12.79% | 0.759 | -0.0469 |
| 10 | d2_entry_72_85 | 42 | 36/6 | 2.97% | 1.09% | -12.65% | 0.776 | -0.0494 |
| 11 | entry_72_82 | 50 | 39/11 | -0.19% | -2.08% | -15.08% | 0.769 | -0.0736 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 23 | 19/4 | -0.90% | -2.75% | -21.02% | 0.780 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 57 | 51/6 | 8.11% | -0.62% | 0.754 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 64 | 56/8 | 5.58% | -3.34% | 0.755 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
