#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 13 giugno 2024.

Esercizio 1 (compensi NBA, domande 1-6) ed Esercizio 2 (esenzione fiscale e
tasso di fertilita', domande 7-10).  Ogni figura visualizza solo la decisione
scritta nella risposta corrispondente; le serie dell'Esercizio 2 non sono
disponibili come dati e non si simula nulla.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
from scipy import stats
import matplotlib.pyplot as plt

es.use()
OUT = pathlib.Path(__file__).resolve().parent

SEED = 20240613

# ------------------------------------------------------------------ Esercizio 1
N, K = 269, 8
DF = N - K - 1                       # 260 gradi di liberta' residui
B = {"const": 6.60075, "guard": -0.213447, "forward": -0.00439273,
     "exper": 0.193112, "expersq": -0.00593377, "age": -0.0454382,
     "points": 0.0617670, "rebounds": 0.0388834, "assists": 0.0471301}
SE = {"const": 0.725801, "guard": 0.148364, "forward": 0.121028,
      "exper": 0.0585684, "expersq": 0.00211655, "age": 0.0312218,
      "points": 0.00810962, "rebounds": 0.0196173, "assists": 0.0201958}
R2C = 0.516307

T_2 = stats.norm.ppf(0.975)          # 1,96
T_1 = stats.norm.ppf(0.95)           # 1,645


def it(v, d=4):
    return f"{v:.{d}f}".replace(".", ",")


# --------------------------------------------------------------- utilita' grafiche
# Nel documento le figure sono incluse a 0,86\linewidth su un testo di 15 cm:
# una figura larga 6,3" arriva in pagina a 0,81 della sua dimensione nominale.
# Le figure piu' larghe vanno quindi compensate, altrimenti il corpo effettivo
# in stampa scende sotto i 7 pt.


def headroom(ax, k):
    """Allarga verso l'alto il limite dell'asse y, per liberare la fascia
    in cui va la legenda senza toccare i dati."""
    lo, hi = ax.get_ylim()
    ax.set_ylim(lo, lo + (hi - lo) * k)
    return ax


def cap_vlines(ax, frac):
    """Accorcia le rette verticali gia' disegnate (valori critici, statistica)
    perche' si fermino sotto la legenda invece di attraversarla."""
    for ln in ax.lines:
        xd, yd = np.asarray(ln.get_xdata()), np.asarray(ln.get_ydata())
        if xd.size == 2 and xd[0] == xd[1] and tuple(yd) == (0.0, 1.0):
            ln.set_ydata([0.0, frac])
    return ax


def bump(fig, width_in, tick=8.5, label=9.5):
    """Riporta tick, etichette degli assi e legende al corpo effettivo che
    hanno nelle figure larghe 6,3 pollici."""
    k = width_in / 6.3
    for ax in fig.axes:
        ax.tick_params(axis="both", labelsize=tick * k)
        ax.xaxis.label.set_fontsize(label * k)
        ax.yaxis.label.set_fontsize(label * k)
        lg = ax.get_legend()
        if lg is not None:
            for t in lg.get_texts():
                t.set_fontsize(t.get_fontsize() * k)
    return fig


# ---------------------------------------------------------------- D1: forward
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.0),
                         gridspec_kw={"height_ratios": [1.55, 1]})
t_obs = B["forward"] / SE["forward"]
es.dist_test("z", stat=t_obs, crit=T_1, tail="left", ax=axes[0],
             statlabel=f"$t$ osservata = {it(t_obs, 4)}",
             pvalue=stats.norm.cdf(t_obs),
             title=r"(a) $H_0:\beta_2=0$ contro $H_1:\beta_2<0$  —  "
                   r"rifiuto in coda sinistra")
axes[0].set_xlim(-4.2, 4.2)
lo = B["forward"] - T_2 * SE["forward"]
hi = B["forward"] + T_2 * SE["forward"]
es.ci_line(B["forward"], lo, hi, h0=0.0, ax=axes[1], decimals=4,
           xlabel=r"$\beta_2$ = differenziale di log-salario ala vs centro",
           title=r"(b) intervallo di confidenza al 95% per $\beta_2$")
fig.tight_layout()
es.save(fig, OUT / "d01-forward-vs-centro.pdf")

# ---------------------------------------------------------- D2: F congiunta
fig, ax = plt.subplots(figsize=(6.3, 3.0))
Fcrit = stats.f.ppf(0.95, 2, DF)
es.dist_test("F", (2, DF), crit=Fcrit, tail="right", ax=ax,
             title=r"$H_0:\beta_1=\beta_2=0$  —  regione di rifiuto del test $F$ al 5%")
ax.set_xlim(0, 8)
fig.tight_layout()
es.save(fig, OUT / "d02-dummy-congiunta.pdf")

# ------------------------------------------------------ D3: non linearita'
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.4))
t_sq = B["expersq"] / SE["expersq"]
es.dist_test("z", stat=t_sq, crit=T_2, tail="two", ax=axes[0],
             statlabel=f"$t$ = {it(t_sq, 4)}",
             title=r"(a) $H_0:\beta_5=0$ contro $H_1:\beta_5\neq0$  —  test bilaterale")
axes[0].set_xlim(-4.6, 4.6)
headroom(axes[0], 1.42)
cap_vlines(axes[0], 0.58)
axes[0].legend(loc="upper left", fontsize=8.2)

_, ax2, turn = es.quadratic_effect(B["exper"], B["expersq"], xmax=20, xmin=0,
                                   ax=axes[1], varname="exper",
                                   ylabel=r"$\partial\log(wage)/\partial\,exper$",
                                   title=r"(b) effetto marginale dell'esperienza: "
                                         r"decrescente perché $\beta_5<0$")
# la virgola decimale dentro $...$ diventa "0, 1931": i numeri escono dal math
ax2.get_lines()[0].set_label(
    r"$\partial\log(wage)/\partial\,exper$ = "
    f"{it(B['exper'], 4)} $-$ {it(abs(2 * B['expersq']), 4)}" r"$\,exper$")
# "effetto nullo in exper = 16,272" sbordava dal bordo destro degli assi
for t in ax2.texts:
    if t.get_text().startswith("effetto nullo"):
        t.set_ha("right")
        t.set_va("bottom")
        t.set_position((-10, 10))
ax2.set_ylim(-0.062, 0.243)          # spazio per l'etichetta del punto in exper = 0
for e in (0, 5, 10):
    me = B["exper"] + 2 * B["expersq"] * e
    ax2.plot([e], [me], "o", color=es.TEAL, ms=5, zorder=7)
    ax2.annotate(it(me, 4), xy=(e, me), xytext=(5, 6), textcoords="offset points",
                 fontsize=8, color=es.TEAL)
ax2.legend(loc="lower left")
fig.tight_layout()
es.save(fig, OUT / "d03-esperienza-nonlineare.pdf")

# --------------------------------------------------- D4: White vs Breusch-Pagan
LM_W, DF_W, P_W = 42.5928, 40, 0.360144
LM_B, DF_B, P_B = 24.6878, 8, 0.00175558
fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.1))
es.dist_test("chi2", DF_W, stat=LM_W, crit=stats.chi2.ppf(0.95, DF_W), tail="right",
             ax=axes[0], statlabel=f"LM = {it(LM_W, 4)}", pvalue=P_W,
             title=r"(a) White: $\chi^2_{40}$")
es.dist_test("chi2", DF_B, stat=LM_B, crit=stats.chi2.ppf(0.95, DF_B), tail="right",
             ax=axes[1], statlabel=f"LM = {it(LM_B, 4)}", pvalue=P_B,
             title=r"(b) Breusch-Pagan: $\chi^2_{8}$")
for ax in axes:
    headroom(ax, 1.62)               # fascia libera in cima per la legenda
    cap_vlines(ax, 0.55)             # statistica e valore critico si fermano sotto
    ax.legend(loc="upper right", fontsize=7.4)
bump(fig, 7.1)
fig.tight_layout()
es.save(fig, OUT / "d04-white-vs-bp.pdf")

# ------------------------------------------------------------- D5: due punti
# 2 punti in piu' valgono almeno il 10% <=> 2*beta7 >= 0,10 <=> beta7 >= 0,05
q5 = 0.10 / 2
lo5, hi5 = B["points"] - T_2 * SE["points"], B["points"] + T_2 * SE["points"]
fig, ax = plt.subplots(figsize=(6.3, 2.3))
es.ci_line(B["points"], lo5, hi5, h0=q5, ax=ax, decimals=4,
           xlabel=r"$\beta_7$ = effetto di un punto in più a partita sul log-salario",
           title=r"intervallo di confidenza al 95% per $\beta_7$ e soglia $0{,}05$ "
                 r"(2 punti $\Rightarrow$ 10%)")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
es.save(fig, OUT / "d05-due-punti-in-piu.pdf")

# --------------------------------------------------------- D6: esperienza ottima
e_star = -B["exper"] / (2 * B["expersq"])
g_max = -B["exper"] ** 2 / (4 * B["expersq"])
e = np.linspace(0, 22, 500)
g = B["exper"] * e + B["expersq"] * e ** 2
fig, ax = plt.subplots(figsize=(6.3, 3.0))
ax.plot(e, g, color=es.BLUE, lw=1.8,
        label=r"$\beta_4\,exper+\beta_5\,exper^2$")
ax.fill_between(e, g, 0, color=es.BLUEBG)
ax.plot([e_star], [g_max], "*", color=es.RED, ms=16, zorder=6)
ax.axvline(e_star, color=es.RED, ls=":", lw=1.0)
ax.set_ylim(-0.06, 2.20)
ax.annotate(f"massimo in exper = {it(e_star, 3)} anni",
            xy=(e_star, g_max), xytext=(-14, 12), textcoords="offset points",
            ha="right", va="bottom", fontsize=9, color=es.RED, fontweight="bold")
ax.set_xlabel("exper (anni da professionista)")
ax.set_ylabel("contributo a $\\log(wage)$")
ax.set_yticks([0, 0.5, 1.0, 1.5])
ax.legend(loc="lower left")
es.commas(ax, "y")
fig.tight_layout()
es.save(fig, OUT / "d06-esperienza-ottima.pdf")

# ------------------------------------------------------------------ Esercizio 2
# ------------------------------------------------------------------ D7: ADF
fig, ax = plt.subplots(figsize=(6.3, 2.6))
XLO, XHI = -4.25, -1.00
ax.set_xlim(XLO, XHI)
ax.set_ylim(-1.00, 1.00)
ax.axvspan(XLO, -2.38, color=es.REDBG, alpha=0.75)
ax.axvline(-2.38, color=es.RED, lw=1.8)
ax.annotate("valore critico 5%\nfornito dal testo: $-$2,38", xy=(-2.38, 0.62),
            xytext=(5, 0), textcoords="offset points", fontsize=8.5,
            color=es.RED, fontweight="bold", va="center", ha="left")
for v, lab, dy in ((-3.306, "gfr: $-$3,306", 0.22), (-2.871, "pe: $-$2,871", -0.22)):
    ax.plot([v], [dy], "o", color=es.BLUE, ms=9, zorder=6)
    ax.annotate(lab, xy=(v, dy), xytext=(0, 12), textcoords="offset points",
                ha="center", fontsize=9, color=es.BLUE, fontweight="bold")
ax.annotate("regione di rifiuto di $H_0$ (radice unitaria)", xy=(XLO + 0.08, -0.80),
            fontsize=8.5, color=es.RED, ha="left", va="center")
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("statistica ADF (test unilaterale sinistro)")
es.commas(ax, "x", decimals=2)
fig.tight_layout()
es.save(fig, OUT / "d07-adf-radici-unitarie.pdf")

# ----------------------------------------------------- D8: Engle-Granger
fig, ax = plt.subplots(figsize=(6.3, 2.6))
ax.set_xlim(0, 1)
ax.axhspan(-1, 1, xmin=0, xmax=0.05, color=es.REDBG)
ax.axvline(0.05, color=es.RED, lw=1.6)
ax.annotate("rifiuto se p-value < 0,05\n(radice unitaria rifiutata)", xy=(0.05, -0.55),
            xytext=(6, 0), textcoords="offset points", fontsize=8.5,
            color=es.RED, va="center")
ax.plot([0.68], [0.15], "o", color=es.BLUE, ms=10, zorder=6)
ax.annotate("Engle-Granger: p-value = 0,68\nnon si rifiuta $H_0$:\nradice unitaria nei residui",
            xy=(0.68, 0.15), xytext=(0, 16), textcoords="offset points",
            ha="center", fontsize=8.8, color=es.BLUE, fontweight="bold")
ax.set_ylim(-1, 1)
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xlabel(r"p-value del test ADF sui residui $\hat u_t$")
es.commas(ax, "x", decimals=2)
fig.tight_layout()
es.save(fig, OUT / "d08-engle-granger.pdf")

# ------------------------------------------------------------------- D9: QLR
fig, ax = plt.subplots(figsize=(6.3, 2.6))
ax.set_xlim(0, 1)
ax.axhspan(-1, 1, xmin=0, xmax=0.05, color=es.REDBG)
ax.axvline(0.05, color=es.RED, lw=1.6)
ax.annotate("rifiuto di $H_0$ (esiste un break)\nse p-value < 0,05", xy=(0.05, -0.55),
            xytext=(6, 0), textcoords="offset points", fontsize=8.5,
            color=es.RED, va="center")
ax.plot([0.372], [0.15], "o", color=es.BLUE, ms=10, zorder=6)
ax.annotate("QLR: p-value = 0,372\nnon si rifiuta $H_0$:\nnessun break",
            xy=(0.372, 0.15), xytext=(0, 16), textcoords="offset points",
            ha="center", fontsize=8.8, color=es.BLUE, fontweight="bold")
ax.set_ylim(-1, 1)
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("p-value del test QLR")
es.commas(ax, "x", decimals=2)
fig.tight_layout()
es.save(fig, OUT / "d09-qlr-break.pdf")

# --------------------------------------------------------------- D10: ACF/PACF
ACF_OBS = [0.45, 0.16, -0.23, -0.13, -0.21, -0.08, -0.10,
           0.03, 0.06, 0.19, 0.14, 0.13, -0.13, -0.22]
PACF_OBS = [0.45, -0.03, -0.38, 0.19, -0.16, -0.07, 0.01,
            0.01, 0.04, 0.12, 0.01, 0.04, -0.22, -0.07]
T10 = 71

fig, axs = plt.subplots(2, 1, figsize=(6.3, 4.2), sharex=True)
es.acf_pacf(ACF_OBS, PACF_OBS, n=T10, axes=[axs[0], axs[1]])
for ax in axs:
    ax.set_ylim(-0.48, 0.58)
    ax.set_xticks(range(0, 15, 2))
    ax.legend(loc="lower right", fontsize=7.2)
fig.tight_layout()
es.save(fig, OUT / "d10-acf-pacf-dgfr.pdf")

print("fatto.")
