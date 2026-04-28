# WeatherBot — Workflow Guide

## System Overview

```
WORK MACHINE (Windows / VS Code)         PERSONAL MACHINE (Windows / GitHub)
- Build code                             - Run trading bot
- No GitHub access                       - Paper + live simulations
- Outlook email                          - Gmail email
          |                                         |
          |---- [WeatherBot Code] email ---------> |  scripts\receive_bundle.ps1
          |         (git bundle, code only)         |
          |                                         |
          | <--- [WeatherBot Data] email ---------- |  scripts\ship_data_back.py
                  (zip: data/markets, state,        |
                   calibration)
```

**Rule: Code flows WORK → PERSONAL only. Data flows PERSONAL → WORK only.**  
**Rule: Secrets (.env) and config.json stay on each machine — never transferred.**

---

## One-Time Setup

### Work Machine

**1. Confirm Python is installed**
```powershell
python --version    # should be 3.10+
```

**2. Copy .env from template and fill in your values**
```powershell
Copy-Item .env.example .env
notepad .env
```
Fill in:
- `VC_KEY` — from https://www.visualcrossing.com/weather-api (free)
- `PERSONAL_EMAIL` — your Gmail address (e.g. nacho@gmail.com)
- Leave `POLYGON_PRIVATE_KEY` blank for now
- `PAPER_TRADING=true`

**3. Copy config from template**
```powershell
Copy-Item config.template.json config.json
```
Edit `balance` to whatever you want as your paper trading starting balance.

**4. Set up virtual environment**
```powershell
scripts\setup_venv.ps1
```

**5. Activate venv (in VS Code: select the .venv interpreter, or in terminal)**
```powershell
.venv\Scripts\Activate.ps1
```

**6. Test the project works**
```powershell
python main.py probe      # one scan, no trades opened
python -m pytest tests/   # run all tests
```

---

### Personal Machine

**1. Pull latest code from GitHub**
```powershell
cd path\to\weatherbot
git pull origin master
```

**2. Set up virtual environment**
```powershell
scripts\setup_venv.ps1
.venv\Scripts\Activate.ps1
```

**3. Copy .env and fill in ALL values**
```powershell
Copy-Item .env.example .env
notepad .env
```
Fill in everything including the Gmail transfer variables:
- `GMAIL_ADDRESS` — your Gmail address
- `GMAIL_APP_PASSWORD` — see **Gmail App Password Setup** below
- `WORK_EMAIL` — your work Outlook address
- `VC_KEY` — Visual Crossing API key (same key as on work machine)
- `PAPER_TRADING=true` (until you're confident in live trading)

**4. Copy and configure config.json**
```powershell
Copy-Item config.template.json config.json
notepad config.json
```
Set `balance` to your actual starting USDC balance on Polymarket.

**5. Untrack config.json if still tracked by git**
```powershell
git ls-files config.json    # if this returns 'config.json', run next line:
git rm --cached config.json
git commit -m "chore: untrack config.json"
git push origin master
```

**6. Test**
```powershell
python main.py probe
```

---

### Gmail App Password Setup (Personal Machine Only)

Gmail requires an **App Password** (not your regular Gmail password) to send email via scripts.

1. Go to https://myaccount.google.com/security
2. Ensure **2-Step Verification** is ON (required)
3. Search for **"App passwords"** (or go to: https://myaccount.google.com/apppasswords)
4. Create a new app password: name it `WeatherBot`
5. Copy the 16-character code (e.g. `abcd efgh ijkl mnop`)
6. In your `.env` on the personal machine:
   ```
   GMAIL_APP_PASSWORD=abcdefghijklmnop
   ```
   (remove the spaces when pasting)

---

## Daily Workflow

### Sending Code: Work → Personal

When you've made changes at work and want them on the personal machine:

**On work machine (terminal in VS Code):**
```powershell
scripts\ship_to_personal.ps1
```

This will:
1. Commit any unsaved changes with a timestamp
2. Create an incremental git bundle (only new commits)
3. Tag the commit `shipped_YYYYMMDD_HHMM`
4. Send it via Outlook to your Gmail

**On personal machine:**
1. Open Gmail, find the email `[WeatherBot Code] YYYYMMDD_HHMM`
2. Download the `.bundle` attachment to your Downloads folder
3. Run:
```powershell
scripts\receive_bundle.ps1
```
This auto-detects the bundle from Downloads, applies it, and pushes to GitHub.

> **First time?** If no bundle exists on personal yet, run:
> `scripts\ship_to_personal.ps1 -Full`  (sends the full repo, not just diffs)

---

### Sending Data: Personal → Work

When you want to sync trade results back to the work machine for analysis:

**On personal machine:**
```powershell
python scripts\ship_data_back.py
```

This zips `data/` (markets, state, calibration) and emails it to your work Outlook.

**On work machine:**
1. Wait for the email `[WeatherBot Data] YYYYMMDD_HHMM` to arrive in Outlook
2. Run:
```powershell
scripts\receive_from_personal.ps1
```
This auto-detects the latest data email, downloads the zip, and extracts it into `data/`.

---

## Running the Bot (Personal Machine)

```powershell
# Activate venv first
.venv\Scripts\Activate.ps1

# Dry run — one scan, no positions opened
python main.py probe

# Check portfolio status
python main.py status

# Full trading loop (runs continuously)
python main.py

# Trade history report
python main.py report
```

---

## What Is and Is NOT Transferred

| File/Folder | In bundle? | In data zip? | Notes |
|---|---|---|---|
| `core/*.py` | YES | NO | All code |
| `scripts/*.ps1` / `.py` | YES | NO | Transfer scripts themselves |
| `requirements.txt` | YES | NO | |
| `.env.example` | YES | NO | Template only, not real keys |
| `config.template.json` | YES | NO | |
| `.env` | **NEVER** | **NEVER** | Contains secrets |
| `config.json` | **NEVER** | **NEVER** | Machine-specific |
| `data/markets/*.json` | NO | YES | Trade records |
| `data/state.json` | NO | YES | Portfolio balance |
| `data/calibration.json` | NO | YES | Forecast accuracy |
| `.venv/` | NEVER | NEVER | Too large, platform-specific |

---

## Troubleshooting

### "PERSONAL_EMAIL not set in .env" (work machine)
Open `.env` in the project root and add:
```
PERSONAL_EMAIL=your.gmail@gmail.com
```

### "Could not launch Outlook COM" (work machine)
Outlook must be open and logged in when running `ship_to_personal.ps1`.

### "Gmail authentication failed" (personal machine)
- You must use an **App Password**, not your regular Gmail password.
- See **Gmail App Password Setup** above.
- If your App Password has spaces, remove them.

### "No WeatherBot_CODE_*.bundle found in Downloads"
Either:
- The bundle wasn't downloaded from Gmail yet (download it first), or
- Specify the path explicitly: `scripts\receive_bundle.ps1 -BundlePath C:\path\to\file.bundle`

### "No emails found with [WeatherBot Data]" (work machine)
- Make sure Outlook is synced (click Send/Receive).
- The personal machine's `ship_data_back.py` must have run successfully.

### "VC_KEY is not set" when running main.py
Copy `.env.example` to `.env` and fill in `VC_KEY` from https://www.visualcrossing.com/weather-api

### Bundle pull fails with merge conflict
This would be unusual (personal should never commit code changes). If it happens:
```powershell
git stash          # stash any local changes
git pull bundle.bundle master
git stash pop      # reapply local changes if any
```

---

## Security Notes

- **Private key (`POLYGON_PRIVATE_KEY`)**: Only ever on the personal machine. Never in bundle, never in email.
- **App Password (`GMAIL_APP_PASSWORD`)**: Only in `.env` on personal machine.
- **VC_KEY**: Low-risk (free-tier weather API). Still only in `.env`.
- **config.json**: Never transferred. Contains your trading balance.
- All transfers are via email over HTTPS (encrypted in transit).
- Bundles contain only Python source code — no credentials.

---

## File Reference

| Script | Machine | What it does |
|---|---|---|
| `scripts/setup_venv.ps1` | Both | Create/update Python venv |
| `scripts/ship_to_personal.ps1` | Work | Bundle code + email via Outlook |
| `scripts/receive_from_personal.ps1` | Work | Receive data zip from Outlook |
| `scripts/receive_bundle.ps1` | Personal | Apply incoming code bundle |
| `scripts/ship_data_back.py` | Personal | Zip data + email via Gmail |
