# Strategy Lab
Generated: 2026-08-20T13:14:38.447055+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.65%
  - need post-activation ROI after drag >=3%, have -3.90%
  - need positive bootstrap lower bound, have -6.01%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 133 | 107/26 | 3.36% | 1.45% | -6.12% | 0.759 | -0.0069 |
| 2 | current_paper | 155 | 124/31 | 2.54% | 0.65% | -6.01% | 0.766 | -0.0145 |
| 3 | d2_ev15 | 155 | 124/31 | 2.54% | 0.65% | -6.01% | 0.766 | -0.0145 |
| 4 | d2_ecmwf_only | 155 | 124/31 | 2.54% | 0.65% | -6.01% | 0.766 | -0.0145 |
| 5 | ev15_mixed | 166 | 130/36 | 1.78% | -0.12% | -6.62% | 0.765 | -0.0244 |
| 6 | ev18_mixed | 140 | 110/30 | 1.59% | -0.33% | -7.30% | 0.758 | -0.0289 |
| 7 | ecmwf_only | 161 | 128/33 | 0.68% | -1.21% | -7.80% | 0.767 | -0.0394 |
| 8 | d2_only | 158 | 126/32 | 0.78% | -1.11% | -8.84% | 0.767 | -0.0420 |
| 9 | entry_70_80 | 137 | 106/31 | 0.56% | -1.36% | -8.99% | 0.751 | -0.0451 |
| 10 | d2_entry_72_85 | 142 | 114/28 | 0.46% | -1.42% | -9.07% | 0.774 | -0.0459 |
| 11 | entry_72_82 | 133 | 105/28 | 0.07% | -1.82% | -9.46% | 0.763 | -0.0513 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 137 | 107/30 | -2.02% | -3.90% | -11.20% | 0.767 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 171 | 139/32 | 3.44% | -2.09% | 0.761 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 178 | 144/34 | 2.14% | -3.78% | 0.761 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
