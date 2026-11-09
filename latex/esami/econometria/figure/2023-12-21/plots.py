#!/usr/bin/env python3
"""Figures for the 21 December 2023 Econometria exam solution.

Exercise 1 (wages, schooling, IQ) is built from the numbers printed in the exam
text. The only exception is the residuals-vs-fitted plot (d03), recomputed on
the WAGE2 data of Blackburn & Neumark (1992), `ECON_PS_01_Dati-wage2.csv` (next
to this script), with `pareduc = meduc + feduc` and parents-missing cases
dropped; it reproduces Figure 1 of the exam.

Exercise 2 (gold, silver) has no data: the figures are built from the printed
regression output, plus one seeded simulation of the Dickey-Fuller density.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
from scipy import stats
es.use()
import matplotlib.pyplot as plt

OUT = pathlib.Path(__file__).resolve().parent
SEED = 20231221

# --------------------------------------------------------------------- dati
# A copy of Moodle/01-Econometria/Dataset-CSV/Problem-Set/ECON_PS_01_Dati-wage2.csv,
# kept beside the script so the folder stands on its own.
CSV = OUT / "ECON_PS_01_Dati-wage2.csv"

import pandas as pd

_d = pd.read_csv(CSV)
_d["pareduc"] = _d.meduc + _d.feduc
D = _d.dropna(subset=["meduc", "feduc"]).copy()
# Plain least squares instead of statsmodels: only fitted values and residuals
# are needed, and statsmodels fails to import against the installed scipy.
_X1 = np.column_stack([np.ones(len(D)), D.educ, D.pareduc, D.exper, D.married])
_b1 = np.linalg.lstsq(_X1, D.lwage.values, rcond=None)[0]
FITTED = _X1 @ _b1
RESID = D.lwage.values - FITTED
assert len(D) == 722, len(D)
assert abs(_b1[1] - 0.0650240) < 1e-6

# Model 1 coefficients as printed in the exam text.
B_EDUC = 0.0650240
B_MARR = 0.203713


def it(v, d=3):
    return f"{v:.{d}f}".replace(".", ",")


# ===================================================================== D 1
# Linear approximation: 100 * beta1 * dEduc = 15.
def d01():
    fig, ax = plt.subplots(figsize=(5.4, 2.7))
    dx = np.linspace(0, 4, 400)
    ax.plot(dx, 100 * B_EDUC * dx, color=es.BLUE, lw=1.8,
            label=r"$100\,\beta_1\,\Delta$educ")
    ax.axhline(15, color=es.RED, lw=1.0, ls=":")
    ax.annotate("obiettivo +15%", xy=(3.95, 15), xytext=(0, 5), ha="right",
                textcoords="offset points", fontsize=8.5, color=es.RED)
    x15 = 0.15 / B_EDUC
    ax.plot([x15], [15], "o", color=es.BLUE, ms=6, zorder=6)
    ax.vlines(x15, 0, 15, color=es.BLUE, lw=0.9, ls=":")
    ax.annotate(f"{it(x15, 2)} anni", xy=(x15, 15), xytext=(8, -18),
                textcoords="offset points", fontsize=8.8, color=es.BLUE,
                fontweight="bold")
    ax.set_xlim(0, 4); ax.set_ylim(0, 28)
    ax.set_xlabel(r"$\Delta$educ (anni di istruzione in più)")
    ax.set_ylabel("variazione attesa del salario (%)")
    ax.set_title("Dalla variazione di educ alla variazione %", loc="left")
    ax.legend(loc="upper left")
    es.commas(ax)
    fig.tight_layout()
    es.save(fig, OUT / "d01-anni-per-quindici-percento.pdf")


# ===================================================================== D 2
# The `married` coefficient is a percentage change, not a dollar amount.
def d02():
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    w = np.linspace(0, 3000, 400)
    ax.plot(w, B_MARR * w, color=es.BLUE, lw=1.8,
            label=r"$\Delta$wage $=\hat\beta_4\,$wage$_0$")
    ax.axhline(20, color=es.RED, lw=1.1, ls="--", label="20 dollari (la domanda)")
    w20 = 20 / B_MARR
    ax.plot([w20], [20], "o", color=es.RED, ms=6, zorder=6)
    ax.annotate(f"20 \\$ richiedono\nwage$_0$ = {it(w20, 1)} \\$",
                xy=(w20, 20), xytext=(300, 330), textcoords="data",
                ha="left", va="center", fontsize=8.4, color=es.RED,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.9))
    ax.set_xlim(0, 3000); ax.set_ylim(0, 640)
    ax.set_xlabel("salario mensile di partenza wage$_0$ (dollari)")
    ax.set_ylabel("differenza sposato $-$ single (dollari)")
    ax.set_title("Lo stesso 20,37% vale dollari diversi", loc="left")
    ax.legend(loc="upper left")
    es.commas(ax)
    fig.tight_layout()
    es.save(fig, OUT / "d02-percentuale-non-dollari.pdf")


# ===================================================================== D 3
# Residuals vs fitted values, recomputed on the WAGE2 data: same picture as
# Figure 1 of the exam, with the decile standard deviation as a visual guide.
def d03():
    fig, ax = plt.subplots(figsize=(5.4, 2.9))
    yhat, res = FITTED, RESID
    ax.scatter(yhat, res, s=11, facecolors="none", edgecolors=es.TEAL, lw=0.6,
               alpha=0.85, label="residui OLS")
    ax.axhline(0, color=es.GRAY, lw=0.8, ls=":")
    edges = np.quantile(yhat, np.linspace(0, 1, 11))
    ctr, sd = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (yhat >= a) & (yhat <= b)
        ctr.append(yhat[m].mean()); sd.append(res[m].std(ddof=1))
    ctr, sd = np.array(ctr), np.array(sd)
    ax.plot(ctr, sd, color=es.RED, lw=1.6, marker="o", ms=3.5,
            label=r"$\pm$ dev. std. per decile di $\hat y$")
    ax.plot(ctr, -sd, color=es.RED, lw=1.6, marker="o", ms=3.5)
    ax.set_xlabel(r"valori predetti $\hat y$")
    ax.set_ylabel(r"residui $\hat\epsilon$")
    ax.set_title("Residui contro valori predetti", loc="left")
    ax.set_ylim(-2.2, 2.9)
    ax.legend(loc="upper center", ncol=1, fontsize=8.2, borderaxespad=0.3)
    es.commas(ax)
    fig.tight_layout()
    es.save(fig, OUT / "d03-residui-e-robustezza.pdf")


# ===================================================================== D 4
# Omitted variable: the educ coefficient as printed in the two exam tables
# (Model 1 from the first table, Model 2 from the comparison table).
def d04():
    fig, ax = plt.subplots(figsize=(4.4, 2.85))
    labs = ["Mod. 1\n(senza IQ)", "Mod. 2\n(con IQ)"]
    est, ses = [B_EDUC, 0.035], [0.00764027, 0.008]
    xs = np.arange(2)
    for x, e, s in zip(xs, est, ses):
        ax.errorbar([x], [e], yerr=[1.96 * s], fmt="o", color=es.BLUE, ms=7,
                    capsize=5, lw=1.4)
        ax.annotate(it(e, 4 if x == 0 else 3), xy=(x, e), xytext=(9, 2),
                    textcoords="offset points", fontsize=8.4, color=es.BLUE,
                    fontweight="bold")
    ax.annotate("", xy=(1, est[1]), xytext=(0, est[0]),
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.3, ls="--"))
    ax.annotate(r"$-0{,}030$", xy=(0.5, 0.0575), ha="center", va="center",
                fontsize=8.6, color=es.RED, fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(labs, fontsize=8.4)
    ax.set_xlim(-0.6, 1.7); ax.set_ylim(0.01, 0.09)
    ax.set_ylabel(r"$\hat\beta_{educ}$  (IC 95%)")
    ax.set_title("Il coefficiente di educ cala", loc="left")
    es.commas(ax, "y", decimals=3)
    fig.tight_layout()
    es.save(fig, OUT / "d04-variabile-omessa.pdf")


# ===================================================================== D 5
# Collinearity: ratio of the printed standard errors (Model 1 from the first
# table, Model 2 from the comparison table) against sqrt(10), i.e. VIF = 10.
def d05():
    fig, ax = plt.subplots(figsize=(4.8, 2.9))
    reg = ["educ", "pareduc", "exper", "married"]
    se1 = [0.00764027, 0.00277333, 0.00372447, 0.0462668]
    se2 = [0.008, 0.002, 0.004, 0.045]
    ratio = [b / a for a, b in zip(se1, se2)]
    ys = np.arange(len(reg))[::-1]
    ax.axvline(1, color=es.GRAY, lw=0.9, ls=":")
    ax.axvline(np.sqrt(10), color=es.RED, lw=1.3, ls="--")
    ax.annotate(r"$\sqrt{10}$: VIF = 10", xy=(np.sqrt(10) - 0.06, len(reg) - 0.55),
                ha="right", va="center", fontsize=8.4, color=es.RED,
                fontweight="bold")
    for y, r in zip(ys, ratio):
        ax.plot([r], [y], "o", color=es.BLUE, ms=7, zorder=5)
        left = r < 1
        ax.annotate(it(r, 2), xy=(r, y), xytext=(-9 if left else 9, 0),
                    ha="right" if left else "left", va="center",
                    textcoords="offset points", fontsize=8.4, color=es.BLUE,
                    fontweight="bold")
    ax.set_yticks(ys); ax.set_yticklabels(reg, fontsize=8.4)
    ax.set_xlim(0.4, 3.6); ax.set_ylim(-0.6, len(reg) - 0.2)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("s.e. Mod. 2 / s.e. Mod. 1 (stampati)")
    ax.set_title("Gli errori standard non esplodono", loc="left")
    es.commas(ax, "x", decimals=1)
    fig.tight_layout()
    es.save(fig, OUT / "d05-collinearita.pdf")


# ===================================================================== D 6
# Confidence interval of 100 * 10 * beta_IQ from the printed numbers, with the
# 5% threshold of the question.
def d06():
    est, se = 5.0, 1.0
    fig, ax = plt.subplots(figsize=(6.1, 1.95))
    es.ci_line(est, est - 1.96 * se, est + 1.96 * se, h0=5.0, ax=ax,
               decimals=2, unit="%",
               xlabel=r"variazione attesa del salario per $+10$ punti di IQ (%)",
               title=r"IC 95% di $100\times10\,\beta_{IQ}$")
    fig.tight_layout()
    es.save(fig, OUT / "d06-dieci-punti-di-iq.pdf")


# ===================================================================== D 7
# The test is one-sided to the left of beta1 = 1 (delta < 0).
def d07():
    fig, ax = plt.subplots(figsize=(5.4, 2.3))
    ax.fill_between([0.90, 1.0], -1, 1, color=es.GREENBG, zorder=0)
    ax.fill_between([1.0, 1.04], -1, 1, color=es.REDBG, zorder=0)
    ax.axvline(1.0, color=es.RED, lw=1.6)
    ax.annotate(r"$H_0:\ \beta_1=1\ \Leftrightarrow\ \delta=0$"
                "\nradice unitaria", xy=(0.9955, 0.72), ha="right", va="center",
                fontsize=8.4, color=es.RED, fontweight="bold")
    ax.annotate(r"$H_1:\ \beta_1<1\ \Leftrightarrow\ \delta<0$"
                "\nserie stazionaria", xy=(0.948, -0.45), ha="center",
                va="center", fontsize=8.4, color=es.GREEN, fontweight="bold")
    ax.annotate("", xy=(0.905, 0.05), xytext=(0.995, 0.05),
                arrowprops=dict(arrowstyle="->", color=es.GREEN, lw=1.6))
    ax.set_xlim(0.90, 1.03); ax.set_ylim(-1, 1)
    ax.set_yticks([]); ax.grid(axis="y", visible=False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(r"$\beta_1$ (coefficiente di $\text{gold}_{t-1}$ nell'AR)")
    ax.set_title("Test unilaterale sinistro", loc="left")
    es.commas(ax, "x", decimals=2)
    fig.tight_layout()
    es.save(fig, OUT / "d07-dickey-fuller-impostazione.pdf")


# ---------------------------------------------- distribuzione DF simulata
def _df_null(T=500, R=20000, seed=SEED):
    """Distribuzione simulata della t di Dickey-Fuller con costante."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(R // 2000):
        y = np.cumsum(rng.normal(0, 1, (2000, T + 1)), axis=1)
        x = y[:, :-1]
        dy = np.diff(y, axis=1)
        xc = x - x.mean(axis=1, keepdims=True)
        dc = dy - dy.mean(axis=1, keepdims=True)
        sxx = (xc ** 2).sum(axis=1)
        d = (xc * dc).sum(axis=1) / sxx
        ssr = ((dc - d[:, None] * xc) ** 2).sum(axis=1)
        sig2 = ssr / (T - 2)
        out.append(d / np.sqrt(sig2 / sxx))
    return np.concatenate(out)


# ===================================================================== D 8
def d08():
    t_obs, crit = 0.3448, -2.86
    tt = _df_null()
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    grid = np.linspace(-5.2, 3.2, 700)
    kde = stats.gaussian_kde(tt)
    y = kde(grid)
    ax.plot(grid, y, color=es.BLUE, lw=1.6,
            label="densità Dickey-Fuller\ncon costante (simulata)")
    ax.fill_between(grid, y, color=es.BLUEBG)
    m = grid <= crit
    ax.fill_between(grid[m], y[m], color=es.RED, alpha=0.30,
                    label="regione di rifiuto al 5%")
    ax.axvline(crit, color=es.RED, lw=1.1, ls="--")
    ax.axvline(t_obs, color=es.GREEN, lw=2.2)
    ax.annotate(r"$t^{oss}=0{,}3448$" "\n(p-value ADF = 0,9806)",
                xy=(t_obs, 0.455), xytext=(9, 0), textcoords="offset points",
                ha="left", va="center", fontsize=8.4, color=es.GREEN,
                fontweight="bold")
    ax.set_xlim(-5.2, 4.4); ax.set_ylim(0, 0.80)
    ax.set_yticks([])
    ax.set_xlabel("valore della statistica")
    ax.set_ylabel("densità")
    ax.set_title(r"ADF su gold$_t$: la statistica non cade nella regione di rifiuto",
                 loc="left")
    ax.legend(loc="upper left", fontsize=8.4)
    es.commas(ax, "x", decimals=1)
    es.save(fig, OUT / "d08-adf-gold.pdf")


# ===================================================================== D 9
def d09():
    fig, axes = plt.subplots(2, 1, figsize=(6.1, 4.4),
                             gridspec_kw={"height_ratios": [1.05, 1]})

    ax = axes[0]
    labs = [r"ADF su gold$_t$" "\n(dom. 8)\nnon rifiuto: I(1)",
            r"ADF su silver$_t$" "\n(dato dal testo)\nnon rifiuto: I(1)",
            "Engle-Granger\nsui residui\nrifiuto: stazionari"]
    pv = [0.9806, 0.74, 0.00007]
    cols = [es.BLUE, es.BLUE, es.GREEN]
    xs = np.arange(3)
    ax.bar(xs, pv, 0.45, color=cols, alpha=0.85)
    ax.set_yscale("log")
    ax.axhline(0.05, color=es.RED, lw=1.3, ls="--")
    ax.annotate(r"livello 5%", xy=(1.30, 0.068), ha="left", va="bottom",
                fontsize=8.4, color=es.RED, fontweight="bold")
    for x, p in zip(xs, pv):
        ax.annotate(f"p = {p:.5f}".rstrip("0").replace(".", ","),
                    xy=(x, p), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.4,
                    color=es.INK, fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(labs, fontsize=8.4)
    ax.set_ylim(1e-5, 12)
    ax.set_ylabel("p-value (scala log)")
    ax.set_title("I tre passi della procedura di Engle-Granger", loc="left")

    b, sb = 54.9646, 0.233509
    est, lo, hi = 2 * b, 2 * b - 1.96 * 2 * sb, 2 * b + 1.96 * 2 * sb
    ax = axes[1]
    ax.hlines(0, lo, hi, color=es.BLUE, lw=7, alpha=0.55)
    for v in (lo, hi):
        ax.vlines(v, -0.2, 0.2, color=es.BLUE, lw=1.6)
    ax.plot([est], [0], "o", color=es.BLUE, ms=8, zorder=6)
    ax.annotate(f"stima {it(est,3)} \\$\nIC 95%: [{it(lo,3)} ; {it(hi,3)}]",
                xy=(est, -0.3), ha="center", va="top", fontsize=8.6,
                color=es.BLUE, fontweight="bold")
    ax.plot([75.0], [0], "D", color=es.RED, ms=9, zorder=6)
    ax.annotate("$H_0$: 75 \\$\n(fuori dall'intervallo)",
                xy=(75.0, -0.3), ha="center", va="top", fontsize=8.6,
                color=es.RED, fontweight="bold")
    ax.set_xlim(71, 115); ax.set_ylim(-1.15, 1.25)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel(r"variazione di gold per $+2$ dollari di silver (dollari)")
    ax.set_title(r"$H_0:\ 2\beta=75$, cioè $\beta=37{,}5$", loc="left")
    es.commas(ax, "x", decimals=0)
    fig.tight_layout()
    es.save(fig, OUT / "d09-cointegrazione-e-beta.pdf")


# ===================================================================== D 10
def d10():
    lam = -0.0298275
    phi = 1 + lam
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    h = np.arange(1, 6)
    share = 100 * (1 - phi ** h)
    ax.bar(h, share, 0.55, color=es.BLUE, alpha=0.85)
    ax.axhline(5, color=es.RED, lw=1.2, ls="--")
    ax.annotate("assorbito 5%", xy=(0.45, 5.15), ha="left", va="bottom",
                fontsize=8.4, color=es.RED, fontweight="bold")
    for x, v in zip(h, share):
        ax.annotate(f"{it(v, 2)}%", xy=(x, v), xytext=(0, 3),
                    textcoords="offset points", ha="center", fontsize=8.4,
                    color=es.INK, fontweight="bold")
    ax.set_xticks(h)
    ax.set_xlim(0.4, 5.6); ax.set_ylim(0, 16)
    ax.set_xlabel("giorni di contrattazione dopo lo shock")
    ax.set_ylabel("quota di disequilibrio assorbita (%)")
    ax.set_title(r"$1-(1+\lambda)^h$ con $\hat\lambda=-0{,}0298$", loc="left")
    es.commas(ax, "y", decimals=0)
    fig.tight_layout()
    es.save(fig, OUT / "d10-assorbimento-ecm.pdf")


if __name__ == "__main__":
    d01(); d02(); d03(); d04(); d05(); d06(); d07(); d08(); d09(); d10()
