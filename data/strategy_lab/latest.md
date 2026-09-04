# Strategy Lab
Generated: 2026-09-04T20:49:26.507813+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.22%
  - need post-activation ROI after drag >=3%, have -4.17%
  - need positive bootstrap lower bound, have -5.89%
  - need win rate at least 3 points over avg NO breakeven

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 145 | 116/29 | 2.74% | 0.83% | -5.90% | 0.760 | -0.0123 |
| 2 | current_paper | 168 | 134/34 | 2.11% | 0.22% | -5.89% | 0.768 | -0.0184 |
| 3 | d2_ev15 | 168 | 134/34 | 2.11% | 0.22% | -5.89% | 0.768 | -0.0184 |
| 4 | d2_ecmwf_only | 168 | 134/34 | 2.11% | 0.22% | -5.89% | 0.768 | -0.0184 |
| 5 | ev15_mixed | 179 | 140/39 | 1.43% | -0.47% | -6.56% | 0.767 | -0.0277 |
| 6 | ev18_mixed | 152 | 119/33 | 1.09% | -0.82% | -7.81% | 0.760 | -0.0355 |
| 7 | ecmwf_only | 174 | 138/36 | 0.38% | -1.51% | -7.97% | 0.768 | -0.0430 |
| 8 | d2_only | 171 | 136/35 | 0.47% | -1.42% | -8.28% | 0.768 | -0.0432 |
| 9 | d2_entry_72_85 | 155 | 124/31 | 0.14% | -1.74% | -8.86% | 0.775 | -0.0484 |
| 10 | entry_70_80 | 146 | 112/34 | -0.11% | -2.04% | -9.67% | 0.752 | -0.0542 |
| 11 | entry_72_82 | 144 | 113/31 | -0.40% | -2.30% | -9.81% | 0.764 | -0.0573 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 150 | 117/33 | -2.29% | -4.17% | -10.76% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 184 | 149/35 | 3.01% | -2.43% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 191 | 154/37 | 1.79% | -3.96% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
