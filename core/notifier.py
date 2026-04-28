"""
Email notifications for trade events.

Sends a brief email via Gmail SMTP when a position is opened or closed.
Requires PERSONAL_EMAIL and GMAIL_APP_PASSWORD in .env (personal machine only).
If either var is missing, all calls silently no-op — safe to import everywhere.

Setup:
  1. Enable 2FA on your Google account.
  2. Go to myaccount.google.com > Security > App passwords.
  3. Create an app password, paste it into GMAIL_APP_PASSWORD in .env.
"""

import os
import smtplib
from email.message import EmailMessage

_TO = os.environ.get("PERSONAL_EMAIL", "")
_PW = os.environ.get("GMAIL_APP_PASSWORD", "")
_ENABLED = bool(_TO and _PW)


def _send(subject: str, body: str) -> None:
    if not _ENABLED:
        return
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = _TO
    msg["To"] = _TO
    msg.set_content(body)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as smtp:
            smtp.login(_TO, _PW)
            smtp.send_message(msg)
    except Exception as exc:
        print(f"  [NOTIFY] email failed: {exc}")


def trade_opened(city_name: str, date: str, bucket: str, ask: float,
                 ev: float, size: float, forecast_source: str) -> None:
    """Notify when a new position is opened."""
    _send(
        subject=f"WeatherBot BUY — {city_name} {date}",
        body=(
            f"Opened position\n\n"
            f"  City:    {city_name}\n"
            f"  Date:    {date}\n"
            f"  Bucket:  {bucket}\n"
            f"  Ask:     ${ask:.3f}\n"
            f"  EV:      {ev:+.2%}\n"
            f"  Size:    ${size:.2f}\n"
            f"  Source:  {forecast_source.upper()}\n"
        ),
    )


def trade_closed(city_name: str, date: str, bucket: str, entry: float,
                 exit_price: float, pnl: float, reason: str) -> None:
    """Notify when a position is closed."""
    sign = "+" if pnl >= 0 else ""
    _send(
        subject=f"WeatherBot {'WIN' if pnl >= 0 else 'LOSS'} — {city_name} {date}",
        body=(
            f"Closed position\n\n"
            f"  City:    {city_name}\n"
            f"  Date:    {date}\n"
            f"  Bucket:  {bucket}\n"
            f"  Entry:   ${entry:.3f}\n"
            f"  Exit:    ${exit_price:.3f}\n"
            f"  PnL:     {sign}{pnl:.2f}\n"
            f"  Reason:  {reason}\n"
        ),
    )


def daily_summary(balance: float, start: float, open_count: int,
                  wins: int, losses: int) -> None:
    """Send a brief daily summary (call from the trading loop if desired)."""
    ret = (balance - start) / start * 100
    sign = "+" if ret >= 0 else ""
    total = wins + losses
    wr = f"{wins/total:.0%}" if total else "—"
    _send(
        subject=f"WeatherBot daily — ${balance:,.0f} ({sign}{ret:.1f}%)",
        body=(
            f"Daily summary\n\n"
            f"  Balance:  ${balance:,.2f}  (start ${start:,.2f}, {sign}{ret:.1f}%)\n"
            f"  Trades:   {total} | W: {wins} | L: {losses} | WR: {wr}\n"
            f"  Open:     {open_count}\n"
        ),
    )
