# Strategy Lab
Generated: 2026-09-18T11:24:13.765817+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.21%
  - need post-activation ROI after drag >=3%, have -3.86%
  - need positive bootstrap lower bound, have -5.87%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 155 | 124/31 | 2.57% | 0.67% | -6.23% | 0.761 | -0.0151 |
| 2 | current_paper | 180 | 144/36 | 2.10% | 0.21% | -5.87% | 0.769 | -0.0184 |
| 3 | d2_ev15 | 180 | 144/36 | 2.10% | 0.21% | -5.87% | 0.769 | -0.0184 |
| 4 | d2_ecmwf_only | 180 | 144/36 | 2.10% | 0.21% | -5.87% | 0.769 | -0.0184 |
| 5 | ev15_mixed | 191 | 150/41 | 1.45% | -0.45% | -6.50% | 0.768 | -0.0272 |
| 6 | ev18_mixed | 162 | 127/35 | 1.00% | -0.90% | -7.56% | 0.760 | -0.0355 |
| 7 | d2_only | 183 | 146/37 | 0.53% | -1.35% | -7.83% | 0.769 | -0.0409 |
| 8 | ecmwf_only | 186 | 148/38 | 0.45% | -1.44% | -7.68% | 0.769 | -0.0413 |
| 9 | d2_entry_72_85 | 167 | 134/33 | 0.23% | -1.65% | -8.47% | 0.775 | -0.0461 |
| 10 | entry_72_82 | 154 | 121/33 | -0.42% | -2.31% | -9.61% | 0.764 | -0.0567 |
| 11 | entry_70_80 | 153 | 117/36 | -0.44% | -2.36% | -10.09% | 0.752 | -0.0589 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 162 | 127/35 | -1.98% | -3.86% | -10.21% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 196 | 159/37 | 2.90% | -2.38% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 203 | 164/39 | 1.73% | -3.84% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
