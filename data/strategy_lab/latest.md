# Strategy Lab
Generated: 2026-07-16T14:26:18.097545+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 86
  - need post-activation ROI after drag >=3%, have 2.58%
  - need positive bootstrap lower bound, have -2.90%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 86 | 74/12 | 7.58% | 5.68% | -2.90% | 0.768 | 0.0466 |
| 2 | d2_ev15 | 86 | 74/12 | 7.58% | 5.68% | -2.90% | 0.768 | 0.0466 |
| 3 | d2_ecmwf_only | 86 | 74/12 | 7.58% | 5.68% | -2.90% | 0.768 | 0.0466 |
| 4 | d2_ev18 | 80 | 68/12 | 6.94% | 5.03% | -4.34% | 0.764 | 0.0351 |
| 5 | ev15_mixed | 97 | 80/17 | 5.94% | 4.03% | -4.12% | 0.766 | 0.0259 |
| 6 | d2_only | 89 | 76/13 | 4.62% | 2.73% | -6.91% | 0.769 | 0.0031 |
| 7 | ecmwf_only | 92 | 78/14 | 4.32% | 2.43% | -6.68% | 0.769 | 0.0009 |
| 8 | ev18_mixed | 87 | 71/16 | 4.33% | 2.42% | -6.93% | 0.763 | -0.0001 |
| 9 | d2_entry_72_85 | 80 | 69/11 | 4.32% | 2.44% | -7.55% | 0.776 | -0.0020 |
| 10 | entry_70_80 | 82 | 66/16 | 3.00% | 1.08% | -9.15% | 0.754 | -0.0212 |
| 11 | entry_72_82 | 81 | 66/15 | 1.77% | -0.12% | -10.21% | 0.766 | -0.0369 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 68 | 57/11 | 4.46% | 2.58% | -6.56% | 0.771 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 102 | 89/13 | 7.56% | 0.83% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 109 | 94/15 | 5.53% | -1.95% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
