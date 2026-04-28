"""Tests for core/scanner.py — market parsing logic, no network calls."""

import pytest
from core.scanner import hours_to_resolution, parse_temp_range


class TestParseTempRange:
    def test_between_range(self) -> None:
        assert parse_temp_range("Will highest temperature be between 45-46°F") == (45.0, 46.0)

    def test_or_below(self) -> None:
        assert parse_temp_range("40°F or below") == (-999.0, 40.0)

    def test_or_higher(self) -> None:
        assert parse_temp_range("90°F or higher") == (90.0, 999.0)

    def test_exact_single(self) -> None:
        result = parse_temp_range("Will it be 45°F on Tuesday?")
        assert result == (45.0, 45.0)

    def test_celsius_between(self) -> None:
        result = parse_temp_range("between 10-11°C")
        assert result == (10.0, 11.0)

    def test_celsius_or_below(self) -> None:
        result = parse_temp_range("5°C or below")
        assert result == (-999.0, 5.0)

    def test_negative_temperature(self) -> None:
        result = parse_temp_range("-5°F or below")
        assert result == (-999.0, -5.0)

    def test_empty_string_returns_none(self) -> None:
        assert parse_temp_range("") is None

    def test_unrecognised_returns_none(self) -> None:
        assert parse_temp_range("will it rain?") is None


class TestHoursToResolution:
    def test_future_date_positive(self) -> None:
        from datetime import datetime, timedelta, timezone
        future = (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat()
        hours = hours_to_resolution(future)
        assert 23.0 < hours < 25.0

    def test_past_date_zero(self) -> None:
        from datetime import datetime, timedelta, timezone
        past = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        assert hours_to_resolution(past) == 0.0

    def test_empty_string_returns_999(self) -> None:
        assert hours_to_resolution("") == 999.0

    def test_invalid_string_returns_999(self) -> None:
        assert hours_to_resolution("not-a-date") == 999.0
