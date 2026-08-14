# Strategy Lab
Generated: 2026-08-14T02:48:50.680477+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.36%
  - need post-activation ROI after drag >=3%, have -1.54%
  - need positive bootstrap lower bound, have -4.53%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 142 | 116/26 | 4.26% | 2.36% | -4.53% | 0.764 | 0.0077 |
| 2 | d2_ev15 | 142 | 116/26 | 4.26% | 2.36% | -4.53% | 0.764 | 0.0077 |
| 3 | d2_ecmwf_only | 142 | 116/26 | 4.26% | 2.36% | -4.53% | 0.764 | 0.0077 |
| 4 | d2_ev18 | 125 | 102/23 | 4.51% | 2.60% | -5.29% | 0.758 | 0.0075 |
| 5 | ev15_mixed | 153 | 122/31 | 3.31% | 1.40% | -5.35% | 0.763 | -0.0047 |
| 6 | ev18_mixed | 132 | 105/27 | 2.62% | 0.70% | -6.80% | 0.757 | -0.0168 |
| 7 | d2_only | 145 | 118/27 | 2.27% | 0.38% | -7.32% | 0.765 | -0.0218 |
| 8 | ecmwf_only | 148 | 120/28 | 2.12% | 0.22% | -6.93% | 0.765 | -0.0221 |
| 9 | d2_entry_72_85 | 129 | 106/23 | 2.08% | 0.20% | -7.31% | 0.772 | -0.0236 |
| 10 | entry_70_80 | 129 | 101/28 | 1.38% | -0.55% | -8.46% | 0.751 | -0.0351 |
| 11 | entry_72_82 | 125 | 100/25 | 0.90% | -0.99% | -9.17% | 0.763 | -0.0420 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 124 | 99/25 | 0.35% | -1.54% | -8.70% | 0.765 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 158 | 131/27 | 4.80% | -0.99% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 165 | 136/29 | 3.34% | -2.53% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
