# Strategy Lab
Generated: 2026-07-03T19:52:39.938156+00:00

## Recommendation

- Action: `keep`
- Best candidate: `current_paper`
- Reason: Current paper strategy remains the best risk-adjusted live-applicable candidate.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=100 resolved trades, have 58
  - need post-activation ROI after drag >=3%, have -2.94%
  - need positive bootstrap lower bound, have -5.74%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | current_paper | 58 | 49/9 | 6.48% | 4.58% | -5.74% | 0.772 | 0.0257 |
| 2 | d2_ev15 | 58 | 49/9 | 6.48% | 4.58% | -5.74% | 0.772 | 0.0257 |
| 3 | d2_ecmwf_only | 58 | 49/9 | 6.48% | 4.58% | -5.74% | 0.772 | 0.0257 |
| 4 | d2_ev18 | 55 | 46/9 | 5.91% | 4.01% | -7.57% | 0.770 | 0.0136 |
| 5 | ev15_mixed | 69 | 55/14 | 4.66% | 2.76% | -6.98% | 0.768 | 0.0032 |
| 6 | d2_only | 61 | 51/10 | 3.03% | 1.15% | -9.98% | 0.773 | -0.0234 |
| 7 | ecmwf_only | 64 | 53/11 | 2.75% | 0.87% | -9.97% | 0.772 | -0.0262 |
| 8 | ev18_mixed | 62 | 49/13 | 2.81% | 0.91% | -10.17% | 0.767 | -0.0265 |
| 9 | d2_entry_72_85 | 58 | 48/10 | 2.12% | 0.24% | -11.59% | 0.777 | -0.0382 |
| 10 | entry_70_80 | 62 | 49/13 | 2.15% | 0.24% | -11.86% | 0.760 | -0.0391 |
| 11 | entry_72_82 | 63 | 49/14 | -0.20% | -2.09% | -13.78% | 0.768 | -0.0691 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 40 | 32/8 | -1.08% | -2.94% | -17.45% | 0.778 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 74 | 64/10 | 7.16% | -0.78% | 0.759 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 81 | 69/12 | 4.92% | -3.50% | 0.759 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
