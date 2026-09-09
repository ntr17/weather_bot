# Strategy Lab
Generated: 2026-09-09T11:31:26.057557+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.05%
  - need post-activation ROI after drag >=3%, have -4.32%
  - need positive bootstrap lower bound, have -6.13%
  - need win rate at least 3 points over avg NO breakeven

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 149 | 119/30 | 2.53% | 0.62% | -5.99% | 0.760 | -0.0148 |
| 2 | current_paper | 172 | 137/35 | 1.94% | 0.05% | -6.13% | 0.768 | -0.0209 |
| 3 | d2_ev15 | 172 | 137/35 | 1.94% | 0.05% | -6.13% | 0.768 | -0.0209 |
| 4 | d2_ecmwf_only | 172 | 137/35 | 1.94% | 0.05% | -6.13% | 0.768 | -0.0209 |
| 5 | ev15_mixed | 183 | 143/40 | 1.28% | -0.62% | -6.71% | 0.767 | -0.0297 |
| 6 | ev18_mixed | 156 | 122/34 | 0.92% | -0.99% | -7.84% | 0.760 | -0.0373 |
| 7 | d2_only | 175 | 139/36 | 0.33% | -1.56% | -8.14% | 0.768 | -0.0441 |
| 8 | ecmwf_only | 178 | 141/37 | 0.25% | -1.64% | -8.07% | 0.768 | -0.0446 |
| 9 | d2_entry_72_85 | 159 | 127/32 | -0.01% | -1.88% | -9.14% | 0.774 | -0.0508 |
| 10 | entry_70_80 | 149 | 114/35 | -0.36% | -2.28% | -10.12% | 0.752 | -0.0582 |
| 11 | entry_72_82 | 148 | 116/32 | -0.54% | -2.44% | -10.32% | 0.764 | -0.0605 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 154 | 120/34 | -2.44% | -4.32% | -11.08% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 188 | 152/36 | 2.84% | -2.55% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 195 | 157/38 | 1.65% | -3.92% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
