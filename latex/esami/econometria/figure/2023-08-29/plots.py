#!/usr/bin/env python3
"""Figure per la soluzione dell'appello di Econometria del 29 agosto 2023.

Esercizio 1 — studenti-atleti (log-lin, interazione season x tothrs, White, VIF).
Esercizio 2 — petrolio e occupazione in Texas (ADF, cointegrazione, due ECM).

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
    theta, se = 30 * B_TOT1, 30 * SE_TOT1
    lo, hi = theta - 1.96 * se, theta + 1.96 * se
    h0a, h0b = 0.02, np.log(1.02)
    t_obs = (theta - h0a) / se

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(6.2, 5.0), gridspec_kw={"height_ratios": [1.0, 1.45]})

    ci_soglie(ax1, theta, lo, hi,
              [(h0a, r"$H_0$: 0,0200" + "\nfuori dall'IC: rifiuto", es.RED, 0.45),
               (h0b, r"$\log(1{,}02) = 0{,}0198$", es.TEAL, -0.50)],
              xlabel=r"$\theta = 30\,\beta_4$  (punti di log-gpa)", pad=0.24,
              title="(a) IC al 95% per l'effetto di 30 ore: entrambe le soglie restano fuori")

    es.dist_test("z", stat=t_obs, crit=1.645, tail="right", ax=ax2,
                 title="(b) test unilaterale destro  $H_0:\\theta = 0{,}02$  contro  $H_1:\\theta > 0{,}02$",
                 statlabel=f"$t$ osservata = {n(t_obs, 4)}", pvalue=0.0146,
                 critlabel=r"regione di rifiuto: $z > 1{,}645$ (5%)")
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
    gap_log = B_SEA2 + B_SHRS * h
    gap_pct = 100 * (np.exp(gap_log) - 1)
    turn = -B_SEA2 / B_SHRS
    at50 = 100 * (np.exp(B_SEA2 + 50 * B_SHRS) - 1)

    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    ax.plot(h, gap_pct, color=es.BLUE, lw=1.7,
            label=r"$100\,[\exp(\beta_2 + \beta_5\,\mathrm{tothrs}) - 1]$")
    ax.axhline(0, color=es.GRAY, lw=0.9)
    ax.fill_between(h, gap_pct, 0, where=gap_pct >= 0, color=es.GREENBG)
    ax.fill_between(h, gap_pct, 0, where=gap_pct < 0, color=es.REDBG)

    ax.axvline(turn, color=es.RED, ls=":", lw=1.1)
    ax.plot([turn], [0], "o", color=es.RED, ms=6, zorder=6)
    ax.annotate("gap nullo a tothrs = " + n(turn, 2), xy=(turn, 0),
                xytext=(8, 64), textcoords="offset points",
                fontsize=8.5, color=es.RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))

    ax.plot([50], [at50], "*", color=es.TEAL, ms=15, zorder=7)
    ax.annotate("tothrs = 50:  gap = +" + n(at50, 2) + r"%", xy=(50, at50),
                xytext=(12, -16), textcoords="offset points", va="top",
                fontsize=9, color=es.TEAL, fontweight="bold")

    ax.plot([0], [100 * (np.exp(B_SEA2) - 1)], "s", color=es.AMBER, ms=6, zorder=6)
    ax.annotate("tothrs = 0:  gap = " + n(100 * (np.exp(B_SEA2) - 1), 2) + r"%",
                xy=(0, 100 * (np.exp(B_SEA2) - 1)), xytext=(54, -12),
                textcoords="offset points", va="top", fontsize=8.5, color=es.AMBER,
                arrowprops=dict(arrowstyle="->", color=es.AMBER, lw=0.8))

    es.commas(ax, "both", decimals=1)
    ax.set_xlabel("tothrs (ore frequentate)")
    ax.set_ylabel("effetto di season su gpa (%)")
    ax.set_title("Impatto della stagione agonistica in funzione delle ore frequentate",
                 loc="left")
    ax.legend(loc="upper left")
    ax.set_xlim(0, 120)
    ax.set_ylim(-7.5, 26.5)
    fig.tight_layout()
    es.save(fig, OUT / "d03-gap-season-tothrs.pdf")


# ================================================ D4 — effetto marginale tothrs
def d04():
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(6.2, 5.2), gridspec_kw={"height_ratios": [1.15, 1.0]})

    h = np.linspace(0, 120, 300)
    ax1.plot(h, 100 * (np.exp(B_TOT2 * h) - 1), color=es.BLUE, lw=1.8,
             label=r"season = 0:  $100(e^{\beta_4\,\mathrm{tothrs}}-1)$,  $\beta_4 = 0{,}00130725$")
    ax1.plot(h, 100 * (np.exp((B_TOT2 + B_SHRS) * h) - 1), color=es.AMBER, lw=1.8,
             label=r"season = 1:  $100(e^{(\beta_4+\beta_5)\mathrm{tothrs}}-1)$,  "
                   r"$\beta_4+\beta_5 = 0{,}00328211$")
    ax1.fill_between(h, 100 * (np.exp(B_TOT2 * h) - 1),
                     100 * (np.exp((B_TOT2 + B_SHRS) * h) - 1),
                     color=es.BLUEBG, alpha=0.9)
    for hh in (50, 100):
        ax1.axvline(hh, color=es.RULE, lw=0.8)
    ax1.annotate("la differenza fra le pendenze in log-gpa\nè esattamente  " +
                 r"$\beta_5 = 0{,}00197486$",
                 xy=(88, 0.5 * (100 * (np.exp(B_TOT2 * 88) - 1) +
                                100 * (np.exp((B_TOT2 + B_SHRS) * 88) - 1))),
                 xytext=(0.27, 0.60), textcoords="axes fraction", va="top",
                 fontsize=8.5, color=es.GRAY,
                 arrowprops=dict(arrowstyle="->", color=es.GRAY, lw=0.8))
    es.commas(ax1, "both", decimals=1)
    ax1.set_xlabel("tothrs (ore frequentate)")
    ax1.set_ylabel("gpa rispetto a tothrs = 0 (%)")
    ax1.set_title("(a) profili esatti di gpa: le pendenze in log-gpa differiscono di "
                  r"$\beta_5$", loc="left")
    ax1.legend(loc="upper left")
    ax1.set_xlim(0, 120)
    ax1.set_ylim(0, 66)

    es.dist_test("z", stat=B_SHRS / SE_SHRS, crit=1.96, tail="two", ax=ax2,
                 pvalue=0.0109, statlabel=r"$t$ su $\beta_5$ = 2,5441",
                 title=r"(b) $H_0:\beta_5 = 0$ (effetto marginale indipendente da season) contro $H_1:\beta_5 \neq 0$")
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
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(6.2, 4.6), gridspec_kw={"height_ratios": [1.0, 1.05]})

    ci_soglie(ax1, b, lo, hi,
              [(0.25, r"$H_0$: 0,2500" + "\ndentro l'IC", es.AMBER, 0.45),
               (np.log(1.25), r"$\log(1{,}25) = 0{,}2231$" + "\ndentro l'IC", es.TEAL, -0.50)],
              xlabel=r"$\beta_3$  (punti di log-gpa)",
              title=r"(a) IC al 95% per $\beta_3$: entrambe le soglie cadono dentro")

    vals = [100 * b, 100 * (np.exp(b) - 1)]
    labs = ["approssimazione\n" + r"$100\,\beta_3$",
            "versione esatta\n" + r"$100(e^{\beta_3}-1)$"]
    cols = [es.GRAY, es.BLUE]
    ypos = [0, 1]
    ax2.barh(ypos, vals, color=cols, height=0.5, alpha=0.85)
    # valori dentro le barre: fuori cadrebbero sull'IC esatto disegnato a y = 1
    for y, v in zip(ypos, vals):
        ax2.annotate(n(v, 2) + r"%", xy=(v, y), xytext=(-8, 0),
                     textcoords="offset points", ha="right", va="center",
                     fontsize=9, fontweight="bold", color="white")
    lo_p, hi_p = 100 * (np.exp(lo) - 1), 100 * (np.exp(hi) - 1)
    ax2.hlines(1, lo_p, hi_p, color=es.BLUE, lw=2.4, alpha=0.45)
    ax2.vlines([lo_p, hi_p], 0.87, 1.13, color=es.BLUE, lw=1.3, alpha=0.7)
    ax2.annotate("IC esatto sul premio:  [" + n(lo_p, 2) + r"%; " +
                 n(hi_p, 2) + r"%]", xy=(0.6, 1.34), ha="left", va="bottom",
                 fontsize=8.5, color=es.BLUE)
    ax2.set_ylim(-0.45, 1.85)
    ax2.axvline(25, color=es.RED, ls="--", lw=1.4, label=r"soglia del 25%")
    ax2.set_yticks(ypos)
    ax2.set_yticklabels(labs, fontsize=8.5)
    ax2.set_xlim(0, 38)
    es.commas(ax2, "x", decimals=0)
    ax2.grid(axis="y", visible=False)
    ax2.set_xlabel("premio femminile su gpa (%)")
    ax2.set_title("(b) la stima puntuale sta sotto o sopra il 25% a seconda della convenzione",
                  loc="left")
    ax2.legend(loc="lower right")
    fig.tight_layout()
    es.save(fig, OUT / "d05-premio-femminile.pdf")


# ================================================================== D6 — VIF
def d06():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.2, 5.0))

    names = list(VIF)
    v = np.array([VIF[k] for k in names])
    r = np.sqrt(v)
    x = np.arange(len(names))
    ax1.bar(x - 0.19, v, width=0.36, color=es.RULE, label=r"$\mathrm{VIF}_j$ (varianza)")
    ax1.bar(x + 0.19, r, width=0.36, color=es.BLUE,
            label=r"$\sqrt{\mathrm{VIF}_j}$ (errore standard)")
    for xi, vi, ri in zip(x, v, r):
        ax1.annotate(n(vi, 3), xy=(xi - 0.19, vi), xytext=(0, 4),
                     textcoords="offset points", ha="center", fontsize=8.2,
                     color=es.GRAY)
        ax1.annotate(n(ri, 3), xy=(xi + 0.19, ri), xytext=(0, 4),
                     textcoords="offset points", ha="center", fontsize=8.2,
                     color=es.BLUE, fontweight="bold")
    ax1.axhline(1.0, color=es.GREEN, lw=1.0, ls=":")
    ax1.set_xticks(x)
    ax1.set_xticklabels(names, fontsize=9)
    es.commas(ax1, "y", decimals=1)
    ax1.set_ylim(0, 6.3)
    ax1.set_ylabel("fattore di gonfiaggio")
    ax1.set_title("(a) il VIF gonfia la varianza, la sua radice l'errore standard", loc="left")
    ax1.legend(loc="upper left", fontsize=8.3)

    se_perp = SE_SHRS / np.sqrt(VIF["shrs"])
    t_perp, t_obs = B_SHRS / se_perp, B_SHRS / SE_SHRS
    ax2.bar([0, 1], [t_perp, t_obs], width=0.42, color=[es.GREEN, es.AMBER], alpha=0.85)
    ax2.axhline(1.96, color=es.RED, ls="--", lw=1.2, label=r"soglia $|t| = 1{,}96$")
    for xi, ti in zip([0, 1], [t_perp, t_obs]):
        ax2.annotate("t = " + n(ti, 3), xy=(xi, ti), xytext=(0, 4),
                     textcoords="offset points", ha="center", fontsize=9,
                     fontweight="bold", color=es.INK)
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(["regressori ortogonali\n" + r"se $= 0{,}000357$",
                         "collinearità osservata\n" + r"se $= 0{,}000776$"], fontsize=8.5)
    es.commas(ax2, "y", decimals=1)
    ax2.set_xlim(-0.62, 1.62)
    ax2.set_ylim(0, 6.4)
    ax2.grid(axis="x", visible=False)
    ax2.set_ylabel(r"rapporto $t$ su $\beta_5$")
    ax2.set_title(r"(b) il prezzo pagato dalla $t$ di shrs: da 5,538 a 2,544", loc="left")
    ax2.legend(loc="upper right", fontsize=8.3)
    fig.tight_layout()
    es.save(fig, OUT / "d06-vif-shrs.pdf")


# ---------------------------------------- primitiva locale: test su retta reale
def _stat_line(ax, data, crit, title, xlab, note):
    """Statistiche osservate su una retta numerica, con regione di rifiuto."""
    names = list(data)
    stats_ = [data[k][0] for k in names]
    lo = min(min(stats_), crit) - 1.1
    hi = max(max(stats_), 0.0) + 0.9
    ax.axvspan(lo, crit, color=es.REDBG, alpha=0.85)
    ax.axvspan(crit, hi, color=es.BLUEBG, alpha=0.8)
    ax.annotate(f"$t <$ {n(crit, 2)}", xy=(crit, -0.45), xytext=(-6, 0),
                textcoords="offset points", ha="right", va="center",
                fontsize=8.5, color=es.RED, fontweight="bold")
    # la retta del critico si ferma sotto la fascia delle diciture in alto
    ax.vlines(crit, -0.65, len(names) + 0.12, color=es.RED, ls="--", lw=1.3)
    for i, k in enumerate(names):
        st = data[k][0]
        ax.plot([st], [i], "o", color=es.BLUE, ms=8, zorder=6)
        # se la statistica sfiora il critico, l'etichetta va di fianco al punto
        vicino = abs(st - crit) < 0.5
        ax.annotate(n(st, 4), xy=(st, i),
                    xytext=(11, 3) if vicino else (0, 9),
                    textcoords="offset points",
                    ha="left" if vicino else "center",
                    fontsize=8.5, color=es.BLUE, fontweight="bold")
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=9)
    ax.set_ylim(-0.65, len(names) + 0.9)
    ax.set_xlim(lo, hi)
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x", decimals=1)
    ax.annotate("rifiuto di $H_0$: serie stazionaria" if "ADF" in xlab
                else "rifiuto di $H_0$: cointegrazione",
                xy=(0.015, 0.97), xycoords="axes fraction", ha="left", va="top",
                fontsize=8.5, color=es.RED, fontweight="bold")
    ax.annotate("non rifiuto di $H_0$", xy=(0.985, 0.97), xycoords="axes fraction",
                ha="right", va="top", fontsize=8.5, color=es.BLUE, fontweight="bold")
    ax.set_xlabel(xlab + "\n" + note, fontsize=8.5)
    ax.set_title(title, loc="left")


def _pvalue_bars(ax, data, title):
    names = list(data)
    p = [data[k][1] for k in names]
    y = np.arange(len(names))
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
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.2, 5.0))
    _stat_line(ax1, ADF, -2.85,
               "(a) statistiche ADF e regione di rifiuto",
               "statistica ADF",
               "riferimento minimale $-2{,}85$ (DF con drift, 5%: unico critico\n"
               "tabulato nelle note); con costante e trend il critico è $-3{,}41$,\n"
               "ancora più a sinistra. Per l'ADF vale il p-value")
    _pvalue_bars(ax2, ADF, "(b) p-value: nessuno scende sotto il 5%")
    fig.tight_layout()
    es.save(fig, OUT / "d07-radici-unitarie.pdf")


# ========================================================= D8 — cointegrazione
def d08():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.2, 5.0))
    _stat_line(ax1, CDF, -3.34,
               "(a) statistiche CDF (Engle-Granger) e regione di rifiuto",
               r"statistica CDF, $\tau_c(2)$",
               "il critico al 5% della $\\tau_c(2)$ non è tabulato nelle note:\n"
               "$-3{,}34$ è indicativo, la decisione usa il p-value")
    _pvalue_bars(ax2, CDF, "(b) p-value: tutti vicini a 1, nessuna cointegrazione")
    fig.tight_layout()
    es.save(fig, OUT / "d08-cointegrazione.pdf")


# ======================================================= D9 — assorbimento ECM
def d09():
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(6.2, 5.4), gridspec_kw={"height_ratios": [1.35, 1.0]})
    _, _, tab = es.decay(LAM_TX, horizon=14, targets=(0.5, 0.8), ax=ax1,
                         title=r"(a) quota di disequilibrio residua, $(1+\hat\lambda)^h$ con $\hat\lambda = -0{,}218680$")
    # la primitiva scrive "(1-0,2187)^h" dentro $...$ e mathtext apre uno
    # spazio dopo la virgola: rietichetto tenendo il numero fuori dal math
    ax1.lines[0].set_label(r"$(1+\hat\lambda)^h$  con  $1+\hat\lambda$ = 0,7813")
    es.commas(ax1, "y", decimals=1)
    for t in ax1.texts:
        t.set_fontsize(8.5)
    ax1.legend(loc="upper right")
    print("   orizzonti D9:", tab)

    lo, hi = LAM_TX - 1.96 * SE_LAM_TX, LAM_TX + 1.96 * SE_LAM_TX
    grid = np.linspace(lo, hi, 400)
    hstar = np.ceil(np.log(0.5) / np.log(1 + grid))
    ax2.step(grid, hstar, where="post", color=es.BLUE, lw=1.7,
             label=r"$h^\star = \lceil \ln(0{,}5)/\ln(1+\lambda) \rceil$")
    ax2.fill_between(grid, 0, hstar, step="post", color=es.BLUEBG)
    ax2.plot([LAM_TX], [3], "*", color=es.RED, ms=15, zorder=6)
    ax2.annotate(r"stima puntuale: $h^\star = 3$", xy=(LAM_TX, 3), xytext=(10, -22),
                 textcoords="offset points", fontsize=8.5, color=es.RED,
                 fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))
    ax2.set_xlim(lo, hi)
    ax2.set_ylim(0, 9.5)
    es.commas(ax2, "x", decimals=2)
    es.commas(ax2, "y", decimals=0)
    ax2.set_xlabel(r"$\lambda$ entro l'IC al 95%:  $[-0{,}3496;\ -0{,}0878]$")
    ax2.set_ylabel("trimestri per il 50%")
    ax2.set_title("(b) sensibilità dell'orizzonte all'incertezza su $\\lambda$: da 2 a 8 trimestri",
                  loc="left")
    ax2.legend(loc="upper left")
    fig.tight_layout()
    es.save(fig, OUT / "d09-assorbimento-ecm.pdf")


# =================================================== D10 — disequilibrio < 0
def d10():
    # gamma_0 e' significativa (p = 0,0225): la legge di moto e' AFFINE,
    # z_t = (1+lambda) z_{t-1} + gamma_0, con punto di riposo z* = -gamma_0/lambda.
    # Entrambi i pannelli usano questa stessa legge.
    phi = 1 + LAM_IDX
    zstar = -G0_IDX / LAM_IDX               # +1,255884
    z0 = -1.0                               # disequilibrio normalizzato
    h = np.arange(0, 13)
    z = zstar + phi ** h * (z0 - zstar)     # z_{t-1+h}
    corr = LAM_IDX * z                      # correzione dell'errore
    drift = np.full_like(corr, G0_IDX)      # deriva costante
    tot = drift + corr                      # E[Delta IDX] = lambda (z - z*)
    h_zero = np.log(zstar / (zstar - z0)) / np.log(phi)                   # 3,756
    h_half = np.log((0.5 * z0 - zstar) / (z0 - zstar)) / np.log(phi)      # 1,607
    h_life = np.ceil(np.log(0.5) / np.log(phi))                           # 5
    print("   D10: z* =", round(zstar, 6), " zero a h =", round(h_zero, 4),
          " metà gap a h =", round(h_half, 4), " emivita da z* =", int(h_life))

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(6.2, 5.6), gridspec_kw={"height_ratios": [1.2, 1.0]})

    ax1.plot(h, z, "o-", color=es.BLUE, lw=1.7, ms=4.5,
             label=r"$z_{t-1+h} = z^\star + (1+\hat\lambda)^h (z_{t-1}-z^\star)$")
    ax1.axhline(0, color=es.GREEN, lw=1.3, ls="--",
                label="relazione di lungo periodo stimata ($z = 0$)")
    ax1.axhline(zstar, color=es.AMBER, lw=1.4, ls="-.",
                label=r"punto di riposo $z^\star = -\hat\gamma_0/\hat\lambda = +1{,}2559$")
    ax1.fill_between(h, np.minimum(z, 0.0), 0, color=es.REDBG, alpha=0.9)
    ax1.fill_between(h, np.maximum(z, 0.0), 0, color=es.GREENBG, alpha=0.9)

    # la verticale si ferma sulla curva: piu' in alto taglierebbe la legenda
    ax1.vlines(h_half, -1.8, -0.674, color=es.TEAL, ls=":", lw=1.1)
    ax1.annotate("metà del gap iniziale:\n" + r"$h = 1{,}61 \to 2$ trimestri",
                 xy=(h_half, -0.674), xytext=(26, -19), textcoords="offset points",
                 va="top", fontsize=8.2, color=es.TEAL, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=es.TEAL, lw=0.8))
    ax1.plot([h_zero], [0.0], "*", color=es.RED, ms=15, zorder=7)
    ax1.annotate(r"attraversa lo zero a $h = 3{,}76$", xy=(h_zero, 0.0),
                 xytext=(14, -18), textcoords="offset points", va="top",
                 fontsize=8.5, color=es.RED, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))
    es.commas(ax1, "y", decimals=2)
    ax1.set_xlabel("trimestri dopo il disequilibrio ($h$)")
    ax1.set_ylabel(r"$z$ (normalizzato a $-1$)")
    ax1.set_title(r"(a) con $\hat\gamma_0$ significativa il bersaglio non è lo zero, "
                  r"ma $z^\star > 0$", loc="left")
    ax1.legend(loc="upper left", fontsize=8.3)
    ax1.set_ylim(-1.8, 2.9)

    ax2.bar(h, drift, width=0.62, color=es.RULE,
            label=r"deriva $\hat\gamma_0 = +0{,}1813$")
    ax2.bar(h, corr, width=0.62, bottom=drift, color=es.GREEN, alpha=0.85,
            label=r"correzione $\hat\lambda\,z$: $>0$ finché $z<0$")
    ax2.plot(h, tot, "o-", color=es.BLUE, lw=1.5, ms=4,
             label=r"totale $\operatorname{E}[\Delta IDX] = \hat\lambda (z-z^\star) > 0$")
    ax2.axhline(0, color=es.GRAY, lw=0.8)
    for i in (0, 1, 4):
        ax2.annotate("+" + n(tot[i], 4), xy=(h[i], tot[i]), xytext=(0, 7),
                     textcoords="offset points", ha="center", fontsize=8.2,
                     fontweight="bold", color=es.INK)
    es.commas(ax2, "y", decimals=2)
    ax2.set_xlabel("trimestri dopo il disequilibrio ($h$)")
    ax2.set_ylabel(r"$\operatorname{E}[\Delta IDX]$")
    ax2.set_ylim(-0.09, 0.53)
    ax2.set_title(r"(b) il totale resta positivo, ma dal quarto trimestre la "
                  r"correzione cambia segno", loc="left")
    ax2.legend(loc="upper right", fontsize=8.3)
    fig.tight_layout()
    es.save(fig, OUT / "d10-disequilibrio-negativo.pdf")


if __name__ == "__main__":
    for fn in (d01, d02, d03, d04, d05, d06, d07, d08, d09, d10):
        fn()
    print("fatto.")
