#!/usr/bin/env python3
"""Recompute the exercises of the simulated Finanza Strategica exams from the papers themselves.

The data are parsed from ``FSTR_Esame_Simulato_NN.md``, every result is recomputed with exact
fractions and each one must appear, formatted the Italian way, in ``FSTR_Soluzioni_Simulato_NN.md``.
Nothing here reads the generators' ``calc.py``: the point is an independent check of what a
student would see. Exercise 2 (acquisition with synergies) follows the lecturer's convention, in
which the quota alpha scales only the synergy of the discount rate.

Run it with no arguments for every exam, or with exam numbers to restrict it. Exit status 1 when
any recomputed value is missing from the solutions or a data constraint is violated.
"""
from __future__ import annotations

import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
from pathlib import Path

SRC = Path(__file__).resolve().parent / "esami" / "finanza-strategica" / "src"
# Sign of the NPV of Exercise 2 fixed for each exam in the plan.
EXPECTED_NPV_SIGN = {1: -1, 2: 1, 3: 1, 4: -1, 5: 1, 6: -1, 7: 1, 8: -1, 9: 1, 10: -1}
EXERCISE_1 = {4: "wacc", 6: "dcf", 8: "options"}  # every other exam is the multiples exercise


def num(text: str) -> Fraction:
    """Parse an Italian number such as ``- 1.234,5`` into an exact fraction.

    Args:
        text: The number as printed, with ``.`` for thousands and ``,`` for decimals.

    Returns:
        Its exact value; a leading minus sign may be followed by a space.
    """
    clean = text.replace(" ", "").replace("−", "-").replace(".", "").replace(",", ".")
    return Fraction(Decimal(clean))


def pct(text: str) -> Fraction:
    """Parse a percentage such as ``9,70%`` into a fraction of one (0.097)."""
    return num(text.rstrip("%")) / 100


def rounded(value: Fraction, places: int = 2) -> Decimal:
    """Round half up, the way the solutions present their figures."""
    exact = Decimal(value.numerator) / Decimal(value.denominator)
    return exact.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def grab(pattern: str, text: str) -> str:
    """Return the first group of ``pattern`` in ``text``, or stop saying which pattern is missing."""
    m = re.search(pattern, text)
    if not m:
        raise SystemExit(f"pattern not found in the paper: {pattern}")
    return m.group(1)


def italian(value: Fraction, places: int = 2) -> str:
    """Format the absolute value with ``.`` for thousands and ``,`` for decimals."""
    text = f"{abs(rounded(value, places)):,.{places}f}"
    return text.replace(",", "§").replace(".", ",").replace("§", ".")


class Report:
    """Collects the outcome of every check of one exam."""

    def __init__(self, n: int, solutions: str) -> None:
        self.n = n
        # "{,}" is how the solutions write a decimal comma inside formulas.
        self.text = (solutions.replace("{,}", ",").replace("−", "-").replace("\\%", "%")
                     .replace("\\,", "").replace("\\;", ""))
        self.checked = 0
        self.failures: list[str] = []

    def has(self, label: str, value: Fraction, places: int = 2) -> None:
        """Require the value, formatted to ``places`` decimals, to appear in the solutions."""
        self.checked += 1
        shown = italian(value, places)
        if shown not in self.text:
            self.failures.append(f"[{self.n:02d}] {label}: expected {shown} not found in the solutions")

    def require(self, label: str, condition: bool) -> None:
        """Record a data constraint that the exam must satisfy."""
        self.checked += 1
        if not condition:
            self.failures.append(f"[{self.n:02d}] {label}")


def block(paper: str, heading: str) -> str:
    """Return the Markdown of the callout with the given heading."""
    m = re.search(rf'heading="{heading}"\}}\n(.*?)\n:::::', paper, re.S)
    if not m:
        raise SystemExit(f"block {heading!r} not found")
    return m.group(1)


def table_row(text: str, label: str) -> list[Fraction]:
    """Numbers of the first table row starting with ``label``; empty cells are skipped."""
    m = re.search(rf"^\| {re.escape(label)} \|(.*)\|\s*$", text, re.M)
    if not m:
        raise SystemExit(f"table row {label!r} not found")
    return [num(c) for c in (c.strip() for c in m.group(1).split("|")) if c]


def check_exercise_2(r: Report, paper: str) -> None:
    """Recompute the acquisition exercise and require every figure in the solutions."""
    ex = block(paper, "Esercizio 2")
    tables = re.findall(r"\| Impresa ([AB]) \|\n\|---\|\n((?:\|.*\|\n?){3,5})", ex)
    firms = {}
    for name, body in tables:
        values = [num(v) for v in re.findall(r"[=]\s*([\d.]+(?:,\d+)?%?)", body.replace("%", ""))]
        rate = pct(grab(r"unlevered=([\d,]+%)", body))
        firms[name] = {"fcfo": values[0], "assets": values[1], "pfn": values[2], "r": rate}
    a, b = firms["A"], firms["B"]
    tc = pct(grab(r'"tc".*?pari al (\d+%)', ex))
    alpha = pct(grab(r"acquisto del(?:l')? ?(\d+%)", ex))
    price = num(grab(r"pari complessivamente a ([\d.]+)", ex))
    saving = num(grab(r"per A pari a un flusso di ([\d.]+)", ex))
    r_new = pct(grab(r"nuovo complesso pari al ([\d,]+%)", ex))
    new_debt = num(grab(r"nuovo debito in capo ad A pari a ([\d.]+)", ex))
    extra_flow = num(grab(r"flusso operativo pari a ([\d.]+)", ex))
    bp = re.search(r"valore attuale complessivo è pari a ([\d.]+)", ex)
    v_bp = num(bp.group(1)) if bp else Fraction(0)

    stand_alone = (b["assets"] - b["pfn"]) * alpha
    v_flow = saving / r_new
    v_rate = (a["fcfo"] + alpha * b["fcfo"]) / r_new - (a["fcfo"] / a["r"] + alpha * b["fcfo"] / b["r"])
    v_debt = new_debt * tc
    v_inv = extra_flow / r_new - new_debt
    v_syn = v_flow + v_rate + v_debt + v_inv
    npv = -price + stand_alone + v_syn + v_bp

    r.has("Es.2 stand alone value of the quota", stand_alone)
    r.has("Es.2 synergy of cash flow", v_flow)
    r.has("Es.2 synergy of the discount rate", v_rate)
    r.has("Es.2 synergy of debt", v_debt)
    r.has("Es.2 synergy of the extra investment", v_inv)
    r.has("Es.2 total synergies", v_syn)
    r.has("Es.2 NPV", npv)

    sign = EXPECTED_NPV_SIGN[r.n]
    r.require(f"Es.2 NPV sign is {1 if npv > 0 else -1}, the plan requires {sign}", (npv > 0) == (sign > 0))
    r.require("Es.2 the four synergies are positive", min(v_flow, v_rate, v_debt, v_inv) > 0)
    ratio = price / stand_alone
    lo, hi = (Fraction(92, 100), Fraction(102, 100)) if sign > 0 else (Fraction(108, 100), Fraction(118, 100))
    r.require(f"Es.2 price is {float(ratio):.3f} of the stand alone value, expected {float(lo)}-{float(hi)}",
              lo <= ratio <= hi)
    r.require("Es.2 |NPV| is at least 3% of the price", abs(npv) >= price * Fraction(3, 100))
    if sign < 0:
        r.require("Es.2 synergies are 2-8% of the price", Fraction(2, 100) <= v_syn / price <= Fraction(8, 100))
    r.require("Es.2 new debt is 1.5-3% of the assets of A",
              Fraction(15, 1000) <= new_debt / a["assets"] <= Fraction(3, 100))
    r.require("Es.2 the new rate is below the implied stand alone rate",
              r_new < (a["fcfo"] + alpha * b["fcfo"]) / (a["fcfo"] / a["r"] + alpha * b["fcfo"] / b["r"]))


def check_multiples(r: Report, paper: str) -> None:
    """Recompute the multiples exercise: income statement, sector multiple, unlevered average."""
    ex = block(paper, "Esercizio 1")
    sales = table_row(ex, "Ricavi di vendita")[0]
    cogs, staff, dep, fin, tax, net = (abs(table_row(ex, k)[0]) for k in (
        "Costo del venduto", "Costo del personale", "Ammortamenti", "Oneri finanziari (interessi passivi)",
        "Imposte d'esercizio", "Risultato d'esercizio"))
    r.require("Es.1 the income statement does not add up", sales - cogs - staff - dep - fin - tax == net)
    pfn = num(grab(r"PFN di ([\d.]+) €/k", ex))
    tc = pct(grab(r"tax rate per .*? è pari al (\d+%)", ex))
    sector = num(grab(r"Damodaran è pari a (\d+,\d+)", ex))
    ebitda = sales - cogs - staff
    ebit = ebitda - dep
    r.has("Es.1 EBITDA", ebitda, 0)
    r.has("Es.1 EBIT", ebit, 0)
    r.has("Es.1 EV with the sector multiple", sector * sales)
    r.has("Es.1 equity with the sector multiple", sector * sales - pfn)

    rows = re.findall(r"^\| [A-Z][\w' ]+ \| [A-Z]{1,3} \| (\d+%) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", ex, re.M)
    r.require("Es.1 expected six comparables", len(rows) == 6)
    exact, shown = [], []
    for t, ev, s, p in rows:
        unlevered = (num(ev) - num(p) * pct(t)) / num(s)
        exact.append(unlevered)
        shown.append(Fraction(rounded(unlevered)))
        r.has("Es.1 unlevered EV/Sales of a comparable", unlevered)
        r.require("Es.1 each comparable has EV above its PFN and a unlevered multiple in 0.4-2.0",
                  num(ev) > num(p) and Fraction(4, 10) <= unlevered <= 2)
    mean = sum(shown) / 6
    # The papers ask for no more than two decimals, so the solutions round the average too.
    k = Fraction(rounded(mean))
    r.has("Es.1 average unlevered multiple", k)
    r.require("Es.1 averages of rounded and exact multiples agree to two decimals",
              rounded(sum(exact) / 6) == rounded(mean))
    ev_unlevered = k * sales
    ev = ev_unlevered + pfn * tc
    r.has("Es.1 unlevered EV of the target", ev_unlevered)
    r.has("Es.1 EV with the comparables", ev)
    r.has("Es.1 equity with the comparables", ev - pfn)


def check_wacc(r: Report, paper: str) -> None:
    """Recompute the cost of capital exercise: unlevered betas, CAPM, WACC and NPV."""
    ex = block(paper, "Esercizio 1")
    rf = pct(grab(r"privo di rischio è pari al ([\d,]+%)", ex))
    mrp = pct(grab(r"mercato applicabile all'Italia è pari al ([\d,]+%)", ex))
    tc_project = pct(grab(r"fiscale sul progetto sia pari al (\d+%)", ex))
    betas = []
    for t, d, e, beta in re.findall(r"^\| [A-Z]\w+ \| [A-Z]{1,3} \| (\d+%) \| (-?[\d.]+) \| ([\d.]+) \| ([\d,]+) \|", ex, re.M):
        debt, equity, bl = num(d), num(e), num(beta)
        # Net cash has no market risk: the operating assets are the equity minus the cash.
        bu = bl / (1 + debt / equity * (1 - pct(t))) if debt >= 0 else bl * equity / (equity - abs(debt))
        betas.append(bu)
        r.has("Es.1 unlevered beta of a comparable", bu)
    r.require("Es.1 expected three comparables", len(betas) == 3)
    beta_mean = sum(betas) / 3
    r0 = rf + beta_mean * mrp
    r_e = r0 + (r0 - rf) * (1 - tc_project)
    wacc = r_e / 2 + rf / 2 * (1 - tc_project)
    flows = table_row(ex, "FCFO")
    npv = sum(f / (1 + wacc) ** t for t, f in enumerate(flows))
    r.has("Es.1 average unlevered beta", beta_mean)
    r.has("Es.1 unlevered cost of capital (%)", r0 * 100)
    r.has("Es.1 cost of equity at 50% debt (%)", r_e * 100)
    r.has("Es.1 WACC (%)", wacc * 100)
    r.has("Es.1 NPV at the WACC", npv)


def check_dcf(r: Report, paper: str) -> None:
    """Recompute the DCF exercise: steady state APV and analytic APV with terminal value."""
    ex = block(paper, "Esercizio 1")
    sales = table_row(ex, "Ricavi di vendita")[0]
    cogs, staff, dep, fin = (abs(table_row(ex, k)[0]) for k in (
        "Costo del venduto", "Costo del personale", "Ammortamenti", "Oneri finanziari (interessi passivi)"))
    pfn = num(grab(r"PFN di ([\d.]+) €/k", ex))
    tc = pct(grab(r"deducibilità degli interessi, è pari al (\d+%)", ex))
    rf = pct(grab(r"privo di rischio è pari al ([\d,]+%)", ex))
    beta = num(grab(r"pari a ([\d,]+) e il premio", ex))
    mrp = pct(grab(r"mercato è pari al ([\d,]+%)", ex))
    ebit = sales - cogs - staff - dep
    nopat = ebit * (1 - tc)
    r0 = rf + beta * mrp
    r.has("Es.1 EBIT", ebit, 0)
    r.has("Es.1 NOPAT", nopat, 0)
    r.has("Es.1 unlevered cost of capital (%)", r0 * 100)
    ev_steady = nopat / r0 + pfn * tc
    r.has("Es.1 steady state EV", ev_steady)
    r.has("Es.1 steady state equity", ev_steady - pfn)

    fcfo = table_row(ex, "FCFO")
    interest = table_row(ex, "- Oneri finanziari")
    shields = table_row(ex, "+ Scudi fiscali")
    d_pfn = table_row(ex, "Var. PFN")
    nopat_last = num(grab(r"NOPAT dell'ultimo anno di previsione, di ([\d.]+)", ex))
    rd = fin / pfn
    n = len(fcfo)
    v_u = sum(f / (1 + r0) ** (t + 1) for t, f in enumerate(fcfo))
    v_ts = sum(s / (1 + rd) ** (t + 1) for t, s in enumerate(shields))
    tv_u = nopat_last / r0 / (1 + r0) ** n
    debt_last = pfn + sum(d_pfn)
    tv_ts = debt_last * tc / (1 + rd) ** n
    ev = v_u + v_ts + tv_u + tv_ts
    r.require("Es.1 the tax shields of the plan equal interest times the tax rate",
              all(i * tc == s for i, s in zip(interest, shields)))
    r.has("Es.1 explicit period unlevered value", v_u)
    r.has("Es.1 explicit period tax shield value", v_ts)
    r.has("Es.1 unlevered terminal value", tv_u)
    r.has("Es.1 tax shield terminal value", tv_ts)
    r.has("Es.1 analytic EV", ev)
    r.has("Es.1 analytic equity", ev - pfn)
    r.has("Es.1 terminal value weight (%)", (tv_u + tv_ts) / ev * 100, 1)


def check_options(r: Report, paper: str) -> None:
    """Recompute the real options exercise: NPV per scenario, average and abandonment option."""
    ex = block(paper, "Esercizio 1")
    rate = pct(grab(r"attualizzazione del progetto è pari all'(\d+%)", ex))
    recovery = pct(grab(r"recuperando il (\d+%)", ex))
    optimistic, pessimistic = (table_row(t, "FCFO") for t in re.findall(
        r"\| FLUSSI .*?\n(?:\|.*\n)+", ex))
    npv = lambda flows: sum(f / (1 + rate) ** t for t, f in enumerate(flows))
    npv_opt, npv_pess = npv(optimistic), npv(pessimistic)
    initial = -pessimistic[0]
    npv_pess_abandon = -initial + (pessimistic[1] + recovery * initial) / (1 + rate)
    r.has("Es.1 optimistic NPV", npv_opt)
    r.has("Es.1 pessimistic NPV", npv_pess)
    r.has("Es.1 average NPV", (npv_opt + npv_pess) / 2)
    r.has("Es.1 pessimistic NPV with abandonment", npv_pess_abandon)
    r.has("Es.1 average NPV with the option", (npv_opt + npv_pess_abandon) / 2)
    r.has("Es.1 value of the option", (npv_pess_abandon - npv_pess) / 2)
    r.require("Es.1 abandonment is not convenient in the optimistic scenario",
              (optimistic[1] + recovery * initial) / (1 + rate) < sum(
                  f / (1 + rate) ** t for t, f in enumerate(optimistic) if t >= 1))


def main() -> int:
    """Check the requested exams and print one line per exam plus every failure."""
    numbers = [int(a) for a in sys.argv[1:]] or list(range(1, 11))
    failures: list[str] = []
    for n in numbers:
        paper = (SRC / f"FSTR_Esame_Simulato_{n:02d}.md").read_text()
        report = Report(n, (SRC / f"FSTR_Soluzioni_Simulato_{n:02d}.md").read_text())
        {"wacc": check_wacc, "dcf": check_dcf, "options": check_options}.get(
            EXERCISE_1.get(n, ""), check_multiples)(report, paper)
        check_exercise_2(report, paper)
        status = "ok" if not report.failures else f"{len(report.failures)} FAILED"
        print(f"[{n:02d}] {report.checked} figures recomputed: {status}")
        failures += report.failures
    print("\nFAILURES" if failures else "\nall recomputed figures match the solutions")
    print("\n".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
