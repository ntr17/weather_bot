"""Probe Polymarket API for weather market slug patterns."""
import requests
from datetime import datetime, timedelta, timezone

now = datetime.now(timezone.utc)
MONTHS = ['january','february','march','april','may','june','july','august',
          'september','october','november','december']

# Test highest + lowest temp for NYC across upcoming days
for offset in [0, 1, 2, 3, 4, 5, 6]:
    dt = now + timedelta(days=offset)
    month = MONTHS[dt.month - 1]
    day = dt.day
    year = dt.year
    for prefix in ['highest-temperature', 'lowest-temperature']:
        slug = f'{prefix}-in-new-york-city-on-{month}-{day}-{year}'
        url = f'https://gamma-api.polymarket.com/events?slug={slug}'
        try:
            r = requests.get(url, timeout=10)
            data = r.json()
            found = len(data) > 0 if isinstance(data, list) else False
            status = "FOUND" if found else "empty"
            print(f'{status}: {slug}')
            if found:
                title = data[0].get('title', '?')
                n = len(data[0].get('markets', []))
                print(f'  title: {title}')
                print(f'  markets: {n}')
        except Exception as e:
            print(f'ERROR: {slug} -> {e}')

# Also try some other patterns on a single date
dt = now + timedelta(days=1)
month = MONTHS[dt.month - 1]
day = dt.day
year = dt.year
other_patterns = [
    f'will-it-rain-in-new-york-city-on-{month}-{day}-{year}',
    f'will-it-snow-in-new-york-city-on-{month}-{day}-{year}',
    f'precipitation-in-new-york-city-on-{month}-{day}-{year}',
    f'average-temperature-in-new-york-city-on-{month}-{day}-{year}',
    f'temperature-in-new-york-city-on-{month}-{day}-{year}',
    f'high-temperature-in-new-york-city-on-{month}-{day}-{year}',
    f'low-temperature-in-new-york-city-on-{month}-{day}-{year}',
]
print('\n--- Other patterns ---')
for slug in other_patterns:
    url = f'https://gamma-api.polymarket.com/events?slug={slug}'
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        found = len(data) > 0 if isinstance(data, list) else False
        status = "FOUND" if found else "empty"
        print(f'{status}: {slug}')
    except Exception as e:
        print(f'ERROR: {slug} -> {e}')

print('\nDone')
