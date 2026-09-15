# Strategy Lab
Generated: 2026-09-15T05:00:20.145554+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.03%
  - need post-activation ROI after drag >=3%, have -4.18%
  - need positive bootstrap lower bound, have -5.78%
  - need win rate at least 3 points over avg NO breakeven

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 153 | 122/31 | 2.37% | 0.46% | -6.38% | 0.761 | -0.0177 |
| 2 | current_paper | 178 | 142/36 | 1.92% | 0.03% | -5.78% | 0.769 | -0.0199 |
| 3 | d2_ev15 | 178 | 142/36 | 1.92% | 0.03% | -5.78% | 0.769 | -0.0199 |
| 4 | d2_ecmwf_only | 178 | 142/36 | 1.92% | 0.03% | -5.78% | 0.769 | -0.0199 |
| 5 | ev15_mixed | 189 | 148/41 | 1.28% | -0.62% | -6.72% | 0.768 | -0.0297 |
| 6 | ev18_mixed | 160 | 125/35 | 0.79% | -1.12% | -7.53% | 0.760 | -0.0376 |
| 7 | ecmwf_only | 184 | 146/38 | 0.27% | -1.61% | -7.72% | 0.769 | -0.0431 |
| 8 | d2_only | 181 | 144/37 | 0.35% | -1.53% | -8.41% | 0.769 | -0.0447 |
| 9 | d2_entry_72_85 | 165 | 132/33 | 0.03% | -1.85% | -8.81% | 0.775 | -0.0493 |
| 10 | entry_72_82 | 152 | 119/33 | -0.63% | -2.53% | -10.00% | 0.764 | -0.0603 |
| 11 | entry_70_80 | 151 | 115/36 | -0.65% | -2.57% | -10.27% | 0.751 | -0.0616 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 160 | 125/35 | -2.30% | -4.18% | -10.57% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 194 | 157/37 | 2.78% | -2.58% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 201 | 162/39 | 1.61% | -3.80% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
