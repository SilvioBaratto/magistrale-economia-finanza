"""Print and parse OLS output in the layout of the exam texts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Sequence

from . import config

HEADER = "| | coefficiente | errore std. | rapporto $t$ | p-value |\n|---|---|---|---|---|"
HEADER_NO_P = "| | coefficiente | errore std. | rapporto $t$ |\n|---|---|---|---|"
_COLUMNS = ("coef", "se", "t", "p")
_STAT_LABELS = {"n": "n", "r2": "$R^2$", "ssr": "SSR"}
_STAT_RE = re.compile(r"(n|\$R\^2\$|SSR)\s*=\s*([-+0-9,.e]+)")


@dataclass(frozen=True)
class Table:
    """A regression table as the student reads it, at the printed precision.

    Attributes:
        rows: Regressor name to its ``coef``, ``se``, ``t`` and ``p`` values.
        stats: Fit statistics from the line under the table (``n``, ``r2``, ``ssr``).
    """

    rows: dict[str, dict[str, float]]
    stats: dict[str, float]


def fmt_sig(x: float, sig: int) -> str:
    """Format ``x`` with ``sig`` significant figures and a decimal comma."""
    return f"{x:.{sig}g}".replace(".", ",")


def fmt_p(p: float) -> str:
    """Format a p-value as the exam texts do.

    Four decimals down to 1e-4, three-figure scientific notation below it, so a
    tiny p-value is never shown as a misleading ``0,0000``.
    """
    if p == 0 or p >= 1e-4:
        return f"{p:.4f}".replace(".", ",")
    return f"{p:.3g}".replace(".", ",")


def _cell(x: float, sig: int) -> str:
    text = fmt_sig(x, sig)
    # Scientific notation does not survive the {,} math form, so it stays plain text.
    return text if "e" in text else f"${text.replace(',', '{,}')}$"


def ols_table(res, *, labels: Sequence[str] | None = None,
              stats: Sequence[str] = ("n", "r2", "ssr"), p: bool = True) -> str:
    """Render a fitted statsmodels OLS result as a Markdown table.

    Args:
        res: A ``statsmodels`` ``RegressionResults``.
        labels: Row names in the order of the regressors; defaults to the
            model's own names.
        stats: Fit statistics printed on the line under the table.
        p: Whether to print the p-value column. Turn it off for a Dickey-Fuller
            regression, where the t-based p-value of the lagged level is not the
            test's p-value.

    Returns:
        The table followed by a line such as ``n = 50; $R^2$ = 0,512345; SSR = 12,3456``.
    """
    names = list(labels) if labels is not None else list(res.model.exog_names)
    coef, se, tv, pv = (list(map(float, v)) for v in (res.params, res.bse, res.tvalues, res.pvalues))
    lines = [HEADER if p else HEADER_NO_P]
    for i, name in enumerate(names):
        row = (f"| {name} | {_cell(coef[i], config.SIG_COEF)} | {_cell(se[i], config.SIG_COEF)} "
               f"| {_cell(tv[i], config.SIG_T)} |")
        lines.append(row + (f" {fmt_p(pv[i])} |" if p else ""))
    values = {"n": str(int(res.nobs)), "r2": fmt_sig(float(res.rsquared), config.SIG_COEF),
              "ssr": fmt_sig(float(res.ssr), config.SIG_COEF)}
    line = "; ".join(f"{_STAT_LABELS[k]} = {values[k]}" for k in stats)
    return "\n".join(lines) + "\n\n" + line


def vif_table(vifs: dict[str, float]) -> str:
    """Render variance inflation factors as the exam texts print them.

    Args:
        vifs: Regressor name to its VIF.

    Returns:
        A two-column Markdown table with three decimals and a decimal comma.
    """
    rows = ["| variabile | VIF |", "|---|---|"]
    rows += [f"| {name} | {value:.3f} |".replace(".", ",") for name, value in vifs.items()]
    return "\n".join(rows)


def parse_vif(text: str) -> dict[str, float]:
    """Read back a table printed by :func:`vif_table`, at the printed precision."""
    out: dict[str, float] = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) == 2:
            try:
                out[cells[0]] = float(cells[1].replace(",", "."))
            except ValueError:
                continue
    return out


def _number(cell: str) -> float:
    return float(cell.replace("$", "").replace("{,}", ".").replace(",", "."))


def parse_table(text: str) -> Table:
    """Read a table printed by :func:`ols_table` or copied from an exam text.

    Args:
        text: Markdown with the pipe table and, optionally, the statistics line.

    Returns:
        The values at the precision they were printed.
    """
    rows: dict[str, dict[str, float]] = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells[0] or len(cells) < 4:
            continue
        try:
            rows[cells[0]] = dict(zip(_COLUMNS, (_number(c) for c in cells[1:5])))
        except ValueError:
            continue
    back = {label: key for key, label in _STAT_LABELS.items()}
    stats = {back[m.group(1)]: _number(m.group(2)) for m in _STAT_RE.finditer(text)}
    return Table(rows=rows, stats=stats)
