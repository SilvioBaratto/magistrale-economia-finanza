"""Module 03 - multiple regression: log models, quadratics, collinearity, omitted variables."""

from types import SimpleNamespace

import numpy as np
import statsmodels.api as sm

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import ols_table, parse_vif, vif_table

TITOLO = "Regressione multipla"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

# VIF above which the exam solutions diagnose quasi-collinearity.
SOGLIA_VIF = 10.0


def _fit(y, columns):
    """Fit OLS of ``y`` on a constant and the named columns; return the result and its table."""
    names = list(columns)
    X = sm.add_constant(np.column_stack([columns[k] for k in names]))
    res = sm.OLS(y, X).fit()
    return res, ols_table(res, labels=["const", *names])


def _decide(t):
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


def _pulita(res, eps=1e-9):
    """Return ``res`` with numerically null coefficients printed as exact zeros.

    The constant of a regression on residuals is rounding noise that changes from
    one machine to the next, so a rebuilt table would never be the same twice.
    """
    params = np.where(np.abs(res.params) < eps, 0.0, res.params)
    return SimpleNamespace(
        params=params, bse=res.bse, tvalues=params / res.bse,
        pvalues=np.where(params == 0.0, 1.0, res.pvalues), nobs=res.nobs,
        rsquared=res.rsquared, ssr=res.ssr)


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _intervalli(ax, es, voci, xlabel, colonne=2, ancora=-0.5):
    """Draw one 95% interval per entry of ``voci`` = (height, coefficient, se, label, colour)."""
    for altezza, coef, err, etichetta, colore in voci:
        ax.errorbar(coef, altezza, xerr=Z * err, fmt="o", color=colore, capsize=4,
                    label=etichetta)
    ax.set_yticks([])
    ax.set_ylim(-0.6, max(v[0] for v in voci) + 0.6)
    ax.set_xlabel(xlabel)
    es.commas(ax, "x")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, ancora), ncol=colonne)


@exercise("e03_01", modulo=3, livello=1, tipo="variazione-percentuale-log-livello")
def rendimento_istruzione(rng):
    """Read a log-level coefficient as a percentage change and test its significance."""
    n = 400
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(0, 31, n).astype(float)
    y = 1.15 + 0.075 * istr + 0.012 * esper + rng.normal(0, 0.4, n)
    res, tab = _fit(y, {"istr": istr, "esper": esper})
    b, se, t = res.params[1], res.bse[1], res.tvalues[1]

    def answers(coef, err, ratio):
        """Return every answer from a coefficient, its standard error and its t ratio."""
        return {"beta": Numero(coef, 4), "pct": Numero(100 * coef, 1), "t": Numero(ratio, 2),
                "dec": _decide(ratio), "ic_lo": Numero(coef - Z * err, 4),
                "ic_hi": Numero(coef + Z * err, 4)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``istr``."""
        r = tabelle["ols"].rows["istr"]
        return answers(r["coef"], r["se"], r["t"])

    def figura(path):
        """Draw the 95% interval of the coefficient against H0: beta = 0."""
        es = figs.use_style()
        fig, _ = es.ci_line(b, b - Z * se, b + Z * se, h0=0.0, decimals=4,
                            xlabel=r"$\beta_1$ (istruzione)")
        es.save(fig, path)

    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"ols": tab},
        risposte=answers(b, se, t), studente=studente,
        quesiti={"a": Quesito("pct"), "b": Quesito("dec")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: 5 < r["pct"].valore < 10],
        margini=[Margin(stat=t, crit=Z)], figure={"ic": figura})


@exercise("e03_02", modulo=3, livello=1, tipo="elasticita-log-log")
def elasticita_inquinamento(rng):
    """Read a log-log coefficient as an elasticity and apply it to a percentage change."""
    n, var = 400, 5.0
    nox = rng.lognormal(1.7, 0.35, n)
    dist = rng.lognormal(1.2, 0.5, n)
    y = 10.4 - 0.45 * np.log(nox) - 0.20 * np.log(dist) + rng.normal(0, 0.25, n)
    res, tab = _fit(y, {"l_nox": np.log(nox), "l_dist": np.log(dist)})
    b, se, t = res.params[1], res.bse[1], res.tvalues[1]

    def answers(coef, err, ratio):
        """Return every answer from the elasticity, its standard error and its t ratio."""
        return {"el": Numero(coef, 3), "pct": Numero(var * coef, 2), "t": Numero(ratio, 2),
                "dec": _decide(ratio), "ic_lo": Numero(coef - Z * err, 3),
                "ic_hi": Numero(coef + Z * err, 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``l_nox``."""
        r = tabelle["ols"].rows["l_nox"]
        return answers(r["coef"], r["se"], r["t"])

    def elasticita_coerente(_risposte):
        """Check that the elasticity is the slope of the fitted log price on log nox."""
        h = 0.01
        x = np.array([1.0, np.log(nox.mean()), np.log(dist.mean())])
        up = x + np.array([0.0, np.log(1 + h), 0.0])
        return abs((up - x) @ res.params / np.log(1 + h) - b) < 1e-9

    def figura(path):
        """Draw the price change implied by a change of nox, with the 95% band."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.9))
        s = np.linspace(-10, 10, 101)
        lo, hi = (b - Z * se) * s, (b + Z * se) * s
        ax.fill_between(s, np.minimum(lo, hi), np.maximum(lo, hi), color=es.BLUEBG,
                        label="intervallo di confidenza al 95%")
        ax.plot(s, b * s, color=es.BLUE, lw=1.6, label=r"$\hat\beta_1 \times$ variazione di nox")
        ax.plot([var], [b * var], "o", color=es.RED, ms=7, zorder=5)
        ax.annotate("variazione di nox: +" + f"{var:g}%\nprezzo: " + f"{b * var:.2f}%".replace(".", ","),
                    xy=(var, b * var), xytext=(8, 12), textcoords="offset points", ha="left",
                    fontsize=8.5, color=es.RED, fontweight="bold")
        ax.axhline(0, color=es.GRAY, lw=0.7)
        ax.set_xlabel("variazione percentuale di nox")
        ax.set_ylabel("variazione percentuale attesa del prezzo")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "var": Numero(var, 0)}, tabelle={"ols": tab},
        risposte=answers(b, se, t), studente=studente,
        quesiti={"a": Quesito("el"), "b": Quesito("pct"), "c": Quesito("dec")},
        attese=[lambda r: r["el"].valore < 0, lambda r: r["dec"] == "rifiuta",
                lambda r: -4 < r["pct"].valore < -1, elasticita_coerente],
        margini=[Margin(stat=t, crit=Z)], figure={"effetto": figura})


@exercise("e03_03", modulo=3, livello=1,
          tipo=("collinearita-diagnosi", "vif-inflazione-errore-standard"))
def vif_dalla_tabella(rng):
    """Read the VIF table, count the collinear regressors and turn a VIF into a standard-error factor."""
    n = 150
    red = np.clip(rng.gamma(12.0, 0.4, n), 0.5, 14.0)
    fam = rng.integers(1, 7, n).astype(float)
    eta = rng.integers(25, 71, n).astype(float)
    prop = rng.binomial(1, 0.6, n).astype(float)
    y = (6.0 + 0.12 * red - 0.008 * red**2 + 0.10 * fam + 0.004 * eta + 0.15 * prop
         + rng.normal(0, 0.6, n))
    cols = {"reddito": red, "sq_reddito": red**2, "famiglia": fam, "eta": eta, "proprieta": prop}
    res, tab = _fit(y, cols)
    vifs = _vif(cols)
    tab_vif = vif_table(vifs)
    j = list(cols).index("reddito") + 1

    def answers(vif, ratio):
        """Return every answer from the VIF of each regressor and the t ratio of ``reddito``."""
        alti = [k for k, v in vif.items() if v > SOGLIA_VIF]
        resto = max(v for k, v in vif.items() if k not in alti)
        return {"conta": Numero(float(len(alti)), 0),
                "fattore": Numero(np.sqrt(vif["reddito"]), 2),
                "dec": "sì" if "reddito" in alti and abs(ratio) < Z else "no",
                "vif": Numero(vif["reddito"], 3), "vif_sq": Numero(vif["sq_reddito"], 3),
                "resto": Numero(resto, 3), "t": Numero(ratio, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed VIF table and the printed row of ``reddito``."""
        return answers(parse_vif(tab_vif), tabelle["ols"].rows["reddito"]["t"])

    def identita_vif(_risposte):
        """Check that the variance of each coefficient is sigma^2 * VIF_j / SST_j, exactly."""
        s2 = res.ssr / res.df_resid
        return all(abs(res.bse[i + 1]**2 - s2 * vifs[k] / np.sum((cols[k] - cols[k].mean())**2)) < 1e-12
                   for i, k in enumerate(cols))

    def figura(path):
        """Draw each VIF against the threshold, and the factor it puts on the standard error."""
        es, plt = _stile()
        nomi = list(vifs)
        pos = np.arange(len(nomi))[::-1]
        valori = np.array([vifs[k] for k in nomi])
        colori = [es.RED if v > SOGLIA_VIF else es.BLUE for v in valori]
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.7), sharey=True)
        a1.barh(pos, valori, color=colori)
        a1.axvline(SOGLIA_VIF, color=es.GRAY, ls="--", lw=1.0)
        a1.set_xlabel("VIF (soglia tratteggiata)")
        a2.barh(pos, np.sqrt(valori), color=colori)
        a2.axvline(np.sqrt(SOGLIA_VIF), color=es.GRAY, ls="--", lw=1.0)
        a2.set_xlabel(r"$\sqrt{\mathrm{VIF}}$: volte l'errore standard")
        a1.set_yticks(pos, nomi)
        for ax in (a1, a2):
            es.commas(ax, "x")
        es.save(fig, path)

    truth = answers(vifs, res.tvalues[j])
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"ols": tab, "vif": tab_vif},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("conta"), "b": Quesito("fattore"), "c": Quesito("dec")},
        attese=[lambda r: r["conta"].valore == 2, lambda r: r["dec"] == "sì", identita_vif],
        margini=[Margin(stat=vifs["reddito"], crit=SOGLIA_VIF),
                 Margin(stat=vifs["sq_reddito"], crit=SOGLIA_VIF),
                 Margin(stat=truth["resto"].valore, crit=SOGLIA_VIF),
                 Margin(stat=res.tvalues[j], crit=Z)],
        figure={"vif": figura})


@exercise("e03_04", modulo=3, livello=2,
          tipo=("variazione-percentuale-log-livello", "unita-di-misura-e-scala"))
def salario_sposato(rng):
    """Invert a log-level effect, read a dummy as a percentage and convert it to dollars."""
    n, obiettivo, w0, rivendicato = 500, 15.0, 2000.0, 400.0
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(0, 31, n).astype(float)
    sposato = rng.binomial(1, 0.55, n).astype(float)
    y = 6.2 + 0.062 * istr + 0.016 * esper + 0.115 * sposato + rng.normal(0, 0.42, n)
    res, tab = _fit(y, {"istr": istr, "esper": esper, "sposato": sposato})
    b1, b3, s3 = res.params[1], res.params[3], res.bse[3]

    def answers(c1, c3, e3):
        """Return every answer from the schooling and marriage coefficients and the latter's se."""
        t_riv = (c3 - rivendicato / w0) / e3
        return {"anni": Numero(obiettivo / (100 * c1), 2), "pct": Numero(100 * c3, 1),
                "dollari": Numero(c3 * w0, 0), "dec": "no" if abs(t_riv) > Z else "sì",
                "t_riv": Numero(t_riv, 2), "ic_lo": Numero((c3 - Z * e3) * w0, 0),
                "ic_hi": Numero((c3 + Z * e3) * w0, 0), "b1": Numero(c1, 4), "b3": Numero(c3, 4),
                "se3": Numero(e3, 4), "beta_riv": Numero(rivendicato / w0, 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of ``istr`` and ``sposato``."""
        rows = tabelle["ols"].rows
        return answers(rows["istr"]["coef"], rows["sposato"]["coef"], rows["sposato"]["se"])

    def conversioni_coerenti(r):
        """Check the schooling inversion and the closeness of the dollar conversion."""
        esatto = w0 * (np.exp(b3) - 1)
        return (abs(b1 * r["anni"].valore - obiettivo / 100) < 1e-9
                and abs(esatto - r["dollari"].valore) < 0.06 * r["dollari"].valore)

    def figura(path):
        """Draw the schooling needed for the target, and the dollar interval against the claim."""
        es, plt = _stile()
        fig = plt.figure(figsize=(6.1, 4.0))
        grid = fig.add_gridspec(2, 1, height_ratios=[1.6, 1.0], hspace=0.55)
        ax = fig.add_subplot(grid[0])
        d = np.linspace(0, 6, 100)
        anni = obiettivo / (100 * b1)
        ax.plot(d, 100 * b1 * d, color=es.BLUE, lw=1.6, label=r"$100\,\hat\beta_1\,\Delta$istr")
        ax.axhline(obiettivo, color=es.RED, ls="--", lw=1.0)
        ax.plot([anni], [obiettivo], "o", color=es.RED, ms=7, zorder=5)
        ax.vlines(anni, 0, obiettivo, color=es.RED, ls=":", lw=1.0)
        ax.annotate(f"{anni:.2f} anni".replace(".", ","), xy=(anni, 0), xytext=(4, 6),
                    textcoords="offset points", fontsize=8.5, color=es.RED, fontweight="bold")
        ax.set_xlabel("anni di istruzione in più")
        ax.set_ylabel("variazione % del salario")
        es.commas(ax)
        ax.legend(loc="upper left")
        bx = fig.add_subplot(grid[1])
        es.ci_line(b3 * w0, (b3 - Z * s3) * w0, (b3 + Z * s3) * w0, h0=rivendicato, ax=bx,
                   decimals=0, xlabel="differenza attesa fra sposato e single, in dollari al mese")
        es.save(fig, path)

    truth = answers(b1, b3, s3)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "obiettivo": Numero(obiettivo, 0), "w0": Numero(w0, 0),
                   "riv": Numero(rivendicato, 0)},
        tabelle={"ols": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("anni"), "b": Quesito("pct"), "c": Quesito("dollari"),
                 "d": Quesito("dec")},
        attese=[lambda r: r["dec"] == "no", lambda r: 1 < r["anni"].valore < 5,
                lambda r: r["dollari"].valore > 0, conversioni_coerenti],
        margini=[Margin(stat=truth["t_riv"].valore, crit=Z)], figure={"effetto": figura})


@exercise("e03_05", modulo=3, livello=2,
          tipo=("effetto-livello-log", "unita-di-misura-e-scala"))
def ricchezza_reddito(rng):
    """Read a level-log coefficient in the units of the dependent variable and invert it."""
    n, var, ra, rb, scala, obiettivo = 350, 10.0, 25.0, 80.0, 1000.0, 2100.0
    red = rng.lognormal(3.7, 0.5, n)
    eta = rng.integers(25, 66, n).astype(float)
    y = -20.0 + 14.0 * np.log(red) + 0.45 * eta + rng.normal(0, 12.0, n)
    res, tab = _fit(y, {"l_red": np.log(red), "eta": eta})
    b, se, t = res.params[1], res.bse[1], res.tvalues[1]

    def answers(coef, err, ratio):
        """Return every answer from the log-income coefficient, its se and its t ratio."""
        return {"dollari": Numero(coef * var / 100 * scala, 0),
                "pct": Numero(100 * obiettivo / scala / coef, 1), "dec": _decide(ratio),
                "uguale": "sì", "t": Numero(ratio, 2), "beta": Numero(coef, 4),
                "migliaia": Numero(coef * var / 100, 3),
                "ic_lo": Numero(coef - Z * err, 3), "ic_hi": Numero(coef + Z * err, 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``l_red``."""
        r = tabelle["ols"].rows["l_red"]
        return answers(r["coef"], r["se"], r["t"])

    def fitted(x):
        """Return the fitted wealth at income ``x`` for a 45-year-old."""
        return res.params[0] + res.params[1] * np.log(x) + res.params[2] * 45.0

    def formula_coerente(_risposte):
        """Check that a p% rise of income adds beta*log(1+p), close to beta*p, at any income."""
        p = var / 100
        salti = [fitted(x * (1 + p)) - fitted(x) for x in (ra, rb)]
        uguali = abs(salti[0] - salti[1]) < 1e-9 and abs(salti[0] - b * np.log(1 + p)) < 1e-9
        return uguali and abs(salti[0] - b * p) < 0.05 * abs(b * p)

    def derivata_coerente(_risposte):
        """Check that the slope of the fitted wealth with respect to income is beta / income."""
        h = 1e-5
        return abs((fitted(ra + h) - fitted(ra - h)) / (2 * h) - b / ra) < 1e-7

    def figura(path):
        """Draw the fitted wealth: the same rise in dollars follows a 10% rise at any income."""
        es, plt = _stile()
        from matplotlib.ticker import NullFormatter

        fig, ax = plt.subplots(figsize=(6.1, 3.1))
        x = np.geomspace(10, 110, 200)
        ax.plot(x, fitted(x), color=es.BLUE, lw=1.6, label="ricchezza attesa")
        for x0, colore in ((ra, es.RED), (rb, es.GREEN)):
            fine = x0 * (1 + var / 100)
            ax.plot([x0, fine], [fitted(x0), fitted(fine)], "o-", color=colore, lw=2.6, ms=5,
                    label=f"reddito {x0:g} (+{var:g}%)")
        ax.set_xscale("log")
        ax.set_xticks([10, 20, 40, 80])
        ax.set_xticklabels(["10", "20", "40", "80"])
        ax.xaxis.set_minor_formatter(NullFormatter())
        ax.set_xlabel("reddito (migliaia di dollari, scala logaritmica)")
        ax.set_ylabel("ricchezza netta (migliaia di dollari)")
        es.commas(ax, "y")
        ax.legend(loc="lower right")
        es.save(fig, path)

    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "var": Numero(var, 0), "ra": Numero(ra, 0),
                   "rb": Numero(rb, 0), "scala": Numero(scala, 0),
                   "obiettivo": Numero(obiettivo, 0)},
        tabelle={"ols": tab}, risposte=answers(b, se, t), studente=studente,
        quesiti={"a": Quesito("dollari"), "b": Quesito("pct"), "c": Quesito("dec"),
                 "d": Quesito("uguale")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["dollari"].valore > 0,
                formula_coerente, derivata_coerente],
        margini=[Margin(stat=t, crit=Z)], figure={"curva": figura})


@exercise("e03_06", modulo=3, livello=2,
          tipo=("termine-quadratico-nonlinearita", "punto-di-svolta-quadratico"))
def esperienza_quadratica(rng):
    """Test a squared term, evaluate the marginal effect at a point and find its zero."""
    n, x0, istr0 = 500, 10.0, 12.0
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(0, 41, n).astype(float)
    y = 1.0 + 0.07 * istr + 0.045 * esper - 0.00085 * esper**2 + rng.normal(0, 0.4, n)
    res, tab = _fit(y, {"istr": istr, "esper": esper, "esper2": esper**2})
    b2, b3, t3 = res.params[2], res.params[3], res.tvalues[3]

    def answers(c2, c3, ratio):
        """Return every answer from the two experience coefficients and the squared term's t."""
        return {"b2": Numero(c2, 5), "b3": Numero(c3, 7), "t3": Numero(ratio, 2),
                "dec": _decide(ratio), "eff": Numero(100 * (c2 + 2 * c3 * x0), 2),
                "punto": Numero(-c2 / (2 * c3), 1)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of ``esper`` and ``esper2``."""
        rows = tabelle["ols"].rows
        return answers(rows["esper"]["coef"], rows["esper2"]["coef"], rows["esper2"]["t"])

    def derivata_coerente(_risposte):
        """Check that the marginal-effect formula matches a numeric derivative of the fitted curve."""
        h = 1e-4

        def fitted(x):
            """Return the fitted log wage at ``x`` years of experience and 12 of schooling."""
            return np.array([1.0, istr0, x, x * x]) @ res.params

        return abs((fitted(x0 + h) - fitted(x0 - h)) / (2 * h) - (b2 + 2 * b3 * x0)) < 1e-8

    def figura(path):
        """Draw the marginal effect of experience, positive until it crosses zero."""
        es = figs.use_style()
        fig, _, _ = es.quadratic_effect(b2, b3, xmax=40, varname="esper",
                                        ylabel="effetto marginale su log(salario)")
        es.save(fig, path)

    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "x0": Numero(x0, 0)}, tabelle={"ols": tab},
        risposte=answers(b2, b3, t3), studente=studente,
        quesiti={"a": Quesito("dec"), "b": Quesito("eff"), "c": Quesito("punto")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["eff"].valore > 0,
                lambda r: r["b3"].valore < 0, lambda r: 18 < r["punto"].valore < 40,
                derivata_coerente],
        margini=[Margin(stat=t3, crit=Z)], figure={"effetto": figura})


@exercise("e03_07", modulo=3, livello=2, tipo="endogeneita-variabile-omessa")
def ore_omesse(rng):
    """Show that an omitted variable uncorrelated with the regressor leaves it unbiased."""
    n = 450
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(0, 31, n).astype(float)
    ore = 40.0 - 0.08 * istr + rng.normal(0, 6, n)
    y = 0.9 + 0.07 * istr + 0.012 * esper + 0.014 * ore + rng.normal(0, 0.35, n)
    r1, tab1 = _fit(y, {"istr": istr, "esper": esper})
    r2, tab2 = _fit(y, {"istr": istr, "esper": esper, "ore": ore})
    ra, taba = _fit(ore, {"istr": istr, "esper": esper})

    def answers(b1_ristretto, b1_completo, b_ore, t_ore, delta, t_delta):
        """Return the change, the two tests and the verdict from six printed numbers."""
        return {"a": Numero(100 * (b1_ristretto - b1_completo), 2),
                "rilevante": _decide(t_ore), "correlata": _decide(t_delta),
                "dec": "sì" if abs(t_ore) > Z and abs(t_delta) > Z else "no",
                "c": Numero(100 * b_ore * delta, 2),
                "t_ore": Numero(t_ore, 2), "t_delta": Numero(t_delta, 2),
                "b_ore": Numero(b_ore, 4), "delta": Numero(delta, 4),
                "b1_ristretto": Numero(b1_ristretto, 4), "b1_completo": Numero(b1_completo, 4)}

    def studente(tabelle):
        """Rebuild the answers from the three printed tables."""
        m1, m2, aux = (tabelle[k].rows for k in ("m1", "m2", "aux"))
        return answers(m1["istr"]["coef"], m2["istr"]["coef"], m2["ore"]["coef"],
                       m2["ore"]["t"], aux["istr"]["coef"], aux["istr"]["t"])

    def figura(path):
        """Draw the interval of the schooling coefficient in the two models."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.2))
        _intervalli(ax, es, [(1, r1.params[1], r1.bse[1], "senza ore (Modello 1)", es.RED),
                             (0, r2.params[1], r2.bse[1], "con ore (Modello 2)", es.BLUE)],
                    "coefficiente di istruzione, con intervallo al 95%")
        es.save(fig, path)

    truth = answers(r1.params[1], r2.params[1], r2.params[3], r2.tvalues[3],
                    ra.params[1], ra.tvalues[1])

    def formula_esatta(r):
        """Check that the bias formula holds exactly: change in beta = beta_ore * delta."""
        return abs(r["a"].valore - r["c"].valore) < 1e-6

    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"m1": tab1, "m2": tab2, "aux": taba},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("a"), "b": Quesito("rilevante"), "c": Quesito("correlata"),
                 "d": Quesito("dec")},
        attese=[lambda r: r["dec"] == "no", lambda r: r["rilevante"] == "rifiuta",
                lambda r: r["correlata"] == "non rifiuta", formula_esatta],
        margini=[Margin(stat=r2.tvalues[3], crit=Z), Margin(stat=ra.tvalues[1], crit=Z)],
        figure={"confronto": figura})


@exercise("e03_08", modulo=3, livello=2, tipo="errore-di-misura-endogeneita")
def reddito_dichiarato(rng):
    """Quantify the attenuation caused by a regressor observed with error."""
    n, gamma, sx2, su2 = 300, 1.5, 4.0, 2.25
    x = rng.normal(10.0, np.sqrt(sx2), n)
    xs = x + rng.normal(0.0, np.sqrt(su2), n)
    y = 3.0 + gamma * x + rng.normal(0.0, 2.0, n)
    r1, tab1 = _fit(y, {"red": x})
    r2, tab2 = _fit(y, {"red_dich": xs})
    b, se = r2.params[1], r2.bse[1]
    lam = sx2 / (sx2 + su2)

    def answers(coef, err):
        """Return every answer from the attenuation factor and the coefficient on the noisy income."""
        fuori = abs(coef - gamma) > Z * err
        return {"lam": Numero(lam, 3), "limite": Numero(gamma * lam, 3),
                "cov": Numero(-gamma * su2, 3), "dec": "no" if fuori else "sì",
                "b": Numero(coef, 4), "ic_lo": Numero(coef - Z * err, 3),
                "ic_hi": Numero(coef + Z * err, 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``red_dich``."""
        r = tabelle["dich"].rows["red_dich"]
        return answers(r["coef"], r["se"])

    def limite_coerente(_risposte):
        """Check that a large simulation reproduces the limit of the slope and the covariance."""
        g = np.random.default_rng(1)
        m = 400_000
        xv = g.normal(10.0, np.sqrt(sx2), m)
        u = g.normal(0.0, np.sqrt(su2), m)
        e = g.normal(0.0, 2.0, m)
        proxy = xv + u
        pendenza = np.cov(proxy, 3.0 + gamma * xv + e)[0, 1] / np.var(proxy, ddof=1)
        return (abs(pendenza - gamma * lam) < 0.01
                and abs(np.cov(proxy, e - gamma * u)[0, 1] + gamma * su2) < 0.05)

    def figura(path):
        """Draw the data and the two fitted lines: the noisy regressor flattens the slope."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.2))
        k = slice(0, 120)
        ax.plot(x[k], y[k], "o", color=es.GRAY, ms=3, alpha=0.55, label="reddito vero")
        ax.plot(xs[k], y[k], "o", color=es.RED, ms=3, alpha=0.55, label="reddito dichiarato")
        g = np.linspace(min(x.min(), xs.min()), max(x.max(), xs.max()), 50)
        ax.plot(g, r1.params[0] + r1.params[1] * g, color=es.BLUE, lw=1.6,
                label="retta con il reddito vero")
        ax.plot(g, r2.params[0] + b * g, color=es.RED, lw=1.6, label="retta con il reddito dichiarato")
        ax.set_xlabel("reddito")
        ax.set_ylabel("consumi")
        es.commas(ax)
        ax.legend(loc="lower right")
        es.save(fig, path)

    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "gamma": Numero(gamma, 1), "sx2": Numero(sx2, 2),
                   "su2": Numero(su2, 2)},
        tabelle={"vero": tab1, "dich": tab2}, risposte=answers(b, se), studente=studente,
        quesiti={"a": Quesito("lam"), "b": Quesito("limite"), "c": Quesito("cov"),
                 "d": Quesito("dec")},
        attese=[lambda r: r["dec"] == "no", lambda r: r["b"].valore < gamma,
                lambda r: abs(r["b"].valore - r["limite"].valore) < abs(r["b"].valore - gamma),
                limite_coerente],
        margini=[Margin(stat=(b - gamma) / se, crit=Z)], figure={"rette": figura})


@exercise("e03_09", modulo=3, livello=2, tipo="frisch-waugh-lovell")
def classe_reddito_fwl(rng):
    """Recover a coefficient of the multiple regression from the three Frisch-Waugh-Lovell steps."""
    n = 420
    red = rng.gamma(4.0, 3.5, n)
    classe = 22.0 - 0.18 * red + rng.normal(0, 1.5, n)
    y = 640.0 - 0.30 * classe + 1.85 * red + rng.normal(0, 13.0, n)
    full, _ = _fit(y, {"classe": classe, "reddito": red})
    aux1, tab1 = _fit(classe, {"reddito": red})
    aux2, tab2 = _fit(y, {"reddito": red})
    u_classe, u_punt = aux1.resid, aux2.resid
    r3 = sm.OLS(u_punt, sm.add_constant(u_classe)).fit()
    tab3 = ols_table(_pulita(r3), labels=["const", "u_classe"])
    semplice = sm.OLS(y, sm.add_constant(classe)).fit()

    def answers(coef, ratio, err, r2):
        """Return every answer from the step-3 coefficient, t, se and the step-1 R-squared."""
        return {"beta": Numero(coef, 4), "dec": _decide(ratio), "vif": Numero(1 / (1 - r2), 2),
                "t": Numero(ratio, 2), "ic_lo": Numero(coef - Z * err, 3),
                "ic_hi": Numero(coef + Z * err, 3), "r2": Numero(r2, 4)}

    def studente(tabelle):
        """Rebuild the answers from the step-3 row and the step-1 R-squared."""
        r = tabelle["passo3"].rows["u_classe"]
        return answers(r["coef"], r["t"], r["se"], tabelle["passo1"].stats["r2"])

    def coincide(_risposte):
        """Check that step 3 gives the multiple-regression slope and differs only in the d.f."""
        uguale = abs(r3.params[1] - full.params[1]) < 1e-9
        gradi = abs(full.bse[1] / r3.bse[1] - np.sqrt((n - 2) / (n - 3))) < 1e-9
        stessa_decisione = _decide(full.tvalues[1]) == _decide(r3.tvalues[1])
        return uguale and gradi and stessa_decisione

    def figura(path):
        """Draw the raw scatter against the scatter of the residuals, with their fitted slopes."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9))
        a1.plot(classe, y, "o", color=es.GRAY, ms=2.5, alpha=0.5)
        g = np.linspace(classe.min(), classe.max(), 20)
        a1.plot(g, semplice.params[0] + semplice.params[1] * g, color=es.RED, lw=1.6,
                label=f"pendenza {semplice.params[1]:.2f}".replace(".", ","))
        a1.set_xlabel("classe")
        a1.set_ylabel("punteggio")
        a2.plot(u_classe, u_punt, "o", color=es.GRAY, ms=2.5, alpha=0.5)
        g = np.linspace(u_classe.min(), u_classe.max(), 20)
        a2.plot(g, r3.params[1] * g, color=es.BLUE, lw=1.6,
                label=f"pendenza {r3.params[1]:.2f}".replace(".", ","))
        a2.set_xlabel("u_classe")
        a2.set_ylabel("u_punteggio")
        for ax in (a1, a2):
            es.commas(ax)
            ax.legend(loc="upper right")
        fig.subplots_adjust(wspace=0.35)
        es.save(fig, path)

    truth = answers(full.params[1], r3.tvalues[1], r3.bse[1], aux1.rsquared)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)},
        tabelle={"passo1": tab1, "passo2": tab2, "passo3": tab3},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("beta"), "b": Quesito("dec"), "c": Quesito("vif")},
        attese=[lambda r: r["dec"] == "non rifiuta", lambda r: r["beta"].valore < 0,
                lambda r: semplice.params[1] < 2 * r["beta"].valore, coincide],
        margini=[Margin(stat=r3.tvalues[1], crit=Z), Margin(stat=full.tvalues[1], crit=Z)],
        figure={"residui": figura})


@exercise("e03_10", modulo=3, livello=3, punti=4,
          tipo=("termine-quadratico-nonlinearita", "punto-di-svolta-quadratico",
                "unita-di-misura-e-scala"))
def reddito_quadratico(rng):
    """Test a squared income, find the turning point in dollars and test the effect at a point."""
    n, x0, unita = 300, 5.0, 10000.0
    red = np.clip(rng.gamma(4.0, 1.0, n), 0.3, 12.0)
    eta = rng.integers(25, 66, n).astype(float)
    y = 5.0 + 0.42 * red - 0.037 * red**2 + 0.004 * eta + rng.normal(0, 0.6, n)
    res, tab = _fit(y, {"red": red, "sq_red": red**2, "eta": eta})
    b1, b2, t2 = res.params[1], res.params[2], res.tvalues[2]
    v = res.cov_params()
    cov = round(float(v[1, 2]), 8)

    def answers(c1, s1, c2, s2, ratio2, c12):
        """Return every answer from the two income coefficients, their se, t and covariance."""
        eff = c1 + 2 * c2 * x0
        err = np.sqrt(s1**2 + 4 * x0**2 * s2**2 + 4 * x0 * c12)
        ingenuo = np.sqrt(s1**2 + 4 * x0**2 * s2**2)
        return {"dec": _decide(ratio2), "decr": "sì" if abs(ratio2) > Z and c2 < 0 else "no",
                "punto": Numero(-c1 / (2 * c2) * unita, 0),
                "punto_unita": Numero(-c1 / (2 * c2), 4), "eff": Numero(100 * eff, 2),
                "se_eff": Numero(100 * err, 2), "t_eff": Numero(eff / err, 2),
                "dec_eff": _decide(eff / err), "se_ingenuo": Numero(100 * ingenuo, 2),
                "dec_ingenuo": _decide(eff / ingenuo), "t2": Numero(ratio2, 2),
                "b1": Numero(c1, 6), "b2": Numero(c2, 7), "s1": Numero(s1, 6), "s2": Numero(s2, 7)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of ``red``, ``sq_red`` and the covariance."""
        rows = tabelle["ols"].rows
        return answers(rows["red"]["coef"], rows["red"]["se"], rows["sq_red"]["coef"],
                       rows["sq_red"]["se"], rows["sq_red"]["t"], cov)

    def derivata_coerente(_risposte):
        """Check that the marginal-effect formula matches a numeric derivative of the fitted curve."""
        h = 1e-4

        def fitted(x):
            """Return the fitted log spending at income ``x`` for a 45-year-old."""
            return np.array([1.0, x, x * x, 45.0]) @ res.params

        return abs((fitted(x0 + h) - fitted(x0 - h)) / (2 * h) - (b1 + 2 * b2 * x0)) < 1e-8

    def errore_coerente(r):
        """Check that the se of beta1 + 2*x0*beta2 is the one of the linear combination."""
        peso = np.array([0.0, 1.0, 2 * x0, 0.0])
        return abs(float(res.t_test(peso).sd[0, 0]) * 100 - r["se_eff"].valore) < 1e-9

    def figura(path):
        """Draw the marginal effect with its 95% band, the evaluation point and the zero."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.1))
        x = np.linspace(0.5, 9, 200)
        l = np.column_stack([np.zeros_like(x), np.ones_like(x), 2 * x, np.zeros_like(x)])
        eff = l @ res.params
        err = np.sqrt(np.einsum("ij,jk,ik->i", l, v, l))
        ax.fill_between(x, 100 * (eff - Z * err), 100 * (eff + Z * err), color=es.BLUEBG,
                        label="intervallo di confidenza al 95%")
        ax.plot(x, 100 * eff, color=es.BLUE, lw=1.6, label="effetto marginale stimato")
        ax.axhline(0, color=es.RED, ls="--", lw=1.0)
        ax.axvline(-b1 / (2 * b2), color=es.RED, ls=":", lw=1.0)
        ax.plot([x0], [100 * (b1 + 2 * b2 * x0)], "o", color=es.GREEN, ms=7, zorder=5)
        ax.set_xlabel("reddito (decine di migliaia di dollari)")
        ax.set_ylabel("effetto marginale su log(spesa), in %")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    truth = answers(b1, res.bse[1], b2, res.bse[2], t2, float(v[1, 2]))
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "x0": Numero(x0, 0), "unita": Numero(unita, 0),
                   "cov": Numero(cov, 8)},
        tabelle={"ols": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec"), "b": Quesito("decr"),
                 "c": Quesito("punto", tolleranza=10.0), "d": Quesito("eff"),
                 "e": Quesito("dec_eff")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["decr"] == "sì",
                lambda r: r["eff"].valore > 0, lambda r: 0.5 < r["punto_unita"].valore < 9,
                lambda r: r["dec_eff"] != r["dec_ingenuo"], derivata_coerente, errore_coerente],
        margini=[Margin(stat=t2, crit=Z), Margin(stat=truth["t_eff"].valore, crit=Z),
                 Margin(stat=truth["eff"].valore / truth["se_ingenuo"].valore, crit=Z)],
        figure={"effetto": figura})


@exercise("e03_11", modulo=3, livello=3, punti=4,
          tipo=("elasticita-log-log", "variazione-percentuale-log-livello"))
def affitti_elasticita(rng):
    """Mix an elasticity and a semi-elasticity: compare, offset and test a claim."""
    n, ds, dkm, riv = 300, 10.0, 2.0, 7.0
    mq = rng.lognormal(4.3, 0.3, n)
    km = rng.gamma(2.5, 1.6, n)
    asc = rng.binomial(1, 0.6, n).astype(float)
    y = 4.1 + 0.72 * np.log(mq) - 0.045 * km + 0.08 * asc + rng.normal(0, 0.2, n)
    res, tab = _fit(y, {"l_mq": np.log(mq), "km": km, "ascensore": asc})
    b1, b2 = res.params[1], res.params[2]
    s1 = res.bse[1]

    def answers(c1, e1, c2):
        """Return every answer from the elasticity, its se and the per-km coefficient."""
        el = riv / ds
        t_riv = (c1 - el) / e1
        return {"size": Numero(ds * c1, 2), "km": Numero(100 * c2 * dkm, 2),
                "compensa": Numero(-100 * c2 * dkm / c1, 1),
                "dec": "no" if abs(t_riv) > Z else "sì", "el": Numero(el, 2),
                "t_riv": Numero(t_riv, 2), "b1": Numero(c1, 3), "b2": Numero(c2, 4),
                "ic_lo": Numero(c1 - Z * e1, 3), "ic_hi": Numero(c1 + Z * e1, 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of ``l_mq`` and ``km``."""
        rows = tabelle["ols"].rows
        return answers(rows["l_mq"]["coef"], rows["l_mq"]["se"], rows["km"]["coef"])

    def formule_coerenti(r):
        """Check that the exact percentage changes are close to the approximations used."""
        x = np.array([1.0, np.log(mq.mean()), km.mean(), 1.0])
        grande = x + np.array([0.0, np.log(1 + ds / 100), 0.0, 0.0])
        lontano = x + np.array([0.0, 0.0, dkm, 0.0])
        esatto_size = 100 * (np.exp((grande - x) @ res.params) - 1)
        esatto_km = 100 * (np.exp((lontano - x) @ res.params) - 1)
        return (abs(esatto_size - r["size"].valore) < 0.04 * abs(r["size"].valore)
                and abs(esatto_km - r["km"].valore) < 0.06 * abs(r["km"].valore))

    def compensa_esatto(r):
        """Check that raising the size by the answer offsets the distance penalty."""
        p = r["compensa"].valore / 100
        return abs(b1 * np.log(1 + p) + b2 * dkm) < 0.1 * abs(b2 * dkm)

    def figura(path):
        """Draw the rent change from a size rise against the penalty of the distance."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        s = np.linspace(0, 25, 100)
        penalita = -100 * b2 * dkm
        ax.plot(s, b1 * s, color=es.BLUE, lw=1.6, label=r"$\hat\beta_1 \times$ aumento della superficie")
        ax.axhline(penalita, color=es.RED, ls="--", lw=1.2,
                   label="perdita per i km in più (in valore assoluto)")
        pareggio = penalita / b1
        ax.plot([pareggio], [penalita], "o", color=es.GREEN, ms=7, zorder=5)
        ax.annotate(f"+{pareggio:.1f}% di superficie".replace(".", ","), xy=(pareggio, penalita),
                    xytext=(8, -16), textcoords="offset points", fontsize=8.5, color=es.GREEN,
                    fontweight="bold")
        ax.set_xlabel("aumento percentuale della superficie")
        ax.set_ylabel("variazione percentuale dell'affitto")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    truth = answers(b1, s1, b2)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "ds": Numero(ds, 0), "dkm": Numero(dkm, 0),
                   "riv": Numero(riv, 0)},
        tabelle={"ols": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("size"), "b": Quesito("km"), "c": Quesito("compensa"),
                 "d": Quesito("dec")},
        attese=[lambda r: r["dec"] == "sì", lambda r: 0 < r["size"].valore < ds,
                lambda r: r["km"].valore < 0, formule_coerenti, compensa_esatto],
        margini=[Margin(stat=truth["t_riv"].valore, crit=Z)], figure={"pareggio": figura})


@exercise("e03_12", modulo=3, livello=3, punti=4,
          tipo=("collinearita-diagnosi", "vif-inflazione-errore-standard"))
def esperienza_anzianita(rng):
    """Diagnose collinearity from the VIF and from the standard errors of two models."""
    n = 200
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(2, 36, n).astype(float)
    anz = np.clip(np.round(0.85 * esper + rng.normal(0, 2.5, n)), 0, esper)
    y = 1.3 + 0.06 * istr + 0.010 * esper + 0.012 * anz + rng.normal(0, 0.45, n)
    cols = {"istr": istr, "esper": esper, "anz": anz}
    r1, tab1 = _fit(y, cols)
    r2, tab2 = _fit(y, {"istr": istr, "esper": esper})
    vifs = _vif(cols)
    tab_vif = vif_table(vifs)

    def answers(vif, m1, m2):
        """Return every answer from the printed VIF and the printed rows of ``esper`` in both models."""
        return {"alto": "sì" if max(vif.values()) > SOGLIA_VIF else "no",
                "fattore": Numero(np.sqrt(vif["esper"]), 2),
                "rapporto": Numero(m1["se"] / m2["se"], 2), "dec1": _decide(m1["t"]),
                "dec2": _decide(m2["t"]), "salto": Numero(100 * (m2["coef"] - m1["coef"]), 1),
                "vif": Numero(vif["esper"], 3), "vif_anz": Numero(vif["anz"], 3),
                "vif_istr": Numero(vif["istr"], 3),
                "se1": Numero(m1["se"], 5), "se2": Numero(m2["se"], 5),
                "t1": Numero(m1["t"], 2), "t2": Numero(m2["t"], 2),
                "b1": Numero(m1["coef"], 4), "b2": Numero(m2["coef"], 4)}

    def studente(tabelle):
        """Rebuild the answers from the printed VIF and the printed rows of ``esper``."""
        return answers(parse_vif(tab_vif), tabelle["m1"].rows["esper"], tabelle["m2"].rows["esper"])

    def riga(res):
        """Return the ``esper`` row of a fit as the dictionary the table parser would give."""
        return {"coef": res.params[2], "se": res.bse[2], "t": res.tvalues[2]}

    def identita_vif(_risposte):
        """Check that the variance of each coefficient is sigma^2 * VIF_j / SST_j, exactly."""
        s2 = r1.ssr / r1.df_resid
        return all(abs(r1.bse[i + 1]**2 - s2 * vifs[k] / np.sum((cols[k] - cols[k].mean())**2)) < 1e-12
                   for i, k in enumerate(cols))

    def modello_due_ortogonale(_risposte):
        """Check that, without tenure, experience is nearly orthogonal to schooling."""
        return 1 / (1 - np.corrcoef(esper, istr)[0, 1] ** 2) < 1.1

    def rapporto_vicino(r):
        """Check that the ratio of the standard errors is within 10% of sqrt(VIF)."""
        return abs(r["rapporto"].valore / r["fattore"].valore - 1) < 0.10

    def figura(path):
        """Draw experience against tenure, and the interval of experience with and without tenure."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.8), gridspec_kw={"width_ratios": [1, 1.25]})
        a1.plot(esper, anz, "o", color=es.BLUE, ms=3, alpha=0.5)
        a1.set_xlabel("esper")
        a1.set_ylabel("anz")
        es.commas(a1)
        _intervalli(a2, es, [(1, r1.params[2], r1.bse[2], "con anz (Modello 1)", es.RED),
                             (0, r2.params[2], r2.bse[2], "senza anz (Modello 2)", es.BLUE)],
                    "coefficiente di esper, con intervallo al 95%", colonne=1, ancora=-0.3)
        a2.axvline(0, color=es.GRAY, lw=0.8)
        fig.subplots_adjust(wspace=0.25)
        es.save(fig, path)

    truth = answers(vifs, riga(r1), riga(r2))
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)},
        tabelle={"m1": tab1, "m2": tab2, "vif": tab_vif}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("alto"), "b": Quesito("fattore"), "c": Quesito("rapporto"),
                 "d": Quesito("dec1"), "e": Quesito("dec2"), "f": Quesito("salto")},
        attese=[lambda r: r["alto"] == "sì", lambda r: r["dec1"] == "non rifiuta",
                lambda r: r["dec2"] == "rifiuta", lambda r: r["salto"].valore > 0,
                identita_vif, rapporto_vicino, modello_due_ortogonale],
        margini=[Margin(stat=vifs["esper"], crit=SOGLIA_VIF), Margin(stat=vifs["anz"], crit=SOGLIA_VIF),
                 Margin(stat=vifs["istr"], crit=SOGLIA_VIF),
                 Margin(stat=r1.tvalues[2], crit=Z), Margin(stat=r2.tvalues[2], crit=Z)],
        figure={"collinearita": figura})


@exercise("e03_13", modulo=3, livello=3, punti=4, tipo="endogeneita-variabile-omessa")
def abilita_omessa(rng):
    """Compare a model with and without a relevant regressor and check the bias formula."""
    n = 500
    abil = rng.normal(0, 1, n)
    istr = np.clip(np.round(13 + 1.6 * abil + rng.normal(0, 1.5, n)), 8, 20)
    esper = rng.integers(0, 31, n).astype(float)
    y = 1.2 + 0.05 * istr + 0.012 * esper + 0.10 * abil + rng.normal(0, 0.4, n)
    r1, tab1 = _fit(y, {"istr": istr, "esper": esper})
    r2, tab2 = _fit(y, {"istr": istr, "esper": esper, "abil": abil})
    ra, taba = _fit(abil, {"istr": istr, "esper": esper})

    def answers(b1_ristretto, b1_completo, b_abil, t_abil, delta, t_delta):
        """Return the change, the verdict and the bias formula from six printed numbers."""
        return {"a": Numero(100 * (b1_ristretto - b1_completo), 1),
                "c": Numero(100 * b_abil * delta, 1),
                "dec": "sì" if abs(t_abil) > Z and abs(t_delta) > Z else "no",
                "sovrastima": "sì" if b1_ristretto > b1_completo else "no",
                "t_abil": Numero(t_abil, 2), "t_delta": Numero(t_delta, 2),
                "b_abil": Numero(b_abil, 4), "delta": Numero(delta, 4),
                "b1_ristretto": Numero(b1_ristretto, 4), "b1_completo": Numero(b1_completo, 4)}

    def studente(tabelle):
        """Rebuild the answers from the three printed tables."""
        m1, m2, aux = (tabelle[k].rows for k in ("m1", "m2", "aux"))
        return answers(m1["istr"]["coef"], m2["istr"]["coef"], m2["abil"]["coef"],
                       m2["abil"]["t"], aux["istr"]["coef"], aux["istr"]["t"])

    def figura(path):
        """Draw the interval of the schooling coefficient in the two models."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.2))
        _intervalli(ax, es, [(1, r1.params[1], r1.bse[1], "senza abilità (Modello 1)", es.RED),
                             (0, r2.params[1], r2.bse[1], "con abilità (Modello 2)", es.BLUE)],
                    "coefficiente di istruzione, con intervallo al 95%")
        es.save(fig, path)

    truth = answers(r1.params[1], r2.params[1], r2.params[3], r2.tvalues[3],
                    ra.params[1], ra.tvalues[1])

    def formula_esatta(r):
        """Check that the bias formula holds exactly: change in beta = beta_abil * delta."""
        return abs(r["a"].valore - r["c"].valore) < 1e-6

    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"m1": tab1, "m2": tab2, "aux": taba},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("a"), "b": Quesito("dec"), "c": Quesito("c"),
                 "d": Quesito("sovrastima")},
        attese=[lambda r: r["dec"] == "sì", lambda r: r["a"].valore > 1, formula_esatta,
                lambda r: r["delta"].valore > 0 and r["b_abil"].valore > 0,
                lambda r: r["sovrastima"] == "sì"],
        margini=[Margin(stat=r2.tvalues[3], crit=Z), Margin(stat=ra.tvalues[1], crit=Z)],
        figure={"confronto": figura})
