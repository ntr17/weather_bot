# Strategy Lab
Generated: 2026-09-20T11:32:50.641748+00:00

## Recommendation

- Action: `adapt_paper`
- Best candidate: `d2_ev18`
- Reason: Best candidate beats current risk-adjusted score enough for paper testing.
- Ready for live user review: `False`
- Paper policy activated at: `2026-06-09T18:23:01Z`
- Live blockers:
  - need >=3% ROI after fee/spread drag, have -0.20%
  - need post-activation ROI after drag >=3%, have -4.46%
  - need positive bootstrap lower bound, have -6.38%
  - need win rate at least 3 points over avg NO breakeven

## Ranked Candidates

| Rank | Candidate | N | W/L | ROI | ROI after drag | Boot ROI low | Entry | Score |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | d2_ev18 | 156 | 124/32 | 2.09% | 0.18% | -6.32% | 0.761 | -0.0203 |
| 2 | current_paper | 181 | 144/37 | 1.69% | -0.20% | -6.38% | 0.769 | -0.0243 |
| 3 | d2_ev15 | 181 | 144/37 | 1.69% | -0.20% | -6.38% | 0.769 | -0.0243 |
| 4 | d2_ecmwf_only | 181 | 144/37 | 1.69% | -0.20% | -6.38% | 0.769 | -0.0243 |
| 5 | ev15_mixed | 192 | 150/42 | 1.06% | -0.83% | -6.71% | 0.768 | -0.0318 |
| 6 | ev18_mixed | 163 | 127/36 | 0.54% | -1.37% | -8.18% | 0.760 | -0.0423 |
| 7 | ecmwf_only | 187 | 148/39 | 0.07% | -1.81% | -7.89% | 0.769 | -0.0457 |
| 8 | d2_only | 184 | 146/38 | 0.15% | -1.74% | -8.59% | 0.769 | -0.0475 |
| 9 | d2_entry_72_85 | 168 | 134/34 | -0.19% | -2.06% | -8.76% | 0.775 | -0.0513 |
| 10 | entry_72_82 | 155 | 121/34 | -0.85% | -2.74% | -10.01% | 0.764 | -0.0624 |
| 11 | entry_70_80 | 154 | 117/37 | -0.86% | -2.78% | -10.31% | 0.752 | -0.0639 |
| 12 | d1_only | 13 | 8/5 | 0.19% | -1.71% | -37.72% | 0.759 | -0.2231 |
| 13 | ensemble_only | 8 | 5/3 | -7.40% | -9.24% | -55.25% | 0.768 | -0.3698 |
| 14 | d2_ensemble_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |
| 15 | d2_gfs_only | 0 | 0/0 | 0.00% | 0.00% | 0.00% | 0.000 | -999.0000 |

## Post-Activation Current Paper

| N | W/L | ROI | ROI after drag | Boot ROI low | Entry |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 163 | 127/36 | -2.58% | -4.46% | -10.82% | 0.770 |

## Diagnostics By Horizon

| Horizon | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| D+2 | 197 | 159/38 | 2.57% | -2.64% | 0.764 |
| D+1 | 20 | 13/7 | -8.09% | -38.58% | 0.753 |

## Diagnostics By Source

| Source | N | W/L | ROI after drag | Boot ROI low | Entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFS | 2 | 1/1 | 17.00% | -100.00% | 0.725 |
| ECMWF | 204 | 164/40 | 1.43% | -4.11% | 0.764 |
| ENSEMBLE | 11 | 7/4 | -8.03% | -49.79% | 0.755 |
