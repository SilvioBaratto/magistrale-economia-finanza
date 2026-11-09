#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 21 gennaio 2025.

Ogni figura visualizza la decisione di una singola domanda. I valori provengono
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


def it(v, d=4):
    """Numero in formato italiano (virgola decimale)."""
    return f"{v:.{d}f}".replace(".", ",")


# ====================================================================== dati
# Esercizio 1 -- log(prezzo) su crime, log(nox), rooms, 4 dummy di zona, n = 506
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
    lo, hi = B_ROOMS - 1.96 * SE_ROOMS, B_ROOMS + 1.96 * SE_ROOMS   # IC 95% su beta3

    fig, ax = plt.subplots(figsize=(6.1, 1.95))
    es.ci_line(B_ROOMS, lo, hi, ax=ax, decimals=4,
               xlabel="coefficiente $\\beta_3$ di rooms  (la soglia è $0{,}15$, cioè $2\\beta_3 = 0{,}30$)",
               title="IC al 95% su $\\beta_3$: $0{,}15$ è completamente a destra dell'intervallo")
    # L'etichetta automatica di ci_line ragiona da test bilaterale ("fuori: rifiuto"),
    # ma qui H0 è unilaterale (beta3 <= 0,15) e NON si rifiuta: la soglia si marca a mano.
    ax.plot([0.15], [0], "D", color=es.AMBER, ms=8, zorder=6)
    ax.annotate("soglia $0{,}15$\n(a destra dell'IC: non si rifiuta $H_0$)", xy=(0.15, -0.26),
                ha="center", va="top", fontsize=8.5, color=es.AMBER, fontweight="bold")
    pad = 0.12 * (hi - lo)
    ax.set_xlim(lo - pad, 0.15 + 3 * pad)
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
    ax.set_title("(a) quattro dummy e la costante", loc="left")

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
    ax.set_xlabel("intercetta specifica della zona  ($\\hat\\delta_j$)")
    ax.set_title("(b) nessun coefficiente è un differenziale:\n"
                 "ognuno è l'INTERCETTA della propria zona", loc="left", fontsize=9)
    ax.set_ylim(-0.7, len(names) - 0.3)
    es.commas(ax, "x", decimals=1)
    ax.legend(loc="lower left", fontsize=8)
    fig.tight_layout()
    es.save(fig, OUT / "d02-dummy-senza-intercetta.pdf")


# ================================================ D3 -- elasticita' dell'inquinamento
def d03():
    lo, hi = B_NOX - 1.96 * SE_NOX, B_NOX + 1.96 * SE_NOX
    fig, ax = plt.subplots(figsize=(6.1, 3.1))
    g = np.linspace(0, 6, 100)                       # variazione % di nox

    ax.fill_between(g, lo * g, hi * g, color=es.BLUEBG, label="IC 95% di $\\beta_2$")
    ax.plot(g, B_NOX * g, color=es.BLUE, lw=1.7,
            label="stima: $\\hat\\beta_2$ = $-$0,0281")
    ax.plot(g, -2 * g, "--", color=es.RED, lw=1.4,
            label="elasticità necessaria: $-$2")
    ax.axvline(5, color=es.TEAL, ls=":", lw=1.2)
    ax.plot([5], [B_NOX * 5], "o", color=es.BLUE, ms=6, zorder=6)
    ax.plot([5], [-10], "o", color=es.RED, ms=6, zorder=6)
    ax.annotate("$-$0,14%", xy=(5, B_NOX * 5), xytext=(-8, -16),
                textcoords="offset points", ha="right", fontsize=8.5,
                color=es.BLUE, fontweight="bold")
    ax.annotate("$-$10%", xy=(5, -10), xytext=(-8, 0), textcoords="offset points",
                ha="right", va="center", fontsize=8.5, color=es.RED,
                fontweight="bold")
    ax.set_xlabel("variazione percentuale di nox")
    ax.set_ylabel("variazione percentuale del prezzo")
    ax.set_xlim(0, 6)
    ax.set_ylim(-12.5, 1.5)
    es.commas(ax)
    ax.legend(loc="lower left", fontsize=8.2)
    fig.tight_layout()
    es.save(fig, OUT / "d03-elasticita-nox.pdf")


# ============================== D4 -- differenziale Zona1/Zona2 con la covarianza fornita
def d04():
    d1, s1 = ZONE["zona1"]
    d2, s2 = ZONE["zona2"]
    th = d1 - d2
    se = np.sqrt(s1**2 + s2**2 - 2 * COV_12)

    fig, ax = plt.subplots(figsize=(6.1, 1.95))
    es.ci_line(100 * th, 100 * (th - 1.96 * se), 100 * (th + 1.96 * se), h0=0.0,
               ax=ax, decimals=2, unit="%",
               xlabel="differenziale di prezzo Zona 1 $-$ Zona 2  "
                      "($100\\,(\\delta_1-\\delta_2)$)",
               title="IC al 95% su $\\delta_1-\\delta_2$: lo zero non cade nell'intervallo")
    fig.tight_layout()
    es.save(fig, OUT / "d04-differenziale-zone.pdf")


# =================================== D5 -- "la zona non conta": 3 restrizioni
def d05():
    names = list(ZONE)
    est = np.array([ZONE[z][0] for z in names])
    se = np.array([ZONE[z][1] for z in names])

    fig, ax = plt.subplots(figsize=(5.4, 3.1))
    xs = np.arange(4)
    ax.errorbar(xs, est, yerr=1.96 * se, fmt="o", color=es.BLUE, ms=6, capsize=4,
                lw=1.4, label="stima $\\pm$ 1,96 s.e.")
    for i in range(3):
        ax.annotate("", xy=(i + 1, est[i + 1]), xytext=(i, est[i]),
                    arrowprops=dict(arrowstyle="<->", color=es.AMBER, lw=1.1))
        ax.annotate(f"$r_{i+1}$", xy=(i + 0.5, (est[i] + est[i + 1]) / 2),
                    xytext=(0, 6), textcoords="offset points", ha="center",
                    fontsize=8.5, color=es.AMBER, fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(names)
    ax.set_ylabel("livello medio di log(prezzo)")
    ax.set_title("tre restrizioni $r_1$, $r_2$, $r_3$: $\\delta_1=\\delta_2=\\delta_3=\\delta_4$",
                 loc="left", fontsize=9.3)
    es.commas(ax, "y", decimals=1)
    # Fascia libera sotto il dato piu' basso (11,574) per la legenda.
    ax.set_ylim(11.18, 13.16)
    ax.legend(loc="lower left", fontsize=8.2)
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
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    for a, b, lo, hi in bands:
        c = 0.5 * (a + b)
        ax.add_patch(Rectangle((a, lo), b - a, hi - lo, facecolor=es.BLUEBG,
                               edgecolor=es.BLUE, lw=0.9, alpha=0.9))
        ax.plot([c, c], [lo, hi], color=es.BLUE, lw=1.2)
        ax.annotate(it(hi - lo, 2), xy=(c, hi), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.2,
                    color=es.BLUE)
    ax.axhline(0, color=es.GRAY, ls=":", lw=1.0)
    ax.set_xlim(10.7, 13.2)
    ax.set_ylim(-0.95, 0.85)
    ax.set_xlabel("valori predetti $\\hat{y}$")
    ax.set_ylabel("residui $\\hat\\epsilon$")
    ax.set_title("escursione dei residui per fascia di $\\hat y$ (dalla Figura 1)",
                 loc="left", fontsize=9.3)
    es.commas(ax)
    fig.tight_layout()
    es.save(fig, OUT / "d06-residui-eteroschedasticita.pdf")


# ================== D7 -- ADF: p-value dichiarati contro il 5%
def d07():
    fig, ax = plt.subplots(figsize=(6.1, 2.4))
    names = list(ADF)
    ypos = np.arange(len(names))[::-1]
    for y, name, col in zip(ypos, names, (es.BLUE, es.TEAL)):
        p = ADF_P[name]
        ax.barh(y, p, height=0.5, color=col, alpha=0.8, edgecolor=col, lw=0.8)
        ax.text(0.057, y, "ADF = " + it(ADF[name], 4) + ",  p = " + it(p, 3),
                ha="left", va="center", fontsize=8.4, color=es.INK)
    ax.axvline(0.05, color=es.RED, ls="--", lw=1.2)
    ax.annotate("5%", xy=(0.05, len(names) - 0.45), xytext=(4, 0),
                textcoords="offset points", fontsize=8.5, color=es.RED)
    ax.set_yticks(ypos); ax.set_yticklabels(names)
    ax.set_xlim(0, 0.12)
    ax.set_ylim(-0.6, len(names) - 0.35)
    ax.set_xlabel("p-value del test ADF ($H_0$: radice unitaria)")
    ax.set_title("entrambi i p-value sono sotto il 5%: si rifiuta $H_0$", loc="left")
    es.commas(ax, "x", decimals=2)
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    es.save(fig, OUT / "d07-adf-specificazioni.pdf")


# ======================= D8 -- Engle-Granger: il p-value del 2,67% contro il 5%
def d08():
    fig, ax = plt.subplots(figsize=(6.1, 1.95))
    ax.axhspan(0, 1, xmin=0, xmax=0.05 / 0.10, color=es.GREENBG, alpha=0.9)
    ax.axvline(0.05, color=es.RED, ls="--", lw=1.2)
    ax.annotate("5%", xy=(0.05, 1.03), ha="center", va="bottom", fontsize=8.5,
                color=es.RED)
    ax.annotate("si rifiuta $H_0$", xy=(0.002, 0.88), ha="left", va="top",
                fontsize=8.2, color=es.GRAY)
    ax.plot([EG_P], [0.5], "D", color=es.GREEN, ms=11, zorder=6)
    ax.annotate("Engle-Granger: p = " + it(100 * EG_P, 2) + "%",
                xy=(EG_P, 0.5), xytext=(0, -26), textcoords="offset points",
                ha="center", fontsize=9, color=es.GREEN, fontweight="bold")
    ax.set_xlim(0, 0.10); ax.set_ylim(0, 1.0)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("p-value del test sui residui ($H_0$: radice unitaria)")
    ax.set_title("p-value sotto il 5%: i residui sono stazionari", loc="left")
    es.commas(ax, "x", decimals=2)
    fig.tight_layout()
    es.save(fig, OUT / "d08-engle-granger.pdf")


# ==================================== D9 -- ECM: assorbimento cumulato del disequilibrio
def d09():
    phi = 1 + LAM
    labels = ["subito", "dopo 1\nperiodo", "dopo 2\nperiodi", "dopo 3\nperiodi"]
    cum = [100 * (1 - phi ** (k + 1)) for k in range(len(labels))]
    fig, ax = plt.subplots(figsize=(6.1, 3.0))
    bars = ax.bar(labels, cum, width=0.55, color=es.BLUE, alpha=0.8,
                  edgecolor=es.BLUE, lw=0.8)
    for b, v in zip(bars, cum):
        ax.annotate(it(v, 1) + "%", xy=(b.get_x() + b.get_width() / 2, v),
                    xytext=(0, 4), textcoords="offset points", ha="center",
                    fontsize=8.6, color=es.INK, fontweight="bold")
    ax.axhline(75, color=es.RED, ls="--", lw=1.2)
    ax.annotate("75%", xy=(len(labels) - 0.5, 75), xytext=(0, 3),
                textcoords="offset points", ha="right", fontsize=8.5, color=es.RED)
    ax.set_ylim(0, 100)
    ax.set_ylabel("quota del disequilibrio assorbita (%)")
    ax.set_title("assorbimento cumulato con $\\hat\\lambda$ = $-$0,5032", loc="left")
    es.commas(ax, "y", decimals=0)
    ax.grid(axis="x", visible=False)
    fig.tight_layout()
    es.save(fig, OUT / "d09-ecm-assorbimento.pdf")


# =============== D10 -- ACF e PACF letti dalla Figura 2
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
    axes[0].annotate("8 ritardi fuori banda,\ndecadimento lento",
                     xy=(6, 0.49), xytext=(34, 26), textcoords="offset points",
                     fontsize=8.2, color=es.RED, fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.0))
    axes[1].annotate("un solo picco, $\\approx$ 0,89: AR(1)",
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
