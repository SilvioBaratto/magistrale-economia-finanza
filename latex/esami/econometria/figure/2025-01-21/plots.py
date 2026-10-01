#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 21 gennaio 2025.

Ogni figura visualizza l'inferenza di una singola domanda. I valori provengono
dagli output di regressione riportati nel testo d'esame; dove un numero e' stato
letto a occhio da una figura gretl del testo (Figura 1 p. 4, Figura 2 p. 7) la
cosa e' dichiarata nel commento e nella didascalia del markdown.

    python3 figure/2025-01-21/plots.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
from scipy import stats
es.use()
OUT = pathlib.Path(__file__).resolve().parent

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

SEED = 20250121


def it(v, d=4):
    """Numero in formato italiano (virgola decimale)."""
    return f"{v:.{d}f}".replace(".", ",")


# ====================================================================== dati
# Esercizio 1 -- log(prezzo) su crime, log(nox), rooms, 4 dummy di zona, n = 506
N1, K1 = 506, 7
DF1 = N1 - K1                      # 499: nessuna intercetta, k = 7 regressori
B_CRIME, SE_CRIME = -0.0127792, 0.00248715
B_NOX,   SE_NOX   = -0.0281161, 0.00823410
B_ROOMS, SE_ROOMS = 0.0549082, 0.0215226
ZONE = {                            # delta_j, se(delta_j)
    "zona1": (12.1767, 0.137561),
    "zona2": (11.8342, 0.132916),
    "zona3": (12.7239, 0.169741),
    "zona4": (12.4352, 0.151612),
}
COV_12 = 0.0181234                 # Cov(delta1, delta2), FORNITA dal testo

# Esercizio 2 -- price / invpc USA, annuali 1947-1988
T2 = 42
ADF = {"log(pcinv)": -3.3283, "log(price)": -3.7029}
ADF_P = {"log(pcinv)": 0.001, "log(price)": 0.022}
EG_P = 0.0267
LAM = -0.503193                    # coefficiente di correzione dell'errore


# ================================================== D1 -- soglia del 30% su 2*rooms
def d01():
    th, se = 2 * B_ROOMS, 2 * SE_ROOMS
    c_app, c_ex = 0.30, np.log(1.30)
    t_app, t_ex = (th - c_app) / se, (th - c_ex) / se
    zc = stats.norm.ppf(0.95)

    fig, axes = plt.subplots(2, 1, figsize=(6.1, 5.4))

    # (a) densita' nulla, regione di rifiuto a destra, le due statistiche
    ax = axes[0]
    x = np.linspace(-5.6, 3.4, 900)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color=es.BLUE, lw=1.4, label="densità $N(0,1)$")
    ax.fill_between(x, y, color=es.BLUEBG)
    m = x >= zc
    ax.fill_between(x[m], y[m], color=es.RED, alpha=0.30,
                    label="rifiuto: $t$ > " + it(zc, 3))
    ax.axvline(zc, color=es.RED, ls="--", lw=1.0)
    # Le due statistiche cadono nella coda sinistra, proprio dove sta la legenda:
    # si fermano sotto il riquadro invece di attraversarlo.
    ytop = stats.norm.pdf(0) * 1.62
    hstat = 0.52 * ytop
    ax.vlines(t_app, 0, hstat, color=es.GREEN, lw=2.0,
              label="soglia 0,30:  $t$ = " + it(t_app, 3))
    ax.vlines(t_ex, 0, hstat, color=es.AMBER, lw=2.0,
              label="soglia log(1,30):  $t$ = " + it(t_ex, 3))
    ax.set_ylim(0, ytop)
    ax.set_yticks([]); ax.set_ylabel("densità")
    ax.set_xlabel("valore della statistica")
    ax.set_title("(a) $H_0$: $2\\beta_3$ = soglia  contro  $H_1$: $2\\beta_3$ > soglia",
                 loc="left")
    es.commas(ax, "x")
    ax.legend(loc="upper left", fontsize=8.5)

    # (b) intervallo di confidenza sull'effetto di due stanze
    lo, hi = th - 1.96 * se, th + 1.96 * se
    es.ci_line(th, lo, hi, h0=c_app, ax=axes[1], decimals=4,
               xlabel="variazione di log(prezzo) per due stanze in più  ($2\\beta_3$)",
               title="(b) IC al 95% su $2\\beta_3$: nessuna delle due soglie è contenuta",
               extra=[(c_ex, "log(1,30) = " + it(c_ex, 4), es.AMBER)])
    axes[1].set_xlim(-0.02, 0.34)
    fig.tight_layout()
    es.save(fig, OUT / "d01-soglia-due-stanze.pdf")


# ============================== D2 -- perche' nessuna dummy e' stata eliminata
def d02():
    # 6,1 pollici: nel documento la figura e' ridotta a 0,86 della giustezza,
    # quindi una tela piu' stretta tiene i caratteri sopra i 7 pt effettivi.
    fig, axes = plt.subplots(1, 2, figsize=(6.1, 3.25),
                             gridspec_kw={"width_ratios": [1.05, 1.0]})

    # (a) schema della matrice di disegno: le 4 dummy sommano alla costante
    ax = axes[0]
    ax.set_axis_off()
    rows = [("area A", [1, 0, 0, 0]), ("area B", [0, 1, 0, 0]),
            ("area C", [0, 0, 1, 0]), ("area D", [0, 0, 0, 1])]
    cols = ["zona1", "zona2", "zona3", "zona4"]
    x0, y0, w, h = 0.12, 0.88, 0.165, 0.105
    for j, c in enumerate(cols):
        ax.text(x0 + (j + 0.5) * w, y0 + 0.5 * h + 0.035, c, ha="center",
                va="bottom", fontsize=8, color=es.GRAY, rotation=0)
    ax.text(x0 + 4.72 * w, y0 + 0.5 * h + 0.035, "somma", ha="center",
            va="bottom", fontsize=8, color=es.RED)
    for i, (lab, r) in enumerate(rows):
        yy = y0 - i * h
        ax.text(x0 - 0.02, yy, lab, ha="right", va="center", fontsize=8,
                color=es.GRAY)
        for j, v in enumerate(r):
            ax.add_patch(Rectangle((x0 + j * w, yy - h / 2), w * 0.92, h * 0.86,
                                   facecolor=es.BLUEBG if v else "white",
                                   edgecolor=es.RULE, lw=0.6))
            ax.text(x0 + (j + 0.46) * w, yy, str(v), ha="center", va="center",
                    fontsize=9, color=es.BLUE if v else es.GRAY)
        ax.add_patch(Rectangle((x0 + 4.3 * w, yy - h / 2), w * 0.92, h * 0.86,
                               facecolor=es.REDBG, edgecolor=es.RED, lw=0.8))
        ax.text(x0 + 4.76 * w, yy, "1", ha="center", va="center", fontsize=9,
                color=es.RED, fontweight="bold")
    ax.text(0.5, 0.20,
            "zona1+zona2+zona3+zona4 $\\equiv$ 1:\n"
            "la somma delle dummy È la colonna\ndella costante "
            "$\\Rightarrow$ collinearità perfetta.\n"
            "Si toglie una dummy OPPURE l'intercetta:\n"
            "qui è stata tolta l'intercetta.",
            ha="center", va="center", fontsize=8.2, color=es.INK,
            bbox=dict(boxstyle="round,pad=0.45", facecolor=es.GREENBG,
                      edgecolor=es.GREEN, lw=0.7))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title("(a) la trappola delle dummy", loc="left")

    # (b) i quattro livelli medi stimati, con IC al 95%
    ax = axes[1]
    names = list(ZONE)
    est = np.array([ZONE[z][0] for z in names])
    se = np.array([ZONE[z][1] for z in names])
    ypos = np.arange(len(names))[::-1]
    ax.errorbar(est, ypos, xerr=1.96 * se, fmt="o", color=es.BLUE, ms=6,
                capsize=4, lw=1.4, label="stima $\\pm$ 1,96 s.e.")
    for e, s, y in zip(est, se, ypos):
        ax.annotate(it(e, 4), xy=(e, y), xytext=(0, 9), textcoords="offset points",
                    ha="center", fontsize=8, color=es.BLUE)
    ax.set_yticks(ypos); ax.set_yticklabels(names)
    ax.set_xlabel("livello medio di log(prezzo) della zona  ($\\hat\\delta_j$)")
    ax.set_title("(b) nessun coefficiente è un differenziale:\n"
                 "ognuno è il LIVELLO della propria zona", loc="left", fontsize=9)
    ax.set_ylim(-0.7, len(names) - 0.3)
    es.commas(ax, "x", decimals=1)
    ax.legend(loc="lower left", fontsize=8)
    fig.tight_layout()
    es.save(fig, OUT / "d02-dummy-senza-intercetta.pdf")


# ================================================ D3 -- elasticita' dell'inquinamento
def d03():
    lo, hi = B_NOX - 1.96 * SE_NOX, B_NOX + 1.96 * SE_NOX
    fig, axes = plt.subplots(1, 2, figsize=(6.1, 3.2))

    # (a) %Delta prezzo in funzione di %Delta nox: regola esatta e approssimata
    ax = axes[0]
    g = np.linspace(0, 400, 700)                     # %Delta nox

    def esatto(beta):
        return 100 * (np.exp(beta * np.log(1 + g / 100)) - 1)

    ax.fill_between(g, esatto(lo), esatto(hi), color=es.BLUEBG,
                    label="banda IC 95%")
    # La legenda a quattro voci copriva la curva esatta e la sua banda: resta a
    # legenda la sola banda, le due regole e la soglia sono annotate sul posto.
    ax.plot(g, esatto(B_NOX), color=es.BLUE, lw=1.7)
    ax.plot(g, B_NOX * g, "--", color=es.AMBER, lw=1.4)
    ax.axhline(-10, color=es.RED, ls="--", lw=1.2)
    ax.axvline(5, color=es.TEAL, ls=":", lw=1.2)
    ax.annotate("+5% di nox:\n$-$0,137%", xy=(5, -0.137), xytext=(18, 8),
                textcoords="offset points", ha="left", va="bottom",
                fontsize=8.2, color=es.TEAL,
                arrowprops=dict(arrowstyle="->", color=es.TEAL, lw=0.9))
    ax.annotate("riduzione ipotizzata del 10%", xy=(8, -10), xytext=(0, 5),
                textcoords="offset points", ha="left", va="bottom",
                fontsize=8.2, color=es.RED)
    need_app = -10 / B_NOX
    ax.plot([need_app], [-10], "o", color=es.AMBER, ms=6, zorder=6)
    ax.annotate("regola approssimata:\nservirebbe +" + it(need_app, 0) + "%",
                xy=(need_app, -10), xytext=(-8, -5), textcoords="offset points",
                ha="right", va="top", fontsize=8.2, color=es.AMBER,
                fontweight="bold")
    ax.annotate("regola esatta:\nservirebbe +4141%", xy=(360, esatto(B_NOX)[-70]),
                xytext=(-6, 28), textcoords="offset points", ha="right",
                va="bottom", fontsize=8.2, color=es.BLUE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.BLUE, lw=0.9))
    ax.set_xlabel("variazione percentuale di nox  ($g$)")
    ax.set_ylabel("variazione percentuale del prezzo")
    ax.set_ylim(-13.4, 3.8)
    ax.set_yticks(np.arange(-12, 3, 2))
    es.commas(ax)
    ax.legend(loc="upper right", fontsize=8.2)
    ax.set_title("(a) elasticità costante: nessuna delle\ndue regole arriva a $-$10%",
                 loc="left", fontsize=9)

    # (b) ordine di grandezza dell'effetto di un +5%, scala logaritmica
    ax = axes[1]
    vals = [abs(100 * (np.exp(b * np.log(1.05)) - 1)) for b in (hi, B_NOX, lo)]
    ypos = [2.6, 1.6, 0.6]
    ax.barh(ypos, vals, height=0.52, color=[es.RULE, es.BLUE, es.RULE],
            edgecolor=es.BLUE, lw=0.8)
    ax.barh([-0.8], [10.0], height=0.52, color=es.REDBG, edgecolor=es.RED, lw=1.0)
    for y, v in zip(ypos, vals):
        ax.annotate(it(v, 3) + "%", xy=(v, y), xytext=(5, 0),
                    textcoords="offset points", ha="left", va="center",
                    fontsize=8.2, color=es.INK)
    ax.annotate("10% ipotizzato", xy=(10, -0.8), xytext=(-8, 0),
                textcoords="offset points", ha="right", va="center", fontsize=8.4,
                color=es.RED, fontweight="bold")
    ax.annotate("fattore " + it(10 / vals[1], 0) + "$\\times$",
                xy=(1.0, 0.0), ha="center", va="center", fontsize=9.5,
                color=es.RED, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                          edgecolor=es.RED, lw=0.8))
    ax.set_yticks(ypos + [-0.8])
    ax.set_yticklabels(["IC sup.", "stima", "IC inf.", "ipotesi"])
    ax.set_xscale("log")
    ax.set_xlim(0.03, 30)
    ax.set_xticks([0.1, 0.5, 1, 5, 10])          # senza 0,05: le etichette si toccavano
    ax.set_xticklabels(["0,1", "0,5", "1", "5", "10"])
    ax.set_xlabel("|%$\\Delta$ prezzo| per un +5% di nox  (scala log)")
    ax.set_title("(b) due ordini di grandezza\ndi distanza", loc="left", fontsize=9)
    ax.set_ylim(-1.5, 3.3)
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    es.save(fig, OUT / "d03-elasticita-nox.pdf")


# ============================== D4 -- differenziale Zona1/Zona2 e ruolo della covarianza
def d04():
    d1, s1 = ZONE["zona1"]
    d2, s2 = ZONE["zona2"]
    th = d1 - d2
    V = s1**2 + s2**2 - 2 * COV_12
    se = np.sqrt(V)
    se_bad = np.sqrt(s1**2 + s2**2)          # errore: Cov posta a zero

    fig, axes = plt.subplots(2, 1, figsize=(6.1, 5.1),
                             gridspec_kw={"height_ratios": [1.0, 1.05]})

    # (a) la varianza termine per termine
    ax = axes[0]
    parts = [s1**2, s2**2, -2 * COV_12]
    labs = ["$\\mathrm{Var}(\\hat\\delta_1)$", "$\\mathrm{Var}(\\hat\\delta_2)$",
            "$-2\\mathrm{Cov}(\\hat\\delta_1,\\hat\\delta_2)$"]
    cols = [es.BLUE, es.TEAL, es.RED]
    cum = 0.0
    for p, l, c in zip(parts, labs, cols):
        ax.bar([l], [p], bottom=[cum if p > 0 else cum + p], color=c, alpha=0.75,
               edgecolor=c, lw=0.8, width=0.55)
        ax.annotate(it(p, 6), xy=(l, cum + p / 2), ha="center", va="center",
                    fontsize=8, color="white" if abs(p) > 0.01 else es.INK,
                    fontweight="bold")
        cum += p
    ax.bar(["totale"], [V], color=es.GREEN, edgecolor=es.GREEN, lw=0.9, width=0.55)
    ax.annotate(it(V, 6) + "\n(invisibile a questa scala)",
                xy=("totale", V), xytext=(0, 8),
                textcoords="offset points", ha="center", fontsize=8.5,
                color=es.GREEN, fontweight="bold")
    ax.axhline(0, color=es.GRAY, lw=0.8)
    ax.set_ylabel("contributo alla varianza")
    ax.set_title("(a) $\\mathrm{Var}(\\hat\\delta_1-\\hat\\delta_2)$: la covarianza cancella "
                 "quasi tutto  ($\\rho$ = " + it(COV_12 / (s1 * s2), 4) + ")",
                 loc="left", fontsize=9.3)
    es.commas(ax, "y", decimals=3)
    ax.grid(axis="x", visible=False)

    # (b) IC corretto contro IC sbagliato
    ax = axes[1]
    for y, s, col, lab in ((0.30, se, es.BLUE, "IC corretto (con $\\mathrm{Cov}$)"),
                           (-0.30, se_bad, es.RED,
                            "IC sbagliato ($\\mathrm{Cov}$ posta a 0)")):
        lo, hi = th - 1.96 * s, th + 1.96 * s
        ax.hlines(y, lo, hi, color=col, lw=6, alpha=0.45, label=lab)
        for v in (lo, hi):
            ax.vlines(v, y - 0.08, y + 0.08, color=col, lw=1.5)
            ax.annotate(it(v, 4), xy=(v, y - 0.11),
                        ha="right" if v < th else "left", va="top",
                        fontsize=8, color=col)
        ax.plot([th], [y], "o", color=col, ms=7, zorder=5)
    ax.axvline(0, color=es.AMBER, ls="--", lw=1.4)
    ax.annotate("$H_0$: $\\delta_1-\\delta_2$ = 0", xy=(0, 0.62), ha="center",
                va="bottom", fontsize=9, color=es.AMBER, fontweight="bold")
    ax.annotate("stima " + it(th, 4), xy=(th, 0.46), ha="center", va="bottom",
                fontsize=9, color=es.INK, fontweight="bold")
    ax.annotate("$t$ = " + it(th / se, 2) + ": rifiuto", xy=(th + 1.96 * se, 0.30),
                xytext=(10, 0), textcoords="offset points", va="center",
                fontsize=8.5, color=es.BLUE)
    ax.annotate("$t$ = " + it(th / se_bad, 2) + ": NON rifiuto",
                xy=(th + 1.96 * se_bad, -0.30), xytext=(10, 0),
                textcoords="offset points", va="center", fontsize=8.5, color=es.RED)
    ax.set_xlim(-0.22, 1.28)
    ax.set_ylim(-0.95, 0.95)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("differenziale di log(prezzo) fra Zona 1 e Zona 2")
    ax.set_title("(b) ignorare la covarianza ribalta la conclusione", loc="left")
    es.commas(ax, "x", decimals=2)
    ax.legend(loc="lower right", fontsize=8)
    fig.tight_layout()
    es.save(fig, OUT / "d04-differenziale-zone.pdf")


# =================================== D5 -- "la zona non conta": 3 restrizioni, test F
def d05():
    names = list(ZONE)
    est = np.array([ZONE[z][0] for z in names])
    se = np.array([ZONE[z][1] for z in names])
    lower = (est[0] - est[1]) / np.sqrt(ZONE["zona1"][1]**2 + ZONE["zona2"][1]**2
                                        - 2 * COV_12)
    fcrit = stats.f.ppf(0.95, 3, DF1)

    fig, axes = plt.subplots(1, 2, figsize=(6.2, 3.2),
                             gridspec_kw={"width_ratios": [1.15, 1.0]})

    # (a) modello completo (4 livelli) contro modello ristretto (1 livello)
    ax = axes[0]
    xs = np.arange(4)
    ax.errorbar(xs, est, yerr=1.96 * se, fmt="o", color=es.BLUE, ms=6, capsize=4,
                lw=1.4, label="modello completo: $\\hat\\delta_1,\\dots,\\hat\\delta_4$")
    ax.axhline(est.mean(), color=es.RED, ls="--", lw=1.4,
               label="livello comune ipotetico")
    for i in range(3):
        ax.annotate("", xy=(i + 1, est[i + 1]), xytext=(i, est[i]),
                    arrowprops=dict(arrowstyle="<->", color=es.AMBER, lw=1.1))
        ax.annotate(f"$r_{i+1}$", xy=(i + 0.5, (est[i] + est[i + 1]) / 2),
                    xytext=(0, 6), textcoords="offset points", ha="center",
                    fontsize=8.5, color=es.AMBER, fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(names)
    ax.set_ylabel("livello medio di log(prezzo)")
    ax.set_title("(a) le tre restrizioni indipendenti  $s$ = 3", loc="left")
    es.commas(ax, "y", decimals=1)
    # La legenda in basso a destra finiva sotto la barra d'errore di zona2:
    # si apre una fascia libera sotto il dato piu' basso (11,574) e la si sposta li'.
    ax.set_ylim(11.18, 13.16)
    ax.legend(loc="lower left", fontsize=8.2)

    # (b) densita' F(3, 499) con regione di rifiuto
    ax = axes[1]
    x = np.linspace(0.001, 8, 700)
    y = stats.f.pdf(x, 3, DF1)
    ax.plot(x, y, color=es.BLUE, lw=1.4, label="densità $F_{3,499}$")
    ax.fill_between(x, y, color=es.BLUEBG)
    m = x >= fcrit
    ax.fill_between(x[m], y[m], color=es.RED, alpha=0.30,
                    label="rifiuto: $F$ > " + it(fcrit, 3))
    ax.axvline(fcrit, color=es.RED, ls="--", lw=1.0)
    ax.annotate("$F^{oss}$ non calcolabile:\nil testo non dà $R^2_c$ né $R^2_r$.\n"
                "Ma la D4 rifiuta già $r_1$\ncon $t$ = " + it(lower, 2),
                xy=(7.6, stats.f.pdf(7.6, 3, DF1)), xytext=(-6, 58),
                textcoords="offset points", ha="right", fontsize=8.2, color=es.GREEN,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.GREEN, lw=1.0))
    ax.set_xlabel("valore della statistica $F$")
    ax.set_ylabel("densità"); ax.set_yticks([])
    ax.set_ylim(0, stats.f.pdf(x, 3, DF1).max() * 1.15)
    ax.set_title("(b) test $F$ unilaterale destro", loc="left")
    es.commas(ax, "x", decimals=0)
    ax.legend(loc="upper right", fontsize=8.2)
    fig.tight_layout()
    es.save(fig, OUT / "d05-zona-rilevanza.pdf")


# ============================ D6 -- eteroschedasticita': la nube della Figura 1
def d06():
    # Estremi dei residui letti A OCCHIO dalla Figura 1 del testo (p. 4):
    # per ciascuna fascia di valori predetti, (min, max) approssimati.
    bands = [(10.85, 11.35, -0.27, 0.66),
             (11.45, 11.75, -0.72, 0.42),
             (11.75, 12.10, -0.81, 0.42),
             (12.10, 12.45, -0.25, 0.41),
             (12.55, 12.75, -0.11, 0.38),
             (12.85, 13.08, -0.26, 0.29)]
    fig, axes = plt.subplots(1, 2, figsize=(6.1, 3.0), sharey=True)

    ax = axes[0]
    for a, b, lo, hi in bands:
        c = 0.5 * (a + b)
        ax.add_patch(Rectangle((a, lo), b - a, hi - lo, facecolor=es.BLUEBG,
                               edgecolor=es.BLUE, lw=0.9, alpha=0.9))
        ax.plot([c, c], [lo, hi], color=es.BLUE, lw=1.2)
        ax.annotate(it(hi - lo, 2), xy=(c, hi), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.2,
                    color=es.BLUE)
    ax.axhline(0, color=es.GRAY, ls=":", lw=1.0)
    ax.set_xlabel("valori predetti $\\hat{y}$")
    ax.set_ylabel("residui $\\hat\\epsilon$")
    ax.set_title("(a) escursione letta dalla Figura 1 (p. 4)", loc="left", fontsize=9)
    es.commas(ax)

    ax = axes[1]
    rng = np.random.default_rng(SEED)
    xs = rng.uniform(10.85, 13.08, 460)
    ax.plot(xs, rng.normal(0, 0.155, xs.size), "o", ms=3.2, mfc="none",
            mec=es.GREEN, mew=0.8, alpha=0.75)
    ax.axhline(0, color=es.GRAY, ls=":", lw=1.0)
    for s in (-1.96, 1.96):
        ax.axhline(s * 0.155, color=es.GREEN, ls="--", lw=1.0)
    ax.set_xlabel("valori predetti $\\hat{y}$")
    ax.set_title("(b) come apparirebbe sotto omoschedasticità\n"
                 "(simulazione illustrativa, seme " + str(SEED) + ")",
                 loc="left", fontsize=9)
    ax.set_ylim(-0.9, 0.78)
    es.commas(ax)
    fig.tight_layout()
    es.save(fig, OUT / "d06-residui-eteroschedasticita.pdf")


# ================== D7 -- ADF: le due statistiche e la deterministica che le spiega
def d07():
    # p-value ASINTOTICI di MacKinnon (superficie di risposta, N = 1): non dipendono
    # da T. Calcolati una volta con statsmodels.tsa.adfvalues.mackinnonp e incorporati
    # qui (statsmodels non e' fra le dipendenze di build.py).
    PV = {"senza costante": {-3.3283: 0.00089, -3.7029: 0.00023},
          "con costante":   {-3.3283: 0.01366, -3.7029: 0.00407},
          "cost. + trend":  {-3.3283: 0.06173, -3.7029: 0.02217}}
    CRIT = {"senza costante": -1.95, "con costante": -2.85, "cost. + trend": -3.52}
    # basi diverse: i primi due sono i critici asintotici del corso, il terzo e'
    # il critico MacKinnon a campione finito per T = 42 (asintotico: -3,41).
    BASE = {"senza costante": "asint.", "con costante": "asint.", "cost. + trend": "T = 42"}

    fig, axes = plt.subplots(2, 1, figsize=(6.2, 5.2),
                             gridspec_kw={"height_ratios": [0.85, 1.15]})

    # (a) le due statistiche sulla retta dei valori critici DF
    ax = axes[0]
    for (spec, c), col in zip(CRIT.items(), (es.GRAY, es.AMBER, es.RED)):
        ax.vlines(c, 0.62, 1.30, color=col, ls="--", lw=1.2)
        ax.annotate(spec + "\n" + it(c, 2) + "\n(" + BASE[spec] + ")",
                    xy=(c, 1.34), ha="center", va="bottom",
                    fontsize=7.8, color=col)
    for y, (name, st) in zip((0.18, -0.34), ADF.items()):
        ax.plot([st], [y], "o", color=es.BLUE, ms=9, zorder=6)
        ax.annotate(name + " = " + it(st, 4) + "   (p dichiarato = "
                    + it(ADF_P[name], 3) + ")", xy=(st, y), xytext=(13, 0),
                    textcoords="offset points", ha="left", va="center",
                    fontsize=8.4, color=es.BLUE, fontweight="bold")
    ax.annotate("", xy=(-4.45, -0.92), xytext=(-1.15, -0.92),
                arrowprops=dict(arrowstyle="<-", color=es.RED, lw=1.2))
    ax.text(-2.8, -1.10, "più negativo $\\Rightarrow$ si rifiuta la radice unitaria",
            ha="center", va="top", fontsize=8.2, color=es.RED)
    ax.set_xlim(-4.75, -0.95); ax.set_ylim(-1.55, 2.25)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("statistica ADF")
    ax.set_title("(a) unilaterale SINISTRO, tavole non standard", loc="left")
    es.commas(ax, "x", decimals=1)

    # (b) quale specificazione riproduce i p-value dichiarati
    ax = axes[1]
    specs = list(PV)
    w, xs = 0.36, np.arange(len(specs))
    for i, (name, st) in enumerate(ADF.items()):
        vals = [PV[s][st] for s in specs]
        bars = ax.bar(xs + (i - 0.5) * w, vals, width=w,
                      color=[es.BLUE, es.TEAL][i], alpha=0.8,
                      edgecolor=[es.BLUE, es.TEAL][i], lw=0.8, label=name)
        for b, v, s in zip(bars, vals, specs):
            hit = abs(v - ADF_P[name]) < 0.0015
            ax.annotate(it(v, 4) + ("  = dichiarato" if hit else ""),
                        xy=(b.get_x() + b.get_width() / 2, v),
                        xytext=(0, 12 if hit else 4),
                        textcoords="offset points", ha="center", fontsize=7.8,
                        color=es.GREEN if hit else es.GRAY,
                        fontweight="bold" if hit else "normal")
            if hit:
                b.set_edgecolor(es.GREEN); b.set_linewidth(1.8)
    ax.axhline(0.05, color=es.RED, ls="--", lw=1.1)
    ax.annotate("5%", xy=(len(specs) - 0.55, 0.05), xytext=(0, 3),
                textcoords="offset points", fontsize=8, color=es.RED)
    ax.set_xticks(xs); ax.set_xticklabels(specs)
    ax.set_ylabel("p-value asintotico di MacKinnon")
    ax.set_ylim(0, 0.085)
    ax.set_title("(b) i p-value dichiarati non sono invertiti:\n"
                 "vengono da DUE deterministiche diverse", loc="left", fontsize=9.3)
    es.commas(ax, "y", decimals=2)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left", fontsize=8)
    fig.tight_layout()
    es.save(fig, OUT / "d07-adf-specificazioni.pdf")


# ======================= D8 -- Engle-Granger: la procedura in tre passi e il 2,67%
def d08():
    fig, axes = plt.subplots(2, 1, figsize=(6.2, 5.0),
                             gridspec_kw={"height_ratios": [1.15, 0.85]})

    # (a) i tre passi, con l'esito di ciascuno
    ax = axes[0]
    ax.set_axis_off()
    steps = [
        ("Passo 1", "ADF sulle serie:\nNON si deve rifiutare $H_0$",
         "p = 0,001 e 0,022 $<$ 0,05\n$\\Rightarrow$ si RIFIUTA: serie I(0)", False),
        ("Passo 2", "OLS di lungo periodo\n$\\log(invpc)=\\alpha+\\beta\\log(price)$",
         "$\\hat\\beta$ = 3,87863\n(stima superconsistente solo se I(1))", None),
        ("Passo 3", "Engle-Granger sui residui:\nSI deve rifiutare $H_0$",
         "p = 2,67% $<$ 5%\n$\\Rightarrow$ si rifiuta", True),
    ]
    for i, (tag, what, res, ok) in enumerate(steps):
        y = 0.80 - i * 0.345
        col = {True: es.GREEN, False: es.RED, None: es.GRAY}[ok]
        bg = {True: es.GREENBG, False: es.REDBG, None: "#F1F3F5"}[ok]
        ax.text(0.035, y, tag, fontsize=9, color=col, fontweight="bold",
                va="center")
        ax.text(0.155, y, what, fontsize=8.3, color=es.INK, va="center",
                bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
                          edgecolor=es.RULE, lw=0.7))
        ax.text(0.60, y, res, fontsize=8.3, color=col, va="center",
                bbox=dict(boxstyle="round,pad=0.35", facecolor=bg,
                          edgecolor=col, lw=0.9))
        if i < 2:
            ax.annotate("", xy=(0.10, y - 0.17), xytext=(0.10, y - 0.10),
                        arrowprops=dict(arrowstyle="->", color=es.GRAY, lw=1.1))
    ax.text(0.5, -0.16,
            "Preso alla lettera l'output della D7 il Passo 1 fallisce, e la "
            "cointegrazione\nrichiede ENTRAMBE le condizioni: il 2,67% del Passo 3 "
            "non certifica nulla.",
            ha="center", va="center", fontsize=8.4, color=es.RED,
            bbox=dict(boxstyle="round,pad=0.4", facecolor=es.REDBG,
                      edgecolor=es.RED, lw=0.8))
    ax.set_xlim(0, 1); ax.set_ylim(-0.32, 1.0)
    ax.set_title("(a) la procedura del corso in tre passi", loc="left")

    # (b) dove cade il p-value di Engle-Granger
    ax = axes[1]
    ax.axhspan(0, 1, xmin=0, xmax=0.01 / 0.10, color=es.REDBG, alpha=0.9)
    ax.axvline(0.01, color=es.RED, ls="--", lw=1.2)
    ax.axvline(0.05, color=es.AMBER, ls="--", lw=1.2)
    ax.annotate("1%", xy=(0.01, 1.03), ha="center", va="bottom", fontsize=8.5,
                color=es.RED)
    ax.annotate("5%", xy=(0.05, 1.03), ha="center", va="bottom", fontsize=8.5,
                color=es.AMBER)
    ax.plot([EG_P], [0.5], "D", color=es.GREEN, ms=11, zorder=6)
    ax.annotate("Engle-Granger: p = " + it(100 * EG_P, 2) + "%",
                xy=(EG_P, 0.5), xytext=(0, -26), textcoords="offset points",
                ha="center", fontsize=9, color=es.GREEN, fontweight="bold")
    ax.annotate("si rifiuta al 5%,\nNON all'1%", xy=(EG_P, 0.5),
                xytext=(14, 22), textcoords="offset points", fontsize=8.2,
                color=es.GRAY)
    ax.set_xlim(0, 0.10); ax.set_ylim(0, 1.0)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("p-value asintotico del test $\\tau_c(2)$ sui residui")
    ax.set_title("(b) evidenza al 5%, ma non robusta all'1%", loc="left")
    es.commas(ax, "x", decimals=2)
    fig.tight_layout()
    es.save(fig, OUT / "d08-engle-granger.pdf")


# ==================================== D9 -- ECM: assorbimento del 75% del disequilibrio
def d09():
    fig, ax, table = es.decay(
        LAM, horizon=8, targets=(0.5, 0.75),
        title="Quota di disequilibrio ancora presente dopo $h$ anni: "
              "$(1+\\hat\\lambda)^h$")
    for h, dx in ((1, -4), (2, -4)):
        v = (1 + LAM) ** h
        ax.annotate(it(100 * (1 - v), 1) + "% assorbito", xy=(h, v),
                    xytext=(dx, -26), textcoords="offset points",
                    ha="right" if dx < 0 else "left", fontsize=7.8,
                    color=es.GRAY)
    # la legenda di es.decay compone "0, 4968" in mathtext: la riscriviamo in testo
    ax.legend(ax.get_legend_handles_labels()[0],
              ["quota residua $(1+\\hat\\lambda)^h$ = 0,496807$^h$"],
              loc="upper right")
    ax.annotate("$h^\\star$ = ln(0,25)/ln(0,496807) = " + it(
        np.log(0.25) / np.log(1 + LAM), 4) + " $\\rightarrow$ 2 anni",
        xy=(2, (1 + LAM) ** 2), xytext=(46, 52), textcoords="offset points",
        fontsize=8.6, color=es.RED, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.0))
    ax.set_xlabel("anni dopo lo shock ($h$) — dati annuali 1947–1988")
    print("   h* :", table)
    es.save(fig, OUT / "d09-ecm-assorbimento.pdf")


# =============== D10 -- ACF e PACF letti dalla Figura 2, e la firma che ne esce
def d10():
    # Valori misurati sui pixel della Figura 2 del testo (p. 7), 25 ritardi,
    # calibrando sulle bande +-1,96/sqrt(42) = +-0,3024. Nessuna barra dell'ACF
    # esce dalla banda INFERIORE: la coda negativa si ferma a circa -0,29.
    acf = [0.89, 0.81, 0.70, 0.63, 0.56, 0.49, 0.42, 0.33, 0.25, 0.18, 0.12,
           0.06, 0.02, -0.02, -0.08, -0.13, -0.17, -0.20, -0.23, -0.28, -0.28,
           -0.29, -0.28, -0.28, -0.29]
    pacf = [0.89, 0.03, -0.11, 0.07, 0.01, -0.09, 0.00, -0.14, -0.04, 0.02,
            -0.02, -0.07, 0.05, -0.06, -0.13, 0.02, -0.01, -0.02, -0.03, -0.14,
            0.11, 0.05, 0.01, -0.13, -0.07]

    fig, axes = plt.subplots(2, 1, figsize=(6.2, 4.6), sharex=True)
    es.acf_pacf(acf, pacf, n=T2, axes=axes,
                labels=("ACF letta dalla Figura 2", "PACF letta dalla Figura 2"))
    # Benchmark corretto: NON l'ACF teorica 0,89^j, ma il valore ATTESO dell'ACF
    # CAMPIONARIA di un AR(1) stazionario con phi = 0,89 su T = 42 osservazioni
    # (media di 80.000 repliche simulate). E' molto piu' bassa dell'ACF teorica e
    # passa in negativo da sola: il confronto con 0,89^j non discrimina nulla.
    acf_att = [0.76, 0.58, 0.42, 0.30, 0.20, 0.12, 0.05, 0.00, -0.04, -0.07,
               -0.09, -0.11, -0.13, -0.14, -0.15, -0.15, -0.15, -0.15, -0.15,
               -0.14, -0.14, -0.14, -0.13, -0.12, -0.12]
    lags = np.arange(1, len(acf) + 1)
    axes[0].plot(lags, acf_att, "--", color=es.AMBER, lw=1.3,
                 label="ACF attesa, AR(1) staz. $\\phi$ = 0,89, $T$ = 42")
    axes[0].axhline(0, color=es.GRAY, lw=0.8)
    axes[0].annotate("8 ritardi fuori banda,\ntutti SOPRA l'attesa",
                     xy=(6, 0.49), xytext=(34, 26), textcoords="offset points",
                     fontsize=8.2, color=es.RED, fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.0))
    axes[0].legend(loc="lower left", fontsize=7.4)
    axes[1].annotate("un solo picco, $\\approx$ 0,89:\n$p$ = 1 e $\\phi$ vicino a 1",
                     xy=(1, 0.89), xytext=(34, -14), textcoords="offset points",
                     fontsize=8.2, color=es.RED, fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.0))
    axes[1].set_xlabel("ritardo (bande $\\pm$1,96/$\\sqrt{42}$ = $\\pm$0,3024)")
    fig.tight_layout()
    es.save(fig, OUT / "d10-acf-pacf-lprice.pdf")


if __name__ == "__main__":
    for f in (d01, d02, d03, d04, d05, d06, d07, d08, d09, d10):
        f()
    print("fatto.")
