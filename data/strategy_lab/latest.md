# Strategy Lab
Generated: 2026-07-06T20:16:16.312466+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 65
  - need post-activation ROI after drag >=3%, have 1.08%
  - need positive bootstrap lower bound, have -4.25%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 65 | 56/9 | 7.53% | 5.64% | -4.25% | 0.770 | 0.0415 |
| 2 | d2_ev15 | 65 | 56/9 | 7.53% | 5.64% | -4.25% | 0.770 | 0.0415 |
| 3 | d2_ecmwf_only | 65 | 56/9 | 7.53% | 5.64% | -4.25% | 0.770 | 0.0415 |
| 4 | d2_ev18 | 61 | 52/9 | 7.01% | 5.10% | -5.81% | 0.767 | 0.0307 |
| 5 | ev15_mixed | 76 | 62/14 | 5.67% | 3.76% | -5.28% | 0.767 | 0.0191 |
| 6 | d2_only | 68 | 58/10 | 4.15% | 2.26% | -8.44% | 0.771 | -0.0069 |
| 7 | ecmwf_only | 71 | 60/11 | 3.83% | 1.94% | -8.34% | 0.771 | -0.0098 |
| 8 | ev18_mixed | 68 | 55/13 | 3.99% | 2.09% | -8.81% | 0.765 | -0.0099 |
| 9 | entry_70_80 | 67 | 54/13 | 3.04% | 1.12% | -10.10% | 0.757 | -0.0242 |
| 10 | d2_entry_72_85 | 63 | 53/10 | 2.76% | 0.89% | -10.84% | 0.776 | -0.0290 |
| 11 | entry_72_82 | 67 | 53/14 | 0.36% | -1.53% | -12.95% | 0.767 | -0.0606 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 47 | 39/8 | 2.94% | 1.08% | -11.27% | 0.774 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 81 | 71/10 | 7.72% | 0.16% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 88 | 76/12 | 5.49% | -2.61% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
