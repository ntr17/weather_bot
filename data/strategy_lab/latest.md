# Strategy Lab
Generated: 2026-09-02T16:39:46.438791+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 1.03%
  - need post-activation ROI after drag >=3%, have -3.00%
  - need positive bootstrap lower bound, have -5.24%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 142 | 115/27 | 3.68% | 1.77% | -5.03% | 0.760 | 0.0001 |
| 2 | current_paper | 165 | 133/32 | 2.92% | 1.03% | -5.24% | 0.768 | -0.0080 |
| 3 | d2_ev15 | 165 | 133/32 | 2.92% | 1.03% | -5.24% | 0.768 | -0.0080 |
| 4 | d2_ecmwf_only | 165 | 133/32 | 2.92% | 1.03% | -5.24% | 0.768 | -0.0080 |
| 5 | ev15_mixed | 176 | 139/37 | 2.16% | 0.26% | -5.92% | 0.767 | -0.0181 |
| 6 | ev18_mixed | 149 | 118/31 | 1.97% | 0.06% | -6.67% | 0.760 | -0.0227 |
| 7 | ecmwf_only | 171 | 137/34 | 1.09% | -0.79% | -7.21% | 0.768 | -0.0331 |
| 8 | d2_only | 168 | 135/33 | 1.20% | -0.68% | -7.76% | 0.768 | -0.0340 |
| 9 | d2_entry_72_85 | 152 | 123/29 | 0.93% | -0.94% | -8.27% | 0.775 | -0.0383 |
| 10 | entry_70_80 | 144 | 112/32 | 0.78% | -1.15% | -8.72% | 0.752 | -0.0420 |
| 11 | entry_72_82 | 141 | 112/29 | 0.41% | -1.48% | -9.08% | 0.764 | -0.0466 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 147 | 116/31 | -1.13% | -3.00% | -9.66% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 181 | 148/33 | 3.63% | -1.78% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 188 | 153/35 | 2.36% | -3.46% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
