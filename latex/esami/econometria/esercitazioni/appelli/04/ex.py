"""Appello simulato 4: log-log con interazione ed eteroschedasticità, poi cointegrazione fra due commodity."""

from types import SimpleNamespace

import numpy as np
import statsmodels.api as sm
from scipy import stats
from scipy.signal import lfilter
from statsmodels.stats.diagnostic import het_white
from statsmodels.tsa.stattools import acf, adfuller, pacf

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import fmt_p, fmt_sig, ols_table

TITOLO = "Appello simulato 4"

# Normal quantiles the exam texts fix: two-sided 5% and one-sided 5%.
Z = 1.96
Z1 = 1.64

ALFA = 0.05

# A p-value within half of ALFA from ALFA would let the printed rounding decide.
MARGINE_P = 0.5

# Numbers the student reads in the text: the checks and the solution must use the same values.
N1 = 300
C_RIF = 3.5
VAR_NOX = 8.0
RIV_CRIME = 2.0
DELTA_STANZE = 3.0
LIM = 0.33
OBIETTIVO = 20.0

T2 = 300
ELL = 2
LAG_HAC = 6
B0 = 1.0
Q = 0.90
LAGS_ACF = 12

# True parameters of the simulated error-correction model of exercise 2; G1 + G2 = B_LP
# keeps the long-run slope equal to B_LP.
A_LP, B_LP = 1.10, 0.94
G1, G2, LAMBDA = 0.65, 0.29, -0.45


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _v(x, decimali):
    """Return ``x`` for a figure label, with the decimal comma."""
    return f"{x:.{decimali}f}".replace(".", ",")


def _campiona(g, genera, accetta, tentativi=20000):
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


def _decide(t, crit=Z):
    """Return the two-sided decision for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > crit else "non rifiuta"


def _decide_p(p):
    """Return the decision at 5% from a p-value."""
    return "rifiuta" if p < ALFA else "non rifiuta"


def _white(resid, regressori):
    """Run the White test on continuous regressors.

    The auxiliary regression of the squared residuals has the regressors, their
    squares and their pairwise products. Dummies are left out on purpose: their
    squares repeat the dummy itself, which would make the degrees of freedom ambiguous.

    Args:
        resid: OLS residuals of the model under test.
        regressori: Name to values of the continuous regressors, constant excluded.

    Returns:
        A namespace with the statistic ``lm = n R^2``, its degrees of freedom ``gl``
        and the chi-square p-value ``p``.
    """
    nomi = list(regressori)
    aux = [regressori[k] for k in nomi]
    for i, a in enumerate(nomi):
        aux.append(regressori[a] ** 2)
        for b in nomi[i + 1:]:
            aux.append(regressori[a] * regressori[b])
    res = sm.OLS(resid ** 2, sm.add_constant(np.column_stack(aux))).fit()
    lm = len(resid) * res.rsquared
    return SimpleNamespace(lm=lm, gl=len(aux), p=float(stats.chi2.sf(lm, len(aux))))


def _blocco(nome, lm, gl, p):
    """Return the printed output of a heteroskedasticity test, in the layout of gretl."""
    stat = fmt_sig(lm, 6).replace(",", "{,}")
    return (f"**{nome} per l'eteroschedasticità.** Ipotesi nulla: omoschedasticità. "
            f"Statistica test: $LM = {stat}$, con p-value $P(\\chi^2({gl}) > {stat}) =$ "
            f"{fmt_p(p)}.")


def _ar1(g, n, phi, sd):
    """Draw a stationary AR(1) path of length ``n`` started from its stationary law."""
    e = g.normal(0.0, sd, n)
    e[0] /= np.sqrt(1.0 - phi ** 2)
    return lfilter([1.0], [1.0, -phi], e)


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

    Written out from the sandwich formula, to check the library routine the exercise prints.
    """
    A = np.linalg.inv(X.T @ X)
    S = (X * u[:, None]).T @ (X * u[:, None])
    for j in range(1, m + 1):
        G = (X[j:] * u[j:, None]).T @ (X[:-j] * u[:-j, None])
        S += (1 - j / (m + 1)) * (G + G.T)
    return A @ S @ A


def _dols_coerente(y, x, ell, banda, res):
    """Check a DOLS fit against the regressors and the sandwich formula written out from scratch."""
    dx = np.diff(x, prepend=np.nan)
    t = np.arange(ell + 1, len(y) - ell)
    X = np.column_stack([np.ones(len(t)), x[t]] + [dx[t - j] for j in range(-ell, ell + 1)])
    fit = sm.OLS(y[t], X).fit()
    cov = _hac_manuale(X, fit.resid, banda)
    return (abs(fit.params[1] - res.params[1]) < 1e-9
            and abs(np.sqrt(cov[1, 1]) - res.bse[1]) < 1e-9)


def _ecm(y, x):
    """Estimate the two-step error-correction model with one lag of the differenced regressor.

    The long-run regression gives the residual that enters the ECM lagged once.

    Returns:
        The long-run fit, the ECM fit and the ECM table.
    """
    lungo = sm.OLS(y, sm.add_constant(x)).fit()
    dy, dx, z = np.diff(y), np.diff(x), lungo.resid
    X = np.column_stack([np.ones(len(y) - 2), dx[1:], dx[:-1], z[1:-1]])
    res = sm.OLS(dy[1:], X).fit()
    tab = ols_table(res, labels=["const", "d_l_mais", "d_l_mais_1", "ecm_1"], stats=("n", "r2"))
    return lungo, res, tab


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


def _k_simulato(lungo, res, q, x_fisso):
    """Iterate the fitted ECM in levels with the regressor held fixed and return the periods that absorb ``q``.

    Starts from a unit disequilibrium in ``t - 1`` and neglects the constant, the
    differenced regressor and the shocks, so it checks the closed form of
    :func:`_periodi` against the equation itself.
    """
    lam = res.params[3]
    a, b = lungo.params
    y = a + b * x_fisso + 1.0
    for k in range(1, 1000):
        y = y + lam * (y - a - b * x_fisso)
        if y - a - b * x_fisso <= 1.0 - q:
            return k
    raise RuntimeError("il disequilibrio non si assorbe")


def _acf_pacf(resid, ritardi):
    """Return the sample ACF and PACF of ``resid`` at lags ``1..ritardi``."""
    return (acf(resid, nlags=ritardi, fft=False)[1:],
            pacf(resid, nlags=ritardi, method="ywm")[1:])


def _banda(n):
    """Return the half-width of the 95% band of a sample autocorrelation of ``n`` observations."""
    return Z / np.sqrt(n)


def _atteso(nome, predicato):
    """Wrap ``predicato`` in an expectation named ``nome``, so a failure says which one broke."""
    def check(risposte):
        """Apply the wrapped predicate to the answers."""
        return bool(predicato(risposte))

    check.__name__ = nome
    return check


@exercise("a04_01", modulo=11, livello=3, punti=19,
          tipo=("elasticita-log-log", "interazione-effetto-marginale-condizionato",
                "test-su-valore-specifico", "test-unilaterale-su-soglia",
                "variazione-percentuale-log-livello", "eteroschedasticita-implicazioni"))
def prezzi_case_inquinamento(rng):
    """Read a log-log model with a distance interaction: elasticities, three tests, a White test."""
    n = N1
    coeff = [6.3, -0.55, -0.019, 0.165, -0.08, 0.50]

    def genera(g):
        """Draw the cross-section, fit the model with HC1 errors and run the White test."""
        lnox = g.normal(3.5, 0.30, n)
        crime = np.clip(g.gamma(2.4, 2.6, n), 0.3, 30.0)
        rooms = np.clip(g.normal(6.2, 0.7, n), 4.2, 8.6)
        lontano = (g.random(n) < 1.0 / (1.0 + np.exp(3.0 * (lnox - 3.5)))).astype(float)
        d_nox = lontano * (lnox - C_RIF)
        # The error spread grows with the number of rooms and with crime, so White rejects.
        sd = 0.15 * np.exp(0.35 * (rooms - 6.2)) * (1.0 + 0.03 * crime)
        cols = {"l_nox": lnox, "crime": crime, "rooms": rooms, "lontano": lontano, "d_nox": d_nox}
        X = sm.add_constant(np.column_stack(list(cols.values())))
        y = X @ np.array(coeff) + sd * g.normal(0.0, 1.0, n)
        res = sm.OLS(y, X).fit(cov_type="HC1", use_t=True)
        cov = res.cov_params()
        b, se = res.params, res.bse
        comb, se_comb = b[1] + b[5], np.sqrt(cov[1, 1] + cov[5, 5] + 2 * cov[1, 5])
        w = _white(res.resid, {k: cols[k] for k in ("l_nox", "crime", "rooms")})
        return SimpleNamespace(y=y, X=X, cols=cols, res=res, cov=cov, w=w,
                               t_comb=comb / se_comb,
                               t_valore=(b[2] + RIV_CRIME / 100) / se[2],
                               t_soglia=(b[3] - LIM / DELTA_STANZE) / se[3])

    def accetta(s):
        """Accept a draw where the interaction is significant, the far-area elasticity is not, and every test is clear."""
        t = s.res.tvalues
        return (t[1] < -5.0 and t[5] > 2.6 and s.res.params[4] < -0.04
                and 0.5 < abs(s.t_comb) < 1.6 and 0.3 < abs(s.t_valore) < 1.4
                and s.t_soglia > 2.3 and s.w.p < 0.005)

    s = _campiona(rng, genera, accetta)
    res, cols = s.res, s.cols
    cov = round(float(s.cov[1, 5]), 6)
    tab = ols_table(res, labels=["const", *cols], stats=("n", "r2"))
    tab_white = _blocco("Test di White", s.w.lm, s.w.gl, s.w.p)
    p_stampato = float(fmt_p(s.w.p).replace(",", "."))
    lm_stampato = float(fmt_sig(s.w.lm, 6).replace(",", "."))

    def rows_veri():
        """Return the rows of the table at full precision."""
        nomi = ["const", *cols]
        return {k: {"coef": float(res.params[j]), "se": float(res.bse[j]),
                    "t": float(res.tvalues[j])} for j, k in enumerate(nomi)}

    def answers(rows, c, p_w, lm):
        """Return every answer from the table rows, the covariance of the text and the White output."""
        b = {k: v["coef"] for k, v in rows.items()}
        e = {k: v["se"] for k, v in rows.items()}
        comb = b["l_nox"] + b["d_nox"]
        se_comb = np.sqrt(e["l_nox"] ** 2 + e["d_nox"] ** 2 + 2 * c)
        t_comb = comb / se_comb
        t_valore = (b["crime"] + RIV_CRIME / 100) / e["crime"]
        soglia = LIM / DELTA_STANZE
        t_soglia = (b["rooms"] - soglia) / e["rooms"]
        return {"el": Numero(b["l_nox"], 3), "pct": Numero(VAR_NOX * b["l_nox"], 2),
                "eff": Numero(comb, 3), "t_int": Numero(rows["d_nox"]["t"], 2),
                "dec_int": _decide(rows["d_nox"]["t"]), "se_comb": Numero(se_comb, 4),
                "t_comb": Numero(t_comb, 2), "dec_comb": _decide(t_comb),
                "t_valore": Numero(t_valore, 2), "dec_valore": _decide(t_valore),
                "ic_lo": Numero(100 * (b["crime"] - Z * e["crime"]), 2),
                "ic_hi": Numero(100 * (b["crime"] + Z * e["crime"]), 2),
                "soglia": Numero(soglia, 2), "t_soglia": Numero(t_soglia, 2),
                "dec_soglia": "rifiuta" if t_soglia > Z1 else "non rifiuta",
                "pct_lont": Numero(100 * b["lontano"], 1),
                "stanze": Numero(OBIETTIVO / (100 * b["rooms"]), 2),
                "dec_white": _decide_p(p_w), "endogeno": "no", "robusti": "sì",
                "p_white": fmt_p(p_w), "lm": Numero(lm, 4), "eff6": Numero(comb, 6),
                "pct_crime": Numero(100 * b["crime"], 2),
                "soglia6": Numero(soglia, 6),
                "b_nox": Numero(b["l_nox"], 6), "b_int": Numero(b["d_nox"], 6),
                "b_crime": Numero(b["crime"], 6), "b_rooms": Numero(b["rooms"], 6),
                "b_lont": Numero(b["lontano"], 6), "se_nox": Numero(e["l_nox"], 6),
                "se_int": Numero(e["d_nox"], 6), "se_crime": Numero(e["crime"], 6),
                "se_rooms": Numero(e["rooms"], 6), "t_crime": Numero(b["crime"] / e["crime"], 2),
                "t_rooms": Numero(b["rooms"] / e["rooms"], 2),
                "pct_stanze": Numero(100 * DELTA_STANZE * b["rooms"], 1)}

    def studente(tabelle):
        """Rebuild the answers from the printed table, the covariance and the printed White p-value."""
        return answers(tabelle["ols"].rows, cov, p_stampato, lm_stampato)

    def verita():
        """Return the truth, with the covariance of the text rounded as the student sees it."""
        return answers(rows_veri(), cov, s.w.p, s.w.lm)

    def derivata_coerente(_risposte):
        """Check the two elasticities and the dummy gap against differences of the fitted log price."""
        def fitted(lnox, lontano, crime=6.0, rooms=6.2):
            """Return the fitted log price at the given point."""
            x = np.array([1.0, lnox, crime, rooms, lontano, lontano * (lnox - C_RIF)])
            return float(x @ res.params)

        h = 1e-6
        vicine = (fitted(3.4 + h, 0.0) - fitted(3.4 - h, 0.0)) / (2 * h)
        lontane = (fitted(3.4 + h, 1.0) - fitted(3.4 - h, 1.0)) / (2 * h)
        scarto = fitted(C_RIF, 1.0) - fitted(C_RIF, 0.0)
        r = verita()
        return (abs(vicine - r["el"].valore) < 5e-4
                and abs(lontane - r["eff"].valore) < 5e-4
                and abs(100 * scarto - r["pct_lont"].valore) < 0.05)

    def covarianza_coerente(_risposte):
        """Check the standard error of the far-area elasticity against the quadratic form w' V w."""
        w = np.zeros(6)
        w[1], w[5] = 1.0, 1.0
        esatto = float(np.sqrt(w @ s.cov @ w))
        return abs(esatto - verita()["se_comb"].valore) < 5e-5

    def white_statsmodels(_risposte):
        """Check the statistic and its degrees of freedom against statsmodels."""
        X = sm.add_constant(np.column_stack([cols["l_nox"], cols["crime"], cols["rooms"]]))
        lm, _, _, _ = het_white(res.resid, X)
        return abs(lm - s.w.lm) < 1e-8 and s.w.gl == 9

    def sandwich_hc1(_risposte):
        """Check the HC1 errors of the table against the sandwich formula written out."""
        X, u = s.X, res.resid
        pane = np.linalg.inv(X.T @ X)
        carne = (X * (u ** 2)[:, None]).T @ X
        cov_hc1 = len(u) / (len(u) - X.shape[1]) * pane @ carne @ pane
        return float(np.max(np.abs(np.sqrt(np.diag(cov_hc1)) - res.bse))) < 1e-10

    def obiettivi_coerenti(_risposte):
        """Check the rooms needed and the three-room threshold against the log-price change they imply."""
        r = verita()
        return (abs(res.params[3] * r["stanze"].valore - OBIETTIVO / 100) < 1e-4
                and abs(DELTA_STANZE * r["soglia"].valore - LIM) < 1e-12)

    def figura_elasticita(path):
        """Draw the price change implied by a change of nox in the near areas, with the 95% band."""
        es, plt = _stile()
        b, e = res.params[1], res.bse[1]
        fig, ax = plt.subplots(figsize=(6.1, 2.9))
        x = np.linspace(-10, 10, 101)
        lo, hi = (b - Z * e) * x, (b + Z * e) * x
        ax.fill_between(x, np.minimum(lo, hi), np.maximum(lo, hi), color=es.BLUEBG,
                        label="intervallo di confidenza al 95%")
        ax.plot(x, b * x, color=es.BLUE, lw=1.6, label=r"$\hat\beta_1 \times$ variazione di nox")
        ax.plot([VAR_NOX], [b * VAR_NOX], "o", color=es.RED, ms=7, zorder=5)
        ax.annotate(f"nox +{VAR_NOX:g}%: prezzo {_v(b * VAR_NOX, 2)}%", xy=(VAR_NOX, b * VAR_NOX),
                    xytext=(1.5, 3.0), textcoords="data", ha="left", fontsize=8.5, color=es.RED,
                    fontweight="bold", arrowprops={"arrowstyle": "-", "color": es.RED, "lw": 0.9})
        ax.axhline(0, color=es.GRAY, lw=0.7)
        ax.set_xlabel("variazione percentuale di nox")
        ax.set_ylabel("variazione percentuale attesa del prezzo")
        es.commas(ax)
        ax.legend(loc="lower left")
        es.save(fig, path)

    def figura_interazione(path):
        """Draw the price change against a change of nox for near and far areas, with the far-area band."""
        es, plt = _stile()
        w = np.zeros(6)
        w[1], w[5] = 1.0, 1.0
        b1, comb, se_comb = res.params[1], float(w @ res.params), float(np.sqrt(w @ s.cov @ w))
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        x = np.linspace(-10, 10, 101)
        lo, hi = (comb - Z * se_comb) * x, (comb + Z * se_comb) * x
        ax.fill_between(x, np.minimum(lo, hi), np.maximum(lo, hi), color=es.BLUEBG,
                        label="intervallo al 95% (aree lontane)")
        ax.plot(x, b1 * x, color=es.RED, lw=1.6, label=f"aree vicine: pendenza {_v(b1, 3)}")
        ax.plot(x, comb * x, color=es.BLUE, lw=1.6, label=f"aree lontane: pendenza {_v(comb, 3)}")
        ax.axhline(0, color=es.GRAY, lw=0.7)
        ax.set_xlabel("variazione percentuale di nox")
        ax.set_ylabel("variazione percentuale attesa del prezzo")
        es.commas(ax)
        ax.legend(loc="lower left")
        es.save(fig, path)

    def figura_valore(path):
        """Draw the 95% interval for the percentage effect of one more crime against the claimed value."""
        es = figs.use_style()
        b, e = res.params[2], res.bse[2]
        fig, _ = es.ci_line(100 * b, 100 * (b - Z * e), 100 * (b + Z * e), h0=-RIV_CRIME,
                            decimals=2, xlabel="variazione % del prezzo per un reato in più per mille abitanti")
        es.save(fig, path)

    def figura_soglia(path):
        """Draw the statistic of the one-sided test against the right rejection region."""
        es = figs.use_style()
        t = verita()["t_soglia"].valore
        fig, _ = es.dist_test("z", stat=t, crit=Z1, tail="right", statlabel=f"t = {_v(t, 2)}",
                              critlabel=f"regione di rifiuto: t > {_v(Z1, 2)}")
        es.save(fig, path)

    def figura_percentuali(path):
        """Draw the price change against the rooms added, and the interval for the dummy effect."""
        es, plt = _stile()
        b3, b4, e4 = res.params[3], res.params[4], res.bse[4]
        fig = plt.figure(figsize=(6.1, 4.0))
        grid = fig.add_gridspec(2, 1, height_ratios=[1.6, 1.0], hspace=0.6)
        ax = fig.add_subplot(grid[0])
        d = np.linspace(0, 2.5, 100)
        ob = OBIETTIVO / (100 * b3)
        ax.plot(d, 100 * b3 * d, color=es.BLUE, lw=1.6, label=r"$100\,\hat\beta_3\,\Delta$rooms")
        ax.axhline(OBIETTIVO, color=es.RED, ls="--", lw=1.0)
        ax.plot([ob], [OBIETTIVO], "o", color=es.RED, ms=7, zorder=5)
        ax.vlines(ob, 0, OBIETTIVO, color=es.RED, ls=":", lw=1.0)
        ax.annotate(f"{_v(ob, 2)} stanze", xy=(ob, 0), xytext=(4, 6), textcoords="offset points",
                    fontsize=8.5, color=es.RED, fontweight="bold")
        ax.set_xlabel("stanze in più")
        ax.set_ylabel("variazione % del prezzo")
        es.commas(ax)
        ax.legend(loc="upper left")
        bx = fig.add_subplot(grid[1])
        es.ci_line(100 * b4, 100 * (b4 - Z * e4), 100 * (b4 + Z * e4), ax=bx, decimals=1,
                   xlabel="prezzo di un'area lontana meno prezzo di un'area vicina (%)")
        es.save(fig, path)

    def figura_white(path):
        """Draw the White statistic against the rejection region of its chi-square distribution."""
        es = figs.use_style()
        fig, ax = es.dist_test("chi2", s.w.gl, stat=s.w.lm, crit=float(stats.chi2.ppf(1 - ALFA, s.w.gl)),
                               tail="right", statlabel=f"LM = {_v(s.w.lm, 2)}")
        # The density peaks near the left edge and the statistic sits near the right one.
        ax.legend(loc="upper left", bbox_to_anchor=(0.3, 0.97))
        es.save(fig, path)

    truth = verita()
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "c": Numero(C_RIF, 2), "var": Numero(VAR_NOX, 0),
                   "cov": Numero(cov, 6), "riv": Numero(RIV_CRIME, 0),
                   "delta": Numero(DELTA_STANZE, 0), "perc": Numero(100 * LIM, 0),
                   "lim": Numero(LIM, 2), "ob": Numero(OBIETTIVO, 0), "gl": Numero(s.w.gl, 0)},
        tabelle={"ols": tab, "white": tab_white}, risposte=truth, studente=studente,
        quesiti={"d1a": Quesito("el"), "d1b": Quesito("pct"), "d2a": Quesito("eff"),
                 "d2b": Quesito("dec_int"), "d2c": Quesito("dec_comb"),
                 "d3a": Quesito("t_valore"), "d3b": Quesito("dec_valore"),
                 "d4a": Quesito("soglia"), "d4b": Quesito("t_soglia"), "d4c": Quesito("dec_soglia"),
                 "d5a": Quesito("pct_lont"), "d5b": Quesito("stanze"),
                 "d6a": Quesito("dec_white"), "d6b": Quesito("endogeno"), "d6c": Quesito("robusti")},
        attese=[_atteso("elasticita vicine negativa", lambda r: r["el"].valore < 0),
                _atteso("elasticita lontane negativa", lambda r: r["eff"].valore < 0),
                _atteso("elasticita lontane meno ripida", lambda r: abs(r["eff"].valore) < abs(r["el"].valore)),
                _atteso("interazione significativa", lambda r: r["dec_int"] == "rifiuta"),
                _atteso("effetto lontano non significativo", lambda r: r["dec_comb"] == "non rifiuta"),
                _atteso("affermazione sui reati compatibile", lambda r: r["dec_valore"] == "non rifiuta"),
                _atteso("soglia sulle stanze superata", lambda r: r["dec_soglia"] == "rifiuta"),
                _atteso("White rifiuta", lambda r: r["dec_white"] == "rifiuta"),
                _atteso("dummy negativa", lambda r: r["pct_lont"].valore < 0),
                _atteso("derivate e scarto", derivata_coerente),
                _atteso("errore standard della combinazione", covarianza_coerente),
                _atteso("White come statsmodels", white_statsmodels),
                _atteso("errori HC1 come sandwich", sandwich_hc1),
                _atteso("obiettivi e soglia", obiettivi_coerenti)],
        margini=[Margin(stat=res.tvalues[5], crit=Z), Margin(stat=s.t_comb, crit=Z),
                 Margin(stat=s.t_valore, crit=Z), Margin(stat=s.t_soglia, crit=Z1),
                 Margin(stat=s.t_soglia, crit=Z), Margin(stat=p_stampato, crit=ALFA, rel=MARGINE_P)],
        figure={"elasticita": figura_elasticita, "interazione": figura_interazione,
                "valore": figura_valore, "soglia": figura_soglia, "percentuali": figura_percentuali,
                "white": figura_white})


@exercise("a04_02", modulo=11, livello=3, punti=13,
          tipo=("adf-decisione-statistica-o-pvalue", "stazionarieta-da-correlogramma",
                "inferenza-coefficiente-lungo-periodo", "ecm-velocita-assorbimento"))
def frumento_mais(rng):
    """Walk from unit-root tests to a DOLS inference and the speed of an error-correction model."""
    n = T2

    def genera(g):
        """Draw a cointegrated pair of log prices from an error-correction model with a lagged difference.

        The long-run slope is ``B_LP`` because the short-run coefficients on the
        differenced regressor add up to it; the lagged term makes the long-run error
        correlated with the differences of the regressor, which is what the DOLS corrects.
        """
        dx = 0.0004 + g.normal(0.0, 0.013, n + 1)
        e = g.normal(0.0, 0.010, n + 1)
        x = 5.30 + np.cumsum(dx)
        y = np.empty(n + 1)
        y[0] = A_LP + B_LP * x[0]
        for t in range(1, n + 1):
            z = y[t - 1] - A_LP - B_LP * x[t - 1]
            y[t] = y[t - 1] + G1 * dx[t] + G2 * dx[t - 1] + LAMBDA * z + e[t]
        x, y = x[1:], y[1:]
        lungo = sm.OLS(y, sm.add_constant(x)).fit()
        a, p = _acf_pacf(lungo.resid, LAGS_ACF)
        return SimpleNamespace(x=x, y=y, lungo=lungo, acf=a, pacf=p)

    banda = _banda(n)

    def accetta(s):
        """Accept a draw with a clear correlogram, clear unit-root verdicts, a clear DOLS test and a clear horizon."""
        visto = np.round(s.acf, 2)
        fuori = np.abs(visto) > banda
        k = int(fuori.sum())
        if not (2 <= k <= 5 and fuori[:k].all() and np.all(np.abs(np.abs(visto) - banda) > 0.03)):
            return False
        if (abs(round(s.pacf[0], 2)) < banda + 0.05
                or not np.all(np.abs(np.abs(np.round(s.pacf, 2)) - banda) > 0.02)):
            return False
        p_y = adfuller(s.y, maxlag=1, regression="c", autolag=None)[1]
        p_x = adfuller(s.x, maxlag=1, regression="c", autolag=None)[1]
        if not (p_y > 0.10 and p_x > 0.10):
            return False
        d = _dols(s.y, s.x, ELL, LAG_HAC)
        if not (-4.5 < (d.params[1] - B0) / d.bse[1] < -2.6):
            return False
        _, ecm, _ = _ecm(s.y, s.x)
        lam = ecm.params[3]
        if not (ecm.tvalues[3] < -4.0 and 0.3 < 1 + lam < 0.7):
            return False
        k_ass = _periodi(lam, Q)
        return all(abs((1 + lam) ** j - (1 - Q)) / (1 - Q) > 0.08 for j in (k_ass - 1, k_ass))

    s = _campiona(rng, genera, accetta)
    p_f = round(float(adfuller(s.y, maxlag=1, regression="c", autolag=None)[1]), 4)
    p_m = round(float(adfuller(s.x, maxlag=1, regression="c", autolag=None)[1]), 4)
    dols = _dols(s.y, s.x, ELL, LAG_HAC)
    lungo, ecm, tab_ecm = _ecm(s.y, s.x)
    visto = np.round(s.acf, 2)
    tab_dols = ols_table(dols, labels=["const", "l_mais"], stats=("n", "r2"))

    def answers(pf, pm, acf_visto, riga_b, riga_lam):
        """Return every answer from the printed p-values, the ACF as read, the DOLS row and the ECM row."""
        dec_f, dec_m = _decide_p(pf), _decide_p(pm)
        fuori = int(np.sum(np.abs(acf_visto) > banda))
        staz = "sì" if fuori <= 6 else "no"
        non_staz = "sì" if dec_f == dec_m == "non rifiuta" else "no"
        b, se = riga_b["coef"], riga_b["se"]
        t_b = (b - B0) / se
        lam, t_lam = riga_lam["coef"], riga_lam["t"]
        phi = 1.0 + lam
        k = _periodi(lam, Q)
        return {"dec_f": dec_f, "dec_m": dec_m, "non_staz": non_staz, "fuori": Numero(fuori, 0),
                "staz": staz, "banda": Numero(banda, 3),
                "ben_def": "sì" if non_staz == "sì" and staz == "sì" else "no",
                "b": Numero(b, 5), "se": Numero(se, 5), "t_tabella": Numero(riga_b["t"], 2),
                "t_b": Numero(t_b, 2), "dec_b": _decide(t_b),
                "ic_lo": Numero(b - Z * se, 3), "ic_hi": Numero(b + Z * se, 3),
                "dec_lam": _decide(t_lam), "lam": Numero(lam, 4), "t_lam": Numero(t_lam, 2),
                "phi": Numero(phi, 4), "primo": Numero(-100 * lam, 2), "k": Numero(k, 0),
                "km": Numero(k - 1, 0), "assorbito": Numero(100 * (1 - phi ** k), 2),
                "resto": Numero(phi ** k, 4), "resto_prima": Numero(phi ** (k - 1), 4),
                "obiettivo": Numero(1 - Q, 2), "log": Numero(np.log(1 - Q) / np.log(phi), 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed p-values, the rounded ACF and the printed rows."""
        return answers(p_f, p_m, visto, tabelle["dols"].rows["l_mais"], tabelle["ecm"].rows["ecm_1"])

    def figura_adf(path):
        """Draw the two ADF p-values against the 5% threshold."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.1))
        ax.axvspan(0, ALFA, color=es.REDBG, label="regione di rifiuto")
        ax.axvline(ALFA, color=es.RED, ls="--", lw=1.1)
        for i, (nome, p) in enumerate((("l_frumento", p_f), ("l_mais", p_m))):
            ax.plot([p], [i], "o", color=es.GREEN, ms=7, zorder=5)
            ax.annotate(f"{nome}: {_v(p, 4)}", xy=(p, i), xytext=(10, 8), textcoords="offset points",
                        ha="left", fontsize=8.5, color=es.GREEN)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.7, 1.7)
        ax.set_yticks([])
        ax.set_xlabel("p-value del test ADF (soglia $0{,}05$)")
        es.commas(ax, "x")
        ax.legend(loc="upper right")
        es.save(fig, path)

    def figura_testo(path):
        """Draw the ACF and PACF of the long-run residuals, as in the exam figure."""
        es, plt = _stile()
        fig, axs = plt.subplots(2, 1, figsize=(6.1, 3.7), sharex=True)
        es.acf_pacf(s.acf, s.pacf, n=n, axes=[axs[0], axs[1]])
        axs[1].set_xticks(np.arange(2, LAGS_ACF + 1, 2))
        fig.subplots_adjust(hspace=0.25)
        es.save(fig, path)

    def figura_residui(path):
        """Draw the two log prices and the long-run residuals, which keep returning to zero."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.6))
        t = np.arange(1, n + 1)
        a1.plot(t, s.y, color=es.BLUE, lw=1.1, label="l_frumento")
        a1.plot(t, s.x, color=es.RED, lw=1.1, label="l_mais")
        a1.set_title("logaritmi dei prezzi")
        a1.legend(loc="center left")
        a2.plot(t, lungo.resid, color=es.BLUE, lw=1.1)
        a2.axhline(0, color=es.GRAY, lw=0.8)
        a2.set_title("residui di lungo periodo")
        for ax in (a1, a2):
            ax.set_xlabel("giorno")
            es.commas(ax)
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    def figura_dols(path):
        """Draw the 95% interval of the DOLS coefficient against the claimed elasticity."""
        es = figs.use_style()
        b, e = float(dols.params[1]), float(dols.bse[1])
        fig, _ = es.ci_line(b, b - Z * e, b + Z * e, h0=B0, decimals=3,
                            xlabel=r"coefficiente di lungo periodo $\beta$ (DOLS, errore HAC)")
        es.save(fig, path)

    def figura_assorbimento(path):
        """Draw the share of disequilibrium left after each period, with the horizon of the target."""
        es, _ = _stile()
        fig, _, _ = es.decay(float(ecm.params[3]), horizon=int(truth["k"].valore) + 3, targets=(Q,))
        es.save(fig, path)

    def schema_nitido(_risposte):
        """Check the correlogram: the first bars out of the band, the rest clearly in, a PACF spike at lag one."""
        fuori = np.abs(visto) > banda
        k = int(fuori.sum())
        return (2 <= k <= 5 and fuori[:k].all() and np.all(np.abs(np.abs(visto) - banda) > 0.03)
                and abs(s.pacf[0]) > banda + 0.05
                and np.all(np.abs(np.abs(np.round(s.pacf, 2)) - banda) > 0.02))

    def acf_manuale(_risposte):
        """Check the first sample autocorrelation of the residuals against its definition."""
        u = lungo.resid - lungo.resid.mean()
        return abs(np.sum(u[1:] * u[:-1]) / np.sum(u ** 2) - s.acf[0]) < 1e-12

    def ecm_ben_costruito(_risposte):
        """Check that the ECM regressors are the lagged residual and the differences, aligned in time."""
        a, b = lungo.params
        z = s.y - a - b * s.x
        X = np.column_stack([np.ones(n - 2), np.diff(s.x)[1:], np.diff(s.x)[:-1], z[1:-1]])
        refit = sm.OLS(np.diff(s.y)[1:], X).fit()
        return (abs(refit.params[3] - ecm.params[3]) < 1e-12 and int(ecm.nobs) == n - 2
                and abs(z[1] - lungo.resid[1]) < 1e-12)

    def ricorsione_coerente(r):
        """Check that iterating the fitted equation gives the horizon of the closed form."""
        return _k_simulato(lungo, ecm, Q, 5.0) == r["k"].valore

    truth = answers(p_f, p_m, s.acf, {"coef": float(dols.params[1]), "se": float(dols.bse[1]),
                          "t": float(dols.tvalues[1])},
                    {"coef": float(ecm.params[3]), "t": float(ecm.tvalues[3])})
    return Draft(
        dati=None,
        parametri={"T": Numero(n, 0), "p_f": Numero(p_f, 4), "p_m": Numero(p_m, 4),
                   "ell": Numero(ELL, 0), "m": Numero(LAG_HAC, 0), "b0": Numero(B0, 2),
                   "q": Numero(100 * Q, 0)},
        tabelle={"dols": tab_dols, "ecm": tab_ecm}, risposte=truth, studente=studente,
        quesiti={"d7a": Quesito("dec_f"), "d7b": Quesito("dec_m"), "d7c": Quesito("non_staz"),
                 "d8a": Quesito("fuori"), "d8b": Quesito("staz"),
                 "d9a": Quesito("ben_def"), "d9b": Quesito("t_b"), "d9c": Quesito("dec_b"),
                 "d9d": Quesito("ic_hi"),
                 "d10a": Quesito("dec_lam"), "d10b": Quesito("k"), "d10c": Quesito("assorbito")},
        attese=[_atteso("ADF frumento non rifiuta", lambda r: r["dec_f"] == "non rifiuta"),
                _atteso("ADF mais non rifiuta", lambda r: r["dec_m"] == "non rifiuta"),
                _atteso("serie non stazionarie", lambda r: r["non_staz"] == "sì"),
                _atteso("residui stazionari", lambda r: r["staz"] == "sì"),
                _atteso("relazione ben definita", lambda r: r["ben_def"] == "sì"),
                _atteso("DOLS rifiuta l'elasticita unitaria", lambda r: r["dec_b"] == "rifiuta"),
                _atteso("coefficiente di correzione significativo", lambda r: r["dec_lam"] == "rifiuta"),
                _atteso("coefficiente di correzione negativo", lambda r: r["lam"].valore < 0),
                _atteso("intervallo sotto l'elasticita unitaria", lambda r: r["ic_hi"].valore < B0),
                _atteso("correlogramma nitido", schema_nitido),
                _atteso("ACF come definizione", acf_manuale),
                _atteso("ECM allineato", ecm_ben_costruito),
                _atteso("orizzonte iterato", ricorsione_coerente),
                _atteso("DOLS come sandwich", lambda r: _dols_coerente(s.y, s.x, ELL, LAG_HAC, dols))],
        margini=[Margin(stat=p_f, crit=ALFA, rel=1.0), Margin(stat=p_m, crit=ALFA, rel=1.0),
                 Margin(stat=truth["t_b"].valore, crit=Z), Margin(stat=ecm.tvalues[3], crit=Z)],
        figure={"adf": figura_adf, "correlogramma": figura_testo, "residui": figura_residui,
                "dols": figura_dols, "assorbimento": figura_assorbimento})
