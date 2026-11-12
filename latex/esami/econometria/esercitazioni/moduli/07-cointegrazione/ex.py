"""Module 07 - cointegration: Engle-Granger, DOLS and error-correction models."""

from types import SimpleNamespace

import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, adfuller, coint, pacf

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import ols_table

TITOLO = "Cointegrazione e correzione dell'errore"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

# Dickey-Fuller critical values the exam texts hand out: constant only, constant and trend.
DF_C = -2.38
DF_T = -3.43

# Level of the unit-root and Engle-Granger tests.
ALFA = 0.05


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _num(x, d):
    """Format ``x`` as a math-mode table cell with ``d`` decimals and a decimal comma."""
    return f"${Numero(x, d).tex()}$"


def _tabella(intestazioni, righe):
    """Render a Markdown table from header cells and rows of preformatted cells."""
    linee = ["| " + " | ".join(intestazioni) + " |", "|" + "---|" * len(intestazioni)]
    linee += ["| " + " | ".join(r) + " |" for r in righe]
    return "\n".join(linee)


def _lontano(stat, crit, rel=0.15):
    """Return whether ``stat`` clears ``crit`` by the fraction ``rel``, as the bank's margin does."""
    return abs(abs(stat) - abs(crit)) >= rel * abs(crit)


def _df(t, crit=DF_C):
    """Return the one-sided Dickey-Fuller decision, in the words of the exam."""
    return "rifiuta" if t < crit else "non rifiuta"


def _dec_p(p):
    """Return the decision of a test with null hypothesis rejected for a p-value below 5%."""
    return "rifiuta" if p < ALFA else "non rifiuta"


def _p_lontano(p):
    """Return an expectation that ``p`` stays outside 0.02-0.10, clear of the 5% threshold."""
    def lontano(_risposte):
        """Check that the p-value is below 0.02 or above 0.10."""
        return p < 0.02 or p > 0.10

    return lontano


def _campiona(g, genera, accetta, tentativi=600):
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


def _ar1(g, n, phi, sd):
    """Draw a stationary AR(1) path of length ``n`` started from its stationary law."""
    e = g.normal(0.0, sd, n)
    u = np.empty(n)
    u[0] = e[0] / np.sqrt(1.0 - phi**2)
    for t in range(1, n):
        u[t] = phi * u[t - 1] + e[t]
    return u


def _passeggiata(g, n, x0, drift, sd):
    """Draw a random walk with drift of length ``n`` started at ``x0``."""
    return x0 + np.cumsum(drift + g.normal(0.0, sd, n))


def _coppia(g, n, a, b, phi, su, x0, drift, sx):
    """Draw a cointegrated pair: ``x`` a random walk with drift, ``y = a + b x + u``, ``u`` AR(1)."""
    x = _passeggiata(g, n, x0, drift, sx)
    return x, a + b * x + _ar1(g, n, phi, su)


def _adf(s, nome, ritardi=1, trend=False):
    """Run the augmented Dickey-Fuller regression of ``s``.

    The dependent is the first difference, regressed on a constant, an optional linear
    trend, the lagged level and ``ritardi`` lagged differences.

    Returns:
        The printed table (no p-value column, since the t-based p-value of the lagged
        level is not the test's) and the t ratio of the lagged level.
    """
    d = np.diff(s)
    liv = s[ritardi:-1]
    cols, nomi = [np.ones(len(liv))], ["const"]
    if trend:
        cols.append(np.arange(ritardi + 1, len(s), dtype=float))
        nomi.append("trend")
    cols.append(liv)
    nomi.append(f"{nome}_1")
    for j in range(1, ritardi + 1):
        cols.append(d[ritardi - j:len(d) - j])
        nomi.append(f"d_{nome}_{j}")
    res = sm.OLS(d[ritardi:], np.column_stack(cols)).fit()
    return ols_table(res, labels=nomi, p=False, stats=("n",)), float(res.tvalues[nomi.index(f"{nome}_1")])


def _adf_p(s):
    """Return the MacKinnon p-value of the Dickey-Fuller test with a constant and one lagged difference."""
    return round(float(adfuller(s, maxlag=1, regression="c", autolag=None)[1]), 4)


def _eg_p(y, x):
    """Return the MacKinnon p-value of the Engle-Granger test of ``y`` on ``x`` with a constant."""
    return round(float(coint(y, x, trend="c")[1]), 4)


def _ecm(y, x, nx):
    """Estimate the two-step error-correction model of ``y`` on ``x``.

    The long-run regression gives the residual that enters the ECM lagged once.

    Returns:
        The long-run fit, the ECM fit and the ECM table.
    """
    lungo = sm.OLS(y, sm.add_constant(x)).fit()
    X = np.column_stack([np.ones(len(y) - 1), np.diff(x), lungo.resid[:-1]])
    res = sm.OLS(np.diff(y), X).fit()
    return lungo, res, ols_table(res, labels=["const", f"d_{nx}", "ecm_1"], stats=("n", "r2"))


def _statica(y, x, nx):
    """Fit the static regression of ``y`` on ``x`` and return the fit and its table."""
    res = sm.OLS(y, sm.add_constant(x)).fit()
    return res, ols_table(res, labels=["const", nx])


def _dols(y, x, ell, banda):
    """Fit the dynamic OLS regression of ``y`` on ``x`` with HAC standard errors.

    The regressors are a constant, the level of ``x`` and ``2 * ell + 1`` terms in
    ``Delta x`` (``ell`` leads, the contemporaneous term and ``ell`` lags). Standard
    errors are Newey-West with a Bartlett kernel of bandwidth ``banda``.
    """
    dx = np.diff(x, prepend=np.nan)
    t = np.arange(ell + 1, len(y) - ell)
    cols = [np.ones(len(t)), x[t]] + [dx[t - j] for j in range(-ell, ell + 1)]
    ols = sm.OLS(y[t], np.column_stack(cols)).fit()
    return ols.get_robustcov_results(cov_type="HAC", maxlags=banda)


def _hac_manuale(X, u, m):
    """Return the Newey-West covariance of OLS with a Bartlett kernel and ``m`` autocovariances.

    Written out from the sandwich formula, to check the library routine the exercises print.
    """
    A = np.linalg.inv(X.T @ X)
    S = (X * u[:, None]).T @ (X * u[:, None])
    for j in range(1, m + 1):
        G = (X[j:] * u[j:, None]).T @ (X[:-j] * u[:-j, None])
        S += (1 - j / (m + 1)) * (G + G.T)
    return A @ S @ A


def _disegno_dols(x, ell, n):
    """Return the DOLS regressors built from scratch, to compare with :func:`_dols`."""
    dx = np.diff(x, prepend=np.nan)
    t = np.arange(ell + 1, n - ell)
    return np.column_stack([np.ones(len(t)), x[t]] + [dx[t - j] for j in range(-ell, ell + 1)]), t


def _dols_coerente(y, x, ell, banda, res):
    """Check a DOLS fit against the regressors and the sandwich formula written out from scratch."""
    X, t = _disegno_dols(x, ell, len(y))
    fit = sm.OLS(y[t], X).fit()
    cov = _hac_manuale(X, fit.resid, banda)
    return (abs(fit.params[1] - res.params[1]) < 1e-9
            and abs(np.sqrt(cov[1, 1]) - res.bse[1]) < 1e-9)


def _k_simulato(lungo, res, q, x_fisso):
    """Iterate the fitted ECM in levels with the regressor held fixed and return the periods that absorb ``q``.

    Starts from a unit disequilibrium in ``t - 1`` and neglects the constant and the
    shocks, so it checks the closed form of :func:`_periodi` against the equation itself.
    """
    lam = res.params[2]
    a, b = lungo.params
    y = a + b * x_fisso + 1.0
    for k in range(1, 1000):
        y = y + lam * (y - a - b * x_fisso)
        if y - a - b * x_fisso <= 1.0 - q:
            return k
    raise RuntimeError("il disequilibrio non si assorbe")


def _acf_pacf(resid, ritardi=12):
    """Return the sample ACF and PACF of ``resid`` at lags ``1..ritardi``."""
    return (acf(resid, nlags=ritardi, fft=False)[1:],
            pacf(resid, nlags=ritardi, method="ywm")[1:])


def _banda(n):
    """Return the 95% band of a sample autocorrelation of ``n`` observations."""
    return Z / np.sqrt(n)


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


def _correlogramma(path, pannelli, n):
    """Draw the ACF and PACF of each panel ``(title, acf, pacf)`` with the 95% bands."""
    es, plt = _stile()
    k = len(pannelli)
    fig, axs = plt.subplots(2, k, figsize=(6.1, 3.7), sharex=True, squeeze=False)
    for j, (titolo, a, p) in enumerate(pannelli):
        es.acf_pacf(a, p, n=n, axes=[axs[0, j], axs[1, j]])
        if k > 1:
            axs[0, j].set_title(titolo)
    for ax in axs[1]:
        ax.set_xticks(np.arange(2, len(pannelli[0][1]) + 1, 2))
    fig.subplots_adjust(hspace=0.25, wspace=0.3)
    es.save(fig, path)


def _figura_test(path, nomi_t, valori_t, crit, nomi_p=(), valori_p=()):
    """Draw Dickey-Fuller t ratios against their critical value and p-values against 5%."""
    es, plt = _stile()
    due = len(valori_p) > 0
    fig, axs = plt.subplots(1, 2 if due else 1, figsize=(6.1, 2.3), squeeze=False,
                            gridspec_kw={"width_ratios": [1.6, 1.0]} if due else None)
    ax = axs[0, 0]
    lo, hi = min(min(valori_t), crit) - 1.0, max(max(valori_t), 0.0) + 1.0
    ax.axvspan(lo, crit, color=es.REDBG, label="regione di rifiuto")
    ax.axvline(crit, color=es.RED, ls="--", lw=1.1)
    for i, (nome, v) in enumerate(zip(nomi_t, valori_t)):
        ax.plot([v], [i], "o", color=es.BLUE, ms=7, zorder=5)
        ax.annotate(f"{nome}: {v:.2f}".replace(".", ","), xy=(v, i), xytext=(0, 9),
                    textcoords="offset points", ha="center", fontsize=8.5, color=es.BLUE)
    ax.set_xlim(lo, hi)
    ax.set_ylim(-0.7, len(valori_t) - 0.3 + 0.4)
    ax.set_yticks([])
    ax.set_xlabel("statistica $t$ (valore critico $" + f"{crit:.2f}".replace(".", "{,}") + "$)")
    es.commas(ax, "x")
    ax.legend(loc="upper right")
    if due:
        bx = axs[0, 1]
        for i, (nome, v) in enumerate(zip(nomi_p, valori_p)):
            bx.plot([v], [i], "o", color=es.GREEN, ms=7, zorder=5)
            bx.annotate(f"{nome}: {v:.4f}".replace(".", ","), xy=(v, i), xytext=(10, 9),
                        textcoords="offset points", ha="left", fontsize=8.5, color=es.GREEN)
        bx.axvspan(0, ALFA, color=es.REDBG)
        bx.axvline(ALFA, color=es.RED, ls="--", lw=1.1)
        bx.set_xlim(0, 1)
        bx.set_ylim(-0.7, len(valori_p) - 0.3 + 0.4)
        bx.set_yticks([])
        bx.set_xlabel("p-value EG (soglia $0{,}05$)")
        es.commas(bx, "x")
    fig.subplots_adjust(wspace=0.25)
    es.save(fig, path)


def _intervalli(ax, es, voci, xlabel, riferimento=None, etichetta=None):
    """Draw one 95% interval per entry ``(height, estimate, se, label, colour)`` and an optional claim."""
    for altezza, stima, err, nome, colore in voci:
        ax.errorbar(stima, altezza, xerr=Z * err, fmt="o", color=colore, capsize=4, label=nome)
    if riferimento is not None:
        ax.axvline(riferimento, color=es.GRAY, ls="--", lw=1.1, label=etichetta)
    ax.set_yticks([])
    ax.set_ylim(-0.6, max(v[0] for v in voci) + 0.6)
    ax.set_xlabel(xlabel)
    es.commas(ax, "x")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2)


@exercise("e07_01", modulo=7, livello=1, tipo="cointegrazione-decisione")
def grano_chicago_rotterdam(rng):
    """Decide cointegration from two Dickey-Fuller regressions and an Engle-Granger p-value."""
    n = 120

    def genera(g):
        """Draw a cointegrated pair of prices and run the three tests."""
        x, y = _coppia(g, n, a=18.0, b=1.05, phi=0.7, su=2.0, x0=190.0, drift=0.3, sx=3.0)
        tab_x, tx = _adf(x, "chi")
        tab_y, ty = _adf(y, "rot")
        return SimpleNamespace(tab_x=tab_x, tab_y=tab_y, tx=tx, ty=ty, p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw that keeps both unit roots clearly and rejects no cointegration clearly."""
        return (all(_lontano(t, DF_C) and t > DF_C for t in (s.tx, s.ty)) and 0.0001 <= s.p < 0.02)

    s = _campiona(rng, genera, accetta)

    def answers(ty, tx, p):
        """Return every answer from the two Dickey-Fuller t ratios and the printed p-value."""
        dec_y, dec_x, dec_eg = _df(ty), _df(tx), _dec_p(p)
        coint_ok = (dec_y, dec_x, dec_eg) == ("non rifiuta", "non rifiuta", "rifiuta")
        return {"dec_y": dec_y, "dec_x": dec_x, "dec_eg": dec_eg,
                "coint": "sì" if coint_ok else "no", "t_y": Numero(ty, 2), "t_x": Numero(tx, 2)}

    def studente(tabelle):
        """Rebuild the answers from the two printed lagged-level rows and the printed p-value."""
        return answers(tabelle["adf_y"].rows["rot_1"]["t"], tabelle["adf_x"].rows["chi_1"]["t"], s.p)

    def figura(path):
        """Draw the two Dickey-Fuller statistics and the Engle-Granger p-value against their thresholds."""
        _figura_test(path, ["rot", "chi"], [s.ty, s.tx], DF_C, ["EG"], [s.p])

    truth = answers(s.ty, s.tx, s.p)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "cv": Numero(DF_C, 2), "p_eg": Numero(s.p, 4)},
        tabelle={"adf_y": s.tab_y, "adf_x": s.tab_x}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_y"), "b": Quesito("dec_x"), "c": Quesito("dec_eg"),
                 "d": Quesito("coint")},
        attese=[lambda r: r["coint"] == "sì", _p_lontano(s.p)],
        margini=[Margin(stat=s.ty, crit=DF_C), Margin(stat=s.tx, crit=DF_C),
                 Margin(stat=s.p, crit=ALFA, rel=0.6)],
        figure={"test": figura})


@exercise("e07_02", modulo=7, livello=1, tipo="regressione-statica-ben-definita")
def spread_bund(rng):
    """Recognise that a static regression between a stationary and an integrated series is ill defined."""
    n = 100

    def genera(g):
        """Draw a stationary spread and an independent integrated yield, and regress one on the other."""
        x = _passeggiata(g, n, x0=3.5, drift=0.0, sd=0.30)
        y = 1.6 + _ar1(g, n, 0.7, 0.25)
        tab_x, tx = _adf(x, "bund")
        tab_y, ty = _adf(y, "spread")
        stat, tab = _statica(y, x, "bund")
        return SimpleNamespace(x=x, y=y, tab_x=tab_x, tab_y=tab_y, tx=tx, ty=ty, tab=tab,
                               t_beta=float(stat.tvalues[1]))

    def accetta(s):
        """Accept a draw whose static t looks significant, which is what makes the regression tempting."""
        return (s.ty < DF_C and _lontano(s.ty, DF_C) and s.tx > DF_C and _lontano(s.tx, DF_C)
                and abs(s.t_beta) > 2.8)

    s = _campiona(rng, genera, accetta)

    def answers(ty, tx, t_beta):
        """Return every answer from the two Dickey-Fuller t ratios and the static t of ``bund``."""
        dec_y, dec_x = _df(ty), _df(tx)
        return {"dec_y": dec_y, "dec_x": dec_x,
                "ben_def": "sì" if dec_y == dec_x == "rifiuta" else "no",
                "coint_possibile": "sì" if dec_y == dec_x == "non rifiuta" else "no",
                "t_y": Numero(ty, 2), "t_x": Numero(tx, 2), "t_beta": Numero(t_beta, 2)}

    def studente(tabelle):
        """Rebuild the answers from the two printed lagged-level rows and the static row of ``bund``."""
        return answers(tabelle["adf_y"].rows["spread_1"]["t"], tabelle["adf_x"].rows["bund_1"]["t"],
                       tabelle["statica"].rows["bund"]["t"])

    def figura(path):
        """Draw the two series: the spread returns to its mean, the yield does not."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.5))
        t = np.arange(1, n + 1)
        a1.plot(t, s.y, color=es.BLUE, lw=1.3)
        a1.axhline(s.y.mean(), color=es.GRAY, ls="--", lw=0.9)
        a1.set_title("spread (stazionaria)")
        a2.plot(t, s.x, color=es.RED, lw=1.3)
        a2.set_title("bund (radice unitaria)")
        for ax in (a1, a2):
            ax.set_xlabel("tempo")
            es.commas(ax)
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    truth = answers(s.ty, s.tx, s.t_beta)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "cv": Numero(DF_C, 2)},
        tabelle={"adf_y": s.tab_y, "adf_x": s.tab_x, "statica": s.tab}, risposte=truth,
        studente=studente,
        quesiti={"a": Quesito("dec_y"), "b": Quesito("dec_x"), "c": Quesito("ben_def"),
                 "d": Quesito("coint_possibile")},
        attese=[lambda r: r["ben_def"] == "no", lambda r: r["dec_y"] == "rifiuta"],
        margini=[Margin(stat=s.ty, crit=DF_C), Margin(stat=s.tx, crit=DF_C)],
        figure={"serie": figura})


@exercise("e07_03", modulo=7, livello=1,
          tipo=("ecm-direzione-aggiustamento", "ecm-ben-definito"))
def consumi_reddito_ecm(rng):
    """Read an error-correction model: significance of the adjustment term and the sign of its push."""
    d = -2.0

    def genera(g):
        """Draw a cointegrated consumption-income pair and estimate its error-correction model."""
        x, y = _coppia(g, 120, a=40.0, b=0.9, phi=0.75, su=0.5, x0=450.0, drift=0.6, sx=1.0)
        lungo, res, tab = _ecm(y, x, "red")
        return SimpleNamespace(res=res, tab=tab, p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw with a clearly negative adjustment term and an insignificant constant."""
        return (s.res.tvalues[2] < -3.0 and abs(s.res.tvalues[0]) < 1.6 and 0.0001 <= s.p < 0.02)

    s = _campiona(rng, genera, accetta)
    n = int(s.res.nobs)

    def answers(lam, t_lam, p):
        """Return every answer from the printed row of ``ecm_1`` and the Engle-Granger p-value."""
        buono = t_lam < -Z and lam < 0 and p < ALFA
        return {"dec_lam": "rifiuta" if abs(t_lam) > Z else "non rifiuta",
                "ben_def": "sì" if buono else "no", "piu_alta": "sì" if lam * d > 0 else "no",
                "delta": Numero(lam * d, 3), "lam": Numero(lam, 4), "t_lam": Numero(t_lam, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``ecm_1``."""
        r = tabelle["ecm"].rows["ecm_1"]
        return answers(r["coef"], r["t"], s.p)

    def effetto_lineare(r):
        """Check with the fitted equation that the disequilibrium moves the forecast by lambda * d."""
        con = s.res.predict(np.array([[1.0, 0.0, d]]))[0]
        senza = s.res.predict(np.array([[1.0, 0.0, 0.0]]))[0]
        return abs((con - senza) - r["delta"].valore) < 1e-3

    def figura(path):
        """Draw the expected change of consumption against the disequilibrium, with the scenario marked."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.9))
        e = np.linspace(-4.0, 4.0, 50)
        lam = s.res.params[2]
        ax.plot(e, lam * e, color=es.BLUE, lw=1.6, label=r"$\hat\lambda\,\mathrm{ecm}_t$")
        ax.axhline(0, color=es.GRAY, lw=0.8)
        ax.axvline(0, color=es.GRAY, lw=0.8)
        ax.plot([d], [lam * d], "o", color=es.RED, ms=7, zorder=5)
        ax.annotate(f"ecm = {d:g}: {lam * d:.3f}".replace(".", ","), xy=(d, lam * d), xytext=(8, 8),
                    textcoords="offset points", fontsize=8.5, color=es.RED, fontweight="bold")
        ax.set_xlabel(r"disequilibrio $\mathrm{ecm}_t$ (punti)")
        ax.set_ylabel(r"effetto sulla variazione attesa di cons")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    truth = answers(float(s.res.params[2]), float(s.res.tvalues[2]), s.p)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "p_eg": Numero(s.p, 4), "d": Numero(d, 1)},
        tabelle={"ecm": s.tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_lam"), "b": Quesito("ben_def"), "c": Quesito("piu_alta"),
                 "d": Quesito("delta")},
        attese=[lambda r: r["dec_lam"] == "rifiuta", lambda r: r["ben_def"] == "sì",
                lambda r: r["piu_alta"] == "sì", _p_lontano(s.p), effetto_lineare],
        margini=[Margin(stat=s.res.tvalues[2], crit=Z), Margin(stat=s.p, crit=ALFA, rel=0.6)],
        figure={"effetto": figura})


@exercise("e07_04", modulo=7, livello=2, tipo="ecm-velocita-assorbimento")
def benzina_assorbimento(rng):
    """Count the periods an error-correction model needs to absorb two given shares of a disequilibrium."""
    n, q1, q2, x_fisso = 150, 0.60, 0.90, 70.0

    def genera(g):
        """Draw a cointegrated pump-price and crude-price pair and estimate its error-correction model."""
        x, y = _coppia(g, n, a=60.0, b=0.45, phi=0.7, su=1.5, x0=x_fisso, drift=0.1, sx=2.0)
        lungo, res, tab = _ecm(y, x, "petr")
        return SimpleNamespace(lungo=lungo, res=res, tab=tab)

    def accetta(s):
        """Accept a draw with a clear adjustment, an insignificant constant and non-borderline horizons."""
        lam, t_c = s.res.params[2], s.res.tvalues[0]
        if not (s.res.tvalues[2] < -3.0 and abs(t_c) < 1.6 and 0.55 < 1 + lam < 0.85):
            return False
        return all(_lontano((1 + lam) ** k, 1 - q, 0.04)
                   for q in (q1, q2) for k in (_periodi(lam, q), _periodi(lam, q) - 1) if k > 0)

    s = _campiona(rng, genera, accetta)

    def answers(lam, t_lam):
        """Return every answer from the printed coefficient and t ratio of ``ecm_1``."""
        k1, k2 = _periodi(lam, q1), _periodi(lam, q2)
        phi = 1.0 + lam
        return {"dec_lam": "rifiuta" if abs(t_lam) > Z else "non rifiuta",
                "primo": Numero(-100 * lam, 2), "k1": Numero(k1, 0), "k2": Numero(k2, 0),
                "assorbito": Numero(100 * (1 - phi**k2), 2), "lam": Numero(lam, 4),
                "t_lam": Numero(t_lam, 2), "phi": Numero(phi, 4),
                "resto1": Numero(phi**k1, 4), "resto1_prima": Numero(phi ** (k1 - 1), 4),
                "resto2": Numero(phi**k2, 4), "resto2_prima": Numero(phi ** (k2 - 1), 4),
                "obiettivo1": Numero(1 - q1, 2), "obiettivo2": Numero(1 - q2, 2),
                "k1m": Numero(k1 - 1, 0), "k2m": Numero(k2 - 1, 0),
                "log1": Numero(np.log(1 - q1) / np.log(phi), 2),
                "log2": Numero(np.log(1 - q2) / np.log(phi), 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``ecm_1``."""
        r = tabelle["ecm"].rows["ecm_1"]
        return answers(r["coef"], r["t"])

    def ricorsione_coerente(r):
        """Check that iterating the fitted equation gives the horizons of the closed form."""
        return (_k_simulato(s.lungo, s.res, q1, x_fisso) == r["k1"].valore
                and _k_simulato(s.lungo, s.res, q2, x_fisso) == r["k2"].valore)

    def figura(path):
        """Draw the share of disequilibrium left after each period, with the two horizons marked."""
        es, plt = _stile()
        fig, _, _ = es.decay(float(s.res.params[2]), horizon=int(truth["k2"].valore) + 3,
                               targets=(q1, q2))
        es.save(fig, path)

    truth = answers(float(s.res.params[2]), float(s.res.tvalues[2]))
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "q1": Numero(100 * q1, 0), "q2": Numero(100 * q2, 0)},
        tabelle={"ecm": s.tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_lam"), "b": Quesito("primo"), "c": Quesito("k1"),
                 "d": Quesito("k2"), "e": Quesito("assorbito")},
        attese=[lambda r: r["dec_lam"] == "rifiuta", lambda r: r["k2"].valore > r["k1"].valore,
                ricorsione_coerente],
        margini=[Margin(stat=s.res.tvalues[2], crit=Z)], figure={"assorbimento": figura})


@exercise("e07_05", modulo=7, livello=2, tipo="cointegrazione-decisione")
def correlogrammi_due_coppie(rng):
    """Decide cointegration from the correlogram of the long-run residuals of two pairs, one of them spurious."""
    n = 100

    def genera(g):
        """Draw a cointegrated pair and an unrelated pair, regress each and compute the correlograms."""
        xa, ya = _coppia(g, n, a=1.0, b=0.95, phi=0.5, su=0.30, x0=6.0, drift=0.02, sx=0.35)
        xb = _passeggiata(g, n, 5.0, 0.03, 0.35)
        yb = _passeggiata(g, n, 4.0, 0.03, 0.35)
        ra, taba = _statica(ya, xa, "r3")
        rb, tabb = _statica(yb, xb, "ind")
        (acf_a, pacf_a), (acf_b, pacf_b) = _acf_pacf(ra.resid), _acf_pacf(rb.resid)
        return SimpleNamespace(ra=ra, rb=rb, taba=taba, tabb=tabb, acf_a=acf_a, pacf_a=pacf_a,
                               acf_b=acf_b, pacf_b=pacf_b)

    banda = _banda(n)

    def accetta(s):
        """Accept a draw whose correlograms are unambiguous and whose spurious fit looks excellent."""
        chiari = all(abs(abs(r) - banda) > 0.03 for r in (*s.acf_a, *s.acf_b))
        fuori_a = int(np.sum(np.abs(s.acf_a) > banda))
        return (chiari and 1 <= fuori_a <= 4 and np.all(np.abs(s.acf_b) > banda)
                and s.rb.rsquared > 0.6 and abs(s.rb.tvalues[1]) > 6)

    s = _campiona(rng, genera, accetta)
    # The student reads the bars off the figure, to about two decimals.
    visto_a, visto_b = np.round(s.acf_a, 2), np.round(s.acf_b, 2)

    def answers(acf_a, acf_b):
        """Return every answer from the ACF values read off the figure."""
        fuori_a, fuori_b = int(np.sum(np.abs(acf_a) > banda)), int(np.sum(np.abs(acf_b) > banda))
        staz_a, staz_b = fuori_a <= 6, fuori_b <= 6
        return {"fuori_a": Numero(fuori_a, 0), "fuori_b": Numero(fuori_b, 0),
                "staz_a": "sì" if staz_a else "no", "staz_b": "sì" if staz_b else "no",
                "coint_b": "sì" if staz_b else "no", "banda": Numero(banda, 3)}

    def studente(_tabelle):
        """Rebuild the answers from the rounded bars of the two ACF panels."""
        return answers(visto_a, visto_b)

    def figura(path):
        """Draw the two long-run residual series: one hovers around zero, the other wanders."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.5))
        t = np.arange(1, n + 1)
        a1.plot(t, s.ra.resid, color=es.BLUE, lw=1.3)
        a1.set_title("coppia A")
        a2.plot(t, s.rb.resid, color=es.RED, lw=1.3)
        a2.set_title("coppia B")
        for ax in (a1, a2):
            ax.axhline(0, color=es.GRAY, lw=0.8)
            ax.set_xlabel("tempo")
            es.commas(ax)
        a1.set_ylabel("residuo di lungo periodo")
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    def figura_testo(path):
        """Draw the ACF and PACF of the long-run residuals of both pairs, as in the exam figure."""
        _correlogramma(path, [("coppia A", s.acf_a, s.pacf_a), ("coppia B", s.acf_b, s.pacf_b)], n)

    truth = answers(s.acf_a, s.acf_b)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"a": s.taba, "b": s.tabb},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("fuori_a"), "b": Quesito("staz_a"), "c": Quesito("staz_b"),
                 "d": Quesito("coint_b")},
        attese=[lambda r: r["staz_a"] == "sì", lambda r: r["staz_b"] == "no",
                lambda r: r["fuori_b"].valore == 12],
        margini=[], figure={"correlogrammi": figura_testo, "residui": figura})


@exercise("e07_06", modulo=7, livello=2, tipo="ecm-rispecificazione-da-residui")
def importazioni_residui(rng):
    """Read the correlogram of the residuals of an ECM and decide which dynamics to re-specify."""
    lam_vero, rho_vero = -0.30, 0.55

    def genera(g):
        """Draw a cointegrated pair with omitted short-run dynamics and estimate the simple ECM."""
        x = _passeggiata(g, 150, 300.0, 1.0, 3.0)
        e = g.normal(0.0, 1.0, 250)
        z = np.zeros(250)
        for t in range(2, 250):
            z[t] = (1 + lam_vero + rho_vero) * z[t - 1] - rho_vero * z[t - 2] + e[t]
        y = 20.0 + 0.8 * x + z[100:]
        lungo, res, tab = _ecm(y, x, "pil")
        a, p = _acf_pacf(res.resid)
        return SimpleNamespace(res=res, tab=tab, acf=a, pacf=p, p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw whose autocorrelation peaks at lag 1 and dies out by lag 5, with a clear adjustment."""
        banda = _banda(int(s.res.nobs))
        picchi = (abs(s.acf[0]) == np.max(np.abs(s.acf)) and abs(s.pacf[0]) == np.max(np.abs(s.pacf)))
        coda = np.all(np.abs(s.acf[4:]) < banda) and np.all(np.abs(s.pacf[4:]) < banda)
        return (abs(abs(s.acf[0]) - banda) > 0.04 and s.acf[0] > banda
                and abs(s.pacf[0]) > 1.5 * banda and picchi and coda
                and s.res.tvalues[2] < -3.0 and 0.0001 <= s.p < 0.02)

    s = _campiona(rng, genera, accetta)
    n = int(s.res.nobs)
    visto = round(float(s.acf[0]), 2)

    def answers(rho1, lam, t_lam, p, n_obs):
        """Return every answer from the visible first autocorrelation, the ECM row and the p-value."""
        banda = _banda(n_obs)
        aut = abs(rho1) > banda
        lungo_ok = p < ALFA and t_lam < -Z and lam < 0
        return {"aut1": "sì" if aut else "no", "breve": "sì" if aut else "no",
                "lungo": "no" if lungo_ok else "sì",
                "dec_lam": "rifiuta" if abs(t_lam) > Z else "non rifiuta",
                "banda": Numero(banda, 3), "lam": Numero(lam, 4), "t_lam": Numero(t_lam, 2),
                "rho1": Numero(rho1, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``ecm_1`` and the bar of the first ACF lag."""
        r = tabelle["ecm"].rows["ecm_1"]
        return answers(visto, r["coef"], r["t"], s.p, int(tabelle["ecm"].stats["n"]))

    def figura_testo(path):
        """Draw the ACF and PACF of the ECM residuals, as in the exam figure."""
        _correlogramma(path, [("residui dell'ECM", s.acf, s.pacf)], n)

    def figura(path):
        """Draw each ECM residual against the previous one, with the fitted slope."""
        es, plt = _stile()
        u = s.res.resid
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.plot(u[:-1], u[1:], "o", color=es.GRAY, ms=3, alpha=0.6)
        g = np.linspace(u.min(), u.max(), 20)
        pend = float(s.acf[0])
        ax.plot(g, pend * g, color=es.RED, lw=1.6,
                label=f"pendenza {pend:.2f}".replace(".", ","))
        ax.set_xlabel(r"residuo $\hat\epsilon_{t-1}$")
        ax.set_ylabel(r"residuo $\hat\epsilon_t$")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    truth = answers(visto, float(s.res.params[2]), float(s.res.tvalues[2]), s.p, n)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "p_eg": Numero(s.p, 4)},
        tabelle={"ecm": s.tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_lam"), "b": Quesito("aut1"), "c": Quesito("breve"),
                 "d": Quesito("lungo")},
        attese=[lambda r: r["breve"] == "sì", lambda r: r["lungo"] == "no",
                lambda r: r["dec_lam"] == "rifiuta", _p_lontano(s.p)],
        margini=[Margin(stat=s.res.tvalues[2], crit=Z), Margin(stat=s.p, crit=ALFA, rel=0.6)],
        figure={"correlogramma": figura_testo, "ritardo": figura})


@exercise("e07_07", modulo=7, livello=2,
          tipo=("inferenza-coefficiente-lungo-periodo", "superconsistenza-e-dols"))
def benzina_petrolio_dols(rng):
    """Check a claim on the long-run coefficient with DOLS and HAC, scaling it to a given increase."""
    n, delta, ell, banda = 160, 10.0, 2, 6

    def genera(g):
        """Draw a cointegrated pump-price and crude-price pair, run the tests and fit the DOLS."""
        x, y = _coppia(g, n, a=55.0, b=1.2, phi=0.7, su=2.0, x0=60.0, drift=0.15, sx=2.5)
        res = _dols(y, x, ell, banda)
        riv = float(round(delta * res.params[1]))
        return SimpleNamespace(x=x, y=y, res=res, riv=riv, p_y=_adf_p(y), p_x=_adf_p(x),
                               p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw with unit roots clearly kept, cointegration clearly accepted and a claim in the interval."""
        t_riv = (delta * s.res.params[1] - s.riv) / (delta * s.res.bse[1])
        return (s.p_y > 0.10 and s.p_x > 0.10 and 0.0001 <= s.p < 0.02 and abs(t_riv) < 1.6
                and abs(s.res.params[1] - s.riv) > 3 * Z * s.res.bse[1])

    s = _campiona(rng, genera, accetta)

    def answers(b, se, p_y, p_x, p):
        """Return every answer from the printed ``petr`` row and the three printed p-values."""
        lo, hi = delta * (b - Z * se), delta * (b + Z * se)
        return {"coint": "sì" if p_y > ALFA and p_x > ALFA and p < ALFA else "no",
                "stima": Numero(delta * b, 2), "ic_lo": Numero(lo, 2), "ic_hi": Numero(hi, 2),
                "compat": "sì" if lo <= s.riv <= hi else "no", "b": Numero(b, 4),
                "se": Numero(se, 4), "beta_riv": Numero(s.riv / delta, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``petr``."""
        r = tabelle["dols"].rows["petr"]
        return answers(r["coef"], r["se"], s.p_y, s.p_x, s.p)

    def figura(path):
        """Draw the 95% interval for the effect of the increase, with the claim and the wrong target."""
        es, plt = _stile()
        b, se = s.res.params[1], s.res.bse[1]
        fig, ax = plt.subplots(figsize=(6.1, 2.4))
        _intervalli(ax, es, [(0, delta * b, delta * se, r"$\Delta\cdot\hat\beta$ con intervallo al 95%", es.BLUE)],
                    "variazione attesa della benzina (centesimi al litro)", riferimento=s.riv,
                    etichetta="affermazione")
        es.save(fig, path)

    b, se = float(s.res.params[1]), float(s.res.bse[1])
    truth = answers(b, se, s.p_y, s.p_x, s.p)
    return Draft(
        dati=None,
        parametri={"n": Numero(int(s.res.nobs), 0), "delta": Numero(delta, 0),
                   "riv": Numero(s.riv, 0), "p_y": Numero(s.p_y, 4), "p_x": Numero(s.p_x, 4),
                   "p_eg": Numero(s.p, 4), "ell": Numero(ell, 0), "banda": Numero(banda, 0)},
        tabelle={"dols": ols_table(s.res, labels=["const", "petr"], stats=("n", "r2"))},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("coint"), "b": Quesito("stima"), "c": Quesito("ic_lo"),
                 "d": Quesito("ic_hi"), "e": Quesito("compat")},
        attese=[lambda r: r["coint"] == "sì", lambda r: r["compat"] == "sì",
                lambda r: abs(s.riv - b) > Z * se, lambda r: _dols_coerente(s.y, s.x, ell, banda, s.res),
                _p_lontano(s.p)],
        margini=[Margin(stat=s.p, crit=ALFA, rel=0.6), Margin(stat=s.p_y, crit=ALFA, rel=1.0),
                 Margin(stat=s.p_x, crit=ALFA, rel=1.0)],
        figure={"intervallo": figura})


def _ar1_righe(g, righe, n, phi, sd):
    """Draw ``righe`` independent stationary AR(1) paths of length ``n`` at once."""
    e = g.normal(0.0, sd, (righe, n))
    u = np.empty((righe, n))
    u[:, 0] = e[:, 0] / np.sqrt(1.0 - phi**2)
    for t in range(1, n):
        u[:, t] = phi * u[:, t - 1] + e[:, t]
    return u


def _pendenze(x, y):
    """Return the OLS slope of every row of ``y`` on the same row of ``x``."""
    xc, yc = x - x.mean(axis=1, keepdims=True), y - y.mean(axis=1, keepdims=True)
    return (xc * yc).sum(axis=1) / (xc**2).sum(axis=1)


@exercise("e07_08", modulo=7, livello=2, tipo="superconsistenza-e-dols")
def superconsistenza_simulata(rng):
    """Read a simulation that shows superconsistency of OLS and the failure of the usual t ratio."""
    simulazioni, durate, durata_cop, beta, banda, ell = 1000, (50, 100, 200), 200, 1.5, 8, 2
    deriva, phi_a, phi_b = 0.1, 0.7, 0.5

    sd_a, sd_b = {}, {}
    for T in durate:
        x = np.cumsum(rng.normal(deriva, 1.0, (simulazioni, T)), axis=1)
        y = 2.0 + beta * x + _ar1_righe(rng, simulazioni, T, phi_a, 1.0)
        sd_a[T] = float(np.std(_pendenze(x, y)))
        xs = _ar1_righe(rng, simulazioni, T, phi_b, 1.0)
        ys = 2.0 + beta * xs + rng.normal(0.0, 1.0, (simulazioni, T))
        sd_b[T] = float(np.std(_pendenze(xs, ys)))

    dentro_ols = dentro_dols = 0
    for _ in range(simulazioni):
        x = np.cumsum(rng.normal(deriva, 1.0, durata_cop))
        y = 2.0 + beta * x + _ar1(rng, durata_cop, phi_a, 1.0)
        usuale = sm.OLS(y, sm.add_constant(x)).fit()
        dentro_ols += abs(usuale.params[1] - beta) <= Z * usuale.bse[1]
        dols = _dols(y, x, ell, banda)
        dentro_dols += abs(dols.params[1] - beta) <= Z * dols.bse[1]
    cop_ols, cop_dols = 100.0 * dentro_ols / simulazioni, 100.0 * dentro_dols / simulazioni

    # The student works from the figures printed in the tables, not from the unrounded simulation.
    vis_a = {T: round(v, 4) for T, v in sd_a.items()}
    vis_b = {T: round(v, 4) for T, v in sd_b.items()}
    vis_cop = (round(cop_ols, 1), round(cop_dols, 1))
    tab_sd = _tabella(["$T$", "caso A: serie cointegrate", "caso B: serie stazionarie"],
                      [[str(T), _num(vis_a[T], 4), _num(vis_b[T], 4)] for T in durate])
    tab_cop = _tabella(["stimatore e errore standard", "copertura dell'intervallo al 95\\%"],
                       [["OLS statica, errore standard usuale", _num(vis_cop[0], 1) + "\\%"],
                        ["DOLS, errore standard HAC", _num(vis_cop[1], 1) + "\\%"]])

    def answers(sd_a_, sd_b_, cop):
        """Return every answer from the printed standard deviations and coverages."""
        ra, rb = sd_a_[200] / sd_a_[100], sd_b_[200] / sd_b_[100]
        return {"rapp_a": Numero(ra, 2), "rapp_b": Numero(rb, 2),
                "piu_veloce": "sì" if ra < rb else "no", "manca": Numero(95.0 - cop[0], 1),
                "affidabile": "sì" if abs(cop[0] - 95.0) <= 3.0 else "no",
                "dols_meglio": "sì" if abs(cop[1] - 95.0) < abs(cop[0] - 95.0) else "no",
                "manca_dols": Numero(95.0 - cop[1], 1), "cop_ols": Numero(cop[0], 1),
                "cop_dols": Numero(cop[1], 1), "a100": Numero(sd_a_[100], 4),
                "a200": Numero(sd_a_[200], 4), "b100": Numero(sd_b_[100], 4),
                "b200": Numero(sd_b_[200], 4)}

    def studente(_tabelle):
        """Rebuild the answers from the rounded figures of the two tables."""
        return answers(vis_a, vis_b, vis_cop)

    def pendenze_attese(_risposte):
        """Check that the standard deviation scales like 1/T for cointegrated and 1/sqrt(T) for stationary data."""
        lt = np.log(durate)
        pa = np.polyfit(lt, np.log([sd_a[T] for T in durate]), 1)[0]
        pb = np.polyfit(lt, np.log([sd_b[T] for T in durate]), 1)[0]
        return -1.25 < pa < -0.8 and -0.65 < pb < -0.35

    def figura(path):
        """Draw the standard deviations against T on log scales, and the two coverages."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.8), gridspec_kw={"width_ratios": [1.3, 1]})
        t = np.array(durate, dtype=float)
        a1.loglog(t, [sd_a[T] for T in durate], "o-", color=es.BLUE, label="A: cointegrate")
        a1.loglog(t, [sd_b[T] for T in durate], "s-", color=es.RED, label="B: stazionarie")
        a1.set_xticks(durate, [str(T) for T in durate])
        a1.minorticks_off()
        a1.set_yticks([0.04, 0.06, 0.1, 0.16], ["0,04", "0,06", "0,1", "0,16"])
        a1.set_xlabel("$T$")
        a1.set_ylabel(r"deviazione standard di $\hat\beta$")
        a1.legend(loc="lower left")
        a2.bar([0, 1], [cop_ols, cop_dols], color=[es.RED, es.BLUE], width=0.55)
        a2.axhline(95.0, color=es.GRAY, ls="--", lw=1.0)
        a2.set_xticks([0, 1], ["OLS", "DOLS-HAC"])
        a2.set_ylim(0, 105)
        a2.set_ylabel("copertura simulata (%)")
        for ax in (a1, a2):
            ax.grid(axis="x", visible=False)
        fig.subplots_adjust(wspace=0.4)
        es.save(fig, path)

    truth = answers(sd_a, sd_b, (cop_ols, cop_dols))
    return Draft(
        dati=None,
        parametri={"sim": Numero(simulazioni, 0), "beta": Numero(beta, 1),
                   "durata_cop": Numero(durata_cop, 0), "tolleranza": Numero(3, 0),
                   "deriva": Numero(deriva, 1), "phi_a": Numero(phi_a, 1), "phi_b": Numero(phi_b, 1),
                   "ell": Numero(ell, 0), "banda": Numero(banda, 0)},
        tabelle={"sd": tab_sd, "cop": tab_cop}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("rapp_a"), "b": Quesito("rapp_b"), "c": Quesito("piu_veloce"),
                 "d": Quesito("manca"), "e": Quesito("affidabile"), "f": Quesito("dols_meglio")},
        attese=[lambda r: r["piu_veloce"] == "sì", lambda r: r["affidabile"] == "no",
                lambda r: r["dols_meglio"] == "sì", pendenze_attese,
                lambda r: 0.40 < r["rapp_a"].valore < 0.62 and 0.62 < r["rapp_b"].valore < 0.82],
        margini=[Margin(stat=cop_ols - 95.0, crit=3.0), Margin(stat=cop_dols - 95.0, crit=3.0)],
        figure={"simulazione": figura})


@exercise("e07_09", modulo=7, livello=3, punti=4,
          tipo=("cointegrazione-decisione", "inferenza-coefficiente-lungo-periodo",
                "superconsistenza-e-dols"))
def indici_borsa_dols(rng):
    """Test a claim on the long-run coefficient: the usual OLS error rejects it, DOLS with HAC does not."""
    n, ell, banda = 200, 2, 8

    def genera(g):
        """Draw a cointegrated pair of indices with persistent deviations and fit the static OLS and the DOLS."""
        x, y = _coppia(g, n, a=-300.0, b=1.3, phi=0.8, su=20.0, x0=1000.0, drift=2.0, sx=25.0)
        ols = sm.OLS(y, sm.add_constant(x)).fit()
        dols = _dols(y, x, ell, banda)
        b0 = round(float(dols.params[1] - dols.bse[1]), 2)
        return SimpleNamespace(x=x, y=y, ols=ols, dols=dols, b0=b0, p_y=_adf_p(y), p_x=_adf_p(x),
                               p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw where the two inferences disagree clearly and the cointegration tests are clear."""
        t_d = (s.dols.params[1] - s.b0) / s.dols.bse[1]
        t_o = (s.ols.params[1] - s.b0) / s.ols.bse[1]
        return (s.p_y > 0.10 and s.p_x > 0.10 and 0.0001 <= s.p < 0.02 and 0.3 < abs(t_d) < 1.6
                and abs(t_o) > 2.4)

    s = _campiona(rng, genera, accetta)

    def answers(b_o, se_o, b_d, se_d, p_y, p_x, p):
        """Return every answer from the printed rows of ``dax`` and the three printed p-values."""
        t_o, t_d = (b_o - s.b0) / se_o, (b_d - s.b0) / se_d
        return {"coint": "sì" if p_y > ALFA and p_x > ALFA and p < ALFA else "no",
                "dec_ols": "rifiuta" if abs(t_o) > Z else "non rifiuta",
                "t_dols": Numero(t_d, 2), "compat": "sì" if abs(t_d) < Z else "no",
                "t_ols": Numero(t_o, 2), "b_ols": Numero(b_o, 5), "b_dols": Numero(b_d, 5),
                "se_dols": Numero(se_d, 6), "se_ols": Numero(se_o, 6),
                "rapporto": Numero(se_d / se_o, 1)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of ``dax`` in the two tables."""
        o, d = tabelle["ols"].rows["dax"], tabelle["dols"].rows["dax"]
        return answers(o["coef"], o["se"], d["coef"], d["se"], s.p_y, s.p_x, s.p)

    def figura(path):
        """Draw the two 95% intervals for beta against the claim: only the DOLS one contains it."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.4))
        _intervalli(ax, es, [(1, s.ols.params[1], s.ols.bse[1], "OLS statica, errore usuale", es.RED),
                             (0, s.dols.params[1], s.dols.bse[1], "DOLS, errore HAC", es.BLUE)],
                    r"coefficiente $\beta$ di lungo periodo", riferimento=s.b0, etichetta="affermazione")
        es.save(fig, path)

    truth = answers(float(s.ols.params[1]), float(s.ols.bse[1]), float(s.dols.params[1]),
                    float(s.dols.bse[1]), s.p_y, s.p_x, s.p)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "b0": Numero(s.b0, 2), "p_y": Numero(s.p_y, 4),
                   "p_x": Numero(s.p_x, 4), "p_eg": Numero(s.p, 4), "ell": Numero(ell, 0),
                   "banda": Numero(banda, 0)},
        tabelle={"ols": ols_table(s.ols, labels=["const", "dax"]),
                 "dols": ols_table(s.dols, labels=["const", "dax"], stats=("n", "r2"))},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("coint"), "b": Quesito("dec_ols"), "c": Quesito("t_dols"),
                 "d": Quesito("compat")},
        attese=[lambda r: r["coint"] == "sì", lambda r: r["dec_ols"] == "rifiuta",
                lambda r: r["compat"] == "sì", _p_lontano(s.p),
                lambda r: _dols_coerente(s.y, s.x, ell, banda, s.dols)],
        margini=[Margin(stat=truth["t_dols"].valore, crit=Z), Margin(stat=truth["t_ols"].valore, crit=Z),
                 Margin(stat=s.p, crit=ALFA, rel=0.6), Margin(stat=s.p_y, crit=ALFA, rel=1.0),
                 Margin(stat=s.p_x, crit=ALFA, rel=1.0)],
        figure={"confronto": figura})


@exercise("e07_10", modulo=7, livello=3, punti=4,
          tipo=("regressione-statica-ben-definita", "cointegrazione-decisione"))
def margine_benzina_petrolio(rng):
    """Tell apart a spurious Engle-Granger success (stationary dependent) from a genuine cointegration."""
    n = 140

    def genera(g):
        """Draw a crude price, an unrelated stationary margin and a pump price cointegrated with the crude."""
        x = _passeggiata(g, n, 60.0, 0.1, 2.0)
        y1 = 12.0 + _ar1(g, n, 0.75, 1.0)
        y2 = 55.0 + 1.2 * x + _ar1(g, n, 0.7, 2.0)
        return SimpleNamespace(t_m=_adf(y1, "margine")[1], t_p=_adf(x, "petr")[1],
                               t_b=_adf(y2, "benz")[1], p1=_eg_p(y1, x), p2=_eg_p(y2, x))

    def accetta(s):
        """Accept a draw with clear unit-root verdicts and both Engle-Granger p-values clearly below 5%."""
        return (s.t_m < DF_C and s.t_p > DF_C and s.t_b > DF_C
                and all(_lontano(t, DF_C) for t in (s.t_m, s.t_p, s.t_b))
                and all(0.0001 <= p < 0.02 for p in (s.p1, s.p2)))

    s = _campiona(rng, genera, accetta)
    # The student reads the statistics printed in the tables, rounded to two decimals.
    vis = [round(t, 2) for t in (s.t_m, s.t_p, s.t_b)]
    tab_adf = _tabella(["serie", "statistica $t$ del test ADF"],
                       [["margine", _num(vis[0], 2)], ["petr", _num(vis[1], 2)], ["benz", _num(vis[2], 2)]])
    tab_eg = _tabella(["relazione (dipendente su regressore)", "p-value di Engle-Granger"],
                      [["margine su petr", _num(s.p1, 4)], ["benz su petr", _num(s.p2, 4)]])

    def answers(t_m, t_p, t_b, p1, p2):
        """Return every answer from the three printed statistics and the two printed p-values."""
        dec_m, dec_p, dec_b = _df(t_m), _df(t_p), _df(t_b)
        coint_a = dec_m == dec_p == "non rifiuta" and p1 < ALFA
        coint_b = dec_b == dec_p == "non rifiuta" and p2 < ALFA
        bene_a = (dec_m == dec_p == "rifiuta") or coint_a
        bene_b = (dec_b == dec_p == "rifiuta") or coint_b
        return {"dec_m": dec_m, "coint_a": "sì" if coint_a else "no", "coint_b": "sì" if coint_b else "no",
                "ben_a": "sì" if bene_a else "no", "ben_b": "sì" if bene_b else "no",
                "t_m": Numero(t_m, 2), "t_p": Numero(t_p, 2), "t_b": Numero(t_b, 2),
                "p1": Numero(p1, 4), "p2": Numero(p2, 4)}

    def studente(_tabelle):
        """Rebuild the answers from the rounded statistics and p-values of the two tables."""
        return answers(*vis, s.p1, s.p2)

    def figura(path):
        """Draw the three Dickey-Fuller statistics and the two Engle-Granger p-values against their thresholds."""
        _figura_test(path, ["margine", "petr", "benz"], vis, DF_C, ["margine su petr", "benz su petr"],
                     [s.p1, s.p2])

    truth = answers(*vis, s.p1, s.p2)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "cv": Numero(DF_C, 2)},
        tabelle={"adf": tab_adf, "eg": tab_eg}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_m"), "b": Quesito("coint_a"), "c": Quesito("coint_b"),
                 "d": Quesito("ben_a"), "e": Quesito("ben_b")},
        attese=[lambda r: r["coint_a"] == "no", lambda r: r["coint_b"] == "sì",
                lambda r: r["ben_a"] == "no", lambda r: r["ben_b"] == "sì",
                _p_lontano(s.p1), _p_lontano(s.p2)],
        margini=[Margin(stat=t, crit=DF_C) for t in vis]
        + [Margin(stat=p, crit=ALFA, rel=0.6) for p in (s.p1, s.p2)],
        figure={"test": figura})


@exercise("e07_11", modulo=7, livello=3, punti=4,
          tipo=("ecm-direzione-aggiustamento", "ecm-ben-definito"))
def investimenti_pil_scenario(rng):
    """Forecast growth after a positive disequilibrium: slower than in equilibrium, yet still positive."""
    d, g_x = 3.0, 1.0

    def genera(g):
        """Draw a cointegrated investment-output pair and estimate its error-correction model."""
        x, y = _coppia(g, 140, a=-200.0, b=1.4, phi=0.75, su=1.2, x0=450.0, drift=0.7, sx=1.0)
        lungo, res, tab = _ecm(y, x, "pil")
        return SimpleNamespace(res=res, tab=tab, p_y=_adf_p(y), p_x=_adf_p(x), p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw with a clear adjustment, an insignificant constant and a positive growth forecast."""
        c, gam, lam = s.res.params
        prev = gam * g_x + lam * d
        return (s.res.tvalues[2] < -3.0 and abs(s.res.tvalues[0]) < 1.6 and s.p_y > 0.10
                and s.p_x > 0.10 and 0.0001 <= s.p < 0.02 and 0.25 < prev < gam * g_x - 0.25)

    s = _campiona(rng, genera, accetta)

    def answers(gam, lam, t_lam, p_y, p_x, p):
        """Return every answer from the printed rows of ``d_pil`` and ``ecm_1`` and the three p-values."""
        buono = p_y > ALFA and p_x > ALFA and p < ALFA and lam < 0 and t_lam < -Z
        crescita = gam * g_x + lam * d
        return {"ben_def": "sì" if buono else "no", "crescita": Numero(crescita, 3),
                "effetto": Numero(lam * d, 3), "minore": "sì" if lam * d < 0 else "no",
                "negativa": "sì" if crescita < 0 else "no", "equilibrio": Numero(gam * g_x, 3),
                "gam": Numero(gam, 4), "lam": Numero(lam, 4), "t_lam": Numero(t_lam, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of ``d_pil`` and ``ecm_1``."""
        rows = tabelle["ecm"].rows
        return answers(rows["d_pil"]["coef"], rows["ecm_1"]["coef"], rows["ecm_1"]["t"], s.p_y, s.p_x, s.p)

    def previsione_coerente(r):
        """Check with the fitted equation that the forecast differs from the printed one only by the constant."""
        c = s.res.params[0]
        completa = s.res.predict(np.array([[1.0, g_x, d]]))[0]
        return abs(completa - c - r["crescita"].valore) < 1e-3

    def figura(path):
        """Draw the expected growth against the disequilibrium: positive at the scenario but below the equilibrium line."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        gam, lam = s.res.params[1], s.res.params[2]
        e = np.linspace(-1.0, 8.0, 50)
        ax.plot(e, gam * g_x + lam * e, color=es.BLUE, lw=1.6, label=r"$\hat\gamma_1\,\Delta x+\hat\lambda\,\mathrm{ecm}_t$")
        ax.axhline(gam * g_x, color=es.GRAY, ls="--", lw=1.0, label="crescita in equilibrio")
        ax.axhline(0, color=es.GRAY, lw=0.8)
        ax.plot([d], [gam * g_x + lam * d], "o", color=es.RED, ms=7, zorder=5)
        ax.annotate(f"{gam * g_x + lam * d:.3f}".replace(".", ","), xy=(d, gam * g_x + lam * d),
                    xytext=(8, 8), textcoords="offset points", fontsize=8.5, color=es.RED, fontweight="bold")
        ax.set_xlabel(r"disequilibrio $\mathrm{ecm}_t$")
        ax.set_ylabel(r"variazione attesa di inv in $t+1$")
        es.commas(ax)
        ax.legend(loc="lower left")
        es.save(fig, path)

    truth = answers(float(s.res.params[1]), float(s.res.params[2]), float(s.res.tvalues[2]),
                    s.p_y, s.p_x, s.p)
    return Draft(
        dati=None,
        parametri={"n": Numero(int(s.res.nobs), 0), "d": Numero(d, 1), "g": Numero(g_x, 1),
                   "p_y": Numero(s.p_y, 4), "p_x": Numero(s.p_x, 4), "p_eg": Numero(s.p, 4)},
        tabelle={"ecm": s.tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("ben_def"), "b": Quesito("crescita"), "c": Quesito("effetto"),
                 "d": Quesito("minore"), "e": Quesito("negativa")},
        attese=[lambda r: r["ben_def"] == "sì", lambda r: r["crescita"].valore > 0,
                lambda r: r["minore"] == "sì", lambda r: r["negativa"] == "no", previsione_coerente,
                _p_lontano(s.p)],
        margini=[Margin(stat=s.res.tvalues[2], crit=Z), Margin(stat=s.p, crit=ALFA, rel=0.6),
                 Margin(stat=s.p_y, crit=ALFA, rel=1.0), Margin(stat=s.p_x, crit=ALFA, rel=1.0)],
        figure={"scenario": figura})


@exercise("e07_12", modulo=7, livello=3, punti=4,
          tipo=("ecm-ben-definito", "ecm-rispecificazione-da-residui", "ecm-velocita-assorbimento",
                "cointegrazione-decisione"))
def vendite_reddito_ecm(rng):
    """Judge an error-correction model end to end: cointegration, specification, residuals and speed."""
    q = 0.75

    def genera(g):
        """Draw a trending cointegrated pair, run the tests with trend and estimate the ECM."""
        x, y = _coppia(g, 160, a=20.0, b=0.7, phi=0.8, su=1.0, x0=100.0, drift=0.8, sx=2.0)
        lungo, res, tab = _ecm(y, x, "red")
        a, p = _acf_pacf(res.resid)
        return SimpleNamespace(lungo=lungo, res=res, tab=tab, acf=a, pacf=p,
                               t_x=_adf(x, "red", trend=True)[1],
                               t_y=_adf(y, "vend", trend=True)[1], p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw with clear verdicts, a clear adjustment, a white-noise correlogram and a clear horizon."""
        banda = _banda(int(s.res.nobs))
        bianco = np.all(np.abs(s.acf) < 0.85 * banda) and np.all(np.abs(s.pacf) < 0.85 * banda)
        lam = s.res.params[2]
        if not (0.60 < 1 + lam < 0.90):
            return False
        k = _periodi(lam, q)
        orizzonte_chiaro = all(_lontano((1 + lam) ** j, 1 - q, 0.04) for j in (k - 1, k))
        return (s.t_x > DF_T and s.t_y > DF_T and _lontano(s.t_x, DF_T) and _lontano(s.t_y, DF_T)
                and 0.0001 <= s.p < 0.02 and s.res.tvalues[2] < -3.0 and bianco and orizzonte_chiaro)

    s = _campiona(rng, genera, accetta)
    n = int(s.res.nobs)
    vis = (round(s.t_y, 2), round(s.t_x, 2))
    tab_adf = _tabella(["serie", "statistica $t$ del test ADF con costante e trend"],
                       [["vend", _num(vis[0], 2)], ["red", _num(vis[1], 2)]])
    # The correlogram is only a figure, so the count of bars outside the bands is what the student reads.
    fuori = int(np.sum(np.abs(s.acf) > _banda(n)) + np.sum(np.abs(s.pacf) > _banda(n)))

    def answers(t_y, t_x, p, lam, t_lam, n_fuori):
        """Return every answer from the two printed statistics, the p-value and the ECM row."""
        non_staz = t_y > DF_T and t_x > DF_T
        coint_ok = non_staz and p < ALFA
        ben = coint_ok and lam < 0 and t_lam < -Z
        k = _periodi(lam, q) if -1 < lam < 0 else 0
        phi = 1.0 + lam
        return {"coint": "sì" if coint_ok else "no", "ben_def": "sì" if ben else "no",
                "breve": "sì" if n_fuori > 0 else "no", "k": Numero(k, 0),
                "lam": Numero(lam, 4), "t_lam": Numero(t_lam, 2), "phi": Numero(phi, 4),
                "t_y": Numero(t_y, 2), "t_x": Numero(t_x, 2), "resto": Numero(phi**k, 4), "resto_prima": Numero(phi ** (k - 1), 4),
                "assorbito": Numero(100 * (1 - phi**k), 1), "obiettivo": Numero(1 - q, 2),
                "km": Numero(k - 1, 0),
                "log": Numero(np.log(1 - q) / np.log(phi) if phi > 0 else 0.0, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed statistics, the p-value and the row of ``ecm_1``."""
        r = tabelle["ecm"].rows["ecm_1"]
        return answers(vis[0], vis[1], s.p, r["coef"], r["t"], fuori)

    def figura_testo(path):
        """Draw the ACF and PACF of the ECM residuals, as in the exam figure."""
        _correlogramma(path, [("residui dell'ECM", s.acf, s.pacf)], n)

    def figura(path):
        """Draw the share of disequilibrium left after each period, with the horizon of the target."""
        es, plt = _stile()
        fig, _, _ = es.decay(float(s.res.params[2]), horizon=int(truth["k"].valore) + 4, targets=(q,))
        es.save(fig, path)

    truth = answers(vis[0], vis[1], s.p, float(s.res.params[2]), float(s.res.tvalues[2]), fuori)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "cv": Numero(DF_T, 2), "p_eg": Numero(s.p, 4),
                   "q": Numero(100 * q, 0)},
        tabelle={"adf": tab_adf, "ecm": s.tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("coint"), "b": Quesito("ben_def"), "c": Quesito("breve"),
                 "d": Quesito("k")},
        attese=[lambda r: r["coint"] == "sì", lambda r: r["ben_def"] == "sì",
                lambda r: r["breve"] == "no", _p_lontano(s.p), lambda r: _k_simulato(s.lungo, s.res, q, 100.0) == r["k"].valore],
        margini=[Margin(stat=t, crit=DF_T) for t in vis]
        + [Margin(stat=s.res.tvalues[2], crit=Z), Margin(stat=s.p, crit=ALFA, rel=0.6)],
        figure={"correlogramma": figura_testo, "assorbimento": figura})


@exercise("e07_13", modulo=7, livello=3, punti=4,
          tipo=("ecm-ben-definito", "cointegrazione-decisione"))
def vendite_pubblicita_ecm_spurio(rng):
    """Show that a significant adjustment coefficient does not make an ECM well defined without cointegration."""
    n = 140

    def genera(g):
        """Draw two independent random walks and estimate the ECM built on their static residual."""
        x = _passeggiata(g, n, 50.0, 0.2, 1.5)
        y = _passeggiata(g, n, 80.0, 0.2, 1.5)
        lungo, res, tab = _ecm(y, x, "pub")
        return SimpleNamespace(res=res, tab=tab, t_x=_adf(x, "pub")[1], t_y=_adf(y, "fatt")[1],
                               p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw where both series keep their unit root, Engle-Granger is clearly negative and the ECM term looks significant."""
        return (s.t_x > DF_C and s.t_y > DF_C and _lontano(s.t_x, DF_C) and _lontano(s.t_y, DF_C)
                and s.p > 0.10 and s.res.tvalues[2] < -2.6)

    s = _campiona(rng, genera, accetta)
    vis = (round(s.t_y, 2), round(s.t_x, 2))
    tab_adf = _tabella(["serie", "statistica $t$ del test ADF"],
                       [["fatt", _num(vis[0], 2)], ["pub", _num(vis[1], 2)]])

    def answers(t_y, t_x, p, lam, t_lam):
        """Return every answer from the two printed statistics, the p-value and the ECM row."""
        non_staz = t_y > DF_C and t_x > DF_C
        coint_ok = non_staz and p < ALFA
        return {"coint": "sì" if coint_ok else "no",
                "dec_lam": "rifiuta" if abs(t_lam) > Z else "non rifiuta",
                "ben_def": "sì" if coint_ok and lam < 0 and t_lam < -Z else "no",
                "lam": Numero(lam, 4), "t_lam": Numero(t_lam, 2), "t_y": Numero(t_y, 2),
                "t_x": Numero(t_x, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed statistics, the p-value and the row of ``ecm_1``."""
        r = tabelle["ecm"].rows["ecm_1"]
        return answers(vis[0], vis[1], s.p, r["coef"], r["t"])

    def figura(path):
        """Draw the t ratio of the adjustment term and the Engle-Granger p-value on opposite sides of their thresholds."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.4))
        t = float(s.res.tvalues[2])
        a1.axvspan(-8, -Z, color=es.REDBG)
        a1.axvline(-Z, color=es.RED, ls="--", lw=1.1)
        a1.plot([t], [0], "o", color=es.BLUE, ms=8, zorder=5)
        a1.annotate("$t=" + f"{t:.2f}".replace(".", "{,}") + "$", xy=(t, 0), xytext=(0, 10),
                    textcoords="offset points", ha="center", fontsize=9, color=es.BLUE)
        a1.set_xlim(-6, 1)
        a1.set_yticks([])
        a1.set_xlabel(r"rapporto $t$ di $\hat\lambda$ (soglia $-1{,}96$)")
        a2.axvspan(0, ALFA, color=es.REDBG)
        a2.axvline(ALFA, color=es.RED, ls="--", lw=1.1)
        a2.plot([s.p], [0], "o", color=es.GREEN, ms=8, zorder=5)
        a2.annotate("$p=" + f"{s.p:.4f}".replace(".", "{,}") + "$", xy=(s.p, 0), xytext=(8, 10),
                    textcoords="offset points", ha="left", fontsize=9, color=es.GREEN)
        a2.set_xlim(0, 1)
        a2.set_yticks([])
        a2.set_xlabel("p-value EG (soglia $0{,}05$)")
        for ax in (a1, a2):
            ax.set_ylim(-0.6, 0.9)
            ax.grid(axis="y", visible=False)
            es.commas(ax, "x")
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    truth = answers(vis[0], vis[1], s.p, float(s.res.params[2]), float(s.res.tvalues[2]))
    return Draft(
        dati=None,
        parametri={"n": Numero(int(s.res.nobs), 0), "n_serie": Numero(n, 0), "cv": Numero(DF_C, 2), "p_eg": Numero(s.p, 4)},
        tabelle={"adf": tab_adf, "ecm": s.tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("coint"), "b": Quesito("dec_lam"), "c": Quesito("ben_def")},
        attese=[lambda r: r["coint"] == "no", lambda r: r["dec_lam"] == "rifiuta",
                lambda r: r["ben_def"] == "no", _p_lontano(s.p)],
        margini=[Margin(stat=t, crit=DF_C) for t in vis]
        + [Margin(stat=s.res.tvalues[2], crit=Z), Margin(stat=s.p, crit=ALFA, rel=0.6)],
        figure={"contrasto": figura})
