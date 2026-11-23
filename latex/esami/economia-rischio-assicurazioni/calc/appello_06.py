"""Calculations behind the simulated appello 06 of Economia del Rischio e delle Assicurazioni.

The constants below are the data printed in ERA_Esame_Simulato_06.md. Every figure quoted in
ERA_Soluzioni_Simulato_06.md and in the answer key of piano/appello-06.json is printed by this
script. Exact results are Fractions, irrational ones are floats. Closed forms are checked against
exact integer identities, root finding or constrained optimisation, and a disagreement raises
CheckFailed.

Run it from the repository root with
``python latex/esami/economia-rischio-assicurazioni/calc/appello_06.py``. It writes no file.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import accumulate
from typing import Sequence

from scipy.optimize import brentq

from comune import (
    LOG,
    absolute_aversion,
    check,
    check_derivatives,
    close,
    crra_utility,
    expect,
    expected_slope,
    float_outcomes,
    fmt,
    prudence,
    vector,
)

EQUAL_PROB = Fraction(1, 2)
# Roots found numerically are rational by construction of the data; this bound recovers them.
MAX_DENOMINATOR = 1000

# Domanda A: CRRA with an integer gamma; X = +-HALF_RANGE_A with equal probability at WEALTH_A.
CRRA_GAMMA = 3
WEALTH_A = 20
HALF_RANGE_A = 15
SMALL_SCALE_A = 1e-3

# Domanda B: u = ln, a bet that wins GAIN_B or loses LOSS_B, taken at WEALTH_B and then at double.
WEALTH_B = 30
GAIN_B = 90
LOSS_B = 15
DOUBLING_B = 2

# Domanda C: three prizes and two pairs of lotteries, written as probability vectors.
PRIZES_C = (Fraction(10), Fraction(30), Fraction(70))
CENTRE_C = 1
LOTTERY_P = (Fraction(1, 10), Fraction(6, 10), Fraction(3, 10))
LOTTERY_Q = (Fraction(4, 10), Fraction(2, 10), Fraction(4, 10))
LOTTERY_P2 = (Fraction(2, 6), Fraction(3, 6), Fraction(1, 6))
MIX_WEIGHT_C = Fraction(1, 2)

# Domanda D: u = ln, losses 0, 1, 2, a test pair of multipliers with lambda > beta (r_L - 1).
WEALTH_D = Fraction(20)
LOSSES_D = (0, 1, 2)
NO_LOSS_STATE = 0
WORST_LOSS_STATE = -1
LOW_EFFORT_PROBS = (Fraction(3, 10), Fraction(3, 10), Fraction(4, 10))
HIGH_EFFORT_PROBS = (Fraction(6, 10), Fraction(3, 10), Fraction(1, 10))
LAMBDA_D = Fraction(4)
BETA_D = Fraction(1, 2)

# Domanda E: u = ln, WEALTH_E invested at the net rate RISK_FREE_E, risky net return of two values.
WEALTH_E = 120
RISK_FREE_E = Fraction(1, 20)
NET_RETURNS_E = (Fraction(-2, 5), Fraction(4, 5))
EXCESS_RETURNS_E = tuple(net - RISK_FREE_E for net in NET_RETURNS_E)
PROBS_E = (EQUAL_PROB, EQUAL_PROB)
FINAL_WEALTH_E = WEALTH_E * (1 + RISK_FREE_E)
TAX_E = Fraction(1, 8)
HIGH_TAX_E = Fraction(3, 4)
SURVIVAL_E = Fraction(1, 2)
POSITIVE_EXCESS_E = (Fraction(1, 5), Fraction(3, 5))


def crra_level(wealth: Fraction) -> Fraction:
    """Return the exact CRRA utility W^(1-gamma)/(1-gamma), valid for an integer gamma."""
    return wealth ** (1 - CRRA_GAMMA) / (1 - CRRA_GAMMA)


def premium(spread: float) -> float:
    """Return R = w - CE for the lottery +-spread, inverting the CRRA utility in closed form."""
    utility = crra_utility(CRRA_GAMMA)
    expected = float(EQUAL_PROB) * (
        utility.level(WEALTH_A - spread) + utility.level(WEALTH_A + spread)
    )
    return WEALTH_A - ((1 - CRRA_GAMMA) * expected) ** (1 / (1 - CRRA_GAMMA))


def a1_measures() -> list[str]:
    """A.1: A(W), RR(W) and P(W) of the CRRA utility, checked at one wealth."""
    utility = crra_utility(CRRA_GAMMA)
    aversion = absolute_aversion(utility, WEALTH_A)
    check_derivatives(utility, WEALTH_A)
    check(close(aversion, CRRA_GAMMA / WEALTH_A), "A(W) must be gamma / W")
    check(close(WEALTH_A * aversion, CRRA_GAMMA), "RR(W) must be gamma")
    check(close(prudence(utility, WEALTH_A), (CRRA_GAMMA + 1) / WEALTH_A), "P(W) = (1 + gamma)/W")
    power = CRRA_GAMMA - 1
    return [
        f"A.1  u(W) = -1/({power} W^{power}), A(W) = {CRRA_GAMMA}/W, RR(W) = {CRRA_GAMMA}, "
        f"P(W) = {CRRA_GAMMA + 1}/W"
    ]


def a2_certain_equivalent() -> list[str]:
    """A.2: certain equivalent and premium, checked exactly with Fractions."""
    low, high = Fraction(WEALTH_A - HALF_RANGE_A), Fraction(WEALTH_A + HALF_RANGE_A)
    expected = EQUAL_PROB * (crra_level(low) + crra_level(high))
    certain_equivalent = Fraction(round(WEALTH_A - premium(HALF_RANGE_A)))
    check(crra_level(certain_equivalent) == expected, "the certain equivalent must be rational")
    return [
        f"A.2  final wealth {low} or {high}, E[u] = {fmt(expected)}, "
        f"CE = {fmt(certain_equivalent)}, R = {fmt(WEALTH_A - certain_equivalent)}"
    ]


def a3_arrow_pratt_approximation() -> list[str]:
    """A.3: Arrow-Pratt approximation against the exact premium of A.2."""
    approximation = Fraction(CRRA_GAMMA, 2 * WEALTH_A) * HALF_RANGE_A**2
    exact = premium(HALF_RANGE_A)
    scaled = premium(HALF_RANGE_A * SMALL_SCALE_A) / SMALL_SCALE_A**2
    check(close(scaled, float(approximation)), "R(k) / k^2 must tend to A(w) E[X^2] / 2")
    check(approximation > exact, "the approximation must exceed the exact premium here")
    lowest = WEALTH_A - HALF_RANGE_A
    return [
        f"A.3  A(w) = {Fraction(CRRA_GAMMA, WEALTH_A)}, E[X^2] = {HALF_RANGE_A**2}, "
        f"approximation = {fmt(approximation)}, exact R = {exact:.4f}, "
        f"gap = {float(approximation) - exact:.4f}; "
        f"A(w - b) = {Fraction(CRRA_GAMMA, lowest)} = {Fraction(WEALTH_A, lowest)} A(w)"
    ]


def indifference_probability() -> Fraction:
    """Return the win probability that leaves the ln-agent indifferent at WEALTH_B."""
    kept = WEALTH_B - LOSS_B
    probability = math.log(WEALTH_B / kept) / math.log((WEALTH_B + GAIN_B) / kept)
    return Fraction(probability).limit_denominator(MAX_DENOMINATOR)


def accept_sides(wealth: int, win_probability: Fraction) -> tuple[int, int, str]:
    """Compare taking and refusing the bet with whole numbers.

    E[ln(wealth + X)] >= ln(wealth) iff (w + g)^theta (w - l)^(1 - theta) >= w; both sides are
    raised to the denominator of theta, which keeps the comparison in whole numbers.

    Args:
        wealth: Initial wealth.
        win_probability: Probability of winning, as an exact fraction.

    Returns:
        The two integers (taking, refusing) and the text of the comparison, for the printout.
    """
    numerator, denominator = win_probability.numerator, win_probability.denominator
    loss_power = denominator - numerator
    taking = (wealth + GAIN_B) ** numerator * (wealth - LOSS_B) ** loss_power
    refusing = wealth**denominator
    comparison = (
        f"({wealth + GAIN_B})^{numerator} ({wealth - LOSS_B})^{loss_power} = {taking} "
        f"versus {wealth}^{denominator} = {refusing}"
    )
    return taking, refusing, comparison


def b1_indifference(win_probability: Fraction) -> list[str]:
    """B.1: the indifference probability, verified as an exact integer identity."""
    taking, refusing, comparison = accept_sides(WEALTH_B, win_probability)
    check(taking == refusing, "theta must make the agent exactly indifferent")
    return [f"B.1  theta = {win_probability}: {comparison}"]


def b2_expected_gain_and_premium(win_probability: Fraction) -> list[str]:
    """B.2: expected gain, certain equivalent and premium (expected wealth minus CE)."""
    expected_gain = win_probability * GAIN_B - (1 - win_probability) * LOSS_B
    log_if_win = math.log(WEALTH_B + GAIN_B)
    log_if_loss = math.log(WEALTH_B - LOSS_B)
    expected_log = win_probability * log_if_win + (1 - win_probability) * log_if_loss
    certain_equivalent = math.exp(expected_log)
    check(close(certain_equivalent, WEALTH_B), "indifference at w means CE = w")
    risk_premium = WEALTH_B + expected_gain - certain_equivalent
    check(close(risk_premium, float(expected_gain)), "the premium must equal E[X] when CE = w")
    return [
        f"B.2  E[X] = {fmt(expected_gain)}, CE = {certain_equivalent:.4f}, "
        f"R = E[w + X] - CE = {risk_premium:.4f}"
    ]


def b3_doubled_wealth(win_probability: Fraction) -> list[str]:
    """B.3: the same bet at double the wealth, compared with whole-number powers."""
    wealth = DOUBLING_B * WEALTH_B
    taking, refusing, comparison = accept_sides(wealth, win_probability)
    check(taking > refusing, "the agent must accept at double the wealth")
    expected_utility_gain = math.log(taking / refusing) / win_probability.denominator
    return [
        f"B.3  w = {wealth}: {comparison} (ratio {taking / refusing:.3f}); "
        f"E[u] - u(w) = {expected_utility_gain:.4f}"
    ]


def cdf(probs: Sequence[Fraction]) -> tuple[Fraction, ...]:
    """Return the c.d.f. values of a lottery at each prize."""
    return tuple(accumulate(probs))


def cdf_integrals(probs: Sequence[Fraction]) -> tuple[Fraction, ...]:
    """Return the integral of the c.d.f. from the lowest prize up to each prize."""
    widths = (high - low for low, high in zip(PRIZES_C, PRIZES_C[1:]))
    # The c.d.f. at the top prize closes no interval, so only the lower endpoint of each counts.
    steps = (width * level for width, level in zip(widths, cdf(probs)[:-1], strict=True))
    return (Fraction(0), *accumulate(steps))


def mean_checked(probs: Sequence[Fraction]) -> Fraction:
    """Return E[X], checked against the identity E[X] = top prize - integral of the c.d.f."""
    mean = expect(PRIZES_C, probs)
    check(PRIZES_C[-1] - mean == cdf_integrals(probs)[-1], "c.d.f. integral and mean disagree")
    return mean


def mixed_with_centre() -> tuple[Fraction, ...]:
    """Return q' = w P2 + (1 - w) (certain middle prize), the compound lottery of C.3."""
    return tuple(
        MIX_WEIGHT_C * spread + (1 - MIX_WEIGHT_C) * int(index == CENTRE_C)
        for index, spread in enumerate(LOTTERY_P2)
    )


def dominates_at_second_order(better: Sequence[Fraction], worse: Sequence[Fraction]) -> bool:
    """Return whether the integrals of the c.d.f. of ``better`` never exceed those of ``worse``."""
    return all(low <= high for low, high in zip(cdf_integrals(better), cdf_integrals(worse)))


def c1_crossing() -> list[str]:
    """C.1: the c.d.f.s of p and q cross although p has the higher mean."""
    gaps = [first - second for first, second in zip(cdf(LOTTERY_P), cdf(LOTTERY_Q))]
    check(min(gaps) < 0 < max(gaps), "the c.d.f.s must cross")
    mean_p, mean_q = mean_checked(LOTTERY_P), mean_checked(LOTTERY_Q)
    check(mean_p > mean_q, "p must have the higher mean")
    return [
        f"C.1  c.d.f. p = {vector(cdf(LOTTERY_P))}, c.d.f. q = {vector(cdf(LOTTERY_Q))}; "
        f"E[p] = {fmt(mean_p)}, E[q] = {fmt(mean_q)}"
    ]


def c2_second_order() -> list[str]:
    """C.2: p dominates q at second order with different means, so no mean-preserving spread."""
    integral_p, integral_q = cdf_integrals(LOTTERY_P), cdf_integrals(LOTTERY_Q)
    check(dominates_at_second_order(LOTTERY_P, LOTTERY_Q), "p must dominate q")
    check(integral_p != integral_q, "the dominance must be strict somewhere")
    check(expect(PRIZES_C, LOTTERY_P) != expect(PRIZES_C, LOTTERY_Q), "the means must differ")
    return [
        f"C.2  integrals of the c.d.f. at the prizes: p = {vector(integral_p)}, "
        f"q = {vector(integral_q)}"
    ]


def c3_mean_preserving_spread() -> list[str]:
    """C.3: P2 is a mean-preserving spread of q', so q' dominates it at second order."""
    centre = PRIZES_C[CENTRE_C]
    check(expect(PRIZES_C, LOTTERY_P2) == centre, "the mean of p' must be the middle prize")
    mixed = mixed_with_centre()
    # The mass of q' on the middle prize is spread over the three prizes to rebuild p'.
    noise = tuple(
        (spread - (0 if index == CENTRE_C else coarse)) / mixed[CENTRE_C]
        for index, (spread, coarse) in enumerate(zip(LOTTERY_P2, mixed, strict=True))
    )
    check(sum(noise) == 1 and min(noise) >= 0, "the noise weights must be probabilities")
    noise_mean = sum(weight * (prize - centre) for weight, prize in zip(noise, PRIZES_C))
    check(noise_mean == 0, "the noise must have conditional mean zero")
    check(dominates_at_second_order(mixed, LOTTERY_P2), "q' must dominate p' at second order")
    return [
        f"C.3  E[p'] = {fmt(centre)}, q' = {vector(mixed)}, noise from the middle prize: "
        f"{vector(noise)}; integrals of the c.d.f.: q' = {vector(cdf_integrals(mixed))}, "
        f"p' = {vector(cdf_integrals(LOTTERY_P2))}"
    ]


def d1_policy_from_condition() -> list[str]:
    """D.1: r_l, B_l - l and the premium, checked against condition (5) of the note."""
    ratios = tuple(low / high for low, high in zip(LOW_EFFORT_PROBS, HIGH_EFFORT_PROBS))
    check(all(first < second for first, second in zip(ratios, ratios[1:])), "MLR must hold")
    base_ratio = ratios[NO_LOSS_STATE]
    premium_d = WEALTH_D - LAMBDA_D - BETA_D * (1 - base_ratio)
    indemnities = tuple(
        loss - BETA_D * (ratio - base_ratio) for loss, ratio in zip(LOSSES_D, ratios)
    )
    for loss, ratio, paid in zip(LOSSES_D, ratios, indemnities):
        wealth = WEALTH_D - premium_d - loss + paid
        check(wealth > 0, "final wealth must be positive")
        condition = float(LAMBDA_D + BETA_D * (1 - ratio))
        check(close(1 / LOG.first(float(wealth)), condition), "condition (5) must hold")
    check(indemnities[NO_LOSS_STATE] == 0, "B_0 must be zero")
    first_loss_state = NO_LOSS_STATE + 1
    deductibles = tuple(ratio - base_ratio for ratio in ratios[first_loss_state:])
    loss_labels = ", ".join(str(loss) for loss in LOSSES_D[first_loss_state:])
    return [
        f"D.1  r = {vector(ratios)}; l - B_l = beta (r_l - r_0), coefficients for l = "
        f"{loss_labels}: {vector(deductibles)}; z_2 > 0 iff lambda > beta (r_L - 1) = "
        f"{fmt(ratios[WORST_LOSS_STATE] - 1)} beta",
        f"     test lambda = {LAMBDA_D}, beta = {BETA_D}, w = {WEALTH_D}: p = {fmt(premium_d)}, "
        f"B = {vector(indemnities)}",
    ]


def best_amount(excess: Sequence[Fraction], probs: Sequence[Fraction]) -> float:
    """Return the maximiser on [0, W] of E[ln(w0 + a x)] for a finite excess return.

    The helper in comune.py ties the upper bound to w0, which is wrong once r > 0 (w0 = W (1 + r)),
    so the bound is passed apart here.
    """
    outcomes = float_outcomes(excess, probs)

    def slope(amount: float) -> float:
        """Return V'(amount), the derivative of the expected utility at the invested amount."""
        return expected_slope(LOG.first, float(FINAL_WEALTH_E), outcomes, amount)

    if slope(0.0) <= 0:
        return 0.0
    if slope(WEALTH_E) >= 0:
        return float(WEALTH_E)
    return brentq(slope, 0.0, WEALTH_E)


def optimal_investment() -> Fraction:
    """Return the untaxed optimum alpha* of the base problem, as an exact fraction."""
    amount = best_amount(EXCESS_RETURNS_E, PROBS_E)
    optimum = Fraction(amount).limit_denominator(MAX_DENOMINATOR)
    check(close(amount, float(optimum)), "alpha* must be rational")
    check(0 < optimum < WEALTH_E, "alpha* must be interior")
    return optimum


def survival_probs(probs: Sequence[Fraction]) -> tuple[Fraction, ...]:
    """Return the probabilities of (x, ..., 0) when x survives with probability SURVIVAL_E."""
    return (*(SURVIVAL_E * prob for prob in probs), 1 - SURVIVAL_E)


def after_tax_amount(rate: Fraction) -> float:
    """Return the optimum when the excess return is scaled by 1 - rate (tax with loss subsidy)."""
    return best_amount([(1 - rate) * excess for excess in EXCESS_RETURNS_E], PROBS_E)


def e1_tax(optimum: Fraction) -> list[str]:
    """E.1: investment after a tax with loss subsidy, and the rate from which W binds."""
    lines = [f"E.1  alpha* = {fmt(optimum)} (W = {WEALTH_E}, w0 = {fmt(FINAL_WEALTH_E)})"]
    for rate in (TAX_E, HIGH_TAX_E):
        uncapped = optimum / (1 - rate)
        invested = min(uncapped, Fraction(WEALTH_E))
        check(close(after_tax_amount(rate), float(invested)), "alpha*/(1 - tau), capped at W")
        lines.append(
            f"     tau = {rate}: alpha*/(1 - tau) = {fmt(uncapped)}, invests {fmt(invested)}"
        )
    threshold = 1 - optimum / WEALTH_E
    check(close(after_tax_amount(threshold), WEALTH_E), "at the threshold alpha*/(1 - tau) = W")
    lines.append(f"     W binds for tau >= 1 - alpha*/W = {fmt(threshold)}")
    return lines


def e2a_unchanged_optimum(optimum: Fraction) -> list[str]:
    """E.2 (a): replacing x by a variable equal to x with probability s leaves alpha* unchanged."""
    diluted = best_amount((*EXCESS_RETURNS_E, Fraction(0)), survival_probs(PROBS_E))
    check(close(diluted, float(optimum)), "the optimum must not change")
    return [f"E.2a s = {SURVIVAL_E}: alpha* = {fmt(optimum)}, with the new variable {diluted:.4f}"]


def cdf_at(atoms: Sequence[Fraction], probs: Sequence[Fraction], point: Fraction) -> Fraction:
    """Return P(X <= point) for a finite distribution."""
    return sum((prob for atom, prob in zip(atoms, probs) if atom <= point), Fraction(0))


def e2b_first_order_comparison() -> list[str]:
    """E.2 (b): with x > 0 the c.d.f. of x lies below that of the new variable; alpha = W."""
    diluted_atoms = (*POSITIVE_EXCESS_E, Fraction(0))
    diluted_probs = survival_probs(PROBS_E)
    for atoms, probs in ((POSITIVE_EXCESS_E, PROBS_E), (diluted_atoms, diluted_probs)):
        outcomes = float_outcomes(atoms, probs)
        slope_at_cap = expected_slope(LOG.first, float(FINAL_WEALTH_E), outcomes, WEALTH_E)
        check(slope_at_cap > 0, "with x > 0 the corner W must be optimal")
    points = (Fraction(0), *POSITIVE_EXCESS_E)
    original_cdf = [cdf_at(POSITIVE_EXCESS_E, PROBS_E, point) for point in points]
    diluted_cdf = [cdf_at(diluted_atoms, diluted_probs, point) for point in points]
    expected_cdf = [1 - SURVIVAL_E + SURVIVAL_E * level for level in original_cdf]
    check(diluted_cdf == expected_cdf, "G must equal (1 - s) + s F")
    check(
        all(
            diluted_level >= original_level
            for diluted_level, original_level in zip(diluted_cdf, original_cdf, strict=True)
        ),
        "F must dominate G",
    )
    return [
        f"E.2b x in {vector(POSITIVE_EXCESS_E)}, points {vector(points)}: F = "
        f"{vector(original_cdf)}, G = {vector(diluted_cdf)}; slope at W positive in both cases"
    ]


def e2c_vanishing_net_return(optimum: Fraction) -> list[str]:
    """E.2 (c): if the net return vanishes with r > 0, the slope at alpha* is negative."""
    vanishing = (*EXCESS_RETURNS_E, -RISK_FREE_E)
    probs = survival_probs(PROBS_E)
    outcomes = float_outcomes(vanishing, probs)
    slope = expected_slope(LOG.first, float(FINAL_WEALTH_E), outcomes, float(optimum))
    closed_form = -(1 - SURVIVAL_E) * RISK_FREE_E / (FINAL_WEALTH_E - optimum * RISK_FREE_E)
    check(close(slope, float(closed_form)), "V'(alpha*) = -(1 - s) r u'(w0 - alpha* r)")
    check(slope < 0, "the slope at alpha* must be negative")
    lowered = best_amount(vanishing, probs)
    check(lowered < float(optimum), "the investment must fall")
    return [
        f"E.2c r = {RISK_FREE_E}: V'(alpha*) = -(1 - s) r / (w0 - alpha* r) = {slope:.6f}; "
        f"new optimum {lowered:.4f} < {fmt(optimum)}"
    ]


def main() -> None:
    """Run every section and print its figures."""
    win_probability = indifference_probability()
    optimum = optimal_investment()
    sections = (
        a1_measures(),
        a2_certain_equivalent(),
        a3_arrow_pratt_approximation(),
        b1_indifference(win_probability),
        b2_expected_gain_and_premium(win_probability),
        b3_doubled_wealth(win_probability),
        c1_crossing(),
        c2_second_order(),
        c3_mean_preserving_spread(),
        d1_policy_from_condition(),
        e1_tax(optimum),
        e2a_unchanged_optimum(optimum),
        e2b_first_order_comparison(),
        e2c_vanishing_net_return(optimum),
    )
    for lines in sections:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
