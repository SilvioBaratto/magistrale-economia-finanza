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
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.4), layout="constrained")

    r = np.linspace(3.2, 9.0, 400)
    me = B3 + 2 * B4 * r
    turn = -B3 / (2 * B4)
    ax.plot(r, me, color=es.BLUE, lw=1.7,
            label="effetto marginale  -0,9067 + 0,1838 x rooms")
    ax.axhline(0, color=es.RED, ls="--", lw=1.1)
    ax.fill_between(r, me, 0, where=me > 0, color=es.GREENBG)
    ax.fill_between(r, me, 0, where=me <= 0, color=es.REDBG)
    ax.plot([turn], [0], "o", color=es.RED, ms=7, zorder=6)
    ax.axvline(turn, color=es.RED, ls=":", lw=0.9)
    ax.annotate("punto di svolta  rooms = " + IT(turn, 3),
                xy=(turn, 0), xytext=(12, -14), textcoords="offset points",
                va="top", fontsize=8.5, color=es.RED, fontweight="bold")
    for x0 in (4, 5, 6, 7, 8):
        ax.plot([x0], [B3 + 2 * B4 * x0], "s", color=es.TEAL, ms=4, zorder=5)
        # rooms = 5 e' a un soffio dal punto di svolta: la sua etichetta va
        # spostata a destra, altrimenti la verticale in 4,933 la attraversa
        dx, ha = (9, "left") if x0 == 5 else (0, "center")
        ax.annotate(IT(B3 + 2 * B4 * x0, 3), xy=(x0, B3 + 2 * B4 * x0),
                    xytext=(dx, 10 if x0 == 5 else 7),
                    textcoords="offset points", ha=ha,
                    fontsize=8.3, color=es.TEAL)
    es.commas(ax)
    ax.set_xlabel("rooms (numero medio di stanze)")
    ax.set_ylabel(r"$\partial\,\mathrm{E}[\log(price)]/\partial\,rooms$")
    ax.set_title("La pendenza cresce con rooms perche' il coefficiente di sq_rooms e' positivo",
                 loc="left")
    ax.set_ylim(top=1.06)                 # spazio sopra la retta per la legenda
    ax.legend(loc="upper right")          # a sinistra la tagliava la verticale in 4,933

    t4 = B4 / S4
    es.dist_test("z", stat=t4, crit=Z, tail="two", ax=bx,
                 statlabel="t su sq_rooms = " + IT(t4, 3) + "  (p = 5,0e-07)",
                 title=r"Test della non linearita': $H_0:\beta_4=0$ contro $H_1:\beta_4\neq 0$")
    legenda_sotto(bx)
    es.save(fig, OUT / "d01-effetto-rooms.pdf")


# =========================================================== D2 — differenziale
def d02():
    delta = B5 - B6
    rho = np.linspace(-1, 1, 400)
    se = np.sqrt(S5 ** 2 + S6 ** 2 - 2 * rho * S5 * S6)
    tt = np.abs(delta) / se

    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.5), layout="constrained")
    ax.plot(rho, tt, color=es.BLUE, lw=1.8,
            label="|t| in funzione della correlazione fra le due stime")
    ax.axhline(Z, color=es.RED, ls="--", lw=1.2)
    ax.fill_between(rho, tt, Z, where=tt > Z, color=es.REDBG)
    ax.annotate("soglia 1,96", xy=(-0.97, Z), xytext=(0, 5),
                textcoords="offset points", fontsize=8.5, color=es.RED,
                fontweight="bold")
    tmax = abs(delta) / abs(S5 - S6)
    ax.plot([1.0], [tmax], "o", color=es.GREEN, ms=7, zorder=6)
    ax.annotate("massimo possibile  |t| = " + IT(tmax, 3),
                xy=(1.0, tmax), xytext=(-8, 6), textcoords="offset points",
                ha="right", fontsize=8.5, color=es.GREEN, fontweight="bold")
    tnaive = abs(delta) / np.sqrt(S5 ** 2 + S6 ** 2)
    ax.plot([0.0], [tnaive], "D", color=es.AMBER, ms=6, zorder=6)
    ax.annotate("ipotesi (ingiustificata) Cov = 0:  |t| = " + IT(tnaive, 3),
                xy=(0.0, tnaive), xytext=(6, -14), textcoords="offset points",
                fontsize=8.2, color=es.AMBER)
    ax.set_ylim(0, Z * 1.25)
    es.commas(ax)
    ax.set_xlabel(r"$\rho=\mathrm{Corr}(\hat\beta_5,\hat\beta_6)$, ignota: l'output non la riporta")
    ax.set_ylabel("|t| del differenziale")
    ax.set_title("Qualunque sia la covarianza, |t| resta sotto 1,96", loc="left")
    ax.legend(loc="lower left")

    semin = abs(S5 - S6)
    es.ci_line(delta, delta - Z * semin, delta + Z * semin, h0=0.0, ax=bx,
               decimals=4, label="intervallo piu' stretto compatibile con i dati",
               xlabel=r"$\beta_5-\beta_6$ (differenza attesa di $\log(price)$ con nox = 1)",
               title="Anche nel caso piu' favorevole al rifiuto lo zero resta dentro")
    es.save(fig, OUT / "d02-differenziale-ddist.pdf")


# =========================================================== D3 — elasticita'
def d03():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.4), layout="constrained")
    t3 = B1 / S1
    es.dist_test("z", stat=t3, crit=Z, tail="two", ax=ax,
                 statlabel="t = " + IT(t3, 3) + "  (p = 3,8e-11)",
                 title=r"Elasticita' prezzo-inquinamento nei distretti vicini ($ddist=0$): $H_0:\beta_1=0$")
    legenda_sotto(ax)

    dl = np.log(1.03)
    est = 100 * (np.exp(B1 * dl) - 1)
    lo = 100 * (np.exp((B1 + Z * S1) * dl) - 1)
    hi = 100 * (np.exp((B1 - Z * S1) * dl) - 1)
    es.ci_line(est, min(lo, hi), max(lo, hi), h0=0.0, ax=bx, decimals=2, unit="%",
               label="intervallo di confidenza 95% (versione esatta)",
               xlabel="variazione percentuale attesa del prezzo mediano per +3% di nox",
               title="Il +3% di nox si traduce in circa -2% sul prezzo, con lo zero escluso")
    es.save(fig, OUT / "d03-elasticita-nox.pdf")


# =========================================================== D4 — crime -2%
def d04():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.3), layout="constrained")
    lo, hi = B2 - Z * S2, B2 + Z * S2
    es.ci_line(B2, lo, hi, h0=-0.02, ax=ax, decimals=4,
               extra=[(np.log(0.98), "log(0,98)", es.TEAL)],
               xlabel=r"$\beta_2$ (effetto di una unita' di crime su $\log(price)$)",
               title="Entrambe le letture del -2% cadono dentro l'intervallo")
    t4 = (B2 - (-0.02)) / S2
    es.dist_test("z", stat=t4, crit=Z, tail="two", ax=bx,
                 statlabel="t = " + IT(t4, 3) + "  (p = 0,177)",
                 title=r"$H_0:\beta_2=-0{,}02$ contro $H_1:\beta_2\neq-0{,}02$: non si rifiuta")
    legenda_sotto(bx)
    es.save(fig, OUT / "d04-crime-due-percento.pdf")


# =========================================================== D5 — eteroschedasticita'
def d05():
    a, b = 0.899611, -0.0845877
    sb = 0.0198102
    t5 = b / sb
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.5), layout="constrained")
    es.dist_test("z", stat=t5, crit=Z, tail="two", ax=ax,
                 statlabel="t sulla pendenza = " + IT(t5, 3) + "  (p = 2,3e-05)",
                 title=r"Test ridotto di White: $H_0:\,b=0$ (omoschedasticita')")
    legenda_sotto(ax)

    yh = np.linspace(8.6, 11.3, 300)
    var = a + b * yh
    zero = -a / b
    bx.plot(yh, var, color=es.BLUE, lw=1.8,
            label="varianza condizionale stimata  0,8996 - 0,0846 x y_predetto")
    bx.axhline(0, color=es.RED, ls="--", lw=1.0)
    bx.fill_between(yh, var, 0, where=var > 0, color=es.BLUEBG)
    bx.fill_between(yh, var, 0, where=var <= 0, color=es.REDBG)
    bx.plot([YBAR], [a + b * YBAR], "o", color=es.GREEN, ms=7, zorder=6)
    bx.annotate("alla media di l_price (" + IT(YBAR, 3) + "):\nvarianza " + IT(a + b * YBAR, 4),
                xy=(YBAR, a + b * YBAR), xytext=(12, 10), textcoords="offset points",
                ha="left", va="bottom", fontsize=8.2, color=es.GREEN,
                fontweight="bold")
    # marcatore corto, non una verticale a tutta altezza: cosi' resta libero
    # il triangolo in alto a destra, dove ora stanno legenda e annotazione
    bx.vlines(zero, -0.055, 0.055, color=es.RED, ls=":", lw=1.1)
    bx.annotate("varianza stimata nulla in " + IT(zero, 3) + "\n(oltre: negativa, assurda)",
                xy=(zero, 0), xytext=(-8, -9), textcoords="offset points",
                ha="right", va="top", fontsize=8.2, color=es.RED)
    es.commas(bx)
    bx.set_xlabel("valore predetto di l_price")
    bx.set_ylabel("varianza dei residui")
    bx.set_title("Pendenza negativa: i distretti piu' cari sono i piu' omogenei", loc="left")
    bx.set_ylim(-0.088, 0.203)            # riga sopra la retta per la legenda
    bx.legend(loc="upper right")
    es.save(fig, OUT / "d05-eteroschedasticita.pdf")


# =========================================================== D6 — VIF
def d06():
    nomi = ["l_nox", "crime", "rooms", "sq_rooms", "ddist", "d_nox"]
    vif = np.array([3.122, 1.273, 6.664, 5.586, 3.496, 4.045])
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.7),
                                 gridspec_kw={"height_ratios": [1.25, 1]},
                                 layout="constrained")
    y = np.arange(len(nomi))[::-1]
    col = [es.RED if n == "d_nox" else es.BLUE for n in nomi]
    ax.barh(y, np.sqrt(vif), color=col, height=0.6, alpha=0.85)
    for yi, v in zip(y, vif):
        # alone bianco: le due soglie verticali passano dove cadono le cifre
        ax.annotate("VIF = " + IT(v, 3) + "   se x " + IT(np.sqrt(v), 3),
                    xy=(np.sqrt(v), yi), xytext=(6, 0), textcoords="offset points",
                    va="center", fontsize=8.2, color=es.GRAY, zorder=6,
                    bbox=dict(boxstyle="square,pad=0.16", fc="white", ec="none",
                              alpha=0.92))
    for soglia, lab in ((np.sqrt(5), "VIF = 5"), (np.sqrt(10), "VIF = 10")):
        ax.axvline(soglia, color=es.AMBER, ls="--", lw=1.1)
        # in alto: in basso finivano sulla stessa riga dell'etichetta di d_nox
        ax.annotate(lab, xy=(soglia, 1.0), xycoords=("data", "axes fraction"),
                    xytext=(3, -2), textcoords="offset points", fontsize=8.5,
                    color=es.AMBER, va="top")
    ax.set_yticks(y); ax.set_yticklabels(nomi)
    ax.set_xlim(0, 4.6); ax.set_ylim(-0.62, 5.88)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")
    ax.set_xlabel(r"$\sqrt{\mathrm{VIF}_j}$ = fattore di inflazione dell'errore standard")
    ax.set_title("Il VIF gonfia la varianza: sull'errore standard agisce la sua radice", loc="left")

    se_orth = S6 / np.sqrt(4.045)
    casi = ["t osservato\n(se = 0,1416)", "t se d_nox fosse\nortogonale (se = 0,0704)",
            "soglia di\nsignificativita'"]
    val = [B6 / S6, B6 / se_orth, Z]
    colr = [es.BLUE, es.TEAL, es.RED]
    bx.bar(np.arange(3), val, color=colr, width=0.5, alpha=0.85)
    for i, v in enumerate(val):
        bx.annotate(IT(v, 3), xy=(i, v), xytext=(0, 4), textcoords="offset points",
                    ha="center", fontsize=9, fontweight="bold", color=colr[i])
    bx.set_xticks(np.arange(3)); bx.set_xticklabels(casi, fontsize=8.2)
    bx.set_ylim(0, 2.4)
    bx.grid(axis="x", visible=False)
    es.commas(bx, "y")
    bx.set_ylabel(r"$|t|$ su $\beta_6$")
    bx.set_title("Azzerando del tutto la collinearita', il coefficiente resta non significativo",
                 loc="left")
    es.save(fig, OUT / "d06-vif.pdf")


# =========================================================== D7 — ADF
def d07():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.8),
                                 gridspec_kw={"height_ratios": [1.5, 1]},
                                 layout="constrained")
    ax.plot(TIME, GER, color=es.BLUE, lw=1.4, label="ger (Germania)")
    ax.plot(TIME, IRE, color=es.TEAL, lw=1.4, label="ire (Irlanda)")
    t = np.arange(1, 82)
    for serie, colore in ((GER, es.BLUE), (IRE, es.TEAL)):
        X = np.column_stack([np.ones(81), t])
        c = np.linalg.lstsq(X, serie, rcond=None)[0]
        ax.plot(TIME, X @ c, color=colore, ls="--", lw=1.0, alpha=0.7)
    ax.set_ylim(2.36, 5.66)                # riga sotto il minimo per l'etichetta
    ax.annotate("rette di trend stimate: descrivono male\nla discesa e per niente la risalita",
                xy=(2001.30, 3.02), va="bottom", fontsize=8.2, color=es.GRAY,
                bbox=dict(boxstyle="round,pad=0.24", fc="white", ec="none",
                          alpha=0.88))
    imin = int(np.argmin(GER))
    ax.plot([TIME[imin]], [GER[imin]], "o", color=es.RED, ms=5.5, zorder=7)
    ax.plot([TIME[imin]], [IRE[imin]], "o", color=es.RED, ms=5.5, zorder=7)
    ax.annotate("minimo ~ 3,1 (settembre 2005)", xy=(TIME[imin], IRE[imin]),
                xytext=(0, -26), textcoords="offset points", ha="center",
                va="top", fontsize=8, color=es.RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.9,
                                shrinkA=2, shrinkB=4))
    es.commas(ax, "y")
    ax.set_ylabel("tasso a 10 anni (punti percentuali)")
    ax.set_xlabel("")
    ax.set_title("Discesa prolungata e risalita altrettanto prolungata: firma di un trend stocastico",
                 loc="left")
    ax.legend(loc="upper right", ncol=2)

    bx.hlines(0, -4.0, -1.0, color=es.GRAY, lw=1.0)
    bx.fill_between([-4.0, -2.85], -0.22, 0.22, color=es.REDBG, alpha=0.8)
    bx.annotate("regione di rifiuto della radice unitaria\n(specificazione con sola costante)",
                xy=(-3.42, 0.28), ha="center", va="bottom", fontsize=8.4, color=es.RED)
    for v, lab, colore in ((-2.85, "-2,85\nDF con costante\n(la scelta corretta qui)", es.RED),
                           (-1.95, "-1,95\nDF senza costante\n(qui non adeguato)", es.AMBER)):
        bx.vlines(v, -0.22, 0.22, color=colore, lw=2.0)
        bx.annotate(lab, xy=(v, -0.30), ha="center", va="top", fontsize=8.2,
                    color=colore, fontweight="bold")
    bx.set_xlim(-4.0, -1.0); bx.set_ylim(-1.25, 0.95)
    bx.set_yticks([]); bx.grid(visible=False)
    bx.spines["left"].set_visible(False); bx.spines["bottom"].set_visible(False)
    es.commas(bx, "x")
    bx.set_xlabel(r"valore della statistica $t=\hat\delta/\mathrm{se}(\hat\delta)$ (test unilaterale sinistro)")
    bx.set_title("Valori critici al 5% disponibili nelle note del corso", loc="left")
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
    ax.set_title("Il residuo oscilla attorno allo zero e vi ritorna: e' stazionario",
                 loc="left")
    ax.set_ylim(top=0.222)                 # il residuo risale a 0,128 proprio sotto la legenda
    # maniglie strette: a misura piena la prima riga sbatteva sul bordo destro
    ax.legend(loc="upper right", handlelength=1.4, handletextpad=0.5,
              borderaxespad=0.2)

    bx.hlines(0, -4.2, -1.2, color=es.GRAY, lw=1.0)
    bx.fill_between([-4.2, -1.95], -0.22, 0.22, color=es.REDBG, alpha=0.8)
    bx.annotate("regione di rifiuto di $H_0$: nessuna cointegrazione",
                xy=(-2.05, 0.95), ha="right", va="center", fontsize=8.4, color=es.RED)
    for v, lab, colore, lw in ((-1.95, "-1,95\nvalore critico\nfornito dal testo", es.RED, 2.0),
                               (-2.85, "-2,85\nsoglia piu' severa\n(DF con costante)", es.AMBER, 1.6)):
        bx.vlines(v, -0.22, 0.22, color=colore, lw=lw)
        bx.annotate(lab, xy=(v, -0.30), ha="center", va="top", fontsize=8.2,
                    color=colore, fontweight="bold")
    bx.vlines(-3.58, -0.34, 0.34, color=es.GREEN, lw=2.8)
    bx.annotate("statistica osservata  -3,58", xy=(-3.58, 0.40), ha="center", va="bottom",
                fontsize=8.8, color=es.GREEN, fontweight="bold")
    bx.set_xlim(-4.2, -1.2); bx.set_ylim(-1.35, 1.32)
    bx.set_yticks([]); bx.grid(visible=False)
    bx.spines["left"].set_visible(False); bx.spines["bottom"].set_visible(False)
    es.commas(bx, "x")
    bx.set_xlabel("ADF sui residui (Engle-Granger): si rifiuta oltre ogni soglia plausibile")
    bx.set_title("Passo 3: -3,58 supera sia il critico fornito sia quello piu' severo", loc="left")
    es.save(fig, OUT / "d08-cointegrazione.pdf")


# =========================================================== D9 — ECM
def d09():
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.1, 5.6), layout="constrained")
    _, _, tab = es.decay(LAM, horizon=18, targets=(0.5, 0.8), ax=ax,
                         title="Quota del disequilibrio ancora da riassorbire dopo h mesi")
    leg = ax.get_legend()
    if leg is not None:
        leg.remove()
    ax.legend([ax.get_lines()[0]], ["(1 - 0,2187) elevato a h"], loc="upper right")
    ax.set_xticks(np.arange(0, 19, 3))     # h e' un numero di mesi: tacche intere
    es.commas(ax, "x")

    z0 = 0.50
    h = np.arange(0, 13)
    dire = 100 * LAM * z0 * (1 + LAM) ** h
    bx.bar(h, dire, color=es.RED, width=0.62, alpha=0.85)
    for hi, v in zip(h[:5], dire[:5]):
        bx.annotate(IT(v, 1), xy=(hi, v), xytext=(0, -5), textcoords="offset points",
                    ha="center", va="top", fontsize=8.3, color=es.RED)
    bx.axhline(0, color=es.GRAY, lw=0.9)
    bx.set_ylim(bottom=-12.9)              # l'etichetta -10,9 finiva sotto l'asse
    es.commas(bx, "y")
    bx.set_xlabel("mesi dopo il disequilibrio (h)")
    bx.set_ylabel("variazione attesa di ire (punti base)")
    bx.set_title("Disequilibrio iniziale +50 punti base: ogni variazione attesa e' negativa",
                 loc="left")
    print("    orizzonti di assorbimento:", tab)
    es.save(fig, OUT / "d09-ecm-segno.pdf")


# =========================================================== D10 — sbilanciata
def _beta_hat(T, rng):
    """OLS di una serie I(0) su una I(1) indipendente: pendenza stimata."""
    x = np.cumsum(rng.normal(0, 1, T))
    y = np.zeros(T)
    for t in range(1, T):
        y[t] = 0.6 * y[t - 1] + rng.normal(0, 1)
    X = np.column_stack([np.ones(T), x])
    return np.linalg.lstsq(X, y, rcond=None)[0][1], x, y


def d10():
    rng = np.random.default_rng(20230615)          # simulazione illustrativa
    fig = plt.figure(figsize=(6.1, 5.9), layout="constrained")
    gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1.0])
    ax = fig.add_subplot(gs[0, 0])
    cx = fig.add_subplot(gs[0, 1])
    bx = fig.add_subplot(gs[1, :])

    _, x, y = _beta_hat(200, rng)
    ax.plot(np.arange(200), x, color=es.BLUE, lw=1.3, label="x: I(1), vaga")
    ax.plot(np.arange(200), y, color=es.TEAL, lw=1.0, label="y: I(0), in banda")
    ax.axhline(0, color=es.GRAY, lw=0.8)
    es.commas(ax, "y")
    ax.set_xlabel("tempo")
    ax.set_ylabel("livello della serie")
    ax.set_title("Ordini di integrazione\ndiversi", loc="left", fontsize=9.5)
    ax.legend(loc="upper left")

    taglie = [50, 100, 200, 400, 800]
    for j, T in enumerate(taglie):
        bs = np.array([_beta_hat(T, rng)[0] for _ in range(250)])
        cx.scatter(np.full(bs.size, j) + rng.normal(0, 0.055, bs.size), bs,
                   s=3.5, color=es.BLUE, alpha=0.35)
        cx.plot([j - 0.26, j + 0.26], [bs.mean()] * 2, color=es.RED, lw=1.8)
    cx.axhline(0, color=es.GREEN, lw=1.2, ls="--")
    cx.set_xticks(range(len(taglie)))
    cx.set_xticklabels([str(t) for t in taglie])
    cx.set_xlabel("ampiezza campionaria T")
    cx.set_ylabel(r"$\hat\beta$ stimata")
    es.commas(cx, "y")
    cx.set_title("La pendenza collassa\nsullo zero", loc="left", fontsize=9.5)

    vals = [100 * BG, 102.0, 2.0]
    etichette = ["effetto stimato\n(IC 95%: 113,52 - 117,67)",
                 "lettura alternativa:\n1 punto + 2 punti base",
                 "lettura letterale:\n2 punti base"]
    colori = [es.BLUE, es.TEAL, es.RED]
    ypos = np.arange(3)[::-1]
    bx.barh(ypos, vals, color=colori, height=0.5, alpha=0.85)
    bx.errorbar([100 * BG], [ypos[0]],
                xerr=[[100 * Z * SBG], [100 * Z * SBG]], fmt="none",
                ecolor=es.INK, elinewidth=1.4, capsize=4, zorder=5)
    note = ["115,60 punti base", "t = 12,857  ->  si rifiuta", "t = 107,417  ->  si rifiuta"]
    for yi, v, nt, c in zip(ypos, vals, note, colori):
        bx.annotate(nt, xy=(v, yi), xytext=(10, 0), textcoords="offset points",
                    va="center", fontsize=8.6, color=c, fontweight="bold")
    bx.set_yticks(ypos); bx.set_yticklabels(etichette, fontsize=8.2)
    bx.set_xlim(0, 168)
    bx.grid(axis="y", visible=False)
    es.commas(bx, "x")
    bx.set_xlabel("variazione dei tassi italiani per +1 punto percentuale di ger, in punti base")
    bx.set_title("Due ordini di grandezza separano la stima dalla soglia della domanda",
                 loc="left")
    es.save(fig, OUT / "d10-regressione-sbilanciata.pdf")


if __name__ == "__main__":
    for fn in (d01, d02, d03, d04, d05, d06, d07, d08, d09, d10):
        fn()
    print("fatto.")
