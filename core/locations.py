"""
Static location data: airport ICAO coordinates, timezones, units.

Coordinates are for the AIRPORT (ICAO station), not city centre — this is the
core edge: Polymarket resolves on airport readings, most market participants
price on city-centre forecasts.
"""

from dataclasses import dataclass

MONTHS: list[str] = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
]


@dataclass(frozen=True)
class Location:
    lat: float
    lon: float
    name: str
    station: str   # ICAO code — what Polymarket resolves on
    unit: str      # "F" or "C"
    region: str    # "us" | "eu" | "asia" | "ca" | "sa" | "oc"


LOCATIONS: dict[str, Location] = {
    # ── US (Fahrenheit) ──────────────────────────────────────────────────────
    "nyc":          Location(40.7772,  -73.8726,  "New York City",  "KLGA", "F", "us"),
    "chicago":      Location(41.9742,  -87.9073,  "Chicago",        "KORD", "F", "us"),
    "miami":        Location(25.7959,  -80.2870,  "Miami",          "KMIA", "F", "us"),
    "dallas":       Location(32.8471,  -96.8518,  "Dallas",         "KDAL", "F", "us"),
    "seattle":      Location(47.4502, -122.3088,  "Seattle",        "KSEA", "F", "us"),
    "atlanta":      Location(33.6407,  -84.4277,  "Atlanta",        "KATL", "F", "us"),
    # ── Europe (Celsius) ─────────────────────────────────────────────────────
    "london":       Location(51.5048,    0.0495,  "London",         "EGLC", "C", "eu"),
    "paris":        Location(48.9962,    2.5979,  "Paris",          "LFPG", "C", "eu"),
    "munich":       Location(48.3537,   11.7750,  "Munich",         "EDDM", "C", "eu"),
    "ankara":       Location(40.1281,   32.9951,  "Ankara",         "LTAC", "C", "eu"),
    # ── Asia (Celsius) ───────────────────────────────────────────────────────
    "seoul":        Location(37.4691,  126.4505,  "Seoul",          "RKSI", "C", "asia"),
    "tokyo":        Location(35.7647,  140.3864,  "Tokyo",          "RJTT", "C", "asia"),
    "shanghai":     Location(31.1443,  121.8083,  "Shanghai",       "ZSPD", "C", "asia"),
    "singapore":    Location( 1.3502,  103.9940,  "Singapore",      "WSSS", "C", "asia"),
    "lucknow":      Location(26.7606,   80.8893,  "Lucknow",        "VILK", "C", "asia"),
    "tel-aviv":     Location(32.0114,   34.8867,  "Tel Aviv",       "LLBG", "C", "asia"),
    # ── Other ────────────────────────────────────────────────────────────────
    "toronto":      Location(43.6772,  -79.6306,  "Toronto",        "CYYZ", "C", "ca"),
    "sao-paulo":    Location(-23.4356, -46.4731,  "Sao Paulo",      "SBGR", "C", "sa"),
    "buenos-aires": Location(-34.8222, -58.5358,  "Buenos Aires",   "SAEZ", "C", "sa"),
    "wellington":   Location(-41.3272, 174.8052,  "Wellington",     "NZWN", "C", "oc"),
}

TIMEZONES: dict[str, str] = {
    "nyc":          "America/New_York",
    "chicago":      "America/Chicago",
    "miami":        "America/New_York",
    "dallas":       "America/Chicago",
    "seattle":      "America/Los_Angeles",
    "atlanta":      "America/New_York",
    "london":       "Europe/London",
    "paris":        "Europe/Paris",
    "munich":       "Europe/Berlin",
    "ankara":       "Europe/Istanbul",
    "seoul":        "Asia/Seoul",
    "tokyo":        "Asia/Tokyo",
    "shanghai":     "Asia/Shanghai",
    "singapore":    "Asia/Singapore",
    "lucknow":      "Asia/Kolkata",
    "tel-aviv":     "Asia/Jerusalem",
    "toronto":      "America/Toronto",
    "sao-paulo":    "America/Sao_Paulo",
    "buenos-aires": "America/Argentina/Buenos_Aires",
    "wellington":   "Pacific/Auckland",
}

# All cities in the scanner. The bot skips gracefully if Polymarket has no
# active temperature market for a city on a given day — zero risk from extras.
TIER1_CITIES: list[str] = list(LOCATIONS.keys())
