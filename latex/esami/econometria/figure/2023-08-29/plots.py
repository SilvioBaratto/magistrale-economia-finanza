#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 29 agosto 2023.

Esercizio 1 — studenti-atleti (log-lin, interazione season x tothrs, White, VIF).
Esercizio 2 — petrolio e occupazione in Texas (ADF, cointegrazione, due ECM).
Il coefficiente di shrs e' beta_6, come nel manoscritto del docente.

Tutti i numeri provengono dagli output riportati nel testo d'esame
(`../../Esami/ECON_Esame_2023-08-29.md`): nessun dataset e' disponibile per
questo appello (cfr. `_teoria/dati.md`). L'unica figura con dati generati e'
il pannello (b) di `d02`, esplicitamente dichiarato come simulazione
illustrativa con seme fissato.

    python3 figure/2023-08-29/plots.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
from scipy import stats
es.use()
OUT = pathlib.Path(__file__).resolve().parent

import matplotlib.pyplot as plt

# --------------------------------------------------------------- numeri esame
# Modello 1 (senza shrs), n = 366
B_SAT, SE_SAT = 0.000981546, 7.02429e-05
B_SEA1, SE_SEA1 = -0.0155715, 0.0278561
B_FEM1, SE_FEM1 = 0.239472, 0.0234400
B_TOT1, SE_TOT1 = 0.00144110, 0.000355064
# Modello 2 (con shrs = season x tothrs)
B_SEA2, SE_SEA2 = -0.0249877, 0.0493320
B_FEM2, SE_FEM2 = 0.239155, 0.0235867
B_TOT2, SE_TOT2 = 0.00130725, 0.000635719
B_SHRS, SE_SHRS = 0.00197486, 0.000776246
VIF = {"sat": 1.024, "season": 2.976, "female": 1.076, "tothrs": 3.087, "shrs": 4.738}
# Esercizio 2
ADF = {"USNAG": (-2.79173, 0.2003), "TXNAG": (0.41061, 0.9991), "RPO": (-1.07942, 0.5636)}
CDF = {"TXNAG–RPO": (-0.530515, 0.9612), "USNAG–RPO": (-0.309651, 0.9748),
       "TXNAG–USNAG": (-1.210521, 0.8536)}
LAM_TX, SE_LAM_TX = -0.218680, 0.0667798
LAM_IDX, SE_LAM_IDX = -0.144386, 0.0431124
G0_IDX = 0.181332


def n(x, d=4):
    """numero in stile italiano (virgola decimale)."""
    return f"{x:.{d}f}".replace(".", ",")


def pct(x, d=2):
    return n(x, d) + r"%"


def ci_soglie(ax, est, lo, hi, marks, *, xlabel="", title="", decimals=4,
              pad=0.16):
    """IC su retta numerica con più soglie, etichette a quote diverse.

    Primitiva locale: `es.ci_line` sovrappone le etichette quando la soglia
    cade a ridosso di un estremo dell'intervallo, com'è il caso qui.
    `marks` = lista di (valore, etichetta, colore, quota verticale).
    """
    ax.hlines(0, lo, hi, color=es.BLUE, lw=5.5, alpha=0.45,
              label="intervallo di confidenza al 95%")
    for v in (lo, hi):
        ax.vlines(v, -0.14, 0.14, color=es.BLUE, lw=1.6)
        ax.annotate(n(v, decimals), xy=(v, 0.19), ha="center", va="bottom",
                    fontsize=8.5, color=es.BLUE)
    ax.plot([est], [0], "o", color=es.BLUE, ms=7.5, zorder=6)
    ax.annotate("stima " + n(est, decimals), xy=(est, -0.20), ha="center",
                va="top", fontsize=9, color=es.BLUE, fontweight="bold")
    for v, lab, col, dy in marks:
        ax.plot([v], [0], "D", color=col, ms=7.5, zorder=7)
        ax.vlines(v, 0, dy, color=col, lw=0.9, ls=":")
        ax.annotate(lab, xy=(v, dy), ha="center",
                    va="bottom" if dy > 0 else "top",
                    fontsize=8.5, color=col, fontweight="bold")
    span = hi - lo
    left = min([lo] + [m[0] for m in marks]) - pad * span
    right = max([hi] + [m[0] for m in marks]) + pad * span
    ax.set_xlim(left, right)
    ax.set_ylim(-1.05, 1.15)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x", decimals=decimals)
    ax.set_xlabel(xlabel)
    if title:
        ax.set_title(title, loc="left")
    ax.legend(loc="lower right", fontsize=8.3)


# ============================================================ D1 — soglia 2%
def d01():
    lo, hi = B_TOT1 - 1.96 * SE_TOT1, B_TOT1 + 1.96 * SE_TOT1
    soglia = 0.02 / 30

    fig, ax = plt.subplots(figsize=(6.2, 2.5))
    ci_soglie(ax, B_TOT1, lo, hi,
              [(soglia, r"$0{,}000667$" + "\nfuori dall'IC, a sinistra", es.RED, 0.45)],
              xlabel=r"$\beta_4$  (punti di log-gpa per ora)", pad=0.30,
              decimals=6,
              title=r"IC al 95% per $\beta_4$ e soglia $0{,}02/30$")
    fig.tight_layout()
    es.save(fig, OUT / "d01-soglia-due-percento.pdf")


# ==================================================== D2 — White vs esogeneita
def d02():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 3.1))

    es.dist_test("chi2", 12, stat=24.697, crit=stats.chi2.ppf(0.95, 12),
                 tail="right", ax=ax1, pvalue=0.016,
                 title=r"(a) White: $H_0$ = omoschedasticità",
                 statlabel=r"$T_W$ = 24,697")
    # spazio sopra la densita': altrimenti la legenda ci cade sopra
    ax1.set_ylim(0, ax1.get_ylim()[1] * 1.45)
    # le rette verticali si fermano sotto la legenda, che altrimenti le taglia
    for ln in ax1.lines[1:]:
        ln.set_ydata([0.0, 0.58])
    ax1.legend(loc="upper right", fontsize=8.2)

    rng = np.random.default_rng(20230829)
    x = rng.uniform(800, 1400, 500)
    sd = 0.02 + 0.00012 * (x - 800)
    eps = rng.normal(0.0, sd)
    ax2.scatter(x, eps, s=7, color=es.BLUE, alpha=0.55, lw=0)
    ax2.axhline(0.0, color=es.GREEN, lw=1.8, label=r"$\operatorname{E}[\epsilon\mid X] = 0$: vale")
    grid = np.linspace(800, 1400, 200)
    band = 1.96 * (0.02 + 0.00012 * (grid - 800))
    ax2.plot(grid, band, color=es.RED, ls="--", lw=1.2,
             label=r"$\pm 1{,}96\,\sigma(X)$: $\operatorname{Var}$ cresce")
    ax2.plot(grid, -band, color=es.RED, ls="--", lw=1.2)
    es.commas(ax2, "x", decimals=0)
    es.commas(ax2, "y", decimals=2)
    ax2.set_xlabel("sat")
    ax2.set_ylabel(r"$\epsilon$")
    ax2.set_title("(b) eteroschedasticità con esogeneità intatta", loc="left")
    ax2.set_ylim(-0.30, 0.40)
    ax2.legend(loc="upper left", fontsize=8.2)
    fig.tight_layout()
    es.save(fig, OUT / "d02-white-vs-esogeneita.pdf")


# =============================================== D3 — gap season a tothrs = 50
def d03():
    h = np.linspace(0, 120, 400)
    gap = 100 * (B_SEA2 + B_SHRS * h)
    at50 = 100 * (B_SEA2 + 50 * B_SHRS)
    at0 = 100 * B_SEA2

    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    ax.plot(h, gap, color=es.BLUE, lw=1.7,
            label=r"$100\,(\hat\beta_2 + \hat\beta_6\,\mathrm{tothrs})$")
    ax.axhline(0, color=es.GRAY, lw=0.9)
    ax.fill_between(h, gap, 0, where=gap >= 0, color=es.GREENBG)
    ax.fill_between(h, gap, 0, where=gap < 0, color=es.REDBG)

    ax.plot([50], [at50], "*", color=es.TEAL, ms=15, zorder=7)
    ax.annotate("tothrs = 50:  gap = +" + n(at50, 1) + r"%", xy=(50, at50),
                xytext=(12, -16), textcoords="offset points", va="top",
                fontsize=9, color=es.TEAL, fontweight="bold")

    ax.plot([0], [at0], "s", color=es.AMBER, ms=6, zorder=6)
    ax.annotate("tothrs = 0:  gap = " + n(at0, 1) + r"%", xy=(0, at0),
                xytext=(54, -12), textcoords="offset points", va="top",
                fontsize=8.5, color=es.AMBER,
                arrowprops=dict(arrowstyle="->", color=es.AMBER, lw=0.8))

    es.commas(ax, "both", decimals=1)
    ax.set_xlabel("tothrs (ore frequentate)")
    ax.set_ylabel("gap di season su gpa (%)")
    ax.set_title("Impatto della stagione agonistica in funzione delle ore frequentate",
                 loc="left")
    ax.legend(loc="upper left")
    ax.set_xlim(0, 120)
    ax.set_ylim(-7.5, 26.5)
    fig.tight_layout()
    es.save(fig, OUT / "d03-gap-season-tothrs.pdf")


# ================================================ D4 — effetto marginale tothrs
T_SHRS = 2.5443   # rapporto t riportato nella tabella d'esame


def d04():
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(6.2, 5.2), gridspec_kw={"height_ratios": [1.15, 1.0]})

    h = np.linspace(0, 120, 300)
    ax1.plot(h, 100 * B_TOT2 * h, color=es.BLUE, lw=1.8,
             label=r"season = 0:  pendenza $\beta_4 = 0{,}00130725$")
    ax1.plot(h, 100 * (B_TOT2 + B_SHRS) * h, color=es.AMBER, lw=1.8,
             label=r"season = 1:  pendenza $\beta_4+\beta_6 = 0{,}00328211$")
    ax1.fill_between(h, 100 * B_TOT2 * h, 100 * (B_TOT2 + B_SHRS) * h,
                     color=es.BLUEBG, alpha=0.9)
    ax1.annotate("la differenza fra le pendenze\n" + r"è $\beta_6 = 0{,}00197486$",
                 xy=(88, 100 * (B_TOT2 + 0.5 * B_SHRS) * 88),
                 xytext=(0.27, 0.60), textcoords="axes fraction", va="top",
                 fontsize=8.5, color=es.GRAY,
                 arrowprops=dict(arrowstyle="->", color=es.GRAY, lw=0.8))
    es.commas(ax1, "both", decimals=1)
    ax1.set_xlabel("tothrs (ore frequentate)")
    ax1.set_ylabel(r"$100\,\Delta\mathrm{gpa}/\mathrm{gpa}$ rispetto a tothrs = 0")
    ax1.set_title(r"(a) $\Delta\mathrm{gpa}/\mathrm{gpa} = (\beta_4 + \beta_6\,\mathrm{season})\,\Delta\mathrm{tothrs}$",
                  loc="left")
    ax1.legend(loc="upper left")
    ax1.set_xlim(0, 120)
    ax1.set_ylim(0, 44)

    es.dist_test("z", stat=T_SHRS, crit=1.96, tail="two", ax=ax2,
                 pvalue=0.0109, statlabel=r"$t$ su $\beta_6$ = 2,5443",
                 title=r"(b) $H_0:\beta_6 = 0$ contro $H_1:\beta_6 \neq 0$")
    # nel test bilaterale la legenda finirebbe sul critico negativo: le rette
    # si fermano sotto la fascia che le lascio
    ax2.set_ylim(0, ax2.get_ylim()[1] * 1.42)
    for ln in ax2.lines[1:]:
        ln.set_ydata([0.0, 0.70])
    ax2.legend(loc="upper left", fontsize=8.3)
    fig.tight_layout()
    es.save(fig, OUT / "d04-effetto-marginale-tothrs.pdf")


# ================================================== D5 — premio femminile 25%
def d05():
    b, s = B_FEM2, SE_FEM2
    lo, hi = b - 1.96 * s, b + 1.96 * s
    fig, ax = plt.subplots(figsize=(6.2, 2.5))
    ci_soglie(ax, b, lo, hi,
              [(0.25, r"$0{,}25$" + "\ndentro l'IC", es.AMBER, 0.45)],
              xlabel=r"$\beta_3$  (punti di log-gpa)", pad=0.30,
              title=r"IC al 95% per $\beta_3$ e valore $0{,}25$")
    fig.tight_layout()
    es.save(fig, OUT / "d05-premio-femminile.pdf")


# ================================================================== D6 — VIF
def d06():
    fig, ax = plt.subplots(figsize=(6.2, 3.1))

    names = list(VIF)
    v = np.array([VIF[k] for k in names])
    r = np.sqrt(v)
    x = np.arange(len(names))
    ax.bar(x - 0.19, v, width=0.36, color=es.RULE, label=r"$\mathrm{VIF}_j$ (varianza)")
    ax.bar(x + 0.19, r, width=0.36, color=es.BLUE,
           label=r"$\sqrt{\mathrm{VIF}_j}$ (errore standard)")
    for xi, vi, ri in zip(x, v, r):
        ax.annotate(n(vi, 3), xy=(xi - 0.19, vi), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.2,
                    color=es.GRAY)
        ax.annotate(n(ri, 3), xy=(xi + 0.19, ri), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.2,
                    color=es.BLUE, fontweight="bold")
    ax.axhline(1.0, color=es.GREEN, lw=1.0, ls=":")
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=9)
    es.commas(ax, "y", decimals=1)
    ax.set_ylim(0, 6.3)
    ax.set_ylabel("fattore di gonfiaggio")
    ax.set_title("Il VIF gonfia la varianza, la sua radice l'errore standard", loc="left")
    ax.legend(loc="upper left", fontsize=8.3)
    fig.tight_layout()
    es.save(fig, OUT / "d06-vif-shrs.pdf")


def _pvalue_bars(ax, data, title):
    names = list(data)
    p = [data[k][1] for k in names]
    y = np.arange(len(names))[::-1]
    ax.barh(y, p, height=0.5, color=es.AMBER, alpha=0.85)
    ax.axvline(0.05, color=es.RED, ls="--", lw=1.3)
    for yi, pi in zip(y, p):
        ax.annotate(n(pi, 4), xy=(pi, yi), xytext=(6, 0), textcoords="offset points",
                    va="center", fontsize=8.5, fontweight="bold", color=es.INK)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlim(0, 1.22)
    ax.set_ylim(-0.82, len(names) - 0.1)
    es.commas(ax, "x", decimals=1)
    ax.grid(axis="y", visible=False)
    ax.annotate(r"$\alpha = 5\%$", xy=(0.05, -0.64), xytext=(5, 0),
                textcoords="offset points", ha="left", va="center",
                fontsize=8.5, color=es.RED, fontweight="bold")
    ax.set_xlabel("p-value")
    ax.set_title(title, loc="left")


# ========================================================= D7 — radici unitarie
def d07():
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    _pvalue_bars(ax, ADF, "p-value dei test ADF: nessuno scende sotto il 5%")
    fig.tight_layout()
    es.save(fig, OUT / "d07-radici-unitarie.pdf")


# ========================================================= D8 — cointegrazione
def d08():
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    _pvalue_bars(ax, CDF, "p-value dei test CDF: nessuna coppia scende sotto il 5%")
    fig.tight_layout()
    es.save(fig, OUT / "d08-cointegrazione.pdf")


# ======================================================= D9 — assorbimento ECM
def d09():
    k = np.arange(0, 6)
    cum = 1 - (1 + LAM_TX) ** (k + 1)
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    cols = [es.BLUE if c < 0.5 else es.GREEN for c in cum]
    ax.bar(k, 100 * cum, width=0.55, color=cols, alpha=0.85)
    for ki, ci in zip(k, cum):
        ax.annotate(n(100 * ci, 2) + r"%", xy=(ki, 100 * ci), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.5,
                    fontweight="bold", color=es.INK)
    ax.axhline(50, color=es.RED, ls="--", lw=1.3, label="50% del disequilibrio")
    ax.set_xticks(k)
    ax.set_xticklabels(["subito", "+1", "+2", "+3", "+4", "+5"])
    es.commas(ax, "y", decimals=0)
    ax.set_ylim(0, 92)
    ax.grid(axis="x", visible=False)
    ax.set_xlabel("trimestri dopo l'impatto")
    ax.set_ylabel("disequilibrio assorbito (%)")
    ax.set_title(r"Quota cumulata assorbita, $1-(1+\hat\lambda)^{k+1}$ con $\hat\lambda = -0{,}21868$",
                 loc="left")
    ax.legend(loc="upper left")
    fig.tight_layout()
    es.save(fig, OUT / "d09-assorbimento-ecm.pdf")


# =================================================== D10 — disequilibrio < 0
def d10():
    ecm = np.linspace(-3.0, 0.0, 200)
    corr = LAM_IDX * ecm
    tot = G0_IDX + corr

    fig, ax = plt.subplots(figsize=(6.2, 3.1))
    ax.axhline(0, color=es.GRAY, lw=0.9)
    ax.fill_between(ecm, G0_IDX, tot, color=es.GREENBG)
    ax.plot(ecm, tot, color=es.BLUE, lw=1.8,
            label=r"$\hat\gamma_0 + \hat\lambda\,\mathrm{ecm}_{t-1}$  (con $\Delta RPO_t = 0$)")
    ax.axhline(G0_IDX, color=es.AMBER, ls=":", lw=1.2,
               label=r"$\hat\gamma_0 = 0{,}1813$")
    ax.annotate(r"$\hat\lambda\,\mathrm{ecm}_{t-1} > 0$", xy=(-1.6, 0.30),
                fontsize=9, color=es.GREEN, fontweight="bold", ha="center")
    es.commas(ax, "both", decimals=1)
    ax.set_xlabel(r"disequilibrio negativo, $\mathrm{ecm}_{t-1} < 0$")
    ax.set_ylabel(r"$\operatorname{E}[\Delta IDX_t]$")
    ax.set_xlim(-3.0, 0.0)
    ax.set_ylim(-0.05, 0.70)
    ax.set_title(r"Con $\mathrm{ecm}_{t-1} < 0$ e $\hat\lambda < 0$ la variazione attesa di $IDX$ è positiva",
                 loc="left")
    ax.legend(loc="upper right", fontsize=8.3)
    fig.tight_layout()
    es.save(fig, OUT / "d10-disequilibrio-negativo.pdf")


if __name__ == "__main__":
    for fn in (d01, d02, d03, d04, d05, d06, d07, d08, d09, d10):
        fn()
    print("fatto.")
