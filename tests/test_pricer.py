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
        # With ±0.5 expansion: [69.5, 73.5], Phi((73.5-71.5)/2) - Phi((69.5-71.5)/2)
        # = Phi(1.0) - Phi(-1.0) ≈ 0.683
        p = bucket_prob(71.5, 70.0, 73.0, sigma=2.0)
        assert p == pytest.approx(0.683, abs=0.01)

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

    # ── Single-degree (Celsius) bucket tests ─────────────────────────────
    def test_single_degree_bucket_nonzero(self) -> None:
        """The root cause bug: single-degree bucket (t_low == t_high) must NOT
        return 0.0. Tokyo 20°C with forecast 18.4°C should have real probability."""
        p = bucket_prob(18.4, 20.0, 20.0, sigma=1.2)
        assert p > 0.05  # ~14%, definitely not 0

    def test_single_degree_bucket_exact_forecast(self) -> None:
        """Forecast exactly on the bucket → should be the highest single-degree prob."""
        p = bucket_prob(20.0, 20.0, 20.0, sigma=1.2)
        assert 0.25 < p < 0.45  # ±0.5 captures ~33% of σ=1.2

    def test_single_degree_bucket_far_away(self) -> None:
        """Forecast 5σ away → effectively zero but not crash."""
        p = bucket_prob(26.0, 20.0, 20.0, sigma=1.2)
        assert p < 0.01

    def test_single_degree_bucket_adjacent(self) -> None:
        """Forecast 1°C away from a 1°C bucket → still meaningful probability."""
        p = bucket_prob(19.0, 20.0, 20.0, sigma=1.2)
        assert 0.05 < p < 0.30

    # ── Probability sum tests (mathematical consistency) ─────────────────
    def test_fahrenheit_buckets_sum_to_one(self) -> None:
        """Real NYC bucket structure: ≤53, 54-55, 56-57, ..., 70-71, ≥72.
        Because Polymarket resolves on whole °F readings, we expand 2°F
        ranges slightly — in practice the sum is close to 1.0."""
        buckets = [
            (-999.0, 53.0),
            (54.0, 55.0),
            (56.0, 57.0),
            (58.0, 59.0),
            (60.0, 61.0),
            (62.0, 63.0),
            (64.0, 65.0),
            (66.0, 67.0),
            (68.0, 69.0),
            (70.0, 71.0),
            (72.0, 999.0),
        ]
        forecast = 60.0
        sigma = 2.5
        total = sum(bucket_prob(forecast, lo, hi, sigma) for lo, hi in buckets)
        # Integer-gap buckets won't sum to exactly 1.0 but should be close
        assert total == pytest.approx(1.0, abs=0.10)

    def test_celsius_single_degree_buckets_sum_to_one(self) -> None:
        """Realistic Celsius single-degree buckets: ≤14, 15, 16, 17, 18, 19, 20, 21, 22, 23, ≥24.
        This is the actual Tokyo bucket structure."""
        buckets = [
            (-999.0, 14.0),
            (15.0, 15.0),
            (16.0, 16.0),
            (17.0, 17.0),
            (18.0, 18.0),
            (19.0, 19.0),
            (20.0, 20.0),
            (21.0, 21.0),
            (22.0, 22.0),
            (23.0, 23.0),
            (24.0, 999.0),
        ]
        forecast = 18.4
        sigma = 1.2
        total = sum(bucket_prob(forecast, lo, hi, sigma) for lo, hi in buckets)
        assert total == pytest.approx(1.0, abs=0.02)

    def test_celsius_buckets_peak_at_forecast(self) -> None:
        """The bucket containing the forecast should have the highest probability."""
        buckets = [
            (-999.0, 14.0), (15.0, 15.0), (16.0, 16.0), (17.0, 17.0),
            (18.0, 18.0), (19.0, 19.0), (20.0, 20.0), (21.0, 21.0),
            (22.0, 22.0), (23.0, 23.0), (24.0, 999.0),
        ]
        forecast = 18.4
        sigma = 1.2
        probs = {lo: bucket_prob(forecast, lo, hi, sigma) for lo, hi in buckets}
        # Bucket 18°C should have the highest probability
        assert probs[18.0] == max(probs.values())

    # ── NO position math ─────────────────────────────────────────────────
    def test_no_bet_requires_low_p_yes(self) -> None:
        """For a NO bet to make sense, p_yes should be very low (< 0.15).
        A single-degree bucket 1-2σ away should NOT be < 0.15."""
        # Forecast 18.4, bucket 20°C, sigma 1.2: ~14% — borderline
        p = bucket_prob(18.4, 20.0, 20.0, sigma=1.2)
        # This is ~0.14 — the NO filter requires p_yes < 0.15, so this
        # correctly blocks a NO bet on a bucket this close.
        assert p > 0.10  # meaningful, not zero

    def test_no_bet_safe_when_forecast_far(self) -> None:
        """NO on a bucket 4σ+ away is genuinely safe."""
        p = bucket_prob(18.4, 24.0, 24.0, sigma=1.2)
        assert p < 0.01  # safe to sell NO

    # ── Edge cases ───────────────────────────────────────────────────────
    def test_negative_temperatures(self) -> None:
        """Works with sub-zero Celsius readings."""
        p = bucket_prob(-5.0, -7.0, -3.0, sigma=1.5)
        assert 0.5 < p < 1.0

    def test_very_small_sigma(self) -> None:
        """Very confident forecast (sigma=0.1): almost all probability in one bucket."""
        p = bucket_prob(20.0, 20.0, 20.0, sigma=0.1)
        assert p > 0.95  # nearly certain

    def test_very_large_sigma(self) -> None:
        """Very uncertain forecast: probability spread thinly."""
        p = bucket_prob(20.0, 20.0, 20.0, sigma=10.0)
        assert p < 0.10  # lots of uncertainty


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

    def test_no_position_ev(self) -> None:
        """NO position EV: p_no = 1 - p_yes, price = 1 - yes_bid.
        If p_yes = 0.14, yes_bid = 0.10 → no_price = 0.90, p_no = 0.86.
        EV_no = 0.86 * (1/0.90 - 1) - 0.14 = 0.86*0.111 - 0.14 ≈ -0.044 (negative!)"""
        p_no = 0.86
        no_price = 0.90
        ev = calc_ev(p_no, no_price)
        assert ev < 0  # This should be a BAD bet — expensive NO token

    def test_no_position_ev_with_real_edge(self) -> None:
        """NO is a good bet when p_yes is genuinely tiny and NO is cheap.
        p_yes = 0.02, yes_bid = 0.15 → no_price = 0.85, p_no = 0.98.
        EV_no = 0.98*(1/0.85 - 1) - 0.02 = 0.98*0.176 - 0.02 ≈ 0.153 (positive)."""
        p_no = 0.98
        no_price = 0.85
        ev = calc_ev(p_no, no_price)
        assert ev > 0.10  # genuine edge

    def test_ev_at_fake_p1_was_the_bug(self) -> None:
        """With the old bug: p_no=1.0, no_price=0.47 → EV=1.13. Looked amazing.
        With real p_no=0.86, no_price=0.47 → EV=0.99. Still good but p is real.
        The key test: p=1.0 should NEVER appear in practice."""
        ev_fake = calc_ev(1.0, 0.47)
        ev_real = calc_ev(0.86, 0.47)
        assert ev_fake > ev_real  # fake p inflated the EV


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

    def test_kelly_with_no_position_no_edge(self) -> None:
        """Expensive NO token with marginal edge → Kelly should be tiny or zero."""
        # p_no=0.86, no_price=0.90 → EV is negative → Kelly = 0
        k = calc_kelly(0.86, 0.90, kelly_fraction=0.25)
        assert k == 0.0

    def test_kelly_with_no_position_real_edge(self) -> None:
        """Cheap NO token with real edge → Kelly should be positive but modest."""
        k = calc_kelly(0.98, 0.85, kelly_fraction=0.25)
        assert 0.0 < k < 0.25

    def test_kelly_prevents_ruin(self) -> None:
        """Even with strong edge, quarter-Kelly on a single bet should never
        risk more than 25% of bankroll."""
        k = calc_kelly(0.90, 0.20, kelly_fraction=0.25)
        assert k <= 0.25


class TestBetSize:
    def test_basic_sizing(self) -> None:
        assert bet_size(0.1, 1000.0, 20.0) == pytest.approx(20.0)  # 10% of 1000 = 100, capped at 20

    def test_cap_applied(self) -> None:
        assert bet_size(0.5, 1000.0, 20.0) == 20.0

    def test_small_kelly(self) -> None:
        # 1% kelly on $100 balance = $1
        assert bet_size(0.01, 100.0, 20.0) == pytest.approx(1.0, abs=0.01)
