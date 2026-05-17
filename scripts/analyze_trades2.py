"""Deep analysis of trade outcomes and convergence statistics."""
import sqlite3

conn = sqlite3.connect("data/weatherbot.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Check what's in outcome column
print("=== OUTCOME VALUES ===")
for row in c.execute("""
SELECT outcome, COUNT(*) as n FROM trades GROUP BY outcome
"""):
    print(f"  outcome='{row[0]}': {row[1]}")

# Trades with reason set (actually closed)
print("\n=== TRADES WITH REASON SET (actually closed) ===")
for row in c.execute("""
SELECT reason, COUNT(*) as n, SUM(pnl) as total_pnl,
       AVG(entry_price) as avg_entry, AVG(exit_price) as avg_exit
FROM trades WHERE reason IS NOT NULL
GROUP BY reason ORDER BY n DESC
"""):
    print(f"  {row[0]}: n={row[1]}, pnl={row[2]:.2f}, entry={row[3]:.3f}, exit={row[4]:.3f}")

# Trades with pnl set (closed with profit/loss)
print("\n=== TRADES WITH PNL SET ===")
for row in c.execute("""
SELECT side, horizon, reason, COUNT(*) as n, 
       SUM(pnl) as total_pnl, SUM(cost) as total_cost,
       SUM(CASE WHEN pnl >= 0 THEN 1 ELSE 0 END) as wins,
       SUM(CASE WHEN pnl < 0 THEN 1 ELSE 0 END) as losses
FROM trades WHERE pnl IS NOT NULL
GROUP BY side, horizon, reason ORDER BY side, horizon, reason
"""):
    roi = row[4]/row[5]*100 if row[5]>0 else 0
    print(f"  {row[0]:3} {row[1] or 'None':4} {row[2] or 'None':20} n={row[3]:3} "
          f"W={row[6]} L={row[7]} pnl={row[4]:+8.2f} cost={row[5]:8.2f} ROI={roi:+.1f}%")

# THE KEY ANALYSIS: D+1/D+2 NO with pnl set (the convergence trades)
print("\n=== CONVERGENCE: D+1/D+2 NO trades with PnL ===")
conv = c.execute("""
SELECT city, date, entry_price, exit_price, cost, pnl, horizon, 
       reason, opened_at, closed_at, outcome
FROM trades WHERE side='no' AND horizon IN ('D+1','D+2') AND pnl IS NOT NULL
ORDER BY opened_at
""").fetchall()
wins = [r for r in conv if r["pnl"] >= 0]
losses = [r for r in conv if r["pnl"] < 0]
print(f"Total: {len(conv)}, Wins: {len(wins)}, Losses: {len(losses)}")
if conv:
    total_pnl = sum(r["pnl"] for r in conv)
    total_cost = sum(r["cost"] for r in conv)
    print(f"PnL: {total_pnl:.2f}, Cost: {total_cost:.2f}, ROI: {total_pnl/total_cost*100:.1f}%")
    for r in conv:
        roi = r["pnl"]/r["cost"]*100 if r["cost"]>0 else 0
        print(f"  {r['city']:15} {r['date']} {r['horizon']} "
              f"entry={r['entry_price']:.3f} exit={r['exit_price']:.3f} "
              f"cost={r['cost']:.2f} pnl={r['pnl']:+.2f} ({roi:+.1f}%) "
              f"reason={r['reason']} outcome={r['outcome']}")

# D+0 NO trades with PnL (the resolution trades)
print("\n=== D+0 NO trades with PnL ===")
d0 = c.execute("""
SELECT reason, COUNT(*) as n, SUM(pnl) as total_pnl, SUM(cost) as total_cost,
       SUM(CASE WHEN pnl>=0 THEN 1 ELSE 0 END) as w,
       SUM(CASE WHEN pnl<0 THEN 1 ELSE 0 END) as l
FROM trades WHERE side='no' AND horizon='D+0' AND pnl IS NOT NULL
GROUP BY reason ORDER BY n DESC
""").fetchall()
for row in d0:
    roi = row[2]/row[3]*100 if row[3]>0 else 0
    print(f"  {row[0]}: n={row[1]}, W={row[4]}, L={row[5]}, "
          f"pnl={row[2]:+.2f}, cost={row[3]:.2f}, ROI={roi:+.1f}%")

# YES trades with PnL
print("\n=== YES trades with PnL ===")
yes = c.execute("""
SELECT horizon, reason, COUNT(*) as n, SUM(pnl) as total_pnl, SUM(cost) as total_cost,
       SUM(CASE WHEN pnl>=0 THEN 1 ELSE 0 END) as w,
       SUM(CASE WHEN pnl<0 THEN 1 ELSE 0 END) as l
FROM trades WHERE side='yes' AND pnl IS NOT NULL
GROUP BY horizon, reason ORDER BY horizon, reason
""").fetchall()
for row in yes:
    roi = row[3]/row[4]*100 if row[4]>0 else 0
    print(f"  {row[0] or 'None':4} {row[1] or 'None':20} n={row[2]} W={row[5]} L={row[6]} "
          f"pnl={row[3]:+.2f} cost={row[4]:.2f} ROI={roi:+.1f}%")

# STATISTICAL ANALYSIS
print("\n" + "="*60)
print("STATISTICAL ANALYSIS")
print("="*60)

# All convergence trades (NO D+1/D+2)
all_conv = c.execute("""
SELECT pnl, cost, entry_price, exit_price
FROM trades WHERE side='no' AND horizon IN ('D+1','D+2') AND pnl IS NOT NULL
""").fetchall()

n = len(all_conv)
if n > 0:
    wins = sum(1 for r in all_conv if r["pnl"] >= 0)
    losses = n - wins
    p_hat = wins / n

    # Bayesian posterior: Beta(wins+1, losses+1)
    import math
    a = wins + 1  # alpha
    b = losses + 1  # beta
    post_mean = a / (a + b)
    post_mode = (a - 1) / (a + b - 2) if a > 1 and b > 1 else (1 if a > b else 0)

    # 95% credible interval (normal approx for large n)
    post_var = (a * b) / ((a + b)**2 * (a + b + 1))
    post_std = math.sqrt(post_var)
    ci_low = max(0, post_mean - 1.96 * post_std)
    ci_high = min(1, post_mean + 1.96 * post_std)

    print(f"\nn = {n} trades, Wins = {wins}, Losses = {losses}")
    print(f"Sample win rate: {p_hat:.4f}")
    print(f"Bayesian posterior: Beta({a}, {b})")
    print(f"  Mean: {post_mean:.4f}")
    print(f"  Mode: {post_mode:.4f}")
    print(f"  95% CI: [{ci_low:.4f}, {ci_high:.4f}]")

    # What's the probability p >= 0.90?
    # Using incomplete beta function approximation
    # For n=11, k=11: P(p >= 0.90) is high
    # Exact: P(p >= t | Beta(a,b)) = 1 - I_t(a,b)
    # For Beta(12,1): CDF at t = 1 - (1-t)^12... wait no
    # Beta(a,b) where a=wins+1, b=losses+1
    # If all wins: Beta(n+1, 1) -> PDF = (n+1)*p^n, CDF = p^(n+1)
    # P(p >= 0.90) = 1 - 0.90^(n+1)
    if losses == 0:
        for threshold in [0.80, 0.85, 0.90, 0.95, 0.98]:
            prob_above = 1 - threshold**(n + 1)
            print(f"  P(true WR >= {threshold:.0%}): {prob_above:.4f} ({prob_above*100:.1f}%)")
    
    # Expected ROI with fees
    avg_roi_paper = sum(r["pnl"] for r in all_conv) / sum(r["cost"] for r in all_conv)
    avg_entry = sum(r["entry_price"] for r in all_conv) / n
    avg_shares = sum(r["cost"]/r["entry_price"] for r in all_conv) / n

    # Fee calc: fee = C * 0.05 * p * (1-p)
    avg_entry_fee = avg_shares * 0.05 * avg_entry * (1 - avg_entry)
    avg_exit_price = sum(r["exit_price"] for r in all_conv) / n
    avg_exit_fee = avg_shares * 0.05 * avg_exit_price * (1 - avg_exit_price)
    total_fee_per_trade = avg_entry_fee + avg_exit_fee
    avg_gross_pnl = sum(r["pnl"] for r in all_conv) / n
    avg_cost = sum(r["cost"] for r in all_conv) / n
    net_pnl = avg_gross_pnl - total_fee_per_trade
    
    print(f"\nPaper ROI: {avg_roi_paper*100:.1f}%")
    print(f"Avg entry: {avg_entry:.3f}, Avg exit: {avg_exit_price:.3f}")
    print(f"Avg gross PnL/trade: ${avg_gross_pnl:.2f}")
    print(f"Avg taker fee/trade: ${total_fee_per_trade:.2f}")
    print(f"Avg net PnL/trade (taker): ${net_pnl:.2f}")
    print(f"Net ROI (taker): {net_pnl/avg_cost*100:.1f}%")
    print(f"Net ROI (maker/limit): {avg_roi_paper*100:.1f}% (zero fees)")

    # Per $150 bankroll
    print(f"\n--- WITH $150 BANKROLL ---")
    bet_size = min(15, 150 * 0.10)  # 10% of bankroll, max $15
    print(f"Bet size: ${bet_size:.0f}/trade")
    print(f"Gross profit per win (taker): ${bet_size * avg_roi_paper - total_fee_per_trade * (bet_size/25):.2f}")
    print(f"Gross profit per win (maker): ${bet_size * avg_roi_paper:.2f}")
    if losses == 0:
        # Worst case on a loss: entry_price * shares goes to 0
        max_loss = bet_size  # full cost
        print(f"Max loss per trade: -${max_loss:.2f}")
        print(f"Max daily drawdown (2 losses): -${2*max_loss:.2f} ({2*max_loss/150*100:.0f}% of bankroll)")

conn.close()
