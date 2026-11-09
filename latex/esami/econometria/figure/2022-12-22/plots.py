#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 22 dicembre 2022.

Tutti i numeri provengono dagli output di regressione riportati nel testo
d'esame (`../../Esami/ECON_Esame_2022-12-22.md`); le sole quantita' lette a
occhio sono le autocorrelazioni delle Figure 1 e 2 del testo (pp. 6 e 8),
raccolte in ACF_LP/PACF_LP e ACF_ECM/PACF_ECM e dichiarate come tali nelle
didascalie.  Nessuna serie simulata.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
es.use()
OUT = pathlib.Path(__file__).resolve().parent

import matplotlib.pyplot as plt

def it(v, d=4):
    return f"{v:.{d}f}".replace(".", ",")

# --------------------------------------------------------------- dati d'esame
# Esercizio 1 - modello base (n = 72)
B_AGE, SE_AGE = -0.0179855, 0.0190728
B_DEROG, SE_DEROG = 0.163679, 0.033544
# Esercizio 1 - modello con dummy di istruzione (HC1)
D1, SE_D1 = -2.66015, 0.218020
D2, SE_D2 = -1.17185, 0.174619
# Esercizio 1 - modello quadratico (HC1)
B_INC, SE_INC = 0.233526, 0.144316
B_SQ, SE_SQ = -0.0203474, 0.007891
VIF = {"derog": 1.079, "ownrent": 1.223, "D2": 2.938, "D1": 3.403,
       "sq_income": 14.457, "income": 15.174}
# Esercizio 2
ADF = {"Futures": (-0.0348454, 0.0377242), "Spot": (-0.0375759, 0.0485303)}
ADF_CRIT = -2.38
# T_ECM: osservazioni del modello ECM (2002:04-2007:07).
# T_FULL: campione completo (feb 2002 - lug 2007), usato da gretl per le bande dei
#   correlogrammi di entrambe le figure d'esame: la misura in pixel sul PDF d'esame
#   da' 0,2409 (p. 6) e 0,2404 (p. 8), cioe' 1,96/sqrt(66) = 0,2413 e non 0,245.
T = T_ECM = 64
T_FULL = 66
B_DFUT, SE_DFUT = 1.04948, 0.0529448
LAM, SE_LAM = -0.51197, 0.124091

# autocorrelazioni lette dalle figure del testo (griglia 0,005)
ACF_LP = [0.010, -0.270, 0.025, 0.080, -0.050, 0.040, -0.170, -0.260, 0.015,
          0.200, -0.060, -0.030, 0.025, -0.020, 0.190, 0.150, -0.150, -0.025,
          0.080, 0.000]
PACF_LP = [0.010, -0.270, 0.040, 0.005, -0.035, 0.090, -0.230, -0.240, -0.065,
           0.065, -0.035, 0.025, -0.015, -0.060, 0.160, 0.040, -0.015, 0.060,
           -0.015, 0.005]
ACF_ECM = [0.390, 0.355, 0.175, 0.215, 0.110, 0.130, 0.160, -0.010, 0.020,
           -0.070, -0.040, -0.140, -0.050, -0.255, -0.220, -0.270, -0.060,
           -0.110, -0.120, -0.190]
# PACF_ECM[1] = 0,240: e' il valore misurato sul grafico d'esame ed e' anche quello
# imposto da Yule-Walker, (rho2 - rho1^2)/(1 - rho1^2) = 0,2393.
PACF_ECM = [0.390, 0.240, -0.030, 0.100, -0.020, 0.030, 0.130, -0.160, -0.005,
            -0.090, -0.005, -0.070, 0.030, -0.220, -0.080, -0.050, 0.210,
            -0.050, -0.070, -0.190]
BAND = 1.96 / np.sqrt(T_FULL)


def ci_plot(ax, est, lo, hi, *, label, mark, marklab, markcol, xlabel, title, dec=4,
            markha="center"):
    """Intervallo al 95% su retta numerica con un solo valore di confronto."""
    ax.hlines(0, lo, hi, color=es.BLUE, lw=5, alpha=0.5, label=label)
    for v in (lo, hi):
        ax.vlines(v, -0.16, 0.16, color=es.BLUE, lw=1.6)
        ax.annotate(it(v, dec), xy=(v, -0.20), ha="center", va="top", fontsize=8.5,
                    color=es.BLUE)
    ax.plot([est], [0], "o", color=es.BLUE, ms=7, zorder=5)
    ax.annotate("stima " + it(est, dec), xy=(est, 0.20), ha="center", va="bottom",
                fontsize=9, color=es.BLUE, fontweight="bold")
    ax.plot([mark], [0], "D", color=markcol, ms=8, zorder=6)
    ax.annotate(marklab, xy=(mark, -0.62), ha=markha, va="top", fontsize=8.5,
                color=markcol, fontweight="bold")
    pad = 0.18 * (hi - lo)
    ax.set_xlim(min(lo, mark) - pad, max(hi, mark) + pad)
    ax.set_ylim(-1.15, 0.75)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel(xlabel)
    ax.set_title(title, loc="left")
    ax.legend(loc="upper right")


def tidy_corrgm(axes, band, legend_kw=None):
    """Virgola decimale nell'etichetta della banda e tacche intere sui ritardi."""
    lab = "$\\pm " + f"{band:.3f}".replace(".", "{,}") + "$"
    for ax in axes:
        for art in ax.get_children():
            g = getattr(art, "get_label", None)
            if g is not None and isinstance(g(), str) and g().startswith("$\\pm"):
                art.set_label(lab)
        ax.legend(**(legend_kw or {}).get(ax, {"loc": "upper right"}))
    axes[-1].set_xticks([1, 5, 10, 15, 20])


# ============================================================ D1 - età, IC 95%
def d01():
    lo, hi = B_AGE - 1.96 * SE_AGE, B_AGE + 1.96 * SE_AGE
    fig, ax = plt.subplots(figsize=(6.3, 2.2))
    ci_plot(ax, B_AGE, lo, hi, label="IC 95% per $\\beta_3$", mark=-0.02,
            marklab="$-0{,}02$ (nell'intervallo)", markcol=es.AMBER,
            xlabel="coefficiente di age", dec=4,
            title="$5\\beta_3 = -0{,}10$ equivale a $\\beta_3 = -0{,}02$")
    fig.tight_layout()
    es.save(fig, OUT / "d01-eta-intervallo.pdf")


# ================================================= D2 - derog, test unilaterale
def d02():
    t = (B_DEROG - 0.025) / SE_DEROG
    fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.0))
    es.dist_test("z", stat=t, crit=1.64, tail="left", ax=axes[0], xlim=(-9, 6),
                 title="a) $H_0:\\ \\beta_2 \\geq 0{,}025$ contro $H_1:\\ \\beta_2 < 0{,}025$",
                 statlabel="statistica osservata = " + it(t, 3),
                 critlabel="regione di rifiuto: $z$ < $-1{,}64$")
    lo, hi = B_DEROG - 1.96 * SE_DEROG, B_DEROG + 1.96 * SE_DEROG
    ci_plot(axes[1], B_DEROG, lo, hi, label="IC 95% per $\\beta_2$", mark=0.025,
            marklab="$0{,}025$ (a sinistra dell'intervallo)", markcol=es.GREEN,
            xlabel="coefficiente di derog", dec=4, markha="left",
            title="b) la soglia sta fuori dall'intervallo, a sinistra")
    fig.tight_layout()
    es.save(fig, OUT / "d02-derog-test.pdf")


# =================================================== D3 - dummy titolo di studio
def d03():
    fig, ax = plt.subplots(figsize=(6.3, 2.5))
    labs = ["$\\delta_1$  (elementare/media)", "$\\delta_2$  (diploma)"]
    ypos = [1, 0]
    for y, v, s in zip(ypos, [D1, D2], [SE_D1, SE_D2]):
        ax.hlines(y, v - 1.96 * s, v + 1.96 * s, color=es.BLUE, lw=4, alpha=0.55)
        ax.plot([v], [y], "o", color=es.BLUE, ms=6)
        ax.annotate(it(v), xy=(v, y + 0.16), ha="center", fontsize=8.5,
                    color=es.BLUE, fontweight="bold")
    ax.axvline(0, color=es.RED, ls="--", lw=1.2)
    ax.annotate("$\\delta_j = 0$", xy=(0, 1.42), ha="center", fontsize=8.5, color=es.RED)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labs, fontsize=8.5)
    ax.set_xlim(-3.3, 0.55)
    ax.set_ylim(-0.6, 1.7)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel("scarto rispetto ai laureati (categoria omessa)")
    ax.set_title("IC 95% dei due coefficienti dummy", loc="left")
    fig.tight_layout()
    es.save(fig, OUT / "d03-istruzione.pdf")


# ========================================== D4 - quadratica, effetto marginale
def d04():
    fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.2))
    es.dist_test("z", stat=B_SQ / SE_SQ, crit=1.96, tail="two", ax=axes[0],
                 title="a) la non linearità si testa su $H_0:\\ \\beta_5 = 0$",
                 statlabel="statistica osservata = " + it(B_SQ / SE_SQ, 3),
                 critlabel="regione di rifiuto: $|z|$ > 1,96")
    _, ax, turn = es.quadratic_effect(B_INC, B_SQ, xmin=0.0, xmax=10.0, ax=axes[1],
                                      varname="income",
                                      title="b) effetto marginale del reddito e punto di svolta",
                                      ylabel="$\\beta_1 + 2\\beta_5\\,\\mathrm{income}$")
    ax.set_xlabel("income (decine di migliaia di dollari)")
    ax.annotate("cioè 57.385 dollari l'anno", xy=(turn, 0),
                xytext=(-8, -22), textcoords="offset points", ha="right",
                fontsize=8.5, color=es.RED)
    fig.tight_layout()
    es.save(fig, OUT / "d04-quadratica.pdf")


# ================================================================== D5 - VIF
def d05():
    fig, ax = plt.subplots(figsize=(6.3, 3.0))
    names = list(VIF)
    y = np.arange(len(names))
    cols = [es.RED if VIF[n] > 10 else es.GRAY for n in names]
    ax.barh(y, [VIF[n] for n in names], color=cols, alpha=0.85, height=0.6)
    for yy, n in zip(y, names):
        lab = it(VIF[n], 3)
        if VIF[n] > 10:
            lab += "   errore std. $\\times$ " + it(np.sqrt(VIF[n]), 2)
        ax.annotate(lab, xy=(VIF[n], yy), xytext=(4, 0), textcoords="offset points",
                    va="center", fontsize=8.5, color=es.INK, fontweight="bold")
    ax.axvline(10, color=es.RED, ls="--", lw=1.2)
    ax.annotate("soglia 10", xy=(10, -0.75), xytext=(-4, 0), textcoords="offset points",
                ha="right", va="center", fontsize=8.5, color=es.RED)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8.5)
    ax.set_xlim(0, 27)
    ax.set_ylim(-1.1, len(names) - 0.4)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel("VIF")
    ax.set_title("L'errore standard cresce di $\\sqrt{\\mathrm{VIF}}$", loc="left")
    fig.tight_layout()
    es.save(fig, OUT / "d05-vif.pdf")


# ================================================================== D6 - ADF
def d06():
    fig, ax = plt.subplots(figsize=(6.3, 2.7))
    lo, hi = -3.4, 0.6
    ax.axvspan(lo, ADF_CRIT, color=es.RED, alpha=0.22,
               label="regione di rifiuto (unilaterale sinistra): $t$ < $-2{,}38$")
    ax.axvline(ADF_CRIT, color=es.RED, ls="--", lw=1.2)
    ax.annotate("valore critico dato\ndal testo: $-2{,}38$", xy=(ADF_CRIT, 0.40),
                xytext=(7, 0), textcoords="offset points", ha="left", va="center",
                fontsize=8.5, color=es.RED, fontweight="bold")
    for (name, (c, s)), y, col in zip(ADF.items(), (0.66, 0.36), (es.BLUE, es.TEAL)):
        t = c / s
        ax.plot([t], [y], "o", color=col, ms=9, zorder=6)
        ax.annotate(f"{name}:  $t$ = " + it(t, 4), xy=(t, y), xytext=(10, 0),
                    textcoords="offset points", va="center", fontsize=9,
                    color=col, fontweight="bold")
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel("statistica ADF  $t = \\hat\\delta\\,/\\,\\mathrm{se}(\\hat\\delta)$")
    ax.set_title("Entrambe le statistiche cadono fuori dalla regione di rifiuto",
                 loc="left")
    ax.legend(loc="upper right")
    fig.tight_layout()
    es.save(fig, OUT / "d06-adf.pdf")


# ================================================ D7 - ACF/PACF lungo periodo
def d07():
    fig, axes = es.acf_pacf(ACF_LP, PACF_LP, n=T_FULL,
                            title="Residui della relazione di lungo periodo: nessuna persistenza")
    axes[0].annotate("$\\hat\\rho_1 \\approx 0{,}01$: nessuna memoria al primo ritardo",
                     xy=(1, 0.01), xytext=(2.6, 0.29), fontsize=8.5, color=es.GREEN,
                     arrowprops=dict(arrowstyle="->", color=es.GREEN, lw=0.9))
    for lag in (2, 8):
        axes[0].annotate(f"ritardo {lag}", xy=(lag, 0.0), xytext=(0, 7),
                         textcoords="offset points", ha="center",
                         fontsize=8, color=es.RED)
    tidy_corrgm(axes, BAND)
    fig.tight_layout()
    es.save(fig, OUT / "d07-acf-lungo-periodo.pdf")


# ====================================================== D8 - coefficienti ECM
def d08():
    lo, hi = LAM - 1.96 * SE_LAM, LAM + 1.96 * SE_LAM
    fig, ax = plt.subplots(figsize=(6.3, 2.2))
    ci_plot(ax, LAM, lo, hi, label="IC 95% per $\\lambda$ (HAC)", mark=0.0,
            marklab="$0$ (fuori dall'intervallo)", markcol=es.RED,
            xlabel="coefficiente del termine di correzione",
            title="Il coefficiente di correzione è negativo e significativo")
    fig.tight_layout()
    es.save(fig, OUT / "d08-ecm-coefficienti.pdf")


# ================================================== D9 - ACF/PACF residui ECM
def d09():
    fig, axes = es.acf_pacf(ACF_ECM, PACF_ECM, n=T_FULL,
                            title="Residui del modello ECM: autocorrelazione ai primi ritardi")
    tidy_corrgm(axes, BAND)
    fig.tight_layout()
    es.save(fig, OUT / "d09-acf-ecm.pdf")


# ======================================================= D10 - assorbimento
def d10():
    fig, ax, table = es.decay(LAM, horizon=10, targets=(0.8,),
                              title="Quota di disequilibrio ancora presente dopo $h$ mesi")
    ax.set_xlabel("mesi dopo il disequilibrio ($h$)")
    phi = 1 + LAM
    for h in (1, 2, 3):
        ax.annotate(it(phi ** h, 4), xy=(h, phi ** h), xytext=(-8, -7),
                    textcoords="offset points", ha="right", va="top", fontsize=8,
                    color=es.GRAY)
    ax.annotate("assorbito dopo 1, 2, 3 mesi:\n51,2%, 76,2%, 88,4%",
                xy=(0.40, 0.70), xycoords="axes fraction", fontsize=8.5,
                color=es.INK)
    fig.tight_layout()
    es.save(fig, OUT / "d10-assorbimento.pdf")
    print("  h* (80%):", table)


if __name__ == "__main__":
    for f in (d01, d02, d03, d04, d05, d06, d07, d08, d09, d10):
        f()
