#!/usr/bin/env python3
"""
Ship trade data back to the work machine via Gmail.

Run this on the PERSONAL machine when you want to sync data back to work.

SETUP (one-time):
  See WORKFLOW.md > Gmail App Password Setup

REQUIRED in .env:
  GMAIL_ADDRESS      -- your Gmail address
  GMAIL_APP_PASSWORD -- 16-char app password from Google Account settings
  WORK_EMAIL         -- your work Outlook email

WHAT GETS SENT:
  - data/markets/*.json   (all market records)
  - data/state.json       (portfolio state / balance)
  - data/calibration.json (forecast accuracy per city)

USAGE:
  python scripts/ship_data_back.py
"""

import os
import sys
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(REPO_ROOT / ".env")

GMAIL_ADDRESS      = os.environ.get("GMAIL_ADDRESS", "").strip()
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
WORK_EMAIL         = os.environ.get("WORK_EMAIL", "").strip()

DATA_FILES = [
    "state.json",
    "state.json.bak",
    "calibration.json",
    "calibration.json.bak",
]
DATA_DIRS = ["markets"]   # subdirectories to include in full

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
missing = [k for k, v in {
    "GMAIL_ADDRESS": GMAIL_ADDRESS,
    "GMAIL_APP_PASSWORD": GMAIL_APP_PASSWORD,
    "WORK_EMAIL": WORK_EMAIL,
}.items() if not v]

if missing:
    print(f"ERROR: Missing in .env: {', '.join(missing)}")
    print("See WORKFLOW.md > Gmail App Password Setup")
    sys.exit(1)

data_dir = REPO_ROOT / "data"
if not data_dir.exists():
    print(f"ERROR: data/ directory not found at {data_dir}")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Build zip
# ---------------------------------------------------------------------------
date_str = datetime.now().strftime("%Y%m%d_%H%M")
zip_path = REPO_ROOT / f"WeatherBot_Data_{date_str}.zip"

print(f"Packing data archive: {zip_path.name}")
file_count = 0

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    # Top-level data files
    for fname in DATA_FILES:
        fpath = data_dir / fname
        if fpath.exists():
            zf.write(fpath, fname)
            file_count += 1

    # Subdirectories
    for subdir in DATA_DIRS:
        subpath = data_dir / subdir
        if subpath.exists():
            for f in subpath.rglob("*"):
                if f.is_file():
                    zf.write(f, f.relative_to(data_dir))
                    file_count += 1

if file_count == 0:
    print("WARNING: No data files found in data/ — nothing useful to send.")
    zip_path.unlink(missing_ok=True)
    sys.exit(0)

zip_size_kb = zip_path.stat().st_size / 1024
print(f"  {file_count} files, {zip_size_kb:.1f} KB")

# ---------------------------------------------------------------------------
# Send via Gmail SMTP
# ---------------------------------------------------------------------------
print(f"Sending to {WORK_EMAIL} ...")

msg = MIMEMultipart()
msg["From"]    = GMAIL_ADDRESS
msg["To"]      = WORK_EMAIL
msg["Subject"] = f"[WeatherBot Data] {date_str}"

body = (
    f"WeatherBot trade data -- {date_str}\n\n"
    f"Files: {file_count} | Size: {zip_size_kb:.1f} KB\n\n"
    f"Apply on work machine:\n"
    f"  scripts\\receive_from_personal.ps1\n\n"
    f"(This is an automated transfer. Do not reply.)"
)
msg.attach(MIMEText(body, "plain"))

with open(zip_path, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment", filename=zip_path.name)
msg.attach(part)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(msg)
    print(f"Sent successfully.")
except smtplib.SMTPAuthenticationError:
    print("ERROR: Gmail authentication failed.")
    print("  1. Check GMAIL_APP_PASSWORD in .env (must be an App Password, not your login password).")
    print("  2. See WORKFLOW.md > Gmail App Password Setup.")
    zip_path.unlink(missing_ok=True)
    sys.exit(1)
except Exception as e:
    print(f"ERROR sending email: {e}")
    zip_path.unlink(missing_ok=True)
    sys.exit(1)

# Clean up temp zip
zip_path.unlink()
print("Done. Temp zip removed.")
