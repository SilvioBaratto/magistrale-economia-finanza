"""Numbers of the simulated appello 05 of Economia del Rischio e delle Assicurazioni.

Run from the repository root:
``python latex/esami/economia-rischio-assicurazioni/calc/appello_05.py``.
Every figure quoted by ``ERA_Esame_Simulato_05.md`` and ``ERA_Soluzioni_Simulato_05.md`` is
printed here, and each closed form is checked against a numerical derivative or a direct sum.
Section D (formulation and interpretation of the moral-hazard model) needs no numbers, and
the proof of E.2 only gets a numerical sanity check of the derivative formula it starts from.
"""

from __future__ import annotations

import itertools
import math
import statistics
from fractions import Fraction
from typing import Callable, Sequence

import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

from comune import (
    LOG,
    Outcomes,
    absolute_aversion,
    cara_utility,
    check,
    check_derivatives,
    close,
    covariance,
    crra_utility,
    expect,
    finite_derivative,
    float_outcomes,
    fmt,
    optimal_alpha,
    vector,
)

PERCENT = 100
GROSS_RISK_FREE = Fraction(1)

# Section A: agent 1 has u = ln W, agent 2 has CARA with rate CARA_RATE.
CARA_RATE = Fraction(1, 20)
LOTTERY_WEALTH = 25
LOTTERY_HALF_SPREAD = 15
LOW_WEALTH = 10
HIGH_WEALTH = 40
SMALL_HALF_SPREAD = 1
PROBE_WEALTH = 8.0

# Section B: B.1 calibration, B.2 two countries, B.3 a title in a three-state market.
DISPERSION = Fraction(3, 100)
MODEL_GAMMA = 5
OBSERVED_PREMIUM = Fraction(45, 1000)
APPROXIMATION_TOLERANCE = 0.02
COUNTRIES = 2
COUNTRY_VALUES = (Fraction(1), Fraction(3))
CONTRAST_GAMMA = 2
MARGINALS = {"ln": LOG.first, f"CRRA {CONTRAST_GAMMA}": crra_utility(CONTRAST_GAMMA).first}
MARKET_PAYOFFS = (Fraction(1), Fraction(3), Fraction(6))
TITLE_A_PAYOFFS = (Fraction(1), Fraction(0), Fraction(1))

# Section C: two uniform lotteries (supports) and two normals with the same mean.
UNIFORM_1_SUPPORT = (2, 6)
UNIFORM_2_SUPPORT = (4, 7)
NORMAL_MEAN = 10
NORMAL_VARIANCES = (4, 9)
GRID_SIZE = 2001
GRID_HALF_WIDTH_IN_SIGMAS = 8
CROSSING_PROBE_OFFSET = 1
QUADRATURE_HALF_WIDTH_IN_SIGMAS = 12
# u(x) = sign * exp(rate * x), stored as (sign, rate): e^x is strictly convex, -e^(-x) strictly
# concave, and both are strictly increasing on all of R, the support of the normals.
EXPONENTIAL_UTILITIES = {
    "u=exp(x), convex": (1, 1),
    "u=-exp(-x), concave": (-1, -1),
}

# Section E: CARA portfolio with net returns; agent 2 has twice the aversion of agent 1.
WEALTH = 100
NET_RISK_FREE = Fraction(5, 100)
RISKY_NET_RETURNS = (Fraction(-15, 100), Fraction(35, 100))
EQUAL_PROBABILITIES = [Fraction(1, len(RISKY_NET_RETURNS))] * len(RISKY_NET_RETURNS)
LAMBDA_1 = Fraction(2, 100)
LAMBDA_2 = Fraction(4, 100)
QUADRATIC_POWER = 2
CERTAIN_WEALTH = float(WEALTH * (1 + NET_RISK_FREE))
PHI_COEFFICIENT = float(LAMBDA_1**2 / LAMBDA_2)


def risk_measures() -> list[str]:
    """Return the A.1 lines: A(W) and RR(W) of both agents, checked against finite differences."""
    cara = cara_utility(float(CARA_RATE))
    for utility in (LOG, cara):
        check_derivatives(utility, PROBE_WEALTH)
    check(close(absolute_aversion(LOG, PROBE_WEALTH), 1 / PROBE_WEALTH), "A_1 is not 1/W")
    check(close(absolute_aversion(cara, PROBE_WEALTH), float(CARA_RATE)), "A_2 is not constant")
    return [
        "A.1  agent 1: A(W)=1/W, RR(W)=1: CRRA, not CARA",
        f"A.1  agent 2: A(W)={CARA_RATE}, RR(W)={CARA_RATE}*W: CARA, not CRRA",
    ]


def log_premium(wealth: int, half_spread: int) -> tuple[int, int]:
    """Return (CE, R) of the lottery +-half_spread at ``wealth`` for u = ln.

    E[ln(w+X)] = ln(sqrt(w^2 - b^2)): the certainty equivalent is an integer only if
    w^2 - b^2 is a perfect square, which keeps the exercise solvable by hand.
    """
    squared = wealth**2 - half_spread**2
    certainty_equivalent = math.isqrt(squared)
    check(certainty_equivalent**2 == squared, "CE is not an integer")
    expected_log = statistics.fmean(
        [math.log(wealth - half_spread), math.log(wealth + half_spread)]
    )
    check(close(expected_log, math.log(certainty_equivalent)), "E[ln(w+X)] differs from ln CE")
    return certainty_equivalent, wealth - certainty_equivalent


def lottery_premium() -> list[str]:
    """Return the A.2 line: certainty equivalent and risk premium of the A.2 lottery for u = ln."""
    certainty_equivalent, premium = log_premium(LOTTERY_WEALTH, LOTTERY_HALF_SPREAD)
    return [
        f"A.2  w={LOTTERY_WEALTH}, X=+-{LOTTERY_HALF_SPREAD}: "
        f"CE={certainty_equivalent}, R={premium}"
    ]


def premium_slope(wealth: int, half_spread: int) -> list[str]:
    """Return the A.3 lines: dR/dw = 1 - E[u'(w+X)] / u'(w-R) for u = ln and X = +-half_spread."""
    certainty_equivalent, _ = log_premium(wealth, half_spread)
    expected_marginal = expect(
        [Fraction(1, wealth - half_spread), Fraction(1, wealth + half_spread)]
    )
    slope = 1 - expected_marginal * certainty_equivalent
    numerical = finite_derivative(
        lambda at_wealth: at_wealth - math.sqrt(at_wealth * at_wealth - half_spread**2),
        float(wealth),
        1,
    )
    check(close(float(slope), numerical), "dR/dw disagrees with the finite difference")
    return [
        f"A.3  E[u'(w+X)]={expected_marginal}, u'(CE)=1/{certainty_equivalent}",
        f"A.3  dR/dw = 1 - {fmt(expected_marginal * certainty_equivalent)} = {fmt(slope)}",
    ]


def small_lottery_premiums(half_spread: int) -> list[str]:
    """Return the A.4 lines comparing the agents' premiums for a small lottery at two wealths."""
    rate = float(CARA_RATE)
    lines = [f"A.4  A_1(W)=1/W equals A_2={CARA_RATE} only at W={1 / CARA_RATE}"]
    for wealth in (LOW_WEALTH, HIGH_WEALTH):
        premium_log = wealth - math.sqrt(wealth**2 - half_spread**2)
        premium_cara = math.log(math.cosh(rate * half_spread)) / rate
        log_more_averse = Fraction(1, wealth) > CARA_RATE
        check(log_more_averse == (premium_log > premium_cara), "Arrow-Pratt order violated")
        lines.append(
            f"A.4  w={wealth}: A_1={Fraction(1, wealth)}, A_2={CARA_RATE}; exact premium for "
            f"X=+-{half_spread}: agent 1 {premium_log:.4f}, agent 2 {premium_cara:.4f}"
        )
    return lines


def crra_exact_premium(gamma: int) -> float:
    """Return the exact market premium of y = 1 +- DISPERSION (equiprobable) under CRRA(gamma)."""
    values = [1 - DISPERSION, 1 + DISPERSION]
    marginal = crra_utility(gamma).first
    weighted = expect([value * marginal(value) for value in values])
    return float(expect(values) * expect([marginal(value) for value in values]) / weighted - 1)


def calibration() -> list[str]:
    """Return the B.1 lines: premium for MODEL_GAMMA and the gamma matching OBSERVED_PREMIUM."""
    squared_variation = DISPERSION**2
    approximate = float(MODEL_GAMMA * squared_variation)
    required_gamma = OBSERVED_PREMIUM / squared_variation
    check(required_gamma.denominator == 1, "the gamma needed is not an integer")
    exact = crra_exact_premium(MODEL_GAMMA)
    check(
        abs(exact - approximate) < APPROXIMATION_TOLERANCE * approximate,
        "the approximation is too coarse for the model gamma",
    )
    exact_at_required = crra_exact_premium(int(required_gamma))
    return [
        f"B.1  Var/E^2={float(squared_variation)}; phi~{approximate * PERCENT:.2f}% "
        f"(exact {exact * PERCENT:.3f}%)",
        f"B.1  gamma needed for {float(OBSERVED_PREMIUM) * PERCENT:.1f}%: {fmt(required_gamma)} "
        f"(exact premium at that gamma {exact_at_required * PERCENT:.2f}%)",
    ]


def integrated_wealth(values: Sequence[Fraction]) -> list[Fraction]:
    """Return the consumption of the four equiprobable states with half of each title held."""
    return [sum(pair) / len(pair) for pair in itertools.product(values, repeat=COUNTRIES)]


def country_prices(
    marginal: Callable[[Fraction], Fraction], values: Sequence[Fraction]
) -> tuple[Fraction, Fraction]:
    """Return the domestic title's price in autarky and with integrated markets (i.i.d. values)."""
    own_values = [own for own, _ in itertools.product(values, repeat=COUNTRIES)]
    wealth_by_state = integrated_wealth(values)
    autarky = expect([value * marginal(value) for value in values]) / expect(
        [marginal(value) for value in values]
    )
    weighted_values = expect(
        [own * marginal(wealth) for own, wealth in zip(own_values, wealth_by_state, strict=True)]
    )
    integrated = weighted_values / expect([marginal(wealth) for wealth in wealth_by_state])
    return autarky / GROSS_RISK_FREE, integrated / GROSS_RISK_FREE


def market_premium(values: Sequence[Fraction], price: Fraction) -> Fraction:
    """Return E[y]/P - R_f, the market risk premium of a title."""
    return expect(values) / price - GROSS_RISK_FREE


def two_countries() -> list[str]:
    """Return the B.2 lines: prices and premiums with and without integration, ln and CRRA."""
    lines = []
    for label, marginal in MARGINALS.items():
        autarky, integrated = country_prices(marginal, COUNTRY_VALUES)
        premium_autarky = market_premium(COUNTRY_VALUES, autarky)
        premium_integrated = market_premium(COUNTRY_VALUES, integrated)
        lines.append(
            f"B.2  {label}: autarky P={fmt(autarky)}, phi={fmt(premium_autarky)}; integration "
            f"P={fmt(integrated)}, phi={fmt(premium_integrated)}; "
            f"ratio {fmt(premium_integrated / premium_autarky)}"
        )
    inverse_wealth = expect([1 / wealth for wealth in integrated_wealth(COUNTRY_VALUES)])
    lines.append(f"B.2  integration, u=ln: E[1/W]={fmt(inverse_wealth)}")
    return lines


def pricing_kernel(
    market: Sequence[Fraction], marginal: Callable[[Fraction], Fraction]
) -> list[Fraction]:
    """Return M = u'(y) / E[u'(y)] state by state, with y the value of the whole market."""
    marginals = [marginal(total) for total in market]
    return [value / expect(marginals) for value in marginals]


def covariance_determinant(first: Sequence[Fraction], second: Sequence[Fraction]) -> Fraction:
    """Return the determinant of the covariance matrix of two titles, which must be non-zero.

    With two states the titles would be collinear and only the sum of the shares would be pinned
    down; with three states the matrix is invertible and the equilibrium is unique.
    """
    determinant = covariance(first, first) * covariance(second, second) - covariance(
        first, second
    ) ** 2
    check(determinant != 0, "the covariance matrix of the two titles is singular")
    return determinant


def title_premium(
    market: Sequence[Fraction], title: Sequence[Fraction], marginal: Callable[[Fraction], Fraction]
) -> list[str]:
    """Return the B.3 lines: kernel, price, expected return and premium of ``title``.

    ``market - title`` is the second title b.
    """
    second_title = [total - own for total, own in zip(market, title, strict=True)]
    check(min(second_title) >= 0, "the second title would pay a negative amount")
    kernel = pricing_kernel(market, marginal)
    priced_payoff = expect([own * weight for own, weight in zip(title, kernel, strict=True)])
    price = priced_payoff / GROSS_RISK_FREE
    returns = [own / price for own in title]
    premium = expect(returns) - GROSS_RISK_FREE
    return_kernel_covariance = covariance(returns, kernel)
    check(premium == -return_kernel_covariance, "premium is not -Cov(R, M)")
    expected_product = expect(
        [gross_return * weight for gross_return, weight in zip(returns, kernel, strict=True)]
    )
    check(expected_product == GROSS_RISK_FREE, "E[R M] != R_f")
    return [
        f"B.3  kernel M={vector(kernel)}, E[M]={fmt(expect(kernel))}",
        f"B.3  P_a={fmt(price)}, E[R_a]={fmt(expect(returns))}, premium={fmt(premium)}",
        f"B.3  Cov(R_a, M)={fmt(return_kernel_covariance)}, "
        f"Cov(R_a, y)={fmt(covariance(returns, market))}",
        f"B.3  y_b={vector(second_title)}, det of the covariance matrix of (y_a, y_b) = "
        f"{fmt(covariance_determinant(title, second_title))}",
    ]


def uniform_cdf(support: tuple[int, int], point: int) -> Fraction:
    """Return the c.d.f. of the uniform distribution on ``support`` at ``point``."""
    low, high = support
    return min(Fraction(1), max(Fraction(0), Fraction(point - low, high - low)))


def first_order_dominance() -> list[str]:
    """Check F_2 <= F_1 for the two uniforms and return the C.1 lines with their c.d.f.

    Both c.d.f. are piecewise linear with breakpoints at the support ends, so their difference is
    linear between breakpoints and checking the breakpoints covers every x.
    """
    breakpoints = sorted({*UNIFORM_1_SUPPORT, *UNIFORM_2_SUPPORT})
    cdf_1 = [uniform_cdf(UNIFORM_1_SUPPORT, point) for point in breakpoints]
    cdf_2 = [uniform_cdf(UNIFORM_2_SUPPORT, point) for point in breakpoints]
    cdf_pairs = list(zip(cdf_1, cdf_2, strict=True))
    check(all(second <= first for first, second in cdf_pairs), "F_2 exceeds F_1")
    check(any(second < first for first, second in cdf_pairs), "F_1 equals F_2")
    supports = (UNIFORM_1_SUPPORT, UNIFORM_2_SUPPORT)
    means = [Fraction(sum(support), len(support)) for support in supports]
    return [
        f"C.1  breakpoints {breakpoints}: F_1={vector(cdf_1)}, F_2={vector(cdf_2)}",
        f"C.1  means E[X_1]={fmt(means[0])}, E[X_2]={fmt(means[1])}",
    ]


def integrated_cdf(variance: int, upper: float) -> float:
    """Return the integral of the N(NORMAL_MEAN, variance) c.d.f. from -inf to ``upper``.

    Closed form s [z Phi(z) + phi(z)] with z = (upper - mean) / s and s the standard deviation.
    """
    spread = math.sqrt(variance)
    standardised = (upper - NORMAL_MEAN) / spread
    return spread * (standardised * norm.cdf(standardised) + norm.pdf(standardised))


def second_order_dominance() -> list[str]:
    """Check the integrated c.d.f. ordering and the crossing; return the C.3 line."""
    low_variance, high_variance = NORMAL_VARIANCES
    half_width = GRID_HALF_WIDTH_IN_SIGMAS * math.sqrt(high_variance)
    grid = np.linspace(NORMAL_MEAN - half_width, NORMAL_MEAN + half_width, GRID_SIZE)
    gap = [
        integrated_cdf(high_variance, point) - integrated_cdf(low_variance, point) for point in grid
    ]
    check(min(gap) >= 0.0, "the integrated c.d.f. of the high-variance normal is not above")
    below = NORMAL_MEAN - CROSSING_PROBE_OFFSET
    low_cdf = norm.cdf(below, NORMAL_MEAN, math.sqrt(low_variance))
    high_cdf = norm.cdf(below, NORMAL_MEAN, math.sqrt(high_variance))
    check(low_cdf < high_cdf, "the c.d.f. do not cross at the mean")
    centre_gap = integrated_cdf(high_variance, NORMAL_MEAN) - integrated_cdf(
        low_variance, NORMAL_MEAN
    )
    return [
        f"C.3  Z_2 = Z_1 + N(0, {high_variance - low_variance}); integrated c.d.f. gap at the "
        f"mean {centre_gap:.4f}"
    ]


def exponential_moment_exponent(rate: int, variance: int) -> float:
    """Return rate*mu + rate^2*sigma^2/2, the exponent of E[exp(rate*Z)] for Z ~ N(mu, sigma^2).

    The moment generating function is not in the notes: it only controls the numerical integral.
    """
    return rate * NORMAL_MEAN + rate * rate * variance / 2


def integrated_expected_utility(sign: int, rate: int, variance: int) -> float:
    """Return E[sign * exp(rate * Z)] for Z ~ N(NORMAL_MEAN, variance) by numerical integration."""
    spread = math.sqrt(variance)
    half_width = QUADRATURE_HALF_WIDTH_IN_SIGMAS * spread
    value, _ = quad(
        lambda outcome: sign * math.exp(rate * outcome) * norm.pdf(outcome, NORMAL_MEAN, spread),
        NORMAL_MEAN - half_width,
        NORMAL_MEAN + half_width,
    )
    return value


def normal_expected_utilities() -> list[str]:
    """Return the C.3/C.4 lines: E[u(Z_1)] and E[u(Z_2)] for a convex and a concave utility.

    Z_2 is a mean-preserving spread of Z_1, so the theorem applied to u (concave) or to -u (convex)
    gives the preference: Z_1 for the concave utility, Z_2 for the convex one.
    """
    lines = []
    for label, (sign, rate) in EXPONENTIAL_UTILITIES.items():
        expected_utilities = []
        for variance in NORMAL_VARIANCES:
            integral = integrated_expected_utility(sign, rate, variance)
            exponent = exponential_moment_exponent(rate, variance)
            closed_form = sign * math.exp(exponent)
            check(close(integral, closed_form), f"{label}: integral differs from the closed form")
            expected_utilities.append(integral)
            lines.append(
                f"C.3/C.4  {label}, variance {variance}: E[u(Z)]={integral:.6f} "
                f"(closed form {sign:+d}*exp({exponent:g}))"
            )
        prefers_spread = expected_utilities[1] > expected_utilities[0]
        check(prefers_spread == (sign > 0), f"{label}: Z_1 and Z_2 are ordered the wrong way")
    return lines


def excess_outcomes() -> tuple[list[Fraction], Outcomes]:
    """Return the excess returns x = x0 - r and their float version for the numerical helpers."""
    excess = [net - NET_RISK_FREE for net in RISKY_NET_RETURNS]
    return excess, float_outcomes(excess, EQUAL_PROBABILITIES)


def cara_optimum(rate: Fraction) -> float:
    """Return alpha* = ln(gain / |loss|) / (rate (gain + |loss|)) for the two equiprobable states.

    Checked against the numerical maximiser. CARA makes alpha* independent of w0, so the helper's
    convention of bounding the amount by the wealth does not matter for an interior optimum.
    """
    (loss, gain), outcomes = excess_outcomes()
    closed_form = math.log(float(gain / -loss)) / (float(rate) * float(gain - loss))
    numerical = optimal_alpha(cara_utility(float(rate)).first, CERTAIN_WEALTH, outcomes)
    check(close(closed_form, numerical), "closed-form alpha* differs from the maximiser")
    check(0 < closed_form < WEALTH, "alpha* is not interior")
    return closed_form


def concave_map(value: float) -> float:
    """Return phi(t) = -(lambda_1^2 / lambda_2) t^2, the map with u_2 = phi(u_1) for t < 0.

    The identity needs lambda_2 = 2 lambda_1, since e^(-lambda_2 w) = (e^(-lambda_1 w))^2.
    """
    return -PHI_COEFFICIENT * value**QUADRATIC_POWER


def concave_map_lines() -> list[str]:
    """Check u_2 = phi(u_1) and that phi is strictly concave there; return the E.1 phi line."""
    check(LAMBDA_2 / LAMBDA_1 == QUADRATIC_POWER, "the quadratic phi needs lambda_2 = 2 lambda_1")
    utility_1, utility_2 = (cara_utility(float(rate)) for rate in (LAMBDA_1, LAMBDA_2))
    image = utility_1.level(PROBE_WEALTH)
    check(close(concave_map(image), utility_2.level(PROBE_WEALTH)), "u_2 differs from phi(u_1)")
    second = finite_derivative(concave_map, image, 2)
    check(second < 0, "phi is not concave")
    return [
        f"E.1  phi(t) = -{PHI_COEFFICIENT:g} t^{QUADRATIC_POWER} for t<0, "
        f"phi'' = {second:.4f} < 0"
    ]


def more_averse_agent() -> list[str]:
    """Return the E.1 lines: alpha*_1 and alpha*_2 of the two CARA agents and the map between."""
    (loss, gain), _ = excess_outcomes()
    optimum_1, optimum_2 = (cara_optimum(rate) for rate in (LAMBDA_1, LAMBDA_2))
    check(optimum_2 < optimum_1, "the more averse agent does not invest less")
    return [
        f"E.1  x = {vector([loss, gain])}; gain/|loss| = {fmt(gain / -loss)}",
        f"E.1  alpha*_1={optimum_1:.4f}, alpha*_2={optimum_2:.4f}, "
        f"ratio {optimum_2 / optimum_1:.4f}",
        *concave_map_lines(),
    ]


def wealth_effect() -> list[str]:
    """Check dalpha*/dw0 = -E[x(-u'')]/D for u = ln numerically; return the E.2 line."""
    _, outcomes = excess_outcomes()
    returns, probs = outcomes
    alpha = optimal_alpha(LOG.first, CERTAIN_WEALTH, outcomes)
    minus_second = -LOG.second(CERTAIN_WEALTH + alpha * returns)
    formula = -float(np.sum(probs * returns * minus_second)) / float(
        np.sum(probs * returns**2 * minus_second)
    )
    numerical = finite_derivative(
        lambda wealth: optimal_alpha(LOG.first, wealth, outcomes), CERTAIN_WEALTH, 1
    )
    check(close(formula, numerical), "the derivative formula disagrees with the numerical one")
    return [
        f"E.2  u=ln, w0={CERTAIN_WEALTH:g}: alpha*={alpha:.4f}, dalpha*/dw0={formula:.4f} "
        f"(numerical {numerical:.4f}), A'(w)=-1/w^2<0"
    ]


def main() -> None:
    """Print the numbers of every numerical question, in the order of the exam."""
    sections = (
        risk_measures(),
        lottery_premium(),
        premium_slope(LOTTERY_WEALTH, LOTTERY_HALF_SPREAD),
        small_lottery_premiums(SMALL_HALF_SPREAD),
        calibration(),
        two_countries(),
        title_premium(MARKET_PAYOFFS, TITLE_A_PAYOFFS, LOG.first),
        first_order_dominance(),
        second_order_dominance(),
        normal_expected_utilities(),
        more_averse_agent(),
        wealth_effect(),
    )
    for line in itertools.chain.from_iterable(sections):
        print(line)


if __name__ == "__main__":
    main()
