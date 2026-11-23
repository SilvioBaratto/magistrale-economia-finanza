"""Calculations behind the simulated appello 02 of Economia del Rischio e delle Assicurazioni.

The constants below are the data printed in ERA_Esame_Simulato_02.md. Every figure quoted in
ERA_Soluzioni_Simulato_02.md and in the answer key of piano/appello-02.json is printed by this
script. Exact rational results are Fractions, irrational ones are floats. Closed-form results are
checked against finite differences, root finding or constrained optimisation, and a disagreement
raises CheckFailed (an explicit exception, so ``python -O`` cannot skip it).

Run it with ``python appello_02.py``. It writes no file.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from functools import partial
from typing import Callable, Sequence

import numpy as np
from scipy.optimize import brentq, minimize

from comune import (
    LOG,
    SQRT,
    ZERO_TOLERANCE,
    Outcomes,
    Probabilities,
    Utility,
    absolute_aversion,
    cara_utility,
    check,
    check_derivatives,
    close,
    covariance,
    crra_utility,
    expect,
    expected_slope,
    expected_utility,
    finite_derivative,
    float_outcomes,
    fmt,
    optimal_alpha,
    prudence,
    vector,
)

SEED = 20260124
SOLVER_TOLERANCE = 1e-12
PERCENT = 100

# Domanda A: u1 = sqrt(W), u2 = ln(W); X = +-b with equal probability at wealth w.
GRID_A = (0.5, 1.0, 2.0, 4.0, 10.0, 29.0, 49.0)
WEALTH_A = 29
HALF_RANGE_A = 20
EQUAL_PROB_A = 0.5
COMPARISON_WEALTH_A = 4.0
RANDOM_LOTTERIES_A = 2000
RANDOM_OUTCOMES_A = 3
WEALTH_RANGE_A = (2.0, 60.0)
OUTCOME_SHARE_A = 0.9

# Domanda B: u = ln, R_f = 1, two equiprobable states in which the risky title pays 2 or 3.
STATES_B = (Fraction(2), Fraction(3))
STATE_PROB_B = Fraction(1, 2)
GROSS_RATE_B = Fraction(1)
TITLE_ONE_B = (Fraction(3, 2), Fraction(2))
TITLE_TWO_B = (Fraction(1, 2), Fraction(1))
PARTICIPATION_B = Fraction(1, 3)
PARTICIPATION_TABLE_B = (Fraction(1), Fraction(1, 2), Fraction(1, 3))
BRACKET_SHRINK_B = 0.99
TEST_PRICES_B = np.linspace(1.0, 5.0, 20)

# Domanda C: excess returns (-20%, +10%, +40%) and two pairs of distributions on them.
RETURNS_C = (Fraction(-1, 5), Fraction(1, 10), Fraction(2, 5))
F1_C = (Fraction(4, 10), Fraction(4, 10), Fraction(2, 10))
F2_C = (Fraction(3, 10), Fraction(3, 10), Fraction(4, 10))
F3_C = (Fraction(2, 6), Fraction(1, 6), Fraction(3, 6))
F4_C = (Fraction(1, 6), Fraction(3, 6), Fraction(2, 6))
NOISE_C = (Fraction(-3, 10), Fraction(0), Fraction(3, 10))
NOISE_PROBS_C = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
FLAT_LOTTERY_C = (Fraction(0), Fraction(1), Fraction(0))
SPREAD_LOTTERY_C = (Fraction(3, 10), Fraction(0), Fraction(7, 10))
WEALTH_C = 100.0
ALPHA_GRID_C = np.linspace(0.0, WEALTH_C, 21)
THRESHOLD_RANGE_C = (80.0, 140.0)
RANDOM_UTILITIES_C = 500
UTILITY_PIECES_C = 4
MIN_WEIGHT_C = 0.01
GAMMAS_C = (0.5, 1.0, 2.0, 3.0, 5.0, 8.0)
CARA_RATES_C = (0.005, 0.01, 0.05)
SHOWCASE_GAMMA_C = 5.0
RANDOM_MARGINALS_C = 1000
MIN_MARGINAL = 1e-3
ALPHA_TOLERANCE_C = 1e-7
# Four-point counterexample: the spread acts on the +40% outcome, where g can be convex.
COUNTER_RETURNS_C = (-0.1, 0.2, 0.4, 0.6)
COUNTER_SAFE_C = (1 / 20, 1 / 20, 17 / 20, 1 / 20)
COUNTER_RISKY_C = (1 / 20, 9 / 20, 1 / 20, 9 / 20)
COUNTER_SUBSISTENCE_C = 50.0
COUNTER_GAMMA_C = 6.0
# Index of the +40% outcome in COUNTER_RETURNS_C: the riskier lottery moves mass off it.
SPREAD_CENTRE_C = 2
# Closed form quoted in the solution of C.3: V3' - V4' = factor * sum(weights * marginals).
# Kept apart from F3_C and F4_C so that the check tests the hand derivation, not the data.
SLOPE_GAP_FACTOR_C = Fraction(1, 30)
SLOPE_GAP_WEIGHTS_C = (-1, -1, 2)

# Domanda D: a toy instance with u = ln, losses 0, 1, 2 and two effort levels.
WEALTH_D = 10.0
LOSSES_D = (0.0, 1.0, 2.0)
LOW_EFFORT = 0
HIGH_EFFORT = 1
PROBS_D = {LOW_EFFORT: (0.2, 0.3, 0.5), HIGH_EFFORT: (0.6, 0.3, 0.1)}
EFFORT_COST_D = {LOW_EFFORT: 0.0, HIGH_EFFORT: 0.05}
RESERVE_D = math.log(8.0)
START_LEVELS_D = (2.0, 2.0, 2.0)
SOLVER_ITERATIONS_D = 500
POLICY_TOLERANCE_D = 1e-4
TEST_MULTIPLIERS_D = (0.7, 0.3)
TEST_PREMIUM_D = 1.0
TEST_INDEMNITIES_D = (0.5, 1.2, 1.9)

# Domanda E: r = 0 so w0 = W; random three-outcome returns for the general checks.
WEALTH_E = 100.0
RANDOM_TRIALS_E = 3000
RANDOM_OUTCOMES_E = 3
RETURN_RANGE_E = (-0.8, 0.8)
ALPHA_TOLERANCE_E = 1e-7
SHOWCASE_RETURNS_E = (-0.10, 0.11)
SHOWCASE_PROBS_E = (0.5, 0.5)
SHOWCASE_SCALES_E = (1.0, 10.0, 100.0)
MIN_DRAWS_E = 100
MIN_PAIR_DRAWS_E = 50
UTILITY_POOL_E = (LOG, SQRT)


# --- Domanda A ---------------------------------------------------------------------------


def bracketed(value: Fraction) -> str:
    """Return ``value`` in parentheses when it is not an integer, so that 1/2/W reads (1/2)/W."""
    return str(value) if value.denominator == 1 else f"({value})"


def check_crra_measures(utility: Utility, gamma: Fraction) -> None:
    """Check A, RR, P and the sign of A' of a CRRA utility with exponent ``gamma`` on the grid."""
    for wealth in GRID_A:
        check_derivatives(utility, wealth)
        absolute = absolute_aversion(utility, wealth)
        check(close(absolute, float(gamma) / wealth), f"{utility.name}: A(W) = gamma/W")
        check(close(wealth * absolute, float(gamma)), f"{utility.name}: RR = gamma")
        check(close(prudence(utility, wealth), float(1 + gamma) / wealth), "P(W) = (1+g)/W")
        slope = finite_derivative(lambda w: absolute_aversion(utility, w), wealth, 1)
        check(close(slope, absolute * (absolute - prudence(utility, wealth))), "A' = A (A - P)")
        check(slope < 0, f"{utility.name}: A must be decreasing")


def a1_arrow_pratt() -> list[str]:
    """Check A, RR and P of sqrt and ln, DARA through P > A, and the comparison A2 >= A1."""
    lines = []
    for utility, gamma in ((SQRT, Fraction(1, 2)), (LOG, Fraction(1))):
        check_crra_measures(utility, gamma)
        coefficient, shifted = bracketed(gamma), bracketed(1 + gamma)
        lines.append(
            f"A.1  {utility.name}: A(W) = {coefficient}/W ; RR = {gamma} ; P(W) = {shifted}/W ;"
            f" P - A = 1/W > 0 ; A'(W) = -{coefficient}/W^2 < 0 (DARA)"
        )
    gaps = [absolute_aversion(LOG, w) - absolute_aversion(SQRT, w) for w in GRID_A]
    check(all(gap >= 0 for gap in gaps), "A2 must be at least A1 everywhere")
    lines.append("     A2(W) - A1(W) = 1/(2W) > 0 for every W: the agent with ln is more averse")
    return lines


def certain_equivalents_a() -> tuple[int, Fraction]:
    """Return ``(CE of ln, CE of sqrt)`` for the lottery +-HALF_RANGE_A at WEALTH_A."""
    low, high = WEALTH_A - HALF_RANGE_A, WEALTH_A + HALF_RANGE_A
    root_low, root_high = math.isqrt(low), math.isqrt(high)
    check(root_low**2 == low and root_high**2 == high, "w - b and w + b must be squares")
    return root_low * root_high, Fraction(root_low + root_high, 2) ** 2


def a2_certain_equivalents() -> list[str]:
    """Return CE and R of the two agents for X = +-20 at w = 29, checked on the utilities."""
    low, high = WEALTH_A - HALF_RANGE_A, WEALTH_A + HALF_RANGE_A
    ce_log, ce_sqrt = certain_equivalents_a()
    for utility, certain_equivalent in ((SQRT, float(ce_sqrt)), (LOG, float(ce_log))):
        expected = EQUAL_PROB_A * utility.level(low) + EQUAL_PROB_A * utility.level(high)
        check(close(utility.level(certain_equivalent), expected), f"{utility.name}: u(CE) = E[u]")
    return [
        f"A.2  w - b = {low}, w + b = {high} (squares of {math.isqrt(low)} and {math.isqrt(high)})",
        f"     agent 1 (sqrt): CE1 = {fmt(ce_sqrt)} ; R1 = w - CE1 = {fmt(WEALTH_A - ce_sqrt)}",
        f"     agent 2 (ln):   CE2 = {ce_log} ; R2 = w - CE2 = {WEALTH_A - ce_log}",
    ]


def transform_a(level: float) -> float:
    """Return phi(x) = 2 ln x, the function with u2 = phi(u1)."""
    return 2 * math.log(level)


def a3_concave_transform() -> list[str]:
    """Check u2 = phi(u1) with phi = 2 ln, phi'' and the formula linking it to A1 - A2."""
    for wealth in GRID_A:
        level = SQRT.level(wealth)
        check(close(transform_a(level), LOG.level(wealth)), "u2 must equal phi(u1)")
        second = finite_derivative(transform_a, level, 2)
        check(close(second, -2 / level**2), "phi''(x) must equal -2/x^2")
        factor = LOG.first(wealth) / SQRT.first(wealth) ** 2
        gap = absolute_aversion(SQRT, wealth) - absolute_aversion(LOG, wealth)
        check(close(factor * gap, second), "phi''(u1) must equal u2'/(u1')^2 (A1 - A2)")
        check(close(second, -2 / wealth), "phi''(u1(W)) must equal -2/W")
    wealth = COMPARISON_WEALTH_A
    factor = LOG.first(wealth) / SQRT.first(wealth) ** 2
    return [
        "A.3  phi(x) = 2 ln x ; phi'(x) = 2/x ; phi''(x) = -2/x^2 < 0 (phi is concave)",
        f"     phi''(u1(W)) = -2/W ; at W = {wealth:g}: {-2 / SQRT.level(wealth) ** 2:.4f}",
        f"     u2'/(u1')^2 = {factor:g} ; A1 - A2 = -1/(2W) ; product = -2/W",
    ]


def random_zero_mean_lottery(rng: np.random.Generator, wealth: float) -> Outcomes | None:
    """Draw a lottery with E[X] = 0 and w + X > 0, or return None if the draw is not admissible."""
    reach = OUTCOME_SHARE_A * wealth
    outcomes = rng.uniform(-reach, reach, size=RANDOM_OUTCOMES_A)
    probs = rng.dirichlet(np.ones(RANDOM_OUTCOMES_A))
    outcomes = outcomes - outcomes @ probs
    return None if np.any(wealth + outcomes <= 0) else (outcomes, probs)


def premium_gap_a(rng: np.random.Generator) -> tuple[float, float]:
    """Return ``(R2 - R1, phi(E[u1]) - E[phi(u1)])`` for one admissible random draw."""
    while True:
        wealth = rng.uniform(*WEALTH_RANGE_A)
        lottery = random_zero_mean_lottery(rng, wealth)
        if lottery is not None:
            break
    mean_sqrt = expected_utility(SQRT.level, wealth, lottery)
    mean_log = expected_utility(LOG.level, wealth, lottery)
    premium_sqrt = wealth - mean_sqrt**2
    premium_log = wealth - math.exp(mean_log)
    return premium_log - premium_sqrt, transform_a(mean_sqrt) - mean_log


def a4_premium_ordering() -> list[str]:
    """Check R2 >= R1 for random wealths and zero-mean lotteries, and the Jensen step."""
    rng = np.random.default_rng(SEED)
    draws = [premium_gap_a(rng) for _ in range(RANDOM_LOTTERIES_A)]
    premium_gaps, jensen_gaps = zip(*draws)
    check(min(premium_gaps) >= -ZERO_TOLERANCE, "R2 must be at least R1 for every lottery")
    check(min(jensen_gaps) >= -ZERO_TOLERANCE, "E[phi(u1)] must not exceed phi(E[u1])")
    return [
        f"A.4  {len(draws)} random zero-mean lotteries: smallest R2 - R1 = "
        f"{min(premium_gaps):.6f} >= 0",
        f"     Jensen step phi(E[u1]) - E[phi(u1)] >= 0, smallest value {min(jensen_gaps):.6f}",
    ]


# --- Domanda B ---------------------------------------------------------------------------


def marginal_utilities_b() -> list[Fraction]:
    """Return u'(y) = 1/y in the two states, for u = ln."""
    return [1 / state for state in STATES_B]


def representative_slope(quota: float, price: float) -> float:
    """Return V'(alpha) = E[(y - R_f P) u'(alpha y + (1 - alpha) R_f P)] for u = ln."""
    rate = float(GROSS_RATE_B)
    total = 0.0
    for state in STATES_B:
        payoff = float(state)
        wealth = quota * payoff + (1 - quota) * rate * price
        total += float(STATE_PROB_B) * (payoff - rate * price) / wealth
    return total


def optimal_quota(price: float) -> float:
    """Return the quota alpha with V'(alpha) = 0 at ``price``, on the positive-wealth bracket."""
    y_low, y_high = float(min(STATES_B)), float(max(STATES_B))
    lower = -BRACKET_SHRINK_B * price / (y_high - price)
    upper = BRACKET_SHRINK_B * price / (price - y_low)
    return brentq(lambda quota: representative_slope(quota, price), lower, upper)


def price_b(payoffs: Sequence[Fraction], marginal: Sequence[Fraction]) -> Fraction:
    """Return the price E[payoff m] / (R_f E[m]) of ``payoffs`` given the marginal utilities."""
    return expect([payoff * m for payoff, m in zip(payoffs, marginal)]) / (
        GROSS_RATE_B * expect(marginal)
    )


def b1_price_and_premium() -> list[str]:
    """Return P, R and phi of the representative agent with u = ln, checking alpha* = 1."""
    marginal = marginal_utilities_b()
    price = price_b(STATES_B, marginal)
    expected_payoff = expect(STATES_B)
    gross_return = expected_payoff / price
    check(abs(optimal_quota(float(price)) - 1) < ZERO_TOLERANCE, "the optimal quota must be 1")
    return [
        f"B.1  E[u'(y)] = {fmt(expect(marginal))} ; y u'(y) = 1 in every state",
        f"     P = {fmt(price)} ; E[y] = {fmt(expected_payoff)}",
        f"     R = E[y]/P = {fmt(gross_return)} ; "
        f"phi = R - R_f = {fmt(gross_return - GROSS_RATE_B)}",
    ]


def check_unit_quotas(prices: Sequence[Fraction]) -> None:
    """Check that holding every share of both titles satisfies the FOC of each title.

    With two states the two titles are collinear in their deviations from the mean, so only the
    FOCs are checked: they are necessary and, by concavity, sufficient for the optimum.
    """
    marginal = marginal_utilities_b()
    for title, price in zip((TITLE_ONE_B, TITLE_TWO_B), prices):
        excess = [payoff - GROSS_RATE_B * price for payoff in title]
        slope = expect([x * m for x, m in zip(excess, marginal)])
        check(slope == 0, "FOC of the title at alpha = 1")


def check_kernel_identities(kernel: Sequence[Fraction], prices: Sequence[Fraction]) -> None:
    """Check E[M] = 1, E[R M] = R_f and premium = -Cov(R, M) for both titles."""
    check(expect(kernel) == 1, "E[M] must equal 1")
    for title, price in zip((TITLE_ONE_B, TITLE_TWO_B), prices):
        returns = [payoff / price for payoff in title]
        check(expect([r * m for r, m in zip(returns, kernel)]) == GROSS_RATE_B, "E[R M] = R_f")
        premium = expect(returns) - GROSS_RATE_B
        check(premium == -covariance(returns, kernel), "premium must equal -Cov(R, M)")


def b2_pricing_kernel() -> list[str]:
    """Return the kernel, P2, the return and premium of title 2 and Cov(R2, M)."""
    marginal = marginal_utilities_b()
    kernel = [m / expect(marginal) for m in marginal]
    sums = [first + second for first, second in zip(TITLE_ONE_B, TITLE_TWO_B)]
    check(sums == list(STATES_B), "the two titles must add up to y")
    titles = (TITLE_ONE_B, TITLE_TWO_B)
    prices = [price_b(title, kernel) for title in titles]
    market_price = price_b(STATES_B, marginal)
    check(sum(prices) == market_price, "P1 + P2 must equal the price of y")
    check_kernel_identities(kernel, prices)
    check_unit_quotas(prices)
    returns_two = [payoff / prices[1] for payoff in TITLE_TWO_B]
    return [
        f"B.2  M = {vector(kernel)} in states y = {vector(STATES_B)} ; E[M] = {expect(kernel)}",
        f"     P1 = {fmt(prices[0])} ; P2 = {fmt(prices[1])} ; P1 + P2 = {fmt(sum(prices))}",
        f"     R2 = y2/P2 = {vector(returns_two)} ; E[R2] = {fmt(expect(returns_two))}",
        f"     premium E[R2] - R_f = {fmt(expect(returns_two) - GROSS_RATE_B)} ; "
        f"Cov(R2, M) = {fmt(covariance(returns_two, kernel))}",
        "     FOC of both titles E[(y_i - P_i)/y] = 0 at alpha_1 = alpha_2 = 1 (exact)",
    ]


def participant_wealth(state: Fraction, price: float, participation: float) -> float:
    """Return W_k = P + (y - P)/k, the wealth of a participant (R_f = 1)."""
    return price + (float(state) - price) / participation


def participation_foc(price: float, participation: float) -> float:
    """Return E[(y - P)/W_k], the FOC of a participant at alpha = 1/k, or NaN if W_k <= 0."""
    wealths = [participant_wealth(state, price, participation) for state in STATES_B]
    if min(wealths) <= 0:
        return math.nan
    return sum(
        float(STATE_PROB_B) * (float(state) - price) / wealth
        for state, wealth in zip(STATES_B, wealths)
    )


def quadratic_b(participation: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return ``(a, b, c)`` of a P^2 + b P + c = 0 for the FOC of the participants.

    With ``s = 1 - k`` and states ``y_1, y_2`` the FOC reads
    ``2 s P^2 - (1 + s)(y_1 + y_2) P + 2 y_1 y_2 = 0``.
    """
    spread = 1 - participation
    first, second = STATES_B
    return 2 * spread, -(1 + spread) * (first + second), 2 * first * second


def foc_numerator(price: float, participation: float) -> float:
    """Return E[(y - P)/W_k] times the product of the wealths of the two states."""
    wealths = [participant_wealth(state, price, participation) for state in STATES_B]
    products = (wealths[1], wealths[0])
    return sum(
        float(STATE_PROB_B) * (float(state) - price) * other
        for state, other in zip(STATES_B, products)
    )


def check_quadratic(participation: Fraction) -> None:
    """Check that the FOC numerator equals the quadratic divided by 2k for several prices."""
    a, b, c = (float(coefficient) for coefficient in quadratic_b(participation))
    k = float(participation)
    for price in TEST_PRICES_B:
        check(close(foc_numerator(price, k), (a * price**2 + b * price + c) / (2 * k)), "FOC form")


def integer_coefficients(coefficients: Sequence[Fraction]) -> tuple[int, ...]:
    """Scale Fraction coefficients by the least common multiple of their denominators."""
    scale = math.lcm(*(coefficient.denominator for coefficient in coefficients))
    return tuple(int(coefficient * scale) for coefficient in coefficients)


def exact_roots(participation: Fraction) -> tuple[Fraction, Fraction, tuple[int, ...], int]:
    """Return ``(smaller root, larger root, integer coefficients, discriminant)`` for ``k``."""
    a, b, c = integer_coefficients(quadratic_b(participation))
    discriminant = b * b - 4 * a * c
    root = math.isqrt(discriminant)
    check(root * root == discriminant, "the discriminant must be a perfect square")
    smaller, larger = sorted((Fraction(-b - root, 2 * a), Fraction(-b + root, 2 * a)))
    return smaller, larger, (a, b, c), discriminant


def admissible_price(participation: Fraction) -> float:
    """Return the price at which a participant's wealth stays positive in every state."""
    a, b, c = (float(coefficient) for coefficient in quadratic_b(participation))
    if a == 0:
        return -c / b
    return (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)


def participation_table() -> str:
    """Return P(k) and phi(k) for the values of ``k`` of the table, checking each FOC."""
    expected_payoff = float(expect(STATES_B))
    cells = []
    for participation in PARTICIPATION_TABLE_B:
        price = admissible_price(participation)
        check(abs(participation_foc(price, float(participation))) < ZERO_TOLERANCE, "table FOC")
        cells.append(
            f"k = {participation}: P = {price:.4f}, "
            f"phi = {expected_payoff / price - float(GROSS_RATE_B):.4f}"
        )
    return " | ".join(cells)


def b3_limited_participation() -> list[str]:
    """Solve the participants' FOC for k = 1/3, check the quadratic and tabulate phi(k)."""
    check(GROSS_RATE_B == 1, "the participation formulas assume R_f = 1")
    k = PARTICIPATION_B
    check_quadratic(k)
    smaller, larger, (a, b, c), discriminant = exact_roots(k)
    check(abs(participation_foc(float(smaller), float(k))) < ZERO_TOLERANCE, "FOC at P(k)")
    wealth_small = [participant_wealth(s, float(smaller), float(k)) for s in STATES_B]
    wealth_large = [participant_wealth(s, float(larger), float(k)) for s in STATES_B]
    check(min(wealth_small) > 0 > min(wealth_large), "only the smaller root gives wealth > 0")
    premium = expect(STATES_B) / smaller - GROSS_RATE_B
    return [
        f"B.3  k = {k}: W_k = y/k + (k-1)/k P = {1 / k} y + ({(k - 1) / k}) P",
        f"     FOC E[(y - P)/W_k] = 0 -> {a} P^2 {b:+d} P {c:+d} = 0 ; discriminant "
        f"{discriminant} = {math.isqrt(discriminant)}^2",
        f"     roots P = {smaller} and {larger} ; W_k at P = {smaller}: "
        f"{[round(w, 4) for w in wealth_small]} ; at P = {larger}: "
        f"{[round(w, 4) for w in wealth_large]} (negative)",
        f"     phi(k) = E[y]/P(k) - R_f = {fmt(premium)}",
        "     " + participation_table(),
    ]


def kernel_of(wealths: Sequence[Fraction]) -> list[Fraction]:
    """Return the normalised marginal utility 1/W (u = ln) of ``wealths``."""
    marginal = [1 / wealth for wealth in wealths]
    return [m / expect(marginal) for m in marginal]


def b4_participant_risk() -> list[str]:
    """Compare Var(W_k) with Var(y) and the kernel with and without limited participation."""
    k = PARTICIPATION_B
    price = exact_roots(k)[0]
    wealth = [state / k + (k - 1) / k * price for state in STATES_B]
    variance_y = covariance(STATES_B, STATES_B)
    variance_wealth = covariance(wealth, wealth)
    check(variance_wealth == variance_y / k**2, "Var(W_k) must equal Var(y)/k^2")
    kernel_k, kernel_one = kernel_of(wealth), kernel_of(STATES_B)
    market_premium = -covariance(STATES_B, kernel_k) / price
    check(
        market_premium == expect(STATES_B) / price - GROSS_RATE_B,
        "the premium from the kernel must equal E[y]/P(k) - R_f",
    )
    return [
        f"B.4  Var(y) = {fmt(variance_y)} ; Var(W_k) = {fmt(variance_wealth)} = Var(y)/k^2",
        f"     kernel with k = {k}: {vector(kernel_k)} ; Cov(y, M_k) = "
        f"{fmt(covariance(STATES_B, kernel_k))}",
        f"     kernel with k = 1: {vector(kernel_one)} ; Cov(y, M) = "
        f"{fmt(covariance(STATES_B, kernel_one))}",
    ]


# --- Domanda C ---------------------------------------------------------------------------


def cumulative(probs: Probabilities) -> tuple[Fraction, ...]:
    """Return the c.d.f. values at the outcomes of the exercise."""
    total, result = Fraction(0), []
    for prob in probs:
        total += prob
        result.append(total)
    return tuple(result)


def cdf_integrals(probs: Probabilities) -> tuple[Fraction, ...]:
    """Return the integral of the c.d.f. from the lowest outcome up to each outcome."""
    steps = [later - earlier for earlier, later in zip(RETURNS_C, RETURNS_C[1:])]
    areas, total = [Fraction(0)], Fraction(0)
    for level, step in zip(cumulative(probs), steps):
        total += level * step
        areas.append(total)
    return tuple(areas)


def random_increasing_utility(rng: np.random.Generator) -> Callable[[float], float]:
    """Draw an increasing piecewise-linear utility c0 w + sum c_j max(0, w - t_j)."""
    slopes = rng.uniform(0.0, 1.0, size=UTILITY_PIECES_C + 1)
    thresholds = rng.uniform(*THRESHOLD_RANGE_C, size=UTILITY_PIECES_C)
    base = MIN_WEIGHT_C + slopes[0]
    return lambda w: base * w + sum(s * max(0.0, w - t) for s, t in zip(slopes[1:], thresholds))


def random_concave_utility(rng: np.random.Generator) -> Callable[[float], float]:
    """Draw an increasing concave utility sum c_j min(w, t_j) with c_j > 0."""
    weights = rng.uniform(MIN_WEIGHT_C, 1.0, size=UTILITY_PIECES_C)
    thresholds = rng.uniform(*THRESHOLD_RANGE_C, size=UTILITY_PIECES_C)
    return lambda w: sum(c * min(w, t) for c, t in zip(weights, thresholds))


def square(wealth: float) -> float:
    """Return the convex utility w^2, used to show that concavity is needed for the order."""
    return wealth**2


def signed_points(value: Fraction) -> str:
    """Return ``value`` in percentage points with an explicit sign, and a bare 0 for zero."""
    points = value * PERCENT
    return f"{float(points):+g}" if points else "0"


def return_outcomes(probs: Probabilities) -> Outcomes:
    """Return the returns of the exercise and ``probs`` as float arrays."""
    return float_outcomes(RETURNS_C, probs)


def smallest_gap(
    better: Probabilities, worse: Probabilities, draw: Callable[[np.random.Generator], Callable]
) -> float:
    """Return min over random utilities and alphas of E_better[u] - E_worse[u]."""
    rng = np.random.default_rng(SEED)
    better_outcomes, worse_outcomes = return_outcomes(better), return_outcomes(worse)
    worst = math.inf
    for _ in range(RANDOM_UTILITIES_C):
        level = draw(rng)
        for alpha in ALPHA_GRID_C:
            gap = expected_utility(level, WEALTH_C, better_outcomes, alpha) - expected_utility(
                level, WEALTH_C, worse_outcomes, alpha
            )
            worst = min(worst, gap)
    return worst


def c1_first_order() -> list[str]:
    """Check F2 FOSD F1 on the c.d.f.s and E_F2[u] >= E_F1[u] for random increasing u."""
    cdf1, cdf2 = cumulative(F1_C), cumulative(F2_C)
    check(all(b <= a for a, b in zip(cdf1, cdf2)), "F2 must be below F1 everywhere")
    check(any(b < a for a, b in zip(cdf1, cdf2)), "F2 must be strictly below F1 somewhere")
    worst = smallest_gap(F2_C, F1_C, random_increasing_utility)
    check(worst >= -ZERO_TOLERANCE, "E_F2[u] must be at least E_F1[u]")
    return [
        f"C.1  F1 = {vector(F1_C)} ; F2 = {vector(F2_C)} on returns {vector(RETURNS_C)}",
        f"     c.d.f.: F1 = {vector(cdf1)} ; F2 = {vector(cdf2)} ; F2 <= F1 everywhere (FOSD)",
        f"     {RANDOM_UTILITIES_C} random increasing u, alpha >= 0: smallest E_F2[u] - E_F1[u] = "
        f"{max(worst, 0.0):.6f} >= 0",
    ]


def higher_mean_without_fosd() -> str:
    """Check that a higher mean does not give FOSD and describe the pair used as a reminder."""
    flat, spread = FLAT_LOTTERY_C, SPREAD_LOTTERY_C
    cdf_flat, cdf_spread = cumulative(flat), cumulative(spread)
    check(expect(RETURNS_C, spread) > expect(RETURNS_C, flat), "the spread pair has a higher mean")
    check(not all(a <= b for a, b in zip(cdf_spread, cdf_flat)), "no FOSD of spread over flat")
    cap = RETURNS_C[1]
    capped = [min(float(x), float(cap)) for x in RETURNS_C]
    value_flat = sum(float(p) * v for p, v in zip(flat, capped))
    value_spread = sum(float(p) * v for p, v in zip(spread, capped))
    check(value_spread < value_flat, "the capped utility must prefer the flat lottery")
    return (
        f"higher mean without FOSD: G1 = {vector(flat)} (mean {fmt(expect(RETURNS_C, flat))}), "
        f"G2 = {vector(spread)} (mean {fmt(expect(RETURNS_C, spread))}); c.d.f. G1 = "
        f"{vector(cdf_flat)}, G2 = {vector(cdf_spread)}; u = min(x, {float(cap):.0%}): "
        f"E[u(G1)] = {value_flat:.4f} > E[u(G2)] = {value_spread:.4f}"
    )


def c2_means() -> list[str]:
    """Compare the means, check the c.d.f. identity and a higher-mean pair without FOSD."""
    mean1, mean2 = expect(RETURNS_C, F1_C), expect(RETURNS_C, F2_C)
    check(mean2 > mean1, "F2 must have the larger mean")
    area_gap = cdf_integrals(F1_C)[-1] - cdf_integrals(F2_C)[-1]
    check(area_gap == mean2 - mean1, "E_F2 - E_F1 must equal the area between the c.d.f.s")
    return [
        f"C.2  E[F1] = {fmt(mean1)} ; E[F2] = {fmt(mean2)} ; difference = {fmt(mean2 - mean1)}"
        " = area between the c.d.f.s",
        "     " + higher_mean_without_fosd(),
    ]


def check_noise_decomposition() -> Fraction:
    """Check that F4 plus the noise at the middle outcome gives F3; return the noise mean."""
    noise_mean = sum(n * p for n, p in zip(NOISE_C, NOISE_PROBS_C))
    check(noise_mean == 0, "the noise at the middle outcome must have zero mean")
    rebuilt = (
        F4_C[0] + F4_C[1] * NOISE_PROBS_C[0],
        F4_C[1] * NOISE_PROBS_C[1],
        F4_C[2] + F4_C[1] * NOISE_PROBS_C[2],
    )
    check(rebuilt == F3_C, "F4 plus the noise must give F3")
    moved = [RETURNS_C[1] + noise for noise in NOISE_C]
    check(moved == list(RETURNS_C), "the noise must move the middle outcome onto the others")
    check(expect(RETURNS_C, F3_C) == expect(RETURNS_C, F4_C), "F3 and F4 must have equal means")
    return noise_mean


def showcase_optima() -> tuple[list[float], list[float]]:
    """Return the optimal alpha and the maximal utility with F3 and F4 for CRRA gamma = 5."""
    utility = crra_utility(SHOWCASE_GAMMA_C)
    alphas, values = [], []
    for probs in (F3_C, F4_C):
        outcomes = return_outcomes(probs)
        alpha = optimal_alpha(utility.first, WEALTH_C, outcomes)
        alphas.append(alpha)
        values.append(expected_utility(utility.level, WEALTH_C, outcomes, alpha))
    return alphas, values


def c3_second_order() -> list[str]:
    """Check the noise decomposition, the c.d.f. integrals and the preference for F4."""
    noise_mean = check_noise_decomposition()
    areas3, areas4 = cdf_integrals(F3_C), cdf_integrals(F4_C)
    check(all(a >= b for a, b in zip(areas3, areas4)), "F4 must dominate F3 at the second order")
    worst = smallest_gap(F4_C, F3_C, random_concave_utility)
    check(worst >= -ZERO_TOLERANCE, "E_F4[u] must be at least E_F3[u] for concave u")
    convex_utility = partial(expected_utility, square, WEALTH_C, scale=WEALTH_C)
    convex_gap = convex_utility(return_outcomes(F3_C)) - convex_utility(return_outcomes(F4_C))
    check(convex_gap > 0, "a convex utility must reverse the order")
    alphas, values = showcase_optima()
    check(values[1] > values[0], "the optimum with F4 must be strictly better")
    middle_return = f"{float(RETURNS_C[1]):+.0%}"
    noise_points = " / ".join(signed_points(noise) for noise in NOISE_C)
    return [
        f"C.3  F3 = {vector(F3_C)} ; F4 = {vector(F4_C)} ; E = {fmt(expect(RETURNS_C, F3_C))}",
        f"     F3 = F4 + noise: from {middle_return} the noise is {noise_points} points with "
        f"probability {vector(NOISE_PROBS_C)} ; conditional mean {noise_mean}",
        f"     integrals of the c.d.f. at the outcomes: F3 {vector(areas3)} ; F4 {vector(areas4)}",
        f"     {RANDOM_UTILITIES_C} random concave u: smallest E_F4[u] - E_F3[u] over alpha = "
        f"{max(worst, 0.0):.6f} >= 0 ; with u = x^2 the order reverses by {convex_gap:.2f}",
        f"     CRRA gamma = {SHOWCASE_GAMMA_C:g}, w0 = W = {WEALTH_C:g}: "
        f"alpha3* = {alphas[0]:.4f}, alpha4* = {alphas[1]:.4f} ; "
        f"V3* = {values[0]:.6e} < V4* = {values[1]:.6e}",
    ]


def largest_slope_gap() -> float:
    """Return the largest V3'(alpha) - V4'(alpha) over random decreasing marginal utilities.

    For the three-outcome pair of C.3 the gap equals (1/30)(-m1 - m2 + 2 m3) with m the marginal
    utilities at the three final wealths, so it is never positive when u is concave.
    """
    rng = np.random.default_rng(SEED)
    largest = -math.inf
    for _ in range(RANDOM_MARGINALS_C):
        marginals = np.sort(rng.uniform(MIN_MARGINAL, 1.0, size=len(RETURNS_C)))[::-1]
        slope3 = sum(float(p * x) * m for p, x, m in zip(F3_C, RETURNS_C, marginals))
        slope4 = sum(float(p * x) * m for p, x, m in zip(F4_C, RETURNS_C, marginals))
        closed = float(SLOPE_GAP_FACTOR_C) * float(np.dot(SLOPE_GAP_WEIGHTS_C, marginals))
        check(close(slope3 - slope4, closed), "the slope gap identity must hold")
        largest = max(largest, slope3 - slope4)
    return largest


def counter_example_amounts() -> tuple[float, float]:
    """Return ``(alpha of the riskier, alpha of the less risky)`` for the four-outcome case."""

    def first(wealth: float) -> float:
        """Return u'(w) = (w - s)^(-gamma) of the shifted CRRA utility."""
        return (wealth - COUNTER_SUBSISTENCE_C) ** -COUNTER_GAMMA_C

    risky, safe = np.array(COUNTER_RISKY_C), np.array(COUNTER_SAFE_C)
    returns = np.array(COUNTER_RETURNS_C)
    check(close(float(risky @ returns), float(safe @ returns)), "counterexample means must agree")
    moved = (safe[SPREAD_CENTRE_C] - risky[SPREAD_CENTRE_C]) / 2
    spread = np.zeros(len(risky))
    spread[SPREAD_CENTRE_C - 1] = spread[SPREAD_CENTRE_C + 1] = moved
    spread[SPREAD_CENTRE_C] = -2 * moved
    check(np.allclose(risky - safe, spread), "the riskier lottery must spread the +40% outcome")
    alphas = [optimal_alpha(first, WEALTH_C, (returns, probs)) for probs in (risky, safe)]
    lowest_wealth = min(WEALTH_C + alpha * min(COUNTER_RETURNS_C) for alpha in alphas)
    check(lowest_wealth > COUNTER_SUBSISTENCE_C, "wealth must stay above the subsistence level")
    return alphas[0], alphas[1]


def three_outcome_amounts() -> list[str]:
    """Return ``alpha3*/alpha4*`` for CRRA and CARA utilities, checking alpha3* <= alpha4*."""
    outcomes3, outcomes4 = return_outcomes(F3_C), return_outcomes(F4_C)
    rows = []
    for utility in [crra_utility(g) for g in GAMMAS_C] + [cara_utility(r) for r in CARA_RATES_C]:
        alpha3 = optimal_alpha(utility.first, WEALTH_C, outcomes3)
        alpha4 = optimal_alpha(utility.first, WEALTH_C, outcomes4)
        ordered = alpha3 <= alpha4 + ALPHA_TOLERANCE_C
        check(ordered, f"{utility.name}: alpha3* must not exceed alpha4*")
        rows.append(f"{utility.name}: {alpha3:.2f}/{alpha4:.2f}")
    return rows


def c4_amounts_not_ordered() -> list[str]:
    """Show that SOSD alone does not order the optimal amounts, while the 3-outcome pair does."""
    alpha_risky, alpha_safe = counter_example_amounts()
    check(alpha_risky > alpha_safe, "the counterexample needs the riskier title to attract more")
    largest = largest_slope_gap()
    check(largest <= ZERO_TOLERANCE, "V3' must not exceed V4' for the three-outcome pair")
    gamma = f"{COUNTER_GAMMA_C:g}"
    mean = float(np.array(COUNTER_SAFE_C) @ np.array(COUNTER_RETURNS_C))
    return [
        "C.4  counterexample, SOSD without ordered amounts (four outcomes, "
        f"w0 = W = {WEALTH_C:g}):",
        f"     returns {COUNTER_RETURNS_C}, less risky "
        f"{tuple(round(p, 2) for p in COUNTER_SAFE_C)}, "
        f"riskier {tuple(round(p, 2) for p in COUNTER_RISKY_C)}",
        f"     common mean = {mean:.4f}",
        f"     u'(w) = (w - {COUNTER_SUBSISTENCE_C:g})^-{gamma}: "
        f"alpha(riskier) = {alpha_risky:.4f} > alpha(less risky) = {alpha_safe:.4f}",
        f"     three-outcome pair of C.3: largest V3' - V4' over {RANDOM_MARGINALS_C} random "
        f"marginals = {largest:.6f} <= 0",
        f"     alpha3*/alpha4* (W = {WEALTH_C:g}): " + " ; ".join(three_outcome_amounts()),
    ]


# --- Domanda D ---------------------------------------------------------------------------


def expected_loss(effort: int) -> float:
    """Return E[l | e] for the toy instance."""
    return sum(p * loss for p, loss in zip(PROBS_D[effort], LOSSES_D))


def first_best(effort: int) -> float:
    """Return the profit of the full-cover policy at ``effort``."""
    premium = WEALTH_D - math.exp(EFFORT_COST_D[effort] + RESERVE_D)
    return premium - expected_loss(effort)


def likelihood_ratios() -> list[float]:
    """Return r_l = pi_l(0)/pi_l(1) for the toy instance."""
    return [p0 / p1 for p0, p1 in zip(PROBS_D[LOW_EFFORT], PROBS_D[HIGH_EFFORT])]


def high_effort_wealths() -> np.ndarray:
    """Return the final wealths z_l of the optimal policy inducing e = 1, with PC and IC.

    The problem is convex in the utility levels v = ln z: the profit is minimised in
    E[exp(v)] while PC and IC are linear in v.
    """
    high, low = np.array(PROBS_D[HIGH_EFFORT]), np.array(PROBS_D[LOW_EFFORT])
    gap = EFFORT_COST_D[HIGH_EFFORT] - EFFORT_COST_D[LOW_EFFORT]
    constraints = (
        {"type": "ineq", "fun": lambda v: high @ v - EFFORT_COST_D[HIGH_EFFORT] - RESERVE_D},
        {"type": "ineq", "fun": lambda v: (high - low) @ v - gap},
    )
    result = minimize(
        lambda v: float(high @ np.exp(v)),
        np.array(START_LEVELS_D),
        constraints=constraints,
        method="SLSQP",
        options={"ftol": SOLVER_TOLERANCE, "maxiter": SOLVER_ITERATIONS_D},
    )
    check(result.success, "the second-best problem must converge")
    return np.exp(result.x)


def fitted_multipliers(wealths: np.ndarray) -> tuple[float, float]:
    """Return ``(lambda, beta)`` with z_l = lambda + beta (1 - r_l), checking the fit is exact."""
    design = np.column_stack([np.ones(len(wealths)), 1 - np.array(likelihood_ratios())])
    multipliers = np.linalg.lstsq(design, wealths, rcond=None)[0]
    exact = np.allclose(design @ multipliers, wealths, atol=POLICY_TOLERANCE_D)
    check(exact, "1/u'(z_l) = z_l must equal lambda + beta (1 - r_l) at the optimum")
    return float(multipliers[0]), float(multipliers[1])


def indemnified_wealth_d(index: int, indemnity: float) -> float:
    """Return z_l = W - premium - l + B_l for the loss ``l = index`` and the test premium."""
    return WEALTH_D - TEST_PREMIUM_D - LOSSES_D[index] + indemnity


def lagrangian_term(index: int, indemnity: float) -> float:
    """Return the part of the Lagrangian of the toy instance that depends on B_l, l = index."""
    lam, beta = TEST_MULTIPLIERS_D
    high, low = PROBS_D[HIGH_EFFORT][index], PROBS_D[LOW_EFFORT][index]
    wealth = indemnified_wealth_d(index, indemnity)
    return -high * indemnity + (lam * high + beta * (high - low)) * math.log(wealth)


def check_foc_formula() -> None:
    """Check dL/dB_l by finite differences and its rearrangement into condition (5)."""
    lam, beta = TEST_MULTIPLIERS_D
    for index, indemnity in enumerate(TEST_INDEMNITIES_D):
        high, low = PROBS_D[HIGH_EFFORT][index], PROBS_D[LOW_EFFORT][index]
        wealth = indemnified_wealth_d(index, indemnity)
        numerical = finite_derivative(partial(lagrangian_term, index), indemnity, 1)
        formula = -high + lam * high / wealth + beta * (high - low) / wealth
        check(close(numerical, formula), "dL/dB_l must match the formula")
        rearranged = (lam + beta * (1 - low / high) - wealth) * high / wealth
        check(close(formula, rearranged), "dividing by pi_l(1) u'(z) must give condition (5)")


def d1_first_order_condition() -> list[str]:
    """Check the FOC in B_l and the condition 1/u'(z_l) = lambda + beta (1 - r_l) at the optimum."""
    check_foc_formula()
    wealths = high_effort_wealths()
    lam, beta = fitted_multipliers(wealths)
    ratios = [round(r, 3) for r in likelihood_ratios()]
    return [
        "D.1  dL/dB_l = -pi_l(1) + [lambda pi_l(1) + beta (pi_l(1) - pi_l(0))] u'(z_l); dividing "
        "by pi_l(1) u'(z_l):",
        f"     1/u'(z_l) = lambda + beta (1 - r_l) ; toy instance (u = ln): r_l = {ratios}",
        f"     optimum: z_l = {np.round(wealths, 4).tolist()} ; lambda = {lam:.4f} ; "
        f"beta = {beta:.4f}",
    ]


def d2_participation_active() -> list[str]:
    """Check r_0 < 1 < r_L, that lambda = 0 contradicts the condition, and PC binds."""
    ratios = likelihood_ratios()
    high = PROBS_D[HIGH_EFFORT]
    check(all(a < b for a, b in zip(ratios, ratios[1:])), "ratios must be strictly increasing")
    check(close(sum(p * (r - 1) for p, r in zip(high, ratios)), 0.0), "sum pi(1)(r - 1) = 0")
    check(ratios[0] < 1 < ratios[-1], "MLR must give r_0 < 1 < r_L")
    wealths = high_effort_wealths()
    lam, beta = fitted_multipliers(wealths)
    check(lam > 0 and beta > 0, "both multipliers must be positive")
    without_lambda = [beta * (1 - r) for r in ratios]
    check(without_lambda[-1] < 0, "with lambda = 0 the right-hand side is negative at l = L")
    slack = float(np.array(high) @ np.log(wealths)) - EFFORT_COST_D[HIGH_EFFORT] - RESERVE_D
    check(abs(slack) < POLICY_TOLERANCE_D, "PC must bind")
    return [
        f"D.2  sum_l pi_l(1)(r_l - 1) = 0 ; r_0 = {ratios[0]:.3f} < 1 < r_L = {ratios[-1]:.3f}",
        f"     with lambda = 0: beta (1 - r_l) = {[round(v, 3) for v in without_lambda]}, "
        "negative at l = L while 1/u'(z_l) > 0",
        f"     lambda = {lam:.4f} > 0 ; PC slack = {slack:.2e} (binds)",
    ]


def d3_inefficiency() -> list[str]:
    """Compare the first-best and second-best outcomes when e* = 1."""
    profit_fb = [first_best(effort) for effort in (LOW_EFFORT, HIGH_EFFORT)]
    check(profit_fb[HIGH_EFFORT] > profit_fb[LOW_EFFORT], "the first best must pick e = 1")
    wealths = high_effort_wealths()
    losses = np.array(LOSSES_D)
    # With the normalisation B_0 = 0 the difference z_l - z_0 equals B_l - l.
    gaps = wealths - wealths[0]
    check(gaps[0] > gaps[1] > gaps[2], "B_l - l must be strictly decreasing")
    check(gaps[1] < 0 and gaps[2] < 0, "the cover must be partial for every l >= 1")
    profit_high = WEALTH_D - float(np.array(PROBS_D[HIGH_EFFORT]) @ (wealths + losses))
    check(profit_high < profit_fb[HIGH_EFFORT], "inducing e = 1 must earn less than its first best")
    effort_gap = EFFORT_COST_D[HIGH_EFFORT] - EFFORT_COST_D[LOW_EFFORT]
    check(effort_gap > 0, "full cover with e = 1 must violate IC")
    best_second = max(profit_high, profit_fb[LOW_EFFORT])
    return [
        f"D.3  first best: Pi(0) = {profit_fb[LOW_EFFORT]:.4f} < "
        f"Pi(1) = {profit_fb[HIGH_EFFORT]:.4f}, so e* = 1",
        f"     full cover with e = 1 violates IC: d(1) - d(0) = {effort_gap:.2f} > 0",
        f"     second best inducing e = 1: B_l - l = (0, {gaps[1]:.4f}, {gaps[2]:.4f}), profit "
        f"{profit_high:.4f} < Pi(1) ; consumer utility = reserve {RESERVE_D:.4f}",
        f"     inducing e = 0 earns Pi(0) = {profit_fb[LOW_EFFORT]:.4f}: e** = "
        f"{HIGH_EFFORT if profit_high > profit_fb[LOW_EFFORT] else LOW_EFFORT}, "
        "profit lost against the first best = "
        f"{profit_fb[HIGH_EFFORT] - best_second:.4f}",
    ]


# --- Domanda E ---------------------------------------------------------------------------


def random_outcomes(rng: np.random.Generator) -> Outcomes:
    """Draw a three-valued return with positive probabilities."""
    returns = np.sort(rng.uniform(*RETURN_RANGE_E, size=RANDOM_OUTCOMES_E))
    return returns, rng.dirichlet(np.ones(RANDOM_OUTCOMES_E))


def check_slope_at_zero(rng: np.random.Generator) -> tuple[int, int]:
    """Check V'(0) and the sign of alpha* on random draws; return how many had E[x] > 0 or not."""
    positive = nonpositive = 0
    for _ in range(RANDOM_TRIALS_E):
        outcomes = random_outcomes(rng)
        utility = UTILITY_POOL_E[int(rng.integers(len(UTILITY_POOL_E)))]
        mean = float(outcomes[0] @ outcomes[1])
        objective = partial(expected_utility, utility.level, WEALTH_E, outcomes)
        slope = finite_derivative(objective, 0.0, 1)
        check(close(slope, utility.first(WEALTH_E) * mean), "V'(0) must equal u'(w0) E[x]")
        alpha = optimal_alpha(utility.first, WEALTH_E, outcomes)
        if mean > 0:
            positive += 1
            check(alpha > 0, "alpha* must be positive when E[x] > 0")
        else:
            nonpositive += 1
            check(alpha == 0.0, "alpha* must vanish when E[x] <= 0")
    check(min(positive, nonpositive) >= MIN_DRAWS_E, "too few draws of one sign")
    return positive, nonpositive


def gain_and_premium(scale: float, outcomes: Outcomes) -> str:
    """Return the expected gain and the risk premium of investing ``scale`` in the risky title."""
    returns, probs = outcomes
    mean = float(returns @ probs)
    expected_log = expected_utility(math.log, WEALTH_E, outcomes, scale)
    premium = WEALTH_E + scale * mean - math.exp(expected_log)
    return f"eps = {scale:g}: gain {scale * mean:.4f}, premium {premium:.6f}"


def e1_slope_at_zero() -> list[str]:
    """Check V'(0) = u'(w0) E[x], alpha* > 0 iff E[x] > 0, and the orders of gain and premium."""
    positive, nonpositive = check_slope_at_zero(np.random.default_rng(SEED))
    outcomes = (np.array(SHOWCASE_RETURNS_E), np.array(SHOWCASE_PROBS_E))
    mean = float(outcomes[0] @ outcomes[1])
    variance = float(outcomes[1] @ (outcomes[0] - mean) ** 2)
    alpha = optimal_alpha(LOG.first, WEALTH_E, outcomes)
    rows = [gain_and_premium(scale, outcomes) for scale in SHOWCASE_SCALES_E]
    approximation = 0.5 * absolute_aversion(LOG, WEALTH_E) * variance
    return [
        f"E.1  {positive} draws with E[x] > 0 give alpha* > 0, {nonpositive} with E[x] <= 0 give 0",
        "     V'(0) = u'(w0) E[x] checked by finite differences on every draw",
        f"     example u = ln, w0 = {WEALTH_E:g}, x = {SHOWCASE_RETURNS_E} equiprobable: "
        f"E[x] = {mean:.4f}, alpha* = {alpha:.4f}",
        "     " + " ; ".join(rows) + f" ; premium ~ {approximation:.6f} eps^2",
        f"     gain = premium at eps ~ {mean / approximation:.1f}",
    ]


@dataclass(frozen=True)
class Transform:
    """An increasing strictly concave function phi with its derivative.

    Attributes:
        name: Label used in the printed output.
        level: Function phi(t).
        first: Function phi'(t).
    """

    name: str
    level: Callable[[float], float]
    first: Callable[[float], float]


E2_PAIRS = (
    (LOG, Transform("-exp(-t)", lambda t: -math.exp(-t), lambda t: math.exp(-t))),
    (SQRT, Transform("ln t", math.log, lambda t: 1 / t)),
    (SQRT, Transform("-1/t", lambda t: -1 / t, lambda t: t**-2)),
)


def transformed_marginal(base: Utility, phi: Transform) -> Callable[[float], float]:
    """Return u2'(w) = phi'(u1(w)) u1'(w) for u2 = phi(u1)."""
    return lambda wealth: phi.first(base.level(wealth)) * base.first(wealth)


def e2_trial(rng: np.random.Generator, base: Utility, phi: Transform) -> tuple[float, float] | None:
    """Return ``(alpha2* - alpha1*, V1'(alpha2*))`` for an admissible draw, or None."""
    outcomes = random_outcomes(rng)
    marginal_two = transformed_marginal(base, phi)
    inadmissible = float(outcomes[0] @ outcomes[1]) <= 0
    if inadmissible or expected_slope(marginal_two, WEALTH_E, outcomes, WEALTH_E) >= 0:
        return None
    alpha_two = optimal_alpha(marginal_two, WEALTH_E, outcomes)
    alpha_one = optimal_alpha(base.first, WEALTH_E, outcomes)
    return alpha_two - alpha_one, expected_slope(base.first, WEALTH_E, outcomes, alpha_two)


def e2_risk_aversion_and_investment() -> list[str]:
    """Check alpha2* < alpha1* and the chain of the proof for u2 = phi(u1), phi strictly concave."""
    rng = np.random.default_rng(SEED)
    lines = []
    for base, phi in E2_PAIRS:
        gaps, slopes = [], []
        for _ in range(RANDOM_TRIALS_E):
            trial = e2_trial(rng, base, phi)
            if trial is not None:
                gaps.append(trial[0])
                slopes.append(trial[1])
        check(len(gaps) >= MIN_PAIR_DRAWS_E, "too few admissible draws")
        check(max(gaps) < ALPHA_TOLERANCE_E, "alpha2* must stay below alpha1*")
        check(min(slopes) > 0, "V1'(alpha2*) must be positive")
        lines.append(
            f"E.2  u1 = {base.name}, phi = {phi.name}: {len(gaps)} draws, largest "
            f"alpha2* - alpha1* = {max(gaps):.4f} < 0, "
            f"smallest V1'(alpha2*) = {min(slopes):.2e} > 0"
        )
    return lines


SECTIONS = (
    a1_arrow_pratt,
    a2_certain_equivalents,
    a3_concave_transform,
    a4_premium_ordering,
    b1_price_and_premium,
    b2_pricing_kernel,
    b3_limited_participation,
    b4_participant_risk,
    c1_first_order,
    c2_means,
    c3_second_order,
    c4_amounts_not_ordered,
    d1_first_order_condition,
    d2_participation_active,
    d3_inefficiency,
    e1_slope_at_zero,
    e2_risk_aversion_and_investment,
)


def main() -> None:
    """Run every section and print its figures."""
    for section in SECTIONS:
        print("\n".join(section()))


if __name__ == "__main__":
    main()
