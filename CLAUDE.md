# WeatherBot — Polymarket Weather Trading Bot

**Edge**: Polymarket resolves on AIRPORT coordinates. Most traders price on city center.
That 3-8 deg delta = systematic mispricing on 1-2 deg bucket markets.

## State
Phase 1 — Paper trading. Architecture complete. Needs to run and accumulate calibration data.

## Active TODOs
- [ ] Verify scanner slug format matches current Polymarket event slugs
- [ ] Run research/airport_offset.py to confirm edge still present
- [ ] Run paper trading for 1 week, review data/state.json
- [ ] (Personal) paste any todos from last session here

## Commands
```
python main.py probe     # one scan, no trades (safe test)
python main.py status    # balance + open positions
python main.py           # full trading loop
pytest tests/            # run tests
scripts\bundle.ps1       # ship code to personal (work machine only)
scripts\receive_bundle.ps1  # apply bundle from Downloads (personal machine only)
```

## Rules
- Work machine: edit code + run pytest ONLY. Never main.py (calls Polymarket API).
- .env and config.json are gitignored — each machine has its own copy.
- data/ is gitignored — lives on personal machine only.