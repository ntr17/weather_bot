# Strategy Lab
Generated: 2026-10-08T23:26:19.540341+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `unknown`
- Live blockers:
  - need >=30 post-activation resolved trades, have 0
  - need >=3% ROI after fee/spread drag, have 0.02%
  - need positive bootstrap lower bound, have -6.58%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 160 | 127/33 | 1.92% | 0.02% | -6.58% | 0.762 | -0.0228 |
| 2 | d2_ev18 | 160 | 127/33 | 1.92% | 0.02% | -6.58% | 0.762 | -0.0228 |
| 3 | d2_ev15 | 185 | 147/38 | 1.55% | -0.34% | -6.39% | 0.769 | -0.0258 |
| 4 | d2_ecmwf_only | 185 | 147/38 | 1.55% | -0.34% | -6.39% | 0.769 | -0.0258 |
| 5 | ev15_mixed | 196 | 153/43 | 0.94% | -0.95% | -6.48% | 0.768 | -0.0322 |
| 6 | ev18_mixed | 167 | 130/37 | 0.41% | -1.50% | -8.11% | 0.761 | -0.0434 |
| 7 | ecmwf_only | 191 | 151/40 | -0.03% | -1.92% | -7.97% | 0.770 | -0.0471 |
| 8 | d2_only | 188 | 149/39 | 0.04% | -1.84% | -8.28% | 0.770 | -0.0474 |
| 9 | d2_entry_72_85 | 172 | 137/35 | -0.30% | -2.17% | -9.07% | 0.776 | -0.0534 |
| 10 | entry_72_82 | 159 | 124/35 | -0.95% | -2.85% | -9.98% | 0.765 | -0.0634 |
| 11 | entry_70_80 | 157 | 119/38 | -1.06% | -2.98% | -10.53% | 0.753 | -0.0667 |
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
| D+2 | 201 | 162/39 | 2.44% | -2.76% | 0.765 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 208 | 167/41 | 1.32% | -4.05% | 0.765 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
