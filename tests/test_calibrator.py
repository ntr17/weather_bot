"""Tests for core/calibrator.py — sigma logic, no file I/O."""

from unittest.mock import patch

import pytest
from core.calibrator import get_sigma, run_calibration
from core.config import DEFAULT_SIGMA_C, DEFAULT_SIGMA_F


class TestGetSigma:
    def test_returns_default_f_when_no_calibration(self) -> None:
        sigma = get_sigma("nyc", "ecmwf", {})
        assert sigma == DEFAULT_SIGMA_F

    def test_returns_default_c_when_no_calibration(self) -> None:
        sigma = get_sigma("london", "ecmwf", {})
        assert sigma == DEFAULT_SIGMA_C

    def test_returns_calibrated_when_available(self) -> None:
        cal = {"nyc_ecmwf": {"sigma": 1.5, "n": 50}}
        assert get_sigma("nyc", "ecmwf", cal) == 1.5

    def test_unknown_city_returns_celsius_default(self) -> None:
        sigma = get_sigma("unknown_city", "ecmwf", {})
        assert sigma == DEFAULT_SIGMA_C


class TestRunCalibration:
    def _make_market(self, city: str, actual: float, forecast: float) -> dict:
        return {
            "city": city,
            "status": "resolved",
            "actual_temp": actual,
            "forecast_snapshots": [
                {"best": forecast, "best_source": "ecmwf"}
            ],
        }

    def test_no_update_below_minimum(self) -> None:
        """Should not update calibration when fewer than min resolved markets."""
        markets = [self._make_market("nyc", 50.0, 48.0) for _ in range(5)]
        with patch("core.calibrator.load_calibration", return_value={}), \
             patch("core.calibrator.save_calibration") as mock_save:
            result = run_calibration(markets, calibration_min=30)
        mock_save.assert_called_once()   # saves even if no updates
        assert "nyc_ecmwf" not in result

    def test_updates_after_minimum_reached(self) -> None:
        """Should calculate and store sigma after 30+ resolved markets."""
        # 30 markets with consistent 2°F error
        markets = [self._make_market("nyc", 50.0, 48.0) for _ in range(30)]
        with patch("core.calibrator.load_calibration", return_value={}), \
             patch("core.calibrator.save_calibration"):
            result = run_calibration(markets, calibration_min=30)
        assert "nyc_ecmwf" in result
        assert result["nyc_ecmwf"]["sigma"] == pytest.approx(2.0, abs=0.01)

    def test_skips_markets_without_actual_temp(self) -> None:
        markets = [
            {
                "city": "nyc",
                "status": "resolved",
                "actual_temp": None,  # no actual temp
                "forecast_snapshots": [{"best": 50.0, "best_source": "ecmwf"}],
            }
            for _ in range(30)
        ]
        with patch("core.calibrator.load_calibration", return_value={}), \
             patch("core.calibrator.save_calibration"):
            result = run_calibration(markets, calibration_min=30)
        assert "nyc_ecmwf" not in result
