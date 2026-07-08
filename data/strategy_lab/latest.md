# Strategy Lab
Generated: 2026-07-08T08:46:41.607652+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 69
  - need post-activation ROI after drag >=3%, have 2.98%
  - need positive bootstrap lower bound, have -3.01%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 69 | 60/9 | 8.12% | 6.23% | -3.01% | 0.770 | 0.0518 |
| 2 | d2_ev15 | 69 | 60/9 | 8.12% | 6.23% | -3.01% | 0.770 | 0.0518 |
| 3 | d2_ecmwf_only | 69 | 60/9 | 8.12% | 6.23% | -3.01% | 0.770 | 0.0518 |
| 4 | d2_ev18 | 64 | 55/9 | 7.59% | 5.69% | -4.97% | 0.766 | 0.0395 |
| 5 | ev15_mixed | 80 | 66/14 | 6.23% | 4.33% | -4.56% | 0.767 | 0.0273 |
| 6 | d2_only | 72 | 62/10 | 4.77% | 2.88% | -7.30% | 0.771 | 0.0032 |
| 7 | ev18_mixed | 71 | 58/13 | 4.61% | 2.71% | -7.72% | 0.764 | 0.0001 |
| 8 | ecmwf_only | 75 | 64/11 | 4.43% | 2.54% | -7.44% | 0.771 | -0.0006 |
| 9 | entry_70_80 | 70 | 57/13 | 3.58% | 1.67% | -9.33% | 0.757 | -0.0159 |
| 10 | d2_entry_72_85 | 67 | 57/10 | 3.46% | 1.59% | -9.46% | 0.776 | -0.0172 |
| 11 | entry_72_82 | 70 | 56/14 | 0.98% | -0.91% | -12.05% | 0.766 | -0.0513 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 51 | 43/8 | 4.84% | 2.98% | -8.92% | 0.774 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 85 | 75/10 | 8.05% | 0.80% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 92 | 80/12 | 5.83% | -2.01% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
