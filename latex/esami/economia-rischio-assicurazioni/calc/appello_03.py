"""Calculations behind the simulated appello 03 of Economia del Rischio e delle Assicurazioni.

The constants below are the data of ERA_Esame_Simulato_03.md; every figure quoted in
ERA_Soluzioni_Simulato_03.md and in piano/appello-03.json is printed here. Closed forms are checked
against the definition, finite differences or root finding, and a disagreement raises CheckFailed.
Run it from the repository root with ``python <path of this file>``; it writes no file.
"""

from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Iterable
from fractions import Fraction
from functools import partial
from typing import NamedTuple

import numpy as np

from comune import (
    LOG,
    Outcomes,
    Utility,
    absolute_aversion,
    cara_utility,
    check,
    close,
    crra_utility,
    expect,
    expected_utility,
    finite_derivative,
    float_outcomes,
    fmt,
    optimal_alpha,
    prudence,
    vector,
)

Distribution = dict[Fraction, Fraction]


class SquareUtility(NamedTuple):
    """The utility u(x) = sign * (x - anchor)^2."""

    sign: int
    anchor: Fraction


# Domanda A: CARA utility. The lottery loses 3/2 ln 2 or gains 1/2 ln 2, so exp(-rate * x) is
# 8 or 1/2 and the premium has a closed form.
CARA_RATE = 2
LOTTERY_BASE = 2
LN_BASE = math.log(LOTTERY_BASE)
LOTTERY_STEPS = (Fraction(-3, 2), Fraction(1, 2))  # multiples of ln 2
LOTTERY_PROBS = (Fraction(1, 4), Fraction(3, 4))
WEALTH_A = 5.0
WEALTH_GRID_A = (1.0, WEALTH_A, 20.0)

# Domanda B: u = sqrt on perfect-square prizes; a two-stage lottery and an urn.
PRIZES = (1, 25, 81)
PRIZE_UTILITIES = tuple(math.isqrt(prize) for prize in PRIZES)
FIRST_STAGE_WEIGHT = Fraction(1, 3)
FIRST_COMPONENT = (Fraction(0), Fraction(1, 4), Fraction(3, 4))
SECOND_COMPONENT = (Fraction(3, 4), Fraction(1, 4), Fraction(0))
URN_BALLS, RED_BALLS, MIN_BLUE_BALLS = 10, 4, 2
COLOR_RED, COLOR_BLUE, COLOR_GREEN = "red", "blue", "green"
BET_T1, BET_T2, BET_T3, BET_T4 = "T1", "T2", "T3", "T4"
BETS = {
    BET_T1: {COLOR_RED},
    BET_T2: {COLOR_BLUE},
    BET_T3: {COLOR_RED, COLOR_GREEN},
    BET_T4: {COLOR_BLUE, COLOR_GREEN},
}

# Domanda C: income changes of a member of a community that shares the losses equally.
LOSS = Fraction(400)
HALF_LOSS = LOSS / 2
LOSS_PROB = Fraction(1, 5)
NO_LOSS = Fraction(0)
ALONE_MEMBERS, COMMUNITY_MEMBERS = 1, 2
# u(x) = sign * (x - anchor)^2 is increasing on the incomes in [-LOSS, 0]: concave with sign -1 and
# anchor above them, convex with sign 1 and anchor at or below them.
CONCAVE_UTILITY = SquareUtility(sign=-1, anchor=Fraction(100))
CONVEX_UTILITY = SquareUtility(sign=1, anchor=-LOSS)
# With one hit among the two members the income is -LOSS / 2; the noise moves it to -LOSS or 0.
NOISY_INCOME = -HALF_LOSS
NOISE_OUTCOMES = (-HALF_LOSS, HALF_LOSS)
NOISE_PROBS = (Fraction(1, 2), Fraction(1, 2))

# Domanda D: ln utility, two types, contract (benefit B, premium p).
WEALTH_D, LOSS_D = 20.0, 8.0
LOW_RISK, HIGH_RISK = 0.1, 0.4
TEST_CONTRACT = (3.0, 0.5)
COVER_SHARES = (0.5, 1.0, 1.5)  # B as a multiple of the loss: partial, full, over-cover

# Domanda E: only the initial wealth W can be invested, while w0 = W (1 + r) is larger, so the
# cap alpha <= W is not implied by alpha <= w0 and has to be checked on its own.
RISKY_NET_RETURNS = (Fraction(-3, 10), Fraction(1))
RISK_FREE_RATE = Fraction(1, 10)
EXCESS_RETURNS = tuple(net - RISK_FREE_RATE for net in RISKY_NET_RETURNS)
EXCESS_LOSS, EXCESS_GAIN = EXCESS_RETURNS
RETURN_PROBS = (Fraction(1, 2), Fraction(1, 2))
WEALTH_GRID_E = (100.0, 200.0)  # initial wealth W
INVERSE_WEALTH = crra_utility(2.0)  # u(c) = -1/c
BASE_WEALTH_H = 10.0
Y_GRID_H = (-4.0, 0.0, 3.0)
GAMMA_GRID = (0.5, 1.0, 2.0)
CONDITION_WEALTH = 8.0  # a power of 2: for ln, RR = 1 and RP = 2 come out exactly, with no rounding
RELATIVE_AVERSION_BOUND, RELATIVE_PRUDENCE_BOUND = 1, 2


def cara_lottery() -> Outcomes:
    """Return the zero-mean lottery of A in euros, as arrays of values and probabilities."""
    steps, probs = float_outcomes(LOTTERY_STEPS, LOTTERY_PROBS)
    return steps * LN_BASE, probs


def premium_from_definition(rate: float, wealth: float, lottery: Outcomes) -> float:
    """Return w - CE for a CARA agent, inverting u(CE) = E[u(w + X)] numerically."""
    level = cara_utility(rate).level
    return wealth + math.log(-rate * expected_utility(level, wealth, lottery)) / rate


def exponential_mean() -> Fraction:
    """Return E[exp(-rate X)] exactly: with X in multiples of ln 2 every exponential is 2^n."""
    exponents = [-CARA_RATE * step for step in LOTTERY_STEPS]
    check(all(power.denominator == 1 for power in exponents), "rate * step must be an integer")
    base = Fraction(LOTTERY_BASE)
    return expect([base ** int(exponent) for exponent in exponents], LOTTERY_PROBS)


def a1_arrow_pratt() -> list[str]:
    """A.1: A(W) is the rate, RR(W) grows with W."""
    cara = cara_utility(CARA_RATE)
    relative = [wealth * absolute_aversion(cara, wealth) for wealth in WEALTH_GRID_A]
    for wealth, value in zip(WEALTH_GRID_A, relative, strict=True):
        check(close(absolute_aversion(cara, wealth), CARA_RATE), "A(W) must equal the rate")
        check(close(value, CARA_RATE * wealth), "RR(W) must equal rate * W")
    check(not close(max(relative), min(relative)), "RR must not be constant")
    return [f"A.1  A(W) = {CARA_RATE}, RR(W) = {CARA_RATE} W (not constant): CARA, not CRRA"]


def a2_certain_equivalent() -> list[str]:
    """A.2: closed-form premium and certain equivalent of the zero-mean lottery."""
    lottery = cara_lottery()
    values, probs = lottery
    check(close(float(np.dot(probs, values)), 0.0), "the lottery must have zero mean")
    mean = exponential_mean()
    premium = math.log(mean) / CARA_RATE
    check(close(premium_from_definition(CARA_RATE, WEALTH_A, lottery), premium), "premium mismatch")
    return [
        f"A.2  E[exp(-rate X)] = {mean}, R = ln({mean}) / {CARA_RATE} = {premium:.4f}, "
        f"CE(w = {WEALTH_A:g}) = {WEALTH_A - premium:.4f}"
    ]


def a3_wealth_effect() -> list[str]:
    """A.3: P, A' and the premium across wealth."""
    cara, lottery = cara_utility(CARA_RATE), cara_lottery()
    aversion, prudence_value = absolute_aversion(cara, WEALTH_A), prudence(cara, WEALTH_A)
    identity = aversion * (aversion - prudence_value)
    slope = finite_derivative(lambda wealth: absolute_aversion(cara, wealth), WEALTH_A, 1)
    check(close(slope, identity), "identity A' = A (A - P) fails")
    check(close(slope, 0.0), "A' must vanish for CARA")
    premiums = [premium_from_definition(CARA_RATE, wealth, lottery) for wealth in WEALTH_GRID_A]
    check(all(close(premium, premiums[0]) for premium in premiums), "premium must not depend on w")
    return [
        f"A.3  P(W) = {prudence_value:g}, A(A - P) = {identity:g} = A'(W); "
        f"premium at w = {', '.join(f'{wealth:g}' for wealth in WEALTH_GRID_A)}: "
        f"{', '.join(f'{premium:.4f}' for premium in premiums)}"
    ]


def a4_small_lottery_expansion() -> list[str]:
    """A.4: R''(0) = A(w) E[X^2] for the premium R(k) of kX, the limit behind (3) => (2)."""
    cara = cara_utility(CARA_RATE)
    values, probs = cara_lottery()
    second_moment = float(np.dot(probs, values**2))
    expected = absolute_aversion(cara, WEALTH_A) * second_moment
    # R(k) is smooth through k = 0 for CARA, so the central stencil may use negative scales.
    numerical = finite_derivative(
        lambda scale: premium_from_definition(CARA_RATE, WEALTH_A, (scale * values, probs)), 0.0, 2
    )
    check(close(numerical, expected), "R''(0) must equal A(w) E[X^2]")
    return [
        f"A.4  E[X^2] = {second_moment:.4f}, R''(0) = A E[X^2] = {expected:.4f} "
        f"(numerical {numerical:.4f}), so R(k) = {expected / 2:.4f} k^2 + o(k^2)"
    ]


def mix(weight: Fraction, first: tuple, second: tuple) -> tuple:
    """Return weight * first + (1 - weight) * second, element by element."""
    return tuple(
        weight * first_item + (1 - weight) * second_item
        for first_item, second_item in zip(first, second, strict=True)
    )


def b1_b2_two_stage_lottery() -> list[str]:
    """B.1: reduction and mean; B.2: expected utility, CE and premium E - CE."""
    reduced = mix(FIRST_STAGE_WEIGHT, FIRST_COMPONENT, SECOND_COMPONENT)
    check(sum(reduced) == 1, "reduced probabilities must sum to 1")
    mean = expect(PRIZES, reduced)
    first_mean, second_mean = (expect(PRIZES, part) for part in (FIRST_COMPONENT, SECOND_COMPONENT))
    check(mean == mix(FIRST_STAGE_WEIGHT, (first_mean,), (second_mean,))[0], "E must be linear")
    squares = zip(PRIZE_UTILITIES, PRIZES, strict=True)
    check(all(root * root == prize for root, prize in squares), "prizes must be perfect squares")
    mean_utility = expect(PRIZE_UTILITIES, reduced)
    return [
        f"B.1  reduced {vector(reduced)}, E = {fmt(mean)} (parts {first_mean}, {second_mean})",
        f"B.2  E[u] = {fmt(mean_utility)}, CE = {fmt(mean_utility**2)}, "
        f"R = E - CE = {fmt(mean - mean_utility**2)}",
    ]


def bet_utility(event: set[str], blue: Fraction) -> Fraction:
    """Return E[u] of a bet paying the top prize if the colour is in ``event``, else the lowest."""
    unknown = Fraction(URN_BALLS - RED_BALLS, URN_BALLS)
    shares = {
        COLOR_RED: Fraction(RED_BALLS, URN_BALLS),
        COLOR_BLUE: blue,
        COLOR_GREEN: unknown - blue,
    }
    low, _, high = PRIZE_UTILITIES
    return low + (high - low) * sum(shares[color] for color in event)


def preference_margins(blue: Fraction) -> tuple[Fraction, Fraction]:
    """Return the expected-utility margins U(T1) - U(T2) and U(T4) - U(T3) at a given blue share."""
    return (
        bet_utility(BETS[BET_T1], blue) - bet_utility(BETS[BET_T2], blue),
        bet_utility(BETS[BET_T4], blue) - bet_utility(BETS[BET_T3], blue),
    )


def b3_b4_ambiguity() -> list[str]:
    """B.3: max-min utilities of the four bets; B.4: no subjective blue share explains both."""
    # E[u] is linear in the blue share, so its minimum is at an end of the admissible range.
    blue_range = (Fraction(MIN_BLUE_BALLS, URN_BALLS), Fraction(URN_BALLS - RED_BALLS, URN_BALLS))
    worst = {
        name: min(bet_utility(event, blue) for blue in blue_range) for name, event in BETS.items()
    }
    explained = worst[BET_T1] > worst[BET_T2] and worst[BET_T4] > worst[BET_T3]
    check(explained, "max-min must explain T1 > T2 and T4 > T3")
    red = Fraction(RED_BALLS, URN_BALLS)
    check(preference_margins(red) == (0, 0), "both choices must be ties at P(blue) = P(red)")
    grid = [Fraction(count, URN_BALLS) for count in range(URN_BALLS - RED_BALLS + 1)]
    margins = map(preference_margins, grid)
    both = any(t1_over_t2 > 0 and t4_over_t3 > 0 for t1_over_t2, t4_over_t3 in margins)
    check(not both, "a share does both")
    return [
        "B.3  U_min: " + ", ".join(f"{name} = {fmt(value)}" for name, value in worst.items()),
        f"B.4  T1 > T2 needs P(blue) < {red}, T4 > T3 needs P(blue) > {red}: no share does both",
    ]


def one_exposed(members: int) -> Distribution:
    """Income change of a member when only one agent can be hit and the loss is shared equally."""
    return {-LOSS / members: LOSS_PROB, NO_LOSS: 1 - LOSS_PROB}


def independent_shocks(members: int) -> Distribution:
    """Income change of a member when each agent is hit independently and losses are shared."""
    return {
        -LOSS * hits / members: math.comb(members, hits)
        * LOSS_PROB**hits
        * (1 - LOSS_PROB) ** (members - hits)
        for hits in range(members + 1)
    }


def cdf(distribution: Distribution, point: Fraction) -> Fraction:
    """Return P(X <= point) for a discrete distribution."""
    return sum((prob for value, prob in distribution.items() if value <= point), Fraction(0))


def dominates(better: Distribution, worse: Distribution) -> bool:
    """Return whether ``better`` first-order dominates ``worse`` (c.d.f. never above)."""
    return all(cdf(better, point) <= cdf(worse, point) for point in set(better) | set(worse))


def mean_of(distribution: Distribution) -> Fraction:
    """Return the expected value of a discrete distribution."""
    return expect(list(distribution), list(distribution.values()))


def cdf_text(named: dict[str, Distribution]) -> str:
    """Format the c.d.f.s of the named distributions on the union of their supports."""
    points = sorted({value for distribution in named.values() for value in distribution})
    columns = (
        f"{name} {vector([cdf(distribution, point) for point in points])}"
        for name, distribution in named.items()
    )
    return f"c.d.f. at {vector(points)}: {', '.join(columns)}"


def expected_square(distribution: Distribution, utility: SquareUtility) -> Fraction:
    """Return E[u(X)] for a square utility."""
    squares = (
        prob * utility.sign * (value - utility.anchor) ** 2 for value, prob in distribution.items()
    )
    return sum(squares, Fraction(0))


def square_label(utility: SquareUtility) -> str:
    """Return the printed form of ``utility``: ``u = -(x - 100)^2`` or ``u = (x + 400)^2``."""
    sign = "-" if utility.sign < 0 else ""
    offset = "-" if utility.anchor > 0 else "+"
    return f"u = {sign}(x {offset} {abs(utility.anchor)})^2"


def utility_by_members(
    by_members: dict[int, Distribution], utility: SquareUtility
) -> dict[int, Fraction]:
    """Return E[u(X)] of a square utility for each community size of ``by_members``."""
    return {
        members: expected_square(distribution, utility)
        for members, distribution in by_members.items()
    }


def c1_c2_first_order() -> list[str]:
    """C.1 and C.2: the community dominates for the exposed agent, staying alone for the other."""
    alone, community = one_exposed(ALONE_MEMBERS), one_exposed(COMMUNITY_MEMBERS)
    safe = {NO_LOSS: Fraction(1)}
    check(dominates(community, alone) and not dominates(alone, community), "C.1: community wins")
    check(dominates(safe, community) and not dominates(community, safe), "C.2: staying alone wins")
    return [
        "C.1  " + cdf_text({"alone": alone, "community": community}),
        "C.2  " + cdf_text({"alone": safe, "community": community}),
    ]


def add_noise(base: Distribution, noise: dict[Fraction, Distribution]) -> Distribution:
    """Return the law of X + e, with e drawn from ``noise[x]`` given X = x (no noise if absent)."""
    result: Distribution = defaultdict(Fraction)
    for value, prob in base.items():
        for shock, shock_prob in noise.get(value, {NO_LOSS: Fraction(1)}).items():
            result[value + shock] += prob * shock_prob
    return dict(result)


def c3_c4_independent_shocks() -> list[str]:
    """C.3: equal means, crossing c.d.f.s, disagreeing utilities; C.4: N = 1 is N = 2 plus noise."""
    by_members = {
        members: independent_shocks(members) for members in (ALONE_MEMBERS, COMMUNITY_MEMBERS)
    }
    single, pair = by_members[ALONE_MEMBERS], by_members[COMMUNITY_MEMBERS]
    check(mean_of(single) == mean_of(pair), "the means must coincide")
    check(not dominates(single, pair) and not dominates(pair, single), "the c.d.f.s must cross")
    concave = utility_by_members(by_members, CONCAVE_UTILITY)
    convex = utility_by_members(by_members, CONVEX_UTILITY)
    check(concave[COMMUNITY_MEMBERS] > concave[ALONE_MEMBERS], "the concave u must prefer N = 2")
    check(convex[ALONE_MEMBERS] > convex[COMMUNITY_MEMBERS], "the convex u must prefer N = 1")
    noise = {NOISY_INCOME: dict(zip(NOISE_OUTCOMES, NOISE_PROBS, strict=True))}
    check(all(mean_of(shocks) == 0 for shocks in noise.values()), "noise must have zero mean")
    spread = add_noise(pair, noise)
    check(spread == single, "N = 2 plus noise must reproduce N = 1")
    named = {f"N={members}": distribution for members, distribution in by_members.items()}
    return [
        f"C.3  E = {fmt(mean_of(single))} for both; " + cdf_text(named),
        f"C.3  E[u] for N=1, N=2: {square_label(CONCAVE_UTILITY)} gives "
        f"{vector(concave.values())}; {square_label(CONVEX_UTILITY)} gives "
        f"{vector(convex.values())}",
        f"C.4  N=2 plus a noise of mean zero at {NOISY_INCOME} "
        f"(to {-LOSS} or {NO_LOSS}) gives N=1: "
        f"{', '.join(f'P({value}) = {prob}' for value, prob in sorted(spread.items()))}",
    ]


def marginal_utilities(benefit: float, premium: float) -> tuple[float, float]:
    """Return u' of the ln consumer in the loss state and in the no-loss state."""
    return LOG.first(WEALTH_D - premium - LOSS_D + benefit), LOG.first(WEALTH_D - premium)


def contract_utility(benefit: float, premium: float, risk: float) -> float:
    """Return EU(B, p; pi) of the ln consumer."""
    loss_wealth = WEALTH_D - premium - LOSS_D + benefit
    return risk * LOG.level(loss_wealth) + (1 - risk) * LOG.level(WEALTH_D - premium)


def indifference_slope(benefit: float, premium: float, risk: float) -> float:
    """Return s = pi a / (pi a + (1 - pi) b), with a, b the marginal utilities of the two states."""
    in_loss, no_loss = marginal_utilities(benefit, premium)
    return risk * in_loss / (risk * in_loss + (1 - risk) * no_loss)


def d1_d2_single_crossing() -> list[str]:
    """D.1: slope of the indifference curve and ds/dpi; D.2: slope against the zero-profit line."""
    benefit, premium = TEST_CONTRACT
    gain = finite_derivative(lambda cover: contract_utility(cover, premium, HIGH_RISK), benefit, 1)
    cost = finite_derivative(lambda price: contract_utility(benefit, price, HIGH_RISK), premium, 1)
    check(close(-gain / cost, indifference_slope(benefit, premium, HIGH_RISK)), "slope mismatch")
    in_loss, no_loss = marginal_utilities(benefit, premium)
    closed = in_loss * no_loss / (HIGH_RISK * in_loss + (1 - HIGH_RISK) * no_loss) ** 2
    numerical = finite_derivative(
        lambda risk: indifference_slope(benefit, premium, risk), HIGH_RISK, 1
    )
    check(close(numerical, closed) and closed > 0, "ds/dpi mismatch or not positive")
    benefits = [share * LOSS_D for share in COVER_SHARES]
    under_cover, full, over = (
        indifference_slope(cover, HIGH_RISK * cover, HIGH_RISK) for cover in benefits
    )
    check(under_cover > HIGH_RISK and close(full, HIGH_RISK) and over < HIGH_RISK, "slope order")
    slope_low, slope_high = (
        indifference_slope(benefit, premium, risk) for risk in (LOW_RISK, HIGH_RISK)
    )
    return [
        f"D.1  at (B, p) = {TEST_CONTRACT}: s_l = {slope_low:.4f}, s_h = {slope_high:.4f}; "
        f"ds/dpi = {closed:.4f} (numerical {numerical:.4f})",
        f"D.2  line slope pi_h = {HIGH_RISK}; indifference slope at "
        f"B = {benefits[0]:g}: {under_cover:.4f}, B = {benefits[1]:g}: {full:.4f}, "
        f"B = {benefits[2]:g}: {over:.4f}",
    ]


def closed_form_shares() -> tuple[Fraction, Fraction]:
    """Return alpha*/w0 for ln and for -1/c, solving the first-order condition by hand."""
    prob_loss, prob_gain = RETURN_PROBS
    log_share = -expect(EXCESS_RETURNS, RETURN_PROBS) / (EXCESS_LOSS * EXCESS_GAIN)
    ratio = prob_loss * -EXCESS_LOSS / (prob_gain * EXCESS_GAIN)  # squared ratio of the two wealths
    root = Fraction(math.isqrt(ratio.numerator), math.isqrt(ratio.denominator))
    check(root * root == ratio, "the data must make the FOC of -1/c solvable with an exact root")
    return log_share, (1 - root) / (root * EXCESS_GAIN - EXCESS_LOSS)


def tabulate(figures: Iterable[tuple[Utility, str]]) -> str:
    """Format one figure per utility as ``name figure`` for the printed lines."""
    return ", ".join(f"{utility.name} {figure}" for utility, figure in figures)


def e1_portfolio() -> list[str]:
    """E.1: alpha* as a multiple of w0 and of W for ln and -1/c, checked against the numerics."""
    growth = 1 + RISK_FREE_RATE
    log_share, inverse_share = closed_form_shares()
    check(inverse_share < log_share, "the more averse agent must invest less")
    shares = ((LOG, log_share), (INVERSE_WEALTH, inverse_share))
    check(all(share * growth < 1 for _, share in shares), "alpha* must stay below W")
    outcomes = float_outcomes(EXCESS_RETURNS, RETURN_PROBS)
    lines = [
        "E.1  alpha*/w0: " + tabulate((utility, fmt(share)) for utility, share in shares),
        "E.1  alpha*/W: " + tabulate((utility, fmt(share * growth)) for utility, share in shares),
    ]
    for initial in WEALTH_GRID_E:
        w0 = initial * float(growth)
        for utility, share in shares:
            # optimal_alpha caps at w0, above W: it still returns the interior root, which the
            # check on alpha*/W above shows to be feasible.
            optimum = optimal_alpha(utility.first, w0, outcomes)
            check(close(optimum, float(share) * w0), f"alpha* mismatch for {utility.name}")
        more_averse = absolute_aversion(INVERSE_WEALTH, w0) > absolute_aversion(LOG, w0)
        check(more_averse, "the -1/c agent must have the larger A")
        check(close(INVERSE_WEALTH.level(w0), -math.exp(-LOG.level(w0))), "u2 = phi(u1)")
        amounts = tabulate((utility, f"{float(share) * w0:.2f}") for utility, share in shares)
        lines.append(f"E.1  W = {initial:g} (w0 = {w0:g}): {amounts}")
    return lines


def h_value(utility: Utility, base: float, shift: float) -> float:
    """Return h(y) = y u'(w0 + y) at y = ``shift``."""
    return shift * utility.first(base + shift)


def h_second_derivative(utility: Utility, base: float, shift: float) -> float:
    """Return h''(y) = -u''(w0 + y) [RP - 2 - w0 P] at y = ``shift``, RP and P at w0 + y."""
    wealth = base + shift
    prudence_value = prudence(utility, wealth)
    bracket = wealth * prudence_value - RELATIVE_PRUDENCE_BOUND - base * prudence_value
    return -utility.second(wealth) * bracket


def crra_condition_row(gamma: float) -> str:
    """Check RR < 1, P > 0, RP < 2 for the CRRA utility with ``gamma`` and describe the result."""
    utility = crra_utility(gamma)
    relative_aversion = CONDITION_WEALTH * absolute_aversion(utility, CONDITION_WEALTH)
    absolute_prudence = prudence(utility, CONDITION_WEALTH)
    relative_prudence = CONDITION_WEALTH * absolute_prudence
    holds = (
        relative_aversion < RELATIVE_AVERSION_BOUND
        and absolute_prudence > 0
        and relative_prudence < RELATIVE_PRUDENCE_BOUND
    )
    check(holds == (gamma < RELATIVE_AVERSION_BOUND), "the conditions must hold iff gamma < 1")
    return (
        f"gamma = {gamma:g}: RR = {relative_aversion:g}, RP = {relative_prudence:g}, "
        f"all three: {holds}"
    )


def e2_concavity() -> list[str]:
    """E.2: the h'' formula, which CRRA utilities meet the three conditions, and the logarithm."""
    for gamma in GAMMA_GRID:
        utility = crra_utility(gamma)
        for shift in Y_GRID_H:
            numerical = finite_derivative(partial(h_value, utility, BASE_WEALTH_H), shift, 2)
            closed = h_second_derivative(utility, BASE_WEALTH_H, shift)
            check(close(numerical, closed), f"h'' formula fails for {utility.name} at y = {shift}")
    for shift in Y_GRID_H:
        slope = finite_derivative(partial(h_value, LOG, BASE_WEALTH_H), shift, 1)
        slope_ln = BASE_WEALTH_H / (BASE_WEALTH_H + shift) ** 2
        check(close(slope, slope_ln) and slope > 0, "h' for ln")
        check(h_second_derivative(LOG, BASE_WEALTH_H, shift) < 0, "h'' for ln must be negative")
    return ["E.2  " + "; ".join(crra_condition_row(gamma) for gamma in GAMMA_GRID)]


SECTIONS = (
    a1_arrow_pratt,
    a2_certain_equivalent,
    a3_wealth_effect,
    a4_small_lottery_expansion,
    b1_b2_two_stage_lottery,
    b3_b4_ambiguity,
    c1_c2_first_order,
    c3_c4_independent_shocks,
    d1_d2_single_crossing,
    e1_portfolio,
    e2_concavity,
)


def main() -> None:
    """Run every section and print its figures."""
    for section in SECTIONS:
        print("\n".join(section()))


if __name__ == "__main__":
    main()
