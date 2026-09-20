# Strategy Lab
Generated: 2026-09-20T16:13:33.501092+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `unknown`
- Live blockers:
  - need >=30 post-activation resolved trades, have 0
  - need >=3% ROI after fee/spread drag, have 0.18%
  - need positive bootstrap lower bound, have -6.32%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 156 | 124/32 | 2.09% | 0.18% | -6.32% | 0.761 | -0.0203 |
| 2 | d2_ev18 | 156 | 124/32 | 2.09% | 0.18% | -6.32% | 0.761 | -0.0203 |
| 3 | d2_ev15 | 181 | 144/37 | 1.69% | -0.20% | -6.38% | 0.769 | -0.0243 |
| 4 | d2_ecmwf_only | 181 | 144/37 | 1.69% | -0.20% | -6.38% | 0.769 | -0.0243 |
| 5 | ev15_mixed | 192 | 150/42 | 1.06% | -0.83% | -6.71% | 0.768 | -0.0318 |
| 6 | ev18_mixed | 163 | 127/36 | 0.54% | -1.37% | -8.18% | 0.760 | -0.0423 |
| 7 | ecmwf_only | 187 | 148/39 | 0.07% | -1.81% | -7.89% | 0.769 | -0.0457 |
| 8 | d2_only | 184 | 146/38 | 0.15% | -1.74% | -8.59% | 0.769 | -0.0475 |
| 9 | d2_entry_72_85 | 168 | 134/34 | -0.19% | -2.06% | -8.76% | 0.775 | -0.0513 |
| 10 | entry_72_82 | 155 | 121/34 | -0.85% | -2.74% | -10.01% | 0.764 | -0.0624 |
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
| D+2 | 197 | 159/38 | 2.57% | -2.64% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 204 | 164/40 | 1.43% | -4.11% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
