# Strategy Lab
Generated: 2026-09-01T11:45:35.792223+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.94%
  - need post-activation ROI after drag >=3%, have -3.16%
  - need positive bootstrap lower bound, have -5.53%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 141 | 114/27 | 3.59% | 1.68% | -5.36% | 0.760 | -0.0020 |
| 2 | current_paper | 164 | 132/32 | 2.84% | 0.94% | -5.53% | 0.767 | -0.0100 |
| 3 | d2_ev15 | 164 | 132/32 | 2.84% | 0.94% | -5.53% | 0.767 | -0.0100 |
| 4 | d2_ecmwf_only | 164 | 132/32 | 2.84% | 0.94% | -5.53% | 0.767 | -0.0100 |
| 5 | ev15_mixed | 175 | 138/37 | 2.08% | 0.18% | -6.24% | 0.766 | -0.0200 |
| 6 | ev18_mixed | 148 | 117/31 | 1.88% | -0.04% | -7.04% | 0.759 | -0.0250 |
| 7 | ecmwf_only | 170 | 136/34 | 1.01% | -0.88% | -7.32% | 0.768 | -0.0344 |
| 8 | d2_only | 167 | 134/33 | 1.12% | -0.77% | -7.73% | 0.768 | -0.0348 |
| 9 | d2_entry_72_85 | 151 | 122/29 | 0.84% | -1.03% | -8.55% | 0.775 | -0.0402 |
| 10 | entry_70_80 | 144 | 112/32 | 0.78% | -1.15% | -8.72% | 0.752 | -0.0420 |
| 11 | entry_72_82 | 140 | 111/29 | 0.31% | -1.58% | -9.02% | 0.763 | -0.0474 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 146 | 115/31 | -1.28% | -3.16% | -10.20% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 180 | 147/33 | 3.58% | -1.89% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 187 | 152/35 | 2.30% | -3.44% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
