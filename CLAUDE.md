# WeatherBot — Polymarket Weather Trading Bot

## Critical Domain Knowledge

### Airport Stations (markets resolve on these, NOT city centers)
| City | ICAO | Airport |
|------|------|---------|
| NYC | KLGA | LaGuardia |
| Chicago | KORD | O'Hare |
| Miami | KMIA | Miami Intl |
| Dallas | KDAL | Love Field |
| Seattle | KSEA | Sea-Tac |
| Atlanta | KATL | Hartsfield |
| London | EGLC | London City |
| Tokyo | RJTT | Haneda |

3–8°F delta between city center and airport. On 1–2°F bucket markets, this is the trade.

### Forecast Sources
- **ECMWF** via Open-Meteo — updates 00:00/12:00 UTC (~6h lag)
- **HRRR/GFS** via Open-Meteo — updates hourly (US only)
- **METAR** via aviationweather.gov — real-time, no lag

### Config (config.json)
- `min_ev: 0.1` — minimum expected value to enter
- `kelly_fraction: 0.25` — quarter-Kelly position sizing
- `max_price: 0.45` — never buy above 45 cents
- `max_slippage: 0.03` — skip if bid/ask spread > $0.03
- `scan_interval: 3600` — hourly scan

## Related Projects (in ~/Documents/Projects/)
- `polymarket-mcp-server/` — 45 MCP tools for direct Polymarket access (needs Polygon wallet)
- `polymarket-skills/` — scanner, analyzer, paper-trader, live-executor skills
- `TradingAgents/` — multi-agent bull/bear debate framework (needs API keys in .env)
- `prediction-market-analysis/` — 36GB Polymarket/Kalshi history (`make setup` to download)
- `everything-claude-code/` — ECC source (installed globally to ~/.claude/)
