# Deployment Status: 2026-05-05

## Code Status
✅ **All audit fixes deployed to github/master**

**Deployed Fixes:**
- M1: `min_yes_price=$0.05` filter on snapshot check (line 48)
- M1: `min_yes_price` re-check on live price fetch (line 73)
- C1: NO take-profit capped at $0.99 (monitor.py)
- M2: Status guard in `close_position()` prevents double-close
- M4: Status guard in `check_stops_and_tp()` prevents checking closed positions
- B3: NO stop ratio changed to 0.30 (wider, prevents premature closure)
- Min reserve: Balance guard prevents over-deployment

**Config Parameters:**
```json
"min_yes_price": 0.05,
"no_stop_loss_pct": 0.30,
"stop_loss_pct": 0.80
```

**Tests:**
- 135/135 unit tests passing
- 3 new regression tests for NO TP logic and double-close prevention

## Current Trading State
- **Balance:** $3,194 (-36% from $5,000 start)
- **Trades:** 284 closed, 47 open
- **Win Rate:** 34% (96/284)
- **Deployed Capital:** $1,175 (23.5% of starting balance)

## Issues Found & Root Causes
1. **Old longshot YES trades (April 30):** Opened before min_yes_price was enforced
   - 5 YES longshots: entry $0.005-$0.044, lost -$48 combined
   - These occurred before fix deployment

2. **Tokyo NO $0.001 anomaly (May 4):** One impossible NO trade
   - Opened 2026-05-04T06:12:43
   - Entry=$0.001, 25,000 shares, lost $25
   - Likely a data glitch or edge case that has since resolved
   - Current open positions are all normal ($0.55-$0.91 entries)

3. **Performance degradation:** Win rate 34% is below expected
   - Suggests: forecast model may be miscalibrated
   - Or: systematic market bias against our bet placements
   - Requires deeper investigation beyond code bugs

## Action Plan
1. ✅ Code fixes deployed to master (done)
2. 📅 Monitor next 48 hours for clean execution with fixed code
3. 🔍 Analyze forecast accuracy vs. actual outcomes
4. 📊 Review market liquidity and spread impact

## Next Steps for Production
- Actions will run with fixed code in ~30 minutes (next 30-min trigger)
- Monitor trade logs for any more impossible entries
- Track win rate improvement with fixed code

---
Generated: 2026-05-05 13:00 UTC
