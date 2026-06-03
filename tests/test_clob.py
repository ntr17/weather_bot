"""Tests for CLOB live-trading preflight."""

from unittest.mock import Mock, patch

from core.clob import preflight_live_trading


def test_preflight_blocks_missing_credentials(monkeypatch):
    monkeypatch.delenv("PK", raising=False)
    monkeypatch.delenv("FUNDER", raising=False)

    ok, reason = preflight_live_trading(check_geoblock=False)

    assert not ok
    assert reason == "PK is not set"


def test_preflight_blocks_geoblocked_runner(monkeypatch):
    monkeypatch.setenv("PK", "private-key")
    monkeypatch.setenv("FUNDER", "0x123")
    response = Mock()
    response.json.return_value = {"blocked": True, "country": "US", "region": "NY"}
    response.raise_for_status.return_value = None

    with patch("core.clob.requests.get", return_value=response):
        ok, reason = preflight_live_trading(check_geoblock=True)

    assert not ok
    assert "geoblock active" in reason
    assert "country=US" in reason


def test_preflight_allows_unblocked_runner(monkeypatch):
    monkeypatch.setenv("PK", "private-key")
    monkeypatch.setenv("FUNDER", "0x123")
    response = Mock()
    response.json.return_value = {"blocked": False, "country": "ES", "region": "MD"}
    response.raise_for_status.return_value = None

    with patch("core.clob.requests.get", return_value=response):
        ok, reason = preflight_live_trading(check_geoblock=True)

    assert ok
    assert reason == ""
