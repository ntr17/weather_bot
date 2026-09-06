# Strategy Lab
Generated: 2026-09-06T04:46:51.587287+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.32%
  - need post-activation ROI after drag >=3%, have -4.00%
  - need positive bootstrap lower bound, have -5.70%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 146 | 117/29 | 2.84% | 0.94% | -5.91% | 0.761 | -0.0113 |
| 2 | current_paper | 169 | 135/34 | 2.21% | 0.32% | -5.70% | 0.768 | -0.0168 |
| 3 | d2_ev15 | 169 | 135/34 | 2.21% | 0.32% | -5.70% | 0.768 | -0.0168 |
| 4 | d2_ecmwf_only | 169 | 135/34 | 2.21% | 0.32% | -5.70% | 0.768 | -0.0168 |
| 5 | ev15_mixed | 180 | 141/39 | 1.51% | -0.38% | -6.53% | 0.767 | -0.0267 |
| 6 | ev18_mixed | 153 | 120/33 | 1.20% | -0.71% | -7.39% | 0.760 | -0.0330 |
| 7 | ecmwf_only | 175 | 139/36 | 0.47% | -1.42% | -8.02% | 0.768 | -0.0423 |
| 8 | d2_only | 172 | 137/35 | 0.56% | -1.32% | -8.33% | 0.768 | -0.0423 |
| 9 | d2_entry_72_85 | 156 | 125/31 | 0.24% | -1.63% | -8.70% | 0.775 | -0.0467 |
| 10 | entry_70_80 | 146 | 112/34 | -0.11% | -2.04% | -9.67% | 0.752 | -0.0542 |
| 11 | entry_72_82 | 145 | 114/31 | -0.30% | -2.19% | -9.84% | 0.764 | -0.0563 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 151 | 118/33 | -2.12% | -4.00% | -10.50% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 185 | 150/35 | 3.07% | -2.53% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 192 | 155/37 | 1.85% | -3.72% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
