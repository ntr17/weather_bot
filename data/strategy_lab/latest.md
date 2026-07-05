# Strategy Lab
Generated: 2026-07-05T14:11:58.874272+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 61
  - need post-activation ROI after drag >=3%, have -0.62%
  - need positive bootstrap lower bound, have -4.91%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 61 | 52/9 | 7.10% | 5.20% | -4.91% | 0.771 | 0.0348 |
| 2 | d2_ev15 | 61 | 52/9 | 7.10% | 5.20% | -4.91% | 0.771 | 0.0348 |
| 3 | d2_ecmwf_only | 61 | 52/9 | 7.10% | 5.20% | -4.91% | 0.771 | 0.0348 |
| 4 | d2_ev18 | 58 | 49/9 | 6.60% | 4.70% | -6.38% | 0.769 | 0.0247 |
| 5 | ev15_mixed | 72 | 58/14 | 5.23% | 3.33% | -6.10% | 0.768 | 0.0120 |
| 6 | d2_only | 64 | 54/10 | 3.66% | 1.77% | -9.32% | 0.772 | -0.0149 |
| 7 | ev18_mixed | 65 | 52/13 | 3.54% | 1.63% | -9.77% | 0.767 | -0.0179 |
| 8 | ecmwf_only | 67 | 56/11 | 3.35% | 1.47% | -9.39% | 0.772 | -0.0182 |
| 9 | entry_70_80 | 64 | 51/13 | 2.63% | 0.72% | -10.85% | 0.759 | -0.0308 |
| 10 | d2_entry_72_85 | 60 | 50/10 | 2.51% | 0.63% | -10.99% | 0.777 | -0.0322 |
| 11 | entry_72_82 | 65 | 51/14 | 0.19% | -1.69% | -12.84% | 0.768 | -0.0618 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 43 | 35/8 | 1.24% | -0.62% | -14.55% | 0.776 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 77 | 67/10 | 7.49% | -0.26% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 84 | 72/12 | 5.25% | -2.90% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
