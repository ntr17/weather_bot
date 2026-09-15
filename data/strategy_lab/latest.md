# Strategy Lab
Generated: 2026-09-15T21:27:01.975312+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev18`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have 0.09%
  - need post-activation ROI after drag >=3%, have -4.06%
  - need positive bootstrap lower bound, have -5.79%
  - need win rate at least 3 points over avg NO breakeven

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 154 | 123/31 | 2.44% | 0.53% | -6.08% | 0.761 | -0.0160 |
| 2 | current_paper | 179 | 143/36 | 1.98% | 0.09% | -5.79% | 0.769 | -0.0194 |
| 3 | d2_ev15 | 179 | 143/36 | 1.98% | 0.09% | -5.79% | 0.769 | -0.0194 |
| 4 | d2_ecmwf_only | 179 | 143/36 | 1.98% | 0.09% | -5.79% | 0.769 | -0.0194 |
| 5 | ev15_mixed | 190 | 149/41 | 1.33% | -0.56% | -6.53% | 0.768 | -0.0284 |
| 6 | ev18_mixed | 161 | 126/35 | 0.86% | -1.05% | -7.56% | 0.760 | -0.0370 |
| 7 | ecmwf_only | 185 | 147/38 | 0.33% | -1.55% | -7.81% | 0.769 | -0.0428 |
| 8 | d2_only | 182 | 145/37 | 0.41% | -1.47% | -8.49% | 0.769 | -0.0444 |
| 9 | d2_entry_72_85 | 166 | 133/33 | 0.09% | -1.78% | -8.79% | 0.775 | -0.0486 |
| 10 | entry_72_82 | 153 | 120/33 | -0.56% | -2.45% | -10.02% | 0.764 | -0.0596 |
| 11 | entry_70_80 | 152 | 116/36 | -0.57% | -2.50% | -10.09% | 0.752 | -0.0603 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 161 | 126/35 | -2.19% | -4.06% | -10.42% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 195 | 158/37 | 2.81% | -2.65% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 202 | 163/39 | 1.65% | -3.76% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
