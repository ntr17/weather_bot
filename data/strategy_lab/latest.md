# Strategy Lab
Generated: 2026-08-22T18:51:37.301153+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.25%
  - need post-activation ROI after drag >=3%, have -4.47%
  - need positive bootstrap lower bound, have -6.33%
  - need win rate at least 3 points over avg NO breakeven

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 134 | 107/27 | 2.82% | 0.90% | -6.55% | 0.759 | -0.0139 |
| 2 | current_paper | 157 | 125/32 | 2.15% | 0.25% | -6.33% | 0.767 | -0.0197 |
| 3 | d2_ev15 | 157 | 125/32 | 2.15% | 0.25% | -6.33% | 0.767 | -0.0197 |
| 4 | d2_ecmwf_only | 157 | 125/32 | 2.15% | 0.25% | -6.33% | 0.767 | -0.0197 |
| 5 | ev15_mixed | 168 | 131/37 | 1.43% | -0.47% | -6.98% | 0.766 | -0.0291 |
| 6 | ev18_mixed | 141 | 110/31 | 1.07% | -0.84% | -7.93% | 0.758 | -0.0362 |
| 7 | ecmwf_only | 163 | 129/34 | 0.33% | -1.56% | -8.37% | 0.767 | -0.0449 |
| 8 | d2_only | 160 | 127/33 | 0.42% | -1.47% | -8.76% | 0.767 | -0.0454 |
| 9 | d2_entry_72_85 | 144 | 115/29 | 0.07% | -1.80% | -9.38% | 0.774 | -0.0508 |
| 10 | entry_70_80 | 138 | 106/32 | 0.10% | -1.82% | -9.77% | 0.751 | -0.0524 |
| 11 | entry_72_82 | 134 | 105/29 | -0.40% | -2.30% | -10.06% | 0.763 | -0.0582 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 139 | 108/31 | -2.59% | -4.47% | -11.64% | 0.768 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 173 | 140/33 | 3.13% | -2.58% | 0.762 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 180 | 145/35 | 1.86% | -4.05% | 0.762 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
