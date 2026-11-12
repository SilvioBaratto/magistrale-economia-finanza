"""Module 05 - heteroskedasticity: residual plots, tests, robust standard errors, implications."""

from types import SimpleNamespace

import numpy as np
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan, het_white

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import fmt_p, fmt_sig, ols_table

TITOLO = "Eteroschedasticità"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

ALFA = 0.05

# A p-value within half of ALFA from ALFA would let the printed rounding decide.
MARGINE_P = 0.5


def _fit(y, columns):
    """Fit OLS of ``y`` on a constant and the named columns; return result, design matrix and table."""
    names = list(columns)
    X = sm.add_constant(np.column_stack([columns[k] for k in names]))
    res = sm.OLS(y, X).fit()
    return res, X, ols_table(res, labels=["const", *names])


def _fit_robusto(y, X, names):
    """Fit OLS with HC1 standard errors and t-based p-values; return result and table.

    HC1 is the variant gretl and Stata print by default, and the one of the exam texts.
    """
    res = sm.OLS(y, X).fit(cov_type="HC1", use_t=True)
    return res, ols_table(res, labels=["const", *names])


def _sandwich(X, e):
    """Return the HC1 covariance matrix of the OLS coefficients from the sandwich formula."""
    n, p = X.shape
    pane = np.linalg.inv(X.T @ X)
    carne = (X * (e ** 2)[:, None]).T @ X
    return n / (n - p) * pane @ carne @ pane


def _varianza_white(X, e, j):
    """Return the HC1 variance of coefficient ``j`` as sum(r^2 e^2) / sum(r^2)^2, scaled by n/(n-p).

    ``r`` is the residual of the regression of column ``j`` on the other columns.
    """
    n, p = X.shape
    altri = np.delete(X, j, axis=1)
    r = X[:, j] - altri @ np.linalg.lstsq(altri, X[:, j], rcond=None)[0]
    return n / (n - p) * np.sum(r ** 2 * e ** 2) / np.sum(r ** 2) ** 2


def _decide(t):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > Z else "non rifiuta"


def _p_stampato(p):
    """Return ``p`` as the student reads it, after the rounding of the printed output."""
    return float(fmt_p(p).replace(",", "."))


def _decide_p(p_testo):
    """Return the decision at 5% from a printed p-value."""
    return "rifiuta" if p_testo < ALFA else "non rifiuta"


def _lm_test(resid, columns, white=False):
    """Run the auxiliary regression of the squared residuals and return LM = n R^2.

    Args:
        resid: OLS residuals of the model under test.
        columns: Regressor name to values, constant excluded.
        white: Whether to add squares and cross products, as the White test does.

    Returns:
        A namespace with the auxiliary fit ``res``, the regressor names ``nomi``, the
        statistic ``lm``, its degrees of freedom ``gl`` and the chi-square p-value ``p``.
    """
    aux = dict(columns)
    if white:
        nomi = list(columns)
        for i, a in enumerate(nomi):
            aux[f"{a}^2"] = columns[a] ** 2
            for b in nomi[i + 1:]:
                aux[f"{a}*{b}"] = columns[a] * columns[b]
    res = sm.OLS(resid ** 2, sm.add_constant(np.column_stack(list(aux.values())))).fit()
    lm = len(resid) * res.rsquared
    return SimpleNamespace(res=res, nomi=list(aux), lm=lm, gl=len(aux),
                           p=float(stats.chi2.sf(lm, len(aux))))


def _blocco(nome, lm, gl, p):
    """Return the printed output of a heteroskedasticity test, in the layout of gretl."""
    stat = fmt_sig(lm, 6).replace(",", "{,}")
    return (f"**{nome} per l'eteroschedasticità.** Ipotesi nulla: omoschedasticità. "
            f"Statistica test: $LM = {stat}$, con p-value $P(\\chi^2({gl}) > {stat}) =$ "
            f"{fmt_p(p)}.")


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _intervalli(ax, es, voci, xlabel, ancora=-0.4):
    """Draw one 95% interval per entry of ``voci`` = (height, coefficient, se, label, colour)."""
    for altezza, coef, err, etichetta, colore in voci:
        ax.errorbar(coef, altezza, xerr=Z * err, fmt="o", color=colore, capsize=4,
                    label=etichetta)
    ax.axvline(0, color=es.GRAY, lw=0.8)
    ax.set_yticks([])
    ax.set_ylim(-0.6, max(v[0] for v in voci) + 0.6)
    ax.set_xlabel(xlabel)
    es.commas(ax, "x")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, ancora), ncol=2)


def _residui(ax, es, fitted, resid, titolo):
    """Draw the residuals against the fitted values with the zero line."""
    ax.plot(fitted, resid, "o", color=es.BLUE, ms=3, alpha=0.55)
    ax.axhline(0, color=es.RED, lw=1.0)
    ax.set_xlabel(r"valori predetti $\hat y$")
    ax.set_ylabel(r"residui $\hat\epsilon$")
    ax.set_title(titolo, loc="left")
    es.commas(ax)


def _quartili(fitted, resid):
    """Return the standard deviation of the residuals in each quartile of the fitted values."""
    bordi = np.quantile(fitted, [0.25, 0.5, 0.75])
    classe = np.digitize(fitted, bordi)
    return np.array([resid[classe == q].std(ddof=1) for q in range(4)])


@exercise("e05_01", modulo=5, livello=1, tipo="eteroschedasticita-grafico-residui")
def due_grafici(rng):
    """Judge two residual plots: a fan shape against a homogeneous band."""
    n = 300
    x_a = rng.uniform(3, 40, n)
    mu_a = 2 + 2.6 * x_a
    y_a = mu_a + 0.2 * mu_a * rng.normal(0, 1, n)
    x_b = rng.uniform(3, 40, n)
    y_b = 8 + 2.5 * x_b + rng.normal(0, 11, n)
    ra, Xa, _ = _fit(y_a, {"x": x_a})
    rb, Xb, _ = _fit(y_b, {"x": x_b})
    pa, pb = het_breuschpagan(ra.resid, Xa)[1], het_breuschpagan(rb.resid, Xb)[1]
    qa, qb = _quartili(ra.fittedvalues, ra.resid), _quartili(rb.fittedvalues, rb.resid)

    truth = {"a": "no" if pa < ALFA else "sì", "b": "no" if pb < ALFA else "sì",
             "c": "no" if pa < ALFA else "sì",
             "rapporto_a": Numero(qa[3] / qa[0], 1), "rapporto_b": Numero(qb[3] / qb[0], 1)}

    def studente(_tabelle):
        """Return the verdicts, which are read from the figure and not from a table."""
        return dict(truth)

    def figura_dati(path):
        """Draw the two residual plots side by side on the same vertical scale."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), sharey=True)
        _residui(a1, es, ra.fittedvalues, ra.resid, "Modello A")
        _residui(a2, es, rb.fittedvalues, rb.resid, "Modello B")
        a2.set_ylabel("")
        fig.subplots_adjust(wspace=0.08)
        es.save(fig, path)

    def figura_quartili(path):
        """Draw the spread of the residuals in each quartile of the fitted values."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.8))
        pos = np.arange(4)
        ax.bar(pos - 0.2, qa, 0.4, color=es.RED, label="Modello A")
        ax.bar(pos + 0.2, qb, 0.4, color=es.BLUE, label="Modello B")
        ax.set_xticks(pos, ["1°", "2°", "3°", "4°"])
        ax.set_xlabel(r"quartile dei valori predetti $\hat y$")
        ax.set_ylabel(r"deviazione standard dei residui")
        es.commas(ax, "y")
        ax.legend(loc="upper left")
        es.save(fig, path)

    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("a"), "b": Quesito("b"), "c": Quesito("c")},
        attese=[lambda r: np.corrcoef(np.abs(ra.resid), ra.fittedvalues)[0, 1] > 0.3,
                lambda r: abs(np.corrcoef(np.abs(rb.resid), rb.fittedvalues)[0, 1]) < 0.1,
                lambda r: pa < 1e-4 and pb > 0.3, lambda r: qa[3] / qa[0] > 2.5,
                lambda r: qb[3] / qb[0] < 1.5],
        margini=[Margin(stat=pa, crit=ALFA, rel=MARGINE_P), Margin(stat=pb, crit=ALFA, rel=MARGINE_P)],
        figure={"residui": figura_dati, "quartili": figura_quartili})


@exercise("e05_02", modulo=5, livello=1, tipo="test-eteroschedasticita")
def breusch_pagan_lm(rng):
    """Compute LM = n R^2 from the auxiliary regression and decide against a chi-square critical value."""
    n = 250
    sup = rng.normal(95, 25, n)
    dist = rng.gamma(3.0, 1.5, n)
    eta = rng.uniform(0, 60, n)
    sd = 5.0 * np.exp(0.006 * (sup - 95) + 0.008 * (eta - 30))
    y = 40 + 2.2 * sup - 3.5 * dist - 0.5 * eta + sd * rng.normal(0, 1, n)
    cols = {"sup": sup, "dist": dist, "eta": eta}
    res, X, tab = _fit(y, cols)
    bp = _lm_test(res.resid, cols)
    tab_aux = ols_table(bp.res, labels=["const", *cols], stats=("n", "r2"), p=False)
    crit = float(stats.chi2.ppf(1 - ALFA, bp.gl))
    crit_stampato = float(f"{crit:.3f}")

    def answers(n_oss, r2):
        """Return every answer from the sample size and the R-squared of the auxiliary regression."""
        lm = n_oss * r2
        return {"lm": Numero(lm, 2), "dec": "rifiuta" if lm > crit_stampato else "non rifiuta",
                "robusti": "sì" if lm > crit_stampato else "no", "r2": Numero(r2, 4)}

    def studente(tabelle):
        """Rebuild the answers from the line under the auxiliary table."""
        st = tabelle["aus"].stats
        return answers(st["n"], st["r2"])

    def coerente_con_statsmodels(r):
        """Check that LM is the Koenker statistic n R^2 of the Breusch-Pagan test."""
        return abs(het_breuschpagan(res.resid, X)[0] - r["lm"].valore) < 1e-2

    def figura(path):
        """Draw LM against the rejection region of the chi-square distribution."""
        es = figs.use_style()
        fig, _ = es.dist_test("chi2", bp.gl, stat=bp.lm, crit=crit, tail="right")
        es.save(fig, path)

    truth = answers(n, bp.res.rsquared)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "k": Numero(bp.gl, 0), "crit": Numero(crit, 3)},
        tabelle={"ols": tab, "aus": tab_aux}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("lm"), "b": Quesito("dec"), "c": Quesito("robusti")},
        attese=[lambda r: r["dec"] == "rifiuta", coerente_con_statsmodels],
        margini=[Margin(stat=bp.lm, crit=crit_stampato)], figure={"chi2": figura})


@exercise("e05_03", modulo=5, livello=1, tipo="errori-standard-robusti")
def usuali_contro_robusti(rng):
    """Compare usual and HC1 standard errors, and see a decision change with no change of coefficients."""
    n = 250
    sup = rng.normal(110, 30, n).clip(40, None)
    giard = rng.gamma(1.6, 1.2, n)
    cam = rng.integers(1, 6, n).astype(float)
    mu = 20 + 1.2 * sup + 2.0 * giard + 2.0 * cam
    y = mu + (4 + 5.0 * giard + 0.05 * sup) * rng.normal(0, 1, n)
    cols = {"sup": sup, "giardino": giard, "camere": cam}
    res, X, tab = _fit(y, cols)
    rob, tab_rob = _fit_robusto(y, X, list(cols))
    j = 2

    def answers(naive, robusta):
        """Return every answer from the printed ``giardino`` rows of the two tables."""
        return {"fattore": Numero(robusta["se"] / naive["se"], 2),
                "dec_usuale": _decide(naive["t"]), "dec_robusto": _decide(robusta["t"]),
                "cambiano": "no" if naive["coef"] == robusta["coef"] else "sì",
                "b": Numero(naive["coef"], 4), "se_usuale": Numero(naive["se"], 4),
                "se_robusto": Numero(robusta["se"], 4), "t_usuale": Numero(naive["t"], 2),
                "t_robusto": Numero(robusta["t"], 2),
                "ic_lo": Numero(robusta["coef"] - Z * robusta["se"], 3),
                "ic_hi": Numero(robusta["coef"] + Z * robusta["se"], 3)}

    def studente(tabelle):
        """Rebuild the answers from the ``giardino`` row of both printed tables."""
        return answers(tabelle["ols"].rows["giardino"], tabelle["rob"].rows["giardino"])

    def riga(fit):
        """Return the ``giardino`` row of a fit as the dictionary the table parser would give."""
        return {"coef": fit.params[j], "se": fit.bse[j], "t": fit.tvalues[j]}

    def sandwich_coerente(_risposte):
        """Check HC1 against the sandwich formula, whole and coefficient by coefficient, and against HC0 times n/(n-k-1)."""
        v = _sandwich(X, res.resid)
        per_coefficiente = [_varianza_white(X, res.resid, i) for i in range(X.shape[1])]
        hc0 = sm.OLS(y, X).fit(cov_type="HC0")
        return (np.allclose(np.sqrt(np.diag(v)), rob.bse, rtol=1e-10)
                and np.allclose(np.sqrt(per_coefficiente), rob.bse, rtol=1e-10)
                and np.allclose(rob.bse ** 2 / hc0.bse ** 2, n / (n - X.shape[1]), rtol=1e-10))

    def figura(path):
        """Draw the 95% intervals of the garden coefficient with the usual and the robust errors."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.0))
        _intervalli(ax, es, [(1, res.params[j], res.bse[j], "errori standard usuali", es.RED),
                             (0, rob.params[j], rob.bse[j], "errori standard robusti", es.BLUE)],
                    "coefficiente di giardino, con intervallo al 95%")
        es.save(fig, path)

    truth = answers(riga(res), riga(rob))
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"ols": tab, "rob": tab_rob},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("fattore"), "b": Quesito("dec_usuale"),
                 "c": Quesito("dec_robusto"), "d": Quesito("cambiano")},
        attese=[lambda r: r["dec_usuale"] == "rifiuta", lambda r: r["dec_robusto"] == "non rifiuta",
                lambda r: r["cambiano"] == "no", sandwich_coerente],
        margini=[Margin(stat=res.tvalues[j], crit=Z), Margin(stat=rob.tvalues[j], crit=Z)],
        figure={"intervalli": figura})


@exercise("e05_04", modulo=5, livello=2,
          tipo=("eteroschedasticita-grafico-residui", "test-eteroschedasticita"))
def residui_quadrati_su_previsti(rng):
    """Read a narrowing funnel, test the squared residuals on the fitted values and use the fit."""
    n, y0 = 300, 50.0
    ore = rng.uniform(2, 40, n)
    media = rng.normal(24, 2.5, n)
    mu = 15 + 1.5 * ore + 1.2 * (media - 24)
    y = mu + np.clip(8 - 0.09 * mu, 1.0, None) * rng.normal(0, 1, n)
    res, X, tab = _fit(y, {"ore": ore, "media": media})
    previsti, e = res.fittedvalues, res.resid
    aux = sm.OLS(e ** 2, sm.add_constant(previsti)).fit()
    tab_aux = ols_table(aux, labels=["const", "y_pred"], stats=("n", "r2"))

    def answers(a, b, ratio):
        """Return every answer from the intercept, slope and t ratio of the auxiliary regression."""
        return {"cresce": "sì" if b > 0 else "no", "dec": _decide(ratio),
                "sd": Numero(np.sqrt(a + b * y0), 2), "robusti": "sì" if abs(ratio) > Z else "no",
                "a": Numero(a, 3), "b": Numero(b, 4), "t": Numero(ratio, 2),
                "var": Numero(a + b * y0, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of the auxiliary regression."""
        rows = tabelle["aus"].rows
        return answers(rows["const"]["coef"], rows["y_pred"]["coef"], rows["y_pred"]["t"])

    def figura_dati(path):
        """Draw the residuals against the fitted values."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        _residui(ax, es, previsti, e, "")
        ax.set_title("")
        es.save(fig, path)

    def figura(path):
        """Draw the squared residuals with the auxiliary line and its value at the chosen point."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.plot(previsti, e ** 2, "o", color=es.GRAY, ms=3, alpha=0.5)
        g = np.linspace(previsti.min(), previsti.max(), 50)
        ax.plot(g, aux.params[0] + aux.params[1] * g, color=es.BLUE, lw=1.8,
                label=r"$\hat a+\hat b\,\hat y$")
        ax.plot([y0], [aux.params[0] + aux.params[1] * y0], "o", color=es.RED, ms=7, zorder=5,
                label=f"valore stimato in {y0:g}".replace(".", ","))
        ax.set_xlabel(r"valori predetti $\hat y$")
        ax.set_ylabel(r"residui al quadrato $\hat\epsilon^2$")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    truth = answers(aux.params[0], aux.params[1], aux.tvalues[1])
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "y0": Numero(y0, 0)},
        tabelle={"ols": tab, "aus": tab_aux}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("cresce"), "b": Quesito("dec"), "c": Quesito("sd"),
                 "d": Quesito("robusti")},
        attese=[lambda r: r["cresce"] == "no", lambda r: r["dec"] == "rifiuta",
                lambda r: np.corrcoef(np.abs(e), previsti)[0, 1] < -0.3,
                lambda r: r["var"].valore > 1.0, lambda r: previsti.min() < y0 < previsti.max(),
                lambda r: abs(float(aux.predict([[1.0, y0]])[0]) - r["var"].valore) < 1e-2],
        margini=[Margin(stat=aux.tvalues[1], crit=Z)],
        figure={"residui": figura_dati, "ausiliaria": figura})


@exercise("e05_05", modulo=5, livello=2, tipo="test-eteroschedasticita")
def white_contro_breusch_pagan(rng):
    """Read two tests that disagree: Breusch-Pagan rejects homoskedasticity and White does not."""
    n = 250
    z = [rng.normal(0, 1, n) for _ in range(4)]
    # Variance linear in the first regressor only: White spends 14 d.f. on terms that add no power.
    sd = np.sqrt(np.clip(1 + 0.5 * z[0], 0.15, None))
    y = 10 + z[0] + 0.8 * z[1] - 0.6 * z[2] + 0.4 * z[3] + sd * rng.normal(0, 1, n)
    cols = {"istr": 13 + 2.5 * z[0], "esper": 12 + 7 * z[1], "ore": 38 + 5 * z[2],
            "anz": 8 + 5 * z[3]}
    res, X, _ = _fit(y, cols)
    bp, wh = _lm_test(res.resid, cols), _lm_test(res.resid, cols, white=True)
    p_bp, p_w = _p_stampato(bp.p), _p_stampato(wh.p)

    def studente(_tabelle):
        """Return the answers read from the two printed tests."""
        return truth

    def coerente_con_statsmodels(_risposte):
        """Check both statistics and their degrees of freedom against statsmodels."""
        return (abs(het_breuschpagan(res.resid, X)[0] - bp.lm) < 1e-8
                and abs(het_white(res.resid, X)[0] - wh.lm) < 1e-8 and bp.gl == 4 and wh.gl == 14)

    def figura(path):
        """Draw the two statistics against the rejection region of their chi-square distributions."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 3.4))
        for ax, t, nome in ((a1, bp, "Breusch-Pagan"), (a2, wh, "White")):
            es.dist_test("chi2", t.gl, stat=t.lm, crit=float(stats.chi2.ppf(1 - ALFA, t.gl)),
                         tail="right", ax=ax, title=nome)
            ax.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.28))
        fig.subplots_adjust(wspace=0.2, bottom=0.34)
        es.save(fig, path)

    truth = {"dec_bp": _decide_p(p_bp), "dec_w": _decide_p(p_w), "accetta": "no",
             "robusti": "sì", "p_bp": fmt_p(bp.p), "p_w": fmt_p(wh.p),
             "gl_bp": Numero(bp.gl, 0), "gl_w": Numero(wh.gl, 0)}
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)},
        tabelle={"bp": _blocco("Test di Breusch-Pagan", bp.lm, bp.gl, bp.p),
                 "white": _blocco("Test di White", wh.lm, wh.gl, wh.p)},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_bp"), "b": Quesito("dec_w"), "c": Quesito("accetta"),
                 "d": Quesito("robusti")},
        attese=[lambda r: r["dec_bp"] == "rifiuta", lambda r: r["dec_w"] == "non rifiuta",
                coerente_con_statsmodels],
        margini=[Margin(stat=p_bp, crit=ALFA, rel=MARGINE_P),
                 Margin(stat=p_w, crit=ALFA, rel=MARGINE_P)],
        figure={"test": figura})


def _monte_carlo(x, e, beta):
    """Estimate the slope of ``y = 1 + beta x + e`` in every sample and summarise the estimates.

    Args:
        x: Regressor, one sample per row.
        e: Errors, same shape as ``x``.
        beta: True slope, which the t ratios are centred on.

    Returns:
        A namespace with the slopes ``b``, the usual and HC1 standard errors ``se_u`` and
        ``se_r`` per sample, the summaries ``media``, ``dev``, ``mcse``, ``mse_u``, ``mse_r``,
        and the percentage of samples in which each t ratio rejects the true ``beta``
        (``rif_u``, ``rif_r``).
    """
    reps, n = x.shape
    y = 1.0 + beta * x + e
    xc = x - x.mean(axis=1, keepdims=True)
    sxx = np.sum(xc ** 2, axis=1)
    b = np.sum(xc * y, axis=1) / sxx
    res = y - y.mean(axis=1, keepdims=True) - b[:, None] * xc
    se_u = np.sqrt(np.sum(res ** 2, axis=1) / (n - 2) / sxx)
    se_r = np.sqrt(n / (n - 2) * np.sum(xc ** 2 * res ** 2, axis=1)) / sxx
    return SimpleNamespace(
        b=b, se_u=se_u, se_r=se_r, media=b.mean(), dev=b.std(ddof=1),
        mcse=b.std(ddof=1) / np.sqrt(reps), mse_u=se_u.mean(), mse_r=se_r.mean(),
        rif_u=100 * np.mean(np.abs((b - beta) / se_u) > Z),
        rif_r=100 * np.mean(np.abs((b - beta) / se_r) > Z))


def _tabella(intestazioni, righe):
    """Render a Markdown pipe table from header cells and ``(label, cells)`` rows."""
    out = ["| | " + " | ".join(intestazioni) + " |", "|---|" + "---|" * len(intestazioni)]
    out += [f"| {etichetta} | " + " | ".join(celle) + " |" for etichetta, celle in righe]
    return "\n".join(out)


def _celle(valori, decimali):
    """Return the cells of a row at the printed precision, and the values the student reads back."""
    testi = [f"{v:.{decimali}f}" for v in valori]
    return [t.replace(".", ",") for t in testi], [float(t) for t in testi]


@exercise("e05_06", modulo=5, livello=2, tipo="eteroschedasticita-implicazioni")
def consistenza_con_eteroschedasticita(rng):
    """Read a Monte Carlo of OLS under heteroskedasticity: unbiased, but the usual errors never converge."""
    reps, beta, tol, dimensioni = 6000, 2.0, 1.5, (50, 200, 800)
    sim = []
    for n in dimensioni:
        x = rng.normal(0, 1, (reps, n))
        sim.append(_monte_carlo(x, np.abs(x) * rng.normal(0, 1, (reps, n)), beta))
    spec = [("media delle stime di $\\beta_1$", "media", 3),
            ("deviazione standard delle stime", "dev", 5),
            ("errore di simulazione della media", "mcse", 5),
            ("media dell'errore standard usuale", "mse_u", 5),
            ("media dell'errore standard robusto (HC1)", "mse_r", 5),
            ("rifiuti di $H_0$ vera con il $t$ usuale (\\%)", "rif_u", 1),
            ("rifiuti di $H_0$ vera con il $t$ robusto (\\%)", "rif_r", 1)]
    righe, letti = [], {}
    for etichetta, campo, dec in spec:
        celle, valori = _celle([getattr(s, campo) for s in sim], dec)
        righe.append((etichetta, celle))
        letti[campo] = valori
    tab = _tabella([f"$n={m}$" for m in dimensioni], righe)

    def answers(v):
        """Return every answer from the printed values of the table."""
        z = [abs(m - beta) / s for m, s in zip(v["media"], v["mcse"])]
        return {"distorto": "sì" if max(z) > 2 else "no",
                "rapporto": Numero(v["dev"][2] / v["mse_u"][2], 2),
                "usuali_ok": "sì" if abs(v["rif_u"][2] - 5) <= tol else "no",
                "robusti_ok": "sì" if abs(v["rif_r"][2] - 5) <= tol else "no",
                "teorico": Numero(np.sqrt(3.0), 2), "z_max": Numero(max(z), 2),
                "rif_u": Numero(v["rif_u"][2], 1), "rif_r": Numero(v["rif_r"][2], 1),
                "media": Numero(v["media"][2], 3), "dev": Numero(v["dev"][2], 5),
                "mse_u": Numero(v["mse_u"][2], 5)}

    def studente(_tabelle):
        """Rebuild the answers from the values printed in the table."""
        return answers(letti)

    def sandwich_coerente(_risposte):
        """Check the closed-form HC1 error of the simulation against the matrix sandwich of statsmodels."""
        x0 = np.random.default_rng(0).normal(0, 1, (2, 60))
        e0 = np.abs(x0) * np.random.default_rng(1).normal(0, 1, (2, 60))
        sample = _monte_carlo(x0, e0, beta)
        y0 = 1.0 + beta * x0[0] + e0[0]
        robusto = sm.OLS(y0, sm.add_constant(x0[0])).fit(cov_type="HC1").bse[1]
        usuale = sm.OLS(y0, sm.add_constant(x0[0])).fit().bse[1]
        return abs(sample.se_r[0] - robusto) < 1e-12 and abs(sample.se_u[0] - usuale) < 1e-12

    def figura(path):
        """Draw the rejection frequency of the true null for both t ratios against the sample size."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.9))
        ax.plot(dimensioni, [s.rif_u for s in sim], "o-", color=es.RED, lw=1.6,
                label="errori standard usuali")
        ax.plot(dimensioni, [s.rif_r for s in sim], "o-", color=es.BLUE, lw=1.6,
                label="errori standard robusti")
        ax.axhline(100 * ALFA, color=es.GRAY, ls="--", lw=1.0)
        ax.set_xscale("log")
        ax.set_xticks(dimensioni, [str(m) for m in dimensioni])
        ax.minorticks_off()
        ax.set_xlabel("numerosità campionaria $n$")
        ax.set_ylabel("rifiuti della $H_0$ vera (%)")
        es.commas(ax, "y")
        ax.legend(loc="center right")
        es.save(fig, path)

    truth = answers(letti)
    return Draft(
        dati=None,
        parametri={"R": Numero(reps, 0), "beta": Numero(beta, 0), "tol": Numero(tol, 1),
                   "n1": Numero(dimensioni[0], 0), "n2": Numero(dimensioni[1], 0),
                   "n3": Numero(dimensioni[2], 0)},
        tabelle={"mc": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("distorto"), "b": Quesito("rapporto"), "c": Quesito("usuali_ok"),
                 "d": Quesito("robusti_ok")},
        attese=[lambda r: r["distorto"] == "no", lambda r: r["usuali_ok"] == "no",
                lambda r: r["robusti_ok"] == "sì",
                lambda r: abs(r["rapporto"].valore - r["teorico"].valore) < 0.1,
                lambda r: r["z_max"].valore < 1.7, sandwich_coerente],
        margini=[Margin(stat=truth["z_max"].valore, crit=2.0),
                 Margin(stat=letti["rif_r"][2] - 5, crit=tol),
                 Margin(stat=letti["rif_u"][2] - 5, crit=tol)],
        figure={"frequenze": figura})


@exercise("e05_07", modulo=5, livello=2, tipo="errori-standard-robusti")
def errori_robusti_piu_piccoli(rng):
    """Show robust errors smaller than the usual ones, which turns a coefficient significant."""
    n = 200
    z1, z2 = rng.normal(0, 1, n), rng.normal(0, 1, n)
    irrig = rng.integers(0, 2, n).astype(float)
    # Large errors sit where the temperature gap is small, i.e. where r^2 is small, so HC1 shrinks the error.
    sd = 0.3 + 3.0 * np.exp(-z2 ** 2)
    y = 50 + z1 + 0.1 * z2 + 0.5 * irrig + sd * rng.normal(0, 1, n)
    cols = {"azoto": 120 + 25 * z1, "scarto": 4 * z2, "irrig": irrig}
    res, X, tab = _fit(y, cols)
    rob, tab_rob = _fit_robusto(y, X, list(cols))
    j = 2

    def answers(naive, robusta):
        """Return every answer from the printed ``scarto`` rows of the two tables."""
        return {"fattore": Numero(robusta["se"] / naive["se"], 2),
                "dec_usuale": _decide(naive["t"]), "dec_robusto": _decide(robusta["t"]),
                "ic_lo": Numero(robusta["coef"] - Z * robusta["se"], 4),
                "ic_hi": Numero(robusta["coef"] + Z * robusta["se"], 4),
                "b": Numero(naive["coef"], 4), "se_usuale": Numero(naive["se"], 4),
                "se_robusto": Numero(robusta["se"], 4), "t_usuale": Numero(naive["t"], 2),
                "t_robusto": Numero(robusta["t"], 2)}

    def studente(tabelle):
        """Rebuild the answers from the ``scarto`` row of both printed tables."""
        return answers(tabelle["ols"].rows["scarto"], tabelle["rob"].rows["scarto"])

    def riga(fit):
        """Return the ``scarto`` row of a fit as the dictionary the table parser would give."""
        return {"coef": fit.params[j], "se": fit.bse[j], "t": fit.tvalues[j]}

    def sandwich_coerente(_risposte):
        """Check the printed robust error against the coefficient-by-coefficient sandwich formula."""
        return abs(np.sqrt(_varianza_white(X, res.resid, j)) - rob.bse[j]) < 1e-12

    def figura(path):
        """Draw the residuals against the temperature gap, and the two intervals of its coefficient."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1, 1.1]})
        a1.plot(cols["scarto"], res.resid, "o", color=es.BLUE, ms=3, alpha=0.5)
        a1.axhline(0, color=es.RED, lw=1.0)
        a1.set_xlabel("scarto")
        a1.set_ylabel(r"residui $\hat\epsilon$")
        es.commas(a1)
        _intervalli(a2, es, [(1, res.params[j], res.bse[j], "usuali", es.RED),
                             (0, rob.params[j], rob.bse[j], "robusti", es.BLUE)],
                    "coefficiente di scarto", ancora=-0.25)
        fig.subplots_adjust(wspace=0.25)
        es.save(fig, path)

    truth = answers(riga(res), riga(rob))
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"ols": tab, "rob": tab_rob},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("fattore"), "b": Quesito("dec_usuale"),
                 "c": Quesito("dec_robusto"), "d": Quesito("ic_lo")},
        attese=[lambda r: r["dec_usuale"] == "non rifiuta", lambda r: r["dec_robusto"] == "rifiuta",
                lambda r: r["fattore"].valore < 0.8, lambda r: r["ic_lo"].valore > 0.002,
                sandwich_coerente],
        margini=[Margin(stat=res.tvalues[j], crit=Z), Margin(stat=rob.tvalues[j], crit=Z)],
        figure={"scarto": figura})


@exercise("e05_08", modulo=5, livello=3, punti=4,
          tipo=("eteroschedasticita-grafico-residui", "test-eteroschedasticita",
                "eteroschedasticita-implicazioni", "errori-standard-robusti"))
def grafico_pulito_test_rifiuta(rng):
    """Combine a homogeneous residual plot with a rejecting Breusch-Pagan test and robust errors."""
    n = 300
    cap = rng.normal(50, 10, n)
    z2, z3 = rng.normal(0, 1, n), rng.normal(0, 1, n)
    # The variance moves with one weak regressor, which barely moves the fitted values.
    sd = 3.0 * np.exp(0.45 * z2)
    y = 20 + 1.5 * cap + 1.0 * z2 + 0.5 * z3 + sd * rng.normal(0, 1, n)
    cols = {"capitale": cap, "formazione": 20 + 5 * z2, "anzianita": 10 + 4 * z3}
    res, X, tab = _fit(y, cols)
    rob, tab_rob = _fit_robusto(y, X, list(cols))
    bp = _lm_test(res.resid, cols)
    p_bp = _p_stampato(bp.p)
    previsti, e = res.fittedvalues, res.resid
    p_previsti = sm.OLS(e ** 2, sm.add_constant(previsti)).fit().pvalues[1]
    j = 2

    def answers(riga_rob):
        """Return every answer from the printed p-value and the robust row of ``formazione``."""
        return {"coerente": "sì" if p_previsti > ALFA else "no", "dec_bp": _decide_p(p_bp),
                "basta": "no", "t_rob": Numero(riga_rob["t"], 2),
                "dec_rob": _decide(riga_rob["t"]), "p_bp": fmt_p(bp.p),
                "b": Numero(riga_rob["coef"], 4), "se_rob": Numero(riga_rob["se"], 4)}

    def studente(tabelle):
        """Rebuild the answers from the robust row of ``formazione``."""
        return answers(tabelle["rob"].rows["formazione"])

    def sandwich_coerente(_risposte):
        """Check the printed robust error against the coefficient-by-coefficient sandwich formula."""
        return abs(np.sqrt(_varianza_white(X, e, j)) - rob.bse[j]) < 1e-12

    def figura_dati(path):
        """Draw the residuals against the fitted values."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        _residui(ax, es, previsti, e, "")
        es.save(fig, path)

    def figura(path):
        """Draw the residuals against the fitted values and against the regressor that drives the variance."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), sharey=True)
        a1.plot(previsti, e, "o", color=es.BLUE, ms=3, alpha=0.5)
        a2.plot(cols["formazione"], e, "o", color=es.RED, ms=3, alpha=0.5)
        for ax, nome in ((a1, r"valori predetti $\hat y$"), (a2, "formazione")):
            ax.axhline(0, color=es.GRAY, lw=0.8)
            ax.set_xlabel(nome)
            es.commas(ax)
        a1.set_ylabel(r"residui $\hat\epsilon$")
        fig.subplots_adjust(wspace=0.08)
        es.save(fig, path)

    truth = answers({"coef": rob.params[j], "se": rob.bse[j], "t": rob.tvalues[j]})
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)},
        tabelle={"ols": tab, "rob": tab_rob,
                 "bp": _blocco("Test di Breusch-Pagan", bp.lm, bp.gl, bp.p)},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("coerente"), "b": Quesito("dec_bp"), "c": Quesito("basta"),
                 "d": Quesito("t_rob"), "e": Quesito("dec_rob")},
        attese=[lambda r: r["coerente"] == "sì", lambda r: r["dec_bp"] == "rifiuta",
                lambda r: r["dec_rob"] == "rifiuta",
                lambda r: abs(np.corrcoef(np.abs(e), previsti)[0, 1]) < 0.1,
                lambda r: bp.p < 1e-6, sandwich_coerente],
        margini=[Margin(stat=p_previsti, crit=ALFA, rel=MARGINE_P),
                 Margin(stat=p_bp, crit=ALFA, rel=MARGINE_P), Margin(stat=rob.tvalues[j], crit=Z)],
        figure={"residui": figura_dati, "confronto": figura})


def _wald_f(cov, params, restr):
    """Return the F statistic W/q of ``restr @ beta = 0`` from a covariance matrix of the estimates."""
    scarto = restr @ params
    return float(scarto @ np.linalg.solve(restr @ cov @ restr.T, scarto) / restr.shape[0])


@exercise("e05_09", modulo=5, livello=3, punti=4,
          tipo=("test-eteroschedasticita", "errori-standard-robusti"))
def f_usuale_contro_f_robusta(rng):
    """Test two coefficients jointly with the usual F and the robust F, which disagree."""
    n, q = 200, 2
    z = [rng.normal(0, 1, n) for _ in range(3)]
    sd = 0.3 * np.exp(0.5 * np.abs(z[1]) + 0.5 * np.abs(z[2]))
    y = 1 + z[0] + 0.22 * z[1] + 0.22 * z[2] + sd * rng.normal(0, 1, n)
    cols = {"capitale": 40 + 8 * z[0], "formazione": 20 + 5 * z[1], "ricerca": 10 + 4 * z[2]}
    res, X, tab = _fit(y, cols)
    rid, _, tab_rid = _fit(y, {"capitale": cols["capitale"]})
    wh = _lm_test(res.resid, cols, white=True)
    p_w = _p_stampato(wh.p)
    gl = n - X.shape[1]
    crit = float(stats.f.ppf(1 - ALFA, q, gl))
    crit_stampato = float(f"{crit:.3f}")
    restr = np.array([[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
    f_rob = _wald_f(_sandwich(X, res.resid), res.params, restr)
    f_rob_stampato = float(fmt_sig(f_rob, 5).replace(",", "."))
    p_rob = float(stats.f.sf(f_rob, q, gl))
    blocco_f = (f"**Test $F$ con errori standard robusti (HC1)** per $H_0:\\beta_2=\\beta_3=0$: "
                f"$F({q},\\,{gl}) = {fmt_sig(f_rob, 5).replace(',', '{,}')}$, "
                f"p-value = {fmt_p(p_rob)}.")

    def answers(ssr_u, ssr_r, n_oss, f_stampato):
        """Return every answer from the two printed SSR, the sample size and the printed robust F."""
        f_us = (ssr_r - ssr_u) / q / (ssr_u / (n_oss - X.shape[1]))
        return {"dec_w": _decide_p(p_w), "F": Numero(f_us, 2),
                "dec_f": "rifiuta" if f_us > crit_stampato else "non rifiuta",
                "dec_f_rob": "rifiuta" if f_stampato > crit_stampato else "non rifiuta",
                "cambia": "sì" if (f_us > crit_stampato) != (f_stampato > crit_stampato) else "no",
                "p_w": fmt_p(wh.p), "ssr_u": Numero(ssr_u, 3), "ssr_r": Numero(ssr_r, 3)}

    def studente(tabelle):
        """Rebuild the answers from the two printed SSR and the printed robust F."""
        return answers(tabelle["ols"].stats["ssr"], tabelle["rid"].stats["ssr"],
                       tabelle["ols"].stats["n"], f_rob_stampato)

    def wald_coerente(_risposte):
        """Check the robust F against statsmodels and the usual F against its SSR form."""
        rob = sm.OLS(y, X).fit(cov_type="HC1", use_t=True)
        usuale = res.f_test(restr)
        return (abs(float(rob.f_test(restr).fvalue) - f_rob) < 1e-8
                and abs(float(usuale.fvalue) - truth["F"].valore) < 1e-8
                and abs(float(stats.f.sf(float(usuale.fvalue), q, gl)) - usuale.pvalue) < 1e-12)

    def figura(path):
        """Draw the usual and the robust F against the 5% critical value."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 3.4))
        for ax, stat, nome in ((a1, truth["F"].valore, "F usuale"), (a2, f_rob, "F robusta")):
            es.dist_test("F", (q, gl), stat=stat, crit=crit, tail="right", ax=ax, title=nome)
            ax.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.28))
        fig.subplots_adjust(wspace=0.2, bottom=0.34)
        es.save(fig, path)

    truth = answers(res.ssr, rid.ssr, n, f_rob_stampato)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "q": Numero(q, 0), "gl": Numero(gl, 0),
                   "crit": Numero(crit, 3), "F_rob": Numero(f_rob_stampato, 2)},
        tabelle={"ols": tab, "rid": tab_rid,
                 "white": _blocco("Test di White", wh.lm, wh.gl, wh.p), "frob": blocco_f},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_w"), "b": Quesito("F"), "c": Quesito("dec_f"),
                 "d": Quesito("dec_f_rob"), "e": Quesito("cambia")},
        attese=[lambda r: r["dec_w"] == "rifiuta", lambda r: r["dec_f"] == "rifiuta",
                lambda r: r["dec_f_rob"] == "non rifiuta", lambda r: r["cambia"] == "sì",
                wald_coerente],
        margini=[Margin(stat=p_w, crit=ALFA, rel=MARGINE_P),
                 Margin(stat=truth["F"].valore, crit=crit_stampato),
                 Margin(stat=f_rob_stampato, crit=crit_stampato)],
        figure={"f": figura})


@exercise("e05_10", modulo=5, livello=3, punti=4,
          tipo=("eteroschedasticita-implicazioni", "errori-standard-robusti"))
def eteroschedasticita_non_e_endogeneita(rng):
    """Separate heteroskedasticity from an error correlated with the regressor, in a Monte Carlo."""
    reps, n, beta, tol, rho, gamma = 5000, 200, 2.0, 1.5, 0.5, 0.3
    x_i = rng.normal(0, 1, (reps, n))
    e_i = rng.normal(0, 1, (reps, n))
    x_ii = rng.normal(0, 1, (reps, n))
    e_ii = np.abs(x_ii) * rng.normal(0, 1, (reps, n))
    w = rng.normal(0, 1, (reps, n))
    x_iii = rho * w + np.sqrt(1 - rho ** 2) * rng.normal(0, 1, (reps, n))
    e_iii = gamma * w + np.sqrt(1 - gamma ** 2) * rng.normal(0, 1, (reps, n))
    sim = [_monte_carlo(x_i, e_i, beta), _monte_carlo(x_ii, e_ii, beta),
           _monte_carlo(x_iii, e_iii, beta)]
    spec = [("media delle stime di $\\beta_1$", "media", 3),
            ("deviazione standard delle stime", "dev", 5),
            ("errore di simulazione della media", "mcse", 5),
            ("media dell'errore standard usuale", "mse_u", 5),
            ("media dell'errore standard robusto (HC1)", "mse_r", 5),
            ("rifiuti di $H_0:\\beta_1=\\beta_1^{\\text{vero}}$ con il $t$ usuale (\\%)", "rif_u", 1),
            ("rifiuti di $H_0:\\beta_1=\\beta_1^{\\text{vero}}$ con il $t$ robusto (\\%)", "rif_r", 1)]
    righe, letti = [], {}
    for etichetta, campo, dec in spec:
        celle, valori = _celle([getattr(s, campo) for s in sim], dec)
        righe.append((etichetta, celle))
        letti[campo] = valori
    tab = _tabella(["scenario I", "scenario II", "scenario III"], righe)
    xs = rng.normal(0, 1, n)
    ys = 1.0 + beta * xs + np.abs(xs) * rng.normal(0, 1, n)
    res_s, _, _ = _fit(ys, {"x": xs})
    wh = _lm_test(res_s.resid, {"x": xs}, white=True)
    p_w = _p_stampato(wh.p)

    def answers(v):
        """Return every answer from the printed table and the printed White p-value."""
        z2 = abs(v["media"][1] - beta) / v["mcse"][1]
        return {"distorto": "sì" if z2 > 2 else "no",
                "distorsione": Numero(v["media"][2] - beta, 3),
                "bias_se": Numero((v["media"][2] - beta) / v["dev"][2], 1),
                "risolvono": "sì" if abs(v["rif_r"][2] - 5) <= tol else "no",
                "esogeno": "no", "z_ii": Numero(z2, 2), "p_w": fmt_p(wh.p),
                "rif_u_ii": Numero(v["rif_u"][1], 1), "rif_r_ii": Numero(v["rif_r"][1], 1),
                "rif_r_iii": Numero(v["rif_r"][2], 1), "rif_u_iii": Numero(v["rif_u"][2], 1),
                "teorica": Numero(rho * gamma, 2)}

    def studente(_tabelle):
        """Rebuild the answers from the values printed in the table."""
        return answers(letti)

    def teoria_coerente(_risposte):
        """Check that the bias is Cov(x, e) / Var(x) = rho * gamma and that II shows no bias beyond noise."""
        return (abs(sim[2].media - beta - rho * gamma) < 4 * sim[2].mcse
                and abs(sim[1].media - beta) < 4 * sim[1].mcse)

    def figura(path):
        """Draw the average bias and the robust rejection frequency of the true null by scenario."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.8))
        nomi = ["I", "II", "III"]
        a1.bar(nomi, [s.media - beta for s in sim], color=[es.BLUE, es.BLUE, es.RED])
        a1.set_xlabel("scenario")
        a1.set_ylabel(r"media delle stime meno $\beta_1$")
        a2.bar(nomi, [s.rif_r for s in sim], color=[es.BLUE, es.BLUE, es.RED])
        a2.axhline(100 * ALFA, color=es.GRAY, ls="--", lw=1.0)
        a2.set_xlabel("scenario")
        a2.set_ylabel("rifiuti della $H_0$ vera, $t$ robusto (%)")
        for ax in (a1, a2):
            es.commas(ax, "y")
        fig.subplots_adjust(wspace=0.35)
        es.save(fig, path)

    truth = answers(letti)
    return Draft(
        dati=None,
        parametri={"R": Numero(reps, 0), "n": Numero(n, 0), "beta": Numero(beta, 0),
                   "tol": Numero(tol, 1), "rho": Numero(rho, 1), "gamma": Numero(gamma, 1),
                   "gl_w": Numero(wh.gl, 0)},
        tabelle={"mc": tab, "white": _blocco("Test di White", wh.lm, wh.gl, wh.p)},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("distorto"), "b": Quesito("distorsione"),
                 "c": Quesito("risolvono"), "d": Quesito("esogeno")},
        attese=[lambda r: r["distorto"] == "no", lambda r: r["risolvono"] == "no",
                lambda r: r["distorsione"].valore > 0.1, lambda r: wh.p < 0.01, teoria_coerente],
        margini=[Margin(stat=truth["z_ii"].valore, crit=2.0),
                 Margin(stat=letti["rif_r"][2] - 5, crit=tol),
                 Margin(stat=p_w, crit=ALFA, rel=MARGINE_P)],
        figure={"scenari": figura})
