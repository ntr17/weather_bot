"""Tests for core/pricer.py — pure math functions, no I/O."""

import pytest
from core.pricer import bet_size, bucket_prob, calc_ev, calc_kelly, in_bucket, norm_cdf


class TestNormCdf:
    def test_midpoint_is_half(self) -> None:
        assert norm_cdf(0.0) == pytest.approx(0.5, abs=1e-6)

    def test_large_positive_approaches_one(self) -> None:
        assert norm_cdf(10.0) > 0.9999

    def test_large_negative_approaches_zero(self) -> None:
        assert norm_cdf(-10.0) < 0.0001

    def test_symmetry(self) -> None:
        assert norm_cdf(1.0) == pytest.approx(1.0 - norm_cdf(-1.0), abs=1e-9)


class TestInBucket:
    def test_within_range(self) -> None:
        assert in_bucket(45.5, 45.0, 46.0)

    def test_at_lower_bound(self) -> None:
        assert in_bucket(45.0, 45.0, 46.0)

    def test_at_upper_bound(self) -> None:
        assert in_bucket(46.0, 45.0, 46.0)

    def test_below_range(self) -> None:
        assert not in_bucket(44.9, 45.0, 46.0)

    def test_above_range(self) -> None:
        assert not in_bucket(46.1, 45.0, 46.0)

    def test_exact_single_degree(self) -> None:
        assert in_bucket(45.0, 45.0, 45.0)
        assert in_bucket(45.4, 45.0, 45.0)    # rounds to 45
        assert not in_bucket(45.6, 45.0, 45.0)  # rounds to 46


class TestBucketProb:
    def test_middle_bucket_in_is_not_one(self) -> None:
        # Forecast exactly in middle of a 1°F bucket, sigma=2°F.
        # CDF-based: Phi((46-45.5)/2) - Phi((45-45.5)/2) ≈ 0.20 — NOT 1.0
        p = bucket_prob(45.5, 45.0, 46.0, sigma=2.0)
        assert 0.10 < p < 0.40   # reasonable range, definitely not 1.0

    def test_middle_bucket_forecast_centred(self) -> None:
        # Wide bucket (70-73°F), forecast at centre 71.5°F, sigma=2°F.
        # Phi((73-71.5)/2) - Phi((70-71.5)/2) = Phi(0.75) - Phi(-0.75) ≈ 0.547
        p = bucket_prob(71.5, 70.0, 73.0, sigma=2.0)
        assert p == pytest.approx(0.547, abs=0.01)

    def test_middle_bucket_out_is_low_not_zero(self) -> None:
        # Forecast far outside bucket — probability low but not exactly 0
        p = bucket_prob(55.0, 45.0, 46.0, sigma=2.0)
        assert p < 0.001   # essentially zero

    def test_middle_bucket_adjacent_has_some_probability(self) -> None:
        # Forecast 72°F; adjacent bucket 73-76°F.
        # Even though forecast is outside, there's real probability mass there.
        p = bucket_prob(72.0, 73.0, 76.0, sigma=2.0)
        assert p > 0.10   # meaningful probability — was wrongly 0.0 before

    def test_higher_sigma_spreads_probability(self) -> None:
        # With larger sigma, more probability leaks into adjacent buckets
        p_tight = bucket_prob(72.0, 70.0, 73.0, sigma=1.0)
        p_wide  = bucket_prob(72.0, 70.0, 73.0, sigma=4.0)
        assert p_tight > p_wide   # tighter sigma → more concentrated

    def test_sigma_guard_no_division_by_zero(self) -> None:
        # sigma=0 should not crash
        p = bucket_prob(72.0, 70.0, 73.0, sigma=0.0)
        assert 0.0 <= p <= 1.0

    def test_lower_edge_bucket(self) -> None:
        # "40°F or below" — forecast well below threshold
        p = bucket_prob(35.0, -999.0, 40.0, sigma=2.0)
        assert p > 0.9   # forecast is 5°F below ceiling → very likely

    def test_lower_edge_bucket_above_threshold(self) -> None:
        p = bucket_prob(45.0, -999.0, 40.0, sigma=2.0)
        assert p < 0.1   # forecast is above ceiling → very unlikely

    def test_upper_edge_bucket(self) -> None:
        # "90°F or higher" — forecast well above threshold
        p = bucket_prob(95.0, 90.0, 999.0, sigma=2.0)
        assert p > 0.9

    def test_upper_edge_bucket_below_threshold(self) -> None:
        p = bucket_prob(85.0, 90.0, 999.0, sigma=2.0)
        assert p < 0.1


class TestCalcEv:
    def test_positive_ev(self) -> None:
        # p=0.8, price=$0.50 → EV = 0.8*(2-1) - 0.2 = 0.6
        assert calc_ev(0.8, 0.5) == pytest.approx(0.6, abs=0.001)

    def test_negative_ev(self) -> None:
        # p=0.2, price=$0.50 → EV = 0.2*(2-1) - 0.8 = -0.6
        assert calc_ev(0.2, 0.5) == pytest.approx(-0.6, abs=0.001)

    def test_zero_price_returns_zero(self) -> None:
        assert calc_ev(0.5, 0.0) == 0.0

    def test_one_price_returns_zero(self) -> None:
        assert calc_ev(0.5, 1.0) == 0.0

    def test_breakeven(self) -> None:
        # p == price → EV = 0
        assert calc_ev(0.3, 0.3) == pytest.approx(0.0, abs=0.001)


class TestCalcKelly:
    def test_positive_kelly(self) -> None:
        # Strong edge should yield positive Kelly
        k = calc_kelly(0.8, 0.3, kelly_fraction=1.0)
        assert k > 0

    def test_quarter_kelly_fraction(self) -> None:
        full = calc_kelly(0.8, 0.3, kelly_fraction=1.0)
        quarter = calc_kelly(0.8, 0.3, kelly_fraction=0.25)
        assert quarter == pytest.approx(full * 0.25, abs=0.001)

    def test_no_edge_returns_zero(self) -> None:
        # p == price → Kelly = 0
        assert calc_kelly(0.3, 0.3) == 0.0

    def test_negative_edge_clamped_to_zero(self) -> None:
        assert calc_kelly(0.1, 0.5) == 0.0

    def test_bounded_to_one(self) -> None:
        # Absurdly good edge — capped at 1.0
        assert calc_kelly(0.999, 0.01, kelly_fraction=1.0) <= 1.0


class TestBetSize:
    def test_basic_sizing(self) -> None:
        assert bet_size(0.1, 1000.0, 20.0) == pytest.approx(20.0)  # 10% of 1000 = 100, capped at 20

    def test_cap_applied(self) -> None:
        assert bet_size(0.5, 1000.0, 20.0) == 20.0

    def test_small_kelly(self) -> None:
        # 1% kelly on $100 balance = $1
        assert bet_size(0.01, 100.0, 20.0) == pytest.approx(1.0, abs=0.01)
