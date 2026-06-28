# Strategy Lab
Generated: 2026-06-28T09:34:24.661255+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 50
  - need post-activation ROI after drag >=3%, have -9.75%
  - need positive bootstrap lower bound, have -8.34%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 50 | 41/9 | 5.10% | 3.20% | -8.34% | 0.771 | 0.0028 |
| 2 | d2_ev15 | 50 | 41/9 | 5.10% | 3.20% | -8.34% | 0.771 | 0.0028 |
| 3 | d2_ecmwf_only | 50 | 41/9 | 5.10% | 3.20% | -8.34% | 0.771 | 0.0028 |
| 4 | ev15_mixed | 61 | 47/14 | 3.37% | 1.46% | -9.28% | 0.767 | -0.0179 |
| 5 | d2_ev18 | 47 | 38/9 | 4.34% | 2.43% | -10.41% | 0.769 | -0.0181 |
| 6 | d2_only | 53 | 43/10 | 1.60% | -0.29% | -12.55% | 0.772 | -0.0468 |
| 7 | ecmwf_only | 56 | 45/11 | 1.38% | -0.51% | -12.28% | 0.772 | -0.0481 |
| 8 | ev18_mixed | 54 | 41/13 | 1.11% | -0.79% | -12.86% | 0.766 | -0.0529 |
| 9 | entry_70_80 | 56 | 43/13 | 1.01% | -0.91% | -13.70% | 0.760 | -0.0570 |
| 10 | d2_entry_72_85 | 50 | 40/10 | 0.54% | -1.34% | -14.89% | 0.776 | -0.0655 |
| 11 | entry_72_82 | 57 | 43/14 | -1.48% | -3.37% | -15.71% | 0.769 | -0.0887 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 32 | 24/8 | -7.89% | -9.75% | -27.22% | 0.778 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 66 | 56/10 | 6.45% | -2.16% | 0.757 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 73 | 61/12 | 4.20% | -4.59% | 0.757 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
