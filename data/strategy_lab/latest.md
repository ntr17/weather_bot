# Strategy Lab
Generated: 2026-08-05T19:58:48.500481+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 2.33%
  - need post-activation ROI after drag >=3%, have -2.29%
  - need positive bootstrap lower bound, have -4.99%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 108 | 88/20 | 4.71% | 2.80% | -5.89% | 0.759 | 0.0074 |
| 2 | current_paper | 123 | 100/23 | 4.23% | 2.33% | -4.99% | 0.765 | 0.0058 |
| 3 | d2_ev15 | 123 | 100/23 | 4.23% | 2.33% | -4.99% | 0.765 | 0.0058 |
| 4 | d2_ecmwf_only | 123 | 100/23 | 4.23% | 2.33% | -4.99% | 0.765 | 0.0058 |
| 5 | ev15_mixed | 134 | 106/28 | 3.20% | 1.29% | -5.97% | 0.764 | -0.0080 |
| 6 | ev18_mixed | 115 | 91/24 | 2.62% | 0.71% | -7.43% | 0.758 | -0.0189 |
| 7 | d2_only | 126 | 102/24 | 2.06% | 0.17% | -7.82% | 0.766 | -0.0257 |
| 8 | ecmwf_only | 129 | 104/25 | 1.90% | 0.01% | -7.39% | 0.766 | -0.0258 |
| 9 | d2_entry_72_85 | 113 | 92/21 | 1.71% | -0.17% | -8.65% | 0.773 | -0.0320 |
| 10 | entry_70_80 | 113 | 88/25 | 1.33% | -0.60% | -9.21% | 0.751 | -0.0382 |
| 11 | entry_72_82 | 110 | 87/23 | 0.53% | -1.36% | -9.87% | 0.763 | -0.0481 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 105 | 83/22 | -0.40% | -2.29% | -10.23% | 0.766 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 139 | 115/24 | 4.95% | -1.34% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 146 | 120/26 | 3.39% | -2.96% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
