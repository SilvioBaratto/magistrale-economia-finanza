#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 15 giugno 2023.

Una figura per ognuna delle dieci domande.  Tutti i numeri provengono
dall'output di regressione riportato nel testo d'esame; le due serie storiche
dell'Esercizio 2 sono ottenute **digitalizzando la Figura 1 del testo**
(p. 4 del PDF): il PNG a 400 dpi e' stato scansionato colonna per colonna
isolando i pixel verdi della curva e calibrando l'asse verticale sui suoi
estremi (3,0 e 5,5).  Precisione stimata +/- 0,02 punti percentuali: sono
valori *letti dalla figura*, non i dati originali dell'esame.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
from scipy import stats
es.use()
import matplotlib.pyplot as plt
OUT = pathlib.Path(__file__).resolve().parent

IT = lambda v, d=4: f"{v:.{d}f}".replace(".", ",")

# --------------------------------------------------------------- Esercizio 1
A, SA = 13.2154, 0.783757
B1, S1 = -0.682711, 0.100950      # l_nox
B2, S2 = -0.0164052, 0.00266355   # crime
B3, S3 = -0.906738, 0.234877      # rooms
B4, S4 = 0.0919130, 0.0180442     # sq_rooms
B5, S5 = -0.0783599, 0.0302638    # ddist
B6, S6 = 0.0577240, 0.141590      # d_nox
N, K = 506, 6
YBAR, YSD = 9.941057, 0.409255
Z = 1.96

# --------------------------------------------------------------- Esercizio 2
# Figura 1 del testo (p. 4), digitalizzata.  T = 81 mesi, 2001:03 - 2007:11.
GER = [4.686, 4.839, 5.044, 5.003, 5.012, 4.831, 4.802, 4.606, 4.467, 4.734,
       4.860, 4.931, 5.153, 5.156, 5.168, 5.024, 4.865, 4.598, 4.391, 4.457,
       4.478, 4.332, 4.178, 3.963, 4.004, 4.136, 3.830, 3.635, 3.956, 4.125,
       4.172, 4.223, 4.344, 4.290, 4.175, 4.108, 3.924, 4.097, 4.244, 4.306,
       4.240, 4.081, 4.017, 3.890, 3.772, 3.587, 3.558, 3.547, 3.688, 3.480,
       3.298, 3.137, 3.198, 3.221, 3.078, 3.242, 3.442, 3.342, 3.323, 3.471,
       3.644, 3.883, 3.958, 3.963, 4.005, 3.880, 3.757, 3.787, 3.716, 3.782,
       4.007, 4.047, 3.951, 4.148, 4.288, 4.549, 4.495, 4.309, 4.225, 4.275,
       4.108]
IRE = [4.938, 5.095, 5.274, 5.234, 5.222, 5.020, 5.001, 4.779, 4.648, 4.923,
       5.029, 5.206, 5.412, 5.411, 5.407, 5.256, 5.107, 4.847, 4.643, 4.699,
       4.666, 4.466, 4.273, 4.072, 4.097, 4.209, 3.904, 3.710, 3.999, 4.167,
       4.193, 4.255, 4.388, 4.357, 4.209, 4.149, 3.983, 4.169, 4.308, 4.379,
       4.274, 4.104, 4.042, 3.926, 3.803, 3.630, 3.529, 3.517, 3.654, 3.470,
       3.290, 3.144, 3.182, 3.218, 3.054, 3.188, 3.390, 3.365, 3.328, 3.466,
       3.648, 3.887, 3.960, 3.981, 4.002, 3.890, 3.773, 3.783, 3.727, 3.767,
       4.020, 4.072, 3.981, 4.180, 4.320, 4.599, 4.592, 4.417, 4.330, 4.390,
       4.322]
GER, IRE = np.array(GER), np.array(IRE)
TIME = 2001 + (3 - 1) / 12 + np.arange(81) / 12.0
LAM, SLAM = -0.218680, 0.0667798
G1, SG1 = 0.993058, 0.0203199
BG, SBG = 1.15597, 0.0105753
AG = -0.562147


def band(ax):
    ax.axhline(0, color=es.GRAY, lw=0.8)


def legenda_sotto(ax, ncol=3):
    """Porta la legenda sotto gli assi.

    Nei pannelli di ``es.dist_test`` le rette verticali (valori critici e
    statistica) attraversano tutta l'altezza del riquadro: qualunque angolo
    interno finisce tagliato, e il testo della legenda copre la densita'.
    Le legende della casa sono senza cornice, quindi non c'e' sfondo che
    protegga il testo: l'unica collocazione pulita e' fuori dagli assi.
    """
    leg = ax.get_legend()
    if leg is not None:
        leg.remove()
    return ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.30),
                     ncol=ncol, borderaxespad=0.0, columnspacing=1.5,
                     handlelength=1.5, handletextpad=0.6)


# =========================================================== D1 — rooms
def d01():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.2), layout="constrained")

    r = np.linspace(3.2, 9.0, 400)
    me = B3 + 2 * B4 * r
    ax.plot(r, me, color=es.BLUE, lw=1.7,
            label="effetto marginale  -0,9067 + 0,1838 x rooms")
    ax.axhline(0, color=es.GRAY, lw=0.8)
    es.commas(ax)
    ax.set_xlabel("rooms (numero medio di stanze)")
    ax.set_ylabel(r"$\partial\,\mathrm{E}[\log(price)]/\partial\,rooms$")
    ax.set_title("La pendenza cresce con rooms perché il coefficiente di sq_rooms è positivo",
                 loc="left")
    ax.set_ylim(top=1.06)                 # spazio sopra la retta per la legenda
    ax.legend(loc="upper left")

    t4 = B4 / S4
    es.dist_test("z", stat=t4, crit=Z, tail="two", ax=bx,
                 statlabel="t su sq_rooms = " + IT(t4, 3) + "  (p = 5,0e-07)",
                 title=r"Test della non linearità: $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$")
    legenda_sotto(bx)
    es.save(fig, OUT / "d01-effetto-rooms.pdf")


# =========================================================== D2 — differenziale
def d02():
    delta = B5 - B6
    fig, ax = plt.subplots(figsize=(6.1, 3.2), layout="constrained")
    x = np.linspace(-1.0, 0.6, 200)
    ax.plot(x, B5 + B6 * (x - 1), color=es.BLUE, lw=1.7,
            label="effetto di ddist  -0,0784 + 0,0577 (log nox - 1)")
    ax.axhline(0, color=es.GRAY, lw=0.8)
    ax.plot([0.0], [delta], "o", color=es.RED, ms=7, zorder=6)
    ax.annotate("nox = 1:  " + IT(B5, 4) + " - 0,0577 = " + IT(delta, 3),
                xy=(0.0, delta), xytext=(-10, 14), textcoords="offset points",
                ha="right", va="bottom", fontsize=8.6, color=es.RED, fontweight="bold")
    es.commas(ax)
    ax.set_ylim(-0.21, 0.03)
    ax.set_xlabel("log(nox)")
    ax.set_ylabel(r"$\Delta\,\log(price)$ per ddist da 0 a 1")
    ax.set_title(r"Con $\mathrm{nox}=1$ l'effetto di ddist vale $\beta_5-\beta_6$", loc="left")
    ax.legend(loc="upper left")
    es.save(fig, OUT / "d02-differenziale-ddist.pdf")


# =========================================================== D3 — elasticita'
def d03():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.4), layout="constrained")
    t3 = B1 / S1
    es.dist_test("z", stat=t3, crit=Z, tail="two", ax=ax,
                 statlabel="t = " + IT(t3, 3) + "  (p = 3,8e-11)",
                 title=r"Elasticità prezzo-inquinamento nei distretti vicini ($ddist=0$): $H_0:\beta_1=0$")
    legenda_sotto(ax)

    est = 100 * B1 * 0.03
    lo, hi = 100 * (B1 - Z * S1) * 0.03, 100 * (B1 + Z * S1) * 0.03
    es.ci_line(est, lo, hi, h0=0.0, ax=bx, decimals=2, unit="%",
               label="intervallo di confidenza 95%",
               xlabel="variazione percentuale attesa del prezzo per +3% di nox",
               title="Il +3% di nox si traduce in circa -2% sul prezzo, con lo zero escluso")
    es.save(fig, OUT / "d03-elasticita-nox.pdf")


# =========================================================== D4 — crime -2%
def d04():
    fig, ax = plt.subplots(figsize=(6.1, 2.5), layout="constrained")
    lo, hi = B2 - Z * S2, B2 + Z * S2
    es.ci_line(B2, lo, hi, ax=ax, decimals=4,
               extra=[(-0.02, "-0,02", es.AMBER)],
               xlabel=r"$\beta_2$ (effetto di una unità di crime su $\log(price)$)",
               title="Il valore -0,02 cade dentro l'intervallo di confidenza")
    es.save(fig, OUT / "d04-crime-due-percento.pdf")


# =========================================================== D5 — eteroschedasticita'
def d05():
    b, sb = -0.0845877, 0.0198102
    t5 = b / sb
    fig, ax = plt.subplots(figsize=(6.1, 3.5), layout="constrained")
    es.dist_test("z", stat=t5, crit=Z, tail="two", ax=ax,
                 statlabel="t sulla pendenza = " + IT(t5, 3) + "  (p = 2,3e-05)",
                 title=r"Regressione ausiliaria di $\hat\epsilon^2$ su $\hat y$: $H_0:\,b=0$")
    legenda_sotto(ax)
    es.save(fig, OUT / "d05-eteroschedasticita.pdf")


# =========================================================== D6 — VIF
def d06():
    nomi = ["l_nox", "crime", "rooms", "sq_rooms", "ddist", "d_nox"]
    vif = np.array([3.122, 1.273, 6.664, 5.586, 3.496, 4.045])
    fig, ax = plt.subplots(figsize=(6.1, 3.5), layout="constrained")
    y = np.arange(len(nomi))[::-1]
    col = [es.RED if n == "d_nox" else es.BLUE for n in nomi]
    ax.barh(y, vif, color=col, height=0.6, alpha=0.85)
    for yi, v in zip(y, vif):
        ax.annotate(IT(v, 3), xy=(v, yi), xytext=(5, 0), textcoords="offset points",
                    va="center", fontsize=8.6, color=es.GRAY)
    ax.axvline(10, color=es.AMBER, ls="--", lw=1.2)
    ax.annotate("soglia VIF = 10", xy=(10, 1.0), xycoords=("data", "axes fraction"),
                xytext=(-4, -3), textcoords="offset points", fontsize=8.6,
                color=es.AMBER, va="top", ha="right")
    ax.set_yticks(y); ax.set_yticklabels(nomi)
    ax.set_xlim(0, 11); ax.set_ylim(-0.62, 5.7)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel("VIF")
    ax.set_title("Tutti i VIF sono sotto 10; d_nox in evidenza", loc="left")
    es.save(fig, OUT / "d06-vif.pdf")


# =========================================================== D7 — ADF
def d07():
    fig, ax = plt.subplots(figsize=(6.1, 3.3), layout="constrained")
    ax.plot(TIME, GER, color=es.BLUE, lw=1.4, label="ger (Germania)")
    ax.plot(TIME, IRE, color=es.TEAL, lw=1.4, label="ire (Irlanda)")
    ax.set_ylim(2.8, 5.9)
    es.commas(ax, "y")
    ax.set_ylabel("tasso a 10 anni (punti percentuali)")
    ax.set_title("Figura 1 del tema: le serie non mostrano un trend chiaro", loc="left")
    ax.legend(loc="upper right", ncol=2)
    es.save(fig, OUT / "d07-adf-specificazione.pdf")


# =========================================================== D8 — cointegrazione
def d08():
    X = np.column_stack([np.ones(81), GER])
    c = np.linalg.lstsq(X, IRE, rcond=None)[0]
    u = IRE - X @ c
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.7),
                                 gridspec_kw={"height_ratios": [1.35, 1]},
                                 layout="constrained")
    ax.plot(TIME, u, color=es.BLUE, lw=1.4,
            label="residuo della relazione di lungo periodo (dati digitalizzati)")
    ax.axhline(0, color=es.GRAY, lw=0.9)
    sd = u.std(ddof=1)
    ax.axhspan(-2 * sd, 2 * sd, color=es.GREENBG, zorder=0,
               label="banda +/- 2 deviazioni standard (" + IT(2 * sd, 3) + ")")
    es.commas(ax, "y")
    ax.set_ylabel("punti percentuali")
    ax.set_title("Il residuo oscilla attorno allo zero e vi ritorna: è stazionario",
                 loc="left")
    ax.set_ylim(top=0.222)                 # il residuo risale a 0,128 proprio sotto la legenda
    # maniglie strette: a misura piena la prima riga sbatteva sul bordo destro
    ax.legend(loc="upper right", handlelength=1.4, handletextpad=0.5,
              borderaxespad=0.2)

    bx.hlines(0, -4.2, -1.2, color=es.GRAY, lw=1.0)
    bx.fill_between([-4.2, -1.95], -0.22, 0.22, color=es.REDBG, alpha=0.8)
    bx.annotate("regione di rifiuto di $H_0$: radice unitaria nei residui",
                xy=(-2.05, 0.95), ha="right", va="center", fontsize=8.4, color=es.RED)
    bx.vlines(-1.95, -0.22, 0.22, color=es.RED, lw=2.0)
    bx.annotate("-1,95\nvalore critico\nfornito dal testo", xy=(-1.95, -0.30), ha="center",
                va="top", fontsize=8.2, color=es.RED, fontweight="bold")
    bx.vlines(-3.58, -0.34, 0.34, color=es.GREEN, lw=2.8)
    bx.annotate("statistica osservata  -3,58", xy=(-3.58, 0.40), ha="center", va="bottom",
                fontsize=8.8, color=es.GREEN, fontweight="bold")
    bx.set_xlim(-4.2, -1.2); bx.set_ylim(-1.35, 1.32)
    bx.set_yticks([]); bx.grid(visible=False)
    bx.spines["left"].set_visible(False); bx.spines["bottom"].set_visible(False)
    es.commas(bx, "x")
    bx.set_xlabel("statistica ADF sui residui")
    bx.set_title("ADF sui residui: -3,58 è a sinistra del valore critico -1,95", loc="left")
    es.save(fig, OUT / "d08-cointegrazione.pdf")


# =========================================================== D9 — ECM
def d09():
    fig, ax = plt.subplots(figsize=(6.1, 3.4), layout="constrained")
    h = np.arange(1, 9)
    dire = LAM * (1 + LAM) ** (h - 1)
    ax.bar(h, dire, color=es.RED, width=0.62, alpha=0.85)
    for hi, v in zip(h, dire):
        ax.annotate(IT(v, 3), xy=(hi, v), xytext=(0, -4), textcoords="offset points",
                    ha="center", va="top", fontsize=8.3, color=es.RED)
    ax.axhline(0, color=es.GRAY, lw=0.9)
    ax.set_ylim(-0.27, 0.02)
    ax.set_xticks(h)
    es.commas(ax, "y")
    ax.set_xlabel("periodi dopo il disequilibrio (h)")
    ax.set_ylabel(r"$\Delta\,\mathrm{ire}_{t+h}$ (punti percentuali)")
    ax.set_title(r"Disequilibrio $\mathrm{ecm}_t=1$ con ger stabile: ogni variazione attesa è negativa",
                 loc="left")
    es.save(fig, OUT / "d09-ecm-segno.pdf")


# =========================================================== D10 — sbilanciata
def d10():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 4.6),
                                 gridspec_kw={"height_ratios": [1.15, 1]},
                                 layout="constrained")
    ax.hlines(0, -6.2, -2.4, color=es.GRAY, lw=1.0)
    ax.fill_between([-6.2, -3.43], -0.22, 0.22, color=es.REDBG, alpha=0.8)
    ax.annotate("regione di rifiuto di $H_0$: radice unitaria", xy=(-3.55, 0.80),
                ha="right", va="center", fontsize=8.4, color=es.RED)
    ax.vlines(-3.43, -0.22, 0.22, color=es.RED, lw=2.0)
    ax.annotate("-3,43\nvalore critico", xy=(-3.43, -0.30), ha="center", va="top",
                fontsize=8.2, color=es.RED, fontweight="bold")
    ax.vlines(-5.12, -0.34, 0.34, color=es.GREEN, lw=2.8)
    ax.annotate("ita: statistica osservata  -5,12", xy=(-5.12, 0.40), ha="center",
                va="bottom", fontsize=8.8, color=es.GREEN, fontweight="bold")
    ax.set_xlim(-6.2, -2.4); ax.set_ylim(-0.95, 1.15)
    ax.set_yticks([]); ax.grid(visible=False)
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
    es.commas(ax, "x")
    ax.set_xlabel("statistica del test di radice unitaria")
    ax.set_title("ita: si rifiuta la radice unitaria", loc="left")

    bx.barh([0], [25], color=es.BLUE, height=0.5, alpha=0.85)
    bx.annotate("25%", xy=(25, 0), xytext=(6, 0), textcoords="offset points",
                va="center", fontsize=8.8, color=es.BLUE, fontweight="bold")
    bx.axvline(5, color=es.RED, ls="--", lw=1.2)
    bx.annotate("livello 5%", xy=(5, 0.5), xytext=(4, 0), textcoords="offset points",
                fontsize=8.4, color=es.RED, va="bottom")
    bx.set_yticks([0]); bx.set_yticklabels(["ger"])
    bx.set_xlim(0, 40); bx.set_ylim(-0.5, 0.75)
    bx.grid(axis="y", visible=False)
    es.commas(bx, "x")
    bx.set_xlabel("p-value del test di radice unitaria (in %)")
    bx.set_title("ger: non si rifiuta la radice unitaria", loc="left")
    es.save(fig, OUT / "d10-regressione-sbilanciata.pdf")


if __name__ == "__main__":
    for fn in (d01, d02, d03, d04, d05, d06, d07, d08, d09, d10):
        fn()
    print("fatto.")
