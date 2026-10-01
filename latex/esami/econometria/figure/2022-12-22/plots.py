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
from scipy import stats
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


def ljung_box(rho, T, j):
    return T * (T + 2) * sum(r ** 2 / (T - i - 1) for i, r in enumerate(rho[:j]))


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


# ============================================================ D1 - eta', IC 95%
def d01():
    est = 5 * B_AGE
    se = 5 * SE_AGE
    lo, hi = est - 1.96 * se, est + 1.96 * se
    fig, axes = plt.subplots(2, 1, figsize=(6.3, 3.9))
    es.ci_line(est, lo, hi, h0=-0.10, ax=axes[0], decimals=4,
               label="IC 95% per $5\\beta_3$",
               title="a) scala logaritmica: intervallo per $5\\,\\beta_3$",
               xlabel="variazione di $\\log(\\mathrm{expend})$ per $+5$ anni di eta'")
    axes[0].plot([np.log(0.90)], [0], "s", color=es.TEAL, ms=6, zorder=7)
    axes[0].annotate("soglia esatta  log(0,90) = " + it(np.log(0.9)),
                     xy=(np.log(0.9), 0.58), xytext=(-4, 0), textcoords="offset points",
                     ha="right", va="center", fontsize=8, color=es.TEAL)
    axes[0].plot([0.0], [0], "s", color=es.GRAY, ms=6, zorder=7)
    axes[0].annotate("nessun effetto", xy=(0.0, 0.30), xytext=(6, 0),
                     textcoords="offset points", ha="left", va="center",
                     fontsize=8, color=es.GRAY)

    ax = axes[1]
    plo, phi_ = 100 * (np.exp(lo) - 1), 100 * (np.exp(hi) - 1)
    pest = 100 * (np.exp(est) - 1)
    ax.hlines(0, plo, phi_, color=es.BLUE, lw=5, alpha=0.5,
              label="stesso intervallo, in variazione percentuale esatta")
    for v in (plo, phi_):
        ax.vlines(v, -0.16, 0.16, color=es.BLUE, lw=1.6)
        ax.annotate(it(v, 2) + "%", xy=(v, -0.22), ha="center", va="top",
                    fontsize=8.5, color=es.BLUE)
    ax.plot([pest], [0], "o", color=es.BLUE, ms=7, zorder=5)
    ax.annotate("stima " + it(pest, 2) + "%", xy=(pest, 0.22), ha="center",
                va="bottom", fontsize=9, color=es.BLUE, fontweight="bold")
    ax.plot([-10.0], [0], "D", color=es.AMBER, ms=8, zorder=6)
    ax.annotate("$-10\\%$ ipotizzato\n(nell'intervallo)", xy=(-10.0, -0.26),
                ha="center", va="top", fontsize=8.5, color=es.AMBER, fontweight="bold")
    ax.set_xlim(plo - 4, phi_ + 4)
    ax.set_ylim(-0.95, 0.75)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel("variazione percentuale della spesa attesa")
    ax.set_title("b) stessa conclusione sulla scala percentuale", loc="left")
    ax.legend(loc="upper right")
    fig.tight_layout()
    es.save(fig, OUT / "d01-eta-intervallo.pdf")


# ================================================= D2 - derog, test unilaterale
def d02():
    th, se = 2 * B_DEROG, 2 * SE_DEROG
    t_app = (th - 0.05) / se
    t_ex = (th - np.log(1.05)) / se
    fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.0))
    es.dist_test("z", stat=t_app, crit=1.64, tail="right", ax=axes[0],
                 title="a) $H_0:\\ 2\\beta_2 = 0{,}05$ contro $H_1:\\ 2\\beta_2 > 0{,}05$",
                 statlabel="statistica osservata = " + it(t_app, 3),
                 critlabel="regione di rifiuto: $z$ > 1,64 (valore critico dato dal testo)")
    ax = axes[1]
    lo, hi = th - 1.96 * se, th + 1.96 * se
    ax.hlines(0, lo, hi, color=es.BLUE, lw=5, alpha=0.5, label="IC 95% per $2\\beta_2$")
    for v in (lo, hi):
        ax.vlines(v, -0.16, 0.16, color=es.BLUE, lw=1.6)
        ax.annotate(it(v), xy=(v, -0.20), ha="center", va="top", fontsize=8.5,
                    color=es.BLUE)
    ax.plot([th], [0], "o", color=es.BLUE, ms=7, zorder=5)
    ax.annotate("stima " + it(th) + "   (+" + it(100 * (np.exp(th) - 1), 2) + "%)",
                xy=(th, 0.20), ha="center", va="bottom", fontsize=9,
                color=es.BLUE, fontweight="bold")
    ax.plot([0.05], [0], "D", color=es.RED, ms=8, zorder=6)
    ax.plot([np.log(1.05)], [0], "D", color=es.AMBER, ms=8, zorder=7)
    ax.annotate("soglie del $5\\%$: 0,0500 (approssimata)\n"
                "e log(1,05) = 0,0488 (esatta)\n"
                "entrambe fuori dall'intervallo", xy=(0.05, -0.62), ha="left",
                va="top", fontsize=8.5, color=es.RED, fontweight="bold")
    ax.set_xlim(-0.02, hi + 0.06)
    ax.set_ylim(-1.45, 0.75)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel("effetto di due segnalazioni negative su $\\log(\\mathrm{expend})$")
    ax.set_title("b) le due soglie cadono entrambe fuori dall'intervallo", loc="left")
    ax.legend(loc="upper right")
    fig.tight_layout()
    es.save(fig, OUT / "d02-derog-test.pdf")


# =================================================== D3 - dummy titolo di studio
def d03():
    fig, axd = plt.subplot_mosaic([["a", "b"], ["c", "c"]], figsize=(6.4, 5.4),
                                  height_ratios=[1.0, 1.05])
    ax = axd["a"]
    labs = ["$\\delta_1$  (elementare/media)", "$\\delta_2$  (diploma)"]
    vals = [D1, D2]
    ses = [SE_D1, SE_D2]
    ypos = [1, 0]
    for y, v, s in zip(ypos, vals, ses):
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
    ax.set_xlabel("scarto rispetto ai laureati (categoria base)")
    ax.set_title("a) IC 95% dei due coefficienti dummy", loc="left")

    ax = axd["b"]
    cats = ["elementare/\nmedia", "diploma", "laurea\n(base)"]
    rel = [100 * np.exp(D1), 100 * np.exp(D2), 100.0]
    cols = [es.RED, es.AMBER, es.GREEN]
    bars = ax.bar(cats, rel, color=cols, alpha=0.85, width=0.62)
    for b, v in zip(bars, rel):
        ax.annotate(it(v, 2), xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, 3),
                    textcoords="offset points", ha="center", fontsize=8.5,
                    fontweight="bold", color=es.INK)
    ax.set_ylim(0, 118)
    ax.set_ylabel("spesa attesa, laureati = 100")
    es.commas(ax, "y")
    ax.set_title("b) livelli relativi $e^{\\delta_j}$", loc="left")

    es.dist_test("F", (2, 65), crit=stats.f.ppf(0.95, 2, 65), tail="right",
                 ax=axd["c"], xlim=(0, 8),
                 title="c) regione di rifiuto del test proposto  $H_0:\\ \\delta_1 = \\delta_2 = 0$",
                 critlabel="regione di rifiuto al 5%: $F$ > 3,138")
    axd["c"].annotate("il testo non riporta la statistica $F$ osservata:\n"
                      "qui si mostra solo la regola di decisione",
                      xy=(0.42, 0.52), xycoords="axes fraction", fontsize=8.5,
                      color=es.GRAY, ha="left")
    fig.tight_layout()
    es.save(fig, OUT / "d03-istruzione.pdf")


# ========================================== D4 - quadratica, effetto marginale
def d04():
    fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.2))
    es.dist_test("z", stat=B_SQ / SE_SQ, crit=1.96, tail="two", ax=axes[0],
                 title="a) la non linearita' si testa su $H_0:\\ \\beta_{sq} = 0$",
                 statlabel="statistica osservata = " + it(B_SQ / SE_SQ, 3),
                 critlabel="regione di rifiuto: $|z|$ > 1,96")
    _, ax, turn = es.quadratic_effect(B_INC, B_SQ, xmin=0.0, xmax=10.0, ax=axes[1],
                                      varname="income",
                                      title="b) effetto marginale del reddito e punto di svolta",
                                      ylabel="$\\partial\\,\\log(\\mathrm{expend})/\\partial\\,\\mathrm{income}$")
    ax.set_xlabel("income (decine di migliaia di dollari)")
    ax.annotate("cioe' 57.385 dollari l'anno", xy=(turn, 0),
                xytext=(10, -26), textcoords="offset points",
                fontsize=8.5, color=es.RED)
    fig.tight_layout()
    es.save(fig, OUT / "d04-quadratica.pdf")


# ================================================================== D5 - VIF
def d05():
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 3.3), width_ratios=[1.35, 1.0])
    ax = axes[0]
    names = list(VIF)
    vals = [VIF[n] for n in names]
    roots = [np.sqrt(v) for v in vals]
    y = np.arange(len(names))
    cols = [es.RED if v >= 10 else es.GRAY for v in vals]
    ax.barh(y, roots, color=cols, alpha=0.85, height=0.6)
    for yy, r, v in zip(y, roots, vals):
        ax.annotate(it(r, 3) + "x", xy=(r, yy), xytext=(4, 0),
                    textcoords="offset points", va="center", fontsize=8.5,
                    color=es.INK, fontweight="bold")
    ax.axvline(1.0, color=es.GREEN, ls="--", lw=1.2)
    ax.annotate("1 = caso ideale, regressori ortogonali", xy=(1.0, -1.05),
                xytext=(5, 0), textcoords="offset points", fontsize=8,
                va="center", color=es.GREEN)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8.5)
    ax.set_xlim(0, 4.9)
    ax.set_ylim(-1.5, len(names) - 0.4)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel("fattore di inflazione dell'errore standard, $\\sqrt{\\mathrm{VIF}_j}$")
    ax.set_title("a) l'errore standard cresce di $\\sqrt{\\mathrm{VIF}}$, non di VIF", loc="left")

    ax = axes[1]
    se_orth = SE_INC / np.sqrt(VIF["income"])
    ax.bar(["ortogonale\n(ipotetico)", "osservato\n(VIF = 15,174)"],
           [se_orth, SE_INC], color=[es.GREEN, es.RED], alpha=0.85, width=0.58)
    for i, v in enumerate([se_orth, SE_INC]):
        ax.annotate(it(v, 5), xy=(i, v), xytext=(0, 3), textcoords="offset points",
                    ha="center", fontsize=8.5, fontweight="bold", color=es.INK)
    ax.annotate("$t$ = " + it(B_INC / se_orth, 2), xy=(0, se_orth / 2), ha="center",
                fontsize=9, color="white", fontweight="bold")
    ax.annotate("$t$ = " + it(B_INC / SE_INC, 2), xy=(1, SE_INC / 2), ha="center",
                fontsize=9, color="white", fontweight="bold")
    ax.set_ylim(0, SE_INC * 1.30)
    ax.annotate("valore ipotetico indicativo:\nse HC1 diviso per $\\sqrt{\\mathrm{VIF}}$",
                xy=(0.02, 0.985), xycoords="axes fraction", ha="left", va="top",
                fontsize=7.4, color=es.GRAY)
    es.commas(ax, "y")
    ax.set_ylabel("errore standard di $\\hat\\beta_{income}$")
    ax.set_title("b) che cosa costa la collinearita'", loc="left")
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
    ax.axvline(-2.85, color=es.GRAY, ls=":", lw=1.1)
    ax.annotate("$-2{,}85$\n(DF con drift,\nvalore del corso)", xy=(-2.85, 0.16),
                xytext=(-6, 0), textcoords="offset points", ha="right", va="bottom",
                fontsize=8, color=es.GRAY)
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
                     xy=(1, 0.01), xytext=(1.6, 0.20), fontsize=8.5, color=es.GREEN,
                     arrowprops=dict(arrowstyle="->", color=es.GREEN, lw=0.9))
    for lag in (2, 8):
        axes[0].annotate(f"ritardo {lag}", xy=(lag, 0.0), xytext=(0, 7),
                         textcoords="offset points", ha="center",
                         fontsize=8, color=es.RED)
    q = ljung_box(ACF_LP, T_FULL, 8)
    axes[0].annotate("Ljung-Box $Q(8)$ = " + it(q, 3) + "  <  " +
                     it(stats.chi2.ppf(0.95, 8), 3) + "  (p = " +
                     it(1 - stats.chi2.cdf(q, 8), 3) + ")",
                     xy=(0.02, 0.06), xycoords="axes fraction", fontsize=8.5,
                     color=es.GREEN)
    tidy_corrgm(axes, BAND)
    fig.tight_layout()
    es.save(fig, OUT / "d07-acf-lungo-periodo.pdf")


# ====================================================== D8 - coefficienti ECM
def d08():
    fig, axes = plt.subplots(2, 1, figsize=(6.3, 3.9))
    es.ci_line(B_DFUT, B_DFUT - 1.96 * SE_DFUT, B_DFUT + 1.96 * SE_DFUT, h0=1.0,
               ax=axes[0], decimals=4, label="IC 95% per $\\beta$ (HAC)",
               title="a) effetto di breve periodo: $\\beta$ non e' distinguibile da 1",
               xlabel="coefficiente di $\\Delta \\mathrm{futures}_t$")
    es.ci_line(LAM, LAM - 1.96 * SE_LAM, LAM + 1.96 * SE_LAM, h0=0.0,
               ax=axes[1], decimals=4, label="IC 95% per $\\lambda$ (HAC)",
               title="b) coefficiente di correzione: negativo, significativo, dentro $(-1,0)$",
               xlabel="coefficiente di $(\\mathrm{spot}_{t-1} - a - b\\,\\mathrm{futures}_{t-1})$",
               extra=[(-1.0, "$\\lambda = -1$ (rientro immediato)", es.TEAL)])
    axes[1].axvspan(-1.0, 0.0, color=es.GREENBG, zorder=0)
    axes[1].set_xlim(-1.08, 0.12)
    fig.tight_layout()
    es.save(fig, OUT / "d08-ecm-coefficienti.pdf")


# ================================================== D9 - ACF/PACF residui ECM
def d09():
    fig, axes = es.acf_pacf(ACF_ECM, PACF_ECM, n=T_FULL,
                            title="Residui del modello ECM: persistenza positiva, PACF che rientra dopo il primo ritardo")
    h = np.arange(1, 21)
    axes[0].plot(h, 0.39 ** h, ls="--", lw=1.1, color=es.AMBER,
                 label="decadimento geometrico $0{,}39^{\\,h}$ (AR(1) di confronto)")
    q = ljung_box(ACF_ECM, T_ECM, 8)
    axes[0].annotate("Ljung-Box $Q(8)$ = " + it(q, 3) + "  >  " +
                     it(stats.chi2.ppf(0.95, 8), 3) + "  (p = " +
                     it(1 - stats.chi2.cdf(q, 8), 5) + ")",
                     xy=(0.02, 0.05), xycoords="axes fraction", fontsize=8.5,
                     color=es.RED)
    axes[1].annotate("un picco netto, il secondo sul bordo: AR(1)-AR(2) nei residui",
                     xy=(0.17, 0.04), xycoords="axes fraction", fontsize=8.5,
                     color=es.RED)
    tidy_corrgm(axes, BAND, {axes[0]: {"loc": "upper right", "fontsize": 7.6}})
    fig.tight_layout()
    es.save(fig, OUT / "d09-acf-ecm.pdf")


# ======================================================= D10 - assorbimento
def d10():
    fig, ax, table = es.decay(LAM, horizon=10, targets=(0.5, 0.8),
                              title="Quota di disequilibrio ancora presente dopo $h$ mesi")
    ax.set_xlabel("mesi dopo lo shock ($h$)")
    phi = 1 + LAM
    for h in (1, 2, 3):
        ax.annotate(it(phi ** h, 4), xy=(h, phi ** h), xytext=(-8, -7),
                    textcoords="offset points", ha="right", va="top", fontsize=8,
                    color=es.GRAY)
    ax.annotate("dopo 2 mesi resta il 23,82%: non basta\n"
                "dopo 3 mesi resta l'11,62%: assorbito l'88,38%",
                xy=(0.40, 0.70), xycoords="axes fraction", fontsize=8.5,
                color=es.INK)
    fig.tight_layout()
    es.save(fig, OUT / "d10-assorbimento.pdf")
    print("  h* (50%, 80%):", table)


if __name__ == "__main__":
    for f in (d01, d02, d03, d04, d05, d06, d07, d08, d09, d10):
        f()
