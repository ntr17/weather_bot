# Strategy Lab
Generated: 2026-06-04T05:12:22.426926+00:00

## Recommendation

- Action: `keep`
- Best candidate: `d1_only`
- Reason: A variant ranks higher, but the improvement is too weak for automatic adaptation.
- Ready for live user review: `False`
- Live blockers:
  - need >=100 resolved trades, have 22
  - need positive bootstrap lower bound, have -9.63%

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d1_only | 3 | 3/0 | 25.05% | 23.15% | 10.52% | 0.760 | 0.1375 |
| 2 | ensemble_only | 1 | 1/0 | 21.80% | 20.07% | 21.80% | 0.821 | 0.1027 |
| 3 | ev15 | 18 | 17/1 | 11.54% | 9.62% | -3.28% | 0.753 | 0.0207 |
| 4 | d2_ev15 | 16 | 15/1 | 9.65% | 7.73% | -7.19% | 0.756 | -0.0159 |
| 5 | ev18 | 14 | 13/1 | 9.27% | 7.35% | -9.38% | 0.754 | -0.0313 |
| 6 | current_safe | 22 | 20/2 | 7.02% | 5.13% | -9.63% | 0.763 | -0.0384 |
| 7 | entry_70_80 | 20 | 18/2 | 6.03% | 4.11% | -12.14% | 0.757 | -0.0614 |
| 8 | ecmwf_only | 20 | 18/2 | 4.49% | 2.60% | -13.05% | 0.763 | -0.0797 |
| 9 | d2_only | 19 | 17/2 | 4.18% | 2.28% | -14.12% | 0.763 | -0.0886 |
| 10 | entry_72_82 | 19 | 17/2 | 4.13% | 2.24% | -14.19% | 0.766 | -0.0893 |
| 11 | d2_entry_72_85 | 18 | 16/2 | 3.77% | 1.88% | -15.47% | 0.767 | -0.0993 |
