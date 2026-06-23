# Strategy Lab
Generated: 2026-06-23T10:05:15.218783+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 44
  - need >=30 post-activation resolved trades, have 26
  - need post-activation ROI after drag >=3%, have -8.84%
  - need positive bootstrap lower bound, have -7.32%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 44 | 37/7 | 6.04% | 4.14% | -7.32% | 0.771 | 0.0038 |
| 2 | d2_ev15 | 44 | 37/7 | 6.04% | 4.14% | -7.32% | 0.771 | 0.0038 |
| 3 | d2_ecmwf_only | 44 | 37/7 | 6.04% | 4.14% | -7.32% | 0.771 | 0.0038 |
| 4 | ev15_mixed | 55 | 43/12 | 4.09% | 2.18% | -8.44% | 0.767 | -0.0077 |
| 5 | d2_ev18 | 41 | 34/7 | 5.33% | 3.43% | -9.90% | 0.769 | -0.0184 |
| 6 | ecmwf_only | 50 | 41/9 | 1.99% | 0.10% | -11.80% | 0.772 | -0.0403 |
| 7 | d2_only | 47 | 39/8 | 2.25% | 0.37% | -12.34% | 0.773 | -0.0455 |
| 8 | ev18_mixed | 48 | 37/11 | 1.86% | -0.05% | -12.93% | 0.766 | -0.0498 |
| 9 | entry_70_80 | 50 | 39/11 | 1.60% | -0.32% | -13.81% | 0.759 | -0.0515 |
| 10 | d2_entry_72_85 | 45 | 37/8 | 1.52% | -0.36% | -13.63% | 0.776 | -0.0613 |
| 11 | entry_72_82 | 52 | 40/12 | -0.67% | -2.55% | -15.01% | 0.768 | -0.0780 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 26 | 20/6 | -6.99% | -8.84% | -27.44% | 0.780 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 60 | 52/8 | 7.09% | -1.63% | 0.755 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 67 | 57/10 | 4.71% | -4.18% | 0.756 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
