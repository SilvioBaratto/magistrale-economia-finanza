#!/usr/bin/env python3
"""Figure per la soluzione dell'esame di Econometria del 21 dicembre 2023.

Esercizio 1 (salari, istruzione, IQ) usa i DATI VERI: WAGE2 di Blackburn &
Neumark (1992), `ECON_PS_01_Dati-wage2.csv` (accanto a questo script),
con `pareduc = meduc + feduc` e drop dei casi con genitori mancanti -> n = 722.
La riproduzione restituisce i coefficienti e gli errori standard HC1 del testo
d'esame alla sesta cifra decimale.

Esercizio 2 (oro e argento) non ha dati: le figure sono costruite
analiticamente dall'output di regressione riportato nel testo, piu' due
simulazioni illustrative (seme fissato) per la distribuzione di Dickey-Fuller
e per le due specificazioni della parte deterministica.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
from scipy import stats
es.use()
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = pathlib.Path(__file__).resolve().parent
SEED = 20231221

# --------------------------------------------------------------------- dati
# A copy of Moodle/01-Econometria/Dataset-CSV/Problem-Set/ECON_PS_01_Dati-wage2.csv,
# kept beside the script so the folder stands on its own.
CSV = OUT / "ECON_PS_01_Dati-wage2.csv"

import pandas as pd
import statsmodels.formula.api as smf

_d = pd.read_csv(CSV)
_d["pareduc"] = _d.meduc + _d.feduc
D = _d.dropna(subset=["meduc", "feduc"]).copy()
F1 = "lwage ~ educ + pareduc + exper + married"
F2 = "lwage ~ educ + pareduc + exper + married + IQ"
M1 = smf.ols(F1, data=D).fit(cov_type="HC1")
M2 = smf.ols(F2, data=D).fit(cov_type="HC1")
M1N = smf.ols(F1, data=D).fit()
M2N = smf.ols(F2, data=D).fit()
assert len(D) == 722, len(D)
assert abs(M1.params["educ"] - 0.0650240) < 1e-6

# valori del TESTO d'esame (Mod. 1, output completo)
B_EDUC, SE_EDUC = 0.0650240, 0.00764027
B_MARR, SE_MARR = 0.203713, 0.0462668


def it(v, d=3):
    return f"{v:.{d}f}".replace(".", ",")


# ===================================================================== D 1
# Quanti anni di istruzione servono per +15% di salario atteso.
def d01():
    fig, axes = plt.subplots(1, 2, figsize=(6.0, 2.82),
                             gridspec_kw={"width_ratios": [1.35, 1]})
    ax = axes[0]
    dx = np.linspace(0, 4, 400)
    appr = 100 * B_EDUC * dx
    exact = 100 * (np.exp(B_EDUC * dx) - 1)
    ax.plot(dx, appr, color=es.AMBER, lw=1.5, ls="--",
            label=r"approssimato: $100\,\beta_1\,\Delta$educ")
    ax.plot(dx, exact, color=es.BLUE, lw=1.8,
            label=r"esatto: $100(e^{\beta_1\Delta\mathrm{educ}}-1)$")
    ax.axhline(15, color=es.RED, lw=1.0, ls=":")
    ax.annotate("obiettivo +15%", xy=(3.95, 15), xytext=(0, 5), ha="right",
                textcoords="offset points", fontsize=8.5, color=es.RED)
    for x, col, lab in ((0.15 / B_EDUC, es.AMBER, "2,307"),
                        (np.log(1.15) / B_EDUC, es.BLUE, "2,149")):
        ax.plot([x], [15], "o", color=col, ms=6, zorder=6)
        ax.vlines(x, 0, 15, color=col, lw=0.9, ls=":")
    ax.annotate("2,149 anni\n(esatto)", xy=(np.log(1.15) / B_EDUC, 15),
                xytext=(-64, 8), textcoords="offset points", fontsize=8.5,
                color=es.BLUE, fontweight="bold")
    ax.annotate("2,307 anni\n(approssimato)", xy=(0.15 / B_EDUC, 15),
                xytext=(6, -26), textcoords="offset points", fontsize=8.5,
                color=es.AMBER, fontweight="bold")
    ax.set_xlim(0, 4); ax.set_ylim(0, 30)
    ax.set_xlabel(r"$\Delta$educ (anni di istruzione in piu')")
    ax.set_ylabel("variazione attesa del salario (%)")
    ax.set_title("Dalla variazione di educ alla variazione %", loc="left")
    leg = ax.legend(loc="upper left", frameon=True, framealpha=1.0,
                    facecolor="white", edgecolor="none")
    leg.set_zorder(8)
    es.commas(ax)

    ax = axes[1]
    lo, hi = B_EDUC - 1.96 * SE_EDUC, B_EDUC + 1.96 * SE_EDUC
    yl, yh = np.log(1.15) / hi, np.log(1.15) / lo
    ax.hlines(1, yl, yh, color=es.TEAL, lw=7, alpha=0.45)
    ax.plot([np.log(1.15) / B_EDUC], [1], "o", color=es.TEAL, ms=8, zorder=6)
    for v, dy in ((yl, 0), (yh, 0)):
        ax.vlines(v, 0.84, 1.16, color=es.TEAL, lw=1.6)
        ax.annotate(it(v), xy=(v, 0.79), ha="center", va="top",
                    fontsize=8.5, color=es.TEAL)
    ax.annotate("stima 2,149", xy=(np.log(1.15) / B_EDUC, 1.2), ha="center",
                va="bottom", fontsize=9, color=es.TEAL, fontweight="bold")
    ax.set_xlim(1.55, 2.99); ax.set_ylim(0.3, 1.7)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("anni necessari per +15%")
    ax.set_title("Incertezza campionaria", loc="left")
    es.commas(ax, "x")
    fig.tight_layout()
    es.save(fig, OUT / "d01-anni-per-quindici-percento.pdf")


# ===================================================================== D 2
# Il coefficiente di married e' una percentuale, non dollari.
def d02():
    fig, axes = plt.subplots(1, 2, figsize=(6.0, 2.9),
                             gridspec_kw={"width_ratios": [1.15, 1]})
    gap = np.exp(B_MARR) - 1
    w = np.linspace(0, 3200, 400)

    ax = axes[0]
    ax.plot(w, gap * w, color=es.BLUE, lw=1.8,
            label=r"$\Delta$wage $= $wage$_0\,(e^{\delta}-1)$")
    ax.axhline(20, color=es.RED, lw=1.1, ls="--", label="20 dollari (la domanda)")
    w20 = 20 / gap
    ax.plot([w20], [20], "o", color=es.RED, ms=6, zorder=6)
    ax.annotate(f"per ottenere 20 \\$ servirebbe\nwage$_0$ = {it(w20, 1)} \\$,"
                "\nsotto il minimo osservato (115 \\$)",
                xy=(w20, 20), xytext=(3150, 52), textcoords="data",
                ha="right", fontsize=8.2, color=es.RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.9))
    q1, q2, q3 = D.wage.quantile([0.25, 0.5, 0.75])
    for q, lab in ((q1, "Q1"), (q2, "mediana"), (q3, "Q3")):
        ax.plot([q], [gap * q], "s", color=es.TEAL, ms=6, zorder=6)
        ax.annotate(f"{lab}: {it(gap*q,0)} \\$", xy=(q, gap * q), xytext=(9, -10),
                    textcoords="offset points", ha="left", va="top",
                    fontsize=8.4, color=es.TEAL)
    ax.set_xlim(0, 3200); ax.set_ylim(0, 760)
    ax.set_xlabel("salario mensile di partenza wage$_0$ (dollari)")
    ax.set_ylabel("differenza sposato $-$ single (dollari)")
    ax.set_title("Lo stesso 22,59% vale dollari diversi", loc="left")
    ax.legend(loc="upper left")
    es.commas(ax)

    ax = axes[1]
    ax.hist(D.wage, bins=40, color=es.BLUEBG, edgecolor=es.BLUE, lw=0.6)
    ax.axvline(D.wage.min(), color=es.RED, lw=1.2, ls="--")
    ax.axvline(w20, color=es.AMBER, lw=1.6)
    ax.text(190, 95, f"minimo osservato: {int(D.wage.min())} \\$",
            ha="left", va="center", fontsize=8.4, color=es.RED,
            fontweight="bold")
    ax.text(190, 86, f"wage$_0$ che darebbe 20 \\$: {it(w20,1)} \\$",
            ha="left", va="center", fontsize=8.4, color=es.AMBER,
            fontweight="bold")
    ax.set_ylim(0, 102)
    ax.set_xlabel("wage (dollari al mese), n = 722")
    ax.set_ylabel("frequenza")
    ax.set_title("Distribuzione dei salari nel campione", loc="left")
    es.commas(ax, "x")
    fig.tight_layout()
    es.save(fig, OUT / "d02-percentuale-non-dollari.pdf")


# ===================================================================== D 3
# Residui vs valori predetti (dati veri) + test BP + s.e. naive vs HC1.
def d03():
    fig = plt.figure(figsize=(6.6, 5.4))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.25, 1], hspace=0.48, wspace=0.32)

    ax = fig.add_subplot(gs[0, :])
    yhat, res = M1N.fittedvalues.values, M1N.resid.values
    ax.scatter(yhat, res, s=13, facecolors="none", edgecolors=es.TEAL, lw=0.6,
               alpha=0.85, label="residui OLS (n = 722)")
    ax.axhline(0, color=es.GRAY, lw=0.8, ls=":")
    edges = np.quantile(yhat, np.linspace(0, 1, 11))
    ctr, sd = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (yhat >= a) & (yhat <= b)
        ctr.append(yhat[m].mean()); sd.append(res[m].std(ddof=1))
    ctr, sd = np.array(ctr), np.array(sd)
    ax.plot(ctr, sd, color=es.RED, lw=1.6, marker="o", ms=4,
            label=r"$\pm$ dev. std. dei residui per decile di $\hat y$")
    ax.plot(ctr, -sd, color=es.RED, lw=1.6, marker="o", ms=4)
    ax.set_xlabel(r"valori predetti $\hat y$")
    ax.set_ylabel(r"residui $\hat\epsilon$")
    ax.set_title("Figura 1 dell'esame, ricalcolata sui dati veri", loc="left")
    ax.set_ylim(top=2.10)
    ax.legend(loc="upper center", ncol=2, fontsize=8.4, borderaxespad=0.4)
    es.commas(ax)

    ax = fig.add_subplot(gs[1, 0])
    bp_lm, bp_p = 11.00518, 0.02651
    crit = stats.chi2.ppf(0.95, 4)
    x = np.linspace(0, 20, 500)
    y = stats.chi2(4).pdf(x)
    ax.plot(x, y, color=es.BLUE, lw=1.4)
    ax.fill_between(x, y, color=es.BLUEBG)
    m = x >= crit
    ax.fill_between(x[m], y[m], color=es.RED, alpha=0.30)
    ax.axvline(bp_lm, color=es.GREEN, lw=2.0)
    ax.set_xlabel("statistica"); ax.set_ylabel("densità"); ax.set_yticks([])
    ax.set_xlim(0, 22)
    ymax = stats.chi2(4).pdf(2) * 1.62
    ax.set_ylim(0, ymax)
    ax.set_title("Breusch-Pagan sui dati veri", loc="left")
    ax.annotate(f"rifiuto:\n$\\chi^2_4$ > {it(crit)}", xy=(10.4, 0.010),
                xytext=(6.2, 0.86 * ymax), textcoords="data",
                ha="center", va="center", fontsize=8.4, color=es.RED,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))
    ax.annotate(f"BP = {it(bp_lm)}\n(p = {it(bp_p, 4)})",
                xy=(11.8, 0.62 * ymax), ha="left", va="center",
                fontsize=8.4, color=es.GREEN, fontweight="bold")
    es.commas(ax, "x")

    ax = fig.add_subplot(gs[1, 1])
    names = ["educ", "pareduc", "exper", "married"]
    xs = np.arange(len(names))
    ratio = np.array([M1.bse[k] / M1N.bse[k] for k in names])
    ax.bar(xs, ratio - 1, 0.5, bottom=1,
           color=[es.RED if r > 1 else es.BLUE for r in ratio], alpha=0.85)
    ax.axhline(1, color=es.GRAY, lw=1.0)
    for i, r in enumerate(ratio):
        ax.annotate(it(r, 3), xy=(i, r), xytext=(0, 4 if r > 1 else -12),
                    textcoords="offset points", ha="center", fontsize=8,
                    color=es.INK, fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(names, fontsize=8)
    ax.set_ylim(0.90, 1.10)
    ax.set_ylabel("s.e. HC1 / s.e. classico")
    ax.set_title("I due errori standard coincidono", loc="left")
    es.commas(ax, "y", decimals=2)
    es.save(fig, OUT / "d03-residui-e-robustezza.pdf")


# ===================================================================== D 4
# Distorsione da variabile omessa: educ e IQ.
def d04():
    fig, axes = plt.subplots(1, 2, figsize=(6.0, 2.85))

    ax = axes[0]
    labs = ["Mod. 1\n(senza IQ)\ntesto", "Mod. 2\n(con IQ)\ntesto",
            "Mod. 1\ndati veri", "Mod. 2\ndati veri"]
    est = [0.065, 0.035, M1.params["educ"], M2.params["educ"]]
    ses = [0.007, 0.008, M1.bse["educ"], M2.bse["educ"]]
    cols = [es.AMBER, es.AMBER, es.BLUE, es.BLUE]
    xs = np.arange(4)
    for x, e, s, c in zip(xs, est, ses, cols):
        ax.errorbar([x], [e], yerr=[1.96 * s], fmt="o", color=c, ms=7, capsize=5,
                    lw=1.4)
        ax.annotate(it(e, 4), xy=(x, e), xytext=(9, 2), textcoords="offset points",
                    fontsize=8.2, color=c, fontweight="bold")
    ax.annotate("", xy=(1, est[1]), xytext=(0, est[0]),
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.3, ls="--"))
    ax.annotate("", xy=(3, est[3]), xytext=(2, est[2]),
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.3, ls="--"))
    ax.annotate(r"bias $+0{,}030$", xy=(0.5, 0.0163),
                ha="center", va="center", fontsize=8.4, color=es.RED,
                fontweight="bold")
    ax.annotate(r"bias $\beta_{IQ}\delta=+0{,}0148$", xy=(2.5, 0.0163),
                ha="center", va="center", fontsize=8.4, color=es.RED,
                fontweight="bold")
    ax.annotate("distorsione da variabile omessa", xy=(1.65, 0.0862),
                ha="center", va="center", fontsize=8.4, color=es.RED,
                fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(labs, fontsize=8.2)
    ax.set_xlim(-0.55, 3.9); ax.set_ylim(0.0112, 0.0905)
    ax.set_ylabel(r"$\hat\beta_{educ}$  (IC 95%)")
    ax.set_title("Il rendimento stimato dell'istruzione cala", loc="left")
    es.commas(ax, "y", decimals=3)

    ax = axes[1]
    rng = np.random.default_rng(SEED)
    jx = D.educ + rng.uniform(-0.22, 0.22, len(D))
    ax.scatter(jx, D.IQ, s=11, facecolors="none", edgecolors=es.TEAL, lw=0.5,
               alpha=0.7)
    xs = np.linspace(D.educ.min(), D.educ.max(), 50)
    b0, b1 = np.polyfit(D.educ, D.IQ, 1)
    ax.plot(xs, b0 * xs + b1, color=es.RED, lw=1.8,
            label=f"pendenza semplice = {it(b0, 3)}")
    ax.plot([], [], " ", label=f"pendenza parziale $\\delta$ = {it(3.10997, 3)}")
    ax.plot([], [], " ", label=f"corr(educ, IQ) = {it(D.educ.corr(D.IQ), 3)}")
    ax.set_xlabel("educ (anni, con jitter grafico)")
    ax.set_ylabel("IQ")
    ax.set_title(r"$\operatorname{Cov}(\mathrm{educ},\mathrm{IQ})>0$", loc="left")
    leg = ax.legend(loc="upper left", fontsize=8.4, frameon=True,
                    framealpha=1.0, facecolor="white", edgecolor="none")
    leg.set_zorder(8)
    es.commas(ax)
    fig.tight_layout()
    es.save(fig, OUT / "d04-variabile-omessa.pdf")


# ===================================================================== D 5
# Collinearita': se(educ) in funzione di R^2_j, e cosa si puo' leggere
# dall'output arrotondato.
def d05():
    fig, axes = plt.subplots(1, 2, figsize=(6.1, 2.9))

    R1 = smf.ols("educ ~ pareduc + exper + married", data=D).fit().rsquared
    R2 = smf.ols("educ ~ pareduc + exper + married + IQ", data=D).fit().rsquared

    ax = axes[0]
    r = np.linspace(0, 0.95, 400)
    ax.plot(r, 1 / np.sqrt(1 - r), color=es.BLUE, lw=1.8,
            label=r"$1/\sqrt{1-R_j^2}=\sqrt{\mathrm{VIF}_j}$")
    for R, col, lab, txy in ((R1, es.TEAL, "Mod. 1", (0.035, 2.42)),
                             (R2, es.AMBER, "Mod. 2", (0.035, 3.58))):
        v = 1 / np.sqrt(1 - R)
        ax.plot([R], [v], "o", color=col, ms=7, zorder=6)
        ax.vlines(R, 1, v, color=col, lw=1.0, ls=":")
        ax.annotate(f"{lab}: $R_j^2$ = {it(R, 3)}\nVIF = {it(1/(1-R), 3)}, "
                    fr"$\sqrt{{\mathrm{{VIF}}}}$ = {it(v, 3)}",
                    xy=(R, v), xytext=txy, textcoords="data",
                    ha="left", va="center", fontsize=8.4, color=col,
                    fontweight="bold",
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.7,
                                    shrinkB=6))
    ax.set_xlim(0, 0.95); ax.set_ylim(1, 4.6)
    ax.set_xlabel(r"$R_j^2$ della regressione ausiliaria di educ")
    ax.set_ylabel("inflazione dell'errore standard")
    ax.set_title("Collinearita' presente, ma lontana dal ginocchio", loc="left")
    ax.legend(loc="lower right")
    es.commas(ax)

    ax = axes[1]
    ratio_naive = M2N.bse["educ"] / M1N.bse["educ"]
    ratio_hc1 = M2.bse["educ"] / M1.bse["educ"]
    vif_part = np.sqrt((1 - R1) / (1 - R2))
    sig_part = np.sqrt(M2N.mse_resid) / np.sqrt(M1N.mse_resid)
    lo, hi = 0.0075 / 0.0075, 0.0085 / 0.0065
    ax.add_patch(Rectangle((lo, -1.05), hi - lo, 5.3, color=es.REDBG, zorder=0))
    ax.annotate("l'output stampato consente\n"
                f"solo di dire \"fra {it(lo,2)} e {it(hi,2)}\"",
                xy=(0.5 * (lo + hi), -0.55), ha="center", va="center",
                fontsize=8.4, color=es.RED, fontweight="bold")
    rows = [("rapporto s.e. HC1 (dati veri)", ratio_hc1, es.BLUE),
            ("rapporto s.e. classici (dati veri)", ratio_naive, es.TEAL),
            (r"parte dovuta al VIF: $\sqrt{\mathrm{VIF}_2/\mathrm{VIF}_1}$",
             vif_part, es.AMBER),
            (r"parte dovuta a $\hat\sigma$: $\hat\sigma_2/\hat\sigma_1$",
             sig_part, es.GRAY)]
    for i, (lab, v, col) in enumerate(rows):
        y = i + 0.22
        ax.plot([v], [y], "o", color=col, ms=8, zorder=5)
        ax.annotate(it(v, 4), xy=(v, y), xytext=(9, 0), ha="left", va="center",
                    textcoords="offset points", fontsize=8.4, color=col,
                    fontweight="bold")
        ax.annotate(lab, xy=(0.937, y + 0.40), ha="left", va="center",
                    fontsize=8.4, color=col)
    ax.vlines(1, -1.05, 0.02, color=es.GRAY, lw=0.9, ls=":")
    ax.set_yticks([])
    ax.set_ylim(-1.10, 4.25)
    ax.set_xlim(0.93, 1.40)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel(r"se($\hat\beta_{educ}$) del Mod. 2 / del Mod. 1")
    ax.set_title("Quanto e' davvero cresciuto l'errore standard", loc="left")
    es.commas(ax, "x")
    fig.tight_layout()
    es.save(fig, OUT / "d05-collinearita.pdf")


# ===================================================================== D 6
# 10 punti di IQ valgono almeno il 5%?
def d06():
    fig, axes = plt.subplots(2, 1, figsize=(6.1, 4.3),
                             gridspec_kw={"height_ratios": [1, 1.15]})

    est, se = 0.05, 0.01
    es.ci_line(est, est - 1.96 * se, est + 1.96 * se, h0=np.log(1.05), ax=axes[0],
               decimals=4, xlabel=r"$10\,\beta_{IQ}$ (variazione di $\log$ wage)",
               title=r"IC 95% di $10\beta_{IQ}$ costruito sui numeri stampati")

    ax = axes[1]
    b = np.linspace(0.0045, 0.0055, 300)
    for thr, col, lab in ((0.05, es.BLUE, r"$H_0:\ 10\beta_{IQ}=0{,}05$"),
                          (np.log(1.05), es.TEAL,
                           r"$H_0:\ 10\beta_{IQ}=\log(1{,}05)=0{,}0488$")):
        ax.plot(b, (10 * b - thr) / 0.01, color=col, lw=1.8, label=lab)
    ax.axhline(0, color=es.GRAY, lw=0.8)
    for c, ls in ((1.96, "--"), (-1.96, "--"), (-1.645, ":")):
        ax.axhline(c, color=es.RED, lw=1.0, ls=ls)
    ax.annotate(r"$\pm1{,}96$: rifiuto bilaterale", xy=(0.005485, 1.96),
                xytext=(0, 5), ha="right", textcoords="offset points",
                fontsize=8.4, color=es.RED)
    ax.annotate(r"$-1{,}645$: rifiuto unilaterale sinistro",
                xy=(0.005485, -1.645), xytext=(0, -15), ha="right",
                textcoords="offset points", fontsize=8.4, color=es.RED)
    ax.plot([0.005], [0.0], "o", color=es.BLUE, ms=7, zorder=6)
    ax.annotate("stampato 0,005:\nt = 0", xy=(0.005, 0), xytext=(11, 6),
                textcoords="offset points", fontsize=8.4, color=es.BLUE,
                fontweight="bold")
    ax.plot([M2.params["IQ"]], [(10 * M2.params["IQ"] - 0.05) / 0.01], "D",
            color=es.GRAY, ms=6, zorder=6)
    ax.annotate("dati veri 0,004771:\nt = $-$0,229 a se = 0,01",
                xy=(M2.params["IQ"], (10 * M2.params["IQ"] - 0.05) / 0.01),
                xytext=(-9, 8), textcoords="offset points", ha="right",
                va="bottom", fontsize=8.4, color=es.GRAY, fontweight="bold")
    ax.set_xlim(0.0045, 0.0055); ax.set_ylim(-3.4, 4.8)
    ax.set_xlabel(r"valore di $\beta_{IQ}$ compatibile con l'arrotondamento a 0,005")
    ax.set_ylabel("statistica $t$")
    ax.set_title("L'arrotondamento non cambia la decisione", loc="left")
    ax.legend(loc="upper left", fontsize=8.4)
    es.commas(ax, "x", decimals=4); es.commas(ax, "y", decimals=1)
    fig.tight_layout()
    es.save(fig, OUT / "d06-dieci-punti-di-iq.pdf")


# ===================================================================== D 7
# Come si sceglie la deterministica della regressione DF, e il sistema di
# ipotesi sulla riparametrizzazione delta = beta1 - 1.
def d07():
    fig, axes = plt.subplots(1, 2, figsize=(6.1, 2.7),
                             gridspec_kw={"width_ratios": [1.25, 1]})
    rng = np.random.default_rng(SEED)
    T = 400
    e = rng.normal(0, 1, T)
    rw = np.cumsum(0.06 + e)                       # random walk con drift
    ts = 0.06 * np.arange(T) + 3.0 * rng.normal(0, 1, T)   # trend-stazionario

    ax = axes[0]
    ax.plot(rw, color=es.BLUE, lw=1.1, label=r"$H_0$: random walk con drift")
    ax.plot(ts, color=es.AMBER, lw=1.1, alpha=0.9,
            label=r"$H_1$: stazionaria attorno a un trend")
    ax.plot(0.06 * np.arange(T), color=es.RED, lw=1.2, ls="--",
            label="parte deterministica")
    ax.set_xlabel("tempo")
    ax.set_ylabel("livello")
    ax.set_title("Guardare basta per la deterministica, non per il test",
                 loc="left", fontsize=9.2)
    ax.legend(loc="upper left", fontsize=8.4)
    es.commas(ax, "y", decimals=0)

    ax = axes[1]
    b1 = np.linspace(0.90, 1.04, 200)
    ax.fill_between([0.90, 1.0], -1, 1, color=es.GREENBG, zorder=0)
    ax.fill_between([1.0, 1.04], -1, 1, color=es.REDBG, zorder=0)
    ax.axvline(1.0, color=es.RED, lw=1.6)
    ax.annotate(r"$H_0:\ \beta_1=1\ \Leftrightarrow\ \delta=0$"
                "\nradice unitaria", xy=(0.9955, 0.72), ha="right", va="center",
                fontsize=8.4, color=es.RED, fontweight="bold")
    ax.annotate(r"$H_1:\ \beta_1<1\ \Leftrightarrow\ \delta<0$"
                "\nserie stazionaria", xy=(0.948, -0.45), ha="center",
                va="center", fontsize=8.4, color=es.GREEN, fontweight="bold")
    ax.annotate("", xy=(0.905, 0.05), xytext=(0.995, 0.05),
                arrowprops=dict(arrowstyle="->", color=es.GREEN, lw=1.6))
    ax.set_xlim(0.90, 1.03); ax.set_ylim(-1, 1)
    ax.set_yticks([]); ax.grid(axis="y", visible=False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(r"$\beta_1$ (coefficiente di $Y_{t-1}$ nell'AR)")
    ax.set_title("Test unilaterale sinistro", loc="left")
    es.commas(ax, "x", decimals=2)
    fig.tight_layout()
    es.save(fig, OUT / "d07-dickey-fuller-impostazione.pdf")


# ---------------------------------------------- distribuzione DF simulata
def _df_null(T=500, R=20000, seed=SEED):
    """Distribuzione simulata della t di Dickey-Fuller con costante."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(R // 2000):
        y = np.cumsum(rng.normal(0, 1, (2000, T + 1)), axis=1)
        x = y[:, :-1]
        dy = np.diff(y, axis=1)
        xc = x - x.mean(axis=1, keepdims=True)
        dc = dy - dy.mean(axis=1, keepdims=True)
        sxx = (xc ** 2).sum(axis=1)
        d = (xc * dc).sum(axis=1) / sxx
        ssr = ((dc - d[:, None] * xc) ** 2).sum(axis=1)
        sig2 = ssr / (T - 2)
        out.append(d / np.sqrt(sig2 / sxx))
    return np.concatenate(out)


# ===================================================================== D 8
def d08():
    t_obs, crit = 0.3448, -2.85
    tt = _df_null()
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    grid = np.linspace(-5.2, 3.2, 700)
    kde = stats.gaussian_kde(tt)
    y = kde(grid)
    ax.plot(grid, y, color=es.BLUE, lw=1.6,
            label="densità Dickey-Fuller\ncon costante (simulata)")
    ax.fill_between(grid, y, color=es.BLUEBG)
    m = grid <= crit
    ax.fill_between(grid[m], y[m], color=es.RED, alpha=0.30,
                    label=r"regione di rifiuto: $t<-2{,}85$")
    ax.axvline(crit, color=es.RED, lw=1.1, ls="--")
    ax.plot(grid, stats.norm.pdf(grid), color=es.GRAY, lw=1.2, ls=":",
            label="N(0,1), per confronto")
    ax.axvline(t_obs, color=es.GREEN, lw=2.2)
    ax.annotate(r"$t^{oss}=0{,}3448$" "\n(p-value ADF = 0,9806)",
                xy=(t_obs, 0.455), xytext=(9, 0), textcoords="offset points",
                ha="left", va="center", fontsize=8.4, color=es.GREEN,
                fontweight="bold")
    ax.annotate(f"5° percentile simulato:\n{it(np.quantile(tt, 0.05))}",
                xy=(-2.867, 0.012), xytext=(-5.15, 0.145), fontsize=8.4,
                color=es.RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))
    ax.set_xlim(-5.2, 4.4); ax.set_ylim(0, 0.80)
    ax.set_yticks([])
    ax.set_xlabel("valore della statistica")
    ax.set_ylabel("densità")
    ax.set_title(r"ADF su gold$_t$: la statistica cade nella coda sbagliata",
                 loc="left")
    ax.legend(loc="upper left", fontsize=8.4)
    es.commas(ax, "x", decimals=1)
    es.save(fig, OUT / "d08-adf-gold.pdf")


# ===================================================================== D 9
def d09():
    fig, axes = plt.subplots(2, 1, figsize=(6.1, 4.4),
                             gridspec_kw={"height_ratios": [1.05, 1]})

    ax = axes[0]
    labs = [r"ADF su gold$_t$" "\n(dom. 8)\nnon rifiuto: I(1)",
            r"ADF su silver$_t$" "\n(dato dal testo)\nnon rifiuto: I(1)",
            "Engle-Granger\nsui residui\nrifiuto: stazionari"]
    pv = [0.9806, 0.74, 0.00007]
    cols = [es.BLUE, es.BLUE, es.GREEN]
    xs = np.arange(3)
    ax.bar(xs, pv, 0.45, color=cols, alpha=0.85)
    ax.set_yscale("log")
    ax.axhline(0.05, color=es.RED, lw=1.3, ls="--")
    ax.annotate(r"livello 5%", xy=(1.30, 0.068), ha="left", va="bottom",
                fontsize=8.4, color=es.RED, fontweight="bold")
    for x, p in zip(xs, pv):
        ax.annotate(f"p = {p:.5f}".rstrip("0").replace(".", ","),
                    xy=(x, p), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.4,
                    color=es.INK, fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(labs, fontsize=8.4)
    ax.set_ylim(1e-5, 12)
    ax.set_ylabel("p-value (scala log)")
    ax.set_title("I tre passi della procedura di Engle-Granger", loc="left")

    b, sb = 54.9646, 0.233509
    est, lo, hi = 2 * b, 2 * b - 1.96 * 2 * sb, 2 * b + 1.96 * 2 * sb
    ax = axes[1]
    ax.hlines(0, lo, hi, color=es.BLUE, lw=7, alpha=0.55)
    for v in (lo, hi):
        ax.vlines(v, -0.2, 0.2, color=es.BLUE, lw=1.6)
    ax.plot([est], [0], "o", color=es.BLUE, ms=8, zorder=6)
    ax.annotate(f"stima {it(est,3)} \\$\nIC 95%: [{it(lo,3)} ; {it(hi,3)}]",
                xy=(est, -0.3), ha="center", va="top", fontsize=8.6,
                color=es.BLUE, fontweight="bold")
    ax.plot([75.0], [0], "D", color=es.RED, ms=9, zorder=6)
    ax.annotate("$H_0$: 75,000 \\$\n(fuori dall'intervallo: rifiuto)",
                xy=(75.0, -0.3), ha="center", va="top", fontsize=8.6,
                color=es.RED, fontweight="bold")
    ax.annotate("", xy=(est, 0.62), xytext=(75.0, 0.62),
                arrowprops=dict(arrowstyle="<->", color=es.AMBER, lw=1.3))
    ax.annotate(r"scarto $34{,}929$ \$ = $74{,}79$ errori standard",
                xy=(0.5 * (75 + est), 0.68), ha="center", va="bottom",
                fontsize=8.4, color=es.AMBER, fontweight="bold")
    ax.set_xlim(71, 115); ax.set_ylim(-1.15, 1.25)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel(r"variazione di gold per $+2$ dollari di silver (dollari)")
    ax.set_title(r"$H_0:\ 2\beta=75$, cioè $\beta=37{,}5$", loc="left")
    es.commas(ax, "x", decimals=0)
    fig.tight_layout()
    es.save(fig, OUT / "d09-cointegrazione-e-beta.pdf")


# ===================================================================== D 10
def d10():
    lam = -0.0298275
    phi = 1 + lam
    fig, axes = plt.subplots(1, 2, figsize=(6.1, 2.9))

    _, _, tab = es.decay(lam, horizon=12, targets=(0.05,), ax=axes[0],
                         title="Zoom sui primi giorni")
    axes[0].set_ylim(0.70, 1.02)
    axes[0].set_xlabel("giorni di contrattazione dopo lo shock")
    for t in axes[0].texts:
        t.set_fontsize(8.4)
    # dentro $...$ la virgola fra cifre diventa uno spazio: la riscrivo con {,}
    axes[0].legend([r"$(1-0{,}0298)^h$"], loc="lower left", fontsize=8.4)

    ax = axes[1]
    h = np.arange(0, 161)
    ax.plot(h, 1 - phi ** h, color=es.BLUE, lw=1.7,
            label=r"quota assorbita $1-(1+\lambda)^h$")
    for s, col, off in ((0.05, es.GREEN, (14, 10)), (0.5, es.AMBER, (10, -16)),
                        (0.95, es.RED, (-8, 13))):
        hs = int(np.ceil(np.log(1 - s) / np.log(phi)))
        ax.axhline(s, color=col, lw=0.9, ls=":")
        ax.plot([hs], [1 - phi ** hs], "*", color=col, ms=13, zorder=6)
        ax.annotate(f"{int(s*100)}% in {hs} giorni", xy=(hs, 1 - phi ** hs),
                    xytext=off, textcoords="offset points", fontsize=8.4,
                    ha="right" if off[0] < 0 else "left",
                    color=col, fontweight="bold")
    ax.set_xlim(0, 168); ax.set_ylim(0, 1.15)
    ax.set_xlabel("giorni di contrattazione dopo lo shock")
    ax.set_ylabel("quota di disequilibrio assorbita")
    ax.set_title(r"$\lambda=-0{,}0298$: aggiustamento lento", loc="left")
    ax.legend(loc="center right", fontsize=8.4)
    es.commas(ax, "y", decimals=2)
    fig.tight_layout()
    es.save(fig, OUT / "d10-assorbimento-ecm.pdf")
    print("   h* per il 5% =", tab)


if __name__ == "__main__":
    d01(); d02(); d03(); d04(); d05(); d06(); d07(); d08(); d09(); d10()
