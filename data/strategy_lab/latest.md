# Strategy Lab
Generated: 2026-08-27T09:56:53.098082+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.49%
  - need post-activation ROI after drag >=3%, have -3.99%
  - need positive bootstrap lower bound, have -5.76%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 137 | 110/27 | 3.08% | 1.17% | -6.05% | 0.760 | -0.0095 |
| 2 | current_paper | 160 | 128/32 | 2.39% | 0.49% | -5.76% | 0.767 | -0.0153 |
| 3 | d2_ev15 | 160 | 128/32 | 2.39% | 0.49% | -5.76% | 0.767 | -0.0153 |
| 4 | d2_ecmwf_only | 160 | 128/32 | 2.39% | 0.49% | -5.76% | 0.767 | -0.0153 |
| 5 | ev15_mixed | 171 | 134/37 | 1.65% | -0.24% | -6.49% | 0.766 | -0.0251 |
| 6 | ev18_mixed | 144 | 113/31 | 1.35% | -0.56% | -7.51% | 0.759 | -0.0319 |
| 7 | ecmwf_only | 166 | 132/34 | 0.57% | -1.32% | -8.06% | 0.768 | -0.0414 |
| 8 | d2_only | 163 | 130/33 | 0.67% | -1.22% | -8.56% | 0.768 | -0.0422 |
| 9 | d2_entry_72_85 | 147 | 118/29 | 0.34% | -1.53% | -9.30% | 0.775 | -0.0478 |
| 10 | entry_70_80 | 140 | 108/32 | 0.28% | -1.64% | -9.49% | 0.751 | -0.0496 |
| 11 | entry_72_82 | 136 | 107/29 | -0.21% | -2.11% | -10.01% | 0.763 | -0.0561 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 142 | 111/31 | -2.11% | -3.99% | -10.92% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 176 | 143/33 | 3.28% | -2.16% | 0.762 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 183 | 148/35 | 2.01% | -3.78% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
