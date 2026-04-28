# Hermes Agent + Polymarket: Self-Learning Weather Trading Guide

My previous guide on the Weather Clawdbot reached **2.5M views**. Since then, the landscape has shifted. On February 25, 2026, @NousResearch released the **Hermes Agent**. After a month of daily use in the Polymarket trenches, I can confidently say it is the best agent currently on the market.

Automated, self-learning agents have a massive edge in weather, crypto, and sports markets. They don't sleep, they don't have emotions, and they remember every tick of data.

### Proven Success Stories:
* **ColdMath:** Weather trading bot ($300 → $219K in 3 months).
* **Sharky6999:** Crypto trading bot ($819K PnL, 99.3% win-rate).
* **RN1:** Sports bot ($1.2K → $7.3M).

---

## What Is Hermes Agent?

Released by **Nous Research** (the team behind YaRN and Psyche), Hermes is not just a chatbot. It is a persistent staff member that grows more capable over time through dedicated machine access and a multi-level memory system.



### The Three Layers of Hermes:
1.  **Knowledge Layer:** Built-in memory and session search. It doesn't just answer; it accumulates expertise.
2.  **Execution Layer:** Decomposes tasks, runs child agents in parallel, and uses MCP (Model Context Protocol) for tool integration.
3.  **Output Layer:** Delivers results via Cron jobs to Telegram, Slack, or Discord.

### Why It Beats OpenClaw (Moltbot):
* **The Learning Loop:** OpenClaw is static. Hermes reviews its performance every ~15 tool calls and writes reusable **skills** (.md files) to improve its future logic.
* **Persistent Memory:** Hermes uses `MEMORY.md` (facts/conventions) and `USER.md` (preferences) to maintain context indefinitely.

---

## Installation Guide (Under 5 Minutes)

Hermes supports Linux, macOS, and WSL2. We recommend a **Hetzner VPS** for 24/7 uptime.

1.  **Prepare VPS:** Rent a standard VPS on Hetzner and SSH into it:
    ```bash
    ssh root@your_server_ip
    ```
2.  **Install Hermes:** Run the official auto-installer:
    ```bash
    curl -fsSL [https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh](https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh) | bash
    source ~/.bashrc
    ```
3.  **Setup Gateway:** Connect Hermes to Telegram so you can trade from your phone:
    ```bash
    hermes gateway setup
    ```
4.  **Launch:** Start the CLI:
    ```bash
    hermes
    ```

---

## Building the Weather Trading Agent

We will use the logic inspired by @AlterEgo_eth to build a bot that scans 20+ cities across 3 forecast sources using the **Kelly Criterion** for position sizing. 

> **Note:** Just copy-paste these prompts directly into your Hermes terminal or Telegram chat.

### Phase 1: Environment & Wallet
**Prompt 1 (Setup):**
```text
clone this repo and set up the python environment:
git clone [https://github.com/alteregoeth-ai/weatherbot.git](https://github.com/alteregoeth-ai/weatherbot.git)
cd weatherbot
create a python venv and install: py-clob-client python-dotenv requests web3
Prompt 2 (Wallet):

Plaintext

create a new Polygon wallet using eth_account in python. 
save the private key to weatherbot/.env as:
PK=your_key
WALLET=your_address
SIG_TYPE=0
Fund this wallet with USDC.e and a small amount of POL for gas.

Phase 2: On-Chain Permissions
Prompt 3 (Approvals):

Plaintext

I need to approve USDC.e spending for 3 Polymarket contracts. 
My PK is in the .env. Send max uint256 approvals for USDC.e to:
1. CTF Exchange: 0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E
2. Neg Risk Exchange: 0xC5d563A36AE78145C45a50134d48A1215220f80a
3. Router: 0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296
Also setApprovalForAll for the Conditional Tokens contract.
Phase 3: Configuration & Launch
Prompt 4 (Configure):
Get your API key from Visual Crossing.

Plaintext

edit weatherbot/config.json:
- balance: [Actual USDC amount]
- max_bet: 2.0
- min_ev: 0.10
- mode: live
- vc_key: [YOUR_API_KEY]
Prompt 5 (Deployment):

Plaintext

start the weather bot in continuous mode as a background process.
it should scan every 60 minutes and self-learn based on trade outcomes.
show me the Polymarket portfolio link for my wallet.
The Result
You now have a production-grade agent that self-calibrates. As it completes trades, Hermes will generate new skills to refine its weather prediction accuracy based on historical wins and losses. You can monitor everything via your Telegram bot, receiving real-time Expected Value (EV) reports as the trades execute.