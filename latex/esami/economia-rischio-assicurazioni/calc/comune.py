"""Helpers shared by the calculation scripts of the simulated appelli.

The scripts run as ``python calc/appello_NN.py``, which puts this folder in ``sys.path``, so
``from comune import ...`` resolves without installing a package.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Sequence

import numpy as np
from scipy.optimize import brentq

Probabilities = Sequence[Fraction]
Outcomes = tuple[np.ndarray, np.ndarray]

FINITE_STEP = 1e-3
RELATIVE_TOLERANCE = 1e-4
ZERO_TOLERANCE = 1e-9
# Central-difference stencils per derivative order: (offset in steps, weight).
STENCILS = {
    1: ((-1, -0.5), (1, 0.5)),
    2: ((-1, 1.0), (0, -2.0), (1, 1.0)),
    3: ((-2, -0.5), (-1, 1.0), (1, -1.0), (2, 0.5)),
}


class CheckFailed(Exception):
    """Raised when a closed-form result disagrees with its numerical check.

    An explicit exception rather than ``assert``, so that ``python -O`` cannot skip the check.
    """


def check(condition: bool, message: str) -> None:
    """Raise ``CheckFailed`` with ``message`` unless ``condition`` holds.

    Args:
        condition: The verified statement.
        message: What a failure means, shown in the exception.

    Raises:
        CheckFailed: If ``condition`` is false.
    """
    if not condition:
        raise CheckFailed(message)


def close(first: float, second: float) -> bool:
    """Compare two floats within the shared tolerances.

    Args:
        first: One of the values.
        second: The other value.

    Returns:
        True if they agree to ``RELATIVE_TOLERANCE``, or to ``ZERO_TOLERANCE`` in absolute terms
        when both are near 0.
    """
    return math.isclose(first, second, rel_tol=RELATIVE_TOLERANCE, abs_tol=ZERO_TOLERANCE)


def fmt(value: Fraction | float) -> str:
    """Format a number for the printed solution.

    Args:
        value: An exact Fraction or a float.

    Returns:
        ``p/q (decimal)`` for a non-integer Fraction, the bare integer for an integral Fraction,
        and four decimals for a float.
    """
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value} ({float(value):.4f})"
    return f"{value:.4f}"


def vector(values: Sequence[Fraction]) -> str:
    """Format exact values as ``(a, b, c)``, each in its ``p/q`` form with no decimal part."""
    return "(" + ", ".join(str(value) for value in values) + ")"


def finite_derivative(func: Callable[[float], float], point: float, order: int) -> float:
    """Differentiate numerically with the central stencils of ``STENCILS``.

    The step grows with ``abs(point)`` so that the relative accuracy holds away from the origin.

    Args:
        func: Real function of one variable.
        point: Where to differentiate.
        order: Order of the derivative, 1 to 3.

    Returns:
        The finite-difference approximation of the ``order``-th derivative of ``func`` at ``point``.

    Raises:
        KeyError: If ``order`` has no stencil.
    """
    step = FINITE_STEP * max(1.0, abs(point))
    total = sum(weight * func(point + offset * step) for offset, weight in STENCILS[order])
    return total / step**order


def expect(values: Sequence[Fraction], probs: Probabilities | None = None) -> Fraction:
    """Compute an exact expected value.

    Args:
        values: The possible outcomes.
        probs: Their probabilities. ``None`` means equiprobable states.

    Returns:
        The expected value of ``values``.
    """
    if probs is None:
        return sum(values) * Fraction(1, len(values))
    return sum(value * prob for value, prob in zip(values, probs))


def covariance(
    first: Sequence[Fraction], second: Sequence[Fraction], probs: Probabilities | None = None
) -> Fraction:
    """Compute Cov(first, second) = E[first * second] - E[first] E[second] exactly.

    Args:
        first: Outcomes of the first variable, one per state.
        second: Outcomes of the second variable, in the same states.
        probs: State probabilities. ``None`` means equiprobable states.

    Returns:
        The covariance of the two variables.
    """
    products = [x * y for x, y in zip(first, second)]
    return expect(products, probs) - expect(first, probs) * expect(second, probs)


def float_outcomes(returns: Sequence[Fraction], probs: Probabilities) -> Outcomes:
    """Convert exact returns and probabilities into the float arrays the numerics expect.

    Args:
        returns: The possible values x of the risky title.
        probs: Their probabilities, in the same order.

    Returns:
        The pair ``(returns, probs)`` as float arrays.
    """
    return np.array([float(x) for x in returns]), np.array([float(p) for p in probs])


@dataclass(frozen=True)
class Utility:
    """A Bernoulli utility with its first three derivatives.

    Attributes:
        name: Label used in the printed output.
        level: Function u(w).
        first: Function u'(w).
        second: Function u''(w).
        third: Function u'''(w).
    """

    name: str
    level: Callable[[float], float]
    first: Callable[[float], float]
    second: Callable[[float], float]
    third: Callable[[float], float]


SQRT = Utility(
    "sqrt",
    math.sqrt,
    lambda w: 0.5 * w**-0.5,
    lambda w: -0.25 * w**-1.5,
    lambda w: 0.375 * w**-2.5,
)
LOG = Utility("ln", math.log, lambda w: 1 / w, lambda w: -(w**-2), lambda w: 2 * w**-3)


def crra_utility(gamma: float) -> Utility:
    """Build the CRRA utility w^(1-gamma)/(1-gamma).

    Args:
        gamma: Relative risk aversion. 1 gives the logarithm, the shared ``LOG``.

    Returns:
        The utility with its closed-form derivatives.
    """
    if gamma == 1.0:
        return LOG
    return Utility(
        f"CRRA {gamma:g}",
        lambda w: w ** (1 - gamma) / (1 - gamma),
        lambda w: w**-gamma,
        lambda w: -gamma * w ** (-gamma - 1),
        lambda w: gamma * (gamma + 1) * w ** (-gamma - 2),
    )


def cara_utility(rate: float) -> Utility:
    """Build the CARA utility -exp(-rate * w) / rate.

    Args:
        rate: Absolute risk aversion, constant in wealth.

    Returns:
        The utility with its closed-form derivatives.
    """
    return Utility(
        f"CARA {rate:g}",
        lambda w: -math.exp(-rate * w) / rate,
        lambda w: math.exp(-rate * w),
        lambda w: -rate * math.exp(-rate * w),
        lambda w: rate**2 * math.exp(-rate * w),
    )


def absolute_aversion(utility: Utility, wealth: float) -> float:
    """Return the Arrow-Pratt coefficient A(W) = -u''(W) / u'(W) of ``utility`` at ``wealth``."""
    return -utility.second(wealth) / utility.first(wealth)


def prudence(utility: Utility, wealth: float) -> float:
    """Return the absolute prudence P(W) = -u'''(W) / u''(W) of ``utility`` at ``wealth``."""
    return -utility.third(wealth) / utility.second(wealth)


def check_derivatives(utility: Utility, wealth: float) -> None:
    """Check the closed-form derivatives of ``utility`` against finite differences.

    Raises:
        CheckFailed: If any of the first three derivatives disagrees at ``wealth``.
    """
    for order, derivative in enumerate((utility.first, utility.second, utility.third), start=1):
        numerical = finite_derivative(utility.level, wealth, order)
        check(close(numerical, derivative(wealth)), f"{utility.name}: derivative {order} mismatch")


def expected_utility(
    level: Callable[[float], float], wealth: float, outcomes: Outcomes, scale: float = 1.0
) -> float:
    """Return E[u(wealth + scale * x)] for ``outcomes = (returns, probs)``.

    Args:
        level: The utility function u.
        wealth: Initial wealth.
        outcomes: Pair of arrays, the possible values x and their probabilities.
        scale: Amount invested in the risky title; 1 leaves the outcomes unscaled.
    """
    returns, probs = outcomes
    return float(sum(p * level(wealth + scale * x) for x, p in zip(returns, probs)))


def expected_slope(
    first: Callable[[float], float], wealth: float, outcomes: Outcomes, scale: float
) -> float:
    """Return V'(alpha) = E[x u'(wealth + alpha x)] for ``outcomes = (returns, probs)``.

    Args:
        first: The marginal utility u'.
        wealth: Initial wealth.
        outcomes: Pair of arrays, the possible values x and their probabilities.
        scale: Amount alpha invested in the risky title.
    """
    returns, probs = outcomes
    return float(sum(p * x * first(wealth + scale * x) for x, p in zip(returns, probs)))


def optimal_alpha(first: Callable[[float], float], wealth: float, outcomes: Outcomes) -> float:
    """Return the maximiser on [0, wealth] of E[u(wealth + alpha x)].

    The investable amount equals the initial wealth (r = 0), and V is concave, so the maximiser
    is the corner or the root of the slope.

    Args:
        first: The marginal utility u'.
        wealth: Initial wealth and upper bound of the amount invested.
        outcomes: Pair of arrays, the possible values x and their probabilities.
    """
    if expected_slope(first, wealth, outcomes, 0.0) <= 0:
        return 0.0
    if expected_slope(first, wealth, outcomes, wealth) >= 0:
        return wealth
    return brentq(lambda alpha: expected_slope(first, wealth, outcomes, alpha), 0.0, wealth)
