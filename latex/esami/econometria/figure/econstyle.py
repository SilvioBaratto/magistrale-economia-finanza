"""Shared plotting style + primitives for the Econometria exam solutions.

Every ``figure/<data>/plots.py`` starts with::

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
    import econstyle as es
    es.use()
    OUT = pathlib.Path(__file__).resolve().parent

...and ends each figure with ``es.save(fig, OUT / "fig01-nome.pdf")``.

Text is Latin Modern, the face of the shared template the solutions are set
in (latex/template/dispensa.latex), so labels match the page.
Primitives here cover the cases that recur across every exam (test densities,
confidence intervals, ECM decay, quadratic marginal effects, ACF/PACF); anything
else is plain matplotlib.
"""
from __future__ import annotations

import numpy as np
from scipy import stats

# ------------------------------------------------------------------- palette
# Tavolozza sobria, coerente con l'impostazione monocromatica del testo:
# inchiostro nero, un blu di Prussia come accento primario, un rosso mattone
# per le regioni di rifiuto, grigi per il contorno. I nomi restano quelli
# originali perche' i sette plots.py li usano.
INK = "#111111"
BLUE = "#1F3A5F"      # accento primario (densita', stime)
TEAL = "#3D4F4C"      # seconda serie
AMBER = "#6B5B3E"     # terza serie
RED = "#7B2018"       # regione di rifiuto, valori critici
GREEN = "#2E4230"     # statistica osservata
GRAY = "#5A5A5A"
RULE = "#BFBFBF"
BLUEBG = "#ECEFF3"
REDBG = "#EFE1DE"
GREENBG = "#E6EAE5"

CYCLE = [BLUE, RED, TEAL, AMBER, GREEN, GRAY]


def use() -> None:
    """Install the house style. Call once at the top of every plots.py."""
    import matplotlib
    matplotlib.use("pdf")
    import matplotlib.pyplot as plt
    from cycler import cycler
    import shutil
    import subprocess
    from matplotlib import font_manager
    from pathlib import Path

    lm = Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/lm")
    if shutil.which("kpsewhich"):
        hit = subprocess.run(["kpsewhich", "lmroman10-regular.otf"],
                             capture_output=True, text=True).stdout.strip()
        lm = Path(hit).parent if hit else lm
    for cut in ("regular", "bold", "italic", "bolditalic"):
        if (lm / f"lmroman10-{cut}.otf").exists():
            font_manager.fontManager.addfont(str(lm / f"lmroman10-{cut}.otf"))

    plt.rcParams.update({
        "font.family": "Latin Modern Roman",
        "mathtext.fontset": "cm",
        "font.size": 9.5,
        "axes.titlesize": 10.5,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 9.5,
        "axes.edgecolor": GRAY,
        "axes.labelcolor": INK,
        "axes.titlecolor": INK,
        "axes.linewidth": 0.7,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,
        "axes.prop_cycle": cycler(color=CYCLE),
        "grid.color": RULE,
        "grid.linewidth": 0.5,
        "grid.alpha": 0.8,
        "xtick.color": GRAY,
        "ytick.color": GRAY,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "legend.frameon": False,
        "legend.fontsize": 8.5,
        "figure.titlesize": 11,
        "figure.dpi": 140,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.03,
        "pdf.fonttype": 42,
        "axes.unicode_minus": False,
    })


def commas(ax, axis="both", decimals=None):
    """Italian decimal comma on the tick labels of `ax`."""
    from matplotlib.ticker import FuncFormatter

    def fmt(v, _pos):
        txt = f"{v:.{decimals}f}" if decimals is not None else f"{v:g}"
        return txt.replace(".", ",")

    for a in ((ax.xaxis, ax.yaxis) if axis == "both" else
              (ax.xaxis,) if axis == "x" else (ax.yaxis,)):
        a.set_major_formatter(FuncFormatter(fmt))
    return ax


def save(fig, path) -> None:
    """Write `fig` to `path` as PDF and close it."""
    import matplotlib.pyplot as plt
    from pathlib import Path
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="pdf")
    plt.close(fig)
    print(f"  wrote {path.name}")


# -------------------------------------------------------- distribution + test
def _frozen(kind: str, df):
    kind = kind.lower()
    if kind in {"z", "normal", "norm"}:
        return stats.norm(), "N(0,1)"
    if kind == "t":
        return stats.t(df), f"$t_{{{df}}}$"
    if kind in {"chi2", "chisq"}:
        return stats.chi2(df), rf"$\chi^2_{{{df}}}$"
    if kind == "f":
        d1, d2 = df
        return stats.f(d1, d2), f"$F_{{{d1},{d2}}}$"
    raise ValueError(f"unknown distribution {kind!r}")


def dist_test(kind, df=None, *, stat=None, crit=None, tail="two", ax=None,
              title=None, statlabel=None, critlabel=None, pvalue=None,
              xlim=None, annotate=True):
    """Density of the null distribution with the rejection region shaded.

    kind: 'z' | 't' | 'chi2' | 'F'; df: int, or (d1, d2) for F.
    tail: 'two' | 'right' | 'left'.  stat: the observed statistic.
    crit: critical value (positive; mirrored for a two-sided test).
    Returns (fig, ax).
    """
    import matplotlib.pyplot as plt

    rv, name = _frozen(kind, df)
    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(6.1, 2.9))

    lo, hi = rv.ppf(1e-5), rv.ppf(1 - 1e-5)
    if kind.lower() in {"chi2", "chisq", "f"}:
        lo = 0.0
    pts = [v for v in (stat, crit, -crit if (crit and tail == "two") else None) if v is not None]
    if pts:
        lo, hi = min(lo, min(pts) * 1.15 - 0.4), max(hi, max(pts) * 1.15 + 0.4)
    if xlim:
        lo, hi = xlim
    x = np.linspace(lo, hi, 900)
    y = rv.pdf(x)

    ax.plot(x, y, color=BLUE, lw=1.4, label=f"densità {name}")
    ax.fill_between(x, y, color=BLUEBG)

    def it(v, d=3):
        return f"{v:.{d}f}".replace(".", ",")

    if crit is not None:
        sym = {"t": "t", "z": "z", "normal": "z", "norm": "z",
               "chi2": r"\chi^2", "chisq": r"\chi^2", "f": "F"}[kind.lower()]
        # numbers stay OUT of mathtext: "1,960" inside $...$ renders as "1, 960"
        rule = {"two": rf"$|{sym}|$ > {it(abs(crit))}",
                "right": rf"${sym}$ > {it(crit)}",
                "left": rf"${sym}$ < {it(-abs(crit))}"}[tail]
        regions = {"two": [(abs(crit), hi), (lo, -abs(crit))],
                   "right": [(crit, hi)],
                   "left": [(lo, -abs(crit))]}[tail]
        first = True
        for a, b in regions:
            m = (x >= a) & (x <= b)
            if m.any():
                ax.fill_between(x[m], y[m], color=RED, alpha=0.30,
                                label=(critlabel or f"regione di rifiuto: {rule}") if first else None)
                first = False
        for c in ([abs(crit), -abs(crit)] if tail == "two"
                  else [crit if tail == "right" else -abs(crit)]):
            ax.axvline(c, color=RED, ls="--", lw=1.0)

    if stat is not None:
        lab = statlabel or f"statistica = {it(stat)}"
        if pvalue is not None:
            lab += f"  (p-value = {it(pvalue, 4)})"
        ax.axvline(stat, color=GREEN, lw=2.0, label=lab)

    commas(ax, "x")
    peak = rv.pdf(rv.ppf(0.5) if kind.lower() not in {"chi2", "chisq", "f"} else rv.ppf(0.35))
    ax.set_ylim(0, peak * 1.34)
    ax.set_xlabel("valore della statistica")
    ax.set_ylabel("densità")
    ax.set_yticks([])
    if title:
        ax.set_title(title, loc="left")
    ax.legend(loc="upper right" if (stat is None or stat <= 0.5 * (lo + hi)) else "upper left")
    return fig, ax


def ci_line(est, lo, hi, *, h0=None, ax=None, label=None, title=None,
            xlabel=None, unit="", decimals=4, extra=None):
    """A confidence interval drawn on a number line, with H0 marked.

    extra: optional list of (value, label, colour) points to mark as well.
    """
    import matplotlib.pyplot as plt
    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(6.1, 1.95))

    def fmt(v):
        return f"{v:,.{decimals}f}".replace(",", " ").replace(".", ",")

    ax.hlines(0, lo, hi, color=BLUE, lw=5, alpha=0.5,
              label=label or "intervallo di confidenza 95%")
    for v in (lo, hi):
        ax.vlines(v, -0.16, 0.16, color=BLUE, lw=1.6)
        ax.annotate(fmt(v) + unit, xy=(v, -0.22), ha="center", va="top",
                    fontsize=8.5, color=BLUE)
    ax.plot([est], [0], "o", color=BLUE, ms=7, zorder=5)
    ax.annotate("stima " + fmt(est) + unit, xy=(est, 0.2), ha="center", va="bottom",
                fontsize=9, color=BLUE, fontweight="bold")

    if h0 is not None:
        inside = lo <= h0 <= hi
        col = AMBER if inside else RED
        ax.plot([h0], [0], "D", color=col, ms=8, zorder=6)
        ax.annotate(rf"$H_0$: {fmt(h0)}{unit}" + ("\n(nell'intervallo)" if inside
                                                  else "\n(fuori: rifiuto)"),
                    xy=(h0, -0.26), ha="center", va="top", fontsize=8.5,
                    color=col, fontweight="bold")

    for v, lab, col in (extra or []):
        ax.plot([v], [0], "s", color=col, ms=6, zorder=5)
        ax.annotate(lab, xy=(v, 0.22), ha="center", va="bottom", fontsize=8, color=col)

    pad = 0.12 * (hi - lo) + 1e-12
    ax.set_xlim(min(lo, h0 if h0 is not None else lo) - pad,
                max(hi, h0 if h0 is not None else hi) + pad)
    ax.set_ylim(-0.75, 0.75)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    commas(ax, "x")
    ax.set_xlabel(xlabel or "")
    if title:
        ax.set_title(title, loc="left")
    return fig, ax


def decay(lam, *, horizon=24, targets=(0.5, 0.8), ax=None, title=None,
          ylabel="quota del disequilibrio ancora presente"):
    """ECM adjustment path (1+lambda)^h, with the horizons that absorb `targets`.

    lam is the ECM coefficient as reported (negative), e.g. -0.5120.
    Returns (fig, ax, table) where table maps each target to the integer horizon.
    """
    import matplotlib.pyplot as plt
    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(6.1, 3.2))

    phi = 1.0 + lam
    h = np.arange(0, horizon + 1)
    share = phi ** h
    ax.plot(h, share, "o-", color=BLUE, lw=1.5, ms=4,
            label=rf"$(1{lam:+.4f})^h$".replace(".", ","))
    ax.axhline(0, color=GRAY, lw=0.7)

    table = {}
    for i, tgt in enumerate(targets):
        rem = 1.0 - tgt
        hstar = int(np.ceil(np.log(rem) / np.log(phi))) if 0 < phi < 1 else None
        table[tgt] = hstar
        col = [AMBER, RED, TEAL][i % 3]
        ax.axhline(rem, color=col, ls=":", lw=1.1)
        ax.annotate(f"assorbito {tgt:.0%}".replace("%", r"\%") if False
                    else f"assorbito {int(tgt*100)}%",
                    xy=(horizon, rem), xytext=(-4, 4), textcoords="offset points",
                    ha="right", fontsize=8, color=col)
        if hstar is not None and hstar <= horizon:
            ax.plot([hstar], [phi ** hstar], "*", color=col, ms=13, zorder=6)
            ax.annotate(f"h = {hstar}", xy=(hstar, phi ** hstar), xytext=(6, 8),
                        textcoords="offset points", fontsize=8.5, color=col,
                        fontweight="bold")

    commas(ax, "y")
    ax.set_xlabel("periodi dopo lo shock ($h$)")
    ax.set_ylabel(ylabel)
    ax.set_xlim(-0.4, horizon + 0.4)
    ax.set_ylim(min(0, share.min()) - 0.04, max(1.02, share.max() + 0.04))
    if title:
        ax.set_title(title, loc="left")
    ax.legend(loc="upper right")
    return fig, ax, table


def quadratic_effect(b1, b2, *, xmax, xmin=0.0, ax=None, varname="x",
                     title=None, ylabel=None, se_b1=None, se_b2=None):
    """Marginal effect b1 + 2*b2*x of a quadratic specification, with its zero.

    Returns (fig, ax, turning_point).
    """
    import matplotlib.pyplot as plt
    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(6.1, 3.0))

    x = np.linspace(xmin, xmax, 400)
    me = b1 + 2 * b2 * x
    ax.plot(x, me, color=BLUE, lw=1.6,
            label=rf"$\partial y/\partial {varname} = {b1:.4f}{2*b2:+.4f}\,{varname}$".replace(".", ","))
    ax.axhline(0, color=RED, ls="--", lw=1.1)

    turn = -b1 / (2 * b2) if b2 else None
    if turn is not None and xmin <= turn <= xmax:
        ax.plot([turn], [0], "o", color=RED, ms=7, zorder=6)
        ax.annotate(f"effetto nullo in {varname} = " + f"{turn:.3f}".replace(".", ","),
                    xy=(turn, 0), xytext=(8, 14), textcoords="offset points",
                    fontsize=8.5, color=RED, fontweight="bold")
        ax.axvline(turn, color=RED, ls=":", lw=0.9)
    pos = me > 0
    ax.fill_between(x, me, 0, where=pos, color=GREENBG, alpha=0.9)
    ax.fill_between(x, me, 0, where=~pos, color=REDBG, alpha=0.9)

    commas(ax)
    ax.set_xlabel(varname)
    ax.set_ylabel(ylabel or "effetto marginale")
    if title:
        ax.set_title(title, loc="left")
    ax.legend(loc="best")
    return fig, ax, turn


def acf_pacf(acf_vals, pacf_vals, *, n, alpha=0.05, axes=None, title=None,
             labels=("ACF", "PACF")):
    """Stem plots of ACF and PACF with +/- z_{alpha/2}/sqrt(n) bands."""
    import matplotlib.pyplot as plt
    fig = None
    if axes is None:
        fig, axes = plt.subplots(2, 1, figsize=(6.1, 4.2), sharex=True)
    band = stats.norm.ppf(1 - alpha / 2) / np.sqrt(n)

    for ax, vals, lab in zip(axes, (acf_vals, pacf_vals), labels):
        lags = np.arange(1, len(vals) + 1)
        sig = np.abs(vals) > band
        ax.axhspan(-band, band, color=BLUEBG, zorder=0,
                   label=rf"$\pm{band:.3f}$".replace(".", ","))
        ax.axhline(0, color=GRAY, lw=0.8)
        ax.vlines(lags, 0, vals, color=[RED if s else BLUE for s in sig], lw=2.4)
        ax.plot(lags, vals, "o", ms=4,
                color=BLUE, mfc="white", mec=BLUE, zorder=5)
        ax.set_ylabel(lab)
        ax.set_ylim(min(-band * 1.5, min(vals) * 1.25 - 0.05),
                    max(band * 1.5, max(vals) * 1.25 + 0.05))
        ax.legend(loc="upper right")
        commas(ax, "y")
    axes[-1].set_xlabel("ritardo")
    if title and fig is not None:
        fig.suptitle(title, x=0.01, ha="left", color=BLUE, fontweight="bold")
    return fig, axes
