# Strategy Lab
Generated: 2026-09-06T20:29:04.512729+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.36%
  - need post-activation ROI after drag >=3%, have -3.90%
  - need positive bootstrap lower bound, have -5.75%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 147 | 118/29 | 2.89% | 0.98% | -5.67% | 0.761 | -0.0100 |
| 2 | current_paper | 170 | 136/34 | 2.25% | 0.36% | -5.75% | 0.768 | -0.0165 |
| 3 | d2_ev15 | 170 | 136/34 | 2.25% | 0.36% | -5.75% | 0.768 | -0.0165 |
| 4 | d2_ecmwf_only | 170 | 136/34 | 2.25% | 0.36% | -5.75% | 0.768 | -0.0165 |
| 5 | ev15_mixed | 181 | 142/39 | 1.56% | -0.34% | -6.51% | 0.767 | -0.0262 |
| 6 | ev18_mixed | 154 | 121/33 | 1.25% | -0.66% | -7.67% | 0.760 | -0.0335 |
| 7 | ecmwf_only | 176 | 140/36 | 0.52% | -1.37% | -7.74% | 0.768 | -0.0408 |
| 8 | d2_only | 173 | 138/35 | 0.61% | -1.28% | -8.17% | 0.768 | -0.0414 |
| 9 | d2_entry_72_85 | 157 | 126/31 | 0.29% | -1.58% | -8.64% | 0.775 | -0.0460 |
| 10 | entry_70_80 | 147 | 113/34 | -0.06% | -1.98% | -9.47% | 0.752 | -0.0529 |
| 11 | entry_72_82 | 146 | 115/31 | -0.24% | -2.13% | -9.79% | 0.764 | -0.0556 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 152 | 119/33 | -2.02% | -3.90% | -10.63% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 186 | 151/35 | 3.09% | -2.07% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 193 | 156/37 | 1.87% | -4.00% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
