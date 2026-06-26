# Strategy Lab
Generated: 2026-06-26T20:13:33.076555+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 49
  - need post-activation ROI after drag >=3%, have -6.78%
  - need positive bootstrap lower bound, have -7.22%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 49 | 41/8 | 6.03% | 4.13% | -7.22% | 0.770 | 0.0140 |
| 2 | d2_ev15 | 49 | 41/8 | 6.03% | 4.13% | -7.22% | 0.770 | 0.0140 |
| 3 | d2_ecmwf_only | 49 | 41/8 | 6.03% | 4.13% | -7.22% | 0.770 | 0.0140 |
| 4 | ev15_mixed | 60 | 47/13 | 4.15% | 2.25% | -7.62% | 0.767 | -0.0042 |
| 5 | d2_ev18 | 46 | 38/8 | 5.36% | 3.45% | -9.66% | 0.769 | -0.0073 |
| 6 | d2_only | 52 | 43/9 | 2.39% | 0.51% | -11.58% | 0.772 | -0.0354 |
| 7 | ecmwf_only | 55 | 45/10 | 2.13% | 0.24% | -11.36% | 0.771 | -0.0374 |
| 8 | ev18_mixed | 53 | 41/12 | 2.04% | 0.13% | -11.95% | 0.766 | -0.0405 |
| 9 | entry_70_80 | 55 | 43/12 | 1.75% | -0.16% | -12.81% | 0.759 | -0.0464 |
| 10 | d2_entry_72_85 | 49 | 40/9 | 1.37% | -0.51% | -14.07% | 0.776 | -0.0563 |
| 11 | entry_72_82 | 56 | 43/13 | -0.73% | -2.62% | -15.26% | 0.769 | -0.0796 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 24/7 | -4.92% | -6.78% | -24.17% | 0.778 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 65 | 56/9 | 7.01% | -1.23% | 0.756 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 72 | 61/11 | 4.70% | -4.10% | 0.756 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
