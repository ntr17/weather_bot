"""
Verify that each city slug matches an active Polymarket temperature event.

Run on PERSONAL MACHINE (hits Polymarket API):
    python scripts/verify_slugs.py

Prints a table showing which cities have live markets today and the next
3 days. Any city that shows ALL "—" for every date is missing from
Polymarket and should be removed or its slug corrected in core/locations.py.

Also prints the actual Polymarket event title for each hit so you can
confirm the slug format manually.
"""

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from core.locations import LOCATIONS, MONTHS
from core.scanner import get_event


def main() -> None:
    now = datetime.now(timezone.utc)
    dates = [(now + timedelta(days=i)) for i in range(4)]
    date_strs = [d.strftime("%Y-%m-%d") for d in dates]

    print(f"\n{'='*70}")
    print(f"  POLYMARKET SLUG VERIFICATION — {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"  Checking dates: {' | '.join(date_strs)}")
    print(f"{'='*70}\n")

    header = f"{'City':<18} {'Slug':<18} " + "  ".join(f"D+{i}" for i in range(4))
    print(header)
    print("-" * len(header))

    hits = 0
    misses = []

    for city_slug, loc in LOCATIONS.items():
        row = f"{loc.name:<18} {city_slug:<18} "
        city_hits = 0
        first_title = None
        for i, dt in enumerate(dates):
            event = get_event(city_slug, dt.month, dt.day, dt.year)
            if event:
                row += " ✓  "
                city_hits += 1
                hits += 1
                if first_title is None:
                    first_title = event.get("title", event.get("slug", ""))
            else:
                row += " —  "
            time.sleep(0.2)   # polite to API
        print(row)
        if city_hits == 0:
            misses.append(city_slug)
        elif first_title:
            print(f"  └ event title: {first_title}")

    print(f"\n{'='*70}")
    print(f"  SUMMARY: {hits} events found | {len(misses)} cities with no events")
    if misses:
        print(f"\n  Cities with NO active markets:")
        for slug in misses:
            loc = LOCATIONS[slug]
            print(f"    {slug:<20} ({loc.name})")
        print()
        print("  Options:")
        print("  1. Polymarket hasn't launched markets for these cities yet.")
        print("  2. The slug format is wrong — check what Polymarket actually uses.")
        print("  3. Remove them from TIER1_CITIES in core/locations.py for now.")
        print()
        print("  To check the actual Polymarket slug format, search:")
        print("  https://gamma-api.polymarket.com/events?slug=highest-temperature-in-<city>-on-<month>-<day>-<year>")
    else:
        print("  All cities have active markets — slugs are correct!")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
