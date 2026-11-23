"""Calculations behind the simulated appello 01 of Economia del Rischio e delle Assicurazioni.

The constants below are the data printed in ERA_Esame_Simulato_01.md. Every figure quoted in
ERA_Soluzioni_Simulato_01.md and in the answer key of piano/appello-01.json is printed by this
script. Exact rational results are Fractions, irrational ones are floats. Closed-form solutions
are checked against finite differences, root finding or constrained optimisation, and a
disagreement raises CheckFailed (an explicit exception, so ``python -O`` cannot skip it).

Run it with ``python appello_01.py``. It writes no file.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Sequence

import numpy as np
from scipy.optimize import brentq, minimize

Distribution = tuple[Fraction, ...]

SEED = 20260123
FINITE_STEP = 1e-2
RELATIVE_TOLERANCE = 1e-3
ZERO_TOLERANCE = 1e-9
STENCILS = {
    1: ((-1, -0.5), (1, 0.5)),
    2: ((-1, 1.0), (0, -2.0), (1, 1.0)),
    3: ((-2, -0.5), (-1, 1.0), (1, -1.0), (2, 0.5)),
}

# Domanda A: u(W) = -1/W; X loses 2 with probability 2/3 and gains 4 with probability 1/3.
LOTTERY_A = ((Fraction(-2), Fraction(2, 3)), (Fraction(4), Fraction(1, 3)))
WEALTH_A_LOW = Fraction(4)
WEALTH_A_HIGH = Fraction(6)
SMALL_SCALES = (Fraction(1, 100), Fraction(1, 10))
SCALES_A = (Fraction(1, 2), Fraction(1), Fraction(3, 2))
# The smallest wealth must stay above the largest loss 2k (k = 3/2) so that u stays defined.
WEALTHS_A = (Fraction(4), Fraction(5), Fraction(6), Fraction(8), Fraction(13))

# Domanda B: u(W) = sqrt(W); w and w - L are perfect squares.
WEALTH_B = Fraction(36)
LOSS_B = Fraction(20)
PROB_B = Fraction(1, 4)
PRICE_B = Fraction(11)
POPULATION_MEAN_B = Fraction(1, 2)
ROOT_WEALTH_B = math.sqrt(WEALTH_B)
GAIN_FROM_COVER_B = ROOT_WEALTH_B - math.sqrt(WEALTH_B - LOSS_B)
GRID_POINTS_B = 2000

# Domanda C: three equally spaced premiums, two pairs of lotteries.
PREMIUMS_C = (Fraction(20), Fraction(30), Fraction(40))
LOTTERY_P = (Fraction(1, 10), Fraction(7, 10), Fraction(2, 10))
LOTTERY_Q = (Fraction(2, 10), Fraction(5, 10), Fraction(3, 10))
MIX_WEIGHT = Fraction(1, 2)
COMMON_COMPONENT = (Fraction(0), Fraction(1), Fraction(0))
RANDOM_UTILITIES = 5000
UTILITY_INCREMENTS_C = 2
UTILITY_STEP_RANGE = (0.01, 5.0)

# Domanda D: a toy instance with u = ln, losses 0, 1, 2 and two effort levels.
WEALTH_D = 10.0
LOSSES_D = np.array([0.0, 1.0, 2.0])
PROBS_D = {0: np.array([0.2, 0.3, 0.5]), 1: np.array([0.5, 0.3, 0.2])}
EFFORT_COST_D = {0: 0.0, 1: 0.30}
# The solver works on the utility levels u(z_l) = ln z_l of the final wealth, where the
# problem is convex: profit is convex-minimised and PC and IC are linear in the levels.
LEVEL_BOUNDS = ((0.0, 3.0), (0.0, 3.0), (0.0, 3.0))
START_LEVELS = (2.0, 2.0, 2.0)
SOLVER_TOLERANCE = 1e-12
SOLVER_ITERATIONS = 500
POLICY_TOLERANCE = 1e-4

# Domanda E: r = 0, so w0 = W; the excess return is -50% or +100% with equal probability.
RISK_FREE_E = 0.0
EXCESS_RETURNS_E = np.array([-0.5, 1.0])
PROBS_E = np.array([0.5, 0.5])
WEALTH_E = 100.0
PROBE_WEALTHS_E = (50.0, 100.0)
PROBE_SHIFTS_E = (-20.0, 10.0, 40.0)
PROBE_ALPHA = 40.0
WEALTH_STEP_E = 0.5
CARA_RATE = 0.01
RANDOM_TRIALS_E = 2000
RANDOM_OUTCOMES_E = 3
MIN_ADMISSIBLE_TRIALS = 100
# Returns above -1 keep the final wealth positive for every investment alpha <= W.
RETURN_RANGE_E = (-0.8, 0.8)
SPREAD_RANGE_E = (0.0, 0.15)
GRID_E = np.linspace(-0.9, 1.4, 47)
ALPHA_TOLERANCE = 1e-7


class CheckFailed(Exception):
    """Raised when a closed-form result disagrees with its numerical check."""


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


def fmt(value: Fraction | float) -> str:
    """Format an exact Fraction as ``p/q (decimal)`` and a float with four decimals."""
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value} ({float(value):.4f})"
    return f"{value:.4f}"


def vector(values: Sequence[Fraction]) -> str:
    """Format a sequence of Fractions as ``(a, b, c)``."""
    return "(" + ", ".join(str(value) for value in values) + ")"


def finite_derivative(func: Callable[[float], float], point: float, order: int) -> float:
    """Return the central finite-difference derivative of ``func`` at ``point``.

    Args:
        func: Real function of one variable.
        point: Where to differentiate.
        order: Order of the derivative, 1 to 3.
    """
    total = sum(weight * func(point + offset * FINITE_STEP) for offset, weight in STENCILS[order])
    return total / FINITE_STEP**order


def exact_root(value: Fraction) -> Fraction:
    """Return the square root of a Fraction that is a perfect square.

    Raises:
        CheckFailed: If ``value`` is not the square of a rational number.
    """
    root = Fraction(math.isqrt(value.numerator), math.isqrt(value.denominator))
    check(root * root == value, f"{value} is not a perfect square")
    return root


# --- Domanda A ---------------------------------------------------------------------------


def utility_a(wealth: Fraction | float) -> Fraction | float:
    """Return u(W) = -1/W, for Fractions and floats alike."""
    return -1 / wealth


def expected_utility_a(wealth: Fraction, scale: Fraction = Fraction(1)) -> Fraction:
    """Return E[u(w + kX)] for the lottery X of question A and ``scale`` k."""
    return sum(prob * utility_a(wealth + scale * outcome) for outcome, prob in LOTTERY_A)


def risk_premium_a(wealth: Fraction, scale: Fraction = Fraction(1)) -> tuple[Fraction, Fraction]:
    """Return ``(CE, R)`` for the lottery kX at ``wealth``.

    CE solves u(CE) = E[u(w + kX)] and R = w - CE holds because E[X] = 0.
    """
    certain_equivalent = -1 / expected_utility_a(wealth, scale)
    return certain_equivalent, wealth - certain_equivalent


def a1_arrow_pratt() -> list[str]:
    """Check A(W) = 2/W, RR(W) = 2 and P(W) = 3/W against finite differences of u."""
    check(
        sum(prob * outcome for outcome, prob in LOTTERY_A) == 0,
        "E[X] of the lottery of question A must be zero",
    )
    for wealth in WEALTHS_A:
        point = float(wealth)
        orders = (1, 2, 3)
        first, second, third = (finite_derivative(utility_a, point, n) for n in orders)
        absolute, prudence = -second / first, -third / second
        check(math.isclose(absolute, 2 / point, rel_tol=RELATIVE_TOLERANCE), "A(W) must equal 2/W")
        check(math.isclose(point * absolute, 2, rel_tol=RELATIVE_TOLERANCE), "RR(W) must equal 2")
        check(math.isclose(prudence, 3 / point, rel_tol=RELATIVE_TOLERANCE), "P(W) must equal 3/W")
        slope = finite_derivative(lambda w: 2 / w, point, 1)
        check(
            math.isclose(slope, absolute * (absolute - prudence), rel_tol=RELATIVE_TOLERANCE),
            "A'(W) must equal A * (A - P)",
        )
    return [
        "A.1  A(W) = 2/W ; RR(W) = W*A(W) = 2 for every W (CRRA with gamma = 2)",
        "     P(W) = 3/W ; A'(W) = -2/W^2 = A*(A - P) < 0",
    ]


def a2_certain_equivalent() -> list[str]:
    """Return CE and R at w1 and check the closed form R = 2 a^2 / (w + a), a = 2k."""
    for wealth in WEALTHS_A:
        for scale in SCALES_A:
            loss = 2 * scale
            check(
                risk_premium_a(wealth, scale)[1] == 2 * loss**2 / (wealth + loss),
                "R must equal 2 a^2 / (w + a)",
            )
    expected = expected_utility_a(WEALTH_A_LOW)
    certain_equivalent, premium = risk_premium_a(WEALTH_A_LOW)
    return [
        f"A.2  w1 = {WEALTH_A_LOW}: E[u] = {fmt(expected)}",
        f"     CE = {fmt(certain_equivalent)} ; R = w1 - CE = {fmt(premium)}",
    ]


def a3_wealth_effect() -> list[str]:
    """Return CE and R at w2 and check that the premium falls with wealth, as P > A implies."""
    premiums = [risk_premium_a(wealth)[1] for wealth in WEALTHS_A]
    check(
        all(later < earlier for earlier, later in zip(premiums, premiums[1:])),
        "the premium must fall as wealth grows",
    )
    certain_equivalent, premium_high = risk_premium_a(WEALTH_A_HIGH)
    premium_low = risk_premium_a(WEALTH_A_LOW)[1]
    check(premium_high < premium_low, "R at w2 must be below R at w1")
    return [
        f"A.3  w2 = {WEALTH_A_HIGH}: E[u] = {fmt(expected_utility_a(WEALTH_A_HIGH))}",
        f"     CE = {fmt(certain_equivalent)} ; R2 = {fmt(premium_high)} < R1 = {fmt(premium_low)}",
        "     P(W) - A(W) = 1/W > 0, so A is decreasing: DARA, and R falls as w grows",
    ]


def a4_small_lottery() -> list[str]:
    """Compare the exact premium of kX with the quadratic approximation and its doubling."""
    second_moment = sum(prob * outcome**2 for outcome, prob in LOTTERY_A)
    absolute = 2 / WEALTH_A_LOW
    lines = [f"A.4  E[X^2] = {fmt(second_moment)} ; A(w1) = {fmt(absolute)}"]
    for scale in SMALL_SCALES:
        exact = risk_premium_a(WEALTH_A_LOW, scale)[1]
        approximation = absolute * second_moment * scale**2 / 2
        ratio = risk_premium_a(WEALTH_A_LOW, 2 * scale)[1] / exact
        lines.append(
            f"     k = {scale}: R(k) = {float(exact):.6f} ; approx 2k^2 = "
            f"{float(approximation):.6f} ; R(2k)/R(k) = {float(ratio):.3f}"
        )
    return lines


# --- Domanda B ---------------------------------------------------------------------------


def uncovered_utility_b() -> Fraction:
    """Return the expected utility of consumer B without insurance, in sqrt units."""
    loss_root = exact_root(WEALTH_B - LOSS_B)
    return PROB_B * loss_root + (1 - PROB_B) * exact_root(WEALTH_B)


def b1_fair_premium() -> list[str]:
    """Compare expected utility with and without full cover at the fair premium."""
    fair = PROB_B * LOSS_B
    insured_wealth = WEALTH_B - fair
    uncovered = uncovered_utility_b()
    check(
        uncovered**2 < insured_wealth,
        "full cover must be strictly preferred at the fair premium",
    )
    return [
        f"B.1  fair premium = pi*L = {fmt(fair)} ; wealth if insured = {fmt(insured_wealth)}",
        f"     EU without cover = {fmt(uncovered)} ; EU with cover = sqrt({fmt(insured_wealth)})"
        f" = {math.sqrt(insured_wealth):.4f}",
        f"     squares: {fmt(uncovered**2)} < {fmt(insured_wealth)}: cover strictly preferred",
    ]


def b2_certain_equivalent() -> list[str]:
    """Return CE, the maximum premium and the risk premium for the uncovered position."""
    uncovered = uncovered_utility_b()
    certain_equivalent = uncovered**2
    expected_wealth = WEALTH_B - PROB_B * LOSS_B
    premium = expected_wealth - certain_equivalent
    max_price = WEALTH_B - certain_equivalent
    check(
        exact_root(WEALTH_B - max_price) == uncovered,
        "u(w - maximum premium) must equal the uncovered utility",
    )
    check(
        max_price == PROB_B * LOSS_B + premium,
        "maximum premium must be fair premium plus risk premium",
    )
    return [
        f"B.2  CE = {fmt(certain_equivalent)} ; expected wealth = {fmt(expected_wealth)}",
        f"     maximum premium = w - CE = {fmt(max_price)} ; risk premium = {fmt(premium)}",
    ]


def threshold_b(price: Fraction) -> Fraction:
    """Return h(p) = (u(w) - u(w - p)) / (u(w) - u(w - L)) for u = sqrt, exactly."""
    root_wealth = exact_root(WEALTH_B)
    gain_from_cover = root_wealth - exact_root(WEALTH_B - LOSS_B)
    return (root_wealth - exact_root(WEALTH_B - price)) / gain_from_cover


def uniform_profit_b(price: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return ``(h, E[pi | pi >= h], profit per policy)`` for pi uniform on [0, 1]."""
    threshold = threshold_b(price)
    buyers_mean = (1 + threshold) / 2
    return threshold, buyers_mean, price - buyers_mean * LOSS_B


def float_gap_b(price: float) -> float:
    """Return the buyers' expected claim cost minus the price, in floats."""
    threshold = (ROOT_WEALTH_B - math.sqrt(WEALTH_B - price)) / GAIN_FROM_COVER_B
    return (1 + threshold) / 2 * float(LOSS_B) - price


def b3_adverse_selection() -> list[str]:
    """Test the prices p = 11 and p = L as equilibria and scan [0, L) for any other."""
    threshold, mean, profit = uniform_profit_b(PRICE_B)
    check(profit != 0, "p = 11 must not be an equilibrium")
    threshold_l, mean_l, profit_l = uniform_profit_b(LOSS_B)
    check(profit_l == 0 and threshold_l == 1, "p = L must be an equilibrium with threshold 1")
    grid = np.linspace(0.0, float(LOSS_B), GRID_POINTS_B, endpoint=False)
    check(min(float_gap_b(price) for price in grid) > 0, "no equilibrium price below L expected")
    return [
        f"B.3  p = {PRICE_B}: h(p) = {fmt(threshold)} ; E[pi | buyers] = {fmt(mean)}",
        f"     expected claim = {fmt(mean * LOSS_B)} ; profit per policy = {fmt(profit)}"
        " (not an equilibrium)",
        f"     p = L = {LOSS_B}: h = {fmt(threshold_l)} ; limit mean = {fmt(mean_l)}"
        f" ; profit = {fmt(profit_l)} (equilibrium)",
        f"     wrong shortcut, population mean {POPULATION_MEAN_B}: cost "
        f"{fmt(POPULATION_MEAN_B * LOSS_B)}, profit {fmt(PRICE_B - POPULATION_MEAN_B * LOSS_B)}",
        "     scan of [0, L): the cost of the buyers always exceeds p, so L is the only one",
    ]


# --- Domanda C ---------------------------------------------------------------------------


def mean_c(distribution: Distribution) -> Fraction:
    """Return the expected premium of a lottery on the three premiums."""
    return sum(prob * premium for premium, prob in zip(PREMIUMS_C, distribution))


def cdf_c(distribution: Distribution) -> Distribution:
    """Return the c.d.f. of a lottery at the three premiums."""
    running = Fraction(0)
    values = []
    for prob in distribution:
        running += prob
        values.append(running)
    return tuple(values)


def integrated_cdf_c(distribution: Distribution) -> Distribution:
    """Return the integral of the c.d.f. from the lowest premium to each premium."""
    cdf = cdf_c(distribution)
    totals = [Fraction(0)]
    for index in range(len(PREMIUMS_C) - 1):
        gap = PREMIUMS_C[index + 1] - PREMIUMS_C[index]
        totals.append(totals[-1] + cdf[index] * gap)
    return tuple(totals)


def dominates(better: Distribution, worse: Distribution, order: int) -> bool:
    """Return whether ``better`` dominates ``worse`` at the first or second order."""
    transform = cdf_c if order == 1 else integrated_cdf_c
    return all(b <= w for b, w in zip(transform(better), transform(worse)))


def mix_c(first: Distribution, second: Distribution, weight: Fraction) -> Distribution:
    """Return the reduced compound lottery ``weight * first + (1 - weight) * second``."""
    return tuple(weight * a + (1 - weight) * b for a, b in zip(first, second))


def expected_utility_c(distribution: Distribution, utilities: Sequence[float]) -> float:
    """Return the expected utility of a lottery given the utilities of the three premiums."""
    return sum(float(prob) * value for prob, value in zip(distribution, utilities))


def utility_gap_c(first: Distribution, second: Distribution, utilities: Sequence[float]) -> float:
    """Return EU(first) - EU(second) for the given premium utilities."""
    return expected_utility_c(first, utilities) - expected_utility_c(second, utilities)


def random_utilities_c(count: int) -> list[tuple[float, float, float]]:
    """Return ``count`` increasing utility triples with random increments (0, a, a + b)."""
    rng = np.random.default_rng(SEED)
    increments = rng.uniform(*UTILITY_STEP_RANGE, size=(count, UTILITY_INCREMENTS_C))
    return [(0.0, float(a), float(a + b)) for a, b in increments]


def c1_first_order() -> list[str]:
    """Show that p and q have equal means, crossing c.d.f.s and are ordered both ways."""
    check(mean_c(LOTTERY_P) == mean_c(LOTTERY_Q), "p and q must have equal means")
    check(
        not dominates(LOTTERY_P, LOTTERY_Q, 1) and not dominates(LOTTERY_Q, LOTTERY_P, 1),
        "p and q must not be ordered at the first order",
    )
    families = {
        "concave sqrt": [math.sqrt(float(x)) for x in PREMIUMS_C],
        "linear": [float(x) for x in PREMIUMS_C],
        "convex square": [float(x) ** 2 for x in PREMIUMS_C],
    }
    gaps = {name: utility_gap_c(LOTTERY_P, LOTTERY_Q, values) for name, values in families.items()}
    check(
        gaps["concave sqrt"] > 0 > gaps["convex square"],
        "the concave utility must prefer p and the convex one q",
    )
    check(
        abs(gaps["linear"]) < ZERO_TOLERANCE,
        "a linear utility must be indifferent between p and q",
    )
    cdf_p, cdf_q = cdf_c(LOTTERY_P), cdf_c(LOTTERY_Q)
    return [
        f"C.1  mean(p) = {fmt(mean_c(LOTTERY_P))} = mean(q) = {fmt(mean_c(LOTTERY_Q))}",
        f"     F_p = {vector(cdf_p)} ; F_q = {vector(cdf_q)}",
        "     F_p - F_q = " + vector([a - b for a, b in zip(cdf_p, cdf_q)]),
        "     EU(p) - EU(q): "
        + " ; ".join(f"{name} {gap:+.4f}" for name, gap in gaps.items()),
    ]


def spread_probability_c() -> Fraction:
    """Return the probability of moving the middle premium down (and up) to turn p into q."""
    shift = (LOTTERY_Q[0] - LOTTERY_P[0]) / LOTTERY_P[1]
    rebuilt = (
        LOTTERY_P[0] + shift * LOTTERY_P[1],
        LOTTERY_P[1] * (1 - 2 * shift),
        LOTTERY_P[2] + shift * LOTTERY_P[1],
    )
    check(rebuilt == LOTTERY_Q, "the spread of the middle premium must turn p into q")
    return shift


def c2_second_order() -> list[str]:
    """Check SOSD, the mean-preserving-spread construction and random concave utilities."""
    check(
        dominates(LOTTERY_P, LOTTERY_Q, 2) and not dominates(LOTTERY_Q, LOTTERY_P, 2),
        "p must dominate q at the second order and not conversely",
    )
    shift = spread_probability_c()
    step = PREMIUMS_C[1] - PREMIUMS_C[0]
    for utilities in random_utilities_c(RANDOM_UTILITIES):
        _, low, high = utilities
        concave = (0.0, low, low + min(low, high - low))
        check(
            utility_gap_c(LOTTERY_P, LOTTERY_Q, concave) >= -ZERO_TOLERANCE,
            "every concave utility must prefer p",
        )
    return [
        f"C.2  integral of F_p = {vector(integrated_cdf_c(LOTTERY_P))}",
        f"     integral of F_q = {vector(integrated_cdf_c(LOTTERY_Q))} : p SOSD q",
        f"     q = p + noise: from {PREMIUMS_C[1]} move -{step} w.p. {shift}, +{step} w.p. "
        f"{shift}, stay w.p. {1 - 2 * shift}",
        f"     {RANDOM_UTILITIES} random concave increasing u: EU(p) >= EU(q) in all",
    ]


def mixed_pair_c() -> tuple[Distribution, Distribution]:
    """Return the compound lotteries ``(p', q')``: p and q mixed with the common component."""
    return (
        mix_c(LOTTERY_P, COMMON_COMPONENT, MIX_WEIGHT),
        mix_c(LOTTERY_Q, COMMON_COMPONENT, MIX_WEIGHT),
    )


def c3_independence() -> list[str]:
    """Check q' - p' = alpha (q - p) and that the order of p, q carries over to p', q'."""
    p_prime, q_prime = mixed_pair_c()
    differences = [b - a for a, b in zip(p_prime, q_prime)]
    check(
        differences == [MIX_WEIGHT * (b - a) for a, b in zip(LOTTERY_P, LOTTERY_Q)],
        "q' - p' must equal alpha (q - p)",
    )
    for values in random_utilities_c(RANDOM_UTILITIES):
        base = utility_gap_c(LOTTERY_P, LOTTERY_Q, values)
        mixed = utility_gap_c(p_prime, q_prime, values)
        check(
            math.isclose(mixed, float(MIX_WEIGHT) * base, abs_tol=ZERO_TOLERANCE),
            "EU(p') - EU(q') must equal alpha (EU(p) - EU(q))",
        )
    return [
        f"C.3  p' = {vector(p_prime)} ; q' = {vector(q_prime)}",
        f"     means: {fmt(mean_c(p_prime))} and {fmt(mean_c(q_prime))}",
        f"     q' - p' = {vector(differences)} = alpha (q - p), alpha = {MIX_WEIGHT}",
        f"     {RANDOM_UTILITIES} random increasing u: EU(p') - EU(q') = alpha (EU(p) - EU(q))",
    ]


def c4_triangle() -> list[str]:
    """Return the Machina-triangle coordinates (pi_1, pi_3) of the four lotteries."""
    p_prime, q_prime = mixed_pair_c()
    points = {"p": LOTTERY_P, "q": LOTTERY_Q, "p'": p_prime, "q'": q_prime}
    lines = ["C.4  coordinates (pi_1, pi_3):"]
    lines += [f"     {name} = ({lottery[0]}, {lottery[2]})" for name, lottery in points.items()]
    slope = (LOTTERY_Q[2] - LOTTERY_P[2]) / (LOTTERY_Q[0] - LOTTERY_P[0])
    slope_prime = (q_prime[2] - p_prime[2]) / (q_prime[0] - p_prime[0])
    check(slope == slope_prime, "p->q and p'->q' must have the same slope")
    lines.append(f"     slope of p->q = slope of p'->q' = {slope}")
    return lines


# --- Domanda D ---------------------------------------------------------------------------


def client_utility_d(effort: int, levels: Sequence[float]) -> float:
    """Return the client's utility with ``effort`` when u(z_l) = ``levels[l]`` in every state."""
    return float(PROBS_D[effort] @ np.asarray(levels)) - EFFORT_COST_D[effort]


def profit_d(effort: int, levels: Sequence[float]) -> float:
    """Return the company's profit w - E_e[z] - E_e[l] given the wealth z_l = exp(levels[l]).

    The profit does not depend on how the premium and the indemnities split z_l: only the final
    wealth of the client in each state matters.
    """
    wealth = np.exp(np.asarray(levels))
    return WEALTH_D - float(PROBS_D[effort] @ wealth) - float(PROBS_D[effort] @ LOSSES_D)


def reservation_utility_d() -> float:
    """Return the utility of not buying, with the best effort."""
    return max(
        float(PROBS_D[effort] @ np.log(WEALTH_D - LOSSES_D)) - EFFORT_COST_D[effort]
        for effort in PROBS_D
    )


def best_levels_d(effort: int, with_incentive: bool) -> np.ndarray:
    """Solve the company's problem for ``effort`` and return the utility levels u(z_l).

    Args:
        effort: Effort level the company wants to induce, 0 or 1.
        with_incentive: Whether the client must prefer ``effort`` to the other level.

    Raises:
        CheckFailed: If the solver does not converge.
    """
    reserve = reservation_utility_d()
    other = next(level for level in PROBS_D if level != effort)
    participation = {"type": "ineq", "fun": lambda x: client_utility_d(effort, x) - reserve}
    incentive = {
        "type": "ineq",
        "fun": lambda x: client_utility_d(effort, x) - client_utility_d(other, x),
    }
    result = minimize(
        lambda x: -profit_d(effort, x),
        START_LEVELS,
        method="SLSQP",
        bounds=LEVEL_BOUNDS,
        constraints=[participation, incentive] if with_incentive else [participation],
        options={"ftol": SOLVER_TOLERANCE, "maxiter": SOLVER_ITERATIONS},
    )
    check(result.success, result.message)
    return result.x


def indemnity_gaps_d(levels: Sequence[float]) -> np.ndarray:
    """Return B_l - l = z_l - z_0 for each state, with the normalisation B_0 = 0."""
    wealth = np.exp(np.asarray(levels))
    return wealth - wealth[0]


def first_best_profit_d(effort: int) -> float:
    """Return the first-best profit p(e) - E_e[l] with p(e) = w - exp(d(e) + reserve)."""
    premium = WEALTH_D - math.exp(EFFORT_COST_D[effort] + reservation_utility_d())
    return premium - float(PROBS_D[effort] @ LOSSES_D)


def describe_instance_d() -> str:
    """Return the data line of question D, built from the constants so it cannot drift."""
    losses = ",".join(f"{loss:g}" for loss in LOSSES_D)
    return (
        f"D.1  toy instance: u = ln, w = {WEALTH_D:g}, l in {{{losses}}}, "
        f"d(0) = {EFFORT_COST_D[0]:g}, d(1) = {EFFORT_COST_D[1]:.2f}"
    )


def d1_full_cover() -> list[str]:
    """Check that the observable-effort optimum is full cover with a binding PC."""
    reserve = reservation_utility_d()
    lines = [describe_instance_d()]
    for effort in PROBS_D:
        levels = best_levels_d(effort, with_incentive=False)
        check(
            np.allclose(indemnity_gaps_d(levels), 0.0, atol=POLICY_TOLERANCE),
            "the observable-effort optimum must be full cover",
        )
        check(
            abs(client_utility_d(effort, levels) - reserve) < POLICY_TOLERANCE,
            "the participation constraint must bind",
        )
        premium = WEALTH_D - math.exp(levels[0])
        closed_form = WEALTH_D - math.exp(EFFORT_COST_D[effort] + reserve)
        check(
            abs(premium - closed_form) < POLICY_TOLERANCE,
            "the premium must match its closed form",
        )
        lines.append(f"     e = {effort}: p = {premium:.4f} ; B_l - l = (0, 0, 0) ; PC binds")
    return lines


def d2_low_effort_incentive() -> list[str]:
    """Check that full cover satisfies IC for e = 0 and the constrained optimum equals it."""
    constrained = best_levels_d(0, with_incentive=True)
    free = best_levels_d(0, with_incentive=False)
    check(
        np.allclose(constrained, free, atol=POLICY_TOLERANCE),
        "IC must leave the e = 0 optimum unchanged",
    )
    slack = client_utility_d(0, free) - client_utility_d(1, free)
    check(
        math.isclose(slack, EFFORT_COST_D[1] - EFFORT_COST_D[0], abs_tol=POLICY_TOLERANCE),
        "the IC slack must equal d(1) - d(0)",
    )
    return [
        f"D.2  e = 0 with IC: p = {WEALTH_D - math.exp(constrained[0]):.4f}, B_l - l = (0, 0, 0)",
        f"     IC slack at full cover = d(1) - d(0) = {slack:.4f} > 0",
    ]


def d3_efficiency() -> list[str]:
    """Compare first-best profits and the best profit when e = 1 must satisfy PC and IC."""
    ratios = PROBS_D[0] / PROBS_D[1]
    check(np.all(np.diff(ratios) > 0), "likelihood ratios must be strictly increasing (MLR)")
    first_best = {effort: first_best_profit_d(effort) for effort in PROBS_D}
    check(first_best[0] > first_best[1], "the first best must pick e = 0")
    levels = best_levels_d(1, with_incentive=True)
    second_best_high = profit_d(1, levels)
    check(
        second_best_high < first_best[1] < first_best[0],
        "inducing e = 1 must earn less than its first best",
    )
    gaps = indemnity_gaps_d(levels)
    check(0 > gaps[1] > gaps[2], "B_l - l must be strictly decreasing")
    return [
        f"D.3  MLR ratios r_l = {np.round(ratios, 3).tolist()} (increasing)",
        f"     first best: Pi(0) = {first_best[0]:.4f} > Pi(1) = {first_best[1]:.4f}, so e* = 0",
        f"     e = 1 with IC: profit {second_best_high:.4f} < Pi(1); "
        f"B_l - l = (0, {gaps[1]:.4f}, {gaps[2]:.4f}) strictly decreasing",
        f"     second best keeps e = 0, same policy, profit {first_best[0]:.4f}",
    ]


# --- Domanda E ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Utility:
    """An increasing concave utility with its first two derivatives.

    Attributes:
        name: Label used in the printed output.
        level: Function u(w).
        first: Function u'(w).
        second: Function u''(w).
    """

    name: str
    level: Callable[[float], float]
    first: Callable[[float], float]
    second: Callable[[float], float]


UTILITIES_E = (
    Utility("ln", math.log, lambda w: 1 / w, lambda w: -1 / w**2),
    Utility("-1/w", lambda w: -1 / w, lambda w: w**-2, lambda w: -2 * w**-3),
    Utility(
        "CARA 0.01",
        lambda w: -math.exp(-CARA_RATE * w) / CARA_RATE,
        lambda w: math.exp(-CARA_RATE * w),
        lambda w: -CARA_RATE * math.exp(-CARA_RATE * w),
    ),
)
# CRRA with gamma = 1/2 (RR = 1/2 < 1): the utility of the monotonicity proof.
SQRT_UTILITY = Utility(
    "2*sqrt(w)", lambda w: 2 * math.sqrt(w), lambda w: w**-0.5, lambda w: -0.5 * w**-1.5
)


def objective_e(utility: Utility, wealth0: float, alpha: float, lottery) -> float:
    """Return V(alpha) = E[u(w0 + alpha x)] for ``lottery = (returns, probs)``."""
    returns, probs = lottery
    return float(sum(p * utility.level(wealth0 + alpha * x) for x, p in zip(returns, probs)))


def slope_e(utility: Utility, wealth0: float, alpha: float, lottery) -> float:
    """Return V'(alpha) = E[x u'(w0 + alpha x)] for ``lottery = (returns, probs)``."""
    returns, probs = lottery
    return float(sum(p * x * utility.first(wealth0 + alpha * x) for x, p in zip(returns, probs)))


def curvature_e(utility: Utility, wealth0: float, alpha: float, lottery) -> float:
    """Return V''(alpha) = E[x^2 u''(w0 + alpha x)] for ``lottery = (returns, probs)``."""
    returns, probs = lottery
    return float(
        sum(p * x**2 * utility.second(wealth0 + alpha * x) for x, p in zip(returns, probs))
    )


def optimum_e(utility: Utility, wealth0: float, lottery) -> float:
    """Return the maximiser of V on [0, W], with W = w0 because r = 0."""
    if slope_e(utility, wealth0, wealth0, lottery) >= 0:
        return wealth0
    return brentq(lambda alpha: slope_e(utility, wealth0, alpha, lottery), 0.0, wealth0)


def implicit_derivative_e(utility: Utility, wealth0: float, alpha: float, lottery) -> float:
    """Return d alpha*/d w0 = -E[x u''] / E[x^2 u''] at an interior optimum."""
    returns, probs = lottery
    cross = sum(p * x * utility.second(wealth0 + alpha * x) for x, p in zip(returns, probs))
    return -cross / curvature_e(utility, wealth0, alpha, lottery)


def check_derivatives_e(utility: Utility, lottery) -> None:
    """Check V' and V'' against finite differences of V at a probe investment."""
    def level(alpha: float) -> float:
        """Return V(alpha) at the fixed wealth and lottery."""
        return objective_e(utility, WEALTH_E, alpha, lottery)

    slope = slope_e(utility, WEALTH_E, PROBE_ALPHA, lottery)
    curvature = curvature_e(utility, WEALTH_E, PROBE_ALPHA, lottery)
    check(
        math.isclose(finite_derivative(level, PROBE_ALPHA, 1), slope, rel_tol=RELATIVE_TOLERANCE),
        "V' must match the finite difference of V",
    )
    second_difference = finite_derivative(level, PROBE_ALPHA, 2)
    check(
        math.isclose(second_difference, curvature, rel_tol=RELATIVE_TOLERANCE),
        "V'' must match the finite difference of V",
    )


def describe_portfolio_e() -> str:
    """Return the data line of question E, built from the constants so it cannot drift."""
    returns = " or ".join(f"{excess:+g}" for excess in EXCESS_RETURNS_E)
    probability = Fraction(PROBS_E[0]).limit_denominator()
    return (
        f"E.1  r = {RISK_FREE_E:g}, W = w0 = {WEALTH_E:g}, x = {returns} "
        f"with probability {probability}"
    )


def e1_first_order() -> list[str]:
    """Check V', V'', the FOC and the implicit derivative of alpha* with respect to w0."""
    check(RISK_FREE_E == 0, "the functions of question E take W = w0, which holds only for r = 0")
    lottery = (EXCESS_RETURNS_E, PROBS_E)
    lines = [describe_portfolio_e()]
    for utility in UTILITIES_E:
        check_derivatives_e(utility, lottery)
        alpha = optimum_e(utility, WEALTH_E, lottery)
        formula = implicit_derivative_e(utility, WEALTH_E, alpha, lottery)
        below = optimum_e(utility, WEALTH_E - WEALTH_STEP_E, lottery)
        above = optimum_e(utility, WEALTH_E + WEALTH_STEP_E, lottery)
        numeric = (above - below) / (2 * WEALTH_STEP_E)
        check(
            math.isclose(formula, numeric, rel_tol=RELATIVE_TOLERANCE, abs_tol=ZERO_TOLERANCE),
            "the implicit derivative must match the finite difference of alpha*",
        )
        lines.append(f"     {utility.name}: alpha* = {alpha:.4f} ; d alpha*/d w0 = {formula:.4f}")
    return lines


def check_derivative_identity_e() -> None:
    """Check h'(y) = u'(w0 + y) [1 - RR + w0 A] against finite differences for every utility."""
    cases = itertools.product(UTILITIES_E + (SQRT_UTILITY,), PROBE_WEALTHS_E, PROBE_SHIFTS_E)
    for utility, wealth0, shift in cases:
        point = wealth0 + shift
        absolute = -utility.second(point) / utility.first(point)
        closed = utility.first(point) * (1 - point * absolute + wealth0 * absolute)
        numeric = finite_derivative(lambda y: y * utility.first(wealth0 + y), shift, 1)
        check(
            math.isclose(closed, numeric, rel_tol=RELATIVE_TOLERANCE, abs_tol=ZERO_TOLERANCE),
            "h' must match its closed form",
        )


def mean_preserving_spread(returns: np.ndarray, probs: np.ndarray, spreads: np.ndarray):
    """Split each return x into x - s and x + s with equal probability."""
    new_returns = np.concatenate([returns - spreads, returns + spreads])
    return new_returns, np.concatenate([probs / 2, probs / 2])


def concave_on_grid(utility: Utility, wealth0: float, alpha: float) -> bool:
    """Return whether g(x) = x u'(w0 + alpha x) has no positive second difference on the grid."""
    def g(x: float) -> float:
        """Return g(x) = x u'(w0 + alpha x)."""
        return x * utility.first(wealth0 + alpha * x)

    step = GRID_E[1] - GRID_E[0]
    second = [g(a) - 2 * g(b) + g(c) for a, b, c in zip(GRID_E, GRID_E[1:], GRID_E[2:])]
    return max(second) / step**2 <= ZERO_TOLERANCE


def sosd_trial(rng: np.random.Generator) -> float | None:
    """Draw one pair F_2 SOSD F_1 and return alpha_2* - alpha_1*, or None if not admissible.

    The pair is admissible when the riskier lottery F_1 has a positive mean and an interior
    optimum, the setting of the proof.
    """
    returns = np.sort(rng.uniform(*RETURN_RANGE_E, size=RANDOM_OUTCOMES_E))
    probs = rng.dirichlet(np.ones(RANDOM_OUTCOMES_E))
    spreads = rng.uniform(*SPREAD_RANGE_E, size=RANDOM_OUTCOMES_E)
    risky = mean_preserving_spread(returns, probs, spreads)
    if returns @ probs <= 0 or slope_e(SQRT_UTILITY, WEALTH_E, WEALTH_E, risky) >= 0:
        return None
    alpha_risky = optimum_e(SQRT_UTILITY, WEALTH_E, risky)
    check(concave_on_grid(SQRT_UTILITY, WEALTH_E, alpha_risky), "g must be concave on the grid")
    return optimum_e(SQRT_UTILITY, WEALTH_E, (returns, probs)) - alpha_risky


def e2_monotonicity() -> list[str]:
    """Check h', and that alpha_2* >= alpha_1* for random SOSD pairs when RR < 1."""
    check_derivative_identity_e()
    rng = np.random.default_rng(SEED)
    gaps = [gap for gap in (sosd_trial(rng) for _ in range(RANDOM_TRIALS_E)) if gap is not None]
    check(len(gaps) >= MIN_ADMISSIBLE_TRIALS, "too few admissible random pairs")
    check(min(gaps) >= -ALPHA_TOLERANCE, "alpha_2* must not fall below alpha_1*")
    return [
        "E.2  h'(y) = u'(w0+y)[1 - RR + w0 A] matches finite differences "
        f"({len(UTILITIES_E) + 1} utilities)",
        f"     u = 2 sqrt(w), RR = 1/2: {len(gaps)} random SOSD pairs, g concave, "
        f"smallest alpha_2* - alpha_1* = {min(gaps):.4f} >= 0",
    ]


SECTIONS = (
    a1_arrow_pratt,
    a2_certain_equivalent,
    a3_wealth_effect,
    a4_small_lottery,
    b1_fair_premium,
    b2_certain_equivalent,
    b3_adverse_selection,
    c1_first_order,
    c2_second_order,
    c3_independence,
    c4_triangle,
    d1_full_cover,
    d2_low_effort_incentive,
    d3_efficiency,
    e1_first_order,
    e2_monotonicity,
)


def main() -> None:
    """Run every section and print its figures."""
    for section in SECTIONS:
        print("\n".join(section()))


if __name__ == "__main__":
    main()
