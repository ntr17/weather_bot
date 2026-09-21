# Strategy Lab
Generated: 2026-09-21T05:04:58.007871+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `unknown`
- Live blockers:
  - need >=30 post-activation resolved trades, have 0
  - need >=3% ROI after fee/spread drag, have 0.28%
  - need positive bootstrap lower bound, have -6.35%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 157 | 125/32 | 2.19% | 0.28% | -6.35% | 0.761 | -0.0194 |
| 2 | d2_ev18 | 157 | 125/32 | 2.19% | 0.28% | -6.35% | 0.761 | -0.0194 |
| 3 | d2_ev15 | 182 | 145/37 | 1.77% | -0.12% | -6.01% | 0.769 | -0.0222 |
| 4 | d2_ecmwf_only | 182 | 145/37 | 1.77% | -0.12% | -6.01% | 0.769 | -0.0222 |
| 5 | ev15_mixed | 193 | 151/42 | 1.14% | -0.75% | -6.53% | 0.768 | -0.0303 |
| 6 | ev18_mixed | 164 | 128/36 | 0.64% | -1.27% | -7.92% | 0.761 | -0.0404 |
| 7 | ecmwf_only | 188 | 149/39 | 0.15% | -1.73% | -7.90% | 0.769 | -0.0449 |
| 8 | d2_only | 185 | 147/38 | 0.23% | -1.65% | -8.26% | 0.769 | -0.0454 |
| 9 | d2_entry_72_85 | 169 | 135/34 | -0.10% | -1.97% | -8.97% | 0.776 | -0.0511 |
| 10 | entry_72_82 | 156 | 122/34 | -0.75% | -2.64% | -10.06% | 0.765 | -0.0616 |
| 11 | entry_70_80 | 154 | 117/37 | -0.86% | -2.78% | -10.31% | 0.752 | -0.0639 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 198 | 160/38 | 2.63% | -2.62% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 205 | 165/40 | 1.49% | -3.89% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
