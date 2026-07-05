# Strategy Lab
Generated: 2026-07-05T19:45:18.160639+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 62
  - need post-activation ROI after drag >=3%, have -0.40%
  - need positive bootstrap lower bound, have -4.45%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 62 | 53/9 | 7.13% | 5.23% | -4.45% | 0.770 | 0.0367 |
| 2 | d2_ev15 | 62 | 53/9 | 7.13% | 5.23% | -4.45% | 0.770 | 0.0367 |
| 3 | d2_ecmwf_only | 62 | 53/9 | 7.13% | 5.23% | -4.45% | 0.770 | 0.0367 |
| 4 | d2_ev18 | 59 | 50/9 | 6.64% | 4.74% | -6.58% | 0.769 | 0.0244 |
| 5 | ev15_mixed | 73 | 59/14 | 5.27% | 3.37% | -6.07% | 0.767 | 0.0125 |
| 6 | d2_only | 65 | 55/10 | 3.71% | 1.82% | -9.16% | 0.772 | -0.0139 |
| 7 | ev18_mixed | 66 | 53/13 | 3.60% | 1.69% | -9.09% | 0.766 | -0.0149 |
| 8 | ecmwf_only | 68 | 57/11 | 3.41% | 1.52% | -9.17% | 0.771 | -0.0169 |
| 9 | entry_70_80 | 65 | 52/13 | 2.69% | 0.78% | -10.60% | 0.759 | -0.0293 |
| 10 | d2_entry_72_85 | 61 | 51/10 | 2.57% | 0.69% | -10.99% | 0.776 | -0.0316 |
| 11 | entry_72_82 | 66 | 52/14 | 0.27% | -1.62% | -13.00% | 0.768 | -0.0617 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 44 | 36/8 | 1.46% | -0.40% | -13.67% | 0.775 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 78 | 68/10 | 7.50% | -0.15% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 85 | 73/12 | 5.27% | -3.22% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
