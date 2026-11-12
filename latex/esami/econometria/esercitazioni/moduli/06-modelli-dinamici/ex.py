"""Module 06 - dynamic models: AR/MA, correlograms, unit-root tests, spurious regression, breaks."""

from functools import lru_cache

import numpy as np
import statsmodels.api as sm
from scipy import stats
from scipy.signal import lfilter
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import acf, adfuller, pacf

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import fmt_p, fmt_sig, ols_table

TITOLO = "Modelli dinamici"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

# Dickey-Fuller critical values at 5% as the exam texts give them.
DF_C, DF_CT = -2.38, -3.43

# MacKinnon asymptotic 5% values: the margins are also checked against them, so that
# the decision does not depend on which convention a reader applies.
MK_C, MK_CT = -2.86, -3.41

# QLR 5% critical value for two restrictions and 15% trimming (ECON 06, Exelon example).
QLR_CRIT = 5.86
TRIM = 0.15


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _finche(rng, draw, ok, tries=4000):
    """Return the first sample from ``draw(rng)`` that ``ok`` accepts.

    The examples must show a pattern a reader cannot misjudge, as the figures of a
    textbook do. The generator is seeded by the exercise id, so the sample is
    reproducible.

    Raises:
        RuntimeError: If no sample satisfies the conditions.
    """
    for _ in range(tries):
        out = draw(rng)
        if ok(out):
            return out
    raise RuntimeError("nessun campione soddisfa le condizioni dell'esempio")


def _ar(rng, n, phis, const=0.0, sigma=1.0, burn=300):
    """Simulate a stationary AR(p) with intercept ``const`` after ``burn`` warm-up draws."""
    e = rng.normal(0.0, sigma, n + burn) + const
    return lfilter([1.0], np.r_[1.0, -np.asarray(phis, dtype=float)], e)[burn:]


def _i1(rng, n, drift=0.0, dphis=(), sigma=1.0, y0=0.0):
    """Simulate an integrated series whose differences are drift plus an AR(``dphis``)."""
    du = _ar(rng, n, dphis, sigma=sigma) if len(dphis) else rng.normal(0.0, sigma, n)
    return y0 + np.cumsum(drift + du)


def _ma(rng, n, thetas, sigma=1.0):
    """Simulate a zero-mean MA(q) with coefficients ``thetas``."""
    q = len(thetas)
    e = rng.normal(0.0, sigma, n + q)
    out = e[q:].copy()
    for j, th in enumerate(thetas, start=1):
        out += th * e[q - j:n + q - j]
    return out


def _correlogramma(y, k):
    """Return the sample ACF and PACF of ``y`` at lags 1..``k``."""
    return acf(y, nlags=k, fft=False)[1:], pacf(y, nlags=k, method="ywm")[1:]


def _banda(n):
    """Return the half-width of the 5% significance band of a correlogram."""
    return Z / np.sqrt(n)


def _adf(y, lags, nome, trend=False):
    """Fit the augmented Dickey-Fuller regression and return the result and its table.

    The regressors are the constant, the optional trend ``time``, the lagged level
    ``<nome>_1`` and ``lags`` lagged differences, in the order gretl prints them.
    """
    dy = np.diff(y)
    m = len(dy) - lags
    cols, labels = [np.ones(m)], ["const"]
    if trend:
        cols.append(np.arange(1.0, m + 1))
        labels.append("time")
    cols.append(y[lags:-1])
    labels.append(f"{nome}_1")
    for j in range(1, lags + 1):
        cols.append(dy[lags - j:len(dy) - j])
        labels.append(f"d_{nome}_{j}")
    res = sm.OLS(dy[lags:], np.column_stack(cols)).fit()
    return res, ols_table(res, labels=labels, p=False, stats=("n",))


def _t_livello(res, trend=False):
    """Return the t ratio of the lagged level in an ADF fit made by :func:`_adf`."""
    return float(res.tvalues[1 + int(trend)])


def _stampata(t):
    """Return ``t`` rounded to the four significant digits the tables print, so figures match the text."""
    return float(f"{t:.4g}")


def _decide_df(t, crit):
    """Return the one-sided decision of a unit-root test, in the words of the exam."""
    return "rifiuta" if t < crit else "non rifiuta"


def _decide_z(t):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > Z else "non rifiuta"


def _asse_test(ax, es, voci, crit, alt=None):
    """Draw statistics on a number line against the left rejection region of a test.

    Args:
        ax: Axes to draw on.
        es: The ``econstyle`` module.
        voci: ``(label, statistic, colour)`` per series, drawn from the bottom up.
        crit: Critical value; the region to its left is the rejection region.
        alt: Optional wrong critical value (for example the normal one), drawn dashed.
    """
    valori = [v[1] for v in voci] + [crit] + ([alt] if alt is not None else [])
    lo, hi = min(valori) - 1.3, max(valori) + 1.3
    ax.axvspan(lo, crit, color=es.REDBG, zorder=0)
    ax.axvline(crit, color=es.RED, lw=1.3)
    ax.text(crit, -0.55, f"valore critico {crit:.2f} ".replace(".", ","), color=es.RED, ha="right",
            va="bottom", fontsize=8)
    if alt is not None:
        ax.axvline(alt, color=es.GRAY, lw=1.0, ls="--")
        ax.text(alt, -0.55, f" soglia normale {alt:.2f}".replace(".", ","), color=es.GRAY, ha="left",
                va="bottom", fontsize=8)
    for i, (nome, stat, colore) in enumerate(voci):
        ax.plot([stat], [i], "o", color=colore, ms=7, zorder=5)
        a_sinistra = stat < (lo + hi) / 2
        ax.annotate(f"{nome}: " + f"{stat:.2f}".replace(".", ","), xy=(stat, i),
                    xytext=(-6 if not a_sinistra else 6, 9), textcoords="offset points",
                    ha="left" if a_sinistra else "right", fontsize=8.5, color=colore,
                    fontweight="bold")
    ax.set_xlim(lo, hi)
    ax.set_ylim(-0.6, len(voci) - 0.4)
    ax.set_yticks([])
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x")


def _retta_test(path, gruppi):
    """Write one number line per group of statistics sharing a critical value.

    Args:
        path: Output PDF.
        gruppi: ``(voci, crit, alt)`` per row, with ``voci`` as in :func:`_asse_test`.
    """
    es, plt = _stile()
    altezze = [0.8 + 0.5 * len(g[0]) for g in gruppi]
    fig, axs = plt.subplots(len(gruppi), 1, figsize=(6.1, sum(altezze) + 0.5), squeeze=False,
                            gridspec_kw={"height_ratios": altezze, "hspace": 0.55})
    for ax, (voci, crit, alt) in zip(axs[:, 0], gruppi):
        _asse_test(ax, es, voci, crit, alt)
    axs[-1, 0].set_xlabel("statistica del test (rapporto $t$ del livello ritardato)")
    es.save(fig, path)


def _figura_correlogrammi(path, serie, n, k, titoli, altezza=4.2):
    """Draw the ACF (top) and PACF (bottom) of each series in its own column.

    Args:
        path: Output PDF.
        serie: ``(acf, pacf)`` per series, lags 1..``k``.
        n: Observations the 5% band is computed from.
        k: Number of lags shown.
        titoli: Column titles.
        altezza: Figure height in inches.
    """
    es, plt = _stile()
    fig, ax = plt.subplots(2, len(serie), figsize=(6.1, altezza), sharex=True, squeeze=False)
    for j, ((c, p), titolo) in enumerate(zip(serie, titoli)):
        es.acf_pacf(c, p, n=n, axes=(ax[0, j], ax[1, j]))
        ax[0, j].set_title(titolo)
    for a in ax[1]:
        a.set_xticks(np.arange(2, k + 1, 2))
    fig.subplots_adjust(wspace=0.32, hspace=0.12)
    es.save(fig, path)


@exercise("e06_01", modulo=6, livello=1, tipo="proprieta-ar-ma")
def momenti_ar_ma(rng):
    """Compute mean, variance and autocorrelations of an AR(1) and an MA(1) from their parameters."""
    c, phi, s2, theta, k = 3.0, 0.7, 4.0, -0.6, 3

    def answers(c_, f_, v_, th_):
        """Return every answer from the intercept, AR and MA coefficients and the shock variance."""
        return {"media": Numero(c_ / (1 - f_), 2), "var": Numero(v_ / (1 - f_**2), 2),
                "rho_k": Numero(f_**k, 3), "var_ma": Numero((1 + th_**2) * v_, 2),
                "rho1_ma": Numero(th_ / (1 + th_**2), 3), "rw": "no"}

    def studente(_tabelle):
        """Rebuild the answers from the parameters printed in the text."""
        return answers(c, phi, s2, theta)

    def simulazione_coerente(_risposte):
        """Check the closed forms against a long simulation of both processes."""
        g = np.random.default_rng(1)
        m = 400_000
        a = _ar(g, m, [phi], const=c, sigma=np.sqrt(s2))
        b = _ma(g, m, [theta], sigma=np.sqrt(s2))
        ra, rb = acf(a, nlags=k, fft=True), acf(b, nlags=2, fft=True)
        return (abs(a.mean() - c / (1 - phi)) < 0.05
                and abs(a.var() / (s2 / (1 - phi**2)) - 1) < 0.02
                and abs(ra[k] - phi**k) < 0.01
                and abs(b.var() / ((1 + theta**2) * s2) - 1) < 0.01
                and abs(rb[1] - theta / (1 + theta**2)) < 0.01 and abs(rb[2]) < 0.01)

    def varianza_rw_cresce(_risposte):
        """Check by simulation that the variance of a random walk grows linearly with t."""
        g = np.random.default_rng(2)
        w = np.cumsum(g.normal(size=(40_000, 100)), axis=1)
        return abs(w[:, 99].var() / w[:, 24].var() - 4.0) < 0.2

    def figura(path):
        """Draw the theoretical ACF of both processes against a long simulated sample."""
        es, plt = _stile()
        g = np.random.default_rng(3)
        m, lags = 200_000, np.arange(1, 9)
        a = acf(_ar(g, m, [phi], const=c, sigma=np.sqrt(s2)), nlags=8, fft=True)[1:]
        b = acf(_ma(g, m, [theta], sigma=np.sqrt(s2)), nlags=8, fft=True)[1:]
        teorica_a = phi**lags
        teorica_b = np.where(lags == 1, theta / (1 + theta**2), 0.0)
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.6), sharey=True)
        for ax, teo, camp, titolo in ((a1, teorica_a, a, "AR(1)"), (a2, teorica_b, b, "MA(1)")):
            ax.vlines(lags, 0, teo, color=es.BLUE, lw=2.4, label="teorica")
            ax.plot(lags, camp, "o", ms=4.5, color=es.RED, label="campione simulato", zorder=5)
            ax.axhline(0, color=es.GRAY, lw=0.8)
            ax.set_title(titolo)
            ax.set_xlabel("ritardo")
            es.commas(ax)
        a1.set_ylabel("autocorrelazione")
        a1.legend(loc="upper right")
        es.save(fig, path)

    return Draft(
        dati=None,
        parametri={"c": Numero(c, 0), "phi": Numero(phi, 1), "s2": Numero(s2, 0),
                   "theta": Numero(theta, 1), "k": Numero(k, 0)},
        tabelle={}, risposte=answers(c, phi, s2, theta), studente=studente,
        quesiti={"a": Quesito("media"), "b": Quesito("var"), "c": Quesito("rho_k"),
                 "d": Quesito("var_ma"), "e": Quesito("rho1_ma"), "f": Quesito("rw")},
        attese=[lambda r: r["var"].valore > s2, lambda r: r["rho1_ma"].valore < 0,
                simulazione_coerente, varianza_rw_cresce],
        margini=[], figure={"acf": figura})


@exercise("e06_02", modulo=6, livello=1, tipo="stazionarieta-da-correlogramma")
def correlogramma_due_serie(rng):
    """Judge stationarity from the correlogram of an AR(1) and of a random walk."""
    n, k, phi = 150, 12, 0.6
    band = _banda(n)

    def estrai(g):
        """Draw the AR(1) series and the random walk."""
        return _ar(g, n, [phi]), _i1(g, n)

    def netto(serie):
        """Accept samples whose lags are clearly outside or clearly inside the bands."""
        (aa, ap), (ba, bp) = (_correlogramma(s, k) for s in serie)
        return (abs(ap[0]) >= 1.5 * band and abs(aa[0]) >= 1.5 * band
                and np.all(np.abs(ap[1:]) <= 0.6 * band)
                and np.all(np.abs(ba) >= 1.5 * band) and abs(bp[0]) >= 1.5 * band)

    a, b = _finche(rng, estrai, netto)
    acf_a, pacf_a = (np.round(v, 3) for v in _correlogramma(a, k))
    acf_b, pacf_b = (np.round(v, 3) for v in _correlogramma(b, k))

    def answers(ca, pa, cb, pb):
        """Return every answer from the ACF and PACF of A and of B as read on the figure."""
        def stazionaria(c):
            """Call a series stationary when its ACF falls inside the bands within the lags shown."""
            return "sì" if np.any(np.abs(c) <= band) else "no"

        return {"sta_a": stazionaria(ca), "sta_b": stazionaria(cb),
                "n_pacf": Numero(float(np.sum(np.abs(pa) > band)), 0),
                "banda": Numero(band, 3), "acf1_a": Numero(ca[0], 3), "pacf1_a": Numero(pa[0], 3),
                "rientro": Numero(float(np.argmax(np.abs(ca) <= band) + 1), 0),
                "acf_b_min": Numero(np.abs(cb).min(), 3), "pacf1_b": Numero(pb[0], 3)}

    def studente(_tabelle):
        """Rebuild the answers from the correlograms as read on the figure."""
        return answers(acf_a, pacf_a, acf_b, pacf_b)

    def figura_dati(path):
        """Draw the ACF and PACF of both series with the 5% bands."""
        _figura_correlogrammi(path, [(acf_a, pacf_a), (acf_b, pacf_b)], n, k,
                              ["serie A", "serie B"])

    def figura(path):
        """Draw the two ACFs on the same axes: A dies out, B stays near one."""
        es, plt = _stile()
        lags = np.arange(1, k + 1)
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.axhspan(-band, band, color=es.BLUEBG, zorder=0,
                   label=rf"banda $\pm{band:.3f}$".replace(".", ","))
        ax.plot(lags, acf_a, "o-", color=es.BLUE, ms=4.5, lw=1.4, label="ACF della serie A")
        ax.plot(lags, acf_b, "s-", color=es.RED, ms=4.5, lw=1.4, label="ACF della serie B")
        ax.axhline(0, color=es.GRAY, lw=0.8)
        ax.set_xlabel("ritardo")
        ax.set_ylabel("autocorrelazione")
        es.commas(ax)
        ax.legend(loc="center right")
        es.save(fig, path)

    def schema_nitido(_risposte):
        """Check the margins of the pattern: clear spikes, clear silence, persistent random walk."""
        return (np.all(np.abs(pacf_a[1:]) <= 0.6 * band) and abs(pacf_a[0]) >= 1.5 * band
                and np.all(np.abs(acf_b) >= 1.5 * band) and np.abs(acf_b).min() > 0.5)

    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "k": Numero(k, 0)}, tabelle={},
        risposte=answers(acf_a, pacf_a, acf_b, pacf_b), studente=studente,
        quesiti={"a": Quesito("sta_a"), "b": Quesito("sta_b"), "c": Quesito("n_pacf")},
        attese=[lambda r: r["sta_a"] == "sì", lambda r: r["sta_b"] == "no",
                lambda r: r["n_pacf"].valore == 1, schema_nitido],
        margini=[], figure={"dati": figura_dati, "acf": figura})


@exercise("e06_03", modulo=6, livello=1, tipo="adf-lettura-output-regressione")
def adf_due_serie(rng):
    """Read the lagged-level statistic in two ADF outputs and decide on the unit root."""
    n, lags = 150, 2

    def estrai(g):
        """Draw a random walk and a stationary AR(1)."""
        return _i1(g, n, sigma=1.2, y0=100.0), _ar(g, n, [0.6], const=1.0)

    def netto(serie):
        """Accept samples with a statistic well on each side of the critical value."""
        ta = _t_livello(_adf(serie[0], lags, "cambio")[0])
        tb = _t_livello(_adf(serie[1], lags, "spread")[0])
        return -1.8 < ta < -0.4 and tb < -4.0

    a, b = _finche(rng, estrai, netto)
    ra, tab_a = _adf(a, lags, "cambio")
    rb, tab_b = _adf(b, lags, "spread")
    ta, tb = _t_livello(ra), _t_livello(rb)

    def answers(rowa, rowb):
        """Return every answer from the printed row of the lagged level in the two tables."""
        return {"ta": Numero(rowa["t"], 2), "deca": _decide_df(rowa["t"], DF_C),
                "tb": Numero(rowb["t"], 2), "decb": _decide_df(rowb["t"], DF_C),
                "conta": Numero(float((rowa["t"] < DF_C) + (rowb["t"] < DF_C)), 0),
                "ca": Numero(rowa["coef"], 5), "sa": Numero(rowa["se"], 5),
                "cb": Numero(rowb["coef"], 5), "sb": Numero(rowb["se"], 5)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows ``cambio_1`` and ``spread_1``."""
        return answers(tabelle["a"].rows["cambio_1"], tabelle["b"].rows["spread_1"])

    def equivalenza_ar(_risposte):
        """Check that the ADF fit is a reparametrisation of the AR(3): same SSR, delta = sum(phi) - 1."""
        ar = sm.OLS(a[3:], sm.add_constant(np.column_stack([a[2:-1], a[1:-2], a[:-3]]))).fit()
        return (abs(ar.ssr - ra.ssr) < 1e-8 * ar.ssr
                and abs(ar.params[1:].sum() - 1 - ra.params[1]) < 1e-9)

    def figura(path):
        """Draw the two statistics against the rejection region."""
        es, _ = _stile()
        _retta_test(path, [([("cambio", _stampata(ta), es.GREEN),
                             ("spread", _stampata(tb), es.BLUE)], DF_C, -Z)])

    truth = answers(*({"coef": r.params[1], "se": r.bse[1], "t": r.tvalues[1]} for r in (ra, rb)))
    return Draft(
        dati=None, parametri={"T": Numero(n, 0), "crit": Numero(DF_C, 2)},
        tabelle={"a": tab_a, "b": tab_b}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("ta"), "b": Quesito("deca"), "c": Quesito("tb"),
                 "d": Quesito("decb"), "e": Quesito("conta")},
        attese=[lambda r: r["deca"] == "non rifiuta", lambda r: r["decb"] == "rifiuta",
                equivalenza_ar],
        margini=[Margin(stat=ta, crit=DF_C), Margin(stat=tb, crit=DF_C),
                 Margin(stat=ta, crit=MK_C), Margin(stat=tb, crit=MK_C)],
        figure={"stat": figura})


def _terzi(y):
    """Return the mean of the first third, the mean of the last third and the std of ``y``."""
    m = len(y) // 3
    return float(y[:m].mean()), float(y[-m:].mean()), float(y.std(ddof=1))


def _figura_serie(path, serie, titoli, sovrapposte=None):
    """Draw each series in its own panel, with an optional deterministic component on top.

    Args:
        path: Output PDF.
        serie: One array per panel.
        titoli: One title per panel.
        sovrapposte: Per panel, ``None`` or ``(values, label)`` drawn as a line.
    """
    es, plt = _stile()
    fig, axs = plt.subplots(1, len(serie), figsize=(6.1, 2.6), squeeze=False)
    for j, (y, titolo) in enumerate(zip(serie, titoli)):
        ax = axs[0, j]
        ax.plot(np.arange(1, len(y) + 1), y, color=es.BLUE, lw=1.2, label="serie")
        if sovrapposte and sovrapposte[j] is not None:
            ax.plot(np.arange(1, len(y) + 1), sovrapposte[j][0], color=es.RED, lw=1.6,
                    ls="--", label=sovrapposte[j][1])
            ax.legend(loc="best")
        ax.set_title(titolo)
        ax.set_xlabel("periodo")
        es.commas(ax)
    fig.subplots_adjust(wspace=0.3)
    es.save(fig, path)


@exercise("e06_04", modulo=6, livello=2, tipo="adf-specificazione-regressione")
def adf_specificazione(rng):
    """Choose the trend and the lags of the ADF regression from the plots of two series."""
    n, p = 150, 3
    b1, b2, b3 = 0.9, -0.2, 0.1
    t = np.arange(1.0, n + 1)

    def estrai(g):
        """Draw a series around a linear trend and one around a constant."""
        return 10.0 + 0.12 * t + _ar(g, n, [0.5], sigma=1.2), 5.0 + _ar(g, n, [0.8], sigma=0.5)

    def netto(serie):
        """Accept samples where only the first series has a visible trend."""
        m1, m3, sd = _terzi(serie[1])
        return abs(m3 - m1) < 0.5 * sd

    a, b = _finche(rng, estrai, netto)
    desc = {nome: tuple(round(v, 1) for v in _terzi(y)) for nome, y in
            (("produzione", a), ("tasso", b))}
    tab = "\n".join(["| serie | media primo terzo | media ultimo terzo | dev. std. |", "|---|---|---|---|"]
                    + [f"| {k} | " + " | ".join(Numero(x, 1).testo() for x in v) + " |"
                       for k, v in desc.items()])
    ra, _ = _adf(a, p - 1, "produzione", trend=True)
    rb, _ = _adf(b, p - 1, "tasso")
    ar3 = sm.OLS(b[3:], sm.add_constant(np.column_stack([b[2:-1], b[1:-2], b[:-3]]))).fit()

    def answers(d, ordine, c1, c2, c3):
        """Return every answer from the printed descriptive table and the AR(3) coefficients."""
        def trend(riga):
            """Call a trend visible when the thirds differ by more than one standard deviation."""
            return "sì" if abs(riga[1] - riga[0]) > riga[2] else "no"

        return {"trend_a": trend(d["produzione"]), "trend_b": trend(d["tasso"]),
                "ritardi": Numero(ordine - 1.0, 0), "n_coef": Numero(3.0 + ordine - 1, 0),
                "delta": Numero(c1 + c2 + c3 - 1, 2), "psi1": Numero(-(c2 + c3), 2),
                "psi2": Numero(-c3, 2),
                **{f"{k}_{s}": Numero(d[nome][i], 1) for s, nome in (("a", "produzione"), ("b", "tasso"))
                   for i, k in enumerate(("m1", "m3", "sd"))}}

    def studente(_tabelle):
        """Rebuild the answers from the printed table and the parameters of the text."""
        return answers(desc, p, b1, b2, b3)

    def identita_adf(_risposte):
        """Check that the ADF fit reparametrises the AR(3): delta, psi and the SSR are exact."""
        beta = ar3.params[1:]
        return (abs(rb.params[1] - (beta.sum() - 1)) < 1e-9
                and abs(rb.params[2] + beta[1:].sum()) < 1e-9
                and abs(rb.params[3] + beta[2]) < 1e-9 and abs(ar3.ssr - rb.ssr) < 1e-8 * ar3.ssr)

    def figura_dati(path):
        """Draw the two series."""
        _figura_serie(path, [a, b], ["produzione", "tasso"])

    def figura(path):
        """Draw the series with the deterministic component each ADF regression must contain."""
        retta = np.polyval(np.polyfit(t, a, 1), t)
        _figura_serie(path, [a, b], ["produzione", "tasso"],
                      [(retta, "costante e trend"), (np.full(n, b.mean()), "solo costante")])

    truth = answers(desc, p, b1, b2, b3)
    return Draft(
        dati=None,
        parametri={"T": Numero(n, 0), "p": Numero(p, 0), "b1": Numero(b1, 1), "b2": Numero(b2, 1),
                   "b3": Numero(b3, 1)},
        tabelle={"desc": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("trend_a"), "b": Quesito("trend_b"), "c": Quesito("ritardi"),
                 "d": Quesito("n_coef"), "e": Quesito("delta")},
        attese=[lambda r: r["trend_a"] == "sì", lambda r: r["trend_b"] == "no",
                lambda r: r["n_coef"].valore == len(ra.params), identita_adf],
        margini=[], figure={"dati": figura_dati, "componenti": figura})


@exercise("e06_05", modulo=6, livello=2,
          tipo=("adf-decisione-statistica-o-pvalue", "adf-lettura-output-regressione"))
def adf_prezzo_differenze(rng):
    """Run the ADF test on a trending price and on its differences, and decide whether to difference."""
    n = 140

    def estrai(g):
        """Draw a random walk with drift whose differences are an AR(1)."""
        return _i1(g, n, drift=0.45, dphis=(0.3,), y0=50.0)

    def netto(y):
        """Accept samples with a clear non-rejection in levels and a clear rejection in differences."""
        return (_t_livello(_adf(y, 1, "prezzo", trend=True)[0]) > -2.5
                and _t_livello(_adf(np.diff(y), 1, "dprezzo")[0]) < -4.0)

    y = _finche(rng, estrai, netto)
    r1, tab1 = _adf(y, 1, "prezzo", trend=True)
    r2, tab2 = _adf(np.diff(y), 1, "dprezzo")

    def answers(row1, row2):
        """Return every answer from the printed rows of the lagged level in both tables."""
        d1, d2 = _decide_df(row1["t"], DF_CT), _decide_df(row2["t"], DF_C)
        return {"t1": Numero(row1["t"], 2), "dec1": d1, "t2": Numero(row2["t"], 2), "dec2": d2,
                "diff": "sì" if d1 == "non rifiuta" and d2 == "rifiuta" else "no",
                "c1": Numero(row1["coef"], 5), "s1": Numero(row1["se"], 5),
                "c2": Numero(row2["coef"], 4), "s2": Numero(row2["se"], 4)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows ``prezzo_1`` and ``dprezzo_1``."""
        return answers(tabelle["liv"].rows["prezzo_1"], tabelle["dif"].rows["dprezzo_1"])

    def confronto_adfuller(_risposte):
        """Check the statistics against the ``adfuller`` routine, with the same lags and terms."""
        s1 = adfuller(y, maxlag=1, regression="ct", autolag=None)[0]
        s2 = adfuller(np.diff(y), maxlag=1, regression="c", autolag=None)[0]
        return abs(s1 - r1.tvalues[2]) < 1e-9 and abs(s2 - r2.tvalues[1]) < 1e-9

    def figura(path):
        """Draw both statistics against their own critical value."""
        es, _ = _stile()
        _retta_test(path, [([("prezzo, costante e trend", _stampata(_t_livello(r1, True)), es.GREEN)],
                            DF_CT, None),
                           ([("differenze di prezzo, costante", _stampata(_t_livello(r2)), es.BLUE)],
                            DF_C, None)])

    truth = answers(*({"coef": r.params[i], "se": r.bse[i], "t": r.tvalues[i]}
                      for r, i in ((r1, 2), (r2, 1))))
    return Draft(
        dati=None,
        parametri={"T": Numero(n, 0), "crit_ct": Numero(DF_CT, 2), "crit_c": Numero(DF_C, 2)},
        tabelle={"liv": tab1, "dif": tab2}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("t1"), "b": Quesito("dec1"), "c": Quesito("t2"),
                 "d": Quesito("dec2"), "e": Quesito("diff")},
        attese=[lambda r: r["dec1"] == "non rifiuta", lambda r: r["dec2"] == "rifiuta",
                lambda r: r["diff"] == "sì", confronto_adfuller],
        margini=[Margin(stat=r1.tvalues[2], crit=DF_CT), Margin(stat=r1.tvalues[2], crit=MK_CT),
                 Margin(stat=r2.tvalues[1], crit=DF_C), Margin(stat=r2.tvalues[1], crit=MK_C)],
        figure={"stat": figura})


@lru_cache(maxsize=None)
def _spuria_mc(n, reps=5000):
    """Simulate regressions of a random walk on an independent one; return the t ratios and R^2.

    The generator is fixed, so the figure and the checks always see the same draws.
    """
    g = np.random.default_rng(11)
    x = np.cumsum(g.normal(size=(reps, n)), axis=1)
    y = np.cumsum(g.normal(size=(reps, n)), axis=1)
    xc, yc = x - x.mean(1, keepdims=True), y - y.mean(1, keepdims=True)
    b = (xc * yc).sum(1) / (xc**2).sum(1)
    e = yc - b[:, None] * xc
    t = b / np.sqrt((e**2).sum(1) / (n - 2) / (xc**2).sum(1))
    return t, 1 - (e**2).sum(1) / (yc**2).sum(1)


def _simple(y, x, nomi=("const", "x")):
    """Fit y on a constant and ``x`` and return the result and its table with p-values."""
    res = sm.OLS(y, sm.add_constant(x)).fit()
    return res, ols_table(res, labels=list(nomi))


@exercise("e06_06", modulo=6, livello=2, tipo="random-walk-e-regressione-spuria")
def regressione_spuria(rng):
    """Show that two independent random walks give a significant regression, and its differences do not."""
    n = 150

    def estrai(g):
        """Draw two independent random walks."""
        return _i1(g, n), _i1(g, n)

    def netto(s):
        """Accept samples with a strong spurious fit in levels and a clear null in differences."""
        x, y = s
        rl, rd = _simple(y, x)[0], _simple(np.diff(y), np.diff(x))[0]
        return abs(rl.tvalues[1]) > 8.0 and rl.rsquared > 0.5 and abs(rd.tvalues[1]) < 1.2

    x, y = _finche(rng, estrai, netto)
    rl, tab_l = _simple(y, x)
    rd, tab_d = _simple(np.diff(y), np.diff(x), nomi=("const", "dx"))

    def answers(liv, dif, r2, r2_dif):
        """Return every answer from the printed slope rows and R-squared of both regressions."""
        return {"dec_liv": _decide_z(liv["t"]), "r2": Numero(r2, 3), "affidabile": "no",
                "dec_dif": _decide_z(dif["t"]), "t_liv": Numero(liv["t"], 2),
                "t_dif": Numero(dif["t"], 2), "b_liv": Numero(liv["coef"], 4),
                "b_dif": Numero(dif["coef"], 4), "r2_dif": Numero(r2_dif, 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed slope rows and R-squared."""
        return answers(tabelle["liv"].rows["x"], tabelle["dif"].rows["dx"],
                       tabelle["liv"].stats["r2"], tabelle["dif"].stats["r2"])

    def simulazione_coerente(_risposte):
        """Check by simulation that |t| > 1.96 rejects most spurious regressions in levels."""
        t, r2 = _spuria_mc(n)
        return (float(np.mean(np.abs(t) > Z)) > 0.6 and float(np.median(r2)) > 0.1
                and float(np.mean(np.abs(t) > 3 * Z)) > 0.4)

    def differenze_neutre(_risposte):
        """Check that the same test on the differences rejects about 5% of the time."""
        g = np.random.default_rng(12)
        m = 5000
        dx, dy = g.normal(size=(m, n - 1)), g.normal(size=(m, n - 1))
        xc, yc = dx - dx.mean(1, keepdims=True), dy - dy.mean(1, keepdims=True)
        b = (xc * yc).sum(1) / (xc**2).sum(1)
        e = yc - b[:, None] * xc
        t = b / np.sqrt((e**2).sum(1) / (n - 3) / (xc**2).sum(1))
        return 0.02 < float(np.mean(np.abs(t) > Z)) < 0.09

    def figura(path):
        """Draw the two series and the simulated distribution of the t ratio in levels."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.8), gridspec_kw={"width_ratios": [1, 1.1]})
        a1.plot(np.arange(1, n + 1), x, color=es.BLUE, lw=1.2, label="x")
        a1.plot(np.arange(1, n + 1), y, color=es.RED, lw=1.2, label="y")
        a1.set_xlabel("periodo")
        a1.legend(loc="upper left")
        t, _ = _spuria_mc(n)
        griglia = np.linspace(-25, 25, 300)
        quota = 100 * np.mean(np.abs(t) > Z)
        a2.hist(np.clip(t, -25, 25), bins=50, range=(-25, 25), density=True, color=es.REDBG,
                edgecolor=es.RED, label=f"simulata: $|t|>1{{,}}96$ nel {quota:.0f}%")
        a2.plot(griglia, stats.norm.pdf(griglia), color=es.BLUE, lw=1.6, label="Normale standard")
        for v in (-Z, Z):
            a2.axvline(v, color=es.GRAY, ls="--", lw=1.0)
        a2.set_xlabel("rapporto $t$ del coefficiente di $x$")
        a2.set_yticks([])
        a2.legend(loc="upper left", fontsize=7.5)
        fig.subplots_adjust(wspace=0.18)
        es.save(fig, path)

    truth = answers({"t": rl.tvalues[1], "coef": rl.params[1]}, {"t": rd.tvalues[1], "coef": rd.params[1]},
                    rl.rsquared, rd.rsquared)
    return Draft(
        dati=None, parametri={"T": Numero(n, 0)}, tabelle={"liv": tab_l, "dif": tab_d},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_liv"), "b": Quesito("r2"), "c": Quesito("affidabile"),
                 "d": Quesito("dec_dif")},
        attese=[lambda r: r["dec_liv"] == "rifiuta", lambda r: r["dec_dif"] == "non rifiuta",
                lambda r: r["r2"].valore > 0.5, simulazione_coerente, differenze_neutre],
        margini=[Margin(stat=rl.tvalues[1], crit=Z), Margin(stat=rd.tvalues[1], crit=Z)],
        figure={"spuria": figura})


def _ultimo_fuori(v, band):
    """Return the last lag (1-based) of ``v`` that leaves the band, or 0 if none does."""
    fuori = np.flatnonzero(np.abs(v) > band)
    return int(fuori[-1]) + 1 if len(fuori) else 0


@exercise("e06_07", modulo=6, livello=2,
          tipo=("identificazione-ar-ma-arma", "stazionarieta-da-correlogramma"))
def identificazione_ar_ma(rng):
    """Identify an AR(2) and an MA(2) from their correlograms and check both are stationary."""
    n, k = 250, 12
    band = _banda(n)
    phis, thetas = (0.5, 0.2), (0.7, -0.4)

    def ok_c(y):
        """Accept an AR(2) sample whose PACF has two clear spikes and then silence."""
        c, p = _correlogramma(y, k)
        return (np.all(np.abs(p[:2]) >= 1.5 * band) and np.all(np.abs(p[2:]) <= 0.6 * band)
                and np.all(np.abs(c[:3]) >= 1.5 * band) and np.all(np.abs(c[9:]) <= band))

    def ok_d(y):
        """Accept an MA(2) sample whose ACF has two clear spikes and then silence."""
        c, p = _correlogramma(y, k)
        return (np.all(np.abs(c[:2]) >= 1.5 * band) and np.all(np.abs(c[2:]) <= 0.6 * band)
                and np.any(np.abs(p[2:6]) >= 1.5 * band))

    c = _finche(rng, lambda g: _ar(g, n, phis), ok_c)
    d = _finche(rng, lambda g: _ma(g, n, thetas), ok_d)
    cc, cp = (np.round(v, 3) for v in _correlogramma(c, k))
    dc, dp = (np.round(v, 3) for v in _correlogramma(d, k))

    def answers(c_acf, c_pacf, d_acf, d_pacf):
        """Return every answer from the ACF and PACF of both series as read on the figure."""
        def modello(a, p):
            """Return whether the PACF stops first (an AR) and the lag where the stopping function ends."""
            ferma_pacf, ferma_acf = _ultimo_fuori(p, band), _ultimo_fuori(a, band)
            return ("sì", ferma_pacf) if ferma_pacf < ferma_acf else ("no", ferma_acf)

        def dentro(a):
            """Tell whether the ACF falls inside the band at some lag shown."""
            return bool(np.any(np.abs(a) <= band))

        ar_c, ord_c = modello(c_acf, c_pacf)
        ar_d, ord_d = modello(d_acf, d_pacf)
        return {"ar_c": ar_c, "ord_c": Numero(float(ord_c), 0), "ar_d": ar_d,
                "ord_d": Numero(float(ord_d), 0),
                "stazionarie": "sì" if dentro(c_acf) and dentro(d_acf) else "no",
                "banda": Numero(band, 3), "pacf1_c": Numero(c_pacf[0], 3), "pacf2_c": Numero(c_pacf[1], 3),
                "acf1_d": Numero(d_acf[0], 3), "acf2_d": Numero(d_acf[1], 3),
                "acf_c_ult": Numero(float(_ultimo_fuori(c_acf, band)), 0),
                "pacf_d_ult": Numero(float(_ultimo_fuori(d_pacf, band)), 0),
                "n_pacf_d": Numero(float(np.sum(np.abs(d_pacf) > band)), 0)}

    def studente(_tabelle):
        """Rebuild the answers from the correlograms as read on the figure."""
        return answers(cc, cp, dc, dp)

    def teoria_coerente(_risposte):
        """Check that the theoretical ACF and PACF of the two models have the textbook cut-offs."""
        ar = ArmaProcess(ar=np.r_[1.0, -np.asarray(phis)], ma=[1.0])
        ma = ArmaProcess(ar=[1.0], ma=np.r_[1.0, thetas])
        return (np.all(np.abs(ar.pacf(k + 1)[3:]) < 1e-9) and abs(ar.pacf(3)[2]) > 0.15
                and np.all(np.abs(ma.acf(k + 1)[3:]) < 1e-9) and np.all(np.abs(ma.pacf(6)[1:]) > 0.1))

    def schema_nitido(_risposte):
        """Check on the printed values that every lag is clearly outside or clearly inside the band."""
        return (np.all(np.abs(cp[:2]) >= 1.5 * band) and np.all(np.abs(cp[2:]) <= 0.6 * band)
                and np.all(np.abs(cc[:3]) >= 1.5 * band) and np.all(np.abs(cc[9:]) <= band)
                and np.all(np.abs(dc[:2]) >= 1.5 * band) and np.all(np.abs(dc[2:]) <= 0.6 * band)
                and np.any(np.abs(dp[2:6]) >= 1.5 * band))

    def figura_dati(path):
        """Draw the correlograms of both series."""
        _figura_correlogrammi(path, [(cc, cp), (dc, dp)], n, k, ["serie C", "serie D"])

    def figura(path):
        """Draw the sample correlograms (dots) against the theoretical pattern of AR(2) and MA(2)."""
        es, plt = _stile()
        lags = np.arange(1, k + 1)
        ar = ArmaProcess(ar=np.r_[1.0, -np.asarray(phis)], ma=[1.0])
        ma = ArmaProcess(ar=[1.0], ma=np.r_[1.0, thetas])
        fig, ax = plt.subplots(2, 2, figsize=(6.1, 4.2), sharex=True)
        pannelli = ((ax[0, 0], ar.acf(k + 1)[1:], cc, "ACF"), (ax[1, 0], ar.pacf(k + 1)[1:], cp, "PACF"),
                    (ax[0, 1], ma.acf(k + 1)[1:], dc, "ACF"), (ax[1, 1], ma.pacf(k + 1)[1:], dp, "PACF"))
        for a, teo, camp, nome in pannelli:
            a.axhspan(-band, band, color=es.BLUEBG, zorder=0)
            a.vlines(lags, 0, teo, color=es.BLUE, lw=2.4)
            a.plot(lags, camp, "o", ms=4.5, color=es.RED, zorder=5)
            a.axhline(0, color=es.GRAY, lw=0.8)
            a.set_ylabel(nome)
            es.commas(a, "y")
        ax[0, 0].set_title("AR(2): la PACF si annulla")
        ax[0, 1].set_title("MA(2): l'ACF si annulla")
        for a in ax[1]:
            a.set_xlabel("ritardo")
            a.set_xticks(np.arange(2, k + 1, 2))
        fig.subplots_adjust(wspace=0.32, hspace=0.12)
        es.save(fig, path)

    return Draft(
        dati=None, parametri={"T": Numero(n, 0), "k": Numero(k, 0)}, tabelle={},
        risposte=answers(cc, cp, dc, dp), studente=studente,
        quesiti={"a": Quesito("ar_c"), "b": Quesito("ord_c"), "c": Quesito("ar_d"),
                 "d": Quesito("ord_d"), "e": Quesito("stazionarie")},
        attese=[lambda r: r["ar_c"] == "sì" and r["ord_c"].valore == 2,
                lambda r: r["ar_d"] == "no" and r["ord_d"].valore == 2,
                lambda r: r["stazionarie"] == "sì", lambda r: r["acf_c_ult"].valore >= 3,
                lambda r: r["pacf_d_ult"].valore >= 3, teoria_coerente, schema_nitido],
        margini=[], figure={"dati": figura_dati, "teoria": figura})


@lru_cache(maxsize=None)
def _df_nulla(n, reps=6000):
    """Simulate the Dickey-Fuller t ratio (constant only) of a random walk; fixed generator."""
    g = np.random.default_rng(21)
    y = np.cumsum(g.normal(size=(reps, n)), axis=1)
    lag, dy = y[:, :-1], np.diff(y, axis=1)
    xc, dc = lag - lag.mean(1, keepdims=True), dy - dy.mean(1, keepdims=True)
    b = (xc * dc).sum(1) / (xc**2).sum(1)
    e = dc - b[:, None] * xc
    return b / np.sqrt((e**2).sum(1) / (n - 3) / (xc**2).sum(1))


def _m(testo):
    """Wrap a number printed with a decimal comma in math mode, so its minus sign is a real one."""
    return testo if "e" in testo else f"${testo.replace(',', '{,}')}$"


def _adf_riga(y, termini):
    """Return the ADF statistic and MacKinnon p-value of ``y`` with two lagged differences."""
    stat, pval = adfuller(y, maxlag=2, regression=termini, autolag=None)[:2]
    return float(stat), float(pval)


@exercise("e06_08", modulo=6, livello=2, tipo="adf-decisione-statistica-o-pvalue")
def adf_pvalue(rng):
    """Decide on the unit root of three series from the statistic and p-value of the ADF test."""
    n = 200
    nomi = ("oro", "argento", "tasso")
    termini = ("ct", "c", "c")

    def estrai(g):
        """Draw a random walk with drift, a driftless random walk and a stationary AR(1)."""
        return (_i1(g, n, drift=0.25, y0=30.0), _i1(g, n, y0=20.0), _ar(g, n, [0.5], const=1.0))

    def netto(serie):
        """Accept samples with clear p-values and a trap statistic for the second series."""
        (_, p1), (s2, p2), (_, p3) = (_adf_riga(y, t) for y, t in zip(serie, termini))
        return p1 > 0.2 and -2.2 < s2 < -1.75 and p3 < 0.01

    serie = _finche(rng, estrai, netto)
    calcolati = [_adf_riga(y, t) for y, t in zip(serie, termini)]
    stampati = [(float(fmt_sig(s, 4).replace(",", ".")), float(fmt_p(p).replace(",", ".")))
                for s, p in calcolati]
    descr = {"ct": "costante e trend", "c": "costante"}
    tab = "\n".join(["| serie | termini deterministici | statistica ADF | p-value |", "|---|---|---|---|"]
                    + [f"| {nm} | {descr[t]} | {_m(fmt_sig(s, 4))} | {fmt_p(p)} |"
                       for nm, t, (s, p) in zip(nomi, termini, calcolati)])

    def answers(righe):
        """Return every answer from the printed statistics and p-values."""
        dec = [("rifiuta" if p < 0.05 else "non rifiuta") for _, p in righe]
        return {"dec_oro": dec[0], "dec_argento": dec[1], "dec_tasso": dec[2],
                "conta": Numero(float(dec.count("non rifiuta")), 0), "normale": "no",
                "stat_arg": Numero(righe[1][0], 3), "p_arg": _m(fmt_p(righe[1][1])),
                "p_oro": _m(fmt_p(righe[0][1])), "p_tasso": _m(fmt_p(righe[2][1]))}

    def studente(_tabelle):
        """Rebuild the answers from the printed table."""
        return answers(stampati)

    def coerente_con_regressione(_risposte):
        """Check the statistic of the second series against its own ADF regression."""
        return abs(_t_livello(_adf(serie[1], 2, "argento")[0]) - calcolati[1][0]) < 1e-9

    def trappola(_risposte):
        """Check that the normal threshold -1.64 would wrongly reject for the second series."""
        return calcolati[1][0] < -1.64 and calcolati[1][1] > 0.2

    def figura(path):
        """Draw the simulated null distribution of the ADF statistic against the normal one."""
        es, plt = _stile()
        sim = _df_nulla(n)
        crit = float(np.quantile(sim, 0.05))
        x = np.linspace(-5, 3.5, 300)
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.hist(sim, bins=70, range=(-5, 3.5), density=True, color=es.BLUEBG, edgecolor=es.BLUE,
                label="statistica ADF simulata sotto $H_0$")
        ax.plot(x, stats.norm.pdf(x), color=es.GRAY, lw=1.3, ls="--", label="Normale standard")
        ax.axvline(-1.64, color=es.GRAY, lw=1.0, ls=":")
        ax.axvline(crit, color=es.RED, lw=1.4, label=f"5% di Dickey-Fuller: {crit:.2f}".replace(".", ","))
        ax.axvline(calcolati[1][0], color=es.GREEN, lw=1.6,
                   label=f"argento: {calcolati[1][0]:.2f}".replace(".", ","))
        ax.set_xlabel("statistica del test")
        ax.set_yticks([])
        es.commas(ax, "x")
        ax.legend(loc="upper right", fontsize=7.8)
        es.save(fig, path)

    return Draft(
        dati=None, parametri={"T": Numero(n, 0)}, tabelle={"adf": tab},
        risposte=answers(stampati), studente=studente,
        quesiti={"a": Quesito("dec_oro"), "b": Quesito("dec_argento"), "c": Quesito("dec_tasso"),
                 "d": Quesito("conta"), "e": Quesito("normale")},
        attese=[lambda r: r["dec_oro"] == "non rifiuta", lambda r: r["dec_argento"] == "non rifiuta",
                lambda r: r["dec_tasso"] == "rifiuta", lambda r: r["conta"].valore == 2,
                coerente_con_regressione, trappola],
        margini=[Margin(stat=p, crit=0.05) for _, p in calcolati], figure={"nulla": figura})


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
        ``(taus, F)`` with ``F`` shaped like ``y`` without the last axis replaced by the dates.
    """
    y2, x2 = np.atleast_2d(y), np.atleast_2d(x)
    T = y2.shape[1]
    taus = np.arange(int(np.ceil(trim * T)), int(np.floor((1 - trim) * T)) + 1)
    cum = [np.cumsum(v, axis=1) for v in (x2, y2, x2 * x2, x2 * y2, y2 * y2)]
    tot = [c[:, -1:] for c in cum]

    def ssr(m, sx, sy, sxx, sxy, syy):
        """Return the SSR of the simple regression from the sums of ``m`` observations."""
        return (syy - sy**2 / m) - (sxy - sx * sy / m) ** 2 / (sxx - sx**2 / m)

    pieno = ssr(T, *tot)
    s1 = ssr(taus, *(c[:, taus - 1] for c in cum))
    s2 = ssr(T - taus, *(t - c[:, taus - 1] for t, c in zip(tot, cum)))
    f = ((pieno - s1 - s2) / 2) / ((s1 + s2) / (T - 4))
    return taus, (f[0] if np.ndim(y) == 1 else f)


@lru_cache(maxsize=None)
def _qlr_mc(T, reps=6000):
    """Return the Monte Carlo 95th percentile of the QLR statistic under no break.

    Gaussian errors, a stable regression on one regressor, 15% trimming; the generator
    is fixed so the figures and the checks always see the same value.
    """
    g = np.random.default_rng(31)
    x = g.normal(size=(reps, T))
    y = 0.2 + 0.9 * x + g.normal(size=(reps, T))
    return float(np.quantile(_chow_percorso(y, x)[1].max(axis=1), 0.95))


def _chow_da_ssr(pieno, s1, s2, n, k=2):
    """Return the Chow F from the three sums of squared residuals and the sample size."""
    return ((pieno - s1 - s2) / k) / ((s1 + s2) / (n - 2 * k))


def _dummy_f(y, x, tau):
    """Return the F test of the dummy-interaction model that the note uses for the Chow test."""
    d = (np.arange(1, len(y) + 1) > tau).astype(float)
    res = sm.OLS(y, sm.add_constant(np.column_stack([x, d, d * x]))).fit()
    return float(res.f_test(np.array([[0, 0, 1, 0], [0, 0, 0, 1]])).fvalue)


def _fig_rette(ax, es, x, y, tau, titolo=None):
    """Scatter the two sub-samples and draw the sub-sample lines and the pooled one."""
    pieno = np.polyfit(x, y, 1)
    for sl, colore, nome in ((slice(0, tau), es.BLUE, "primo sottocampione"),
                             (slice(tau, None), es.RED, "secondo sottocampione")):
        ax.plot(x[sl], y[sl], "o", ms=3, alpha=0.5, color=colore, label=nome)
        c = np.polyfit(x[sl], y[sl], 1)
        g = np.linspace(x[sl].min(), x[sl].max(), 20)
        ax.plot(g, np.polyval(c, g), color=colore, lw=1.8)
    g = np.linspace(x.min(), x.max(), 20)
    ax.plot(g, np.polyval(pieno, g), color=es.GRAY, lw=1.4, ls="--", label="intero campione")
    if titolo:
        ax.set_title(titolo)
    es.commas(ax)


@exercise("e06_09", modulo=6, livello=2, tipo="test-di-chow")
def chow_data_nota(rng):
    """Compute the Chow F from three regressions for a break at a known date and decide."""
    T, tau = 120, 70
    fcrit = float(stats.f.ppf(0.95, 2, T - 4))
    x = rng.normal(20.0, 3.0, T)
    y = np.where(np.arange(1, T + 1) <= tau, 5.0 + 0.8 * x, 9.0 + 0.45 * x) + rng.normal(0, 1.5, T)
    r_p, tab_p = _simple(y, x, ("const", "reddito"))
    r_1, tab_1 = _simple(y[:tau], x[:tau], ("const", "reddito"))
    r_2, tab_2 = _simple(y[tau:], x[tau:], ("const", "reddito"))

    def answers(sp, s1, s2, n, c1, c2):
        """Return every answer from the printed SSR, the sample size and the two slopes."""
        f = _chow_da_ssr(sp, s1, s2, n)
        return {"F": Numero(f, 2), "dec": "rifiuta" if f > fcrit else "non rifiuta",
                "salto": Numero(c2 - c1, 3), "gl": Numero(n - 4.0, 0),
                "ssr_p": Numero(sp, 3), "ssr_1": Numero(s1, 3), "ssr_2": Numero(s2, 3),
                "b1": Numero(c1, 4), "b2": Numero(c2, 4)}

    def studente(tabelle):
        """Rebuild the answers from the SSR line and the slope row of each table."""
        p_, a_, b_ = tabelle["intero"], tabelle["prima"], tabelle["dopo"]
        return answers(p_.stats["ssr"], a_.stats["ssr"], b_.stats["ssr"], p_.stats["n"],
                       a_.rows["reddito"]["coef"], b_.rows["reddito"]["coef"])

    def uguale_al_modello_con_dummy(_risposte):
        """Check the F equals the joint test on the dummy and its interactions, and the critical value."""
        f = _chow_da_ssr(r_p.ssr, r_1.ssr, r_2.ssr, T)
        veloce = _chow_percorso(y, x)
        return (abs(f - _dummy_f(y, x, tau)) < 1e-9
                and abs(f - veloce[1][tau - veloce[0][0]]) < 1e-9
                and abs(fcrit - stats.f.isf(0.05, 2, 116)) < 1e-12)

    def figura(path):
        """Draw the data with the lines of the two sub-samples and the pooled line."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.2))
        _fig_rette(ax, es, x, y, tau)
        ax.set_xlabel("reddito")
        ax.set_ylabel("consumo")
        ax.legend(loc="upper left")
        es.save(fig, path)

    truth = answers(r_p.ssr, r_1.ssr, r_2.ssr, T, r_1.params[1], r_2.params[1])
    return Draft(
        dati=None, parametri={"T": Numero(T, 0), "tau": Numero(tau, 0), "fcrit": Numero(fcrit, 2)},
        tabelle={"intero": tab_p, "prima": tab_1, "dopo": tab_2}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("F"), "b": Quesito("dec"), "c": Quesito("salto"), "d": Quesito("gl")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["salto"].valore < 0,
                uguale_al_modello_con_dummy],
        margini=[Margin(stat=truth["F"].valore, crit=fcrit)], figure={"rette": figura})


@exercise("e06_10", modulo=6, livello=2,
          tipo=("break-strutturale-qlr", "test-di-chow"))
def qlr_data_ignota(rng):
    """Decide with the QLR critical value, not the ordinary F one, when the break date is unknown."""
    T = 120
    fcrit = float(stats.f.ppf(0.95, 2, T - 4))
    q95 = _qlr_mc(T)

    def estrai(g):
        """Draw a stable regression of the excess return on the market return."""
        x = g.normal(0.0, 1.0, T)
        return x, 0.2 + 0.9 * x + g.normal(0.0, 1.1, T)

    def netto(dati):
        """Accept samples whose maximum F beats the ordinary F value but not the QLR one."""
        f = _chow_percorso(dati[1], dati[0])[1].max()
        return 3.8 < f < 4.6

    x, y = _finche(rng, estrai, netto)
    taus, f_path = _chow_percorso(y, x)
    tau = int(taus[np.argmax(f_path)])
    sp, s1, s2 = (sm.OLS(v, sm.add_constant(u)).fit().ssr for v, u in
                  ((y, x), (y[:tau], x[:tau]), (y[tau:], x[tau:])))
    righe = [("intero campione", T, sp), (f"osservazioni 1-{tau}", tau, s1),
             (f"osservazioni {tau + 1}-{T}", T - tau, s2)]
    stampate = [float(fmt_sig(v, 6).replace(",", ".")) for v in (sp, s1, s2)]
    tab = "\n".join(["| campione | osservazioni | SSR |", "|---|---|---|"]
                    + [f"| {nome} | {m} | {fmt_sig(v, 6)} |" for nome, m, v in righe])

    def answers(a, b, c):
        """Return every answer from the three printed sums of squared residuals."""
        f = _chow_da_ssr(a, b, c, T)
        return {"F": Numero(f, 2), "dec": "rifiuta" if f > QLR_CRIT else "non rifiuta",
                "naive": "sì" if f > fcrit else "no", "problema": "sì" if f > QLR_CRIT else "no",
                "ssr_p": Numero(a, 3), "ssr_1": Numero(b, 3), "ssr_2": Numero(c, 3)}

    def studente(_tabelle):
        """Rebuild the answers from the printed table."""
        return answers(*stampate)

    def qlr_calibrato(_risposte):
        """Check that the simulated 95th percentile of the QLR statistic is close to the quoted one."""
        return abs(q95 - QLR_CRIT) < 0.5 and fcrit < QLR_CRIT

    def massimo_coerente(_risposte):
        """Check that the F from the three SSR is the maximum of the path and matches the dummy model."""
        return (abs(answers(sp, s1, s2)["F"].valore - f_path.max()) < 0.01
                and abs(_dummy_f(y, x, tau) - f_path.max()) < 1e-9)

    def figura(path):
        """Draw the sequence of Chow statistics with the two critical values."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.plot(taus, f_path, color=es.BLUE, lw=1.5, label="$F(\\tau)$")
        ax.axhline(fcrit, color=es.GRAY, ls="--", lw=1.1,
                   label=f"F(2, {T - 4}) al 5%: {fcrit:.2f}".replace(".", ","))
        ax.axhline(QLR_CRIT, color=es.RED, lw=1.4,
                   label=f"QLR al 5%: {QLR_CRIT:.2f}".replace(".", ","))
        ax.plot([tau], [f_path.max()], "o", color=es.GREEN, ms=7, zorder=5,
                label=f"massimo: {f_path.max():.2f}".replace(".", ","))
        ax.set_xlabel("data candidata $\\tau$ (osservazione)")
        ax.set_ylabel("statistica di Chow")
        es.commas(ax)
        ax.set_ylim(0, QLR_CRIT * 1.5)
        ax.legend(loc="upper left", ncol=2, fontsize=8)
        es.save(fig, path)

    truth = answers(sp, s1, s2)
    return Draft(
        dati=None,
        parametri={"T": Numero(T, 0), "tau": Numero(tau, 0), "qcrit": Numero(QLR_CRIT, 2),
                   "fcrit": Numero(fcrit, 2)},
        tabelle={"ssr": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("F"), "b": Quesito("dec"), "c": Quesito("naive"),
                 "d": Quesito("problema")},
        attese=[lambda r: r["dec"] == "non rifiuta", lambda r: r["naive"] == "sì",
                lambda r: r["problema"] == "no", qlr_calibrato, massimo_coerente],
        margini=[Margin(stat=truth["F"].valore, crit=QLR_CRIT), Margin(stat=truth["F"].valore, crit=fcrit),
                 Margin(stat=truth["F"].valore, crit=q95)],
        figure={"percorso": figura})


@exercise("e06_11", modulo=6, livello=3, punti=4,
          tipo=("adf-specificazione-regressione", "adf-lettura-output-regressione",
                "adf-decisione-statistica-o-pvalue"))
def adf_senza_trend_sbagliato(rng):
    """Show that omitting the trend from the ADF regression hides the stationarity of a trending series."""
    n, lags = 120, 2
    t = np.arange(1.0, n + 1)

    def estrai(g):
        """Draw a series that is stationary around a linear trend."""
        return 10.0 + 0.15 * t + _ar(g, n, [0.6])

    def netto(y):
        """Accept samples where the correct test rejects clearly and the one without trend clearly does not."""
        return (_t_livello(_adf(y, lags, "pil", trend=True)[0], True) < -4.2
                and _t_livello(_adf(y, lags, "pil")[0]) > -2.0)

    y = _finche(rng, estrai, netto)
    r1, tab1 = _adf(y, lags, "pil")
    r2, tab2 = _adf(y, lags, "pil", trend=True)
    m1, m3, sd = (round(v, 1) for v in _terzi(y))
    tab = "\n".join(["| serie | media primo terzo | media ultimo terzo | dev. std. |", "|---|---|---|---|",
                     "| pil | " + " | ".join(Numero(v, 1).testo() for v in (m1, m3, sd)) + " |"])

    def answers(desc, row1, row2):
        """Return every answer from the printed table and the lagged-level rows of both models."""
        dec = _decide_df(row2["t"], DF_CT)
        return {"trend": "sì" if abs(desc[1] - desc[0]) > desc[2] else "no",
                "t2": Numero(row2["t"], 2), "dec": dec, "staz": "sì" if dec == "rifiuta" else "no",
                "stessa": "sì" if _decide_df(row1["t"], DF_C) == dec else "no",
                "somma": Numero(1 + row2["coef"], 3), "t1": Numero(row1["t"], 2),
                "c2": Numero(row2["coef"], 5), "s2": Numero(row2["se"], 5),
                "m1": Numero(desc[0], 1), "m3": Numero(desc[1], 1), "sd": Numero(desc[2], 1)}

    def studente(tabelle):
        """Rebuild the answers from the descriptive table and the rows ``pil_1`` of both models."""
        return answers((m1, m3, sd), tabelle["m1"].rows["pil_1"], tabelle["m2"].rows["pil_1"])

    def equivale_ar3(_risposte):
        """Check that the model with trend reparametrises the AR(3) with trend: sum(beta) = 1 + delta."""
        tempo = np.arange(1.0, n - 2)
        ar = sm.OLS(y[3:], np.column_stack([np.ones(n - 3), tempo, y[2:-1], y[1:-2], y[:-3]])).fit()
        return (abs(ar.params[2:].sum() - (1 + r2.params[2])) < 1e-9
                and abs(ar.ssr - r2.ssr) < 1e-8 * ar.ssr)

    def figura_dati(path):
        """Draw the series."""
        _figura_serie(path, [y], ["pil"])

    def figura(path):
        """Draw the series with its fitted trend and the two statistics against their critical values."""
        es, plt = _stile()
        fig = plt.figure(figsize=(6.1, 4.2))
        grid = fig.add_gridspec(3, 1, height_ratios=[2.0, 0.7, 0.7], hspace=0.6)
        ax = fig.add_subplot(grid[0])
        ax.plot(t, y, color=es.BLUE, lw=1.2, label="pil")
        ax.plot(t, np.polyval(np.polyfit(t, y, 1), t), color=es.RED, lw=1.6, ls="--", label="trend lineare")
        ax.set_xlabel("periodo")
        ax.legend(loc="upper left")
        es.commas(ax)
        _asse_test(fig.add_subplot(grid[1]), es,
                   [("solo costante", _stampata(_t_livello(r1)), es.GRAY)], DF_C)
        _asse_test(fig.add_subplot(grid[2]), es,
                   [("costante e trend", _stampata(_t_livello(r2, True)), es.GREEN)], DF_CT)
        es.save(fig, path)

    truth = answers((m1, m3, sd), {"t": r1.tvalues[1], "coef": r1.params[1]},
                    {"t": r2.tvalues[2], "coef": r2.params[2], "se": r2.bse[2]})
    return Draft(
        dati=None,
        parametri={"T": Numero(n, 0), "lags": Numero(lags, 0), "crit_c": Numero(DF_C, 2),
                   "crit_ct": Numero(DF_CT, 2)},
        tabelle={"desc": tab, "m1": tab1, "m2": tab2}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("trend"), "b": Quesito("t2"), "c": Quesito("dec"),
                 "d": Quesito("staz"), "e": Quesito("stessa"), "f": Quesito("somma")},
        attese=[lambda r: r["trend"] == "sì", lambda r: r["dec"] == "rifiuta",
                lambda r: r["stessa"] == "no", lambda r: 0 < r["somma"].valore < 1, equivale_ar3],
        margini=[Margin(stat=r2.tvalues[2], crit=DF_CT), Margin(stat=r2.tvalues[2], crit=MK_CT),
                 Margin(stat=r1.tvalues[1], crit=DF_C), Margin(stat=r1.tvalues[1], crit=MK_C)],
        figure={"dati": figura_dati, "test": figura})


def _theta_da_rho(rho):
    """Return the invertible root (|theta| < 1) of ``rho = theta / (1 + theta**2)``."""
    return (1 - np.sqrt(1 - 4 * rho**2)) / (2 * rho)


@exercise("e06_12", modulo=6, livello=3, punti=4,
          tipo=("stazionarieta-da-correlogramma", "identificazione-ar-ma-arma"))
def correlogrammi_livello_differenza(rng):
    """Read the correlograms of a series and of its differences, identify an MA(1) and recover its theta."""
    n, k, mu, theta = 200, 12, 0.3, -0.7
    band = _banda(n)

    def estrai(g):
        """Draw a series whose differences are a drift plus an MA(1); return level and differences."""
        dy = mu + _ma(g, n, [theta])
        return 20.0 + np.r_[0.0, np.cumsum(dy)], dy

    def netto(s):
        """Accept samples with a persistent level, a clear MA(1) cut-off and a usable rho_1."""
        (ay, py), (ad, pd) = (_correlogramma(v, k) for v in s)
        return (np.all(np.abs(ay) >= 1.5 * band) and abs(py[0]) >= 1.5 * band
                and ad[0] <= -1.5 * band and np.all(np.abs(ad[1:]) <= 0.6 * band)
                and np.all(pd[:2] <= -1.5 * band) and abs(round(ad[0], 2)) <= 0.48)

    y, dy = _finche(rng, estrai, netto)
    ay, py = (np.round(v, 3) for v in _correlogramma(y, k))
    ad, pd = (np.round(v, 3) for v in _correlogramma(dy, k))
    rho1 = round(float(_correlogramma(dy, k)[0][0]), 2)

    def answers(c_y, p_y, c_d, p_d, rho):
        """Return every answer from the correlograms of both series and the printed rho_1."""
        def stazionaria(c):
            """Call a series stationary when its ACF falls inside the bands within the lags shown."""
            return "sì" if np.any(np.abs(c) <= band) else "no"

        ordine = _ultimo_fuori(c_d, band)
        th = _theta_da_rho(rho)
        return {"sta_y": stazionaria(c_y), "sta_d": stazionaria(c_d),
                "ar_d": "sì" if _ultimo_fuori(p_d, band) < ordine else "no",
                "ord_d": Numero(float(ordine), 0), "theta": Numero(th, 2),
                "theta_alt": Numero(1 / th, 2), "banda": Numero(band, 3),
                "acf_y_min": Numero(np.abs(c_y).min(), 3), "pacf1_y": Numero(p_y[0], 3),
                "acf1_d": Numero(c_d[0], 3), "pacf_d_ult": Numero(float(_ultimo_fuori(p_d, band)), 0),
                "n_pacf_d": Numero(float(np.sum(np.abs(p_d) > band)), 0)}

    def studente(_tabelle):
        """Rebuild the answers from the correlograms as read on the figure and the printed rho_1."""
        return answers(ay, py, ad, pd, rho1)

    def schema_nitido(_risposte):
        """Check on the printed values the persistent level and the clear MA(1) cut-off."""
        return (np.all(np.abs(ay) >= 1.5 * band) and abs(py[0]) >= 1.5 * band
                and ad[0] <= -1.5 * band and np.all(np.abs(ad[1:]) <= 0.6 * band)
                and np.all(pd[:2] <= -1.5 * band) and abs(rho1) < 0.5)

    def formula_coerente(_risposte):
        """Check rho_1 = theta/(1+theta^2) for the invertible root and against a long simulation."""
        th = _theta_da_rho(rho1)
        g = np.random.default_rng(5)
        s = _ma(g, 400_000, [th])
        return (abs(th / (1 + th**2) - rho1) < 1e-12 and abs(th) < 1
                and abs(acf(s, nlags=1, fft=True)[1] - rho1) < 0.01)

    def figura_dati(path):
        """Draw the correlograms of the level and of the differences."""
        _figura_correlogrammi(path, [(ay, py), (ad, pd)], n, k, ["$y$", "$\\Delta y$"])

    def figura(path):
        """Draw rho_1 as a function of theta, with the two roots of the observed value."""
        es, plt = _stile()
        th = _theta_da_rho(rho1)
        x = np.r_[np.linspace(-3, -0.05, 200), np.linspace(0.05, 3, 200)]
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.plot(x, x / (1 + x**2), color=es.BLUE, lw=1.6, label=r"$\rho_1=\theta/(1+\theta^2)$")
        ax.axhline(rho1, color=es.GRAY, ls="--", lw=1.0,
                   label=rf"$\hat\rho_1={rho1:.2f}$".replace(".", "{,}"))
        ax.plot([th], [rho1], "o", color=es.GREEN, ms=8, zorder=5,
                label=rf"$|\theta|<1$: $\theta={th:.2f}$".replace(".", "{,}"))
        ax.plot([1 / th], [rho1], "o", mfc="white", color=es.RED, ms=8, zorder=5,
                label=rf"scartata: $1/\theta={1 / th:.2f}$".replace(".", "{,}"))
        ax.set_xlabel(r"$\theta$")
        ax.set_ylabel(r"$\rho_1$")
        es.commas(ax)
        ax.legend(loc="upper left", fontsize=8)
        es.save(fig, path)

    truth = answers(ay, py, ad, pd, rho1)
    return Draft(
        dati=None, parametri={"T": Numero(n, 0), "k": Numero(k, 0), "rho1": Numero(rho1, 2)},
        tabelle={}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("sta_y"), "b": Quesito("sta_d"), "c": Quesito("ar_d"),
                 "d": Quesito("ord_d"), "e": Quesito("theta")},
        attese=[lambda r: r["sta_y"] == "no", lambda r: r["sta_d"] == "sì", lambda r: r["ar_d"] == "no",
                lambda r: r["ord_d"].valore == 1, lambda r: r["pacf_d_ult"].valore >= 2,
                lambda r: r["theta"].valore < 0 and abs(r["theta"].valore) < 1, schema_nitido,
                formula_coerente],
        margini=[], figure={"dati": figura_dati, "radici": figura})


@exercise("e06_13", modulo=6, livello=3, punti=4, tipo=("break-strutturale-qlr", "test-di-chow"))
def qlr_effetto_mascherato(rng):
    """Show that a break hides a relation on the full sample, and locate it with the QLR test."""
    T, tau0 = 120, 72
    q95 = _qlr_mc(T)

    def estrai(g):
        """Draw a regression whose slope changes sign at ``tau0``."""
        x = g.normal(0.0, 1.0, T)
        beta = np.where(np.arange(1, T + 1) <= tau0, 0.9, -1.3)
        return x, 0.1 + beta * x + g.normal(0.0, 1.0, T)

    def netto(dati):
        """Accept samples with a null slope on the full sample and a clear QLR rejection."""
        x, y = dati
        return (abs(_simple(y, x)[0].tvalues[1]) < 1.2
                and _chow_percorso(y, x)[1].max() > 1.15 * max(QLR_CRIT, q95))

    x, y = _finche(rng, estrai, netto)
    taus, f_path = _chow_percorso(y, x)
    tau = int(taus[np.argmax(f_path)])
    r_p, tab_p = _simple(y, x, ("const", "mkt"))
    r_1, tab_1 = _simple(y[:tau], x[:tau], ("const", "mkt"))
    r_2, tab_2 = _simple(y[tau:], x[tau:], ("const", "mkt"))

    def answers(pieno, sp, s1, s2, n, c1, c2):
        """Return every answer from the full-sample row, the three SSR and the two slopes."""
        f = _chow_da_ssr(sp, s1, s2, n)
        dec_qlr = "rifiuta" if f > QLR_CRIT else "non rifiuta"
        return {"dec_pieno": _decide_z(pieno["t"]), "F": Numero(f, 2), "dec_qlr": dec_qlr,
                "affidabile": "sì" if dec_qlr == "non rifiuta" else "no", "salto": Numero(c2 - c1, 3),
                "t_pieno": Numero(pieno["t"], 2), "b_pieno": Numero(pieno["coef"], 4),
                "ssr_p": Numero(sp, 3), "ssr_1": Numero(s1, 3), "ssr_2": Numero(s2, 3),
                "b1": Numero(c1, 4), "b2": Numero(c2, 4)}

    def studente(tabelle):
        """Rebuild the answers from the three printed tables."""
        p_, a_, b_ = tabelle["pieno"], tabelle["prima"], tabelle["dopo"]
        return answers(p_.rows["mkt"], p_.stats["ssr"], a_.stats["ssr"], b_.stats["ssr"],
                       p_.stats["n"], a_.rows["mkt"]["coef"], b_.rows["mkt"]["coef"])

    def massimo_coerente(_risposte):
        """Check the F from the SSR is the path maximum, equals the dummy-model F and sits near the break."""
        f = _chow_da_ssr(r_p.ssr, r_1.ssr, r_2.ssr, T)
        return (abs(f - f_path.max()) < 1e-9 and abs(f - _dummy_f(y, x, tau)) < 1e-9
                and abs(tau - tau0) <= 8 and abs(q95 - QLR_CRIT) < 0.5)

    def figura(path):
        """Draw the data with the lines of the two regimes and the sequence of Chow statistics."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1, 1.1]})
        _fig_rette(a1, es, x, y, tau)
        a1.set_xlabel("rendimento del mercato")
        a1.set_ylabel("rendimento del titolo")
        a1.legend(loc="upper right", fontsize=7)
        a2.plot(taus, f_path, color=es.BLUE, lw=1.5)
        a2.axhline(QLR_CRIT, color=es.RED, lw=1.4, label=f"QLR al 5%: {QLR_CRIT:.2f}".replace(".", ","))
        a2.plot([tau], [f_path.max()], "o", color=es.GREEN, ms=7, zorder=5,
                label=f"massimo: {f_path.max():.1f}".replace(".", ","))
        a2.set_xlabel("data candidata $\\tau$")
        a2.set_ylabel("$F(\\tau)$")
        a2.legend(loc="upper left", fontsize=8)
        es.commas(a2)
        fig.subplots_adjust(wspace=0.35)
        es.save(fig, path)

    truth = answers({"t": r_p.tvalues[1], "coef": r_p.params[1]}, r_p.ssr, r_1.ssr, r_2.ssr, T,
                    r_1.params[1], r_2.params[1])
    return Draft(
        dati=None, parametri={"T": Numero(T, 0), "tau": Numero(tau, 0), "qcrit": Numero(QLR_CRIT, 2)},
        tabelle={"pieno": tab_p, "prima": tab_1, "dopo": tab_2}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_pieno"), "b": Quesito("F"), "c": Quesito("dec_qlr"),
                 "d": Quesito("affidabile"), "e": Quesito("salto")},
        attese=[lambda r: r["dec_pieno"] == "non rifiuta", lambda r: r["dec_qlr"] == "rifiuta",
                lambda r: r["affidabile"] == "no", lambda r: r["b1"].valore > 0 > r["b2"].valore,
                massimo_coerente],
        margini=[Margin(stat=r_p.tvalues[1], crit=Z), Margin(stat=truth["F"].valore, crit=QLR_CRIT),
                 Margin(stat=truth["F"].valore, crit=q95)],
        figure={"rotture": figura})
