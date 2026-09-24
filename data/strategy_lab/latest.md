# Strategy Lab
Generated: 2026-09-24T21:35:29.728357+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `unknown`
- Live blockers:
  - need >=30 post-activation resolved trades, have 0
  - need >=3% ROI after fee/spread drag, have 0.49%
  - need positive bootstrap lower bound, have -6.10%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 159 | 127/32 | 2.40% | 0.49% | -6.10% | 0.762 | -0.0164 |
| 2 | d2_ev18 | 159 | 127/32 | 2.40% | 0.49% | -6.10% | 0.762 | -0.0164 |
| 3 | d2_ev15 | 184 | 147/37 | 1.96% | 0.07% | -5.79% | 0.769 | -0.0196 |
| 4 | d2_ecmwf_only | 184 | 147/37 | 1.96% | 0.07% | -5.79% | 0.769 | -0.0196 |
| 5 | ev15_mixed | 195 | 153/42 | 1.32% | -0.57% | -6.48% | 0.768 | -0.0284 |
| 6 | ev18_mixed | 166 | 130/36 | 0.86% | -1.05% | -7.74% | 0.761 | -0.0376 |
| 7 | ecmwf_only | 190 | 151/39 | 0.34% | -1.55% | -7.44% | 0.770 | -0.0415 |
| 8 | d2_only | 187 | 149/38 | 0.42% | -1.46% | -8.08% | 0.770 | -0.0429 |
| 9 | d2_entry_72_85 | 171 | 137/34 | 0.11% | -1.76% | -8.55% | 0.776 | -0.0475 |
| 10 | entry_72_82 | 158 | 124/34 | -0.53% | -2.42% | -9.58% | 0.765 | -0.0577 |
| 11 | entry_70_80 | 156 | 119/37 | -0.64% | -2.56% | -10.01% | 0.753 | -0.0606 |
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
| D+2 | 200 | 162/38 | 2.75% | -2.26% | 0.765 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 207 | 167/40 | 1.61% | -3.65% | 0.765 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
