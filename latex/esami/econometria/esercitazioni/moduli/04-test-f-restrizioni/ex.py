"""Module 04 - F tests and multiple restrictions: dummies, interactions, linear combinations."""

import numpy as np
import statsmodels.api as sm
from scipy.stats import f as f_dist

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import ols_table, parse_table

TITOLO = "Test F e restrizioni multiple"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

ALFA = 0.05


class _Fit:
    """An OLS fit together with the labels of its regressors and its printed table."""

    def __init__(self, y, columns, *, const=True, stats=("n", "r2", "ssr")):
        """Fit ``y`` on the named columns, with a constant unless ``const`` is false."""
        self.labels = ["const", *columns] if const else list(columns)
        x = np.column_stack([columns[k] for k in columns])
        self.res = sm.OLS(y, sm.add_constant(x) if const else x).fit()
        self.tab = ols_table(self.res, labels=self.labels, stats=stats)

    def i(self, name):
        """Return the position of the coefficient ``name``."""
        return self.labels.index(name)

    def b(self, name):
        """Return the coefficient ``name``."""
        return float(self.res.params[self.i(name)])

    def rows(self):
        """Return every row as the dictionary the table parser would give, at full precision."""
        return {k: {"coef": float(self.res.params[j]), "se": float(self.res.bse[j]),
                    "t": float(self.res.tvalues[j])} for j, k in enumerate(self.labels)}

    def cov(self, a, b):
        """Return the estimated covariance between the estimators of ``a`` and ``b``."""
        return float(self.res.cov_params()[self.i(a), self.i(b)])

    def combo(self, pesi):
        """Return the estimate and the exact standard error of ``sum(w * beta)``, ``pesi`` = name -> weight."""
        w = np.zeros(len(self.labels))
        for k, v in pesi.items():
            w[self.i(k)] = v
        return float(w @ self.res.params), float(np.sqrt(w @ self.res.cov_params() @ w))

    def f_zero(self, names):
        """Return the F statistic of the joint null that the coefficients ``names`` are all zero."""
        r = np.zeros((len(names), len(self.labels)))
        for row, k in enumerate(names):
            r[row, self.i(k)] = 1.0
        return float(self.res.f_test(r).fvalue)


def _decide(t):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > Z else "non rifiuta"


def _crit(s, df):
    """Return the 5% critical value of F(s, df), rounded to the two decimals the text shows."""
    return round(float(f_dist.ppf(1 - ALFA, s, df)), 2)


def _sig(x, cifre=6):
    """Return ``x`` as a Numero with ``cifre`` significant digits, as a printed table shows it."""
    return Numero(x, max(0, cifre - 1 - int(np.floor(np.log10(abs(x))))))


def _virgola(x, decimali):
    """Return ``x`` for a figure label, with the decimal comma."""
    return f"{x:.{decimali}f}".replace(".", ",")


def _var_comb(pesi, se, cov):
    """Return the variance of ``sum(w * beta)`` from standard errors and pairwise covariances.

    Args:
        pesi: Coefficient name to its weight.
        se: Coefficient name to its standard error.
        cov: ``(a, b)`` to the covariance of the two estimators, in either order.
    """
    nomi = list(pesi)
    var = sum((pesi[k] * se[k]) ** 2 for k in nomi)
    for i, a in enumerate(nomi):
        for b in nomi[i + 1:]:
            c = cov[(a, b)] if (a, b) in cov else cov[(b, a)]
            var += 2 * pesi[a] * pesi[b] * c
    return var


def _stampato(studente, tabelle):
    """Return the answers as recomputed from the printed tables, the numbers the solution text shows."""
    return studente({k: parse_table(v) for k, v in tabelle.items()})


def _legenda(ax):
    """Move the legend of an F density to the empty middle of the panel."""
    ax.legend(loc="upper center", bbox_to_anchor=(0.55, 0.95))


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


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


@exercise("e04_01", modulo=4, livello=1, tipo="dummy-categoria-base")
def ruolo_salario(rng):
    """Read role dummies against the omitted category: two gaps, a reversed gap and two tests."""
    n = 300
    ruolo = rng.choice(3, n, p=[0.40, 0.35, 0.25])
    guardia, ala = (ruolo == 0).astype(float), (ruolo == 1).astype(float)
    punti = rng.gamma(4.0, 2.2, n)
    esper = rng.integers(0, 16, n).astype(float)
    y = (6.0 - 0.24 * guardia - 0.03 * ala + 0.055 * punti + 0.045 * esper
         + rng.normal(0, 0.55, n))
    m = _Fit(y, {"guardia": guardia, "ala": ala, "punti": punti, "esper": esper})

    def answers(rows):
        """Return every answer from the printed rows of ``guardia`` and ``ala``."""
        g, a = rows["guardia"], rows["ala"]
        return {"pct_g": Numero(100 * g["coef"], 1), "pct_c": Numero(-100 * g["coef"], 1),
                "dec_a": _decide(a["t"]), "dec_g": _decide(g["t"]),
                "bg": Numero(g["coef"], 4), "ba": Numero(a["coef"], 4),
                "tg": Numero(g["t"], 2), "ta": Numero(a["t"], 2),
                "g_lo": Numero(g["coef"] - Z * g["se"], 4), "g_hi": Numero(g["coef"] + Z * g["se"], 4),
                "a_lo": Numero(a["coef"] - Z * a["se"], 4), "a_hi": Numero(a["coef"] + Z * a["se"], 4)}

    def studente(tabelle):
        """Rebuild the answers from the printed table."""
        return answers(tabelle["ols"].rows)

    def figura(path):
        """Draw the two role coefficients, in percent, against the reference category."""
        es, plt = _stile()
        r = m.rows()
        fig, ax = plt.subplots(figsize=(6.1, 2.4))
        voci = [("centro (riferimento)", 0.0, None, None, es.GRAY)]
        for nome, k, colore in (("ala", "ala", es.TEAL), ("guardia", "guardia", es.BLUE)):
            voci.append((nome, 100 * r[k]["coef"], 100 * (r[k]["coef"] - Z * r[k]["se"]),
                         100 * (r[k]["coef"] + Z * r[k]["se"]), colore))
        _intervalli(ax, es, voci, "differenza di salario rispetto al centro, in % (intervallo al 95%)")
        es.save(fig, path)

    truth = answers(m.rows())
    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"ols": m.tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("pct_g"), "b": Quesito("pct_c"), "c": Quesito("dec_a"),
                 "d": Quesito("dec_g")},
        attese=[lambda r: r["dec_a"] == "non rifiuta", lambda r: r["dec_g"] == "rifiuta",
                lambda r: r["pct_g"].valore < 0 and r["pct_c"].valore > 0],
        margini=[Margin(stat=m.rows()["ala"]["t"], crit=Z), Margin(stat=m.rows()["guardia"]["t"], crit=Z)],
        figure={"ruoli": figura})


@exercise("e04_02", modulo=4, livello=1, tipo="test-f-calcolo-da-ssr")
def servizi_prezzo(rng):
    """Build F from the SSR of the full and the restricted model, and again from the R-squared."""
    n = 200
    mq = rng.lognormal(4.4, 0.3, n)
    eta = rng.integers(1, 60, n).astype(float)
    asc = rng.binomial(1, 0.55, n).astype(float)
    balcone = rng.binomial(1, 0.6, n).astype(float)
    box = rng.binomial(1, 0.4, n).astype(float)
    y = (3.0 + 0.85 * np.log(mq) - 0.006 * eta + 0.07 * asc + 0.012 * balcone
         + 0.008 * box + rng.normal(0, 0.25, n))
    base = {"l_mq": np.log(mq), "eta": eta, "ascensore": asc}
    comp = _Fit(y, {**base, "balcone": balcone, "box": box})
    rist = _Fit(y, base)
    s, df = 2, n - 5 - 1
    fcrit = _crit(s, df)

    def answers(c, r):
        """Return every answer from ``(ssr, r2, number of regressors)`` of the two models."""
        s_, df_ = c[2] - r[2], n - c[2] - 1
        f_ssr = ((r[0] - c[0]) / s_) / (c[0] / df_)
        f_r2 = ((c[1] - r[1]) / s_) / ((1 - c[1]) / df_)
        return {"s": Numero(s_, 0), "df": Numero(df_, 0), "k": Numero(c[2], 0), "F": Numero(f_ssr, 2),
                "F_r2": Numero(f_r2, 2), "dec": "rifiuta" if f_ssr > fcrit else "non rifiuta",
                "ssr_c": _sig(c[0]), "ssr_r": _sig(r[0]), "r2_c": _sig(c[1]), "r2_r": _sig(r[1]),
                "dssr": _sig(r[0] - c[0], 3)}

    def studente(tabelle):
        """Rebuild the answers from the statistics line and the row count of the two tables."""
        c, r = tabelle["completo"], tabelle["ristretto"]
        return answers((c.stats["ssr"], c.stats["r2"], len(c.rows) - 1),
                       (r.stats["ssr"], r.stats["r2"], len(r.rows) - 1))

    def identita(_risposte):
        """Check that the SSR form equals the R-squared form and the library F test, exactly."""
        f_ssr = ((rist.res.ssr - comp.res.ssr) / s) / (comp.res.ssr / df)
        f_r2 = ((comp.res.rsquared - rist.res.rsquared) / s) / ((1 - comp.res.rsquared) / df)
        return abs(f_ssr - f_r2) < 1e-9 and abs(f_ssr - comp.f_zero(["balcone", "box"])) < 1e-9

    def figura(path):
        """Draw the F density with the 5% rejection region and the observed statistic."""
        es, _ = _stile()
        f = _stampato(studente, tabelle)["F"].valore
        fig, ax = es.dist_test("F", (s, df), stat=f, crit=fcrit, tail="right",
                               statlabel=f"$F$ osservata = {_virgola(f, 2)}",
                               critlabel=f"regione di rifiuto: $F$ > {_virgola(fcrit, 2)}")
        _legenda(ax)
        es.save(fig, path)

    truth = answers((comp.res.ssr, comp.res.rsquared, 5), (rist.res.ssr, rist.res.rsquared, 3))
    tabelle = {"completo": comp.tab, "ristretto": rist.tab}
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "fcrit": Numero(fcrit, 2)},
        tabelle=tabelle, risposte=truth, studente=studente,
        quesiti={"a": Quesito("s"), "b": Quesito("df"), "c": Quesito("F"), "d": Quesito("F_r2"),
                 "e": Quesito("dec")},
        attese=[lambda r: r["dec"] == "non rifiuta", lambda r: r["s"].valore == 2, identita],
        margini=[Margin(stat=truth["F"].valore, crit=fcrit)], figure={"f": figura})


@exercise("e04_03", modulo=4, livello=1, tipo="test-su-combinazione-lineare-dei-coefficienti")
def rendimenti_di_scala(rng):
    """Test constant returns to scale, beta1 + beta2 = 1, with the covariance given in the text."""
    n = 120
    lk = rng.normal(4.0, 0.9, n)
    ll = 1.0 + 0.7 * lk + rng.normal(0, 0.45, n)
    esporta = rng.binomial(1, 0.4, n).astype(float)
    y = 0.8 + 0.35 * lk + 0.48 * ll + 0.10 * esporta + rng.normal(0, 0.30, n)
    m = _Fit(y, {"l_cap": lk, "l_lav": ll, "esporta": esporta})
    cov = round(m.cov("l_cap", "l_lav"), 8)

    def answers(rows, c12):
        """Return every answer from the printed rows of the two inputs and their covariance."""
        a, b = rows["l_cap"], rows["l_lav"]
        stima = a["coef"] + b["coef"]
        se = np.sqrt(a["se"] ** 2 + b["se"] ** 2 + 2 * c12)
        se_ing = np.hypot(a["se"], b["se"])
        t = (stima - 1) / se
        return {"somma": Numero(stima, 3), "se": Numero(se, 4), "t": Numero(t, 2),
                "dec": _decide(t), "F": Numero(t ** 2, 2),
                "ic_lo": Numero(stima - Z * se, 3), "ic_hi": Numero(stima + Z * se, 3),
                "se_ing": Numero(se_ing, 4), "dec_ing": _decide((stima - 1) / se_ing),
                "t_ing": Numero((stima - 1) / se_ing, 2),
                "b1": Numero(a["coef"], 4), "b2": Numero(b["coef"], 4),
                "s1": Numero(a["se"], 5), "s2": Numero(b["se"], 5)}

    def studente(tabelle):
        """Rebuild the answers from the printed table and the covariance of the text."""
        return answers(tabelle["ols"].rows, cov)

    def coerente(r):
        """Check the hand-built standard error against the library's linear-combination test."""
        _, se_lib = m.combo({"l_cap": 1.0, "l_lav": 1.0})
        t_lib = float(m.res.t_test((np.array([[0, 1, 1, 0]]), 1.0)).tvalue[0, 0])
        vincolato = _Fit(y - ll, {"l_cap_su_lav": lk - ll, "esporta": esporta})
        f_ssr = (vincolato.res.ssr - m.res.ssr) / (m.res.ssr / m.res.df_resid)
        return (abs(se_lib - r["se"].valore) < 1e-4
                and abs((m.b("l_cap") + m.b("l_lav") - 1) / se_lib - t_lib) < 1e-9
                and abs(f_ssr - t_lib ** 2) < 1e-8 and abs(r["F"].valore - f_ssr) < 0.02)

    def figura(path):
        """Draw the 95% interval of beta1 + beta2 against the constant-returns value."""
        es, _ = _stile()
        v = _stampato(studente, tabelle)
        fig, _ax = es.ci_line(v["somma"].valore, v["ic_lo"].valore, v["ic_hi"].valore, h0=1.0,
                              decimals=3, xlabel=r"$\beta_1+\beta_2$ (rendimenti di scala)")
        es.save(fig, path)

    truth = answers(m.rows(), cov)
    tabelle = {"ols": m.tab}
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "cov": Numero(cov, 8)}, tabelle=tabelle,
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("somma"), "b": Quesito("se"), "c": Quesito("t"),
                 "d": Quesito("dec"), "e": Quesito("F")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["dec_ing"] == "non rifiuta",
                lambda r: r["somma"].valore < 1, coerente],
        margini=[Margin(stat=truth["t"].valore, crit=Z),
                 Margin(stat=(truth["somma"].valore - 1) / truth["se_ing"].valore, crit=Z)],
        figure={"ic": figura})


@exercise("e04_04", modulo=4, livello=2,
          tipo=("sistema-ipotesi-f-dummy-congiunte", "dummy-categoria-base", "test-f-calcolo-da-ssr"))
def titolo_di_studio(rng):
    """Test that a three-category qualification does not matter, with F built from the R-squared."""
    n = 350
    liv = rng.choice(3, n, p=[0.30, 0.45, 0.25])
    obbl, dipl = (liv == 0).astype(float), (liv == 1).astype(float)
    esper = rng.integers(0, 31, n).astype(float)
    anz = np.minimum(rng.integers(0, 16, n), esper).astype(float)
    y = (6.9 - 0.34 * obbl - 0.17 * dipl + 0.015 * esper + 0.010 * anz + rng.normal(0, 0.45, n))
    cols = {"obbligo": obbl, "diploma": dipl, "esper": esper, "anz": anz}
    comp = _Fit(y, cols, stats=("n", "r2"))
    rist = _Fit(y, {"esper": esper, "anz": anz}, stats=("n", "r2"))
    s, df = 2, n - 4 - 1
    fcrit = _crit(s, df)

    def answers(rows, r2_c, k_c, r2_r, k_r):
        """Return every answer from the full rows, the two R-squared and the regressor counts."""
        s_, df_ = k_c - k_r, n - k_c - 1
        f = ((r2_c - r2_r) / s_) / ((1 - r2_c) / df_)
        return {"s": Numero(s_, 0), "df": Numero(df_, 0), "k": Numero(k_c, 0), "F": Numero(f, 2),
                "dec": "rifiuta" if f > fcrit else "non rifiuta", "inv": "no",
                "r2_c": _sig(r2_c), "r2_r": _sig(r2_r), "dr2": _sig(r2_c - r2_r, 3),
                "d1": Numero(rows["obbligo"]["coef"], 4), "d2": Numero(rows["diploma"]["coef"], 4),
                "t1": Numero(rows["obbligo"]["t"], 2), "t2": Numero(rows["diploma"]["t"], 2)}

    def studente(tabelle):
        """Rebuild the answers from the statistics line and the row count of the two tables."""
        c, r = tabelle["completo"], tabelle["ristretto"]
        return answers(c.rows, c.stats["r2"], len(c.rows) - 1, r.stats["r2"], len(r.rows) - 1)

    def invarianza(_risposte):
        """Check that another reference category gives the same fit and the same F, exactly."""
        altro = _Fit(y, {"obbligo": obbl, "laurea": 1.0 - obbl - dipl, "esper": esper, "anz": anz})
        stessi = np.allclose(altro.res.fittedvalues, comp.res.fittedvalues, atol=1e-9)
        return (stessi and abs(altro.res.ssr - comp.res.ssr) < 1e-9
                and abs(comp.f_zero(["obbligo", "diploma"]) - truth["F"].valore) < 0.01)

    def figura(path):
        """Draw the F density with the 5% rejection region and the observed statistic."""
        es, _ = _stile()
        f = _stampato(studente, tabelle)["F"].valore
        fig, ax = es.dist_test("F", (s, df), stat=f, crit=fcrit, tail="right",
                               statlabel=f"$F$ osservata = {_virgola(f, 2)}",
                               critlabel=f"regione di rifiuto: $F$ > {_virgola(fcrit, 2)}")
        _legenda(ax)
        es.save(fig, path)

    truth = answers(comp.rows(), comp.res.rsquared, 4, rist.res.rsquared, 2)
    tabelle = {"completo": comp.tab, "ristretto": rist.tab}
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "fcrit": Numero(fcrit, 2)},
        tabelle=tabelle, risposte=truth, studente=studente,
        quesiti={"c": Quesito("s"), "d": Quesito("df"), "e": Quesito("F"), "f": Quesito("dec"),
                 "g": Quesito("inv")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["s"].valore == 2, invarianza],
        margini=[Margin(stat=truth["F"].valore, crit=fcrit)], figure={"f": figura})


@exercise("e04_05", modulo=4, livello=2, tipo="interazione-effetto-marginale-condizionato")
def istruzione_genere(rng):
    """Read a dummy-by-regressor interaction: two slopes, a test, a gap at a given schooling."""
    n, e0 = 500, 16.0
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(0, 31, n).astype(float)
    donna = rng.binomial(1, 0.5, n).astype(float)
    y = (1.20 + 0.078 * istr - 0.10 * donna + 0.012 * esper - 0.015 * donna * istr
         + rng.normal(0, 0.40, n))
    m = _Fit(y, {"istr": istr, "donna": donna, "esper": esper, "d_istr": donna * istr})

    def answers(rows):
        """Return every answer from the printed rows of ``istr``, ``donna`` and ``d_istr``."""
        b1, b2, b4 = rows["istr"], rows["donna"], rows["d_istr"]
        return {"eff_u": Numero(100 * b1["coef"], 1), "eff_d": Numero(100 * (b1["coef"] + b4["coef"]), 1),
                "dec": _decide(b4["t"]), "gap": Numero(100 * (b2["coef"] + e0 * b4["coef"]), 1),
                "solo": "no", "b1": Numero(b1["coef"], 4), "b2": Numero(b2["coef"], 4),
                "b4": Numero(b4["coef"], 4), "t4": Numero(b4["t"], 2),
                "lo4": Numero(b4["coef"] - Z * b4["se"], 4), "hi4": Numero(b4["coef"] + Z * b4["se"], 4)}

    def studente(tabelle):
        """Rebuild the answers from the printed table."""
        return answers(tabelle["ols"].rows)

    def effetti_coerenti(r):
        """Check the slopes and the gap against differences of the fitted log wage."""
        def fitted(i, d, e):
            """Return the fitted log wage at schooling ``i``, gender ``d``, experience ``e``."""
            return float(m.res.params @ np.array([1.0, i, d, e, d * i]))

        uomo = fitted(13.0, 0.0, 10.0) - fitted(12.0, 0.0, 10.0)
        donna_ = fitted(13.0, 1.0, 10.0) - fitted(12.0, 1.0, 10.0)
        gap = fitted(e0, 1.0, 10.0) - fitted(e0, 0.0, 10.0)
        return (abs(100 * uomo - r["eff_u"].valore) < 0.05 and abs(100 * donna_ - r["eff_d"].valore) < 0.05
                and abs(100 * gap - r["gap"].valore) < 0.05)

    def figura(path):
        """Draw the two fitted lines of log wage on schooling and the gap at ``e0`` years."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.1))
        x = np.linspace(8, 20, 50)
        base = m.b("const") + m.b("esper") * esper.mean()
        uomo = base + m.b("istr") * x
        donna_ = base + m.b("donna") + (m.b("istr") + m.b("d_istr")) * x
        ax.plot(x, uomo, color=es.BLUE, lw=1.6,
                label=f"uomini: pendenza {_virgola(m.b('istr'), 4)}")
        ax.plot(x, donna_, color=es.RED, lw=1.6,
                label=f"donne: pendenza {_virgola(m.b('istr') + m.b('d_istr'), 4)}")
        yu, yd = base + m.b("istr") * e0, base + m.b("donna") + (m.b("istr") + m.b("d_istr")) * e0
        ax.vlines(e0, yd, yu, color=es.GREEN, lw=2.2)
        ax.annotate(f"differenza a {e0:g} anni:\n{_virgola(yd - yu, 3)}", xy=(e0, yd),
                    xytext=(8, -12), textcoords="offset points", ha="left", va="top",
                    fontsize=8.5, color=es.GREEN, fontweight="bold")
        ax.set_xlabel("anni di istruzione")
        ax.set_ylabel("log(salario) atteso, a esperienza media")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    truth = answers(m.rows())
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "e0": Numero(e0, 0)}, tabelle={"ols": m.tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("eff_u"), "b": Quesito("eff_d"), "c": Quesito("dec"),
                 "d": Quesito("gap"), "e": Quesito("solo")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["eff_d"].valore < r["eff_u"].valore,
                lambda r: r["gap"].valore < 0, effetti_coerenti],
        margini=[Margin(stat=m.rows()["d_istr"]["t"], crit=Z)], figure={"rette": figura})


@exercise("e04_06", modulo=4, livello=2,
          tipo=("differenza-tra-profili-combinazione-lineare", "dummy-categoria-base",
                "test-su-combinazione-lineare-dei-coefficienti"))
def profili_lavoratori(rng):
    """Compare two worker profiles that differ in group and experience: a two-term combination."""
    n, ea, eb = 400, 12.0, 5.0
    sposato = rng.binomial(1, 0.6, n).astype(float)
    laureato = rng.binomial(1, 0.3, n).astype(float)
    sp_nl, si_l, sp_l = sposato * (1 - laureato), (1 - sposato) * laureato, sposato * laureato
    esper = np.clip(np.round(rng.normal(8 + 10 * sposato - 2 * laureato, 6)), 0, 35)
    y = (6.8 + 0.08 * sp_nl + 0.25 * si_l + 0.33 * sp_l + 0.018 * esper + rng.normal(0, 0.45, n))
    m = _Fit(y, {"sp_nl": sp_nl, "si_l": si_l, "sp_l": sp_l, "esper": esper})
    cov = round(m.cov("sp_l", "esper"), 9)
    d = ea - eb

    def answers(rows, c):
        """Return every answer from the printed rows of ``sp_l`` and ``esper`` and their covariance."""
        a, b = rows["sp_l"], rows["esper"]
        stima = a["coef"] + d * b["coef"]
        se = np.sqrt(a["se"] ** 2 + d ** 2 * b["se"] ** 2 + 2 * d * c)
        se_ing = np.sqrt(a["se"] ** 2 + d ** 2 * b["se"] ** 2)
        return {"diff": Numero(100 * stima, 1), "se": Numero(100 * se, 2),
                "lo": Numero(100 * (stima - Z * se), 1), "hi": Numero(100 * (stima + Z * se), 1),
                "dec": _decide(stima / se), "t": Numero(stima / se, 2),
                "se_ing": Numero(100 * se_ing, 2), "dex": Numero(d, 0),
                "b1": Numero(a["coef"], 4), "b2": Numero(b["coef"], 4),
                "s1": Numero(a["se"], 5), "s2": Numero(b["se"], 6),
                "stima": Numero(stima, 4), "var": Numero(se ** 2, 6)}

    def studente(tabelle):
        """Rebuild the answers from the printed table and the covariance of the text."""
        return answers(tabelle["ols"].rows, cov)

    def coerente(r):
        """Check the hand-built estimate and standard error against the library's linear combination."""
        stima, se = m.combo({"sp_l": 1.0, "esper": d})
        return abs(100 * stima - r["diff"].valore) < 0.05 and abs(100 * se - r["se"].valore) < 0.01

    def figura(path):
        """Draw the 95% interval of the percentage difference between the two profiles."""
        es, _ = _stile()
        v = _stampato(studente, tabelle)
        fig, _ax = es.ci_line(v["diff"].valore, v["lo"].valore, v["hi"].valore, h0=0.0, decimals=1,
                              xlabel="differenza attesa fra i due lavoratori, in %")
        es.save(fig, path)

    truth = answers(m.rows(), cov)
    tabelle = {"ols": m.tab}
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "ea": Numero(ea, 0), "eb": Numero(eb, 0), "cov": Numero(cov, 9)},
        tabelle=tabelle, risposte=truth, studente=studente,
        quesiti={"b": Quesito("diff"), "c": Quesito("se"), "d": Quesito("lo"), "e": Quesito("hi"),
                 "f": Quesito("dec")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["diff"].valore > 0, coerente],
        margini=[Margin(stat=truth["diff"].valore / truth["se"].valore, crit=Z)],
        figure={"ic": figura})


@exercise("e04_07", modulo=4, livello=2, tipo="test-f-calcolo-da-ssr")
def punteggi_collineari(rng):
    """Show three non-significant t ratios next to a significant joint F test."""
    n = 100
    abil = rng.normal(0, 1, n)
    mat = 50 + 10 * abil + rng.normal(0, 3.5, n)
    logica = 50 + 10 * abil + rng.normal(0, 3.5, n)
    lingua = 50 + 10 * abil + rng.normal(0, 3.5, n)
    y = 7.2 + 0.016 * mat + 0.010 * logica + 0.010 * lingua + rng.normal(0, 0.35, n)
    m = _Fit(y, {"p_mat": mat, "p_logica": logica, "p_lingua": lingua}, stats=("n", "r2"))
    s, df = 3, n - 3 - 1
    fcrit = _crit(s, df)
    nomi = ["p_mat", "p_logica", "p_lingua"]

    def answers(rows, r2, k):
        """Return every answer from the printed rows, the R-squared and the regressor count."""
        df_ = n - k - 1
        f = (r2 / k) / ((1 - r2) / df_)
        return {"conta": Numero(sum(abs(rows[v]["t"]) > Z for v in nomi), 0), "s": Numero(k, 0),
                "df": Numero(df_, 0), "F": Numero(f, 2),
                "dec": "rifiuta" if f > fcrit else "non rifiuta",
                "prob": Numero(1 - (1 - ALFA) ** k, 4), "r2": _sig(r2),
                "t1": Numero(rows[nomi[0]]["t"], 2), "t2": Numero(rows[nomi[1]]["t"], 2),
                "t3": Numero(rows[nomi[2]]["t"], 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed table."""
        t = tabelle["ols"]
        return answers(t.rows, t.stats["r2"], len(t.rows) - 1)

    def identita(_risposte):
        """Check that the R-squared form is the library's overall F test, exactly."""
        return abs(m.res.fvalue - truth["F"].valore) < 0.01 and abs(m.f_zero(nomi) - m.res.fvalue) < 1e-9

    def figura(path):
        """Draw the three coefficient intervals, all around zero, next to the joint F test."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.7), gridspec_kw={"width_ratios": [1, 1.2]})
        r = m.rows()
        voci = [(k, r[k]["coef"], r[k]["coef"] - Z * r[k]["se"], r[k]["coef"] + Z * r[k]["se"], c)
                for k, c in zip(nomi, (es.BLUE, es.TEAL, es.AMBER))]
        _intervalli(a1, es, voci, "coefficiente, con intervallo al 95%")
        f = _stampato(studente, tabelle)["F"].valore
        es.dist_test("F", (s, df), stat=f, crit=fcrit, tail="right", ax=a2,
                     statlabel=f"$F$ = {_virgola(f, 2)}",
                     critlabel=f"rifiuto: $F$ > {_virgola(fcrit, 2)}")
        a2.legend(loc="upper center", bbox_to_anchor=(0.42, 0.95))
        fig.subplots_adjust(wspace=0.35)
        es.save(fig, path)

    truth = answers(m.rows(), m.res.rsquared, 3)
    tabelle = {"ols": m.tab}
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "fcrit": Numero(fcrit, 2)}, tabelle=tabelle,
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("conta"), "b": Quesito("s"), "c": Quesito("df"), "d": Quesito("F"),
                 "e": Quesito("dec"), "f": Quesito("prob")},
        attese=[lambda r: r["conta"].valore == 0, lambda r: r["dec"] == "rifiuta", identita],
        margini=[Margin(stat=m.rows()[v]["t"], crit=Z) for v in nomi]
        + [Margin(stat=truth["F"].valore, crit=fcrit)],
        figure={"congiunto": figura})


@exercise("e04_08", modulo=4, livello=3, punti=4,
          tipo=("interazione-effetto-marginale-condizionato",
                "test-su-combinazione-lineare-dei-coefficienti"))
def istruzione_esperienza(rng):
    """Evaluate and test the marginal effect of schooling at a given experience, with an interaction."""
    n, x0 = 300, 20.0
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(0, 36, n).astype(float)
    donna = rng.binomial(1, 0.45, n).astype(float)
    y = (1.20 - 0.015 * istr + 0.008 * esper + 0.00245 * istr * esper - 0.11 * donna
         + rng.normal(0, 0.60, n))
    m = _Fit(y, {"istr": istr, "esper": esper, "istr_esp": istr * esper, "donna": donna})
    cov = round(m.cov("istr", "istr_esp"), 9)

    def answers(rows, c):
        """Return every answer from the printed rows and the covariance of the text."""
        b1, b3 = rows["istr"], rows["istr_esp"]
        eff = b1["coef"] + x0 * b3["coef"]
        se = np.sqrt(b1["se"] ** 2 + x0 ** 2 * b3["se"] ** 2 + 2 * x0 * c)
        se_ing = np.hypot(b1["se"], x0 * b3["se"])
        return {"dec_b3": _decide(b3["t"]), "dec_b1": _decide(b1["t"]),
                "eff": Numero(100 * eff, 2), "se": Numero(100 * se, 2), "dec_eff": _decide(eff / se),
                "t_eff": Numero(eff / se, 2), "lo": Numero(100 * (eff - Z * se), 2),
                "hi": Numero(100 * (eff + Z * se), 2), "se_ing": Numero(100 * se_ing, 2),
                "dec_ing": _decide(eff / se_ing), "t_ing": Numero(eff / se_ing, 2),
                "b1": Numero(b1["coef"], 5),
                "b3": Numero(b3["coef"], 6), "t1": Numero(b1["t"], 2), "t3": Numero(b3["t"], 2),
                "s1": Numero(b1["se"], 5), "s3": Numero(b3["se"], 6)}

    def studente(tabelle):
        """Rebuild the answers from the printed table and the covariance of the text."""
        return answers(tabelle["ols"].rows, cov)

    def derivata_coerente(r):
        """Check the effect and its standard error against a numeric derivative and the library."""
        def fitted(i):
            """Return the fitted log wage at schooling ``i``, experience ``x0``, man."""
            return float(m.res.params @ np.array([1.0, i, x0, i * x0, 0.0]))

        h = 1e-4
        derivata = (fitted(12.0 + h) - fitted(12.0 - h)) / (2 * h)
        eff, se = m.combo({"istr": 1.0, "istr_esp": x0})
        return (abs(derivata - eff) < 1e-8 and abs(100 * eff - r["eff"].valore) < 0.01
                and abs(100 * se - r["se"].valore) < 0.01)

    def ricentrata(_risposte):
        """Check that centring experience at ``x0`` turns the combination into a plain coefficient."""
        c = _Fit(y, {"istr": istr, "esper_c": esper - x0, "istr_c": istr * (esper - x0), "donna": donna})
        eff, se = m.combo({"istr": 1.0, "istr_esp": x0})
        return abs(c.b("istr") - eff) < 1e-9 and abs(c.rows()["istr"]["se"] - se) < 1e-9

    def figura(path):
        """Draw the marginal effect of schooling against experience, with the band from the covariance."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.1))
        x = np.linspace(0, 35, 200)
        w = np.zeros((len(x), len(m.labels)))
        w[:, m.i("istr")], w[:, m.i("istr_esp")] = 1.0, x
        eff = w @ m.res.params
        err = np.sqrt(np.einsum("ij,jk,ik->i", w, m.res.cov_params(), w))
        ax.fill_between(x, 100 * (eff - Z * err), 100 * (eff + Z * err), color=es.BLUEBG,
                        label="intervallo di confidenza al 95%")
        ax.plot(x, 100 * eff, color=es.BLUE, lw=1.6, label="effetto marginale stimato")
        ax.axhline(0, color=es.RED, ls="--", lw=1.0)
        ax.plot([x0], [_stampato(studente, tabelle)["eff"].valore], "o", color=es.GREEN, ms=7, zorder=5)
        ax.plot([0], [100 * m.b("istr")], "s", color=es.AMBER, ms=6, zorder=5)
        ax.set_xlabel("anni di esperienza")
        ax.set_ylabel("effetto di un anno di istruzione, in %")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    truth = answers(m.rows(), cov)
    tabelle = {"ols": m.tab}
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "x0": Numero(x0, 0), "cov": Numero(cov, 9)},
        tabelle=tabelle, risposte=truth, studente=studente,
        quesiti={"b": Quesito("dec_b3"), "c": Quesito("dec_b1"), "d": Quesito("eff"),
                 "e": Quesito("se"), "f": Quesito("dec_eff")},
        attese=[lambda r: r["dec_b3"] == "rifiuta", lambda r: r["dec_b1"] == "non rifiuta",
                lambda r: r["dec_eff"] == "rifiuta", lambda r: r["dec_ing"] == "non rifiuta",
                derivata_coerente, ricentrata],
        margini=[Margin(stat=m.rows()["istr_esp"]["t"], crit=Z), Margin(stat=m.rows()["istr"]["t"], crit=Z),
                 Margin(stat=truth["t_eff"].valore, crit=Z),
                 Margin(stat=truth["eff"].valore / truth["se_ing"].valore, crit=Z)],
        figure={"effetto": figura})


@exercise("e04_09", modulo=4, livello=3, punti=4,
          tipo=("differenza-tra-profili-combinazione-lineare",
                "interazione-effetto-marginale-condizionato",
                "test-su-combinazione-lineare-dei-coefficienti"))
def promozione_pubblicita(rng):
    """Test a claim on the advertising effect under promotion and compare two shops on three terms."""
    n, pa, pb, kappa = 450, 5.0, 3.0, 0.02
    promo = rng.binomial(1, 0.5, n).astype(float)
    pub = rng.gamma(3.0, 1.5, n)
    y = (8.0 + 0.18 * promo + 0.052 * pub - 0.030 * pub * promo + rng.normal(0, 0.25, n))
    m = _Fit(y, {"promo": promo, "pub": pub, "pub_promo": pub * promo})
    nomi = ("promo", "pub", "pub_promo")
    covs = {(a, b): round(m.cov(a, b), 9) for i, a in enumerate(nomi) for b in nomi[i + 1:]}
    w = {"promo": 1.0, "pub": pa - pb, "pub_promo": pa}

    def answers(rows, c):
        """Return every answer from the printed rows and the three covariances of the text."""
        se = {k: rows[k]["se"] for k in nomi}
        eff = rows["pub"]["coef"] + rows["pub_promo"]["coef"]
        se_eff = np.sqrt(_var_comb({"pub": 1.0, "pub_promo": 1.0}, se, c))
        diff = sum(w[k] * rows[k]["coef"] for k in nomi)
        se_diff = np.sqrt(_var_comb(w, se, c))
        t_riv = (eff - kappa) / se_eff
        return {"eff": Numero(100 * eff, 2), "dec_riv": _decide(t_riv), "t_riv": Numero(t_riv, 2),
                "eff_lo": Numero(eff - Z * se_eff, 4), "eff_hi": Numero(eff + Z * se_eff, 4),
                "se_eff": Numero(se_eff, 4), "diff": Numero(100 * diff, 1),
                "se_diff": Numero(100 * se_diff, 2), "dec_diff": _decide(diff / se_diff),
                "lo": Numero(100 * (diff - Z * se_diff), 1), "hi": Numero(100 * (diff + Z * se_diff), 1),
                "t_diff": Numero(diff / se_diff, 2), "b_eff": Numero(eff, 4),
                "dpub": Numero(pa - pb, 0), "var_diff": Numero(se_diff ** 2, 6),
                "var_eff": Numero(se_eff ** 2, 6), "diff_u": Numero(diff, 4),
                "b1": Numero(rows["promo"]["coef"], 4), "b2": Numero(rows["pub"]["coef"], 4),
                "b3": Numero(rows["pub_promo"]["coef"], 4), "s1": Numero(se["promo"], 6),
                "s2": Numero(se["pub"], 6), "s3": Numero(se["pub_promo"], 6)}

    def studente(tabelle):
        """Rebuild the answers from the printed table and the covariances of the text."""
        return answers(tabelle["ols"].rows, covs)

    def coerente(r):
        """Check both combinations against the library's linear-combination standard errors."""
        eff, se_eff = m.combo({"pub": 1.0, "pub_promo": 1.0})
        diff, se_diff = m.combo(w)
        return (abs(100 * eff - r["eff"].valore) < 0.01 and abs(se_eff - r["se_eff"].valore) < 1e-4
                and abs(100 * diff - r["diff"].valore) < 0.05 and abs(100 * se_diff - r["se_diff"].valore) < 0.01)

    def previsioni_coerenti(r):
        """Check that the difference is the gap of the fitted log sales of the two shops."""
        def fitted(p, x):
            """Return the fitted log sales for promotion ``p`` and advertising ``x``."""
            return float(m.res.params @ np.array([1.0, p, x, p * x]))

        return abs(100 * (fitted(1.0, pa) - fitted(0.0, pb)) - r["diff"].valore) < 0.05

    def figura(path):
        """Draw the two fitted lines with the two shops, and the interval of their gap."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1.3, 1]})
        x = np.linspace(0, 9, 50)

        def retta(p, x_):
            """Return the fitted log sales at promotion ``p`` and advertising ``x_``."""
            return m.b("const") + m.b("promo") * p + (m.b("pub") + m.b("pub_promo") * p) * x_

        a1.plot(x, retta(0.0, x), color=es.BLUE, lw=1.6, label="senza promozione")
        a1.plot(x, retta(1.0, x), color=es.RED, lw=1.6, label="con promozione")
        a1.plot([pb], [retta(0.0, pb)], "o", color=es.BLUE, ms=7, zorder=5)
        a1.plot([pa], [retta(1.0, pa)], "o", color=es.RED, ms=7, zorder=5)
        a1.annotate("B", xy=(pb, retta(0.0, pb)), xytext=(-9, 5), textcoords="offset points",
                    fontsize=9, color=es.BLUE, fontweight="bold")
        a1.annotate("A", xy=(pa, retta(1.0, pa)), xytext=(6, 5), textcoords="offset points",
                    fontsize=9, color=es.RED, fontweight="bold")
        a1.set_xlabel("pubblicità")
        a1.set_ylabel("log(vendite) atteso")
        es.commas(a1)
        a1.legend(loc="upper left")
        v = _stampato(studente, tabelle)
        es.ci_line(v["diff"].valore, v["lo"].valore, v["hi"].valore, h0=0.0, ax=a2,
                   decimals=1, xlabel="A meno B, in %")
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    truth = answers(m.rows(), covs)
    tabelle = {"ols": m.tab}
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "pa": Numero(pa, 0), "pb": Numero(pb, 0),
                   "kappa": Numero(kappa, 2), "c_pp": Numero(covs[("pub", "pub_promo")], 9),
                   "c_ap": Numero(covs[("promo", "pub")], 9),
                   "c_ai": Numero(covs[("promo", "pub_promo")], 9)},
        tabelle=tabelle, risposte=truth, studente=studente,
        quesiti={"a": Quesito("eff"), "b": Quesito("dec_riv"), "c": Quesito("diff"),
                 "d": Quesito("se_diff"), "e": Quesito("dec_diff")},
        attese=[lambda r: r["dec_riv"] == "non rifiuta", lambda r: r["dec_diff"] == "rifiuta",
                coerente, previsioni_coerenti],
        margini=[Margin(stat=truth["t_riv"].valore, crit=Z), Margin(stat=truth["t_diff"].valore, crit=Z)],
        figure={"profili": figura})


@exercise("e04_10", modulo=4, livello=3, punti=4,
          tipo=("sistema-ipotesi-f-dummy-congiunte", "dummy-categoria-base", "test-f-calcolo-da-ssr"))
def zone_senza_costante(rng):
    """Test equal zone levels in a model without constant, via the SSR, and re-read it with a base zone."""
    n = 400
    zona = rng.choice(4, n, p=[0.30, 0.25, 0.20, 0.25])
    zs = {f"zona{j + 1}": (zona == j).astype(float) for j in range(4)}
    crime = rng.gamma(2.0, 2.0, n)
    rooms = rng.normal(6.2, 0.7, n)
    livelli = np.array([8.40, 8.15, 8.70, 8.52])
    y = livelli[zona] - 0.015 * crime + 0.12 * rooms + rng.normal(0, 0.30, n)
    comp = _Fit(y, {**zs, "crime": crime, "rooms": rooms}, const=False, stats=("n", "ssr"))
    rist = _Fit(y, {"crime": crime, "rooms": rooms}, stats=("n", "ssr"))
    s, df = 3, n - 6
    fcrit = _crit(s, df)

    def answers(rows, ssr_c, p_c, ssr_r, p_r):
        """Return every answer from the zone rows, the SSR and the parameter count of the two tables."""
        s_, df_ = p_c - p_r, n - p_c
        f = ((ssr_r - ssr_c) / s_) / (ssr_c / df_)
        d = [rows[f"zona{j}"]["coef"] for j in (1, 2, 3, 4)]
        return {"s": Numero(s_, 0), "df": Numero(df_, 0), "F": Numero(f, 2),
                "dec": "rifiuta" if f > fcrit else "non rifiuta",
                "coef1": Numero(100 * (d[0] - d[3]), 1), "cost": Numero(d[3], 3),
                "ssr_c": _sig(ssr_c), "ssr_r": _sig(ssr_r), "dssr": _sig(ssr_r - ssr_c, 3),
                "d1": Numero(d[0], 3), "d2": Numero(d[1], 3), "d3": Numero(d[2], 3),
                "d4": Numero(d[3], 3), "p": Numero(p_c, 0), "p_r": Numero(p_r, 0)}

    def studente(tabelle):
        """Rebuild the answers from the two printed tables."""
        c, r = tabelle["completo"], tabelle["ristretto"]
        return answers(c.rows, c.stats["ssr"], len(c.rows), r.stats["ssr"], len(r.rows))

    def riparametrizzazione(r):
        """Check that a constant plus three zone dummies gives the same fit, F and re-read coefficients."""
        alt = _Fit(y, {"zona1": zs["zona1"], "zona2": zs["zona2"], "zona3": zs["zona3"],
                       "crime": crime, "rooms": rooms}, stats=("n", "ssr"))
        stesso = (np.allclose(alt.res.fittedvalues, comp.res.fittedvalues, atol=1e-9)
                  and abs(alt.res.ssr - comp.res.ssr) < 1e-9)
        f_lib = alt.f_zero(["zona1", "zona2", "zona3"])
        return (stesso and abs(f_lib - r["F"].valore) < 0.01
                and abs(100 * alt.b("zona1") - r["coef1"].valore) < 0.05
                and abs(alt.b("const") - r["cost"].valore) < 1e-3)

    def figura(path):
        """Draw the four zone levels with the restricted constant, and the gaps from zone 4 with intervals."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.8), gridspec_kw={"width_ratios": [1, 1.2]})
        r = comp.rows()
        colori = (es.BLUE, es.TEAL, es.AMBER, es.GREEN)
        for j in (1, 2, 3, 4):
            a1.plot([r[f"zona{j}"]["coef"]], [j - 1], "o", color=colori[j - 1], ms=7)
        a1.axvline(rist.b("const"), color=es.GRAY, ls="--", lw=1.0)
        a1.annotate("costante del\nmodello ristretto", xy=(rist.b("const"), 3.8), xytext=(4, 0),
                    textcoords="offset points", ha="left", va="bottom", fontsize=8.5, color=es.GRAY)
        a1.margins(x=0.12)
        a1.set_yticks(range(4), [f"zona {j}" for j in (1, 2, 3, 4)])
        a1.set_ylim(-0.6, 4.9)
        a1.set_xlabel("livello stimato $\\hat\\delta_j$")
        es.commas(a1, "x")
        voci = []
        for j in (1, 2, 3):
            diff, se = comp.combo({f"zona{j}": 1.0, "zona4": -1.0})
            voci.append((f"zona {j}", 100 * diff, 100 * (diff - Z * se),
                         100 * (diff + Z * se), colori[j - 1]))
        _intervalli(a2, es, voci, "differenza dalla zona 4, in %")
        fig.subplots_adjust(wspace=0.4)
        es.save(fig, path)

    truth = answers(comp.rows(), comp.res.ssr, 6, rist.res.ssr, 3)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "fcrit": Numero(fcrit, 2)},
        tabelle={"completo": comp.tab, "ristretto": rist.tab}, risposte=truth, studente=studente,
        quesiti={"c": Quesito("s"), "d": Quesito("df"), "e": Quesito("F"), "f": Quesito("dec"),
                 "g": Quesito("cost"), "h": Quesito("coef1")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["s"].valore == 3, riparametrizzazione],
        margini=[Margin(stat=truth["F"].valore, crit=fcrit)], figure={"livelli": figura})


@exercise("e04_11", modulo=4, livello=3, punti=4,
          tipo=("dummy-categoria-base", "differenza-tra-profili-combinazione-lineare"))
def area_geografica(rng):
    """Change the reference area: the new coefficients are linear combinations of the printed ones."""
    n = 360
    area = rng.choice(3, n, p=[0.40, 0.20, 0.40])
    nord, sud = (area == 0).astype(float), (area == 2).astype(float)
    istr = rng.integers(8, 21, n).astype(float)
    eta = rng.integers(25, 66, n).astype(float)
    y = 9.0 + 0.04 * nord - 0.08 * sud + 0.045 * istr + 0.010 * eta + rng.normal(0, 0.50, n)
    m = _Fit(y, {"nord": nord, "sud": sud, "istr": istr, "eta": eta})
    cov = round(m.cov("nord", "sud"), 9)

    def answers(rows, c):
        """Return every answer from the printed rows of ``nord`` and ``sud`` and their covariance."""
        a, b = rows["nord"], rows["sud"]
        diff = a["coef"] - b["coef"]
        se = np.sqrt(a["se"] ** 2 + b["se"] ** 2 - 2 * c)
        se_ing = np.hypot(a["se"], b["se"])
        return {"dec_nc": _decide(a["t"]), "dec_sc": _decide(b["t"]),
                "centro": Numero(-100 * b["coef"], 1), "nord": Numero(100 * diff, 1),
                "se": Numero(100 * se, 2), "dec_ns": _decide(diff / se), "t_ns": Numero(diff / se, 2),
                "inv": "no", "lo": Numero(100 * (diff - Z * se), 1),
                "hi": Numero(100 * (diff + Z * se), 1), "se_ing": Numero(100 * se_ing, 2),
                "dec_ing": _decide(diff / se_ing), "bn": Numero(a["coef"], 4),
                "bs": Numero(b["coef"], 4), "sn": Numero(a["se"], 5), "ss": Numero(b["se"], 5),
                "tn": Numero(a["t"], 2), "ts": Numero(b["t"], 2)}

    def studente(tabelle):
        """Rebuild the answers from the printed table and the covariance of the text."""
        return answers(tabelle["ols"].rows, cov)

    def riparametrizzazione(r):
        """Check that estimating with the south as base reproduces the combinations, the fit and the F."""
        alt = _Fit(y, {"centro": 1.0 - nord - sud, "nord": nord, "istr": istr, "eta": eta})
        ok_fit = (np.allclose(alt.res.fittedvalues, m.res.fittedvalues, atol=1e-9)
                  and abs(alt.res.ssr - m.res.ssr) < 1e-9)
        ok_coef = (abs(100 * alt.b("centro") - r["centro"].valore) < 0.05
                   and abs(100 * alt.b("nord") - r["nord"].valore) < 0.05
                   and abs(100 * alt.rows()["nord"]["se"] - r["se"].valore) < 0.01)
        return ok_fit and ok_coef and abs(alt.f_zero(["centro", "nord"]) - m.f_zero(["nord", "sud"])) < 1e-8

    def figura(path):
        """Draw the area coefficients with the centre as base and with the south as base."""
        es, plt = _stile()
        r = m.rows()
        d = m.b("nord") - m.b("sud")
        se_ns = np.sqrt(r["nord"]["se"] ** 2 + r["sud"]["se"] ** 2 - 2 * cov)
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.6), sharex=True)
        _intervalli(a1, es, [("centro (base)", 0.0, None, None, es.GRAY),
                             ("nord", 100 * r["nord"]["coef"], 100 * (r["nord"]["coef"] - Z * r["nord"]["se"]),
                              100 * (r["nord"]["coef"] + Z * r["nord"]["se"]), es.TEAL),
                             ("sud", 100 * r["sud"]["coef"], 100 * (r["sud"]["coef"] - Z * r["sud"]["se"]),
                              100 * (r["sud"]["coef"] + Z * r["sud"]["se"]), es.BLUE)],
                    "base centro, in %")
        _intervalli(a2, es, [("sud (base)", 0.0, None, None, es.GRAY),
                             ("nord", 100 * d, 100 * (d - Z * se_ns), 100 * (d + Z * se_ns), es.TEAL),
                             ("centro", -100 * m.b("sud"), -100 * (m.b("sud") + Z * r["sud"]["se"]),
                              -100 * (m.b("sud") - Z * r["sud"]["se"]), es.AMBER)],
                    "base sud, in %")
        fig.subplots_adjust(wspace=0.45)
        es.save(fig, path)

    truth = answers(m.rows(), cov)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "cov": Numero(cov, 9)}, tabelle={"ols": m.tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec_nc"), "b": Quesito("dec_sc"), "c": Quesito("centro"),
                 "d": Quesito("nord"), "e": Quesito("se"), "f": Quesito("dec_ns"),
                 "g": Quesito("inv")},
        attese=[lambda r: r["dec_nc"] == "non rifiuta", lambda r: r["dec_sc"] == "non rifiuta",
                lambda r: r["dec_ns"] == "rifiuta", lambda r: r["dec_ing"] == "non rifiuta",
                riparametrizzazione],
        margini=[Margin(stat=m.rows()["nord"]["t"], crit=Z), Margin(stat=m.rows()["sud"]["t"], crit=Z),
                 Margin(stat=truth["t_ns"].valore, crit=Z),
                 Margin(stat=(m.b("nord") - m.b("sud")) / (truth["se_ing"].valore / 100), crit=Z)],
        figure={"basi": figura})


@exercise("e04_12", modulo=4, livello=3, punti=4,
          tipo=("test-f-calcolo-da-ssr", "test-su-combinazione-lineare-dei-coefficienti"))
def restrizioni_miste(rng):
    """Test two restrictions at once by rewriting the model, and link the single one to a squared t."""
    n = 500
    istr = rng.integers(8, 21, n).astype(float)
    esper = rng.integers(0, 31, n).astype(float)
    anz = np.minimum(rng.integers(0, 16, n), esper).astype(float)
    donna = rng.binomial(1, 0.45, n).astype(float)
    y = (1.0 + 0.062 * istr + 0.024 * esper + 0.014 * anz - 0.11 * donna + rng.normal(0, 0.40, n))
    comp = _Fit(y, {"istr": istr, "esper": esper, "anz": anz, "donna": donna})
    rist = _Fit(y, {"istr_esper": istr + esper, "donna": donna})
    cov = round(comp.cov("istr", "esper"), 9)
    s, df = 2, n - 4 - 1
    fcrit = _crit(s, df)

    def answers(rows, ssr_c, k_c, ssr_r, k_r, c):
        """Return every answer from the full rows, the SSR and regressor counts and the covariance."""
        s_, df_ = k_c - k_r, n - k_c - 1
        f = ((ssr_r - ssr_c) / s_) / (ssr_c / df_)
        a, b = rows["istr"], rows["esper"]
        se_dif = np.sqrt(a["se"] ** 2 + b["se"] ** 2 - 2 * c)
        t = (a["coef"] - b["coef"]) / se_dif
        return {"s": Numero(s_, 0), "df": Numero(df_, 0), "k": Numero(k_c, 0), "F": Numero(f, 2),
                "dec": "rifiuta" if f > fcrit else "non rifiuta", "F1": Numero(t ** 2, 2),
                "dec1": _decide(t), "t1": Numero(t, 2), "ssr_c": _sig(ssr_c), "ssr_r": _sig(ssr_r),
                "dssr": _sig(ssr_r - ssr_c, 3), "b1": Numero(a["coef"], 4), "b2": Numero(b["coef"], 4),
                "s1": Numero(a["se"], 6), "s2": Numero(b["se"], 6),
                "dif": Numero(a["coef"] - b["coef"], 4), "se_dif": Numero(se_dif, 5),
                "t_anz": Numero(rows["anz"]["t"], 2)}

    def studente(tabelle):
        """Rebuild the answers from the two printed tables and the covariance of the text."""
        c, r = tabelle["completo"], tabelle["ristretto"]
        return answers(c.rows, c.stats["ssr"], len(c.rows) - 1, r.stats["ssr"], len(r.rows) - 1, cov)

    def identita(r):
        """Check F against the library, and F = t^2 for the single restriction via its own restricted fit."""
        restr = np.array([[0, 1, -1, 0, 0], [0, 0, 0, 1, 0]], dtype=float)
        f_lib = float(comp.res.f_test(restr).fvalue)
        solo = _Fit(y, {"istr_esper": istr + esper, "anz": anz, "donna": donna})
        f_solo = ((solo.res.ssr - comp.res.ssr) / 1) / (comp.res.ssr / df)
        return (abs(f_lib - r["F"].valore) < 0.01 and abs(f_solo - r["F1"].valore) < 0.05)

    def figura(path):
        """Draw the SSR of the two models and the F density with the rejection region."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.8), gridspec_kw={"width_ratios": [0.8, 1.4]})
        a1.bar([0, 1], [comp.res.ssr, rist.res.ssr], color=[es.BLUE, es.RED], width=0.6)
        for pos, v in ((0, comp.res.ssr), (1, rist.res.ssr)):
            a1.annotate(_virgola(v, 1), xy=(pos, v), xytext=(0, 3), textcoords="offset points",
                        ha="center", fontsize=8.5)
        a1.set_xticks([0, 1], ["completo", "ristretto"])
        a1.set_ylim(0, rist.res.ssr * 1.12)
        a1.set_ylabel("SSR")
        es.commas(a1, "y")
        f = _stampato(studente, tabelle)["F"].valore
        es.dist_test("F", (s, df), stat=f, crit=fcrit, tail="right", ax=a2,
                     statlabel=f"$F$ = {_virgola(f, 2)}",
                     critlabel=f"rifiuto: $F$ > {_virgola(fcrit, 2)}")
        a2.legend(loc="upper center", bbox_to_anchor=(0.42, 0.95))
        fig.subplots_adjust(wspace=0.35)
        es.save(fig, path)

    truth = answers(comp.rows(), comp.res.ssr, 4, rist.res.ssr, 2, cov)
    tabelle = {"completo": comp.tab, "ristretto": rist.tab}
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "fcrit": Numero(fcrit, 2), "cov": Numero(cov, 9)},
        tabelle=tabelle, risposte=truth, studente=studente,
        quesiti={"a": Quesito("s"), "b": Quesito("df"), "c": Quesito("F"), "d": Quesito("dec"),
                 "e": Quesito("F1"), "f": Quesito("dec1")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["dec1"] == "rifiuta",
                lambda r: r["s"].valore == 2, identita],
        margini=[Margin(stat=truth["F"].valore, crit=fcrit), Margin(stat=truth["t1"].valore, crit=Z)],
        figure={"f": figura})
