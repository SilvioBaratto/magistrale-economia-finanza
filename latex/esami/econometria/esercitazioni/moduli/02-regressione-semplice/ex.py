"""Module 02 - simple regression: OLS from sample moments, standard errors, R-squared and tests on the slope."""

import numpy as np
import statsmodels.api as sm

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import ols_table

TITOLO = "Regressione semplice"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

# One-sided 5% quantile of the 2022-12-22 text; the review slides use 1.96 even there.
Z1 = 1.64


def _fit(y, x, nome):
    """Fit OLS of ``y`` on a constant and ``x``; return the result and its printed table."""
    res = sm.OLS(y, sm.add_constant(x)).fit()
    return res, ols_table(res, labels=["const", nome])


def _decide(t, crit=Z):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > crit else "non rifiuta"


def _fmt(x, decimali):
    """Format ``x`` with a decimal comma, as a hand-built table prints it."""
    text = f"{x:.{decimali}f}"
    return (text.lstrip("-") if float(text) == 0 else text).replace(".", ",")


def _leggi(testo):
    """Read a pipe table back as ``{row label: [numbers]}`` at the printed precision."""
    out = {}
    for riga in testo.splitlines():
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if not riga.startswith("|") or not celle[0]:
            continue
        try:
            out[celle[0]] = [float(c.replace(",", ".")) for c in celle[1:]]
        except ValueError:
            continue
    return out


def _pendenze(x, y):
    """Return the OLS slope and its classical standard error for every row of ``x`` and ``y``."""
    n = x.shape[1]
    xc = x - x.mean(axis=1, keepdims=True)
    yc = y - y.mean(axis=1, keepdims=True)
    ssx = (xc**2).sum(axis=1)
    b = (xc * yc).sum(axis=1) / ssx
    ssr = ((yc - b[:, None] * xc)**2).sum(axis=1)
    return b, np.sqrt(ssr / (n - 2) / ssx)


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


@exercise("e02_01", modulo=2, livello=1, tipo="stima-ols-semplice")
def punteggio_ore_studio(rng):
    """Compute intercept and slope from sample moments and use the line for a change and a prediction."""
    n, dx, x0 = 150, 4.0, 15.0
    ore = np.clip(rng.normal(14.0, 4.5, n), 2.0, None)
    y = 38.0 + 2.1 * ore + rng.normal(0.0, 9.0, n)
    res, _ = _fit(y, ore, "ore")
    mx, my = round(float(ore.mean()), 4), round(float(y.mean()), 4)
    vx, vy = round(float(ore.var(ddof=1)), 4), round(float(y.var(ddof=1)), 4)
    cov = round(float(np.cov(ore, y)[0, 1]), 4)
    tab = ("| | media | varianza |\n|---|---|---|\n"
           f"| ore | {_fmt(mx, 4)} | {_fmt(vx, 4)} |\n"
           f"| punteggio | {_fmt(my, 4)} | {_fmt(vy, 4)} |")

    def answers(media_x, media_y, var_x, cov_xy):
        """Return every answer from the two means, the variance of x and the covariance."""
        b = cov_xy / var_x
        a = media_y - b * media_x
        return {"b": Numero(b, 4), "a": Numero(a, 3), "dy": Numero(b * dx, 2),
                "yhat": Numero(a + b * x0, 2)}

    def studente(_tabelle):
        """Rebuild the answers from the printed moments."""
        r = _leggi(tab)
        return answers(r["ore"][0], r["punteggio"][0], r["ore"][1], cov)

    def retta_ols(r):
        """Check that the moment formulas reproduce the least-squares fit and its means identity."""
        return (abs(r["b"].valore - res.params[1]) < 1e-9 and abs(r["a"].valore - res.params[0]) < 1e-9
                and abs(r["a"].valore + r["b"].valore * ore.mean() - y.mean()) < 1e-9)

    def variazione_coerente(_risposte):
        """Check that the fitted change for ``dx`` more hours is exactly the slope times ``dx``."""
        salto = res.predict([[1.0, x0 + dx]]) - res.predict([[1.0, x0]])
        return abs(float(salto[0]) - res.params[1] * dx) < 1e-9

    def figura(path):
        """Draw the scatter, the fitted line through the means and the change for ``dx`` hours."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.2))
        ax.plot(ore, y, "o", color=es.GRAY, ms=3, alpha=0.45)
        g = np.linspace(ore.min(), ore.max(), 50)
        ax.plot(g, res.params[0] + res.params[1] * g, color=es.BLUE, lw=1.6, label="retta OLS")
        ax.plot([ore.mean()], [y.mean()], "o", color=es.RED, ms=7, zorder=5,
                label="punto delle medie")
        y0 = res.params[0] + res.params[1] * x0
        ax.plot([x0, x0 + dx], [y0, y0], color=es.GREEN, lw=1.6)
        ax.plot([x0 + dx, x0 + dx], [y0, y0 + res.params[1] * dx], color=es.GREEN, lw=1.6)
        ax.annotate(f"$\\Delta X$ = {dx:g}".replace(".", ","), xy=(x0 + dx / 2, y0), xytext=(0, -17),
                    textcoords="offset points", ha="center", fontsize=8.5, color=es.GREEN)
        ax.annotate(f"$\\Delta Y$ = {res.params[1] * dx:.2f}".replace(".", ","),
                    xy=(x0 + dx, y0 + res.params[1] * dx / 2), xytext=(5, 0),
                    textcoords="offset points", ha="left", fontsize=8.5, color=es.GREEN)
        ax.set_xlabel("ore di studio")
        ax.set_ylabel("punteggio")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "dx": Numero(dx, 0), "x0": Numero(x0, 0),
                   "mx": Numero(mx, 4), "my": Numero(my, 4), "vx": Numero(vx, 4),
                   "vy": Numero(vy, 4), "cov": Numero(cov, 4)},
        tabelle={"momenti": tab},
        risposte=answers(ore.mean(), y.mean(), ore.var(ddof=1), np.cov(ore, y)[0, 1]),
        studente=studente,
        quesiti={"a": Quesito("b"), "b": Quesito("a"), "c": Quesito("dy"), "d": Quesito("yhat")},
        attese=[lambda r: r["b"].valore > 0, retta_ols, variazione_coerente],
        figure={"retta": figura})


@exercise("e02_02", modulo=2, livello=1, tipo="varianza-errore-standard")
def prezzo_superficie(rng):
    """Estimate the error variance and the slope's standard error from SSR, n and the spread of x."""
    n, m = 60, 4
    sup = rng.normal(95.0, 25.0, n)
    y = 40.0 + 2.2 * sup + rng.normal(0.0, 28.0, n)
    res, _ = _fit(y, sup, "sup")
    ssx = float(np.sum((sup - sup.mean())**2))
    ssr_r, ssx_r = round(float(res.ssr), 2), round(ssx, 2)

    def answers(ssr, somma_x):
        """Return every answer from SSR and the sum of squared deviations of the regressor."""
        s2 = ssr / (n - 2)
        return {"gdl": Numero(n - 2, 0), "s2": Numero(s2, 2), "s": Numero(np.sqrt(s2), 3),
                "se": Numero(np.sqrt(s2 / somma_x), 4), "fattore": Numero(1 / np.sqrt(m), 2),
                "s2_n": Numero(ssr / n, 2)}

    def studente(_tabelle):
        """Rebuild the answers from the printed SSR and sum of squares of x."""
        return answers(ssr_r, ssx_r)

    def identita_se(_risposte):
        """Check that sqrt(sigma^2 / SSx) is the standard error of the fit, to rounding error."""
        return abs(res.bse[1] - np.sqrt(res.ssr / (n - 2) / ssx)) < 1e-12

    def quadruplo_n(r):
        """Check that stacking the sample m times, at fixed sigma, scales the standard error by 1/sqrt(m)."""
        se_m = np.sqrt(res.ssr / (n - 2) / (m * ssx))
        return abs(se_m / res.bse[1] - r["fattore"].valore) < 1e-12

    def sigma_non_distorta(_risposte):
        """Check by simulation that SSR/(n-2) is unbiased for sigma^2 while SSR/n is not."""
        g = np.random.default_rng(1)
        k, sigma = 10, 2.0
        x = g.normal(0.0, 1.0, k)
        X = np.column_stack([np.ones(k), x])
        M = np.eye(k) - X @ np.linalg.solve(X.T @ X, X.T)
        e = g.normal(0.0, sigma, (40_000, k))
        ssr = np.einsum("ri,ij,rj->r", e, M, e)
        return abs(ssr.mean() / (k - 2) / sigma**2 - 1) < 0.02 and ssr.mean() / k / sigma**2 < 0.85

    def figura(path):
        """Draw the standard error against the sample size at fixed sigma and spread of x."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.9))
        k = np.linspace(0.4, 6.0, 120)
        se0 = np.sqrt(res.ssr / (n - 2) / ssx)
        ax.plot(k * n, se0 / np.sqrt(k), color=es.BLUE, lw=1.6,
                label=r"$\widehat{\mathrm{se}}(\hat\beta)\propto 1/\sqrt{n}$")
        for mult, colore in ((1, es.RED), (m, es.GREEN)):
            ax.plot([mult * n], [se0 / np.sqrt(mult)], "o", color=colore, ms=7, zorder=5)
            ax.annotate(f"n = {mult * n}: {se0 / np.sqrt(mult):.4f}".replace(".", ","),
                        xy=(mult * n, se0 / np.sqrt(mult)), xytext=(8, 8),
                        textcoords="offset points", fontsize=8.5, color=colore, fontweight="bold")
        ax.set_xlabel("numerosità del campione")
        ax.set_ylabel("errore standard della pendenza")
        es.commas(ax)
        ax.legend(loc="upper right")
        es.save(fig, path)

    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "m": Numero(m, 0), "ssr": Numero(ssr_r, 2),
                   "ssx": Numero(ssx_r, 2)},
        tabelle={}, risposte=answers(res.ssr, ssx), studente=studente,
        quesiti={"a": Quesito("s2"), "b": Quesito("s"), "c": Quesito("se"),
                 "d": Quesito("fattore")},
        attese=[identita_se, quadruplo_n, sigma_non_distorta], figure={"curva": figura})


@exercise("e02_03", modulo=2, livello=1, tipo="r2-anova")
def affitto_distanza(rng):
    """Complete an incomplete ANOVA table and read R-squared, the residual spread and the correlation."""
    n = 80
    dist = rng.uniform(0.5, 12.0, n)
    y = 9.6 - 0.55 * dist + rng.normal(0.0, 2.2, n)
    res, _ = _fit(y, dist, "dist")
    sst, ssr = float(np.sum((y - y.mean())**2)), float(res.ssr)
    b_r = round(float(res.params[1]), 4)
    sst_r, ssr_r = round(sst, 2), round(ssr, 2)
    tab = ("| fonte | devianza | gdl | media delle devianze |\n|---|---|---|---|\n"
           f"| Residuo | {_fmt(ssr_r, 2)} | {n - 2} | {_fmt(ssr_r / (n - 2), 3)} |\n"
           f"| Totale | {_fmt(sst_r, 2)} | {n - 1} | {_fmt(sst_r / (n - 1), 3)} |")

    def answers(devianza_tot, devianza_res, coef):
        """Return every answer from SST, SSR and the sign of the estimated slope."""
        sse = devianza_tot - devianza_res
        r2 = sse / devianza_tot
        return {"sse": Numero(sse, 1), "r2": Numero(r2, 4), "gdl": Numero(n - 2, 0),
                "s": Numero(np.sqrt(devianza_res / (n - 2)), 3),
                "corr": Numero(np.sign(coef) * np.sqrt(r2), 3), "radice": Numero(np.sqrt(r2), 3),
                "spiegata": Numero(100 * r2, 1), "inspiegata": Numero(100 * (1 - r2), 1)}

    def studente(_tabelle):
        """Rebuild the answers from the printed ANOVA rows and the printed slope."""
        r = _leggi(tab)
        return answers(r["Totale"][0], r["Residuo"][0], b_r)

    def scomposizione(_risposte):
        """Check SST = SSE + SSR, R^2 = Corr(Y, Yhat)^2 = Corr(X, Y)^2 and SSE = b^2 * SSx."""
        sse = float(np.sum((res.fittedvalues - y.mean())**2))
        return (abs(sst - sse - ssr) < 1e-9
                and abs(res.rsquared - np.corrcoef(y, res.fittedvalues)[0, 1]**2) < 1e-12
                and abs(res.rsquared - np.corrcoef(dist, y)[0, 1]**2) < 1e-12
                and abs(sse - res.params[1]**2 * np.sum((dist - dist.mean())**2)) < 1e-8)

    def figura(path):
        """Draw the split of one deviation and the split of SST between SSE and SSR."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1.5, 1]})
        a1.plot(dist, y, "o", color=es.GRAY, ms=3, alpha=0.5)
        g = np.linspace(dist.min(), dist.max(), 30)
        a1.plot(g, res.params[0] + res.params[1] * g, color=es.BLUE, lw=1.6)
        a1.axhline(y.mean(), color=es.GRAY, ls=":", lw=1.0)
        lontani = np.flatnonzero(dist > 8.5)
        i = int(lontani[np.argmax(np.abs(res.resid[lontani]))])
        a1.plot([dist[i] - 0.12] * 2, [y.mean(), res.fittedvalues[i]], color=es.GREEN, lw=2.4,
                label=r"spiegata $\hat y-\bar y$")
        a1.plot([dist[i] + 0.12] * 2, [res.fittedvalues[i], y[i]], color=es.RED, lw=2.4,
                label=r"residuo $y-\hat y$")
        a1.set_xlabel("distanza")
        a1.set_ylabel("affitto")
        es.commas(a1)
        a1.legend(loc="upper right")
        sse = sst - ssr
        a2.barh([0], [sse], color=es.GREEN)
        a2.barh([0], [ssr], left=[sse], color=es.RED)
        a2.text(sse / 2, 0, "SSE", ha="center", va="center", color="white", fontsize=9)
        a2.text(sse + ssr / 2, 0, "SSR", ha="center", va="center", color="white", fontsize=9)
        a2.set_yticks([])
        a2.set_xlabel("SST = SSE + SSR")
        a2.set_title(f"$R^2$ = SSE/SST = {sse / sst:.4f}".replace(".", ","), loc="left", fontsize=9)
        es.commas(a2, "x")
        fig.subplots_adjust(wspace=0.15)
        es.save(fig, path)

    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "b": Numero(b_r, 4), "sst": Numero(sst_r, 2),
                   "ssr": Numero(ssr_r, 2)},
        tabelle={"anova": tab},
        risposte=answers(sst, ssr, res.params[1]), studente=studente,
        quesiti={"a": Quesito("sse"), "b": Quesito("r2"), "c": Quesito("s"), "d": Quesito("corr")},
        attese=[lambda r: 0.3 < r["r2"].valore < 0.7, lambda r: r["corr"].valore < 0, scomposizione],
        figure={"scomposizione": figura})


@exercise("e02_04", modulo=2, livello=1, tipo="proprieta-ols-gauss-markov")
def formazione_endogena(rng):
    """Read a Monte Carlo table: a regressor correlated with the error biases OLS at every sample size."""
    reps, beta, sx2, cov, mu, alpha = 2000, 1.5, 4.0, 2.0, 10.0, 5.0
    taglie = (50, 800)
    stime = {}
    for n in taglie:
        x = rng.normal(mu, np.sqrt(sx2), (reps, n))
        eps = cov / sx2 * (x - mu) + rng.normal(0.0, 1.5, (reps, n))
        stime[n] = _pendenze(x, alpha + beta * x + eps)
    righe = {n: (round(float(b.mean()), 5), round(float(b.std(ddof=1)), 5), round(float(s.mean()), 4))
             for n, (b, s) in stime.items()}
    tab = ("| campioni | media delle stime | dev. std. delle stime | media degli errori std. |\n"
           "|---|---|---|---|\n"
           + "\n".join(f"| n = {n} | {_fmt(m, 5)} | {_fmt(d, 5)} | {_fmt(s, 4)} |"
                       for n, (m, d, s) in righe.items()))

    def distorto(media, dev):
        """Return whether the mean of the estimates is over 3 standard errors from the true slope."""
        return abs(media - beta) / (dev / np.sqrt(reps)) > 3

    def answers(r):
        """Return every answer from the (mean, sd, mean se) triple of each sample size."""
        piccolo, grande = (distorto(r[n][0], r[n][1]) for n in taglie)
        return {"nondist": "no" if piccolo else "sì", "sparisce": "no" if grande else "sì",
                "limite": Numero(beta + cov / sx2, 2), "gm": "no" if piccolo else "sì",
                "rad_r": Numero(np.sqrt(reps), 2),
                "z_piccolo": Numero(abs(r[taglie[0]][0] - beta) / (r[taglie[0]][1] / np.sqrt(reps)), 0),
                "z_grande": Numero(abs(r[taglie[1]][0] - beta) / (r[taglie[1]][1] / np.sqrt(reps)), 0)}

    def studente(_tabelle):
        """Rebuild the answers from the printed Monte Carlo table."""
        letto = _leggi(tab)
        return answers({n: letto[f"n = {n}"] for n in taglie})

    def limite_simulato(r):
        """Check that the simulated means sit on beta + Cov(X, eps) / Var(X), for both sample sizes."""
        return all(abs(righe[n][0] - r["limite"].valore) < 4 * righe[n][1] / np.sqrt(reps)
                   for n in taglie)

    def figura(path):
        """Draw the distribution of the estimates for both sample sizes against beta and its limit."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        for n, colore in zip(taglie, (es.BLUE, es.AMBER)):
            ax.hist(stime[n][0], bins=45, density=True, alpha=0.55, color=colore, label=f"n = {n}")
        ax.axvline(beta, color=es.GREEN, lw=1.8, label=r"valore vero $\beta$")
        ax.axvline(beta + cov / sx2, color=es.RED, ls="--", lw=1.4,
                   label=r"$\beta+\mathrm{Cov}(X,\epsilon)/\mathrm{Var}(X)$")
        ax.set_xlabel(r"stima OLS di $\beta$")
        ax.set_yticks([])
        es.commas(ax, "x")
        ax.legend(loc="upper right")
        es.save(fig, path)

    truth = answers({n: (float(stime[n][0].mean()), float(stime[n][0].std(ddof=1)),
                         float(stime[n][1].mean())) for n in taglie})
    return Draft(
        dati=None,
        parametri={"reps": Numero(reps, 0), "beta": Numero(beta, 1), "sx2": Numero(sx2, 0),
                   "cov": Numero(cov, 0), "n1": Numero(taglie[0], 0), "n2": Numero(taglie[1], 0),
                   "m1": Numero(righe[taglie[0]][0], 5), "m2": Numero(righe[taglie[1]][0], 5),
                   "d1": Numero(righe[taglie[0]][1], 5), "d2": Numero(righe[taglie[1]][1], 5)},
        tabelle={"mc": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("nondist"), "b": Quesito("limite"), "c": Quesito("sparisce"),
                 "d": Quesito("gm")},
        attese=[lambda r: r["nondist"] == "no", lambda r: r["sparisce"] == "no", limite_simulato],
        margini=[Margin(stat=truth["z_piccolo"].valore, crit=3.0),
                 Margin(stat=truth["z_grande"].valore, crit=3.0)],
        figure={"distribuzioni": figura})


@exercise("e02_05", modulo=2, livello=2, tipo=("test-su-valore-specifico", "ic-per-verificare-un-valore"))
def istruzione_due_anni(rng):
    """Test a claim on the effect of two more years of schooling and cross-check it with the interval."""
    n, dx, claim = 300, 2.0, 1.5
    istr = rng.integers(8, 21, n).astype(float)
    y = -1.1 + 0.58 * istr + rng.normal(0.0, 3.2, n)
    res, tab = _fit(y, istr, "istr")
    b, se = res.params[1], res.bse[1]

    def answers(coef, err):
        """Return every answer from the slope and its standard error."""
        k = claim / dx
        t = (coef - k) / err
        lo, hi = dx * (coef - Z * err), dx * (coef + Z * err)
        return {"k": Numero(k, 2), "t": Numero(t, 2), "dec": _decide(t),
                "dentro": "sì" if lo <= claim <= hi else "no", "ic_lo": Numero(lo, 2),
                "ic_hi": Numero(hi, 2), "b": Numero(coef, 4), "se": Numero(err, 4),
                "eff": Numero(dx * coef, 2), "t0": Numero(coef / err, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``istr``."""
        r = tabelle["ols"].rows["istr"]
        return answers(r["coef"], r["se"])

    def formule_coerenti(r):
        """Check dY = beta dX on the fitted line, se(2 beta) = 2 se(beta) and t against statsmodels."""
        salto = float((res.predict([[1.0, 14.0 + dx]]) - res.predict([[1.0, 14.0]]))[0])
        combinato = res.t_test(np.array([0.0, dx]))
        k = claim / dx
        return (abs(salto - r["eff"].valore) < 1e-9 and abs(float(combinato.sd[0, 0]) - dx * se) < 1e-9
                and abs(float(res.t_test(f"x1 = {k}").tvalue) - r["t"].valore) < 1e-9)

    def figura(path):
        """Draw the 95% interval of the two-year effect against the claimed value."""
        es = figs.use_style()
        fig, _ = es.ci_line(dx * b, dx * (b - Z * se), dx * (b + Z * se), h0=claim, decimals=2,
                            xlabel="effetto atteso di due anni di istruzione in più (euro all'ora)")
        es.save(fig, path)

    truth = answers(b, se)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "dx": Numero(dx, 0), "claim": Numero(claim, 2)},
        tabelle={"ols": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("k"), "b": Quesito("t"), "c": Quesito("dec"), "d": Quesito("dentro")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["dentro"] == "no", formule_coerenti],
        margini=[Margin(stat=truth["t"].valore, crit=Z)], figure={"ic": figura})


@exercise("e02_06", modulo=2, livello=2, tipo="test-unilaterale-su-soglia")
def formazione_produttivita(rng):
    """Test an 'at least' claim with a one-sided alternative and read the verdict on the claim."""
    n, dx, dy = 120, 10.0, 3.0
    ore = rng.integers(0, 41, n).astype(float)
    y = 18.0 + 0.22 * ore + rng.normal(0.0, 3.8, n)
    res, tab = _fit(y, ore, "ore")
    b, se = res.params[1], res.bse[1]

    def answers(coef, err):
        """Return every answer from the slope and its standard error."""
        k = dy / dx
        t = (coef - k) / err
        dec = "rifiuta" if t < -Z1 else "non rifiuta"
        return {"k": Numero(k, 2), "t": Numero(t, 2), "dec": dec,
                "compatibile": "sì" if dec == "non rifiuta" else "no",
                "b": Numero(coef, 4), "se": Numero(err, 4), "t0": Numero(coef / err, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``ore``."""
        r = tabelle["ols"].rows["ore"]
        return answers(r["coef"], r["se"])

    def stessa_statistica(r):
        """Check that statsmodels gives the same t for H0: beta = k as the hand formula."""
        return abs(float(res.t_test(f"x1 = {dy / dx}").tvalue) - r["t"].valore) < 1e-9

    def figura(path):
        """Draw the left-tail rejection region of the one-sided test and the observed t."""
        es = figs.use_style()
        t = (b - dy / dx) / se
        fig, _ = es.dist_test("z", stat=t, crit=Z1, tail="left")
        es.save(fig, path)

    truth = answers(b, se)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "dx": Numero(dx, 0), "dy": Numero(dy, 0)},
        tabelle={"ols": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("k"), "b": Quesito("t"), "c": Quesito("dec"),
                 "d": Quesito("compatibile")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["b"].valore < r["k"].valore,
                stessa_statistica],
        margini=[Margin(stat=truth["t"].valore, crit=Z1), Margin(stat=truth["t"].valore, crit=Z)],
        figure={"test": figura})


@exercise("e02_07", modulo=2, livello=2, tipo="ic-per-verificare-un-valore")
def auto_usate(rng):
    """Build the interval of a log-level slope, convert it to a percentage and judge a claimed value."""
    n, dx, claim = 250, 2.0, -20.0
    eta = rng.integers(1, 13, n).astype(float)
    y = 9.9 - 0.095 * eta + rng.normal(0.0, 0.28, n)
    res, tab = _fit(y, eta, "eta")
    b, se = res.params[1], res.bse[1]

    def answers(coef, err):
        """Return every answer from the slope and its standard error."""
        lo, hi = coef - Z * err, coef + Z * err
        k = claim / (100 * dx)
        return {"lo": Numero(lo, 4), "hi": Numero(hi, 4), "plo": Numero(100 * dx * lo, 1),
                "phi": Numero(100 * dx * hi, 1), "plausibile": "sì" if lo <= k <= hi else "no",
                "k": Numero(k, 3), "pct": Numero(100 * dx * coef, 1), "b": Numero(coef, 4),
                "se": Numero(err, 4), "t": Numero((coef - k) / err, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``eta``."""
        r = tabelle["ols"].rows["eta"]
        return answers(r["coef"], r["se"])

    def combinazione_coerente(r):
        """Check that the interval of dx*beta from the linear-combination se is dx times that of beta."""
        comb = res.t_test(np.array([0.0, dx]))
        eff, sd = float(comb.effect[0]), float(comb.sd[0, 0])
        return (abs(100 * (eff - Z * sd) - r["plo"].valore) < 1e-8
                and abs(100 * (eff + Z * sd) - r["phi"].valore) < 1e-8)

    def approssimazione_ragionevole(_risposte):
        """Check that the log approximation stays within 12% of the exact percentage change."""
        esatto = 100 * (np.exp(dx * b) - 1)
        return abs(esatto - 100 * dx * b) < 0.12 * abs(esatto)

    def figura(path):
        """Draw the interval of the slope and of the five-year percentage effect against the claim."""
        es, plt = _stile()
        fig = plt.figure(figsize=(6.1, 3.9))
        grid = fig.add_gridspec(2, 1, hspace=0.6)
        es.ci_line(b, b - Z * se, b + Z * se, h0=claim / (100 * dx), ax=fig.add_subplot(grid[0]),
                   decimals=4, xlabel=r"$\beta$: variazione di log(prezzo) per anno di età")
        es.ci_line(100 * dx * b, 100 * dx * (b - Z * se), 100 * dx * (b + Z * se), h0=claim,
                   ax=fig.add_subplot(grid[1]), decimals=1,
                   xlabel="variazione percentuale del prezzo dopo due anni")
        es.save(fig, path)

    truth = answers(b, se)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "dx": Numero(dx, 0), "claim": Numero(-claim, 0)},
        tabelle={"ols": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("lo"), "b": Quesito("hi"), "c": Quesito("plo"), "d": Quesito("phi"),
                 "e": Quesito("plausibile")},
        attese=[lambda r: r["plausibile"] == "sì", lambda r: r["b"].valore < 0,
                combinazione_coerente, approssimazione_ragionevole],
        margini=[Margin(stat=truth["t"].valore, crit=Z)], figure={"ic": figura})


@exercise("e02_08", modulo=2, livello=2, tipo="proprieta-ols-gauss-markov")
def spesa_eteroschedastica(rng):
    """Separate unbiasedness from reliable standard errors with a Monte Carlo of a heteroskedastic model."""
    reps, n, beta, alpha = 2000, 100, 0.25, 8.0
    # Chosen so both scenarios share the same average error variance, E[(0.18 x)^2] = 6.04^2.
    sd_omo, k_etero = 6.04, 0.18
    scenari = ("omoschedastici", "eteroschedastici")

    def errori(gen, x, scenario):
        """Draw the errors of a scenario: constant spread, or spread proportional to income."""
        z = gen.normal(0.0, 1.0, x.shape)
        return z * sd_omo if scenario == "omoschedastici" else z * k_etero * x

    x = {s: rng.gamma(4.0, 7.5, (reps, n)) for s in scenari}
    err = {s: errori(rng, x[s], s) for s in scenari}
    stime = {s: _pendenze(x[s], alpha + beta * x[s] + err[s]) for s in scenari}
    righe = {s: (round(float(b.mean()), 5), round(float(b.std(ddof=1)), 5), round(float(e.mean()), 5))
             for s, (b, e) in stime.items()}
    tab = ("| scenario | media delle stime | dev. std. delle stime | media degli errori std. |\n"
           "|---|---|---|---|\n"
           + "\n".join(f"| {s} | {_fmt(m, 5)} | {_fmt(d, 5)} | {_fmt(e, 5)} |"
                       for s, (m, d, e) in righe.items()))

    def answers(r):
        """Return every answer from the (mean, sd, mean se) triple of each scenario."""
        m, d, e = r["eteroschedastici"]
        rapporto = d / e
        omo = r["omoschedastici"][1] / r["omoschedastici"][2]
        return {"nondist": "no" if abs(m - beta) / (d / np.sqrt(reps)) > 3 else "sì",
                "gm": "no", "rapporto": Numero(rapporto, 2),
                "affidabili": "sì" if abs(rapporto - 1) < 0.10 else "no",
                "affidabili_omo": "sì" if abs(omo - 1) < 0.10 else "no",
                "z": Numero(abs(m - beta) / (d / np.sqrt(reps)), 1),
                "rapporto_omo": Numero(omo, 2), "rad_r": Numero(np.sqrt(reps), 2)}

    def studente(_tabelle):
        """Rebuild the answers from the printed Monte Carlo table."""
        return answers({k: tuple(v) for k, v in _leggi(tab).items()})

    def frequenza_di_rifiuto(_risposte):
        """Check that t = (b - beta)/se rejects the true beta far above 5% only with heteroskedastic errors."""
        tassi = {k: float(np.mean(np.abs(b - beta) / e > Z)) for k, (b, e) in stime.items()}
        return 0.035 < tassi["omoschedastici"] < 0.065 and tassi["eteroschedastici"] > 0.12

    def figura(path):
        """Draw the estimates under heteroskedasticity against the normal curves of the two spreads."""
        es, plt = _stile()
        from scipy import stats

        b = stime["eteroschedastici"][0]
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        ax.hist(b, bins=45, density=True, alpha=0.45, color=es.BLUE, label="stime OLS simulate")
        g = np.linspace(b.min(), b.max(), 300)
        d, e = righe["eteroschedastici"][1], righe["eteroschedastici"][2]
        ax.plot(g, stats.norm.pdf(g, beta, d), color=es.GREEN, lw=1.8,
                label="dispersione vera delle stime")
        ax.plot(g, stats.norm.pdf(g, beta, e), color=es.RED, lw=1.8, ls="--",
                label="dispersione dichiarata dall'errore standard")
        ax.axvline(beta, color=es.GRAY, lw=1.0)
        ax.set_xlabel(r"stima OLS di $\beta$")
        ax.set_yticks([])
        ax.set_ylim(0, ax.get_ylim()[1] * 1.45)
        es.commas(ax, "x")
        ax.legend(loc="upper right")
        es.save(fig, path)

    def figura_dati(path):
        """Draw one sample per scenario: the spread around the line grows with income only in the second."""
        es, plt = _stile()
        g = np.random.default_rng(2)
        fig, axes = plt.subplots(1, 2, figsize=(6.1, 2.7), sharey=True)
        for ax, s in zip(axes, scenari):
            xs = g.gamma(4.0, 7.5, n)
            ys = alpha + beta * xs + errori(g, xs, s)
            ax.plot(xs, ys, "o", color=es.GRAY, ms=3, alpha=0.6)
            ax.plot([xs.min(), xs.max()], [alpha + beta * xs.min(), alpha + beta * xs.max()],
                    color=es.BLUE, lw=1.4)
            ax.set_title(f"errori {s}", loc="left", fontsize=9)
            ax.set_xlabel("reddito")
            es.commas(ax)
        axes[0].set_ylabel("spesa")
        fig.subplots_adjust(wspace=0.08)
        es.save(fig, path)

    truth = answers({s: (float(stime[s][0].mean()), float(stime[s][0].std(ddof=1)),
                         float(stime[s][1].mean())) for s in scenari})
    return Draft(
        dati=None,
        parametri={"reps": Numero(reps, 0), "n": Numero(n, 0), "beta": Numero(beta, 2),
                   "me": Numero(righe["eteroschedastici"][0], 5),
                   "de": Numero(righe["eteroschedastici"][1], 5),
                   "se_e": Numero(righe["eteroschedastici"][2], 5),
                   "do": Numero(righe["omoschedastici"][1], 5),
                   "se_o": Numero(righe["omoschedastici"][2], 5)},
        tabelle={"mc": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("nondist"), "b": Quesito("gm"), "c": Quesito("rapporto"),
                 "d": Quesito("affidabili"), "e": Quesito("affidabili_omo")},
        attese=[lambda r: r["nondist"] == "sì", lambda r: r["affidabili"] == "no",
                lambda r: r["affidabili_omo"] == "sì", lambda r: r["rapporto"].valore > 1.2,
                frequenza_di_rifiuto],
        margini=[Margin(stat=truth["z"].valore, crit=3.0),
                 Margin(stat=abs(truth["rapporto"].valore - 1), crit=0.10),
                 Margin(stat=abs(truth["rapporto_omo"].valore - 1), crit=0.10)],
        figure={"stime": figura, "dati": figura_dati})


@exercise("e02_09", modulo=2, livello=2, tipo=("r2-anova", "varianza-errore-standard"))
def salario_qi(rng):
    """Chain the ANOVA table into R-squared, the standard error of the slope, the t test and the F statistic."""
    n = 400
    qi = rng.normal(100.0, 15.0, n)
    y = 7.0 + 0.09 * qi + rng.normal(0.0, 5.0, n)
    res, _ = _fit(y, qi, "qi")
    ssx = float(np.sum((qi - qi.mean())**2))
    sst = float(np.sum((y - y.mean())**2))
    ssr, sse = float(res.ssr), sst - float(res.ssr)
    b_r, ssx_r = round(float(res.params[1]), 5), round(ssx, 2)
    sse_r, ssr_r, sst_r = round(sse, 2), round(ssr, 2), round(sst, 2)
    tab = ("| fonte | devianza | gdl | media delle devianze |\n|---|---|---|---|\n"
           f"| Modello (SSE) | {_fmt(sse_r, 2)} | 1 | {_fmt(sse_r, 2)} |\n"
           f"| Residuo (SSR) | {_fmt(ssr_r, 2)} | {n - 2} | {_fmt(ssr_r / (n - 2), 3)} |\n"
           f"| Totale (SST) | {_fmt(sst_r, 2)} | {n - 1} | {_fmt(sst_r / (n - 1), 3)} |")

    def answers(devianza_mod, devianza_res, devianza_tot, coef, somma_x):
        """Return every answer from the three sums of squares, the slope and the spread of x."""
        s = np.sqrt(devianza_res / (n - 2))
        se = s / np.sqrt(somma_x)
        t = coef / se
        return {"r2": Numero(devianza_mod / devianza_tot, 4), "s": Numero(s, 3),
                "gdl": Numero(n - 2, 0),
                "se": Numero(se, 4), "t": Numero(t, 2), "dec": _decide(t),
                "F": Numero(devianza_mod / (devianza_res / (n - 2)), 2),
                "t2": Numero(t**2, 2), "nessun_effetto": "sì" if _decide(t) == "non rifiuta" else "no"}

    def studente(_tabelle):
        """Rebuild the answers from the printed ANOVA rows, the slope and the sum of squares of x."""
        r = _leggi(tab)
        return answers(r["Modello (SSE)"][0], r["Residuo (SSR)"][0], r["Totale (SST)"][0], b_r, ssx_r)

    def identita(r):
        """Check F = t^2 and SSE = b^2 * SSx exactly, and the standard error against statsmodels."""
        return (abs(res.fvalue - r["t2"].valore) < 1e-6 and abs(res.fvalue - r["F"].valore) < 1e-6
                and abs(sse - res.params[1]**2 * ssx) < 1e-8 and abs(res.bse[1] - r["se"].valore) < 1e-4)

    def figura(path):
        """Draw the cloud with the fitted line next to the t test: weak fit, yet a clear slope."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1, 1.2]})
        a1.plot(qi, y, "o", color=es.GRAY, ms=2.5, alpha=0.45)
        g = np.linspace(qi.min(), qi.max(), 30)
        a1.plot(g, res.params[0] + res.params[1] * g, color=es.BLUE, lw=1.8)
        a1.set_xlabel("QI")
        a1.set_ylabel("salario")
        a1.set_title(f"$R^2$ = {res.rsquared:.4f}".replace(".", ","), loc="left", fontsize=9)
        es.commas(a1)
        es.dist_test("z", stat=res.tvalues[1], crit=Z, tail="two", ax=a2, xlim=(-7, 7))
        a2.set_ylim(0, a2.get_ylim()[1] * 1.5)
        a2.legend(loc="upper left", fontsize=7.5)
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    truth = answers(sse, ssr, sst, res.params[1], ssx)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "b": Numero(b_r, 5), "ssx": Numero(ssx_r, 2),
                   "sse": Numero(sse_r, 2), "ssr": Numero(ssr_r, 2), "sst": Numero(sst_r, 2)},
        tabelle={"anova": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("r2"), "b": Quesito("se"), "c": Quesito("t"), "d": Quesito("dec"),
                 "e": Quesito("F"), "f": Quesito("nessun_effetto")},
        attese=[lambda r: r["r2"].valore < 0.12, lambda r: r["dec"] == "rifiuta", identita],
        margini=[Margin(stat=truth["t"].valore, crit=Z)], figure={"quadro": figura})


@exercise("e02_10", modulo=2, livello=3, punti=4, tipo="test-unilaterale-su-soglia")
def visite_vendite(rng):
    """Run both one-sided tests on a threshold the point estimate exceeds, and read what can be claimed."""
    n, dx, soglia = 160, 2.0, 10.0
    visite = rng.integers(1, 16, n).astype(float)
    y = 8.2 + 0.068 * visite + rng.normal(0.0, 0.56, n)
    res, tab = _fit(y, visite, "visite")
    b, se = res.params[1], res.bse[1]

    def answers(coef, err):
        """Return every answer from the slope and its standard error."""
        k = soglia / (100 * dx)
        t = (coef - k) / err
        return {"pct": Numero(100 * dx * coef, 1), "k": Numero(k, 3), "t": Numero(t, 2),
                "dec_almeno": "rifiuta" if t < -Z1 else "non rifiuta",
                "dec_piu": "rifiuta" if t > Z1 else "non rifiuta",
                "afferma": "sì" if t > Z1 else "no", "b": Numero(coef, 4), "se": Numero(err, 4),
                "t0": Numero(coef / err, 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed row of ``visite``."""
        r = tabelle["ols"].rows["visite"]
        return answers(r["coef"], r["se"])

    def stessa_statistica(r):
        """Check the t of H0: beta = k against statsmodels and the size of the log approximation."""
        esatto = 100 * (np.exp(dx * b) - 1)
        return (abs(float(res.t_test(f"x1 = {soglia / (100 * dx)}").tvalue) - r["t"].valore) < 1e-9
                and abs(esatto - r["pct"].valore) < 0.12 * esatto)

    def figura(path):
        """Draw the two one-sided rejection regions with the observed t, which falls in neither."""
        es, plt = _stile()
        t = (b - soglia / (100 * dx)) / se
        fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.1, 4.6))
        es.dist_test("z", stat=t, crit=Z1, tail="left", ax=a1, xlim=(-4.2, 4.2),
                     title=r"Test «almeno»: $H_1:\beta<\kappa$")
        es.dist_test("z", stat=t, crit=Z1, tail="right", ax=a2, xlim=(-4.2, 4.2),
                     title=r"Test «più di»: $H_1:\beta>\kappa$")
        fig.subplots_adjust(hspace=0.6)
        es.save(fig, path)

    truth = answers(b, se)
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "dx": Numero(dx, 0), "soglia": Numero(soglia, 0)},
        tabelle={"ols": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("pct"), "b": Quesito("t"), "c": Quesito("dec_almeno"),
                 "d": Quesito("dec_piu"), "e": Quesito("afferma")},
        attese=[lambda r: r["pct"].valore > soglia, lambda r: r["dec_almeno"] == "non rifiuta",
                lambda r: r["dec_piu"] == "non rifiuta", lambda r: r["afferma"] == "no",
                stessa_statistica],
        margini=[Margin(stat=truth["t"].valore, crit=Z1), Margin(stat=truth["t"].valore, crit=Z)],
        figure={"test": figura})


@exercise("e02_11", modulo=2, livello=3, punti=4,
          tipo=("test-su-valore-specifico", "varianza-errore-standard"))
def costi_produzione(rng):
    """Build both standard errors from SSR and the spread of x, then test a slope and an intercept claim."""
    n, riv_b, riv_a = 36, 3000.0, 35000.0
    prod = rng.normal(40.0, 8.0, n)
    y = 52.0 + 3.03 * prod + rng.normal(0.0, 6.0, n)
    res, _ = _fit(y, prod, "prod")
    ssx = float(np.sum((prod - prod.mean())**2))
    a_r, b_r = round(float(res.params[0]), 4), round(float(res.params[1]), 4)
    ssr_r, ssx_r, mx_r = round(float(res.ssr), 2), round(ssx, 2), round(float(prod.mean()), 4)
    tab = f"| | coefficiente |\n|---|---|\n| const | {_fmt(a_r, 4)} |\n| prod | {_fmt(b_r, 4)} |"

    def answers(alfa, beta, ssr, somma_x, media_x):
        """Return every answer from the coefficients, SSR, the spread of x and its mean."""
        s2 = ssr / (n - 2)
        se_b = np.sqrt(s2 / somma_x)
        se_a = np.sqrt(s2 * (somma_x / n + media_x**2) / somma_x)
        ka, kb = riv_a / 1000, riv_b / 1000
        ta, tb = (alfa - ka) / se_a, (beta - kb) / se_b
        return {"s": Numero(np.sqrt(s2), 3), "se_b": Numero(se_b, 4), "se_a": Numero(se_a, 3),
                "gdl": Numero(n - 2, 0), "scala": Numero(1000, 0),
                "kb": Numero(kb, 1), "ka": Numero(ka, 0), "tb": Numero(tb, 2), "ta": Numero(ta, 2),
                "dec_b": _decide(tb), "dec_a": _decide(ta), "s2": Numero(s2, 3),
                "somma_x2": Numero(somma_x + n * media_x**2, 0)}

    def studente(_tabelle):
        """Rebuild the answers from the printed coefficients and summary numbers."""
        r = _leggi(tab)
        return answers(r["const"][0], r["prod"][0], ssr_r, ssx_r, mx_r)

    def identita_se(r):
        """Check both se formulas against statsmodels and the t of each claim against t_test."""
        return (abs(res.bse[1] - r["se_b"].valore) < 1e-9 and abs(res.bse[0] - r["se_a"].valore) < 1e-9
                and abs(float(res.t_test(f"x1 = {riv_b / 1000}").tvalue) - r["tb"].valore) < 1e-9
                and abs(float(res.t_test(f"const = {riv_a / 1000}").tvalue) - r["ta"].valore) < 1e-9)

    def figura(path):
        """Draw the two 95% intervals with the claimed values, one inside and one outside."""
        es, plt = _stile()
        fig = plt.figure(figsize=(6.1, 3.9))
        grid = fig.add_gridspec(2, 1, hspace=0.7)
        sb, sa = res.bse[1], res.bse[0]
        es.ci_line(res.params[1], res.params[1] - Z * sb, res.params[1] + Z * sb, h0=riv_b / 1000,
                   ax=fig.add_subplot(grid[0]), decimals=3,
                   xlabel=r"$\beta$: costo variabile (migliaia di euro per migliaio di pezzi)")
        es.ci_line(res.params[0], res.params[0] - Z * sa, res.params[0] + Z * sa, h0=riv_a / 1000,
                   ax=fig.add_subplot(grid[1]), decimals=2,
                   xlabel=r"$\alpha$: costi fissi (migliaia di euro)")
        es.save(fig, path)

    truth = answers(res.params[0], res.params[1], res.ssr, ssx, prod.mean())
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "riv_b": Numero(riv_b, 0), "riv_a": Numero(riv_a, 0),
                   "ssr": Numero(ssr_r, 2), "ssx": Numero(ssx_r, 2), "mx": Numero(mx_r, 4),
                   "a": Numero(a_r, 4), "b": Numero(b_r, 4)},
        tabelle={"coef": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("s"), "b": Quesito("se_b"), "c": Quesito("tb"), "d": Quesito("dec_b"),
                 "e": Quesito("se_a"), "f": Quesito("dec_a")},
        attese=[lambda r: r["dec_b"] == "non rifiuta", lambda r: r["dec_a"] == "rifiuta", identita_se],
        margini=[Margin(stat=truth["tb"].valore, crit=Z), Margin(stat=truth["ta"].valore, crit=Z)],
        figure={"intervalli": figura})


@exercise("e02_12", modulo=2, livello=3, punti=4, tipo="ic-per-verificare-un-valore")
def nord_sud(rng):
    """Compare two slopes from independent samples: the intervals overlap yet the difference is significant."""
    nn, ns = 140, 110
    sup_n = rng.normal(95.0, 22.0, nn)
    sup_s = rng.normal(90.0, 22.0, ns)
    y_n = 30.0 + 2.63 * sup_n + rng.normal(0.0, 30.0, nn)
    y_s = 22.0 + 2.20 * sup_s + rng.normal(0.0, 30.0, ns)
    rn, tab_n = _fit(y_n, sup_n, "sup")
    rs, tab_s = _fit(y_s, sup_s, "sup")

    def answers(bn, sn, bs, ss):
        """Return every answer from the two slopes and their standard errors."""
        d, sd = bn - bs, np.sqrt(sn**2 + ss**2)
        lo_n, hi_n, lo_s, hi_s = bn - Z * sn, bn + Z * sn, bs - Z * ss, bs + Z * ss
        return {"sovrapposti": "sì" if max(lo_n, lo_s) <= min(hi_n, hi_s) else "no",
                "d": Numero(d, 4), "sd": Numero(sd, 4), "lo": Numero(d - Z * sd, 4),
                "hi": Numero(d + Z * sd, 4), "signif": "sì" if abs(d) > Z * sd else "no",
                "t": Numero(d / sd, 2), "lo_n": Numero(lo_n, 3), "hi_n": Numero(hi_n, 3),
                "lo_s": Numero(lo_s, 3), "hi_s": Numero(hi_s, 3), "bn": Numero(bn, 4),
                "bs": Numero(bs, 4), "sn": Numero(sn, 4), "ss": Numero(ss, 4),
                "somma_se": Numero(sn + ss, 4), "lo_somma": Numero(d - Z * (sn + ss), 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed rows of the two samples."""
        n_, s_ = tabelle["nord"].rows["sup"], tabelle["sud"].rows["sup"]
        return answers(n_["coef"], n_["se"], s_["coef"], s_["se"])

    def varianza_differenza(r):
        """Check by simulation that Var(bn - bs) = se_n^2 + se_s^2 when the samples are independent."""
        g = np.random.default_rng(1)
        reps = 20_000
        out = []
        for x, sigma in ((sup_n, np.sqrt(rn.scale)), (sup_s, np.sqrt(rs.scale))):
            xc = x - x.mean()
            e = g.normal(0.0, sigma, (reps, x.size))
            out.append(e @ xc / np.sum(xc**2))
        empirica = np.var(out[0] - out[1], ddof=1)
        return abs(empirica / r["sd"].valore**2 - 1) < 0.06

    def sovrapposizione_netta(r):
        """Check that the overlap of the two intervals is wide, so 'overlap' is not a borderline reading."""
        return min(r["hi_n"].valore, r["hi_s"].valore) - max(r["lo_n"].valore, r["lo_s"].valore) > 0.1 * r["sd"].valore

    def figura(path):
        """Draw the two overlapping intervals above the interval of the difference with zero marked."""
        es, plt = _stile()
        fig = plt.figure(figsize=(6.1, 4.0))
        grid = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.0], hspace=0.75)
        ax = fig.add_subplot(grid[0])
        for h, res_, nome, colore in ((1, rn, "Nord", es.BLUE), (0, rs, "Sud", es.RED)):
            ax.errorbar(res_.params[1], h, xerr=Z * res_.bse[1], fmt="o", color=colore, capsize=4,
                        label=f"{nome}: intervallo al 95%")
        ax.set_yticks([])
        ax.set_ylim(-0.6, 1.6)
        ax.set_xlabel(r"$\beta$: migliaia di euro per metro quadrato")
        es.commas(ax, "x")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.45), ncol=2)
        d = rn.params[1] - rs.params[1]
        sd = np.sqrt(rn.bse[1]**2 + rs.bse[1]**2)
        es.ci_line(d, d - Z * sd, d + Z * sd, h0=0.0, ax=fig.add_subplot(grid[1]), decimals=3,
                   xlabel=r"$\beta_N-\beta_S$")
        es.save(fig, path)

    truth = answers(rn.params[1], rn.bse[1], rs.params[1], rs.bse[1])
    return Draft(
        dati=None, parametri={"nn": Numero(nn, 0), "ns": Numero(ns, 0)},
        tabelle={"nord": tab_n, "sud": tab_s}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("sovrapposti"), "b": Quesito("sd"), "c": Quesito("lo"),
                 "d": Quesito("hi"), "e": Quesito("signif")},
        attese=[lambda r: r["sovrapposti"] == "sì", lambda r: r["signif"] == "sì",
                lambda r: r["d"].valore > 0, varianza_differenza, sovrapposizione_netta],
        margini=[Margin(stat=truth["t"].valore, crit=Z)], figure={"differenza": figura})
