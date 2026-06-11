# CTO Audit — 2026-06-11

Full-repo audit: edge validation, code review, live-trading feasibility, and the
changes shipped in response. Written to be read before any live-trading decision.

## 1. Verdict on the edge — weaker than claimed

**The "airport vs city center" thesis as stated in CLAUDE.md ("3–8°F delta =
systematic mispricing") is not supported by this repo's own data.**

- `research/data/airport_offset.json` (90 days, measured by this project):
  mean airport-minus-city deltas are **−0.8 to +1.1°F**, not 3–8°F. Only Miami
  reached "STRONG EDGE" at +1.1°F mean.
- Cumulative paper result: **−99.5%** ($5,000 → $24.81), 912 logged trades,
  net PnL **−$1,097**. Most of the loss came from since-fixed behavior (see §2),
  but no period of the history demonstrates a robust positive edge.
- The one promising slice — **NO on overpriced non-forecast buckets at D+2,
  entry 0.70–0.85** — shows ROI after fee/spread drag of **+8.05% on n=17**
  with a bootstrap lower bound of **−6.35%**. That is statistically
  indistinguishable from zero. It is a hypothesis, not an edge.
- Trades priced with well-calibrated sigma (<3°F) earned **+5.3% ROI (n=159)**
  while sigma 3–6°F lost −3.9% — evidence that what edge exists comes from
  forecast accuracy, and that the sigma bug (§2.1) was destroying it.

Honest framing: this bot's plausible edge is "good free NWP forecasts vs
retail flow on tail buckets," which is real but small, and weather markets
attract sharp specialist traders. Expect low single-digit ROI per trade at
best, on ~$5 trades, ~2–10 trades/day. That is beer money, not income, even
if everything works.

## 2. What was broken (and what I fixed today)

### 2.1 Sigma bootstrap was poisoned — FIXED (the big one)
`research/bootstrap_sigma.py` v1 used **persistence error** (|today − target
day|) as sigma. Its docstring called this "conservative" — true only for
YES-buying. The bot is **NO-only**: inflated sigma (Chicago σ=11.3°F,
max 17°F in the DB vs real ECMWF error ~2–3°F) deflates p(YES) on
near-forecast buckets → inflates p(NO) and EV → the bot systematically bought
NO on buckets that were actually likely. This poisoned every probability,
EV, and Kelly number the bot produced.

Fixes shipped:
- `bootstrap_sigma.py` rewritten to use **real historical model forecast
  errors** (Open-Meteo Previous Runs API: the forecast issued N days ahead vs
  ERA5 actual). Persistence kept only as a labelled fallback.
- `core/calibrator.get_sigma()` now **clamps sigma at read time** to
  [1.0, 5.0]°F / [0.6, 3.0]°C — garbage calibration can no longer blow up
  trade selection, effective immediately on the next bot run.
- `bot.yml` upgraded: it detects v1 persistence calibration in the DB and
  re-bootstraps once with the model-based method.
- Caveat: this container has no network access to Open-Meteo, so the new
  bootstrap endpoint logic is **untested against the live API**. It fails
  safe (per-city try/except, persistence fallback, read-time clamp), and CI
  will exercise it on the next scheduled run — check that run's logs.

### 2.2 Live-money accounting bugs — FIXED
These would have silently corrupted the ledger in live mode:
- **Phantom resolution credit**: a GTC order resting unfilled ("live") at
  market resolution was credited as a full win/loss even though we never
  owned tokens. Now: cancel + exact cost refund (`unfilled_cancelled`).
- **Stale orders**: unfilled GTC orders now get cancelled after 12h
  (`check_pending_orders`); partial fills keep the matched portion and refund
  the unfilled cost.
- Cancelled never-filled orders no longer pollute win/loss stats.

### 2.3 Trade-log horizon was wrong — FIXED
`trades.horizon` recorded the horizon **at close** (always D+0 for resolved
trades), making per-horizon analysis from the trades table garbage
(`strategy_lab.py` worked around it by reconstructing from the markets
table). Horizon is now stored on the position at entry.

### 2.4 Known issues NOT fixed (do these before live)
- **Station verification**: `core/locations.py` Tokyo row says RJTT (Haneda)
  but its coordinates are Narita's. Chicago assumes KORD; some Polymarket
  Chicago markets have historically resolved on Midway. **Action: for each
  city, read the resolution source text on an actual Polymarket market page
  and reconcile station + coordinates.** A wrong station is an unbounded
  silent-loss bug.
- **No balance reconciliation in live mode**: internal `state.balance` is
  never checked against actual USDC/positions on chain. Drift will accumulate
  (e.g. a sell that fills at a different price). Needed before live: a
  reconcile step per cycle using CLOB balances/trades endpoints.
- Paper TP exits fill at best bid with no depth check — paper results are
  slightly optimistic vs live fills.
- `data/status.md` "Return −99.5%" mixes several strategy eras and balance
  resets; treat the trades table, not that headline, as ground truth.

## 3. Live trading feasibility

**The executor is NOT a stub** (CLAUDE.md was stale): `core/clob.py` +
`core/executor.py` implement auth (L1→L2 via py-clob-client-v2), GTC limit
orders on negRisk markets, cancels, order polling, geoblock preflight, and a
kill switch. What actually blocks going live:

1. **Evidence**: the brain's gates (≥100 resolved current-strategy trades,
   ≥30 post-activation, positive bootstrap lower bound) are the right bar and
   are currently far from met (17 / 0 / −6.35%). Note: post-activation count
   has been 0 since 2026-06-09 — D+2-only trades need ~3 days to resolve, and
   caps allow ≤2 new positions/run; expect first resolutions ~June 12–13.
   If still 0 by June 14, something is broken in the pipeline.
2. **Where it runs**: GitHub Actions runners are geoblocked (US) and the
   workflow correctly forces `PAPER_TRADING=true`. Live must run on the
   owner's personal machine (or a VPS in a permitted jurisdiction) with `PK`,
   `FUNDER`, funded USDC, and a passing geoblock preflight. Compliance with
   Polymarket's regional rules is the owner's call — do not "solve" geoblock
   with a VPN; that risks account/funds seizure.
3. **Capital**: $5 orders / $20 exposure means even a true 8% edge ≈
   ~$1–2/day. Scaling up multiplies any remaining bug directly into losses.

**My decision as CTO: do NOT flip live today.** With a negative bootstrap
lower bound, going live is buying variance, not collecting edge. Everything
is wired so that flipping is one env var (`PAPER_TRADING=false`) on the
personal machine once the gates pass.

## 4. Strategy research beyond weather

External web research could not be completed from this session (network
restrictions), so these are assessments from internal data + general market
knowledge — **verify before building**:

- **Near-resolution convergence / favorite-longshot**: the bot's own data
  weakly supports it (the profitable slice IS "sell overpriced longshot
  buckets"). Generalizing beyond weather (any negRisk multi-outcome market
  with a fat-tailed retail-priced longshot) is the most natural extension —
  same executor, same CLOB plumbing.
- **Cross-platform arb (Polymarket vs Kalshi)** is the cleanest structural
  edge if the owner is US-based (Kalshi is CFTC-regulated; Polymarket's US
  status must be checked) — but it needs capital on both venues and fast
  execution; competitive.
- **Sports/economic data**: speed games against well-capitalized bots; not
  winnable with a 30-minute GitHub Actions cron. Skip.
- **Market-making / liquidity rewards**: Polymarket has paid maker rewards;
  for $5 orders this may dominate the trading edge itself. Worth
  investigating as the actual business model for a small bot.

Recommendation: stay on weather until the D+2 hypothesis confirms or dies
(~3–4 weeks of data), because the infrastructure measures itself honestly
now. Build the generalized "overpriced longshot bucket" scanner second.

## 5. What changed in this commit

| File | Change |
|---|---|
| `research/bootstrap_sigma.py` | Rewritten: real model forecast errors (Previous Runs API), persistence only as labelled fallback |
| `core/calibrator.py` | `clamp_sigma()` applied at every `get_sigma()` read |
| `core/config.py` | Sigma clamp bounds |
| `core/monitor.py` | Unfilled live orders refunded at resolution instead of phantom win/loss |
| `main.py` | `check_pending_orders`: 12h TTL cancel, partial-fill cost adjustment |
| `core/executor.py` | Horizon stored at entry; `unfilled_cancelled` close reason excluded from W/L stats |
| `core/storage.py` | Trade log uses entry horizon |
| `.github/workflows/bot.yml` | One-time model-based recalibration trigger |
| `tests/` | 6 new tests (151 total, all green) |
| `CLAUDE.md`, `AGENT_HANDOFF.md` | Stale/overstated claims corrected |

## 6. Checklist for the owner before live

1. Wait for brain gates: ≥100 resolved, ≥30 post-activation, bootstrap low > 0.
2. Verify per-city resolution stations against Polymarket market text (§2.4).
3. Confirm next Actions run replaced `bootstrap_persistence` calibration
   (check `data/status.md` calibration table: source should read
   `bootstrap_model`, sigmas ~1.5–4°F).
4. On the personal machine: `.env` with `PK`, `FUNDER`, `SIGNATURE_TYPE`,
   `VC_KEY`; fund the wallet with a small amount (≤$50); run
   `python main.py probe`, then `PAPER_TRADING=false python main.py once` and
   inspect every line before starting the loop.
5. Keep `max_bet=5`, `max_total_open_cost=20` for the first two live weeks.
