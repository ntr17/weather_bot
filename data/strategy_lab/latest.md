# Strategy Lab
Generated: 2026-09-03T21:07:03.053124+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.58%
  - need post-activation ROI after drag >=3%, have -3.67%
  - need positive bootstrap lower bound, have -5.86%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 143 | 115/28 | 3.16% | 1.25% | -5.70% | 0.760 | -0.0075 |
| 2 | current_paper | 166 | 133/33 | 2.47% | 0.58% | -5.86% | 0.767 | -0.0147 |
| 3 | d2_ev15 | 166 | 133/33 | 2.47% | 0.58% | -5.86% | 0.767 | -0.0147 |
| 4 | d2_ecmwf_only | 166 | 133/33 | 2.47% | 0.58% | -5.86% | 0.767 | -0.0147 |
| 5 | ev15_mixed | 177 | 139/38 | 1.75% | -0.15% | -6.16% | 0.766 | -0.0231 |
| 6 | ev18_mixed | 150 | 118/32 | 1.48% | -0.43% | -7.15% | 0.759 | -0.0293 |
| 7 | ecmwf_only | 172 | 137/35 | 0.69% | -1.19% | -8.01% | 0.768 | -0.0399 |
| 8 | d2_only | 169 | 135/34 | 0.79% | -1.10% | -8.31% | 0.768 | -0.0401 |
| 9 | d2_entry_72_85 | 153 | 123/30 | 0.49% | -1.39% | -8.74% | 0.775 | -0.0445 |
| 10 | entry_70_80 | 145 | 112/33 | 0.33% | -1.59% | -9.24% | 0.752 | -0.0482 |
| 11 | entry_72_82 | 142 | 112/30 | -0.05% | -1.94% | -9.79% | 0.764 | -0.0537 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 148 | 116/32 | -1.79% | -3.67% | -10.59% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 182 | 148/34 | 3.29% | -2.02% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 189 | 153/36 | 2.05% | -3.78% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
