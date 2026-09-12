# Strategy Lab
Generated: 2026-09-12T20:38:34.766291+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.32%
  - need post-activation ROI after drag >=3%, have -3.82%
  - need positive bootstrap lower bound, have -5.90%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 151 | 121/30 | 2.76% | 0.86% | -5.84% | 0.761 | -0.0118 |
| 2 | current_paper | 175 | 140/35 | 2.21% | 0.32% | -5.90% | 0.768 | -0.0175 |
| 3 | d2_ev15 | 175 | 140/35 | 2.21% | 0.32% | -5.90% | 0.768 | -0.0175 |
| 4 | d2_ecmwf_only | 175 | 140/35 | 2.21% | 0.32% | -5.90% | 0.768 | -0.0175 |
| 5 | ev15_mixed | 186 | 146/40 | 1.54% | -0.36% | -6.28% | 0.767 | -0.0256 |
| 6 | ev18_mixed | 158 | 124/34 | 1.16% | -0.75% | -7.34% | 0.760 | -0.0332 |
| 7 | d2_only | 178 | 142/36 | 0.61% | -1.28% | -7.88% | 0.769 | -0.0404 |
| 8 | ecmwf_only | 181 | 144/37 | 0.52% | -1.37% | -7.78% | 0.769 | -0.0409 |
| 9 | d2_entry_72_85 | 162 | 130/32 | 0.30% | -1.57% | -8.33% | 0.775 | -0.0449 |
| 10 | entry_72_82 | 150 | 118/32 | -0.30% | -2.19% | -9.51% | 0.764 | -0.0552 |
| 11 | entry_70_80 | 150 | 115/35 | -0.21% | -2.14% | -9.72% | 0.752 | -0.0554 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 157 | 123/34 | -1.94% | -3.82% | -10.33% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 191 | 155/36 | 3.02% | -2.13% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 198 | 160/38 | 1.83% | -3.53% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
