"""Simulated exam 2 - footballers' wages (cross-section) and two annual series (time series)."""

from functools import lru_cache
from types import SimpleNamespace

import numpy as np
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan, het_white
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import acf, adfuller, coint, pacf

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import fmt_p, fmt_sig, ols_table

TITOLO = "Appello simulato 2"

# Normal quantiles the exam texts fix for a two-sided and a one-sided test at 5%.
Z = 1.96
Z1 = 1.64

ALFA = 0.05

# A p-value within half of ALFA from ALFA would let the printed rounding decide.
MARGINE_P = 0.5

# Dickey-Fuller 5% value the exam texts hand out (constant only), and the MacKinnon
# asymptotic one: the margins are checked against both, so the decision does not
# depend on which convention a reader applies.
DF_C = -2.38
MK_C = -2.86

# QLR 5% critical value for two restrictions and 15% trimming (ECON 06, Exelon example).
QLR_CRIT = 5.86
TRIM = 0.15

# Role codes the text asks the student to give for the omitted category.
RUOLI = {"dif": 1, "cen": 2, "att": 3}

# Autoregressive coefficient of the GDP growth: persistent enough for a clear geometric ACF,
# weak enough for the Dickey-Fuller test on the difference to reject comfortably.
PHI = 0.70


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _virgola(x, decimali):
    """Return ``x`` for a figure label, with the decimal comma."""
    return f"{x:.{decimali}f}".replace(".", ",")


def _m(testo):
    """Wrap a number printed with a decimal comma in math mode, so its minus sign is a real one."""
    return testo if "e" in testo else f"${testo.replace(',', '{,}')}$"


def _stima(y, colonne):
    """Fit OLS of ``y`` on a constant and the named columns; return result, design matrix and table."""
    nomi = list(colonne)
    X = sm.add_constant(np.column_stack([colonne[k] for k in nomi]))
    res = sm.OLS(y, X).fit()
    return res, X, ols_table(res, labels=["const", *nomi])


def _righe(res, nomi):
    """Return every row of a fit as the dictionary the table parser would give, at full precision."""
    return {k: {"coef": float(res.params[j]), "se": float(res.bse[j]), "t": float(res.tvalues[j])}
            for j, k in enumerate(nomi)}


def _decide(t):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > Z else "non rifiuta"


def _decide_p(p_testo):
    """Return the decision at 5% from a printed p-value."""
    return "rifiuta" if p_testo < ALFA else "non rifiuta"


def _decide_df(t):
    """Return the one-sided Dickey-Fuller decision against the critical value of the text."""
    return "rifiuta" if t < DF_C else "non rifiuta"


def _p_stampato(p):
    """Return ``p`` as the student reads it, after the rounding of the printed output."""
    return float(fmt_p(p).replace(",", "."))


def _lm_test(resid, colonne, white=False):
    """Run the auxiliary regression of the squared residuals and return LM = n R^2.

    Args:
        resid: OLS residuals of the model under test.
        colonne: Regressor name to values, constant excluded.
        white: Whether to add squares and cross products, as the White test does.

    Returns:
        A namespace with the statistic ``lm``, its degrees of freedom ``gl`` and the
        chi-square p-value ``p``.
    """
    aux = dict(colonne)
    if white:
        nomi = list(colonne)
        for i, a in enumerate(nomi):
            aux[f"{a}^2"] = colonne[a] ** 2
            for b in nomi[i + 1:]:
                aux[f"{a}*{b}"] = colonne[a] * colonne[b]
    res = sm.OLS(resid ** 2, sm.add_constant(np.column_stack(list(aux.values())))).fit()
    lm = len(resid) * res.rsquared
    return SimpleNamespace(lm=float(lm), gl=len(aux), p=float(stats.chi2.sf(lm, len(aux))))


def _blocco(nome, lm, gl, p):
    """Return the printed output of a heteroskedasticity test, in the layout of gretl."""
    stat = fmt_sig(lm, 6).replace(",", "{,}")
    return (f"**{nome} per l'eteroschedasticità.** Ipotesi nulla: omoschedasticità. "
            f"Statistica test: $LM = {stat}$, con p-value $P(\\chi^2({gl}) > {stat}) =$ "
            f"{fmt_p(p)}.")


def _intervalli(ax, es, voci, xlabel, h0=0.0):
    """Draw one 95% interval per entry of ``voci`` = (label, estimate, low, high, colour).

    An entry with ``low`` equal to ``None`` is a reference value drawn as a diamond.
    """
    for k, (nome, stima, lo, hi, colore) in enumerate(voci):
        if lo is None:
            ax.plot([stima], [k], "D", color=colore, ms=6)
        else:
            ax.hlines(k, lo, hi, color=colore, lw=3, alpha=0.5)
            ax.plot([stima], [k], "o", color=colore, ms=6)
    ax.axvline(h0, color=es.GRAY, lw=0.9, ls="--")
    ax.set_yticks(range(len(voci)), [v[0] for v in voci])
    ax.set_ylim(-0.6, len(voci) - 0.4)
    ax.set_xlabel(xlabel)
    es.commas(ax, "x")


@exercise("a02_01", modulo=9, livello=3, punti=19,
          tipo=("dummy-categoria-base", "sistema-ipotesi-f-dummy-congiunte",
                "termine-quadratico-nonlinearita", "test-eteroschedasticita",
                "variazione-percentuale-log-livello", "test-unilaterale-su-soglia"))
def stipendi_calciatori(rng):
    """Read role dummies, test them jointly, a squared term, two heteroskedasticity tests and two effects."""
    n, dgol, obiettivo, riv = 360, 3.0, 20.0, 1.2
    ruolo = rng.choice(3, n, p=[0.38, 0.34, 0.28])
    dif, cen, att = ((ruolo == j).astype(float) for j in range(3))
    gol = np.round(np.where(ruolo == 2, rng.gamma(3.0, 2.0, n),
                            np.where(ruolo == 1, rng.gamma(2.0, 1.5, n), rng.gamma(1.4, 1.0, n))))
    pres = np.clip(np.round(rng.normal(25, 7, n)), 3, 38)
    esper = rng.integers(1, 17, n).astype(float)
    # The error spread is U-shaped in the appearances: a pattern that is symmetric around
    # the mean is invisible to a regression linear in the regressors (Breusch-Pagan) but not
    # to one with squares (White).
    z = (pres - pres.mean()) / pres.std()
    sd = 0.22 * np.sqrt(0.30 + 0.8 * z ** 2)
    y = (6.1 + 0.035 * gol + 0.012 * pres + 0.20 * esper - 0.0095 * esper ** 2
         - 0.17 * dif + 0.20 * att + sd * rng.normal(0, 1, n))
    cols = {"gol": gol, "pres": pres, "esper": esper, "esper2": esper ** 2, "dif": dif, "att": att}
    res, X, tab = _stima(y, cols)
    nomi = ["const", *cols]
    rist_cols = {k: cols[k] for k in ("gol", "pres", "esper", "esper2")}
    rist, _, tab_r = _stima(y, rist_cols)
    k_r = len(rist.params)
    fcrit = round(float(stats.f.ppf(1 - ALFA, len(res.params) - k_r, n - len(res.params))), 2)
    bp = _lm_test(res.resid, cols)
    wh = _lm_test(res.resid, {k: cols[k] for k in ("gol", "pres", "esper")}, white=True)
    p_bp, p_w = _p_stampato(bp.p), _p_stampato(wh.p)

    def answers(rows, n_oss, ssr_u, ssr_r, p_r, p_bp_s, p_w_s):
        """Return every answer from the printed rows, SSR, sample size, parameter count and test p-values."""
        p_u = len(rows)
        q, gl = p_u - p_r, n_oss - p_u
        f = ((ssr_r - ssr_u) / q) / (ssr_u / gl)
        omesso = next(codice for nome, codice in RUOLI.items() if nome not in rows)
        t_riv = (rows["pres"]["coef"] - riv / 100) / rows["pres"]["se"]
        b_q = rows["esper2"]
        dec_q = _decide(b_q["t"])
        return {"base": Numero(float(omesso), 0), "pct_att": Numero(100 * rows["att"]["coef"], 1),
                "liv_att": Numero(rows["const"]["coef"] + rows["att"]["coef"], 3),
                "q": Numero(float(q), 0), "gl": Numero(float(gl), 0), "F": Numero(f, 2),
                "dec_f": "rifiuta" if f > fcrit else "non rifiuta",
                "dec_q": dec_q, "decr": "sì" if dec_q == "rifiuta" and b_q["coef"] < 0 else "no",
                "dec_bp": _decide_p(p_bp_s), "dec_w": _decide_p(p_w_s),
                "p_bp": fmt_p(p_bp_s), "p_w": fmt_p(p_w_s),
                "gl_bp": Numero(float(bp.gl), 0), "gl_w": Numero(float(wh.gl), 0),
                "robusti": "sì" if min(p_bp_s, p_w_s) < ALFA else "no",
                "pct_gol": Numero(100 * dgol * rows["gol"]["coef"], 1),
                "gol_servono": Numero(obiettivo / (100 * rows["gol"]["coef"]), 2),
                "soglia": Numero(riv / 100, 3), "t_riv": Numero(t_riv, 2),
                "dec_riv": "rifiuta" if t_riv < -Z1 else "non rifiuta",
                "b_gol": Numero(rows["gol"]["coef"], 4), "b_pres": Numero(rows["pres"]["coef"], 6),
                "se_pres": Numero(rows["pres"]["se"], 6), "b_att": Numero(rows["att"]["coef"], 4),
                "b_dif": Numero(rows["dif"]["coef"], 4), "b_const": Numero(rows["const"]["coef"], 4),
                "b_esper": Numero(rows["esper"]["coef"], 4), "b_esper2": Numero(b_q["coef"], 5),
                "t_q": Numero(b_q["t"], 2), "ssr_u": Numero(ssr_u, 4), "ssr_r": Numero(ssr_r, 4),
                "lm_bp": Numero(bp.lm, 2), "lm_w": Numero(wh.lm, 2),
                "t_pres": Numero(rows["pres"]["t"], 2)}

    def studente(tabelle):
        """Rebuild the answers from the two printed tables and the printed p-values of the tests."""
        o, r = tabelle["ols"], tabelle["rist"]
        return answers(o.rows, o.stats["n"], o.stats["ssr"], r.stats["ssr"], len(r.rows), p_bp, p_w)

    def senza_costante(risposte):
        """Check the level of the attackers when the constant is dropped and all three dummies are kept."""
        tutte = np.column_stack([X[:, 1:5], dif, cen, att])
        alt = sm.OLS(y, tutte).fit()
        stessa_adattamento = abs(alt.ssr - res.ssr) < 1e-8
        return (stessa_adattamento
                and abs(alt.params[6] - risposte["liv_att"].valore) < 1e-9
                and abs(alt.params[4] - res.params[0] - res.params[5]) < 1e-9
                and abs(alt.params[5] - res.params[0]) < 1e-9)

    def f_come_statsmodels(risposte):
        """Check the F statistic of the SSR formula against the joint test on the two role dummies."""
        r = np.zeros((2, len(res.params)))
        r[0, 5], r[1, 6] = 1.0, 1.0
        return abs(float(res.f_test(r).fvalue) - risposte["F"].valore) < 1e-8

    def test_come_statsmodels(_risposte):
        """Check both statistics and their degrees of freedom against statsmodels."""
        piccola = sm.add_constant(np.column_stack([gol, pres, esper]))
        return (abs(het_breuschpagan(res.resid, X)[0] - bp.lm) < 1e-8
                and abs(het_white(res.resid, piccola)[0] - wh.lm) < 1e-8
                and bp.gl == 6 and wh.gl == 9)

    def effetto_decrescente(_risposte):
        """Check on the fitted curve that one more year of experience adds less and less."""
        b = res.params
        passo = [b[3] * 1.0 + b[4] * ((x + 1) ** 2 - x ** 2) for x in (2.0, 8.0, 14.0)]
        return passo[0] > passo[1] > passo[2]

    def figura_ruoli(path):
        """Draw the role gaps against the omitted role, and the same roles as levels without constant."""
        es, plt = _stile()
        r = _righe(res, nomi)
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.7), gridspec_kw={"width_ratios": [1.2, 1]})
        voci = [("centrocampista\n(riferimento)", 0.0, None, None, es.GRAY)]
        for etichetta, k, colore in (("difensore", "dif", es.TEAL), ("attaccante", "att", es.BLUE)):
            voci.append((etichetta, 100 * r[k]["coef"], 100 * (r[k]["coef"] - Z * r[k]["se"]),
                         100 * (r[k]["coef"] + Z * r[k]["se"]), colore))
        _intervalli(a1, es, voci, "differenza di salario, in % (IC al 95%)")
        a1.set_title("con la costante")
        livelli = [("centrocampista", r["const"]["coef"], es.GRAY),
                   ("difensore", r["const"]["coef"] + r["dif"]["coef"], es.TEAL),
                   ("attaccante", r["const"]["coef"] + r["att"]["coef"], es.BLUE)]
        for k, (etichetta, v, colore) in enumerate(livelli):
            a2.plot([v], [k], "o", color=colore, ms=7)
            a2.annotate(_virgola(v, 3), xy=(v, k), xytext=(0, 8), textcoords="offset points",
                        ha="center", fontsize=8.5, color=colore)
        a2.set_yticks(range(3), [v[0] for v in livelli])
        a2.set_ylim(-0.6, 2.7)
        a2.margins(x=0.25)
        a2.set_xlabel("log-salario atteso (livello)")
        a2.set_title("senza la costante")
        es.commas(a2, "x")
        fig.subplots_adjust(wspace=0.55)
        es.save(fig, path)

    def figura_f(path):
        """Draw the F statistic against the rejection region of the F distribution."""
        es = figs.use_style()
        f = truth["F"].valore
        fig, _ = es.dist_test("F", (int(truth["q"].valore), int(truth["gl"].valore)), stat=f,
                              crit=fcrit, tail="right")
        es.save(fig, path)

    def figura_effetto(path):
        """Draw the marginal effect of experience, which falls with experience."""
        es = figs.use_style()
        fig, _, _ = es.quadratic_effect(res.params[3], res.params[4], xmax=16, xmin=1,
                                        varname="esper", ylabel="effetto marginale su log(salario)")
        es.save(fig, path)

    def figura_varianza(path):
        """Draw the squared residuals against the appearances: a linear fit is flat, a quadratic one is not."""
        es, plt = _stile()
        u2 = res.resid ** 2
        classi = np.digitize(pres, np.quantile(pres, np.linspace(0, 1, 9)[1:-1]))
        medie = np.array([(pres[classi == c].mean(), u2[classi == c].mean()) for c in range(8)])
        g = np.linspace(pres.min(), pres.max(), 100)
        fig, ax = plt.subplots(figsize=(6.1, 3.3))
        ax.plot(pres, u2, "o", color=es.GRAY, ms=2.5, alpha=0.35, label="residui al quadrato")
        ax.plot(medie[:, 0], medie[:, 1], "o-", color=es.BLUE, lw=1.4, ms=5, label="media per classe di presenze")
        ax.plot(g, np.polyval(np.polyfit(pres, u2, 1), g), color=es.RED, lw=1.6,
                label="retta (come Breusch-Pagan)")
        ax.plot(g, np.polyval(np.polyfit(pres, u2, 2), g), color=es.GREEN, lw=1.6, ls="--",
                label="parabola (come White)")
        ax.set_ylim(0, 1.15 * medie[:, 1].max())
        ax.set_xlabel("presenze")
        ax.set_ylabel(r"$\hat\epsilon^2$")
        es.commas(ax)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), fontsize=8, ncol=2)
        es.save(fig, path)

    def figura_gol(path):
        """Draw the percentage gain of the wage as the goals rise, with the target and the given increase."""
        es, plt = _stile()
        b = res.params[1]
        fig, ax = plt.subplots(figsize=(6.1, 2.9))
        s = np.linspace(0, 10, 100)
        ax.plot(s, 100 * b * s, color=es.BLUE, lw=1.6, label=r"$100\,\hat\beta_1\,\Delta$gol")
        ax.axhline(obiettivo, color=es.RED, ls="--", lw=1.0)
        servono = truth["gol_servono"].valore
        ax.plot([servono], [obiettivo], "o", color=es.RED, ms=7, zorder=5)
        ax.plot([dgol], [100 * b * dgol], "o", color=es.GREEN, ms=7, zorder=5)
        ax.annotate(_virgola(servono, 2) + " gol", xy=(servono, obiettivo), xytext=(-6, 8),
                    textcoords="offset points", ha="right", fontsize=8.5, color=es.RED,
                    fontweight="bold")
        ax.annotate(_virgola(100 * b * dgol, 1) + "%", xy=(dgol, 100 * b * dgol), xytext=(6, -14),
                    textcoords="offset points", ha="left", fontsize=8.5, color=es.GREEN,
                    fontweight="bold")
        ax.set_xlabel("gol in più")
        ax.set_ylabel("variazione % attesa del salario")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    def figura_soglia(path):
        """Draw the left-tail rejection region of the one-sided test and the observed t."""
        es = figs.use_style()
        fig, _ = es.dist_test("z", stat=truth["t_riv"].valore, crit=Z1, tail="left")
        es.save(fig, path)

    truth = answers(_righe(res, nomi), n, res.ssr, rist.ssr, k_r, p_bp, p_w)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "fcrit": Numero(fcrit, 2), "dgol": Numero(dgol, 0),
                   "obiettivo": Numero(obiettivo, 0), "riv": Numero(riv, 1)},
        tabelle={"ols": tab, "rist": tab_r,
                 "bp": _blocco("Test di Breusch-Pagan", bp.lm, bp.gl, bp.p),
                 "white": _blocco("Test di White", wh.lm, wh.gl, wh.p)},
        risposte=truth, studente=studente,
        quesiti={"d1a": Quesito("base"), "d1b": Quesito("pct_att"), "d1c": Quesito("liv_att"),
                 "d2a": Quesito("q"), "d2b": Quesito("gl"), "d2c": Quesito("dec_f"),
                 "d3a": Quesito("dec_q"), "d3b": Quesito("decr"),
                 "d4a": Quesito("dec_bp"), "d4b": Quesito("dec_w"), "d4c": Quesito("robusti"),
                 "d5a": Quesito("pct_gol"), "d5b": Quesito("gol_servono"),
                 "d6a": Quesito("soglia"), "d6b": Quesito("t_riv"), "d6c": Quesito("dec_riv")},
        attese=[lambda r: r["base"].valore == RUOLI["cen"], lambda r: r["b_att"].valore > 0 > r["b_dif"].valore,
                lambda r: r["q"].valore == 2 and r["gl"].valore == n - 7,
                lambda r: r["dec_f"] == "rifiuta",
                lambda r: r["dec_q"] == "rifiuta" and r["decr"] == "sì",
                lambda r: r["dec_bp"] == "non rifiuta" and r["dec_w"] == "rifiuta"
                and r["robusti"] == "sì",
                lambda r: r["dec_riv"] == "rifiuta" and r["b_pres"].valore < riv / 100,
                lambda r: 0 < r["pct_gol"].valore < obiettivo,
                senza_costante, f_come_statsmodels, test_come_statsmodels, effetto_decrescente],
        margini=[Margin(stat=truth["F"].valore, crit=fcrit), Margin(stat=truth["t_q"].valore, crit=Z),
                 Margin(stat=truth["t_riv"].valore, crit=Z1),
                 Margin(stat=p_bp, crit=ALFA, rel=MARGINE_P), Margin(stat=p_w, crit=ALFA, rel=MARGINE_P)],
        figure={"ruoli": figura_ruoli, "f": figura_f, "effetto": figura_effetto,
                "varianza": figura_varianza, "gol": figura_gol, "soglia": figura_soglia})


def _ar1(g, n, phi, sigma):
    """Simulate a zero-mean stationary AR(1) of length ``n`` after a warm-up of 300 draws."""
    e = g.normal(0.0, sigma, n + 300)
    u = np.empty(n + 300)
    u[0] = e[0]
    for t in range(1, n + 300):
        u[t] = phi * u[t - 1] + e[t]
    return u[300:]


def _ultimo_fuori(v, banda):
    """Return the last lag (1-based) of ``v`` that leaves the band, or 0 if none does."""
    fuori = np.flatnonzero(np.abs(v) > banda)
    return int(fuori[-1]) + 1 if len(fuori) else 0


def _chow_percorso(y, x, trim=TRIM):
    """Return the candidate break dates and the Chow F at each, for one series or a batch.

    The date ``tau`` is the size of the first sub-sample. The F statistic is
    ``((SSR - SSR1 - SSR2) / 2) / ((SSR1 + SSR2) / (T - 4))`` for the regression on a
    constant and one regressor, and the dates exclude ``trim`` of the sample at each end.
    Sums are cumulated so a whole batch of series costs one pass.

    Args:
        y: Dependent variable, shape ``(T,)`` or ``(reps, T)``.
        x: Regressor, same shape.
        trim: Share of the sample excluded at each end.

    Returns:
        ``(taus, F)`` with ``F`` shaped like ``y`` with the last axis replaced by the dates.
    """
    y2, x2 = np.atleast_2d(y), np.atleast_2d(x)
    T = y2.shape[1]
    taus = np.arange(int(np.ceil(trim * T)), int(np.floor((1 - trim) * T)) + 1)
    cum = [np.cumsum(v, axis=1) for v in (x2, y2, x2 * x2, x2 * y2, y2 * y2)]
    tot = [c[:, -1:] for c in cum]

    def ssr(m, sx, sy, sxx, sxy, syy):
        """Return the SSR of the simple regression from the sums of ``m`` observations."""
        return (syy - sy ** 2 / m) - (sxy - sx * sy / m) ** 2 / (sxx - sx ** 2 / m)

    pieno = ssr(T, *tot)
    s1 = ssr(taus, *(c[:, taus - 1] for c in cum))
    s2 = ssr(T - taus, *(t - c[:, taus - 1] for t, c in zip(tot, cum)))
    f = ((pieno - s1 - s2) / 2) / ((s1 + s2) / (T - 4))
    return taus, (f[0] if np.ndim(y) == 1 else f)


@lru_cache(maxsize=None)
def _qlr_mc(T, reps=3000):
    """Return the Monte Carlo 95th percentile of the QLR statistic under no break.

    Gaussian errors, a stable regression on one regressor, 15% trimming; the generator
    is fixed so the checks always see the same value.
    """
    g = np.random.default_rng(31)
    x = g.normal(size=(reps, T))
    y = 0.2 + 0.9 * x + g.normal(size=(reps, T))
    return float(np.quantile(_chow_percorso(y, x)[1].max(axis=1), 0.95))


def _dummy_f(y, x, tau):
    """Return the F test of the dummy-interaction model that the note uses for the Chow test."""
    d = (np.arange(1, len(y) + 1) > tau).astype(float)
    res = sm.OLS(y, sm.add_constant(np.column_stack([x, d, d * x]))).fit()
    return float(res.f_test(np.array([[0, 0, 1, 0], [0, 0, 0, 1]])).fvalue)


def _nitido(v, banda):
    """Return whether every entry of ``v`` is clearly inside or clearly outside the 5% band."""
    a = np.abs(v)
    return bool(np.all((a <= 0.85 * banda) | (a >= 1.1 * banda)))


@exercise("a02_02", modulo=9, livello=3, punti=13,
          tipo=("adf-decisione-statistica-o-pvalue", "regressione-statica-ben-definita",
                "break-strutturale-qlr", "identificazione-ar-ma-arma"))
def elettricita_e_pil(rng):
    """Judge two integrated series, a spurious level regression, a break in the differences and an AR(1)."""
    T, k, anno0 = 80, 12, 1940
    n_d = T - 1
    banda = Z / np.sqrt(n_d)

    def estrai(g):
        """Draw the growth of the GDP as an AR(1) with drift and an electricity series whose growth breaks.

        Electricity growth is ``a + b dx + u`` with a slope that drops after a date, so the two
        levels are not cointegrated (the cumulated ``u`` is a random walk) while the regression
        in differences has a break.
        """
        dx = 0.006 + _ar1(g, n_d, PHI, 0.014)
        c = np.round(acf(dx, nlags=k, fft=False)[1:], 3)
        p = np.round(pacf(dx, nlags=k, method="ywm")[1:], 3)
        if not (np.all(np.abs(c[:3]) >= 1.25 * banda) and np.all(np.abs(c[7:]) <= 0.85 * banda)
                and abs(p[0]) >= 1.1 * banda and np.all(np.abs(p[1:]) <= 0.85 * banda)
                and _nitido(c, banda)):
            return None
        tau0 = int(0.55 * n_d)
        b = np.where(np.arange(1, T) > tau0, 0.40, 1.05)
        dy = 0.003 + b * dx + g.normal(0.0, 0.016, n_d)
        x = 5.0 + np.r_[0.0, np.cumsum(dx)]
        y = 4.0 + np.r_[0.0, np.cumsum(dy)]
        return SimpleNamespace(x=x, y=y, dx=dx, dy=dy, c=c, p=p)

    def adf(s, termini="c"):
        """Return the ADF statistic with the given deterministic terms and two lagged differences."""
        return float(adfuller(s, maxlag=2, regression=termini, autolag=None)[0])

    def accetta(s):
        """Accept a draw with unmistakable unit roots, a high EG p-value and a clear break."""
        if s is None:
            return False
        s.t = [adf(s.y), adf(s.x), adf(np.diff(s.y)), adf(np.diff(s.x))]
        if not (s.t[0] > -1.9 and s.t[1] > -1.9 and s.t[2] < -3.4 and s.t[3] < -3.4):
            return False
        # The unit roots must also survive a trend in the test, whose 5% value is -3.43.
        if adf(s.y, "ct") < -2.9 or adf(s.x, "ct") < -2.9:
            return False
        s.p_eg = float(coint(s.y, s.x, trend="c")[1])
        statica_s = sm.OLS(s.y, sm.add_constant(s.x)).fit()
        s.taus, s.f = _chow_percorso(s.dy, s.dx)
        return (s.p_eg > 0.15 and s.f.max() >= 7.5 and float(statica_s.tvalues[1]) > 10
                and statica_s.rsquared > 0.9)

    s = None
    for _ in range(40000):
        s = estrai(rng)
        if accetta(s):
            break
    else:
        raise RuntimeError("nessun campione soddisfa le condizioni dell'esempio")

    tau = int(s.taus[np.argmax(s.f)])
    stat_f = float(s.f.max())
    statica, _, tab_statica = _stima(s.y, {"l_pil": s.x})
    campioni = [("intero campione", slice(None)), ("primo sottocampione", slice(0, tau)),
                ("secondo sottocampione", slice(tau, None))]
    diff = [sm.OLS(s.dy[sl], sm.add_constant(s.dx[sl])).fit() for _, sl in campioni]
    anni = [(anno0 + 1, anno0 + n_d), (anno0 + 1, anno0 + tau), (anno0 + tau + 1, anno0 + n_d)]
    righe_d = [(nome, len(r.resid), float(r.params[1]), float(r.bse[1]), a)
               for (nome, _), r, a in zip(campioni, diff, anni)]
    tab_adf = "\n".join(
        ["| serie | statistica ADF, livello | statistica ADF, differenza prima |", "|---|---|---|"]
        + [f"| {nome} | {_m(fmt_sig(a, 4))} | {_m(fmt_sig(b, 4))} |"
           for nome, a, b in (("log(elet)", s.t[0], s.t[2]), ("log(pil)", s.t[1], s.t[3]))])
    tab_qlr = "\n".join(
        ["| campione | anni | osservazioni | coefficiente di Dpil | errore std. |", "|---|---|---|---|---|"]
        + [f"| {nome} | {a[0]}–{a[1]} | {m} | {_m(fmt_sig(b, 6))} | {_m(fmt_sig(e, 6))} |"
           for nome, m, b, e, a in righe_d])

    def stampato(x, cifre):
        """Return ``x`` rounded to ``cifre`` significant digits, as a printed table shows it."""
        return float(fmt_sig(x, cifre).replace(",", "."))

    f_ordinaria = float(stats.f.ppf(1 - ALFA, 2, n_d - 4))
    adf_s = [stampato(v, 4) for v in s.t]
    p_eg_s = _p_stampato(s.p_eg)
    f_s = round(stat_f, 2)
    pend = [(stampato(b, 6), stampato(e, 6)) for _, _, b, e, _ in righe_d]
    cc, cp = s.c, s.p

    def answers(t, p_eg, f_max, pendenze, c_acf, c_pacf, riga, r2):
        """Return every answer from the printed ADF statistics, EG p-value, QLR value, slopes and correlogram.

        ``t`` holds the ADF statistics of log(elet) and log(pil) on the level, then on the difference;
        ``riga`` is the row of ``l_pil`` in the level regression and ``r2`` its R-squared.
        """
        def ordine(t_liv, t_dif):
            """Return the order of integration from the unit-root decisions on level and difference."""
            return 0 if _decide_df(t_liv) == "rifiuta" else (1 if _decide_df(t_dif) == "rifiuta" else 2)

        o_y, o_x = ordine(t[0], t[2]), ordine(t[1], t[3])
        dec_eg = _decide_p(p_eg)
        dec_q = "rifiuta" if f_max > QLR_CRIT else "non rifiuta"
        ultimo_a, ultimo_p = _ultimo_fuori(c_acf, banda), _ultimo_fuori(c_pacf, banda)
        e_ar = ultimo_p < ultimo_a
        return {"dec_y": _decide_df(t[0]), "dec_x": _decide_df(t[1]),
                "ord_y": Numero(float(o_y), 0),
                "dec_eg": dec_eg, "coerente": "sì" if o_y == o_x == 1 else "no",
                "ben_def": "sì" if o_y == o_x == 1 and dec_eg == "rifiuta" else "no",
                "dec_qlr": dec_q, "problema": "sì" if dec_q == "rifiuta" else "no",
                "salto": Numero(pendenze[2][0] - pendenze[1][0], 3),
                "b_primo": Numero(pendenze[1][0], 4), "b_secondo": Numero(pendenze[2][0], 4),
                "b_intero": Numero(pendenze[0][0], 4),
                "stazionaria": "sì" if bool(np.any(np.abs(c_acf) <= banda)) else "no",
                "ar": "sì" if e_ar else "no",
                "ordine": Numero(float(ultimo_p if e_ar else ultimo_a), 0),
                "acf1": Numero(c_acf[0], 3), "acf2": Numero(c_acf[1], 3),
                "acf3": Numero(c_acf[2], 3),
                "pacf1": Numero(c_pacf[0], 3), "pacf2": Numero(c_pacf[1], 3),
                "banda": Numero(banda, 3),
                "t_y": Numero(t[0], 3), "t_x": Numero(t[1], 3), "t_dy": Numero(t[2], 3),
                "t_dx": Numero(t[3], 3), "f_ord": Numero(f_ordinaria, 2),
                "gl_den": Numero(float(n_d - 4), 0), "r2": Numero(r2, 3), "b_stat": Numero(riga["coef"], 4),
                "t_stat": Numero(riga["t"], 1)}

    def studente(tabelle):
        """Rebuild the answers from the printed tables, the EG p-value, the QLR value and the correlogram."""
        st = tabelle["statica"]
        return answers(adf_s, p_eg_s, f_s, pend, cc, cp, st.rows["l_pil"], st.stats["r2"])

    def teoria_coerente(_risposte):
        """Check that an AR(1) has a geometric ACF and a PACF that stops at lag 1."""
        ar = ArmaProcess(ar=np.r_[1.0, -PHI], ma=[1.0])
        return bool(np.all(np.abs(ar.pacf(k + 1)[2:]) < 1e-9)
                    and np.allclose(ar.acf(k + 1)[1:4], PHI ** np.arange(1, 4)))

    def qlr_calibrato(_risposte):
        """Check that the simulated 95th percentile of the QLR statistic is close to the quoted one."""
        return abs(_qlr_mc(n_d) - QLR_CRIT) < 0.6

    def massimo_coerente(_risposte):
        """Check that the maximum of the path is the F of the dummy-interaction model at its date."""
        return abs(_dummy_f(s.dy, s.dx, tau) - stat_f) < 1e-9

    def regressione_spuria(_risposte):
        """Check the trap: the level regression looks excellent while the series are not cointegrated."""
        return float(statica.tvalues[1]) > 10 and statica.rsquared > 0.9

    def eg_coerente(_risposte):
        """Check that the EG p-value is the library one for the regression of log(elet) on log(pil)."""
        return abs(float(coint(s.y, s.x, trend="c")[1]) - s.p_eg) < 1e-12

    def figura_serie(path):
        """Draw the two series in logs, with the end of the first sub-sample."""
        es, plt = _stile()
        anno = np.arange(anno0, anno0 + T)
        fig, ax = plt.subplots(figsize=(6.1, 2.7))
        ax.plot(anno, s.y, color=es.BLUE, lw=1.4, label="log(elet)")
        ax.plot(anno, s.x, color=es.RED, lw=1.4, label="log(pil)")
        ax.set_xlabel("anno")
        es.commas(ax, "y")
        ax.legend(loc="upper left")
        es.save(fig, path)

    def figura_correlogramma(path):
        """Draw the ACF (top) and PACF (bottom) of the differenced GDP with the 5% band."""
        es, plt = _stile()
        fig, ax = plt.subplots(2, 1, figsize=(6.1, 3.7), sharex=True)
        es.acf_pacf(cc, cp, n=n_d, axes=(ax[0], ax[1]))
        ax[1].set_xticks(np.arange(2, k + 1, 2))
        fig.subplots_adjust(hspace=0.12)
        es.save(fig, path)

    def figura_adf(path):
        """Draw the four ADF statistics on a number line against the critical value of the text."""
        es, plt = _stile()
        voci = [("log(elet), livello", s.t[0], es.RED), ("log(pil), livello", s.t[1], es.RED),
                ("log(elet), differenza", s.t[2], es.BLUE), ("log(pil), differenza", s.t[3], es.BLUE)]
        fig, ax = plt.subplots(figsize=(6.1, 2.6))
        lo, hi = min(v[1] for v in voci) - 1.2, max(v[1] for v in voci) + 1.6
        ax.axvspan(lo, DF_C, color=es.REDBG, zorder=0)
        ax.axvline(DF_C, color=es.RED, lw=1.3)
        ax.text(DF_C, -0.5, " valore critico " + _virgola(DF_C, 2), color=es.RED,
                ha="left", va="bottom", fontsize=8)
        for i, (nome, v, colore) in enumerate(voci):
            ax.plot([v], [i], "o", color=colore, ms=7, zorder=5)
            ax.annotate(nome + ": " + _virgola(v, 2), xy=(v, i), xytext=(8, 0),
                        textcoords="offset points", ha="left", va="center", fontsize=8.5,
                        color=colore)
        ax.set_xlim(lo, hi)
        ax.set_ylim(-0.6, len(voci))
        ax.set_yticks([])
        ax.grid(axis="y", visible=False)
        ax.set_xlabel("statistica ADF (si rifiuta la radice unitaria a sinistra del valore critico)")
        es.commas(ax, "x")
        es.save(fig, path)

    def figura_residui(path):
        """Draw the residuals of the level regression and their ACF: they wander, as a random walk does."""
        es, plt = _stile()
        anno = np.arange(anno0, anno0 + T)
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.7), gridspec_kw={"width_ratios": [1.3, 1]})
        a1.plot(anno, statica.resid, color=es.BLUE, lw=1.3)
        a1.axhline(0, color=es.RED, lw=1.0, ls="--")
        a1.set_xlabel("anno")
        a1.set_title(r"residui $\hat u_t$ della regressione in livelli")
        es.commas(a1)
        r = acf(statica.resid, nlags=10, fft=False)[1:]
        a2.vlines(np.arange(1, 11), 0, r, color=es.BLUE, lw=2.4)
        a2.axhspan(-Z / np.sqrt(T), Z / np.sqrt(T), color=es.BLUEBG, zorder=0)
        a2.axhline(0, color=es.GRAY, lw=0.8)
        a2.set_xlabel("ritardo")
        a2.set_title("ACF dei residui")
        es.commas(a2, "y")
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    def figura_qlr(path):
        """Draw the Chow statistic at every admissible date with the QLR and the ordinary F critical values."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.plot(anno0 + s.taus, s.f, color=es.BLUE, lw=1.5, label=r"$F(\tau)$")
        ax.axhline(f_ordinaria, color=es.GRAY, ls="--", lw=1.1,
                   label="F ordinaria al 5%: " + _virgola(f_ordinaria, 2))
        ax.axhline(QLR_CRIT, color=es.RED, lw=1.4, label="QLR al 5%: " + _virgola(QLR_CRIT, 2))
        ax.plot([anno0 + tau], [stat_f], "o", color=es.GREEN, ms=7, zorder=5,
                label="massimo: " + _virgola(stat_f, 2))
        ax.set_xlabel("ultimo anno del primo sottocampione")
        ax.set_ylabel("statistica di Chow")
        es.commas(ax, "y")
        ax.set_ylim(0, 1.45 * stat_f)
        ax.legend(loc="upper left", ncol=2, fontsize=8)
        es.save(fig, path)

    def figura_teoria(path):
        """Draw the sample correlogram (dots) against the theoretical pattern of the AR(1)."""
        es, plt = _stile()
        ritardi = np.arange(1, k + 1)
        ar = ArmaProcess(ar=np.r_[1.0, -PHI], ma=[1.0])
        fig, ax = plt.subplots(2, 1, figsize=(6.1, 3.7), sharex=True)
        for a, teo, camp, nome in ((ax[0], ar.acf(k + 1)[1:], cc, "ACF"), (ax[1], ar.pacf(k + 1)[1:], cp, "PACF")):
            a.axhspan(-banda, banda, color=es.BLUEBG, zorder=0)
            a.vlines(ritardi, 0, teo, color=es.BLUE, lw=2.4)
            a.plot(ritardi, camp, "o", ms=4.5, color=es.RED, zorder=5)
            a.axhline(0, color=es.GRAY, lw=0.8)
            a.set_ylabel(nome)
            es.commas(a, "y")
        ax[0].set_title("AR(1): la PACF si annulla dopo il ritardo 1, l'ACF decade")
        ax[1].set_xlabel("ritardo")
        ax[1].set_xticks(np.arange(2, k + 1, 2))
        fig.subplots_adjust(hspace=0.12)
        es.save(fig, path)

    truth = answers(s.t, s.p_eg, stat_f, [(r[2], r[3]) for r in righe_d], cc, cp,
                    _righe(statica, ["const", "l_pil"])["l_pil"], statica.rsquared)
    return Draft(
        dati=None,
        parametri={"T": Numero(T, 0), "anno0": Numero(anno0, 0), "anno1": Numero(anno0 + T - 1, 0),
                   "anno_t": Numero(anno0 + tau, 0), "anno_u": Numero(anno0 + tau + 1, 0),
                   "cv": Numero(DF_C, 2), "p_eg": Numero(s.p_eg, 4), "F": Numero(f_s, 2),
                   "qcrit": Numero(QLR_CRIT, 2), "k": Numero(k, 0), "n_d": Numero(n_d, 0)},
        tabelle={"adf": tab_adf, "statica": tab_statica, "qlr": tab_qlr},
        risposte=truth, studente=studente,
        quesiti={"d7a": Quesito("dec_y"), "d7b": Quesito("dec_x"), "d7c": Quesito("ord_y"),
                 "d8a": Quesito("dec_eg"), "d8b": Quesito("coerente"), "d8c": Quesito("ben_def"),
                 "d9a": Quesito("dec_qlr"), "d9b": Quesito("problema"), "d9c": Quesito("salto"),
                 "d10a": Quesito("stazionaria"), "d10b": Quesito("ar"), "d10c": Quesito("ordine")},
        attese=[lambda r: r["dec_y"] == "non rifiuta" and r["dec_x"] == "non rifiuta",
                lambda r: r["ord_y"].valore == 1,
                lambda r: r["dec_eg"] == "non rifiuta" and r["coerente"] == "sì" and r["ben_def"] == "no",
                lambda r: r["dec_qlr"] == "rifiuta" and r["problema"] == "sì" and r["salto"].valore < -0.4,
                lambda r: r["stazionaria"] == "sì" and r["ar"] == "sì" and r["ordine"].valore == 1,
                lambda r: s.p_eg < 0.02 or s.p_eg > 0.10,
                teoria_coerente, qlr_calibrato, massimo_coerente, regressione_spuria, eg_coerente],
        margini=[Margin(stat=t, crit=c) for t in s.t for c in (DF_C, MK_C)]
        + [Margin(stat=stat_f, crit=QLR_CRIT)]
        + [Margin(stat=stat_f, crit=_qlr_mc(n_d))],
        figure={"serie": figura_serie, "correlogramma": figura_correlogramma, "adf": figura_adf,
                "residui": figura_residui, "qlr": figura_qlr, "teoria": figura_teoria})
