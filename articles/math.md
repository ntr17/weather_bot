# Mathematical Infrastructure: Why Simple Arbitrage Math Fails

While you were checking if **YES + NO = $1**, quantitative systems were solving integer programs scanning 17,218 across $2^{63}$ possible outcomes in milliseconds.

When you see a Polymarket market where **YES is $0.62** and **NO is $0.33**, you think that adds up to $0.95—there's arbitrage. You're right. But by the time you place both orders, the spread is gone. 

The difference isn't speed. It's **mathematical infrastructure**.

---

## 1. The Reality of Guaranteed Profit

A 2025 research paper, *"Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets,"* documented that from April 2024 to April 2025, quantitative traders extracted **$39,688,585** in guaranteed arbitrage profits from Polymarket.

* **Top Single Trader:** $2,009,631.76 PnL
* **Trade Count:** 4,049 trades
* **Average Profit:** ~$496 per trade, guaranteed.

This isn't prediction; it's identifying situations where an outcome pays $1 and you buy it for less.

---

## 2. Why Simple Math Fails: The Marginal Polytope Problem

Arbitrage detection isn't just about checking if numbers add up—it’s about **logical dependencies**.

> **Example:**
> * Market A: "Will Trump win Pennsylvania?" (YES: $0.48, NO: $0.52) — *Sum: $1.00*
> * Market B: "Will Republicans win PA by 5+ points?" (YES: $0.32, NO: $0.68) — *Sum: $1.00*

Simple addition shows no arbitrage. However, if Republicans win by 5+ points, Trump **must** win Pennsylvania. These markets are logically linked, creating complex arbitrage opportunities that no manual check can catch.

### The Scale of the Problem
* **US Election 2024:** 305 markets = 46,360 pairs to check.
* **NCAA Tournament:** 63 games = $2^{63}$ ($9,223,372,036,854,775,808$) possible outcomes.



---

## 3. The Quantitative Engine: Frank-Wolfe & Bregman Projection

To solve these exponentially large spaces, systems use the **Frank-Wolfe algorithm**. Instead of checking all $2^{63}$ outcomes, it iteratively grows an "active set" of valid vertices, making the impossible tractable.

1.  **Detection:** Integer programming identifies logical violations.
2.  **Bregman Projection:** Projects the market state onto an arbitrage-free manifold to find the "perfect" trade size.
3.  **Acceleration:** As outcomes settle (e.g., games in a tournament finish), the feasible set shrinks and the system speeds up from 30 seconds to under 5 seconds per solve.

---

## 4. Execution: The Latency Hierarchy

Polymarket uses a **Central Limit Order Book (CLOB)**. Execution is sequential, not atomic. 

* **Manual Reality:** You buy YES at $0.30. By the time you click NO, the price is $0.78. You just lost $0.08.
* **System Reality:** Systems submit all legs of the trade within the same 2-second Polygon block.

### Why Copy-Trading Fails Without High-Speed Tools
If you copy a trade from the blockchain (Block N), you are buying into a moved market at Block N+1. You aren't arbitraging; you are providing **exit liquidity**.

For high-speed execution, I use the **Ares TG Bot**:
* [Join Ares TG Bot](https://t.me/KreoPolyBot?start=ref-discov)
* *Note:* It executes at the block level and tracks the top 15+ "whale" wallets automatically.

---

## 5. The Top 15 Profit Extractors

These wallets are publicly visible on-chain. Their PnL is the result of mechanical consistency:

| Wallet | Strategy | Documented Profit |
| :--- | :--- | :--- |
| **kch123** | Latency Arb (High Freq) | $12,000,000 |
| **RN1** | Market Making | $7,400,000 |
| **Swisstony** | Oracle Arbitrage | $5,900,000 |
| **DrPufferfish** | Combinatorial Arb | $3,400,000 |
| **Sharky6999** | Latency Arb | $813,000 |

---

## 6. How to Start: The Polymarket Drop

Polymarket currently rewards active liquidity via its rewards program. New users can qualify for USDC distributions based on trading volume.

1.  **Register:** Connect via MetaMask or Coinbase Wallet.
2.  **Fund:** Use **USDC.e** on the Polygon network (not ETH mainnet).
3.  **Trade:** Place a small position ($10–$50) to qualify for the initial drop.
4.  **Scale:** Rewards are proportional to volume and early participation.

---

**The math works. The infrastructure exists. The only question is execution.**