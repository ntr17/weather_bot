# Strategy Lab
Generated: 2026-08-26T13:20:43.919611+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.38%
  - need post-activation ROI after drag >=3%, have -4.19%
  - need positive bootstrap lower bound, have -6.29%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 136 | 109/27 | 2.96% | 1.05% | -6.14% | 0.759 | -0.0110 |
| 2 | current_paper | 159 | 127/32 | 2.28% | 0.38% | -6.29% | 0.767 | -0.0182 |
| 3 | d2_ev15 | 159 | 127/32 | 2.28% | 0.38% | -6.29% | 0.767 | -0.0182 |
| 4 | d2_ecmwf_only | 159 | 127/32 | 2.28% | 0.38% | -6.29% | 0.767 | -0.0182 |
| 5 | ev15_mixed | 170 | 133/37 | 1.55% | -0.35% | -6.56% | 0.766 | -0.0265 |
| 6 | ev18_mixed | 143 | 112/31 | 1.23% | -0.69% | -7.67% | 0.759 | -0.0337 |
| 7 | d2_only | 162 | 129/33 | 0.56% | -1.33% | -8.28% | 0.768 | -0.0423 |
| 8 | ecmwf_only | 165 | 131/34 | 0.46% | -1.42% | -8.31% | 0.768 | -0.0433 |
| 9 | d2_entry_72_85 | 146 | 117/29 | 0.22% | -1.65% | -9.04% | 0.775 | -0.0481 |
| 10 | entry_70_80 | 139 | 107/32 | 0.16% | -1.76% | -9.54% | 0.751 | -0.0510 |
| 11 | entry_72_82 | 135 | 106/29 | -0.34% | -2.23% | -9.90% | 0.763 | -0.0570 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 141 | 110/31 | -2.31% | -4.19% | -11.38% | 0.768 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 175 | 142/33 | 3.21% | -2.31% | 0.762 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 182 | 147/35 | 1.94% | -3.79% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
