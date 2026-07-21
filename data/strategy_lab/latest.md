# Strategy Lab
Generated: 2026-07-21T19:54:51.938248+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 96
  - need post-activation ROI after drag >=3%, have 1.14%
  - need positive bootstrap lower bound, have -3.19%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 96 | 81/15 | 6.69% | 4.79% | -3.19% | 0.765 | 0.0367 |
| 2 | d2_ev15 | 96 | 81/15 | 6.69% | 4.79% | -3.19% | 0.765 | 0.0367 |
| 3 | d2_ecmwf_only | 96 | 81/15 | 6.69% | 4.79% | -3.19% | 0.765 | 0.0367 |
| 4 | d2_ev18 | 89 | 74/15 | 5.91% | 4.00% | -5.18% | 0.761 | 0.0219 |
| 5 | ev15_mixed | 107 | 87/20 | 5.23% | 3.33% | -4.32% | 0.764 | 0.0182 |
| 6 | d2_only | 99 | 83/16 | 3.97% | 2.08% | -6.67% | 0.766 | -0.0025 |
| 7 | ecmwf_only | 102 | 85/17 | 3.71% | 1.82% | -6.74% | 0.766 | -0.0054 |
| 8 | d2_entry_72_85 | 87 | 74/13 | 3.81% | 1.93% | -7.80% | 0.775 | -0.0080 |
| 9 | ev18_mixed | 96 | 77/19 | 3.50% | 1.59% | -7.11% | 0.760 | -0.0090 |
| 10 | entry_70_80 | 90 | 71/19 | 2.21% | 0.29% | -9.36% | 0.751 | -0.0299 |
| 11 | entry_72_82 | 87 | 70/17 | 1.27% | -0.62% | -10.19% | 0.765 | -0.0419 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 78 | 64/14 | 3.03% | 1.14% | -8.05% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 112 | 96/16 | 6.88% | 0.23% | 0.758 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 119 | 101/18 | 4.99% | -2.16% | 0.758 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
