# Strategy Lab
Generated: 2026-09-13T04:55:20.283984+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.37%
  - need post-activation ROI after drag >=3%, have -3.72%
  - need positive bootstrap lower bound, have -5.61%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 151 | 121/30 | 2.76% | 0.86% | -5.84% | 0.761 | -0.0118 |
| 2 | current_paper | 176 | 141/35 | 2.26% | 0.37% | -5.61% | 0.769 | -0.0159 |
| 3 | d2_ev15 | 176 | 141/35 | 2.26% | 0.37% | -5.61% | 0.769 | -0.0159 |
| 4 | d2_ecmwf_only | 176 | 141/35 | 2.26% | 0.37% | -5.61% | 0.769 | -0.0159 |
| 5 | ev15_mixed | 187 | 147/40 | 1.58% | -0.31% | -6.15% | 0.768 | -0.0246 |
| 6 | ev18_mixed | 158 | 124/34 | 1.16% | -0.75% | -7.34% | 0.760 | -0.0332 |
| 7 | ecmwf_only | 182 | 145/37 | 0.56% | -1.32% | -7.47% | 0.769 | -0.0393 |
| 8 | d2_only | 179 | 143/36 | 0.66% | -1.23% | -7.91% | 0.769 | -0.0400 |
| 9 | d2_entry_72_85 | 163 | 131/32 | 0.35% | -1.52% | -8.69% | 0.775 | -0.0456 |
| 10 | entry_72_82 | 150 | 118/32 | -0.30% | -2.19% | -9.51% | 0.764 | -0.0552 |
| 11 | entry_70_80 | 150 | 115/35 | -0.21% | -2.14% | -9.72% | 0.752 | -0.0554 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 158 | 124/34 | -1.85% | -3.72% | -10.12% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 192 | 156/36 | 3.05% | -2.49% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 199 | 161/38 | 1.86% | -3.73% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
