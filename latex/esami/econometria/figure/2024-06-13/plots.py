#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 13 giugno 2024.

Esercizio 1 (compensi NBA, domande 1-6) ed Esercizio 2 (esenzione fiscale e
tasso di fertilita', domande 7-10).  Ogni figura visualizza l'inferenza della
domanda corrispondente; le serie storiche dell'Esercizio 2 non sono disponibili
come dati, quindi dove serve illustrare un meccanismo si usa una simulazione
con seme fissato, dichiarata come tale in didascalia.
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

T_2 = stats.t.ppf(0.975, DF)         # 1,96913
T_1 = stats.t.ppf(0.95, DF)          # 1,65074


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
es.dist_test("t", DF, stat=t_obs, crit=T_1, tail="left", ax=axes[0],
             statlabel=f"$t$ osservata = {it(t_obs, 5)}",
             pvalue=stats.t.cdf(t_obs, DF),
             title=r"(a) $H_0:\beta_2=0$ contro $H_1:\beta_2<0$  —  "
                   r"$t_{260}$, rifiuto in coda sinistra")
axes[0].set_xlim(-4.2, 4.2)
lo = B["forward"] - T_2 * SE["forward"]
hi = B["forward"] + T_2 * SE["forward"]
es.ci_line(B["forward"], lo, hi, h0=0.0, ax=axes[1], decimals=4,
           xlabel=r"$\beta_2$ = differenziale di log-salario ala vs centro",
           title=r"(b) intervallo di confidenza al 95% per $\beta_2$")
fig.tight_layout()
es.save(fig, OUT / "d01-forward-vs-centro.pdf")

# ---------------------------------------------------------- D2: F congiunta
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.4))
Fcrit = stats.f.ppf(0.95, 2, DF)
es.dist_test("F", (2, DF), crit=Fcrit, tail="right", ax=axes[0],
             title=r"(a) $H_0:\beta_1=\beta_2=0$  —  densita' $F_{2,260}$ "
                   r"e regione di rifiuto al 5%")
axes[0].set_xlim(0, 8)
axes[0].annotate("statistica non fornita dal testo:\nva calcolata dal modello ristretto",
                 xy=(4.6, 0.30), fontsize=8.5, color=es.GRAY, ha="left")

r2r = np.linspace(0.46, R2C, 400)
Fval = ((R2C - r2r) / 2) / ((1 - R2C) / DF)
axes[1].plot(r2r, Fval, color=es.BLUE, lw=1.6,
             label=r"$F=\dfrac{(R_c^2-R_r^2)/2}{(1-R_c^2)/260}$")
axes[1].axhline(Fcrit, color=es.RED, ls="--", lw=1.1,
                label=f"valore critico al 5% = {it(Fcrit, 4)}")
r2_star = R2C - Fcrit * 2 * (1 - R2C) / DF
axes[1].fill_between(r2r, Fval, Fcrit, where=Fval >= Fcrit, color=es.REDBG)
axes[1].plot([r2_star], [Fcrit], "o", color=es.RED, ms=7, zorder=6)
# la fascia alta e' riservata alla legenda: l'annotazione sta nel vuoto
# fra la retta blu e la legenda, non piu' sopra le voci della legenda
axes[1].set_ylim(0, 22)
axes[1].annotate(f"si rifiuta se $R_r^2 <$ {it(r2_star, 4)}\n"
                 f"(le due dummy devono aggiungere\npiu' di 1,13 punti di $R^2$)",
                 xy=(r2_star, Fcrit), xytext=(-8, 50), textcoords="offset points",
                 fontsize=8.5, color=es.RED, ha="right", va="bottom",
                 fontweight="bold")
axes[1].axvline(R2C, color=es.GRAY, ls=":", lw=1.0)
axes[1].annotate(f"$R_c^2$ = {it(R2C, 6)}", xy=(R2C, 6.4), xytext=(-6, 0),
                 textcoords="offset points", fontsize=8.5, color=es.GRAY, ha="right")
axes[1].set_xlabel(r"$R^2$ del modello ristretto (senza $guard$ e $forward$)")
axes[1].set_ylabel("statistica $F$")
axes[1].set_title("(b) quale perdita di adattamento servirebbe per rifiutare", loc="left")
axes[1].set_yticks([0, 5, 10, 15])
axes[1].legend(loc="upper right")
es.commas(axes[1])
fig.tight_layout()
es.save(fig, OUT / "d02-dummy-congiunta.pdf")

# ------------------------------------------------------ D3: non linearita'
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.4))
t_sq = B["expersq"] / SE["expersq"]
es.dist_test("t", DF, stat=t_sq, crit=T_2, tail="two", ax=axes[0],
             statlabel=f"$t$ ricalcolata = {it(t_sq, 4)}",
             pvalue=2 * stats.t.sf(abs(t_sq), DF),
             title=r"(a) $H_0:\beta_5=0$ contro $H_1:\beta_5\neq0$  —  $t_{260}$ bilaterale")
axes[0].axvline(-2.882, color=es.AMBER, lw=1.6, ls="-.",
                label="$t$ stampata nel testo = $-$2,882")
axes[0].set_xlim(-4.6, 4.6)
# le quattro verticali attraversavano la legenda: si fermano sotto la fascia
# libera aperta in cima al pannello
headroom(axes[0], 1.42)
cap_vlines(axes[0], 0.58)
axes[0].legend(loc="upper left", fontsize=8.2)

_, ax2, turn = es.quadratic_effect(B["exper"], B["expersq"], xmax=20, xmin=0,
                                   ax=axes[1], varname="exper",
                                   ylabel=r"$\partial\log(wage)/\partial\,exper$",
                                   title=r"(b) effetto marginale dell'esperienza: "
                                         r"decrescente perche' $\beta_5<0$")
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
fig, axes = plt.subplots(2, 2, figsize=(7.1, 5.4))
es.dist_test("chi2", DF_W, stat=LM_W, crit=stats.chi2.ppf(0.95, DF_W), tail="right",
             ax=axes[0, 0], statlabel=f"LM = {it(LM_W, 4)}", pvalue=P_W,
             title=r"(a) White: $\chi^2_{40}$, 40 restrizioni")
es.dist_test("chi2", DF_B, stat=LM_B, crit=stats.chi2.ppf(0.95, DF_B), tail="right",
             ax=axes[0, 1], statlabel=f"LM = {it(LM_B, 4)}", pvalue=P_B,
             title=r"(b) Breusch-Pagan: $\chi^2_{8}$, 8 restrizioni")
inc, df_inc = LM_W - LM_B, DF_W - DF_B
es.dist_test("chi2", df_inc, stat=inc, crit=stats.chi2.ppf(0.95, df_inc), tail="right",
             ax=axes[1, 0], statlabel=f"LM incrementale = {it(inc, 4)}",
             pvalue=stats.chi2.sf(inc, df_inc),
             title=r"(c) i 32 termini in piu' di White: $\chi^2_{32}$")

ncp = np.linspace(0, 60, 300)
for d, col, lab in ((DF_B, es.GREEN, "Breusch-Pagan (8 g.d.l.)"),
                    (DF_W, es.RED, "White (40 g.d.l.)")):
    pw = stats.ncx2.sf(stats.chi2.ppf(0.95, d), d, ncp)
    axes[1, 1].plot(ncp, pw, color=col, lw=1.7, label=lab)
axes[1, 1].axhline(0.05, color=es.GRAY, ls=":", lw=0.9)
axes[1, 1].set_xlabel("parametro di non centralita' (intensita' del segnale)")
axes[1, 1].set_ylabel("potenza al 5%")
axes[1, 1].set_title("(d) a parita' di segnale, 40 g.d.l. costano potenza", loc="left")
# la legenda stava sopra la retta dello 0,05: sale nella fascia sopra le curve
axes[1, 1].set_ylim(0, 1.32)
axes[1, 1].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
axes[1, 1].legend(loc="upper left", fontsize=8.5)
es.commas(axes[1, 1], "y", decimals=1)
for ax in axes.ravel()[:3]:
    headroom(ax, 1.48)               # fascia libera in cima per la legenda
    cap_vlines(ax, 0.60)             # statistica e valore critico si fermano sotto
    ax.legend(loc="upper right", fontsize=8.5)
bump(fig, 7.1)
fig.tight_layout()
es.save(fig, OUT / "d04-white-vs-bp.pdf")

# ------------------------------------------------------------- D5: due punti
d5, sd5 = 2 * B["points"], 2 * SE["points"]
q_lin, q_log = 0.10, float(np.log(1.10))
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.4),
                         gridspec_kw={"height_ratios": [1, 1.35]})
lo90, hi90 = d5 - T_1 * sd5, d5 + T_1 * sd5
lo95, hi95 = d5 - T_2 * sd5, d5 + T_2 * sd5
ax = axes[0]
ax.hlines(1.0, lo95, hi95, color=es.BLUE, lw=6, alpha=0.45,
          label="intervallo al 95% (test bilaterale)")
ax.hlines(0.0, lo90, hi90, color=es.TEAL, lw=6, alpha=0.60,
          label="intervallo al 90% (= test unilaterale al 5%)")
for v, y, col in ((lo95, 1.0, es.BLUE), (hi95, 1.0, es.BLUE),
                  (lo90, 0.0, es.TEAL), (hi90, 0.0, es.TEAL)):
    ax.vlines(v, y - 0.22, y + 0.22, color=col, lw=1.6)
    ax.annotate(it(v, 5), xy=(v, y - 0.28), ha="center", va="top",
                fontsize=8, color=col)
ax.plot([d5], [1.0], "o", color=es.BLUE, ms=8, zorder=6)
ax.annotate(f"stima $2\\hat\\beta_7$ = {it(d5, 5)}", xy=(d5, 1.0), xytext=(0, 12),
            textcoords="offset points", ha="center", fontsize=9,
            color=es.BLUE, fontweight="bold")
ax.axvline(q_lin, color=es.AMBER, lw=1.8, ls="-.")
ax.axvline(q_log, color=es.RED, lw=1.8)
ax.set_xlim(0.068, 0.172)
ax.set_ylim(-2.45, 2.95)
# i due commenti vanno negli angoli liberi di sinistra: prima uno sbordava a
# sinistra degli assi e l'altro finiva sotto la legenda
ax.annotate(f"soglia esatta $\\log(1{{,}}10)$ = {it(q_log, 5)}:\n"
            f"FUORI dall'intervallo al 90%\n$\\Rightarrow$ si rifiuta",
            xy=(0.015, 0.97), xycoords="axes fraction",
            ha="left", va="top", fontsize=8.5, color=es.RED, fontweight="bold")
ax.annotate(f"soglia lineare {it(q_lin, 5)}:\nDENTRO l'intervallo al 90%\n"
            f"$\\Rightarrow$ non si rifiuta",
            xy=(0.015, 0.03), xycoords="axes fraction",
            ha="left", va="bottom", fontsize=8.5, color=es.AMBER, fontweight="bold")
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xlabel(r"$2\beta_7=\Delta\log(wage)$ per 2 punti in piu' a partita")
ax.set_title("(a) la conclusione dipende da quale delle due soglie si adotta", loc="left")
ax.legend(loc="upper right", fontsize=8)
es.commas(ax, "x", decimals=2)

t_lin = (d5 - q_lin) / sd5
t_log = (d5 - q_log) / sd5
es.dist_test("t", DF, stat=t_log, crit=T_1, tail="right", ax=axes[1],
             statlabel=f"soglia $\\log(1{{,}}10)$: $t$ = {it(t_log, 4)}",
             pvalue=stats.t.sf(t_log, DF),
             title=r"(b) $H_0:2\beta_7=q$ contro $H_1:2\beta_7>q$  —  $t_{260}$, coda destra")
axes[1].axvline(t_lin, color=es.AMBER, lw=1.8, ls="-.",
                label=f"soglia 0,10: $t$ = {it(t_lin, 4)}  "
                      f"(p-value = {it(stats.t.sf(t_lin, DF), 4)})")
axes[1].set_xlim(-3.6, 3.9)
headroom(axes[1], 1.30)              # la densita' arrivava a toccare la legenda
axes[1].legend(loc="upper left", fontsize=8)
fig.tight_layout()
es.save(fig, OUT / "d05-due-punti-in-piu.pdf")

# --------------------------------------------------------- D6: esperienza ottima
e_star = -B["exper"] / (2 * B["expersq"])
g_max = -B["exper"] ** 2 / (4 * B["expersq"])
e = np.linspace(0, 22, 500)
g = B["exper"] * e + B["expersq"] * e ** 2
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.2), sharex=True)
axes[0].plot(e, g, color=es.BLUE, lw=1.8,
             label=r"$g(exper)=\beta_4\,exper+\beta_5\,exper^2$")
axes[0].fill_between(e, g, 0, color=es.BLUEBG)
axes[0].plot([e_star], [g_max], "*", color=es.RED, ms=16, zorder=6)
axes[0].axvline(e_star, color=es.RED, ls=":", lw=1.0)
# l'etichetta stava sotto la stella e la curva le passava attraverso:
# ora sta nel vuoto sopra il ramo crescente
axes[0].set_ylim(-0.06, 2.20)
axes[0].annotate(f"massimo in exper = {it(e_star, 3)} anni\n$g$ = {it(g_max, 4)}",
                 xy=(e_star, g_max), xytext=(-14, 12), textcoords="offset points",
                 ha="right", va="bottom", fontsize=9, color=es.RED, fontweight="bold")
axes[0].axvspan(15, 22, color=es.RED, alpha=0.06)
axes[0].annotate("zona di estrapolazione:\npochi giocatori\noltre i 15 anni",
                 xy=(18.6, 0.62), ha="center", fontsize=8, color=es.GRAY)
axes[0].set_ylabel("contributo a $\\log(wage)$")
axes[0].set_title("(a) profilo dell'esperienza: quadratica concava", loc="left")
axes[0].set_yticks([0, 0.5, 1.0, 1.5])
axes[0].legend(loc="lower left")
es.commas(axes[0], "y")

axes[1].plot(e, np.exp(g), color=es.TEAL, lw=1.8,
             label=r"$\exp\{g(exper)\}$ = salario relativo a un esordiente")
axes[1].plot([e_star], [np.exp(g_max)], "*", color=es.RED, ms=16, zorder=6)
axes[1].axvline(e_star, color=es.RED, ls=":", lw=1.0)
# etichetta sotto la stella, dentro gli assi: prima sbordava a destra
axes[1].set_ylim(0.85, 5.55)
axes[1].annotate(f"{it(np.exp(g_max), 3)} volte il salario\ndi un esordiente",
                 xy=(e_star, np.exp(g_max)), xytext=(-14, -12),
                 textcoords="offset points", ha="right", va="top",
                 fontsize=8.5, color=es.RED, fontweight="bold")
axes[1].axhline(1, color=es.GRAY, lw=0.8)
axes[1].set_xlabel("exper (anni da professionista)")
axes[1].set_ylabel("moltiplicatore salariale")
axes[1].set_title("(b) lo stesso profilo in livello", loc="left")
axes[1].set_yticks([1, 2, 3, 4, 5])
axes[1].legend(loc="upper left")
es.commas(axes[1], "y", decimals=1)
fig.tight_layout()
es.save(fig, OUT / "d06-esperienza-ottima.pdf")

# ------------------------------------------------------------------ Esercizio 2
# ------------------------------------------------------------------ D7: ADF
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.4),
                         gridspec_kw={"height_ratios": [1, 1.35]})
ax = axes[0]
XLO, XHI = -4.25, -1.00
ax.set_xlim(XLO, XHI)
ax.set_ylim(-1.30, 1.00)
ax.axvspan(XLO, -2.38, color=es.REDBG, alpha=0.75)
ax.axvline(-2.38, color=es.RED, lw=1.8)
ax.annotate("valore critico 5%\nfornito dal testo: $-$2,38", xy=(-2.38, 0.62),
            xytext=(5, 0), textcoords="offset points", fontsize=8.5,
            color=es.RED, fontweight="bold", va="center", ha="left")
# le due verticali tratteggiate si fermano sotto l'etichetta rossa e sopra la
# riga in fondo, che prima attraversavano entrambe
for v, lab, ha, dx in ((-2.85, "$-$2,85: DF con drift (note)", "right", -5),
                       (-1.95, "$-$1,95: DF senza drift (note)", "left", 5)):
    ax.axvline(v, ymin=0.20, ymax=0.72, color=es.GRAY, ls=":", lw=1.1)
    ax.annotate(lab, xy=(v, -0.60), xytext=(dx, 0), textcoords="offset points",
                fontsize=7.8, color=es.GRAY, va="center", ha=ha)
for v, lab, dy in ((-3.306, "gfr: $-$3,306", 0.22), (-2.871, "pe: $-$2,871", -0.22)):
    ax.plot([v], [dy], "o", color=es.BLUE, ms=9, zorder=6)
    ax.annotate(lab, xy=(v, dy), xytext=(0, 12), textcoords="offset points",
                ha="center", fontsize=9, color=es.BLUE, fontweight="bold")
ax.annotate("regione di rifiuto di $H_0$ (radice unitaria)", xy=(XLO + 0.08, -1.05),
            fontsize=8.5, color=es.RED, ha="left", va="center")
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("statistica ADF (test unilaterale sinistro)")
ax.set_title("(a) entrambe le statistiche cadono a sinistra del valore critico", loc="left")
es.commas(ax, "x", decimals=2)

rng = np.random.default_rng(SEED)
T = 72
eps = rng.normal(0, 1, T)
rw = np.cumsum(eps)
ar = np.zeros(T)
for t in range(1, T):
    ar[t] = 0.55 * ar[t - 1] + eps[t]
yrs = np.arange(1913, 1913 + T)
axes[1].plot(yrs, rw, color=es.RED, lw=1.4, label=r"random walk ($H_0$): $\delta=0$")
axes[1].plot(yrs, ar, color=es.GREEN, lw=1.4,
             label=r"AR(1) stazionario ($H_1$): $\beta_1=0{,}55$")
axes[1].axhline(0, color=es.GRAY, lw=0.8)
axes[1].set_xlabel("anno")
axes[1].set_ylabel("livello della serie")
axes[1].set_title("(b) simulazione illustrativa (seme 20240613): i due mondi a confronto",
                  loc="left")
axes[1].legend(loc="upper left")
es.commas(axes[1], "y", decimals=0)
fig.tight_layout()
es.save(fig, OUT / "d07-adf-radici-unitarie.pdf")

# ----------------------------------------------------- D8: Engle-Granger
fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.4),
                         gridspec_kw={"height_ratios": [0.85, 1.4]})
ax = axes[0]
ax.set_xlim(0, 1)
ax.axhspan(-1, 1, xmin=0, xmax=0.05, color=es.REDBG)
ax.axvline(0.05, color=es.RED, lw=1.6)
ax.annotate("rifiuto se p-value < 0,05\n(= cointegrazione)", xy=(0.05, -0.55),
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
ax.set_xlabel(r"p-value asintotico della statistica $\tau_c(2)$ sui residui $\hat u_t$")
ax.set_title("(a) l'esito del test di Engle-Granger", loc="left")
es.commas(ax, "x", decimals=2)

def eg_stat(y, x):
    """t di Dickey-Fuller (con costante) sui residui della regressione statica."""
    Xm = np.column_stack([np.ones_like(x), x])
    u = y - Xm @ np.linalg.lstsq(Xm, y, rcond=None)[0]
    du, ul = np.diff(u), u[:-1]
    Z = np.column_stack([np.ones_like(ul), ul])
    bb, *_ = np.linalg.lstsq(Z, du, rcond=None)
    e = du - Z @ bb
    s2 = e @ e / (len(du) - 2)
    V = s2 * np.linalg.inv(Z.T @ Z)
    return bb[1] / np.sqrt(V[1, 1])


rng = np.random.default_rng(SEED + 7)
T, REP8 = 72, 3000
tau_i0 = np.empty(REP8)
tau_i1 = np.empty(REP8)
for i in range(REP8):
    ex, ey = rng.normal(0, 1, T), rng.normal(0, 1, T)
    xs = np.zeros(T); ys = np.zeros(T)
    for t in range(1, T):
        xs[t] = 0.5 * xs[t - 1] + ex[t]
        ys[t] = 0.5 * ys[t - 1] + ey[t]
    tau_i0[i] = eg_stat(ys, xs)
    tau_i1[i] = eg_stat(np.cumsum(ey), np.cumsum(ex))

bins = np.linspace(-9, 1, 70)
axes[1].hist(tau_i0, bins=bins, density=True, color=es.GREEN, alpha=0.55,
             label=r"serie entrambe $I(0)$ e indipendenti")
axes[1].hist(tau_i1, bins=bins, density=True, color=es.RED, alpha=0.50,
             label=r"due random walk indipendenti (nessuna cointegrazione)")
q_i0, q_i1 = np.median(tau_i0), np.median(tau_i1)
for q, col, lab in ((q_i0, es.GREEN, "mediana"), (q_i1, es.RED, "mediana")):
    axes[1].axvline(q, color=col, ls="--", lw=1.2)
    axes[1].annotate(f"{lab} {it(q, 2)}", xy=(q, 0.40), xytext=(0, 0),
                     textcoords="offset points", rotation=90, ha="right",
                     va="top", fontsize=8, color=col, fontweight="bold")
p68_i1 = float(np.mean(tau_i1 > np.quantile(tau_i1, 1 - 0.68)))
q68 = float(np.quantile(tau_i1, 0.68))
axes[1].axvline(q68, color=es.BLUE, lw=2.0,
                label=f"statistica con p-value = 0,68 sotto $H_0$: {it(q68, 2)}")
n_i0 = int(np.sum(tau_i0 > q68))
axes[1].annotate(f"con due serie $I(0)$ solo {n_i0} repliche\n"
                 f"su {REP8} arrivano cosi' vicino a zero",
                 xy=(0.985, 0.97), xycoords="axes fraction", ha="right", va="top",
                 fontsize=8.5, color=es.BLUE, fontweight="bold")
axes[1].set_xlabel(r"statistica di Dickey-Fuller sui residui $\hat u_t$")
axes[1].set_ylabel("densita' simulata")
axes[1].set_yticks([])
axes[1].set_xlim(-9, 1)
axes[1].set_title("(b) simulazione illustrativa (seme 20240620, 3000 repliche, $T=72$):\n"
                  "con quale dei due mondi e' compatibile un p-value del 68%?", loc="left")
axes[1].legend(loc="upper left", fontsize=7.8)
es.commas(axes[1], "x", decimals=0)
fig.tight_layout()
es.save(fig, OUT / "d08-engle-granger.pdf")

# ------------------------------------------------------------------- D9: QLR
def chow_sequence(y, x, trim=0.15):
    """Sequenza delle F di Chow (2 restrizioni) per ogni data candidata."""
    T = len(y)
    lo, hi = int(np.floor(trim * T)) + 2, int(np.ceil((1 - trim) * T)) - 1
    cx, cy = np.cumsum(x), np.cumsum(y)
    cxx, cyy, cxy = np.cumsum(x * x), np.cumsum(y * y), np.cumsum(x * y)

    def ssr(n, sx, sy, sxx, syy, sxy):
        sxx_c = sxx - sx * sx / n
        syy_c = syy - sy * sy / n
        sxy_c = sxy - sx * sy / n
        return syy_c - np.where(sxx_c > 1e-12, sxy_c ** 2 / np.maximum(sxx_c, 1e-12), 0.0)

    ssr_r = ssr(T, cx[-1], cy[-1], cxx[-1], cyy[-1], cxy[-1])
    taus = np.arange(lo, hi + 1)
    n1 = taus.astype(float)
    s1 = ssr(n1, cx[taus - 1], cy[taus - 1], cxx[taus - 1], cyy[taus - 1], cxy[taus - 1])
    n2 = T - n1
    s2 = ssr(n2, cx[-1] - cx[taus - 1], cy[-1] - cy[taus - 1],
             cxx[-1] - cxx[taus - 1], cyy[-1] - cyy[taus - 1], cxy[-1] - cxy[taus - 1])
    ssr_u = s1 + s2
    return taus, ((ssr_r - ssr_u) / 2) / (ssr_u / (T - 4))


T9 = 71                                   # 1914-1984: differenze prime annuali
rng = np.random.default_rng(SEED + 2)
REP = 4000
qlr_null = np.empty(REP)
for i in range(REP):
    xx = rng.normal(0, 1, T9)
    yy = rng.normal(0, 1, T9)
    qlr_null[i] = chow_sequence(yy, xx)[1].max()
q95 = np.quantile(qlr_null, 0.95)
q_obs = np.quantile(qlr_null, 1 - 0.372)   # valore con p-value QLR = 0,372
p_f_naive = stats.f.sf(q_obs, 2, T9 - 4)

rng = np.random.default_rng(34)   # seme scelto perche' il massimo cade nel 1943
xx = rng.normal(0, 1, T9); yy = rng.normal(0, 1, T9)
taus, seq = chow_sequence(yy, xx)
seq = seq * (q_obs / seq.max())            # riscalata: massimo = statistica implicata
anni = 1914 + taus - 1
i_max = int(np.argmax(seq))

fig, axes = plt.subplots(2, 1, figsize=(6.3, 5.6))
axes[0].plot(anni, seq, color=es.BLUE, lw=1.5, label=r"sequenza $F_\tau$ (Chow, $s=2$)")
axes[0].plot([anni[i_max]], [seq[i_max]], "*", color=es.RED, ms=15, zorder=6)
axes[0].annotate(f"massimo = QLR = {it(q_obs, 3)}\np-value QLR = 0,372",
                 xy=(anni[i_max], seq[i_max]), xytext=(-10, -46),
                 textcoords="offset points", ha="right", fontsize=8.5,
                 color=es.RED, fontweight="bold")
axes[0].axhline(stats.f.ppf(0.95, 2, T9 - 4), color=es.AMBER, ls="--", lw=1.2,
                label=f"critico $F_{{2,67}}$ al 5% = {it(stats.f.ppf(0.95, 2, T9-4), 3)}"
                      " (SBAGLIATO)")
axes[0].axhline(q95, color=es.GREEN, ls="--", lw=1.3,
                label=f"critico QLR al 5% simulato = {it(q95, 3)}")
axes[0].set_xlabel("data candidata del break")
axes[0].set_ylabel("statistica di Chow")
axes[0].set_title("(a) simulazione illustrativa (seme 34): la sequenza di Chow,\n"
                  "riscalata perche' il massimo coincida con il QLR implicato dal testo",
                  loc="left")
axes[0].legend(loc="upper left", fontsize=7.6)
es.commas(axes[0], "y", decimals=1)

grid = np.linspace(0, 16, 500)
axes[1].plot(grid, stats.f.pdf(grid, 2, T9 - 4), color=es.AMBER, lw=1.6,
             label=r"$F_{2,67}$: distribuzione di UNA Chow a data nota")
kde = stats.gaussian_kde(qlr_null)
axes[1].plot(grid, kde(grid), color=es.GREEN, lw=1.8,
             label=f"QLR = massimo su {len(taus)} date (simulato, 4000 repliche)")
axes[1].axvline(q_obs, color=es.RED, lw=1.8,
                label=f"statistica implicata = {it(q_obs, 3)}")
axes[1].annotate(f"sulle tavole $F$ lo stesso valore\ndarebbe p-value = {it(p_f_naive, 4)},\n"
                 f"sei volte piu' piccolo di 0,372",
                 xy=(q_obs, 0.30), xytext=(14, 10), textcoords="offset points",
                 fontsize=8.5, color=es.RED, fontweight="bold")
axes[1].set_xlabel("valore della statistica")
axes[1].set_ylabel("densita'")
axes[1].set_yticks([])
axes[1].set_xlim(0, 16)
axes[1].set_title("(b) perche' il QLR non si legge sulle tavole della $F$", loc="left")
axes[1].legend(loc="upper right", fontsize=8)
es.commas(axes[1], "x", decimals=0)
fig.tight_layout()
es.save(fig, OUT / "d09-qlr-break.pdf")
print(f"  [D9] QLR crit 5% simulato = {q95:.4f}; statistica con p=0,372 -> {q_obs:.4f}; "
      f"p-value F ingenuo = {p_f_naive:.5f}")

# --------------------------------------------------------------- D10: ACF/PACF
ACF_OBS = [0.45, 0.16, -0.23, -0.13, -0.21, -0.08, -0.10,
           0.03, 0.06, 0.19, 0.14, 0.13, -0.13, -0.22]
PACF_OBS = [0.45, -0.03, -0.38, 0.19, -0.16, -0.07, 0.01,
            0.01, 0.04, 0.12, 0.01, 0.04, -0.22, -0.07]
T10 = 71
PHI = np.array([0.4480, 0.1441, -0.3790])       # AR(3) via Durbin-Levinson


def ar_acf(phi, maxlag):
    p = len(phi)
    M = np.zeros((p, p)); rhs = np.zeros(p)
    for k in range(1, p + 1):
        M[k - 1, k - 1] = 1.0
        for j in range(1, p + 1):
            if k - j == 0:
                rhs[k - 1] += phi[j - 1]
            else:
                M[k - 1, abs(k - j) - 1] -= phi[j - 1]
    rho = np.zeros(maxlag + 1); rho[0] = 1.0
    rho[1:p + 1] = np.linalg.solve(M, rhs)
    for k in range(p + 1, maxlag + 1):
        rho[k] = sum(phi[j] * rho[k - 1 - j] for j in range(p))
    return rho


def pacf_from_acf(rho, maxlag):
    out, prev = [], []
    for k in range(1, maxlag + 1):
        if k == 1:
            pk = rho[1]; cur = [pk]
        else:
            num = rho[k] - sum(prev[j] * rho[k - 1 - j] for j in range(k - 1))
            den = 1 - sum(prev[j] * rho[j + 1] for j in range(k - 1))
            pk = num / den
            cur = [prev[j] - pk * prev[k - 2 - j] for j in range(k - 1)] + [pk]
        out.append(pk); prev = cur
    return np.array(out)


rho_th = ar_acf(PHI, 14)
acf_th = list(rho_th[1:])
pacf_th = list(pacf_from_acf(rho_th, 14))
roots = np.roots(np.r_[-PHI[::-1], 1.0])
print("  [D10] moduli delle radici AR(3):", np.round(np.abs(roots), 3))

fig, axs = plt.subplots(2, 2, figsize=(7.2, 4.9), sharex=True)
es.acf_pacf(ACF_OBS, PACF_OBS, n=T10, axes=[axs[0, 0], axs[1, 0]])
es.acf_pacf(acf_th, pacf_th, n=T10, axes=[axs[0, 1], axs[1, 1]])
axs[0, 0].set_title(r"(a) letta dalla Figura 2 del testo ($\Delta gfr$)", loc="left")
axs[0, 1].set_title("(b) teorica del modello proposto: AR(3)", loc="left")
for ax in axs.ravel():
    ax.set_ylim(-0.48, 0.58)
    ax.set_xticks(range(0, 15, 2))
    ax.legend(loc="lower right", fontsize=7.2)
fig.tight_layout()
es.save(fig, OUT / "d10-acf-pacf-dgfr.pdf")

print("fatto.")
