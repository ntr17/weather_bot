# Strategy Lab
Generated: 2026-06-12T20:29:11.090013+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 20
  - need >=30 post-activation resolved trades, have 2
  - need positive bootstrap lower bound, have -5.80%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 20 | 19/1 | 10.28% | 8.36% | -5.80% | 0.759 | 0.0033 |
| 2 | d2_ev15 | 20 | 19/1 | 10.28% | 8.36% | -5.80% | 0.759 | 0.0033 |
| 3 | d2_ecmwf_only | 20 | 19/1 | 10.28% | 8.36% | -5.80% | 0.759 | 0.0033 |
| 4 | ev15_mixed | 31 | 25/6 | 7.08% | 5.16% | -7.09% | 0.757 | -0.0112 |
| 5 | d2_ev18 | 18 | 17/1 | 10.01% | 8.09% | -8.10% | 0.758 | -0.0115 |
| 6 | ev18_mixed | 25 | 20/5 | 5.13% | 3.21% | -13.01% | 0.754 | -0.0634 |
| 7 | d2_only | 23 | 21/2 | 4.94% | 3.04% | -11.89% | 0.765 | -0.0652 |
| 8 | ecmwf_only | 26 | 23/3 | 4.43% | 2.53% | -12.27% | 0.764 | -0.0656 |
| 9 | entry_70_80 | 34 | 27/7 | 2.83% | 0.92% | -14.00% | 0.759 | -0.0718 |
| 10 | d2_entry_72_85 | 22 | 20/2 | 4.59% | 2.70% | -13.28% | 0.768 | -0.0755 |
| 11 | entry_72_82 | 33 | 26/7 | 1.04% | -0.85% | -15.20% | 0.765 | -0.0957 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 2/0 | 14.90% | 13.03% | 14.00% | 0.775 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 36 | 34/2 | 9.69% | 0.03% | 0.739 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 43 | 39/4 | 6.68% | -3.18% | 0.742 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
