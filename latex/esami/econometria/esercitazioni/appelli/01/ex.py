"""Simulated exam 1 - consumer spending (log-level, quadratic, VIF) and spot/futures prices (ADF, EG, ECM)."""

from types import SimpleNamespace

import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.config import SIG_COEF
from esercitazioni.lib.gretl import fmt_sig, ols_table, parse_vif, vif_table

TITOLO = "Appello simulato 1"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

# VIF above which the exam solutions diagnose quasi-collinearity.
SOGLIA_VIF = 10.0

# Dickey-Fuller critical value the exam texts hand out for a regression with a constant.
DF_C = -2.38

# Level of the unit-root, Engle-Granger and t tests.
ALFA = 0.05

# Bartlett bandwidth of the HAC standard errors printed with the error-correction model.
BANDA_HAC = 2


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _campiona(g, genera, accetta, tentativi=2000):
    """Return the first draw of ``genera(g)`` that ``accetta`` approves.

    The seed of an exercise is fixed, so the draw is reproducible; the filter only
    keeps samples whose tests stay clear of their thresholds.

    Raises:
        RuntimeError: If no draw is approved within ``tentativi`` attempts.
    """
    for _ in range(tentativi):
        s = genera(g)
        if accetta(s):
            return s
    raise RuntimeError("nessun campione accettabile")


def _lontano(stat, crit, rel=0.15):
    """Return whether ``stat`` clears ``crit`` by the fraction ``rel``, as the bank's margin does."""
    return abs(abs(stat) - abs(crit)) >= rel * abs(crit)


def _decide_z(t):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > Z else "non rifiuta"


def _vif(columns):
    """Return the VIF of each column, 1 / (1 - R_j^2) from its regression on the others."""
    out = {}
    for name in columns:
        others = np.column_stack([v for k, v in columns.items() if k != name])
        r2 = sm.OLS(columns[name], sm.add_constant(others)).fit().rsquared
        out[name] = 1.0 / (1.0 - r2)
    return out


def _cifre(x, sig=SIG_COEF):
    """Return ``x`` as a :class:`Numero` shown with ``sig`` significant digits, as the printed tables do.

    Showing a coefficient with the digits of its table lets a reader repeat the
    arithmetic of a solution and land on the printed result.
    """
    return Numero(x, max(0, sig - 1 - int(np.floor(np.log10(abs(x))))))


def _tabella_ols(res, etichette):
    """Print an OLS fit with the standard error of the regression under the usual statistics."""
    es_regressione = float(np.sqrt(res.ssr / res.df_resid))
    base = ols_table(res, labels=etichette, stats=("n", "r2"))
    return base + f"; E.S. della regressione = {fmt_sig(es_regressione, SIG_COEF)}"


def _righe(res, etichette):
    """Return coefficient, standard error and t ratio of each row at full precision."""
    return {nome: {"coef": float(res.params[i]), "se": float(res.bse[i]), "t": float(res.tvalues[i])}
            for i, nome in enumerate(etichette)}


def _ar1(g, n, phi, sd):
    """Draw a stationary AR(1) path of length ``n`` started from its stationary law."""
    e = g.normal(0.0, sd, n)
    u = np.empty(n)
    u[0] = e[0] / np.sqrt(1.0 - phi**2)
    for t in range(1, n):
        u[t] = phi * u[t - 1] + e[t]
    return u


def _adf(s, nome, ritardi=2):
    """Run the augmented Dickey-Fuller regression of ``s`` with a constant.

    The dependent is the first difference, regressed on a constant, the lagged level
    and ``ritardi`` lagged differences, in the order gretl prints them.

    Returns:
        The fit and the printed table, without the p-value column: the t-based p-value
        of the lagged level is not the p-value of the test.
    """
    d = np.diff(s)
    cols = [np.ones(len(d) - ritardi), s[ritardi:-1]]
    nomi = ["const", f"{nome}_1"]
    for j in range(1, ritardi + 1):
        cols.append(d[ritardi - j:len(d) - j])
        nomi.append(f"d_{nome}_{j}")
    res = sm.OLS(d[ritardi:], np.column_stack(cols)).fit()
    return res, ols_table(res, labels=nomi, p=False, stats=("n",))


def _eg_p(y, x):
    """Return the MacKinnon p-value of the Engle-Granger test of ``y`` on ``x`` with a constant."""
    return round(float(coint(y, x, trend="c")[1]), 4)


def _p_lontano(p):
    """Return an expectation that ``p`` stays outside 0.02-0.10, clear of the 5% threshold."""
    def lontano(_risposte):
        """Check that the p-value is below 0.02 or above 0.10."""
        return p < 0.02 or p > 0.10

    return lontano


def _hac_manuale(X, u, m):
    """Return the Newey-West covariance of OLS with a Bartlett kernel and ``m`` autocovariances.

    Written out from the sandwich formula, to check the library routine the exercise prints.
    """
    A = np.linalg.inv(X.T @ X)
    S = (X * u[:, None]).T @ (X * u[:, None])
    for j in range(1, m + 1):
        G = (X[j:] * u[j:, None]).T @ (X[:-j] * u[:-j, None])
        S += (1 - j / (m + 1)) * (G + G.T)
    return A @ S @ A


def _periodi(lam, q):
    """Return the least number of adjustment periods that absorb at least the share ``q``.

    With the regressor constant and null shocks the residual disequilibrium after
    ``k`` periods is ``(1 + lam) ** k`` of the initial one.
    """
    phi = 1.0 + lam
    if not 0.0 < phi < 1.0:
        raise ValueError("coefficiente di aggiustamento fuori da (-1, 0)")
    resto, k = 1.0, 0
    while resto > 1.0 - q:
        resto *= phi
        k += 1
    return k


def _k_simulato(lungo, lam, q, x_fisso):
    """Iterate the fitted ECM in levels with the regressor held fixed and return the periods that absorb ``q``.

    Starts from a unit disequilibrium in ``t - 1`` and neglects the constant and the
    shocks, so it checks the closed form of :func:`_periodi` against the equation itself.
    """
    a, b = lungo.params
    y = a + b * x_fisso + 1.0
    for k in range(1, 1000):
        y = y + lam * (y - a - b * x_fisso)
        if y - a - b * x_fisso <= 1.0 - q:
            return k
    raise RuntimeError("il disequilibrio non si assorbe")


@exercise("a01_01", modulo=8, livello=3, punti=19,
          tipo=("variazione-percentuale-log-livello", "ic-per-verificare-un-valore",
                "termine-quadratico-nonlinearita", "punto-di-svolta-quadratico",
                "collinearita-diagnosi", "vif-inflazione-errore-standard"))
def spesa_consumatori(rng):
    """Read a log-level model with a quadratic income term: effects, interval, turning point and VIF."""
    n, dx, obiettivo, rid, r0, unita = 200, 10.0, 10.0, 15.0, 3.0, 10000.0
    nomi = ["reddito", "sq_reddito", "eta", "proprietario"]
    etichette = ["const", *nomi]

    def genera(g):
        """Draw the consumers, fit the model and compute the VIF of each regressor."""
        red = np.clip(g.gamma(4.5, 0.78, n), 0.8, 11.0)
        eta = np.round(g.uniform(21.0, 69.0, n))
        p_casa = 1.0 / (1.0 + np.exp(-(-0.3 + 0.15 * (red - 3.5) + 0.01 * (eta - 45.0))))
        casa = (g.random(n) < p_casa).astype(float)
        y = 6.0 + 0.30 * red - 0.028 * red**2 - 0.0065 * eta + 0.05 * casa + g.normal(0.0, 0.45, n)
        cols = dict(zip(nomi, (red, red**2, eta, casa)))
        res = sm.OLS(y, sm.add_constant(np.column_stack(list(cols.values())))).fit()
        return SimpleNamespace(res=res, cols=cols, vifs=_vif(cols), red=red, eta=eta, casa=casa,
                               rmin=round(float(red.min()), 1), rmax=round(float(red.max()), 1))

    def accetta(s):
        """Accept a draw with clear verdicts: a significant quadratic, a dummy that is not, high VIFs only for income."""
        t, b = s.res.tvalues, s.res.params
        punto = -b[1] / (2 * b[2])
        t_riv = (100 * dx * b[3] + rid) / (100 * dx * s.res.bse[3])
        return (abs(t[4]) < 1.5 and t[3] < -2.6 and t[1] > 2.6 and t[2] < -2.6
                and s.vifs["reddito"] > 11.5 and s.vifs["sq_reddito"] > 11.5
                and s.vifs["eta"] < 8.5 and s.vifs["proprietario"] < 8.5
                and s.rmin + 0.8 < punto < s.rmax - 0.8 and abs(t_riv) > 2.4)

    s = _campiona(rng, genera, accetta)
    tab_ols = _tabella_ols(s.res, etichette)
    tab_vif = vif_table(s.vifs)

    def answers(r, vif):
        """Return every answer from the OLS rows (coefficient, se, t) and the VIF of each regressor."""
        b1, b2, b3, b4 = (r[k]["coef"] for k in nomi)
        se1, se3 = r["reddito"]["se"], r["eta"]["se"]
        t2, t4 = r["sq_reddito"]["t"], r["proprietario"]["t"]
        stima, se_pct = 100 * dx * b3, 100 * dx * se3
        lo, hi = stima - Z * se_pct, stima + Z * se_pct
        punto = -b1 / (2 * b2)
        alti = [k for k, v in vif.items() if v > SOGLIA_VIF]
        resto = max(v for k, v in vif.items() if k not in alti)
        dec_b2 = _decide_z(t2)
        return {
            "pct": Numero(100 * b4, 1), "b_prop": _cifre(b4), "t_prop": Numero(t4, 2),
            "anni": Numero(-obiettivo / (100 * b3), 1), "b_eta": _cifre(b3),
            "stima": Numero(stima, 2), "se_pct": Numero(se_pct, 2), "se_eta": _cifre(se3),
            "ic_lo": Numero(lo, 2), "ic_hi": Numero(hi, 2), "compat": "sì" if lo <= -rid <= hi else "no",
            "t_riv": Numero((stima + rid) / se_pct, 2),
            "dec_b2": dec_b2, "t_sq": Numero(t2, 2), "decr": "sì" if dec_b2 == "rifiuta" and b2 < 0 else "no",
            "b_red": _cifre(b1), "b_sq": _cifre(b2), "t_red": Numero(r["reddito"]["t"], 2),
            "eff": Numero(100 * (b1 + 2 * b2 * r0), 1), "punto": Numero(punto, 2),
            "punto_mila": Numero(punto * unita / 1000.0, 0),
            "dentro": "sì" if s.rmin <= punto <= s.rmax else "no",
            "conta": Numero(float(len(alti)), 0), "resto": Numero(resto, 3),
            "vif_red": Numero(vif["reddito"], 3), "vif_sq": Numero(vif["sq_reddito"], 3),
            "vif_eta": Numero(vif["eta"], 3), "vif_prop": Numero(vif["proprietario"], 3),
            "spiega": "sì" if vif["proprietario"] > SOGLIA_VIF and abs(t4) < Z else "no",
            "f_red": Numero(np.sqrt(vif["reddito"]), 2), "f_sq": Numero(np.sqrt(vif["sq_reddito"]), 2),
            "se_red": _cifre(se1), "se_ideale": _cifre(se1 / np.sqrt(vif["reddito"]), 4),
        }

    def studente(tabelle):
        """Rebuild the answers from the printed OLS rows and the printed VIF table."""
        rows = tabelle["ols"].rows
        return answers({k: rows[k] for k in etichette}, parse_vif(tab_vif))

    def derivata_coerente(_risposte):
        """Check that the marginal-effect formula matches a numeric derivative of the fitted curve."""
        h = 1e-4

        def fitted(x):
            """Return the fitted log spending at income ``x`` for a 40-year-old owner."""
            return np.array([1.0, x, x * x, 40.0, 1.0]) @ s.res.params

        numerica = (fitted(r0 + h) - fitted(r0 - h)) / (2 * h)
        return abs(numerica - (s.res.params[1] + 2 * s.res.params[2] * r0)) < 1e-8

    def inversione_coerente(r):
        """Check with the fitted equation that the years of the answer give the target change."""
        x0 = np.array([1.0, 3.0, 9.0, 40.0, 0.0])
        x1 = x0 + np.array([0.0, 0.0, 0.0, r["anni"].valore, 0.0])
        return abs((x1 - x0) @ s.res.params + obiettivo / 100) < 1e-3 * obiettivo / 100

    def identita_vif(_risposte):
        """Check Var(b_j) = sigma^2 * VIF_j / SST_j exactly, so se / sqrt(VIF) is the independent-regressor se."""
        s2 = s.res.ssr / s.res.df_resid
        sst = {k: np.sum((v - v.mean())**2) for k, v in s.cols.items()}
        return all(abs(s.res.bse[i + 1]**2 - s2 * s.vifs[k] / sst[k]) < 1e-12 for i, k in enumerate(nomi))

    def figura_effetti(path):
        """Draw the fitted log spending against age for owners and non-owners, with both effects marked."""
        es, plt = _stile()
        p = s.res.params
        r_med = float(s.red.mean())
        eta = np.linspace(21.0, 69.0, 100)

        def fitted(a, casa):
            """Return the fitted log spending at age ``a`` and mean income."""
            return p[0] + p[1] * r_med + p[2] * r_med**2 + p[3] * a + p[4] * casa

        fig, ax = plt.subplots(figsize=(6.1, 3.1))
        ax.plot(eta, fitted(eta, 0.0), color=es.BLUE, lw=1.6, label="non proprietario")
        ax.plot(eta, fitted(eta, 1.0), color=es.RED, lw=1.6, label="proprietario")
        a1, a2, a_casa = 30.0, 30.0 + dx, 62.0
        ax.annotate("", xy=(a_casa, fitted(a_casa, 1.0)), xytext=(a_casa, fitted(a_casa, 0.0)),
                    arrowprops={"arrowstyle": "<->", "color": es.RED, "lw": 1.2})
        ax.annotate(f"{100 * p[4]:+.1f}%".replace(".", ","), xy=(a_casa, fitted(a_casa, 0.5)),
                    xytext=(6, 0), textcoords="offset points", fontsize=9, color=es.RED, fontweight="bold",
                    va="center", bbox={"boxstyle": "round,pad=0.15", "fc": "white", "ec": "none"})
        ax.plot([a1, a2], [fitted(a1, 0.0), fitted(a2, 0.0)], "o", color=es.BLUE, ms=6, zorder=5)
        ax.annotate(f"{dx:g} anni: {100 * dx * p[3]:+.2f}%".replace(".", ","),
                    xy=(a2, fitted(a2, 0.0)), xytext=(8, -16), textcoords="offset points",
                    fontsize=9, color=es.BLUE, fontweight="bold")
        ax.set_xlabel("età (anni)")
        ax.set_ylabel("log(spesa) attesa, a reddito medio")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    def figura_ic(path):
        """Draw the 95% interval of the percentage effect of ``dx`` years against the claim."""
        es = figs.use_style()
        stima = 100 * dx * s.res.params[3]
        err = 100 * dx * s.res.bse[3]
        fig, _ = es.ci_line(stima, stima - Z * err, stima + Z * err, h0=-rid, decimals=2, unit="%",
                            xlabel=f"variazione percentuale attesa della spesa per {dx:g} anni in più")
        es.save(fig, path)

    def figura_test_sq(path):
        """Draw the t ratio of the squared term against the two-sided rejection region at 5%."""
        es = figs.use_style()
        t2 = float(s.res.tvalues[2])
        lim = max(4.5, 1.2 * abs(t2))
        fig, _ = es.dist_test("z", stat=t2, crit=Z, tail="two", xlim=(-lim, lim),
                              statlabel=f"$t$ = {t2:.2f}".replace(".", ","))
        es.save(fig, path)

    def figura_svolta(path):
        """Draw the marginal effect of income: positive up to the turning point, negative after it."""
        es = figs.use_style()
        b1, b2 = float(s.res.params[1]), float(s.res.params[2])
        fig, ax, _ = es.quadratic_effect(b1, b2, xmin=0.0, xmax=s.rmax + 1.0, varname="reddito",
                                         ylabel="effetto marginale su log(spesa)")
        ax.plot([r0], [b1 + 2 * b2 * r0], "s", color=es.BLUE, ms=7, zorder=6)
        ax.annotate(f"reddito {r0:g}: {100 * (b1 + 2 * b2 * r0):.1f}%".replace(".", ","),
                    xy=(r0, b1 + 2 * b2 * r0), xytext=(8, 8), textcoords="offset points",
                    fontsize=8.5, color=es.BLUE, fontweight="bold")
        ax.axvspan(s.rmin, s.rmax, color=es.BLUEBG, zorder=0)
        es.save(fig, path)

    def figura_vif(path):
        """Draw each VIF against the threshold of 10."""
        es, plt = _stile()
        nomi_v = list(s.vifs)
        pos = np.arange(len(nomi_v))[::-1]
        valori = np.array([s.vifs[k] for k in nomi_v])
        fig, ax = plt.subplots(figsize=(6.1, 2.4))
        ax.barh(pos, valori, color=[es.RED if v > SOGLIA_VIF else es.BLUE for v in valori])
        ax.axvline(SOGLIA_VIF, color=es.GRAY, ls="--", lw=1.0)
        ax.set_yticks(pos, nomi_v)
        ax.set_xlabel("VIF (soglia tratteggiata)")
        es.commas(ax, "x")
        es.save(fig, path)

    def figura_inflazione(path):
        """Draw the interval of the income coefficient with its own se and with the independent-regressor se."""
        es, plt = _stile()
        b, se = float(s.res.params[1]), float(s.res.bse[1])
        ideale = se / np.sqrt(s.vifs["reddito"])
        fig, ax = plt.subplots(figsize=(6.1, 2.2))
        ax.errorbar(b, 1, xerr=Z * se, fmt="o", color=es.RED, capsize=4, label="errore standard stimato")
        ax.errorbar(b, 0, xerr=Z * ideale, fmt="o", color=es.BLUE, capsize=4,
                    label="errore standard con regressori indipendenti")
        ax.axvline(0, color=es.GRAY, lw=0.8)
        ax.set_yticks([])
        ax.set_ylim(-0.6, 1.6)
        ax.set_xlabel(r"$\hat\beta_1$ (reddito) con intervallo di confidenza al 95%")
        es.commas(ax, "x")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=1)
        es.save(fig, path)

    truth = answers(_righe(s.res, etichette), s.vifs)
    t_sq = float(s.res.tvalues[2])
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "unita": Numero(unita, 0), "dx": Numero(dx, 0),
                   "obiettivo": Numero(obiettivo, 0), "rid": Numero(rid, 0), "r0": Numero(r0, 0),
                   "rmin": Numero(s.rmin, 1), "rmax": Numero(s.rmax, 1)},
        tabelle={"ols": tab_ols, "vif": tab_vif}, risposte=truth, studente=studente,
        quesiti={"d1a": Quesito("pct"), "d1b": Quesito("anni"),
                 "d2a": Quesito("ic_lo"), "d2b": Quesito("ic_hi"), "d2c": Quesito("compat"),
                 "d3a": Quesito("dec_b2"), "d3b": Quesito("decr"),
                 "d4a": Quesito("eff"), "d4b": Quesito("punto"), "d4c": Quesito("dentro"),
                 "d5a": Quesito("conta"), "d5b": Quesito("spiega"),
                 "d6a": Quesito("f_red"), "d6b": Quesito("f_sq")},
        attese=[lambda r: r["compat"] == "no", lambda r: r["dec_b2"] == "rifiuta",
                lambda r: r["decr"] == "sì", lambda r: r["dentro"] == "sì",
                lambda r: r["conta"].valore == 2, lambda r: r["spiega"] == "no",
                lambda r: r["eff"].valore > 0 and r["punto"].valore > r0,
                lambda r: 5 < r["anni"].valore < 40,
                derivata_coerente, inversione_coerente, identita_vif],
        margini=[Margin(stat=t_sq, crit=Z), Margin(stat=float(s.res.tvalues[4]), crit=Z),
                 Margin(stat=truth["t_riv"].valore, crit=Z),
                 Margin(stat=s.vifs["reddito"], crit=SOGLIA_VIF), Margin(stat=s.vifs["sq_reddito"], crit=SOGLIA_VIF),
                 Margin(stat=s.vifs["eta"], crit=SOGLIA_VIF), Margin(stat=s.vifs["proprietario"], crit=SOGLIA_VIF)],
        figure={"effetti": figura_effetti, "ic": figura_ic, "test_sq": figura_test_sq,
                "svolta": figura_svolta, "vif": figura_vif, "inflazione": figura_inflazione})


@exercise("a01_02", modulo=8, livello=3, punti=13,
          tipo=("adf-lettura-output-regressione", "cointegrazione-decisione",
                "ecm-ben-definito", "ecm-velocita-assorbimento"))
def spot_futures(rng):
    """Read two ADF regressions and an Engle-Granger p-value, judge an ECM with HAC errors and time its adjustment."""
    n, q = 96, 0.85

    def genera(g):
        """Draw a cointegrated spot-futures pair, run the three tests and estimate the ECM by two steps."""
        dfut = _ar1(g, n, -0.25, 35.0)
        fut = 1100.0 + np.cumsum(4.0 + dfut)
        spot = -15.0 + 1.01 * fut + _ar1(g, n, 0.70, 12.0)
        res_f, tab_f = _adf(fut, "futures")
        res_s, tab_s = _adf(spot, "spot")
        lungo = sm.OLS(spot, sm.add_constant(fut)).fit()
        X = np.column_stack([np.ones(n - 1), np.diff(fut), lungo.resid[:-1]])
        ecm = sm.OLS(np.diff(spot), X).fit()
        hac = ecm.get_robustcov_results(cov_type="HAC", maxlags=BANDA_HAC)
        return SimpleNamespace(fut=fut, spot=spot, res_f=res_f, res_s=res_s, tab_f=tab_f, tab_s=tab_s,
                               lungo=lungo, X=X, ecm=ecm, hac=hac, p=_eg_p(spot, fut))

    def accetta(s):
        """Accept a draw with clear verdicts, a distracting lagged difference and a horizon clear of the target."""
        lam = s.hac.params[2]
        if not (0.60 < 1.0 + lam < 0.80):
            return False
        k = _periodi(lam, q)
        orizzonte = all(_lontano((1.0 + lam) ** j, 1.0 - q, 0.04) for j in (k - 1, k))
        return (s.res_f.tvalues[1] > -1.9 and s.res_s.tvalues[1] > -1.9 and s.res_s.tvalues[2] < -2.6
                and 0.001 <= s.p < 0.02 and s.hac.tvalues[2] < -3.0 and abs(s.hac.tvalues[0]) < 1.5
                and orizzonte and s.fut.min() > 400.0)

    s = _campiona(rng, genera, accetta)
    tab_ecm = ols_table(s.hac, labels=["const", "d_futures", "ecm_1"], stats=("n", "r2"))
    n_ecm = int(s.hac.nobs)

    def answers(t_f, t_s, t_ds, p, lam, t_lam):
        """Return every answer from the two printed lagged-level t ratios, the p-value and the ECM row."""
        dec_f = "rifiuta" if t_f < DF_C else "non rifiuta"
        dec_s = "rifiuta" if t_s < DF_C else "non rifiuta"
        dec_eg = "rifiuta" if p < ALFA else "non rifiuta"
        coint_ok = dec_f == "non rifiuta" and dec_s == "non rifiuta" and dec_eg == "rifiuta"
        k = _periodi(lam, q) if -1.0 < lam < 0.0 else 0
        phi = 1.0 + lam
        return {"t_f": Numero(t_f, 2), "t_s": Numero(t_s, 2), "t_ds": Numero(t_ds, 2),
                "dec_f": dec_f, "dec_s": dec_s, "dec_eg": dec_eg, "coint": "sì" if coint_ok else "no",
                "dec_lam": _decide_z(t_lam), "ben_def": "sì" if coint_ok and lam < 0 and t_lam < -Z else "no",
                "lam": _cifre(lam), "t_lam": Numero(t_lam, 2), "primo": Numero(-100 * lam, 1),
                "phi": Numero(phi, 6), "k": Numero(k, 0), "km": Numero(k - 1, 0),
                "obiettivo": Numero(1 - q, 2), "log": Numero(np.log(1 - q) / np.log(phi), 2),
                "resto": Numero(phi**k, 4), "resto_prima": Numero(phi ** (k - 1), 4),
                "assorbito": Numero(100 * (1 - phi**k), 1)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of the two ADF tables, the p-value and the row of ``ecm_1``."""
        r = tabelle["ecm"].rows["ecm_1"]
        return answers(tabelle["adf_f"].rows["futures_1"]["t"], tabelle["adf_s"].rows["spot_1"]["t"],
                       tabelle["adf_s"].rows["d_spot_1"]["t"], s.p, r["coef"], r["t"])

    def hac_coerente(_risposte):
        """Check the printed HAC standard errors against the sandwich formula written out from scratch."""
        cov = _hac_manuale(s.X, s.ecm.resid, BANDA_HAC)
        return np.allclose(np.sqrt(np.diag(cov)), s.hac.bse, rtol=0, atol=1e-9)

    def ricorsione_coerente(r):
        """Check that iterating the fitted equation gives the horizon of the closed form."""
        return _k_simulato(s.lungo, float(s.hac.params[2]), q, float(s.fut[-1])) == r["k"].valore

    def figura_serie(path):
        """Draw the two monthly series, which move together and trend upward."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.8))
        mese = np.arange(1, n + 1)
        ax.plot(mese, s.spot, color=es.BLUE, lw=1.4, label="spot")
        ax.plot(mese, s.fut, color=es.RED, lw=1.0, ls="--", label="futures")
        ax.set_xlabel("mese")
        ax.set_ylabel("prezzo dell'indice")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    def figura_adf(path):
        """Draw the two lagged-level t ratios against the left rejection region of the ADF test."""
        es, plt = _stile()
        valori = [float(s.res_s.tvalues[1]), float(s.res_f.tvalues[1])]
        fig, ax = plt.subplots(figsize=(6.1, 2.1))
        lo, hi = min(min(valori), DF_C) - 1.0, max(max(valori), 0.0) + 1.0
        ax.axvspan(lo, DF_C, color=es.REDBG, label="regione di rifiuto")
        ax.axvline(DF_C, color=es.RED, ls="--", lw=1.1)
        for i, (nome, v) in enumerate(zip(("spot", "futures"), valori)):
            ax.plot([v], [i], "o", color=es.BLUE, ms=7, zorder=5)
            ax.annotate(f"{nome}: {v:.2f}".replace(".", ","), xy=(v, i), xytext=(0, 9),
                        textcoords="offset points", ha="center", fontsize=8.5, color=es.BLUE)
        ax.set_xlim(lo, hi)
        ax.set_ylim(-0.7, 1.7)
        ax.set_yticks([])
        ax.set_xlabel("statistica $t$ del livello ritardato (valore critico $" + f"{DF_C:.2f}".replace(".", "{,}") + "$)")
        es.commas(ax, "x")
        ax.legend(loc="upper right")
        es.save(fig, path)

    def figura_eg(path):
        """Draw the long-run residuals around zero and the Engle-Granger p-value against the 5% threshold."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.5), gridspec_kw={"width_ratios": [1.6, 1.0]})
        a1.plot(np.arange(1, n + 1), s.lungo.resid, color=es.BLUE, lw=1.2)
        a1.axhline(0, color=es.GRAY, lw=0.8)
        a1.set_xlabel("mese")
        a1.set_title("residui di lungo periodo")
        a2.axvspan(0, ALFA, color=es.REDBG)
        a2.axvline(ALFA, color=es.RED, ls="--", lw=1.1)
        a2.plot([s.p], [0], "o", color=es.GREEN, ms=8, zorder=5)
        a2.annotate(f"p = {s.p:.4f}".replace(".", ","), xy=(s.p, 0), xytext=(8, 10),
                    textcoords="offset points", ha="left", fontsize=9, color=es.GREEN)
        a2.set_xlim(-0.01, 0.2)
        a2.set_ylim(-0.6, 0.9)
        a2.set_yticks([])
        a2.set_xlabel("p-value EG (soglia $0{,}05$)")
        a2.grid(axis="y", visible=False)
        for ax in (a1, a2):
            es.commas(ax, "x")
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    def figura_lambda(path):
        """Draw the 95% interval of the adjustment coefficient, HAC standard error, against zero."""
        es = figs.use_style()
        lam, err = float(s.hac.params[2]), float(s.hac.bse[2])
        fig, _ = es.ci_line(lam, lam - Z * err, lam + Z * err, h0=0.0, decimals=4,
                            xlabel=r"coefficiente di aggiustamento $\lambda$")
        es.save(fig, path)

    def figura_assorbimento(path):
        """Draw the share of disequilibrium left after each period, with the horizon of the target."""
        es = figs.use_style()
        fig, _, _ = es.decay(float(s.hac.params[2]), horizon=int(truth["k"].valore) + 3, targets=(q,))
        es.save(fig, path)

    truth = answers(float(s.res_f.tvalues[1]), float(s.res_s.tvalues[1]), float(s.res_s.tvalues[2]),
                    s.p, float(s.hac.params[2]), float(s.hac.tvalues[2]))
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "n_ecm": Numero(n_ecm, 0), "cv": Numero(DF_C, 2),
                   "p_eg": Numero(s.p, 4), "q": Numero(100 * q, 0), "banda": Numero(BANDA_HAC, 0)},
        tabelle={"adf_f": s.tab_f, "adf_s": s.tab_s, "ecm": tab_ecm}, risposte=truth, studente=studente,
        quesiti={"d7a": Quesito("t_s"), "d7b": Quesito("dec_f"), "d7c": Quesito("dec_s"),
                 "d8a": Quesito("dec_eg"), "d8b": Quesito("coint"),
                 "d9a": Quesito("dec_lam"), "d9b": Quesito("ben_def"),
                 "d10a": Quesito("primo"), "d10b": Quesito("k")},
        attese=[lambda r: r["dec_f"] == "non rifiuta" and r["dec_s"] == "non rifiuta",
                lambda r: r["coint"] == "sì", lambda r: r["ben_def"] == "sì",
                lambda r: r["t_ds"].valore < DF_C, _p_lontano(s.p), hac_coerente, ricorsione_coerente],
        margini=[Margin(stat=float(s.res_f.tvalues[1]), crit=DF_C), Margin(stat=float(s.res_s.tvalues[1]), crit=DF_C),
                 Margin(stat=s.p, crit=ALFA, rel=0.6), Margin(stat=float(s.hac.tvalues[2]), crit=Z)],
        figure={"serie": figura_serie, "adf": figura_adf, "eg": figura_eg, "lambda": figura_lambda,
                "assorbimento": figura_assorbimento})
