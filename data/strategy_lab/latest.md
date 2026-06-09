# Strategy Lab
Generated: 2026-06-09T15:29:56.435434+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d2_ev15`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Live blockers:
  - need >=100 resolved trades, have 30
  - need >=3% ROI after fee/spread drag, have 2.11%
  - need positive bootstrap lower bound, have -12.11%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev15 | 17 | 16/1 | 9.96% | 8.05% | -6.35% | 0.756 | -0.0077 |
| 2 | ev15 | 25 | 20/5 | 7.32% | 5.40% | -7.89% | 0.754 | -0.0236 |
| 3 | current_safe | 30 | 24/6 | 4.01% | 2.11% | -12.11% | 0.762 | -0.0613 |
| 4 | ecmwf_only | 23 | 20/3 | 4.01% | 2.11% | -12.52% | 0.762 | -0.0767 |
| 5 | ev18 | 19 | 15/4 | 5.28% | 3.36% | -14.70% | 0.750 | -0.0799 |
| 6 | d2_only | 20 | 18/2 | 4.50% | 2.61% | -13.45% | 0.762 | -0.0810 |
| 7 | entry_70_80 | 28 | 22/6 | 2.81% | 0.90% | -14.82% | 0.757 | -0.0869 |
| 8 | d2_entry_72_85 | 19 | 17/2 | 4.12% | 2.23% | -14.90% | 0.766 | -0.0919 |
| 9 | entry_72_82 | 27 | 21/6 | 0.91% | -0.98% | -16.50% | 0.764 | -0.1135 |
| 10 | d1_only | 10 | 6/4 | 1.87% | -0.03% | -42.20% | 0.760 | -0.2280 |
| 11 | ensemble_only | 6 | 3/3 | -15.05% | -16.88% | -80.41% | 0.770 | -0.5382 |
