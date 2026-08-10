# Strategy Lab
Generated: 2026-08-10T13:48:19.895928+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.63%
  - need post-activation ROI after drag >=3%, have -1.42%
  - need positive bootstrap lower bound, have -4.22%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 132 | 108/24 | 4.53% | 2.63% | -4.22% | 0.766 | 0.0115 |
| 2 | d2_ev15 | 132 | 108/24 | 4.53% | 2.63% | -4.22% | 0.766 | 0.0115 |
| 3 | d2_ecmwf_only | 132 | 108/24 | 4.53% | 2.63% | -4.22% | 0.766 | 0.0115 |
| 4 | d2_ev18 | 115 | 94/21 | 4.84% | 2.92% | -5.21% | 0.759 | 0.0110 |
| 5 | ev15_mixed | 143 | 114/29 | 3.51% | 1.61% | -5.32% | 0.765 | -0.0025 |
| 6 | ev18_mixed | 122 | 97/25 | 2.82% | 0.91% | -7.13% | 0.758 | -0.0158 |
| 7 | ecmwf_only | 138 | 112/26 | 2.26% | 0.37% | -7.06% | 0.766 | -0.0210 |
| 8 | d2_only | 135 | 110/25 | 2.43% | 0.54% | -7.70% | 0.766 | -0.0215 |
| 9 | d2_entry_72_85 | 121 | 99/22 | 1.91% | 0.03% | -8.38% | 0.774 | -0.0290 |
| 10 | entry_70_80 | 120 | 94/26 | 1.55% | -0.37% | -8.48% | 0.752 | -0.0334 |
| 11 | entry_72_82 | 117 | 93/24 | 0.69% | -1.21% | -9.60% | 0.764 | -0.0457 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 114 | 91/23 | 0.47% | -1.42% | -9.19% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 148 | 123/25 | 5.08% | -0.99% | 0.760 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 155 | 128/27 | 3.55% | -2.69% | 0.760 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
