"""Appello simulato 3 - formazione finanziata e tasso di scarto; PIL di due paesi e correzione dell'errore."""

from types import SimpleNamespace

import numpy as np
import statsmodels.api as sm
from scipy.special import expit
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.tsa.stattools import acf, adfuller, coint, pacf

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import ols_table, parse_table

TITOLO = "Appello simulato 3"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

ALFA = 0.05

# Dickey-Fuller critical values the exam texts hand out: constant only, constant and trend.
DF_C = -2.38
DF_T = -3.43

# MacKinnon asymptotic 5% value with constant and trend: the margins are also checked against it,
# so that the decision does not depend on which convention a reader applies.
MK_T = -3.41


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _decide(t):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > Z else "non rifiuta"


def _df(t, crit):
    """Return the one-sided Dickey-Fuller decision, in the words of the exam."""
    return "rifiuta" if t < crit else "non rifiuta"


def _dec_p(p):
    """Return the decision of a test that rejects when the p-value is below 5%."""
    return "rifiuta" if p < ALFA else "non rifiuta"


def _sig(x, cifre=6):
    """Return ``x`` as a Numero with ``cifre`` significant digits, as a printed table shows it."""
    return Numero(x, max(0, cifre - 1 - int(np.floor(np.log10(abs(x))))))


def _cov4(c):
    """Round a covariance to the four significant digits the text prints."""
    return float(f"{c:.4g}")


def _decimali(c, cifre=4):
    """Return the decimals that show ``c`` with ``cifre`` significant digits."""
    return max(0, cifre - 1 - int(np.floor(np.log10(abs(c)))))


def _virgola(x, decimali):
    """Return ``x`` for a figure label, with the decimal comma."""
    return f"{x:.{decimali}f}".replace(".", ",")


def _lontano(stat, crit, rel=0.15):
    """Return whether ``stat`` clears ``crit`` by the fraction ``rel``, as the bank's margin does."""
    return abs(abs(stat) - abs(crit)) >= rel * abs(crit)


def _p_lontano(p):
    """Return an expectation that ``p`` stays outside 0.02-0.10, clear of the 5% threshold."""
    def lontano(_risposte):
        """Check that the p-value is below 0.02 or above 0.10."""
        return p < 0.02 or p > 0.10

    return lontano


def _campiona(g, genera, accetta, tentativi=4000):
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


def _fit_robusto(y, X, nomi):
    """Fit OLS with HC1 standard errors and t-based p-values; return the result and its table.

    HC1 is the variant gretl and Stata print by default, and the one of the exam texts.
    """
    res = sm.OLS(y, X).fit(cov_type="HC1", use_t=True)
    return res, ols_table(res, labels=nomi, stats=("n", "r2"))


def _sandwich(X, e):
    """Return the HC1 covariance matrix of the OLS coefficients from the sandwich formula."""
    n, p = X.shape
    pane = np.linalg.inv(X.T @ X)
    carne = (X * (e ** 2)[:, None]).T @ X
    return n / (n - p) * pane @ carne @ pane


def _righe(res, nomi):
    """Return the rows of a fit as the dictionaries the table parser would give, at full precision."""
    return {k: {"coef": float(res.params[j]), "se": float(res.bse[j]), "t": float(res.tvalues[j])}
            for j, k in enumerate(nomi)}


def _quartili(fitted, resid):
    """Return the standard deviation of the residuals in each quartile of the fitted values."""
    bordi = np.quantile(fitted, [0.25, 0.5, 0.75])
    classe = np.digitize(fitted, bordi)
    return np.array([resid[classe == q].std(ddof=1) for q in range(4)])


def _intervalli(ax, es, voci, xlabel):
    """Draw one 95% interval per entry of ``voci`` = (height, coefficient, se, label, colour)."""
    for altezza, coef, err, etichetta, colore in voci:
        ax.errorbar(coef, altezza, xerr=Z * err, fmt="o", color=colore, capsize=4, label=etichetta)
    ax.axvline(0, color=es.GRAY, lw=0.8)
    ax.set_yticks([])
    ax.set_ylim(-0.6, max(v[0] for v in voci) + 0.6)
    ax.set_xlabel(xlabel)
    es.commas(ax, "x")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.4), ncol=2)


def _tabella(intestazioni, righe):
    """Render a Markdown table from header cells and rows of preformatted cells."""
    linee = ["| " + " | ".join(intestazioni) + " |", "|" + "---|" * len(intestazioni)]
    linee += ["| " + " | ".join(r) + " |" for r in righe]
    return "\n".join(linee)


def _num(x, d):
    """Format ``x`` as a math-mode table cell with ``d`` decimals and a decimal comma."""
    return f"${Numero(x, d).tex()}$"


def _adf_t(s, ritardi):
    """Return the t ratio of the lagged level in the ADF regression with constant, trend and lags.

    The dependent is the first difference, regressed on a constant, a linear trend,
    the lagged level and ``ritardi`` lagged differences.
    """
    d = np.diff(s)
    liv = s[ritardi:-1]
    cols = [np.ones(len(liv)), np.arange(1.0, len(liv) + 1), liv]
    cols += [d[ritardi - j:len(d) - j] for j in range(1, ritardi + 1)]
    res = sm.OLS(d[ritardi:], np.column_stack(cols)).fit()
    return float(res.tvalues[2])


def _eg_p(y, x):
    """Return the MacKinnon p-value of the Engle-Granger test of ``y`` on ``x`` with a constant."""
    return round(float(coint(y, x, trend="c")[1]), 4)


def _acf_pacf(resid, ritardi=12):
    """Return the sample ACF and PACF of ``resid`` at lags ``1..ritardi``."""
    return (acf(resid, nlags=ritardi, fft=False)[1:], pacf(resid, nlags=ritardi, method="ywm")[1:])


def _banda(n):
    """Return the 95% band of a sample autocorrelation of ``n`` observations."""
    return Z / np.sqrt(n)


def _figura_serie(path, serie, titoli, rette=False):
    """Draw each series in its own panel, with an optional fitted linear trend dashed on top."""
    es, plt = _stile()
    fig, axs = plt.subplots(1, len(serie), figsize=(6.1, 2.6), squeeze=False)
    for j, (y, titolo) in enumerate(zip(serie, titoli)):
        ax = axs[0, j]
        t = np.arange(1, len(y) + 1)
        ax.plot(t, y, color=es.BLUE, lw=1.2, label="serie")
        if rette:
            ax.plot(t, np.polyval(np.polyfit(t, y, 1), t), color=es.RED, lw=1.6, ls="--",
                    label="retta di trend")
            ax.legend(loc="upper left")
        ax.set_title(titolo)
        ax.set_xlabel("trimestre")
        es.commas(ax)
    fig.subplots_adjust(wspace=0.3)
    es.save(fig, path)


def _formazione():
    """Return the settings of the first exercise: sample size, profiles, claims and units."""
    return SimpleNamespace(n=400, ore_a=6, ore_b=20, ore3=10, riv3=25, s0=5, giornata=8, c6=0.30)


@exercise("a03_01", modulo=10, livello=3, punti=19,
          tipo=("interazione-effetto-marginale-condizionato",
                "differenza-tra-profili-combinazione-lineare", "test-su-valore-specifico",
                "eteroschedasticita-grafico-residui", "endogeneita-variabile-omessa",
                "unita-di-misura-e-scala"))
def formazione_e_scarto(rng):
    """Read an interaction model of defect rates: effects, profiles, claims, residual plot, omitted size."""
    k = _formazione()
    n = k.n
    nomi1 = ["const", "fin", "ore", "ore_fin"]
    nomi2 = nomi1 + ["l_vendite"]
    vero = dict(c=1.60, fin=-0.04, ore=-0.0080, of=-0.0120, lv=-0.18)

    def genera(g):
        """Draw the firms and fit the two models and the auxiliary regression with HC1 errors."""
        lv = g.normal(2.0, 0.8, n)
        fin = g.binomial(1, expit(-0.3 + 0.8 * (lv - 2.0))).astype(float)
        base = np.where(fin == 1, 5 + g.gamma(2.4, 4.5, n), g.gamma(1.8, 6.0, n))
        ore = np.clip(np.round(base + 3.5 * (lv - 2.0)), 0, 40)
        mu = (vero["c"] + vero["fin"] * fin + vero["ore"] * ore + vero["of"] * ore * fin
              + vero["lv"] * (lv - 2.0))
        # The error spread grows with the conditional mean, which gives the fan of the residual plot;
        # the clip keeps a defect rate of the order of the whole production out of the sample.
        y = mu + 0.15 * np.exp(3.0 * (mu - 1.25)) * np.clip(g.normal(0.0, 1.0, n), -2.5, 2.5)
        X1 = sm.add_constant(np.column_stack([fin, ore, ore * fin]))
        m1, tab1 = _fit_robusto(y, X1, nomi1)
        X2 = np.column_stack([X1, lv])
        m2, tab2 = _fit_robusto(y, X2, nomi2)
        aux, tab_aux = _fit_robusto(lv, X1, nomi1)
        ols = sm.OLS(y, X1).fit()
        return SimpleNamespace(m1=m1, m2=m2, aux=aux, X1=X1, y=y, tab1=tab1, tab2=tab2,
                               tab_aux=tab_aux, ols=ols)

    def esito(s):
        """Return the answers of a draw from its full-precision rows, to filter the draws."""
        return answers(_righe(s.m1, nomi1), _righe(s.m2, nomi2), _righe(s.aux, nomi1), covs_di(s))

    def covs_di(s):
        """Return the three covariances of the text, rounded as printed."""
        v = s.m1.cov_params()
        return {"12": _cov4(v[1, 2]), "13": _cov4(v[1, 3]), "23": _cov4(v[2, 3])}

    def answers(r1, r2, ra, c):
        """Return every answer from the printed rows of the three tables and the text's covariances."""
        b1, b2, b3 = (r1[q]["coef"] for q in ("fin", "ore", "ore_fin"))
        s1, s2, s3 = (r1[q]["se"] for q in ("fin", "ore", "ore_fin"))
        dh = k.ore_a - k.ore_b
        diff = b1 + dh * b2 + k.ore_a * b3
        var = ((s1 ** 2) + (dh * s2) ** 2 + (k.ore_a * s3) ** 2
               + 2 * (dh * c["12"] + k.ore_a * c["13"] + dh * k.ore_a * c["23"]))
        se = np.sqrt(var)
        se_ing = np.sqrt(s1 ** 2 + (dh * s2) ** 2 + (k.ore_a * s3) ** 2)
        stima3 = 100 * k.ore3 * b2
        se3 = 100 * k.ore3 * s2
        t3 = (k.ore3 * b2 + k.riv3 / 100) / (k.ore3 * s2)
        b2m, s2m = r2["ore"]["coef"], r2["ore"]["se"]
        b_lv, t_lv = r2["l_vendite"]["coef"], r2["l_vendite"]["t"]
        delta, t_delta = ra["ore"]["coef"], ra["ore"]["t"]
        eff6 = k.giornata * k.s0 * b2m
        se6 = k.giornata * k.s0 * s2m
        t6 = (eff6 + k.c6) / se6
        return {
            "b1": _sig(b1), "b2": _sig(b2), "b3": _sig(b3), "s1": _sig(s1), "s2": _sig(s2),
            "s3": _sig(s3), "eff_fin": Numero(100 * (b2 + b3), 2), "eff_nofin": Numero(100 * b2, 2),
            "t_b3": Numero(r1["ore_fin"]["t"], 2), "dec_b3": _decide(r1["ore_fin"]["t"]),
            "dh": Numero(dh, 0), "diff": _sig(diff, 4), "diff_pct": Numero(100 * diff, 2),
            "var_diff": _sig(var, 4), "se_diff": Numero(100 * se, 2), "se_ing": Numero(100 * se_ing, 2),
            "ic_lo": Numero(100 * (diff - Z * se), 2), "ic_hi": Numero(100 * (diff + Z * se), 2),
            "t_diff": Numero(diff / se, 2), "dec_diff": _decide(diff / se),
            "stima3": Numero(stima3, 2), "se3": Numero(se3, 2), "t3": Numero(t3, 2),
            "dec3": _decide(t3), "beta2_riv": Numero(-k.riv3 / (100 * k.ore3), 4),
            "b2_m1": _sig(b2), "b2_m2": _sig(b2m), "cambio": Numero(100 * (b2 - b2m), 2),
            "b_lv": _sig(b_lv), "t_lv": Numero(t_lv, 2), "dec_lv": _decide(t_lv),
            "delta": _sig(delta), "t_delta": Numero(t_delta, 2),
            "prodotto": Numero(100 * b_lv * delta, 2),
            "distorto": "sì" if abs(t_lv) > Z and abs(t_delta) > Z else "no",
            "b2p": _sig(b2m), "s2p": _sig(s2m), "eff6": Numero(eff6, 3), "se6": Numero(se6, 3),
            "t6": Numero(t6, 2), "dec6": _decide(t6),
            "t6_ora": Numero((eff6 / k.giornata + k.c6) / (se6 / k.giornata), 1),
            "beta6_riv": Numero(-k.c6 / (k.giornata * k.s0), 5),
        }

    def accetta(s):
        """Accept a draw whose tests tell the intended story with clear margins."""
        r = esito(s)
        q = _quartili(s.ols.fittedvalues, s.ols.resid)
        c = np.corrcoef(np.abs(s.ols.resid), s.ols.fittedvalues)[0, 1]
        t6_ignora = (r["eff6"].valore / k.giornata + k.c6) / (r["se6"].valore / k.giornata)
        return (r["dec_b3"] == "rifiuta" and abs(r["t_b3"].valore) > 2.4
                and r["dec_diff"] == "non rifiuta" and abs(r["t_diff"].valore) < 1.5
                and r["dec3"] == "rifiuta" and abs(r["t3"].valore) > 2.4
                and r["dec_lv"] == "rifiuta" and r["distorto"] == "sì"
                and abs(r["t_delta"].valore) > 2.4 and abs(r["cambio"].valore) > 0.4
                and r["dec6"] == "non rifiuta" and abs(r["t6"].valore) < 1.4
                and abs(t6_ignora) > 2.5
                and 2.5 < q[3] / q[0] < 4.5 and c > 0.3
                and het_breuschpagan(s.ols.resid, s.X1)[1] < 1e-4)

    s = _campiona(rng, genera, accetta)
    covs = covs_di(s)
    r1, r2, ra = _righe(s.m1, nomi1), _righe(s.m2, nomi2), _righe(s.aux, nomi1)
    q = _quartili(s.ols.fittedvalues, s.ols.resid)
    verita = answers(r1, r2, ra, covs)
    verita.update({"omo": "no", "usuali": "no", "rapporto": Numero(q[3] / q[0], 1),
                   "sd1": Numero(q[0], 3), "sd4": Numero(q[3], 3)})
    tabelle = {"m1": s.tab1, "m2": s.tab2, "aux": s.tab_aux}

    def studente(tab):
        """Rebuild the answers from the three printed tables and the covariances of the text."""
        out = answers(tab["m1"].rows, tab["m2"].rows, tab["aux"].rows, covs)
        out.update({key: verita[key] for key in ("omo", "usuali", "rapporto", "sd1", "sd4")})
        return out

    def stampato():
        """Return the answers as recomputed from the printed tables, the numbers the solutions show."""
        return studente({key: parse_table(text) for key, text in tabelle.items()})

    def sandwich_coerente(_risposte):
        """Check HC1 against the sandwich formula and the combination errors against the library."""
        formula = np.allclose(_sandwich(s.X1, s.ols.resid), s.m1.cov_params(), rtol=1e-9, atol=0)
        w = np.zeros(4)
        w[1:] = [1.0, k.ore_a - k.ore_b, k.ore_a]
        t_lib = float(s.m1.t_test(w).tvalue.item())
        w3 = np.zeros(4)
        w3[2] = k.ore3
        t3_lib = float(s.m1.t_test((w3, -k.riv3 / 100)).tvalue.item())
        w6 = np.zeros(5)
        w6[2] = k.giornata * k.s0
        t6_lib = float(s.m2.t_test((w6, -k.c6)).tvalue.item())
        return (formula and abs(t_lib - verita["t_diff"].valore) < 0.02
                and abs(t3_lib - verita["t3"].valore) < 0.01
                and abs(t6_lib - verita["t6"].valore) < 0.01)

    def identita_omessa(_risposte):
        """Check that the change of every coefficient is exactly the omitted slope times its auxiliary one."""
        return np.allclose(s.m1.params - s.m2.params[:4], s.m2.params[4] * s.aux.params, atol=1e-12)

    def derivata_coerente(_risposte):
        """Check the marginal effects and the profile gap against differences of the fitted log rate."""
        def fitted(f, h):
            """Return the fitted log scrap rate at financing ``f`` and ``h`` hours."""
            return float(s.m1.params @ np.array([1.0, f, h, f * h]))

        eps = 1e-4
        fin1 = (fitted(1.0, 15.0 + eps) - fitted(1.0, 15.0 - eps)) / (2 * eps)
        fin0 = (fitted(0.0, 15.0 + eps) - fitted(0.0, 15.0 - eps)) / (2 * eps)
        gap = fitted(1.0, k.ore_a) - fitted(0.0, k.ore_b)
        return (abs(100 * fin1 - verita["eff_fin"].valore) < 0.01
                and abs(100 * fin0 - verita["eff_nofin"].valore) < 0.01
                and abs(100 * gap - verita["diff_pct"].valore) < 0.006)

    def conversioni_coerenti(_risposte):
        """Check that the first-order effect of a day of training is close to the exact one."""
        esatto = k.s0 * (np.exp(k.giornata * s.m2.params[2]) - 1)
        return abs(esatto - verita["eff6"].valore) < 0.1 * abs(verita["eff6"].valore)

    def ventaglio(_risposte):
        """Check that the residual spread grows with the fitted values, in every sense."""
        c = np.corrcoef(np.abs(s.ols.resid), s.ols.fittedvalues)[0, 1]
        return (verita["rapporto"].valore > 2.5 and c > 0.3
                and het_breuschpagan(s.ols.resid, s.X1)[1] < 1e-4)

    def figura_residui(path):
        """Draw the residuals of Model 1 against its fitted values, as in the exam figure."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.plot(s.ols.fittedvalues, s.ols.resid, "o", color=es.BLUE, ms=3, alpha=0.55)
        ax.axhline(0, color=es.RED, lw=1.0)
        ax.set_xlabel(r"valori predetti di $\log(\mathrm{scarto})$")
        ax.set_ylabel(r"residui $\hat\epsilon$")
        es.commas(ax)
        es.save(fig, path)

    def figura_effetto(path):
        """Draw the two fitted lines of the log rate on training hours, one per financing status."""
        es, plt = _stile()
        v = stampato()
        p = s.m1.params
        fig, ax = plt.subplots(figsize=(6.1, 3.1))
        h = np.linspace(0, 40, 50)
        ax.plot(h, p[0] + p[2] * h, color=es.BLUE, lw=1.6,
                label="senza finanziamento: " + _virgola(v["eff_nofin"].valore, 2) + "% per ora")
        ax.plot(h, p[0] + p[1] + (p[2] + p[3]) * h, color=es.RED, lw=1.6,
                label="con finanziamento: " + _virgola(v["eff_fin"].valore, 2) + "% per ora")
        ax.set_xlabel("ore annue di formazione per dipendente")
        ax.set_ylabel(r"$\log(\mathrm{scarto})$ atteso")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    def figura_profili(path):
        """Draw the two profiles on the fitted lines, and the interval of their gap."""
        es, plt = _stile()
        v = stampato()
        p = s.m1.params
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1.3, 1]})
        h = np.linspace(0, 40, 50)

        def retta(f, ore):
            """Return the fitted log scrap rate at financing ``f`` and ``ore`` hours."""
            return p[0] + p[1] * f + (p[2] + p[3] * f) * ore

        a1.plot(h, retta(0.0, h), color=es.BLUE, lw=1.6, label="senza finanziamento")
        a1.plot(h, retta(1.0, h), color=es.RED, lw=1.6, label="con finanziamento")
        a1.plot([k.ore_b], [retta(0.0, k.ore_b)], "o", color=es.BLUE, ms=7, zorder=5)
        a1.plot([k.ore_a], [retta(1.0, k.ore_a)], "o", color=es.RED, ms=7, zorder=5)
        a1.annotate("B", xy=(k.ore_b, retta(0.0, k.ore_b)), xytext=(6, 5), textcoords="offset points",
                    fontsize=9, color=es.BLUE, fontweight="bold")
        a1.annotate("A", xy=(k.ore_a, retta(1.0, k.ore_a)), xytext=(-12, -12),
                    textcoords="offset points", fontsize=9, color=es.RED, fontweight="bold")
        a1.set_xlabel("ore di formazione")
        a1.set_ylabel(r"$\log(\mathrm{scarto})$ atteso")
        es.commas(a1)
        a1.legend(loc="upper right")
        es.ci_line(v["diff_pct"].valore, v["ic_lo"].valore, v["ic_hi"].valore, h0=0.0, ax=a2,
                   decimals=2, xlabel="A meno B, in %")
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    def figura_affermazione(path):
        """Draw the interval for the effect of the extra hours, with the claim as the null value."""
        es, _ = _stile()
        v = stampato()
        err = v["se3"].valore
        fig, _ax = es.ci_line(v["stima3"].valore, v["stima3"].valore - Z * err,
                              v["stima3"].valore + Z * err, h0=-float(k.riv3), decimals=1,
                              xlabel="variazione attesa dello scarto per le ore in più, in %")
        es.save(fig, path)

    def figura_quartili(path):
        """Draw the spread of the residuals in each quartile of the fitted values."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.6))
        pos = np.arange(4)
        ax.bar(pos, q, 0.5, color=[es.BLUE, es.BLUE, es.RED, es.RED])
        ax.set_xticks(pos, ["1°", "2°", "3°", "4°"])
        ax.set_xlabel(r"quartile dei valori predetti")
        ax.set_ylabel("deviazione standard dei residui")
        es.commas(ax)
        es.save(fig, path)

    def figura_confronto(path):
        """Draw the interval of the training-hours coefficient in the two models."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.2))
        _intervalli(ax, es, [(1, s.m1.params[2], s.m1.bse[2], "senza vendite (Modello 1)", es.RED),
                             (0, s.m2.params[2], s.m2.bse[2], "con vendite (Modello 2)", es.BLUE)],
                    "coefficiente di ore, con intervallo al 95%")
        es.save(fig, path)

    def figura_giornata(path):
        """Draw the interval for the effect of a day of training in points, with the claim as null."""
        es, _ = _stile()
        v = stampato()
        err = v["se6"].valore
        fig, _ax = es.ci_line(v["eff6"].valore, v["eff6"].valore - Z * err,
                              v["eff6"].valore + Z * err, h0=-k.c6, decimals=3,
                              xlabel="variazione attesa dello scarto per una giornata, in punti")
        es.save(fig, path)

    margini = [Margin(stat=r1["ore_fin"]["t"], crit=Z), Margin(stat=verita["t_diff"].valore, crit=Z),
               Margin(stat=verita["t3"].valore, crit=Z), Margin(stat=r2["l_vendite"]["t"], crit=Z),
               Margin(stat=ra["ore"]["t"], crit=Z), Margin(stat=verita["t6"].valore, crit=Z)]
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "ore_a": Numero(k.ore_a, 0), "ore_b": Numero(k.ore_b, 0),
                   "c12": Numero(covs["12"], _decimali(covs["12"])),
                   "c13": Numero(covs["13"], _decimali(covs["13"])),
                   "c23": Numero(covs["23"], _decimali(covs["23"])),
                   "ore3": Numero(k.ore3, 0), "riv3": Numero(k.riv3, 0), "s0": Numero(k.s0, 0),
                   "giornata": Numero(k.giornata, 0), "c6": Numero(k.c6, 2)},
        tabelle=tabelle, risposte=verita, studente=studente,
        quesiti={"d1a": Quesito("eff_fin"), "d1b": Quesito("eff_nofin"), "d1c": Quesito("dec_b3"),
                 "d2a": Quesito("diff_pct"), "d2b": Quesito("se_diff"), "d2c": Quesito("dec_diff"),
                 "d3a": Quesito("t3"), "d3b": Quesito("dec3"),
                 "d4a": Quesito("omo"), "d4b": Quesito("usuali"),
                 "d5a": Quesito("cambio"), "d5b": Quesito("dec_lv"), "d5c": Quesito("distorto"),
                 "d6a": Quesito("eff6"), "d6b": Quesito("dec6")},
        attese=[sandwich_coerente, identita_omessa, derivata_coerente, conversioni_coerenti, ventaglio,
                lambda r: r["eff_fin"].valore < r["eff_nofin"].valore < 0,
                lambda r: abs(r["cambio"].valore - r["prodotto"].valore) < 0.006],
        margini=margini,
        figure={"residui": figura_residui, "effetto": figura_effetto, "profili": figura_profili,
                "affermazione": figura_affermazione, "quartili": figura_quartili,
                "confronto": figura_confronto, "giornata": figura_giornata})


def _correlogramma(path, a, p, n):
    """Draw the ACF (top) and PACF (bottom) with the 95% bands, as in the exam figures."""
    es, plt = _stile()
    fig, axs = plt.subplots(2, 1, figsize=(6.1, 3.7), sharex=True)
    es.acf_pacf(a, p, n=n, axes=[axs[0], axs[1]])
    axs[1].set_xticks(np.arange(2, len(a) + 1, 2))
    fig.subplots_adjust(hspace=0.25)
    es.save(fig, path)


def _figura_test(path, nomi, valori, p_eg):
    """Draw the Dickey-Fuller t ratios against both critical values and the Engle-Granger p-value against 5%."""
    es, plt = _stile()
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.1, 2.4), gridspec_kw={"width_ratios": [1.7, 1.0]})
    lo, hi = min(min(valori), DF_T) - 0.8, max(max(valori), DF_C) + 1.2
    ax.axvspan(lo, DF_T, color=es.REDBG, label="rifiuto con costante e trend")
    ax.axvline(DF_T, color=es.RED, ls="-", lw=1.3)
    ax.axvline(DF_C, color=es.GRAY, ls="--", lw=1.0, label="solo costante (non adatto)")
    for i, (nome, v) in enumerate(zip(nomi, valori)):
        ax.plot([v], [i], "o", color=es.BLUE, ms=7, zorder=5)
        ax.annotate(f"{nome}: {_virgola(v, 2)}", xy=(v, i), xytext=(0, 9), textcoords="offset points",
                    ha="center", fontsize=8.5, color=es.BLUE)
    ax.set_xlim(lo, hi)
    ax.set_ylim(-0.7, len(valori) - 0.2)
    ax.set_yticks([])
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("statistica $t$ (valori critici $" + _virgola(DF_T, 2).replace(",", "{,}")
                  + "$ e $" + _virgola(DF_C, 2).replace(",", "{,}") + "$)")
    es.commas(ax, "x")
    ax.legend(loc="upper right", fontsize=7.5)
    bx.axvspan(0, ALFA, color=es.REDBG)
    bx.axvline(ALFA, color=es.RED, ls="--", lw=1.1)
    bx.plot([p_eg], [0], "o", color=es.GREEN, ms=7, zorder=5)
    bx.annotate(f"EG: {_virgola(p_eg, 4)}", xy=(p_eg, 0), xytext=(10, 9), textcoords="offset points",
                ha="left", fontsize=8.5, color=es.GREEN)
    bx.set_xlim(0, 1)
    bx.set_ylim(-0.7, 0.9)
    bx.set_yticks([])
    bx.grid(axis="y", visible=False)
    bx.set_xlabel("p-value EG (soglia $0{,}05$)")
    es.commas(bx, "x")
    fig.subplots_adjust(wspace=0.25)
    es.save(fig, path)


@exercise("a03_02", modulo=10, livello=3, punti=13,
          tipo=("adf-specificazione-regressione", "cointegrazione-decisione",
                "ecm-rispecificazione-da-residui", "ecm-direzione-aggiustamento"))
def pil_due_paesi(rng):
    """Specify the ADF regression of two trending GDPs, decide cointegration and read the ECM."""
    T, p_ar, d_dis = 124, 3, 2.0
    ritardi = p_ar - 1
    lam_v, rho_v, sx, se = -0.28, 0.5, 1.3, 0.5
    banda = _banda(T - 1)

    def genera(g):
        """Draw a trending cointegrated pair with omitted short-run dynamics and run every test."""
        x = 440.0 + np.cumsum(0.62 + g.normal(0.0, sx, T))
        e = g.normal(0.0, se, 260)
        z = np.zeros(260)
        for i in range(2, 260):
            z[i] = (1 + lam_v + rho_v) * z[i - 1] - rho_v * z[i - 2] + e[i]
        y = 52.0 + 0.9 * x + z[-T:]
        lungo = sm.OLS(y, sm.add_constant(x)).fit()
        X = np.column_stack([np.ones(T - 1), np.diff(x), lungo.resid[:-1]])
        res = sm.OLS(np.diff(y), X).fit()
        a, pa = _acf_pacf(res.resid)
        return SimpleNamespace(x=x, y=y, lungo=lungo, res=res, acf=a, pacf=pa, t_a=_adf_t(y, ritardi),
                               t_b=_adf_t(x, ritardi), p=_eg_p(y, x))

    def accetta(s):
        """Accept a draw with unit roots kept, cointegration accepted and short-run autocorrelation in the ECM."""
        visto = np.round(s.acf, 2)
        picchi = abs(s.acf[0]) == np.max(np.abs(s.acf)) and abs(s.pacf[0]) == np.max(np.abs(s.pacf))
        nitido = np.all(np.abs(np.abs(visto) - banda) > 0.02)
        radici = all(t > DF_T and _lontano(t, DF_T) and _lontano(t, MK_T) for t in (s.t_a, s.t_b))
        return (radici and 2e-3 <= s.p < 0.02 and s.res.tvalues[2] < -3.0
                and -0.4 < s.res.params[2] < -0.1 and picchi and nitido
                and s.acf[0] > banda + 0.04 and abs(s.pacf[0]) > 1.5 * banda
                and np.all(np.abs(s.acf[2:]) < banda) and np.all(np.abs(s.pacf[2:]) < banda))

    s = _campiona(rng, genera, accetta)
    n_ecm = int(s.res.nobs)
    vis_a, vis_b = round(s.t_a, 2), round(s.t_b, 2)
    visto = np.round(s.acf, 2)
    res_ecm = ols_table(s.res, labels=["const", "d_pil_b", "ecm_1"], stats=("n", "r2"))
    tab_adf = _tabella(["serie", "statistica $t$ del test ADF"],
                       [["pil_a", _num(vis_a, 2)], ["pil_b", _num(vis_b, 2)]])
    tabelle = {"adf": tab_adf, "lungo": ols_table(s.lungo, labels=["const", "pil_b"], stats=("n", "r2")),
               "ecm": res_ecm}

    def answers(t_a, t_b, p, lam, t_lam, barre, n_obs):
        """Return every answer from the printed statistics, the p-value, the ECM row and the visible bars."""
        dec_a, dec_b, dec_eg = _df(t_a, DF_T), _df(t_b, DF_T), _dec_p(p)
        coint_ok = dec_a == dec_b == "non rifiuta" and dec_eg == "rifiuta"
        ben = coint_ok and lam < 0 and t_lam < -Z
        b = _banda(n_obs)
        fuori = int(np.sum(np.abs(barre) > b))
        aut = abs(barre[0]) > b
        return {"trend": "sì", "ritardi": Numero(p_ar - 1, 0), "n_coef": Numero(3 + p_ar - 1, 0),
                "crit": Numero(DF_T, 2),
                "dec_a": dec_a, "dec_b": dec_b, "dec_eg": dec_eg, "coint": "sì" if coint_ok else "no",
                "t_a": Numero(t_a, 2), "t_b": Numero(t_b, 2),
                "bilanciato": "sì" if ben else "no", "fuori": Numero(fuori, 0), "banda": Numero(b, 3),
                "breve": "sì" if aut else "no", "lungo": "no" if ben else "sì",
                "rho1": Numero(barre[0], 2), "lam": Numero(lam, 4), "t_lam": Numero(t_lam, 2),
                "piu_lenta": "sì" if lam * d_dis < 0 else "no", "delta": Numero(lam * d_dis, 3),
                "quota": Numero(-100 * lam, 1), "resto": Numero(1 + lam, 4)}

    def studente(tab):
        """Rebuild the answers from the printed statistics, the p-value and the row of ``ecm_1``."""
        r = tab["ecm"].rows["ecm_1"]
        return answers(vis_a, vis_b, s.p, r["coef"], r["t"], visto, int(tab["ecm"].stats["n"]))

    def stampato():
        """Return the answers as recomputed from the printed tables, the numbers the solutions show."""
        return studente({key: parse_table(text) for key, text in tabelle.items()})

    verita = answers(vis_a, vis_b, s.p, float(s.res.params[2]), float(s.res.tvalues[2]), visto, n_ecm)

    def adf_coerente(_risposte):
        """Check the hand-built ADF statistics against the library's, with constant, trend and two lags."""
        lib = [float(adfuller(v, maxlag=ritardi, regression="ct", autolag=None)[0]) for v in (s.y, s.x)]
        return abs(lib[0] - s.t_a) < 1e-8 and abs(lib[1] - s.t_b) < 1e-8

    def trend_visibile(_risposte):
        """Check that both series climb by more than two standard deviations between first and last third."""
        m = T // 3
        return all(v[-m:].mean() - v[:m].mean() > 2 * v.std(ddof=1) for v in (s.y, s.x))

    def effetto_lineare(_risposte):
        """Check with the fitted equation that the disequilibrium moves the forecast by lambda * d."""
        con = s.res.predict(np.array([[1.0, 0.0, d_dis]]))[0]
        senza = s.res.predict(np.array([[1.0, 0.0, 0.0]]))[0]
        return abs((con - senza) - verita["delta"].valore) < 1e-3

    def assorbimento_coerente(_risposte):
        """Check the absorbed share by iterating the fitted equation with the regressor held fixed."""
        a, b = s.lungo.params
        x_fisso = s.x[-1]
        y = a + b * x_fisso + 1.0
        y = y + s.res.params[2] * (y - a - b * x_fisso)
        return abs((1.0 - (y - a - b * x_fisso)) * 100 - verita["quota"].valore) < 0.06

    def figura_serie(path):
        """Draw the two GDP series, as in the exam figure."""
        _figura_serie(path, [s.y, s.x], ["pil_a", "pil_b"])

    def figura_correlogramma(path):
        """Draw the ACF and PACF of the ECM residuals, as in the exam figure."""
        _correlogramma(path, s.acf, s.pacf, n_ecm)

    def figura_trend(path):
        """Draw the two series with the linear trend the Dickey-Fuller regression must contain."""
        _figura_serie(path, [s.y, s.x], ["pil_a", "pil_b"], rette=True)

    def figura_test(path):
        """Draw the two Dickey-Fuller statistics against both critical values and the EG p-value."""
        _figura_test(path, ["pil_a", "pil_b"], [vis_a, vis_b], s.p)

    def figura_ritardo(path):
        """Draw each ECM residual against the previous one, with the fitted slope."""
        es, plt = _stile()
        u = s.res.resid
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.plot(u[:-1], u[1:], "o", color=es.GRAY, ms=3, alpha=0.6)
        g = np.linspace(u.min(), u.max(), 20)
        pend = float(s.acf[0])
        ax.plot(g, pend * g, color=es.RED, lw=1.6, label="pendenza " + _virgola(pend, 2))
        ax.set_xlabel(r"residuo $\hat\epsilon_{t-1}$")
        ax.set_ylabel(r"residuo $\hat\epsilon_t$")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    def figura_effetto(path):
        """Draw the expected change of pil_a against the disequilibrium, with the scenario marked."""
        es, plt = _stile()
        v = stampato()
        lam = float(s.res.params[2])
        fig, ax = plt.subplots(figsize=(6.1, 2.9))
        e = np.linspace(-4.0, 4.0, 50)
        ax.plot(e, lam * e, color=es.BLUE, lw=1.6, label=r"$\hat\lambda\,\mathrm{ecm}_t$")
        ax.axhline(0, color=es.GRAY, lw=0.8)
        ax.axvline(0, color=es.GRAY, lw=0.8)
        ax.plot([d_dis], [lam * d_dis], "o", color=es.RED, ms=7, zorder=5)
        ax.annotate(f"ecm = {_virgola(d_dis, 1)}: {_virgola(v['delta'].valore, 3)}", xy=(d_dis, lam * d_dis),
                    xytext=(8, 8), textcoords="offset points", fontsize=8.5, color=es.RED,
                    fontweight="bold")
        ax.set_xlabel(r"disequilibrio $\mathrm{ecm}_t$ (punti)")
        ax.set_ylabel(r"effetto sulla variazione attesa di pil_a")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    return Draft(
        dati=None,
        parametri={"T": Numero(T, 0), "n_ecm": Numero(n_ecm, 0), "p": Numero(p_ar, 0),
                   "cv_c": Numero(DF_C, 2), "cv_t": Numero(DF_T, 2), "p_eg": Numero(s.p, 4),
                   "d": Numero(d_dis, 1)},
        tabelle=tabelle, risposte=verita, studente=studente,
        quesiti={"d7a": Quesito("trend"), "d7b": Quesito("n_coef"), "d7c": Quesito("crit"),
                 "d8a": Quesito("dec_a"), "d8b": Quesito("dec_b"), "d8c": Quesito("dec_eg"),
                 "d8d": Quesito("coint"),
                 "d9a": Quesito("bilanciato"), "d9b": Quesito("fuori"), "d9c": Quesito("breve"),
                 "d9d": Quesito("lungo"),
                 "d10a": Quesito("piu_lenta"), "d10b": Quesito("delta"), "d10c": Quesito("quota")},
        attese=[lambda r: r["coint"] == "sì", lambda r: r["bilanciato"] == "sì",
                lambda r: r["breve"] == "sì" and r["lungo"] == "no",
                lambda r: r["piu_lenta"] == "sì", _p_lontano(s.p), adf_coerente, trend_visibile,
                effetto_lineare, assorbimento_coerente],
        margini=[Margin(stat=t, crit=DF_T) for t in (s.t_a, s.t_b)]
        + [Margin(stat=s.res.tvalues[2], crit=Z), Margin(stat=s.p, crit=ALFA, rel=0.6)],
        figure={"serie": figura_serie, "correlogramma": figura_correlogramma, "trend": figura_trend,
                "test": figura_test, "ritardo": figura_ritardo, "effetto": figura_effetto})
