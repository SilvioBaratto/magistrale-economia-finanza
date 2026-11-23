"""Numbers of the simulated appello 04 of Economia del Rischio e delle Assicurazioni.

Run from the root: ``python latex/esami/economia-rischio-assicurazioni/calc/appello_04.py``.
Every section returns the lines with the values that the solutions quote and checks the closed
forms against exact or numerical computation; ``main`` prints them. A change of data is made here
and the output is copied again.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence
from fractions import Fraction
from itertools import accumulate, pairwise, product

import numpy as np
from scipy.optimize import brentq

from comune import (
    SQRT,
    Probabilities,
    Utility,
    absolute_aversion,
    check,
    check_derivatives,
    close,
    covariance,
    expect,
    expected_slope,
    finite_derivative,
    float_outcomes,
    fmt,
    optimal_alpha,
    prudence,
    vector,
)

Values = Sequence[Fraction]

# Section A: quadratic utility u(W) = W - W^2 / (2 CEILING), increasing only below CEILING.
CEILING = Fraction(100)
STAKE = Fraction(12)
WEALTH_LOW = Fraction(65)
WEALTH_HIGH = Fraction(84)
PROBE_WEALTH = 50.0
QUADRATIC = Utility(
    "quadratic",
    lambda w: w - w**2 / (2 * CEILING),
    lambda w: 1 - w / CEILING,
    lambda w: -1 / CEILING,
    lambda w: 0 * w,
)

# Section B, pooling: u = ln, so the thresholds are ratios of logs of powers of QUOTIENT_BASE.
POOL_WEALTH = Fraction(18)
POOL_LOSS = Fraction(10)
QUOTIENT_BASE = Fraction(3, 2)
LOW_PRICE = Fraction(6)
RISK_MIN = Fraction(2, 5)
RISK_MAX = Fraction(4, 5)

# Section B, screening: two types, and the low-risk contract (coverage, premium) given in the text.
SCREEN_WEALTH = Fraction(27)
SCREEN_LOSS = Fraction(24)
LOW_RISK = Fraction(1, 4)
HIGH_RISK = Fraction(1, 2)
LOW_COVERAGE = Fraction(8)
LOW_PREMIUM = Fraction(2)

# Section C, first pair: lotteries on three prizes in euro, and the cap of the concave utility
# min(x, cap), taken at the middle prize so that its expectation is a hand-sized integral.
PRIZES = (Fraction(10), Fraction(50), Fraction(90))
MIDDLE_PRIZE = 1
CAP = PRIZES[MIDDLE_PRIZE]
LOTTERY_P = (Fraction(1, 8), Fraction(6, 8), Fraction(1, 8))
LOTTERY_Q = (Fraction(3, 8), Fraction(1, 8), Fraction(4, 8))

# Section C, second pair: excess returns, RISKIER is SAFER plus noise added at the middle return.
RETURNS = (Fraction(-60, 100), Fraction(20, 100), Fraction(60, 100))
SAFER = (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4))
RISKIER = (Fraction(3, 8), Fraction(1, 8), Fraction(4, 8))
MIDDLE_RETURN = 1
NOISE_SIZES = (Fraction(-80, 100), Fraction(0), Fraction(40, 100))
NOISE_PROBS = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
INVESTOR_WEALTH = 100.0
INVESTOR_UTILITY = SQRT
# The two optima must differ by at least 15% so that rounding cannot flip the answer.
DECISION_MARGIN = 0.15
# Sufficient conditions of the portfolio theorem (ERA 05): RR < 1, P > 0, RP < 2.
MAX_RELATIVE_AVERSION = 1
MAX_RELATIVE_PRUDENCE = 2
WEALTH_GRID_POINTS = 9

# Section D: moral hazard with u(z) = -1/z, whose inverse is explicit.
INSURED_WEALTH = Fraction(3)
RESERVATION_UTILITY = Fraction(-1, 2)
EFFORT_COST = (Fraction(0), Fraction(1, 10))
LOSSES = (Fraction(0), Fraction(1), Fraction(2))
LOSS_PROBS = (
    (Fraction(5, 10), Fraction(1, 10), Fraction(4, 10)),
    (Fraction(8, 10), Fraction(1, 10), Fraction(1, 10)),
)
LOW_EFFORT, HIGH_EFFORT = 0, 1

# Section E: market value and the value of a title independent of it, four equiprobable states.
MARKET_VALUES = (Fraction(4), Fraction(6))
TITLE_VALUES = (Fraction(1), Fraction(3))
RISK_FREE = Fraction(1)
TIED_SHARE = Fraction(1, 2)


def format_line(label: str, **values: object) -> str:
    """Return ``label`` and the named values, formatted as the solutions quote them."""

    def render(value: object) -> str:
        """Format a sequence with ``vector``, a number with ``fmt``, anything else with ``str``."""
        if isinstance(value, (list, tuple)):
            return vector(value)
        return fmt(value) if isinstance(value, (Fraction, float)) else str(value)

    return f"{label}: " + ", ".join(f"{name}={render(value)}" for name, value in values.items())


def risk_premium(wealth: Fraction) -> tuple[Fraction, Fraction]:
    """Compute certain equivalent and risk premium of the lottery +/- STAKE, exactly.

    The quadratic utility is a constant minus (CEILING - W)^2, so the certain equivalent solves
    (CEILING - CE)^2 = (CEILING - wealth)^2 + STAKE^2, a perfect square for the chosen data.

    Args:
        wealth: Initial certain wealth, below CEILING - STAKE.

    Returns:
        The pair (certain equivalent, premium).
    """
    gap_squared = (CEILING - wealth) ** 2 + STAKE**2
    gap = Fraction(math.isqrt(gap_squared.numerator), math.isqrt(gap_squared.denominator))
    check(gap * gap == gap_squared, "the certain equivalent is not exact")
    equivalent = CEILING - gap
    expected = (QUADRATIC.level(wealth + STAKE) + QUADRATIC.level(wealth - STAKE)) / 2
    check(QUADRATIC.level(equivalent) == expected, "u(CE) differs from E[u(w + X)]")
    return equivalent, wealth - equivalent


def section_a_measures() -> list[str]:
    """A.1 and A.3: the measures of the quadratic utility, none of them constant."""
    check_derivatives(QUADRATIC, PROBE_WEALTH)
    lines = []
    for wealth in (WEALTH_LOW, WEALTH_HIGH):
        aversion = absolute_aversion(QUADRATIC, wealth)
        check(aversion == 1 / (CEILING - wealth), "A(W) closed form")
        lines.append(
            format_line(
                f"W={wealth}", A=aversion, RR=wealth * aversion, P=prudence(QUADRATIC, wealth)
            )
        )
    slope = finite_derivative(lambda w: absolute_aversion(QUADRATIC, w), PROBE_WEALTH, 1)
    check(close(slope, 1 / (CEILING - Fraction(PROBE_WEALTH)) ** 2), "A'(W) = A(W)^2 > 0")
    return lines


def section_a_premiums() -> list[str]:
    """A.2-A.3: certain equivalent and risk premium at the two wealths."""
    lines = []
    premiums = []
    for wealth in (WEALTH_LOW, WEALTH_HIGH):
        equivalent, premium = risk_premium(wealth)
        premiums.append(premium)
        lines.append(format_line(f"W={wealth}", CE=equivalent, R=premium))
    check(all(low < high for low, high in pairwise(premiums)), "premium must grow with wealth")
    return lines


def exponent_of_base(value: Fraction) -> int:
    """Return the integer n such that QUOTIENT_BASE ** n == value, or fail if there is none."""
    exponent = round(math.log(value) / math.log(QUOTIENT_BASE))
    check(QUOTIENT_BASE**exponent == value, f"{value} is not a power of {QUOTIENT_BASE}")
    return exponent


def purchase_threshold(price: Fraction) -> Fraction:
    """Compute h(p) = [ln w - ln(w - p)] / [ln w - ln(w - L)] for the pooling market, exactly.

    Args:
        price: Policy price, such that w / (w - price) is a power of QUOTIENT_BASE.

    Returns:
        The probability of loss above which a consumer buys.
    """
    price_quotient = POOL_WEALTH / (POOL_WEALTH - price)
    loss_quotient = POOL_WEALTH / (POOL_WEALTH - POOL_LOSS)
    threshold = Fraction(exponent_of_base(price_quotient), exponent_of_base(loss_quotient))
    check(close(float(threshold), math.log(price_quotient) / math.log(loss_quotient)), "h(p)")
    return threshold


def section_b_pooling() -> list[str]:
    """B.1-B.2: threshold at a given price, then the conjecture p** on uniform risk."""
    fair_share = LOW_PRICE / POOL_LOSS
    low_price_threshold = purchase_threshold(LOW_PRICE)
    check(
        RISK_MIN <= low_price_threshold < fair_share <= RISK_MAX,
        "buyers whose fair premium is below the price must exist in the support of pi",
    )
    conjectured_price = (RISK_MIN + RISK_MAX) / 2 * POOL_LOSS
    threshold = purchase_threshold(conjectured_price)
    check(threshold == low_price_threshold, "h(p**) must coincide with the threshold of B.1")
    check(RISK_MIN < threshold < RISK_MAX, "selection must be active")
    buyers_mean = (threshold + RISK_MAX) / 2
    profit = conjectured_price - buyers_mean * POOL_LOSS
    check(profit < 0, "p** must not be an equilibrium price")
    buying_share = (RISK_MAX - threshold) / (RISK_MAX - RISK_MIN)
    return [
        format_line("B.1", h=low_price_threshold, p_over_L=fair_share),
        format_line("B.2", p_star2=conjectured_price, share=buying_share),
        format_line("B.2 (cont.)", buyers_mean=buyers_mean, profit=profit),
    ]


def is_indifferent(accident: Fraction, safe: Fraction, risk: Fraction, target: Fraction) -> bool:
    """Return whether risk*ln(accident) + (1-risk)*ln(safe) == ln(target), exactly.

    With risk = a/d the equality is accident^a * safe^(d-a) == target^d.
    """
    numerator, denominator = risk.numerator, risk.denominator
    return accident**numerator * safe ** (denominator - numerator) == target**denominator


def high_risk_utility(coverage: float) -> float:
    """Return the high-risk type's utility with the contract (coverage, LOW_RISK * coverage)."""
    wealth, loss = float(SCREEN_WEALTH), float(SCREEN_LOSS)
    premium = float(LOW_RISK) * coverage
    accident = math.log(wealth - premium - loss + coverage)
    return float(HIGH_RISK) * accident + float(1 - HIGH_RISK) * math.log(wealth - premium)


def section_b_screening() -> list[str]:
    """B.3: high-risk contract and utility, and the check of the given low-risk contract."""
    high_premium = HIGH_RISK * SCREEN_LOSS
    full_cover_wealth = SCREEN_WEALTH - high_premium
    check(LOW_PREMIUM == LOW_RISK * LOW_COVERAGE, "the low-risk contract must lie on p = pi_l B")
    safe = SCREEN_WEALTH - LOW_PREMIUM
    accident = safe - SCREEN_LOSS + LOW_COVERAGE
    check(is_indifferent(accident, safe, HIGH_RISK, full_cover_wealth), "high type not indifferent")
    target = math.log(full_cover_wealth)
    root = brentq(lambda cover: high_risk_utility(cover) - target, 0.0, float(SCREEN_LOSS))
    check(close(root, float(LOW_COVERAGE)), "the given contract must solve the separating system")
    return [
        format_line("B.3", B_h=SCREEN_LOSS, p_h=high_premium, u_h=target),
        format_line("B.3 (cont.)", accident=accident, safe=safe, product=accident * safe),
    ]


def cumulative(probs: Probabilities) -> list[Fraction]:
    """Return the c.d.f. of a lottery at each of its values."""
    return list(accumulate(probs))


def integrated_cdf(values: Values, probs: Probabilities) -> list[Fraction]:
    """Return the integral of the c.d.f. from the lowest value, evaluated at each value."""
    # The last c.d.f. level has no interval to its right, so the two sequences differ by one.
    steps = zip(cumulative(probs), pairwise(values), strict=False)
    return [Fraction(0), *accumulate(level * (high - low) for level, (low, high) in steps)]


def first_order_dominates(better: Probabilities, worse: Probabilities) -> bool:
    """Return whether ``better`` has a c.d.f. nowhere above that of ``worse``."""
    return all(low <= high for low, high in zip(cumulative(better), cumulative(worse), strict=True))


def second_order_dominates(values: Values, better: Probabilities, worse: Probabilities) -> bool:
    """Return whether the integrated c.d.f. of ``better`` is nowhere above that of ``worse``."""
    pairs = zip(integrated_cdf(values, better), integrated_cdf(values, worse), strict=True)
    return all(low <= high for low, high in pairs)


def section_c_first_pair() -> list[str]:
    """C.1-C.2: no dominance of either order, and two concave utilities that disagree."""
    for name, pair in (("p over q", (LOTTERY_P, LOTTERY_Q)), ("q over p", (LOTTERY_Q, LOTTERY_P))):
        check(not first_order_dominates(*pair), f"{name}: first order")
        check(not second_order_dominates(PRIZES, *pair), f"{name}: second order")
    mean_p, mean_q = expect(PRIZES, LOTTERY_P), expect(PRIZES, LOTTERY_Q)
    capped_prizes = [min(prize, CAP) for prize in PRIZES]
    capped_p, capped_q = expect(capped_prizes, LOTTERY_P), expect(capped_prizes, LOTTERY_Q)
    check(mean_q > mean_p and capped_p > capped_q, "the linear and the capped utility disagree")
    for probs, capped_mean in ((LOTTERY_P, capped_p), (LOTTERY_Q, capped_q)):
        integral = integrated_cdf(PRIZES, probs)[MIDDLE_PRIZE]
        check(capped_mean == CAP - integral, "E[min(x, cap)] must be cap minus the c.d.f. integral")
    return [
        format_line("C cdf", p=cumulative(LOTTERY_P), q=cumulative(LOTTERY_Q)),
        format_line(
            "C integrals",
            p=integrated_cdf(PRIZES, LOTTERY_P),
            q=integrated_cdf(PRIZES, LOTTERY_Q),
        ),
        format_line("C.2 E[x]", p=mean_p, q=mean_q),
        format_line(f"C.2 E[min(x, {CAP})]", p=capped_p, q=capped_q),
    ]


def spread_distribution() -> list[Fraction]:
    """Return the probabilities of SAFER plus the noise, added at MIDDLE_RETURN only."""
    mixed = {value: Fraction(0) for value in RETURNS}
    for index, (value, prob) in enumerate(zip(RETURNS, SAFER, strict=True)):
        if index != MIDDLE_RETURN:
            mixed[value] += prob
            continue
        for size, noise_prob in zip(NOISE_SIZES, NOISE_PROBS, strict=True):
            mixed[value + size] += prob * noise_prob
    return list(mixed.values())


def meets_portfolio_conditions(utility: Utility, wealths: Iterable[float]) -> bool:
    """Return whether RR < 1, P > 0 and RP < 2 hold at every wealth, as the ERA 05 theorem needs."""
    return all(
        wealth * absolute_aversion(utility, wealth) < MAX_RELATIVE_AVERSION
        and prudence(utility, wealth) > 0
        and wealth * prudence(utility, wealth) < MAX_RELATIVE_PRUDENCE
        for wealth in wealths
    )


def section_c_noise() -> list[str]:
    """C.3: SAFER plus a mean-zero noise is RISKIER, so SAFER dominates at second order."""
    check(expect(NOISE_SIZES, NOISE_PROBS) == 0, "the noise must have zero conditional mean")
    check(spread_distribution() == list(RISKIER), "SAFER plus the noise must be RISKIER")
    check(expect(RETURNS, SAFER) == expect(RETURNS, RISKIER), "the means must coincide")
    check(second_order_dominates(RETURNS, SAFER, RISKIER), "SAFER must dominate at second order")
    check(not first_order_dominates(SAFER, RISKIER), "equal means exclude first-order dominance")
    return [
        format_line("C.3 mean", F2=expect(RETURNS, SAFER), F1=expect(RETURNS, RISKIER)),
        format_line(
            "C.3 integrals",
            F2=integrated_cdf(RETURNS, SAFER),
            F1=integrated_cdf(RETURNS, RISKIER),
        ),
    ]


def section_c_investor() -> list[str]:
    """C.4: the optimal amounts of the square-root investor in the two titles."""
    safer_outcomes = float_outcomes(RETURNS, SAFER)
    riskier_outcomes = float_outcomes(RETURNS, RISKIER)
    final_wealths = np.linspace(
        INVESTOR_WEALTH * (1 + float(min(RETURNS))),
        INVESTOR_WEALTH * (1 + float(max(RETURNS))),
        WEALTH_GRID_POINTS,
    )
    check(
        meets_portfolio_conditions(INVESTOR_UTILITY, final_wealths),
        "the utility must meet the sufficient conditions on RR, P and RP",
    )
    safer_amount = optimal_alpha(INVESTOR_UTILITY.first, INVESTOR_WEALTH, safer_outcomes)
    riskier_amount = optimal_alpha(INVESTOR_UTILITY.first, INVESTOR_WEALTH, riskier_outcomes)
    check(riskier_amount > 0 and safer_amount < INVESTOR_WEALTH, "the optima must be interior")
    check(safer_amount >= riskier_amount * (1 + DECISION_MARGIN), "the gap must clear the margin")
    slope = expected_slope(INVESTOR_UTILITY.first, INVESTOR_WEALTH, safer_outcomes, riskier_amount)
    check(slope > 0, "the safer title must have a positive slope at the riskier optimum")
    return [
        format_line("C.4 alpha*", F2=safer_amount, F1=riskier_amount),
        format_line("C.4 slope of V2 at alpha*(F1)", slope=slope),
    ]


def full_cover_premium(effort: int) -> Fraction:
    """Return p(e) = w - u^-1(d(e) + u_bar), with u^-1(v) = -1/v: participation binds."""
    return INSURED_WEALTH + 1 / (EFFORT_COST[effort] + RESERVATION_UTILITY)


def insured_utility(wealth: Fraction) -> Fraction:
    """Return u(z) = -1/z, the utility of the moral-hazard example."""
    return -1 / wealth


def expected_loss(effort: int) -> Fraction:
    """Return the expected loss when the client exerts ``effort``."""
    return expect(LOSSES, LOSS_PROBS[effort])


def section_d_moral_hazard() -> list[str]:
    """D.1-D.2: benchmark premia and profits, and the deviation to low effort."""
    efforts = (LOW_EFFORT, HIGH_EFFORT)
    premium_e0, premium_e1 = (full_cover_premium(effort) for effort in efforts)
    check(premium_e0 > premium_e1, "p(0) must exceed p(1)")
    loss_e0, loss_e1 = (expected_loss(effort) for effort in efforts)
    profit_e0, profit_e1 = premium_e0 - loss_e0, premium_e1 - loss_e1
    check(profit_e1 > profit_e0 > 0, "e* must be 1, with positive profits")
    for effort in efforts:
        no_policy = [insured_utility(INSURED_WEALTH - loss) for loss in LOSSES]
        uninsured = expect(no_policy, LOSS_PROBS[effort]) - EFFORT_COST[effort]
        check(uninsured <= RESERVATION_UTILITY, "u_bar must not be below the uninsured utility")
    certain_wealth = INSURED_WEALTH - premium_e1
    utility_e0, utility_e1 = (insured_utility(certain_wealth) - cost for cost in EFFORT_COST)
    check(utility_e0 > utility_e1, "the client must prefer low effort")
    actual_profit = premium_e1 - loss_e0
    check(actual_profit < profit_e1, "the company must earn less than the first best")
    return [
        format_line("D.1", p0=premium_e0, p1=premium_e1),
        format_line(
            "D.1 (cont.)", loss0=loss_e0, loss1=loss_e1, profit0=profit_e0, profit1=profit_e1
        ),
        format_line("D.2", wealth=certain_wealth, utility_e0=utility_e0, utility_e1=utility_e1),
        format_line("D.2 (cont.)", actual_profit=actual_profit, first_best=profit_e1),
    ]


def title_premium(market: Values, title: Values) -> tuple[Fraction, Fraction]:
    """Compute price and equilibrium premium E[R_i] - R_f of a title, with u = ln.

    Args:
        market: Value of the market portfolio in each of the equiprobable states.
        title: Value of the title in the same states.

    Returns:
        The pair (price P_i, premium).
    """
    marginal = [1 / value for value in market]
    kernel = [value / expect(marginal) for value in marginal]
    price = (
        expect([payoff * weight for payoff, weight in zip(title, kernel, strict=True)]) / RISK_FREE
    )
    gross = [value / price for value in title]
    pricing = expect([ret * weight for ret, weight in zip(gross, kernel, strict=True)])
    check(expect(kernel) == 1 and pricing == RISK_FREE, "E[M] = 1 and E[R_i M] = R_f")
    premium = expect(gross) - RISK_FREE
    check(premium == -covariance(gross, kernel), "premium = -Cov(R_i, M)")
    return price, premium


def section_e_prices() -> list[str]:
    """E.2: the premium vanishes for a title independent of the market, not for one tied to it."""
    check(min(MARKET_VALUES) >= max(TITLE_VALUES), "the other titles must pay a non-negative sum")
    market, title = zip(*product(MARKET_VALUES, TITLE_VALUES), strict=True)
    independent_price, independent_premium = title_premium(market, title)
    tied_price, tied_premium = title_premium(market, [value * TIED_SHARE for value in market])
    check(independent_premium == 0 < tied_premium, "only the independent title has no premium")
    return [
        format_line("E.2 independent title", P_i=independent_price, premium=independent_premium),
        format_line(f"E.2 {TIED_SHARE} of the market", P_i=tied_price, premium=tied_premium),
    ]


def main() -> None:
    """Print every section of the appello; the only place that writes to stdout."""
    report = []
    for section in (
        section_a_measures,
        section_a_premiums,
        section_b_pooling,
        section_b_screening,
        section_c_first_pair,
        section_c_noise,
        section_c_investor,
        section_d_moral_hazard,
        section_e_prices,
    ):
        report.append(f"--- {section.__name__}")
        report.extend(section())
    print("\n".join(report))


if __name__ == "__main__":
    main()
