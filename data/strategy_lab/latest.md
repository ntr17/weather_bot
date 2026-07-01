# Strategy Lab
Generated: 2026-07-01T10:17:23.342154+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 55
  - need post-activation ROI after drag >=3%, have -4.85%
  - need positive bootstrap lower bound, have -6.56%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 55 | 46/9 | 6.08% | 4.18% | -6.56% | 0.771 | 0.0188 |
| 2 | d2_ev15 | 55 | 46/9 | 6.08% | 4.18% | -6.56% | 0.771 | 0.0188 |
| 3 | d2_ecmwf_only | 55 | 46/9 | 6.08% | 4.18% | -6.56% | 0.771 | 0.0188 |
| 4 | d2_ev18 | 52 | 43/9 | 5.45% | 3.55% | -8.46% | 0.770 | 0.0059 |
| 5 | ev15_mixed | 66 | 52/14 | 4.27% | 2.37% | -7.45% | 0.768 | -0.0024 |
| 6 | d2_only | 58 | 48/10 | 2.60% | 0.71% | -10.60% | 0.773 | -0.0300 |
| 7 | ecmwf_only | 61 | 50/11 | 2.33% | 0.45% | -10.24% | 0.772 | -0.0313 |
| 8 | ev18_mixed | 59 | 46/13 | 2.30% | 0.39% | -11.54% | 0.767 | -0.0365 |
| 9 | entry_70_80 | 60 | 47/13 | 1.84% | -0.07% | -12.28% | 0.760 | -0.0437 |
| 10 | d2_entry_72_85 | 55 | 45/10 | 1.63% | -0.24% | -12.92% | 0.777 | -0.0476 |
| 11 | entry_72_82 | 61 | 47/14 | -0.55% | -2.44% | -14.10% | 0.769 | -0.0737 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 37 | 29/8 | -2.99% | -4.85% | -20.32% | 0.778 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 71 | 61/10 | 6.95% | -1.05% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 78 | 66/12 | 4.71% | -3.95% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
