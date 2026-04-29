"""
Probability, EV, and Kelly sizing math.

All functions are pure — no I/O, no side effects.
"""

import math


def norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bucket_prob(forecast: float, t_low: float, t_high: float, sigma: float = 2.0) -> float:
    """
    Probability that the actual reading lands in [t_low, t_high].

    Uses the normal CDF for all buckets — both edge and middle.
    A forecast of 72°F with sigma=2°F gives ~53% probability for the
    70–73°F bucket, not 100%. This correctly drives Kelly sizing.

    sigma = standard deviation of forecast error for this city+source+horizon,
    learned from historical data by calibrator.py / bootstrap_sigma.py.
    """
    sigma = max(sigma, 0.01)   # guard against zero sigma
    if t_low == -999.0:
        # "X or below" edge bucket — left tail.
        # Polymarket resolves on whole degrees, so "53°F or below" covers up to 53.5
        return norm_cdf((t_high + 0.5 - forecast) / sigma)
    if t_high == 999.0:
        # "X or higher" edge bucket — right tail.
        # "72°F or higher" starts at 71.5 in continuous space
        return 1.0 - norm_cdf((t_low - 0.5 - forecast) / sigma)
    # Middle / single-degree bucket: expand by ±0.5 to account for integer resolution.
    # "54-55°F" really covers readings that round to 54 or 55 → [53.5, 55.5].
    # "20°C" really covers readings that round to 20 → [19.5, 20.5].
    lo = t_low - 0.5
    hi = t_high + 0.5
    return norm_cdf((hi - forecast) / sigma) - norm_cdf((lo - forecast) / sigma)


def calc_ev(p: float, price: float) -> float:
    """
    Expected value of a YES position at given ask price.

    EV = p * (1/price - 1) - (1 - p)
    Positive EV means the bet is profitable in expectation.
    """
    if price <= 0.0 or price >= 1.0:
        return 0.0
    return round(p * (1.0 / price - 1.0) - (1.0 - p), 4)


def calc_kelly(p: float, price: float, kelly_fraction: float = 0.25) -> float:
    """
    Fractional Kelly criterion.

    Full Kelly f* = (p*b - (1-p)) / b  where b = (1/price - 1).
    Returns quarter-Kelly by default, clamped to [0, 1].
    """
    if price <= 0.0 or price >= 1.0:
        return 0.0
    b = 1.0 / price - 1.0
    if b <= 0.0:
        return 0.0
    f_full = (p * b - (1.0 - p)) / b
    return round(min(max(0.0, f_full) * kelly_fraction, 1.0), 4)


def bet_size(kelly: float, balance: float, max_bet: float) -> float:
    """Dollar amount to wager, capped at max_bet."""
    return round(min(kelly * balance, max_bet), 2)


def in_bucket(forecast: float, t_low: float, t_high: float) -> bool:
    """True if forecast falls within the bucket bounds (inclusive)."""
    if t_low == t_high:
        return round(forecast) == round(t_low)
    return t_low <= forecast <= t_high
