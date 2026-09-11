# Strategy Lab
Generated: 2026-09-11T11:29:52.690724+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.12%
  - need post-activation ROI after drag >=3%, have -4.19%
  - need positive bootstrap lower bound, have -6.09%
  - need win rate at least 3 points over avg NO breakeven

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 149 | 119/30 | 2.53% | 0.62% | -5.99% | 0.760 | -0.0148 |
| 2 | current_paper | 173 | 138/35 | 2.01% | 0.12% | -6.09% | 0.768 | -0.0201 |
| 3 | d2_ev15 | 173 | 138/35 | 2.01% | 0.12% | -6.09% | 0.768 | -0.0201 |
| 4 | d2_ecmwf_only | 173 | 138/35 | 2.01% | 0.12% | -6.09% | 0.768 | -0.0201 |
| 5 | ev15_mixed | 184 | 144/40 | 1.34% | -0.56% | -6.77% | 0.767 | -0.0293 |
| 6 | ev18_mixed | 156 | 122/34 | 0.92% | -0.99% | -7.84% | 0.760 | -0.0373 |
| 7 | ecmwf_only | 179 | 142/37 | 0.31% | -1.57% | -7.92% | 0.768 | -0.0434 |
| 8 | d2_only | 176 | 140/36 | 0.40% | -1.49% | -8.46% | 0.769 | -0.0445 |
| 9 | d2_entry_72_85 | 160 | 128/32 | 0.07% | -1.80% | -8.85% | 0.775 | -0.0490 |
| 10 | entry_70_80 | 149 | 114/35 | -0.36% | -2.28% | -10.12% | 0.752 | -0.0582 |
| 11 | entry_72_82 | 148 | 116/32 | -0.54% | -2.44% | -10.32% | 0.764 | -0.0605 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 155 | 121/34 | -2.31% | -4.19% | -10.60% | 0.769 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 189 | 153/36 | 2.88% | -2.36% | 0.763 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 196 | 158/38 | 1.69% | -3.72% | 0.763 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
