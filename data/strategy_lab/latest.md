# Strategy Lab
Generated: 2026-06-19T05:28:19.060878+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 37
  - need >=30 post-activation resolved trades, have 19
  - need post-activation ROI after drag >=3%, have 0.50%
  - need positive bootstrap lower bound, have -5.15%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 37 | 33/4 | 8.70% | 6.79% | -5.15% | 0.767 | 0.0239 |
| 2 | d2_ev15 | 37 | 33/4 | 8.70% | 6.79% | -5.15% | 0.767 | 0.0239 |
| 3 | d2_ecmwf_only | 37 | 33/4 | 8.70% | 6.79% | -5.15% | 0.767 | 0.0239 |
| 4 | ev15_mixed | 48 | 39/9 | 6.21% | 4.30% | -6.43% | 0.763 | 0.0165 |
| 5 | d2_ev18 | 35 | 31/4 | 8.31% | 6.40% | -7.51% | 0.767 | 0.0077 |
| 6 | ev18_mixed | 42 | 34/8 | 4.40% | 2.49% | -10.43% | 0.763 | -0.0276 |
| 7 | ecmwf_only | 43 | 37/6 | 3.94% | 2.05% | -10.51% | 0.769 | -0.0303 |
| 8 | d2_only | 40 | 35/5 | 4.34% | 2.45% | -11.06% | 0.769 | -0.0342 |
| 9 | entry_70_80 | 46 | 37/9 | 2.84% | 0.93% | -12.20% | 0.759 | -0.0414 |
| 10 | d2_entry_72_85 | 38 | 33/5 | 3.67% | 1.79% | -12.04% | 0.773 | -0.0482 |
| 11 | entry_72_82 | 48 | 38/10 | 0.52% | -1.36% | -14.19% | 0.769 | -0.0673 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | 16/3 | 2.36% | 0.50% | -18.88% | 0.776 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 53 | 48/5 | 8.69% | -0.31% | 0.751 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 60 | 53/7 | 6.05% | -2.74% | 0.752 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
