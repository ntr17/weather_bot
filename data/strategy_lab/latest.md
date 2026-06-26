# Strategy Lab
Generated: 2026-06-26T04:43:01.585066+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 48
  - need post-activation ROI after drag >=3%, have -8.11%
  - need positive bootstrap lower bound, have -7.76%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 48 | 40/8 | 5.77% | 3.87% | -7.76% | 0.771 | 0.0075 |
| 2 | d2_ev15 | 48 | 40/8 | 5.77% | 3.87% | -7.76% | 0.771 | 0.0075 |
| 3 | d2_ecmwf_only | 48 | 40/8 | 5.77% | 3.87% | -7.76% | 0.771 | 0.0075 |
| 4 | ev15_mixed | 59 | 46/13 | 3.92% | 2.01% | -8.14% | 0.767 | -0.0084 |
| 5 | d2_ev18 | 45 | 37/8 | 5.06% | 3.16% | -9.43% | 0.769 | -0.0114 |
| 6 | ecmwf_only | 54 | 44/10 | 1.88% | -0.01% | -11.53% | 0.772 | -0.0404 |
| 7 | d2_only | 51 | 42/9 | 2.14% | 0.25% | -12.56% | 0.773 | -0.0415 |
| 8 | ev18_mixed | 52 | 40/12 | 1.73% | -0.17% | -12.76% | 0.766 | -0.0464 |
| 9 | entry_70_80 | 54 | 42/12 | 1.50% | -0.41% | -13.26% | 0.760 | -0.0505 |
| 10 | d2_entry_72_85 | 48 | 39/9 | 1.09% | -0.79% | -14.17% | 0.777 | -0.0615 |
| 11 | entry_72_82 | 55 | 42/13 | -1.01% | -2.89% | -15.25% | 0.769 | -0.0823 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 30 | 23/7 | -6.26% | -8.11% | -26.09% | 0.779 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 64 | 55/9 | 6.87% | -1.27% | 0.757 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 71 | 60/11 | 4.56% | -4.20% | 0.757 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
