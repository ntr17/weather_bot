# Strategy Lab
Generated: 2026-07-04T14:02:02.494073+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 60
  - need post-activation ROI after drag >=3%, have -1.38%
  - need positive bootstrap lower bound, have -5.02%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 60 | 51/9 | 6.88% | 4.99% | -5.02% | 0.771 | 0.0323 |
| 2 | d2_ev15 | 60 | 51/9 | 6.88% | 4.99% | -5.02% | 0.771 | 0.0323 |
| 3 | d2_ecmwf_only | 60 | 51/9 | 6.88% | 4.99% | -5.02% | 0.771 | 0.0323 |
| 4 | d2_ev18 | 57 | 48/9 | 6.36% | 4.46% | -6.83% | 0.770 | 0.0207 |
| 5 | ev15_mixed | 71 | 57/14 | 5.04% | 3.14% | -6.40% | 0.768 | 0.0090 |
| 6 | d2_only | 63 | 53/10 | 3.45% | 1.56% | -9.45% | 0.772 | -0.0175 |
| 7 | ev18_mixed | 64 | 51/13 | 3.29% | 1.38% | -9.73% | 0.767 | -0.0203 |
| 8 | ecmwf_only | 66 | 55/11 | 3.15% | 1.26% | -9.42% | 0.772 | -0.0204 |
| 9 | entry_70_80 | 63 | 50/13 | 2.42% | 0.51% | -11.50% | 0.759 | -0.0352 |
| 10 | d2_entry_72_85 | 59 | 49/10 | 2.27% | 0.39% | -11.93% | 0.777 | -0.0379 |
| 11 | entry_72_82 | 64 | 50/14 | -0.04% | -1.93% | -13.15% | 0.769 | -0.0653 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 42 | 34/8 | 0.48% | -1.38% | -15.21% | 0.777 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 76 | 66/10 | 7.38% | -0.36% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 83 | 71/12 | 5.14% | -3.03% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
