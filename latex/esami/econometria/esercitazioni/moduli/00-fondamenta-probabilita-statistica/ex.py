"""Module 00 - foundations: association, covariance, sampling, confidence intervals and tests."""

import numpy as np
from scipy import stats

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise

TITOLO = "Fondamenta di probabilità e statistica"

# Normal quantiles the exam texts fix: two-sided 5%, one-sided 5% and two-sided 1%.
Z = 1.96
Z_UNI = 1.64
Z_99 = 2.57


def _cella(x, dec):
    """Format ``x`` as a math-mode table cell with a decimal comma."""
    text = f"{x:.{dec}f}"
    # A value that rounds to zero must not keep its sign.
    if float(text) == 0:
        text = text.lstrip("-")
    return "$" + text.replace(".", "{,}") + "$"


def _tabella(intestazione, righe):
    """Build a Markdown pipe table from a header and rows of ready-made cells."""
    linee = ["| " + " | ".join(intestazione) + " |", "|" + "---|" * len(intestazione)]
    linee += ["| " + " | ".join(r) + " |" for r in righe]
    return "\n".join(linee)


def _leggi(testo):
    """Return the numeric cells of each row of a printed table, as the student reads them.

    Labels and header cells are skipped, so a row of the table gives only its numbers.
    """
    righe = []
    for linea in testo.splitlines():
        if not linea.startswith("|"):
            continue
        numeri = []
        for cella in (c.strip() for c in linea.strip().strip("|").split("|")):
            try:
                numeri.append(float(cella.replace("$", "").replace("{,}", ".").replace(",", ".")))
            except ValueError:
                continue
        if numeri:
            righe.append(numeri)
    return righe


def _it(x, dec=2):
    """Format ``x`` with a decimal comma, for text drawn inside figures."""
    return f"{x:.{dec}f}".replace(".", ",")


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


@exercise("e00_01", modulo=0, livello=1,
          tipo=("associazione-variabili-categoriche", "probabilita-condizionata-e-indipendenza"))
def titolo_e_smart_working(rng):
    """Read conditional distributions off a contingency table and judge the association."""
    soglia = 10.0
    dip = rng.multinomial(int(rng.integers(520, 600)), [0.30, 0.28, 0.42])
    lau = rng.multinomial(int(rng.integers(600, 680)), [0.55, 0.25, 0.20])
    tot = dip + lau

    def riga(nome, v):
        """Return a table row: label, the three counts and their total."""
        return [nome, *(_cella(float(c), 0) for c in v), _cella(float(v.sum()), 0)]

    tab = _tabella(["", "favorevole", "indifferente", "contrario", "totale"],
                   [riga("Diplomati", dip), riga("Laureati", lau), riga("Totale", tot)])

    def answers(m):
        """Return every answer from the printed counts of the two groups."""
        d, l = np.array(m[0][:3]), np.array(m[1][:3])
        n_d, n_l, fav = d.sum(), l.sum(), d[0] + l[0]
        cd, cl = 100 * d / n_d, 100 * l / n_l
        diff = cl - cd
        massimo = float(np.abs(diff).max())
        return {
            "cond": Numero(cl[0], 1), "inversa": Numero(100 * l[0] / fav, 1),
            "assoc": "sì" if massimo > soglia else "no",
            "attesi": Numero(n_l * fav / (n_d + n_l), 1),
            "n_dip": Numero(n_d, 0), "n_lau": Numero(n_l, 0), "fav": Numero(fav, 0),
            "lau_fav": Numero(l[0], 0), "tot": Numero(n_d + n_l, 0),
            "p_fav": Numero(100 * fav / (n_d + n_l), 1),
            "cd_f": Numero(cd[0], 1), "cd_i": Numero(cd[1], 1), "cd_c": Numero(cd[2], 1),
            "cl_f": Numero(cl[0], 1), "cl_i": Numero(cl[1], 1), "cl_c": Numero(cl[2], 1),
            "diff_f": Numero(diff[0], 1), "diff_i": Numero(diff[1], 1),
            "diff_c": Numero(diff[2], 1), "massimo": Numero(massimo, 1),
        }

    def studente(_tabelle):
        """Rebuild the answers from the counts of the printed table."""
        return answers(_leggi(tab))

    def attesi_indipendenti(_risposte):
        """Check that the counts expected under independence give identical conditional rows."""
        att = np.outer([dip.sum(), lau.sum()], tot) / tot.sum()
        righe = att / att.sum(axis=1, keepdims=True)
        return bool(np.allclose(righe[0], righe[1]) and np.allclose(righe[0], tot / tot.sum()))

    def figura(path):
        """Draw the two conditional distributions against the overall one."""
        es, plt = _stile()
        r = truth
        cd = [r["cd_f"].valore, r["cd_i"].valore, r["cd_c"].valore]
        cl = [r["cl_f"].valore, r["cl_i"].valore, r["cl_c"].valore]
        tutti = 100 * tot / tot.sum()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        pos, w = np.arange(3), 0.34
        ax.bar(pos - w / 2, cd, w, color=es.BLUE, label="diplomati")
        ax.bar(pos + w / 2, cl, w, color=es.AMBER, label="laureati")
        ax.plot(pos, tutti, "D", color=es.RED, ms=6, zorder=5,
                label="distribuzione complessiva (caso di indipendenza)")
        ax.set_xticks(pos, ["favorevole", "indifferente", "contrario"])
        ax.set_ylabel("% all'interno del gruppo")
        ax.set_ylim(0, max(cd + cl) * 1.4)
        es.commas(ax, "y")
        ax.legend(loc="upper right", fontsize=8)
        es.save(fig, path)

    truth = answers([[*dip, dip.sum()], [*lau, lau.sum()], [*tot, tot.sum()]])
    return Draft(
        dati=(dip, lau), parametri={"soglia": Numero(soglia, 0)}, tabelle={"cont": tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("cond"), "b": Quesito("inversa"), "c": Quesito("assoc"),
                 "d": Quesito("attesi")},
        attese=[lambda r: r["assoc"] == "sì", lambda r: r["cond"].valore > r["cd_f"].valore + soglia,
                lambda r: abs(r["lau_fav"].valore - r["attesi"].valore) > 0.1 * r["attesi"].valore,
                attesi_indipendenti],
        margini=[Margin(stat=truth["massimo"].valore, crit=soglia)],
        figure={"condizionali": figura})


@exercise("e00_02", modulo=0, livello=1, tipo="covarianza-e-sue-proprieta")
def ore_di_studio_e_voti(rng):
    """Compute a sample covariance from six pairs and apply its linearity properties."""
    n, scala, bonus = 6, 60, 2
    while True:
        x = np.sort(rng.choice(np.arange(3, 21), size=n, replace=False)).astype(float)
        y = np.clip(np.round(16 + 0.7 * x + rng.normal(0, 1.8, n)), 18, 30)
        # Integer means keep the hand computation on whole deviations; spread-out hours
        # keep one pair from carrying the whole covariance.
        if (x.sum() % n == 0 and y.sum() % n == 0 and np.diff(x).min() >= 2
                and np.corrcoef(x, y)[0, 1] > 0.7):
            break
    tab = _tabella(["studente", "ore di studio $X$", "voto $Y$"],
                   [[f"S{i + 1}", _cella(x[i], 0), _cella(y[i], 0)] for i in range(n)])

    def answers(xs, ys):
        """Return every answer from the printed hours and marks."""
        mx, my = xs.mean(), ys.mean()
        prodotti = (xs - mx) * (ys - my)
        sxy = prodotti.sum() / len(xs)
        return {"cov": Numero(sxy, 2), "cov_t": Numero(scala * sxy, 0),
                "cov_xx": Numero(((xs - mx) ** 2).sum() / len(xs), 2),
                "stesso": "sì" if sxy > 0 else "no",
                "mx": Numero(mx, 0), "my": Numero(my, 0), "somma": Numero(prodotti.sum(), 0)}

    def studente(_tabelle):
        """Rebuild the answers from the printed pairs."""
        righe = np.array(_leggi(tab))
        return answers(righe[:, 0], righe[:, 1])

    def proprieta_coerenti(r):
        """Check linearity, symmetry and cov(X, X) = Var(X) directly on the data."""
        diretta = np.cov(scala * x, y + bonus, bias=True)[0, 1]
        return (abs(diretta - r["cov_t"].valore) < 1e-9
                and abs(np.cov(y, x, bias=True)[0, 1] - np.cov(x, y, bias=True)[0, 1]) < 1e-12
                and abs(np.cov(x, x, bias=True)[0, 1] - r["cov_xx"].valore) < 1e-9)

    def figura(path):
        """Draw the pairs around their means: positive products are blue, negative red."""
        es, plt = _stile()
        mx, my = x.mean(), y.mean()
        pos = (x - mx) * (y - my) > 0
        fig, ax = plt.subplots(figsize=(6.1, 3.1))
        ax.axvline(mx, color=es.GRAY, ls="--", lw=1.0)
        ax.axhline(my, color=es.GRAY, ls="--", lw=1.0)
        ax.plot(x[pos], y[pos], "o", color=es.BLUE, ms=7, label="$(x_i-\\bar x)(y_i-\\bar y)>0$")
        ax.plot(x[~pos], y[~pos], "o", color=es.RED, ms=7, label="$(x_i-\\bar x)(y_i-\\bar y)<0$")
        ax.set_xlabel("ore di studio")
        ax.set_ylabel("voto")
        es.commas(ax)
        ax.legend(loc="lower right", fontsize=8)
        es.save(fig, path)

    truth = answers(x, y)
    return Draft(
        dati=(x, y),
        parametri={"n": Numero(n, 0), "scala": Numero(scala, 0), "bonus": Numero(bonus, 0)},
        tabelle={"dati": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("cov"), "b": Quesito("cov_t"), "c": Quesito("cov_xx"),
                 "d": Quesito("stesso")},
        attese=[lambda r: r["cov"].valore > 1, lambda r: r["stesso"] == "sì", proprieta_coerenti],
        figure={"quadranti": figura})


@exercise("e00_03", modulo=0, livello=1,
          tipo=("media-e-varianza-di-una-somma", "correlazione-e-indipendenza"))
def redditi_della_coppia(rng):
    """Combine the moments of two incomes into those of their sum and difference."""
    m = 400
    sd = np.array([0.80, 0.60])
    corr = 0.45
    cov_pop = np.array([[sd[0] ** 2, corr * sd[0] * sd[1]], [corr * sd[0] * sd[1], sd[1] ** 2]])
    xy = rng.multivariate_normal([2.1, 1.6], cov_pop, m)
    x, y = xy[:, 0], xy[:, 1]
    mx, my = round(float(x.mean()), 2), round(float(y.mean()), 2)
    sx, sy = round(float(x.std(ddof=1)), 2), round(float(y.std(ddof=1)), 2)
    cov = round(float(np.cov(x, y)[0, 1]), 3)
    tab = _tabella(["", "media", "dev. std."],
                   [["$X$ (marito)", _cella(mx, 2), _cella(sx, 2)],
                    ["$Y$ (moglie)", _cella(my, 2), _cella(sy, 2)]])

    def answers(medie, sds, c):
        """Return every answer from the printed means, standard deviations and covariance."""
        (ma, mb), (sa, sb) = medie, sds
        return {"media_z": Numero(ma + mb, 2), "var_z": Numero(sa**2 + sb**2 + 2 * c, 3),
                "rho": Numero(c / (sa * sb), 3), "var_d": Numero(sa**2 + sb**2 - 2 * c, 3),
                "minore": "sì" if c > 0 else "no", "var_x": Numero(sa**2, 4),
                "var_y": Numero(sb**2, 4), "var_ind": Numero(sa**2 + sb**2, 3),
                "sd_z": Numero(np.sqrt(sa**2 + sb**2 + 2 * c), 3),
                "mx": Numero(ma, 2), "my": Numero(mb, 2), "sx": Numero(sa, 2), "sy": Numero(sb, 2)}

    def studente(_tabelle):
        """Rebuild the answers from the printed table and the printed covariance."""
        (ma, sa), (mb, sb) = _leggi(tab)
        return answers((ma, mb), (sa, sb), cov)

    def identita(_risposte):
        """Check Var(X+Y) and Var(X-Y) on the sample, where the identities are exact."""

        def v(z):
            """Return the sample variance of ``z``."""
            return np.var(z, ddof=1)

        c = np.cov(x, y)[0, 1]
        return (abs(v(x + y) - (v(x) + v(y) + 2 * c)) < 1e-9
                and abs(v(x - y) - (v(x) + v(y) - 2 * c)) < 1e-9)

    def figura(path):
        """Draw the sum of the incomes against the sum obtained with the pairing broken."""
        es, plt = _stile()
        indip = x + np.random.default_rng(0).permutation(y)
        z = x + y
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        griglia = np.linspace(1.2, 6.4, 27)
        altezze, _, _ = ax.hist(z, bins=griglia, density=True, color=es.BLUEBG, edgecolor=es.BLUE,
                                lw=0.6, label=f"$Z=X+Y$ osservata, dev. std. {_it(z.std(ddof=1))}")
        ax.hist(indip, bins=griglia, density=True, histtype="step", color=es.RED, lw=1.5,
                label=f"coppie rimescolate (indipendenza), dev. std. {_it(indip.std(ddof=1))}")
        ax.set_ylim(0, altezze.max() * 1.6)
        ax.set_xlabel("reddito familiare (migliaia di euro al mese)")
        ax.set_ylabel("densità")
        es.commas(ax)
        ax.set_yticks([])
        ax.legend(loc="upper right", fontsize=8)
        es.save(fig, path)

    truth = answers((mx, my), (sx, sy), cov)
    return Draft(
        dati=(x, y), parametri={"cov": Numero(cov, 3)}, tabelle={"stat": tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("media_z"), "b": Quesito("var_z"), "c": Quesito("rho"),
                 "d": Quesito("var_d"), "e": Quesito("minore")},
        attese=[lambda r: 0.2 < r["rho"].valore < 0.8, lambda r: r["var_z"].valore > r["var_ind"].valore,
                lambda r: r["var_d"].valore < r["var_ind"].valore, identita],
        figure={"somma": figura})


@exercise("e00_04", modulo=0, livello=1, tipo="variabile-casuale-valore-atteso-varianza")
def rendimento_con_leva(rng):
    """Compute mean and variance of a discrete variable and of a linear transformation of it."""
    valori = np.array([-4.0, -1.0, 2.0, 5.0, 8.0])
    a, c = 3, 2
    while True:
        k = rng.multinomial(10, rng.dirichlet(np.full(5, 4.0)))
        p = k / 10
        # Tenths make mean and variance exact at one and two decimals.
        if k.min() >= 1 and k.max() <= 4 and 0.5 < float(valori @ p) < 3.5:
            break
    tab = _tabella(["$x$", "$P(X=x)$"], [[_cella(v, 0), _cella(q, 1)] for v, q in zip(valori, p)])

    def answers(xs, ps):
        """Return every answer from the printed support and probabilities."""
        mu = float(xs @ ps)
        var = float(((xs - mu) ** 2) @ ps)
        return {"mu": Numero(mu, 1), "var": Numero(var, 2), "mu_y": Numero(a * mu - c, 1),
                "var_y": Numero(a**2 * var, 2), "sd": Numero(np.sqrt(var), 2),
                "sd_y": Numero(a * np.sqrt(var), 2), "ex2": Numero(float((xs**2) @ ps), 1),
                "a2": Numero(a**2, 0), "p_neg": Numero(float(ps[xs < 0].sum()), 2),
                **{f"x{i + 1}": Numero(v, 0) for i, v in enumerate(xs)},
                **{f"p{i + 1}": Numero(q, 1) for i, q in enumerate(ps)}}

    def studente(_tabelle):
        """Rebuild the answers from the printed probability table."""
        righe = np.array(_leggi(tab))
        return answers(righe[:, 0], righe[:, 1])

    def trasformazione_coerente(r):
        """Check E[aX-c] and Var(aX-c) directly on the distribution of Y = aX - c."""
        y = a * valori - c
        mu_y = float(y @ p)
        return (abs(mu_y - r["mu_y"].valore) < 1e-9
                and abs(float(((y - mu_y) ** 2) @ p) - r["var_y"].valore) < 1e-9
                and abs(p.sum() - 1.0) < 1e-12)

    def figura(path):
        """Draw the distribution of X and of Y = aX - c with mean and standard deviation."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.7))
        for ax, xs, nome, mu, sd, colore in (
                (a1, valori, "$X$", truth["mu"].valore, truth["sd"].valore, es.BLUE),
                (a2, a * valori - c, "$Y=aX-c$", truth["mu_y"].valore, truth["sd_y"].valore, es.AMBER)):
            ax.bar(xs, p, width=0.4 * (xs[1] - xs[0]), color=colore)
            ax.axvline(mu, color=es.RED, lw=1.4, label=f"media {_it(mu)}")
            ax.axvspan(mu - sd, mu + sd, color=es.REDBG, alpha=0.7, zorder=0,
                       label=f"media $\\pm$ dev. std. ({_it(sd)})")
            ax.set_xlabel(nome)
            ax.set_ylabel("probabilità")
            es.commas(ax)
            ax.legend(loc="upper left", fontsize=7)
            ax.set_ylim(0, p.max() * 1.9)
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    truth = answers(valori, p)
    return Draft(
        dati=(valori, p), parametri={"a": Numero(a, 0), "c": Numero(c, 0)}, tabelle={"distr": tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("mu"), "b": Quesito("var"), "c": Quesito("mu_y"),
                 "d": Quesito("var_y")},
        attese=[lambda r: r["mu"].valore > 0.5, lambda r: r["var_y"].valore > 5 * r["var"].valore,
                trasformazione_coerente],
        figure={"distribuzioni": figura})


@exercise("e00_05", modulo=0, livello=1, tipo="intervallo-di-confidenza-per-la-media")
def tempo_di_attesa(rng):
    """Build confidence intervals for a mean at 95% and 99% and decide on a claim with the first."""
    n = 100
    campione = rng.normal(24.0, 9.0, n)
    media, sd = round(float(campione.mean()), 1), round(float(campione.std(ddof=1)), 2)
    # The claim sits at least 2.6 standard errors away, so the interval decides it clearly.
    mu0 = float(np.ceil(media + 2.6 * sd / np.sqrt(n)))
    tab = _tabella(["", "$n$", "media $\\bar y$", "dev. std. $s$"],
                   [["tempo di attesa (minuti)", _cella(n, 0), _cella(media, 1), _cella(sd, 2)]])

    def answers(dim, ybar, s):
        """Return every answer from the printed sample size, mean and standard deviation."""
        se = s / np.sqrt(dim)
        return {"se": Numero(se, 3), "lo": Numero(ybar - Z * se, 2), "hi": Numero(ybar + Z * se, 2),
                "ampiezza": Numero(2 * Z_99 * se, 2),
                "dec": "rifiuta" if abs(ybar - mu0) > Z * se else "non rifiuta", "singoli": "no",
                "n": Numero(dim, 0), "ybar": Numero(ybar, 1), "s": Numero(s, 2),
                "m95": Numero(Z * se, 2),
                "m99": Numero(Z_99 * se, 2), "lo99": Numero(ybar - Z_99 * se, 2),
                "hi99": Numero(ybar + Z_99 * se, 2), "t": Numero((ybar - mu0) / se, 2),
                "lo_s": Numero(ybar - Z * s, 1), "hi_s": Numero(ybar + Z * s, 1)}

    def studente(_tabelle):
        """Rebuild the answers from the printed summary row."""
        dim, ybar, s = _leggi(tab)[0]
        return answers(dim, ybar, s)

    def pochi_nell_intervallo(r):
        """Check on the sample that few single waiting times fall inside the interval of the mean."""
        dentro = (campione >= r["lo"].valore) & (campione <= r["hi"].valore)
        return dentro.mean() < 0.3

    def figura(path):
        """Draw the 99% and 95% intervals of the mean and the range of single values."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 2.6))
        for y0, mezza, colore in ((2, truth["m99"].valore, es.TEAL), (1, truth["m95"].valore, es.BLUE),
                                  (0, Z * sd, es.GRAY)):
            ax.errorbar(media, y0, xerr=mezza, fmt="o", color=colore, capsize=4, lw=2)
        ax.axvline(mu0, color=es.RED, ls="--", lw=1.2)
        ax.annotate("valore dichiarato", xy=(mu0, 2.35), ha="center", fontsize=8.5, color=es.RED)
        ax.set_yticks([0, 1, 2], ["singoli valori\n(media ± 1,96 s)", "IC al 95%", "IC al 99%"])
        ax.set_ylim(-0.5, 2.7)
        ax.set_xlabel("minuti")
        es.commas(ax, "x")
        es.save(fig, path)

    truth = answers(n, media, sd)
    return Draft(
        dati=campione, parametri={"mu0": Numero(mu0, 0)}, tabelle={"stat": tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("se"), "b": Quesito("lo"), "c": Quesito("hi"),
                 "d": Quesito("ampiezza"), "e": Quesito("dec"), "f": Quesito("singoli")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["hi"].valore < mu0 or r["lo"].valore > mu0,
                pochi_nell_intervallo],
        margini=[Margin(stat=truth["t"].valore, crit=Z)], figure={"intervalli": figura})


@exercise("e00_06", modulo=0, livello=1,
          tipo=("test-unilaterali-e-bilaterali-sulla-media", "logica-del-test-e-p-value"))
def peso_delle_confezioni(rng):
    """Run the three tests on a mean on the same data and read the p-value."""
    n, mu0 = 100, 500.0
    while True:
        s = round(float(rng.uniform(3.0, 4.6)), 1)
        media = round(mu0 + float(rng.uniform(-3.3, -2.7)) * s / np.sqrt(n), 1)
        t = (media - mu0) / (s / np.sqrt(n))
        if -3.3 <= t <= -2.7:
            break
    p_sx = round(float(stats.norm.cdf(t)), 4)
    tab = _tabella(["", "$n$", "media $\\bar y$", "dev. std. $s$"],
                   [["peso (grammi)", _cella(n, 0), _cella(media, 1), _cella(s, 1)]])

    def answers(dim, ybar, sd, p):
        """Return every answer from the printed summary row and the one-sided p-value."""
        se = sd / np.sqrt(dim)
        t_obs = (ybar - mu0) / se
        return {"t": Numero(t_obs, 2), "dec_sx": "rifiuta" if t_obs < -Z_UNI else "non rifiuta",
                "dec_dx": "rifiuta" if t_obs > Z_UNI else "non rifiuta",
                "dec_bi": "rifiuta" if abs(t_obs) > Z else "non rifiuta",
                "p_bi": Numero(2 * p, 4), "vera": "no", "se": Numero(se, 3),
                "diff": Numero(ybar - mu0, 1), "p_dx": Numero(1 - p, 4), "n": Numero(dim, 0),
                "t_abs": Numero(abs(t_obs), 2),
                "ybar": Numero(ybar, 1), "s": Numero(sd, 1)}

    def studente(_tabelle):
        """Rebuild the answers from the printed row and the printed p-value."""
        dim, ybar, sd = _leggi(tab)[0]
        return answers(dim, ybar, sd, p_sx)

    def figura(path):
        """Draw the null distribution with the observed t and the three rejection regions."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        x = np.linspace(-4.8, 4.8, 600)
        y = stats.norm.pdf(x)
        ax.plot(x, y, color=es.BLUE, lw=1.4)
        ax.fill_between(x, y, color=es.BLUEBG)
        sx_ = x <= -Z_UNI
        dx_ = x >= Z_UNI
        ax.fill_between(x[sx_], y[sx_], color=es.RED, alpha=0.35,
                        label="rifiuto per $H_1:\\mu<\\mu_0$ ($t$ < −1,64)")
        ax.fill_between(x[dx_], y[dx_], color=es.AMBER, alpha=0.35,
                        label="rifiuto per $H_1:\\mu>\\mu_0$ ($t$ > 1,64)")
        ax.axvline(-Z, color=es.GRAY, ls="--", lw=1.0, label="valori critici del test bilaterale: ±1,96")
        ax.axvline(Z, color=es.GRAY, ls="--", lw=1.0)
        ax.axvline(t, color=es.GREEN, lw=2.0, label=f"$t$ osservata = {_it(t)}")
        ax.set_xlabel("valore della statistica $t$ sotto $H_0$")
        ax.set_yticks([])
        ax.set_ylim(0, 0.62)
        es.commas(ax, "x")
        ax.legend(loc="upper left", fontsize=7.5)
        es.save(fig, path)

    truth = answers(n, media, s, p_sx)
    return Draft(
        dati=None, parametri={"mu0": Numero(mu0, 0), "p_sx": Numero(p_sx, 4)}, tabelle={"stat": tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("t"), "b": Quesito("dec_sx"), "c": Quesito("dec_dx"),
                 "d": Quesito("dec_bi"), "e": Quesito("p_bi", tolleranza=0.0002),
                 "f": Quesito("vera")},
        attese=[lambda r: r["dec_sx"] == "rifiuta", lambda r: r["dec_dx"] == "non rifiuta",
                lambda r: r["dec_bi"] == "rifiuta", lambda r: abs(stats.norm.cdf(t) - p_sx) < 6e-5],
        margini=[Margin(stat=t, crit=Z), Margin(stat=t, crit=Z_UNI)], figure={"regioni": figura})


@exercise("e00_07", modulo=0, livello=2,
          tipo=("campionamento-casuale-semplice", "media-campionaria-correttezza-e-errore-standard",
                "teorema-del-limite-centrale"))
def reddito_campionato(rng):
    """Derive mean, standard error and normal approximation of a sample mean under random sampling."""
    mu, sigma, n, obiettivo = 28.0, 12.0, 64, 1.0
    s_log = np.sqrt(np.log(1 + (sigma / mu) ** 2))
    m_log = np.log(mu) - s_log**2 / 2
    pop = rng.lognormal(m_log, s_log, size=(20000, n))
    medie = pop.mean(axis=1)
    ybar = round(mu + float(rng.uniform(2.4, 3.0)) * sigma / np.sqrt(n), 1)
    par = {"mu": Numero(mu, 0), "sigma": Numero(sigma, 0), "n": Numero(n, 0),
           "obiettivo": Numero(obiettivo, 0), "ybar": Numero(ybar, 1)}

    def answers(m, sg, dim, ob, y):
        """Return every answer from the population moments, the sample size and the observed mean."""
        se = sg / np.sqrt(dim)
        c = Z * se
        return {"var_somma": Numero(2 * sg**2, 0), "corretta": "sì", "se": Numero(se, 2),
                "n_obs": Numero((sg / ob) ** 2, 0), "c": Numero(c, 2),
                "dentro": "sì" if abs(y - m) <= c else "no", "z": Numero((y - m) / se, 2),
                "lo": Numero(m - c, 2), "hi": Numero(m + c, 2), "var": Numero(sg**2, 0),
                "var_media": Numero(sg**2 / dim, 2)}

    def studente(_tabelle):
        """Rebuild the answers from the numbers given in the text."""
        return answers(*(par[k].valore for k in ("mu", "sigma", "n", "obiettivo", "ybar")))

    truth = answers(mu, sigma, n, obiettivo, ybar)

    def simulazione_coerente(r):
        """Check unbiasedness, variance, coverage and independence on 20000 simulated samples."""
        c, sg2 = r["c"].valore, sigma**2
        cov12 = np.cov(pop[:, 0], pop[:, 1])[0, 1]
        varsomma = np.var(pop[:, 0] + pop[:, 1], ddof=1)
        grandi = rng_sim.lognormal(m_log, s_log, size=(20000, int(r["n_obs"].valore))).mean(axis=1)
        return (abs(medie.mean() - mu) < 0.05
                and abs(medie.var(ddof=1) / (sg2 / n) - 1) < 0.04
                and abs(np.mean(np.abs(medie - mu) <= c) - 0.95) < 0.012
                and abs(cov12) < 0.04 * sg2 and abs(varsomma / r["var_somma"].valore - 1) < 0.05
                and abs(grandi.std(ddof=1) / obiettivo - 1) < 0.04)

    rng_sim = np.random.default_rng(7)

    def figura(path):
        """Draw the skewed population and the distribution of the sample mean around mu."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.8))
        x = np.linspace(1, 90, 400)
        dens = stats.lognorm.pdf(x, s_log, scale=np.exp(m_log))
        a1.plot(x, dens, color=es.BLUE, lw=1.4)
        a1.fill_between(x, dens, color=es.BLUEBG)
        a1.axvline(mu, color=es.RED, lw=1.3)
        a1.set_title("popolazione di $Y$", loc="left", fontsize=9)
        a1.set_xlabel("reddito (migliaia di euro)")
        a1.set_yticks([])
        a2.hist(medie, bins=50, density=True, color=es.BLUEBG, edgecolor=es.BLUE, lw=0.4)
        g = np.linspace(mu - 4.5 * truth["se"].valore, mu + 4.5 * truth["se"].valore, 300)
        a2.plot(g, stats.norm.pdf(g, mu, truth["se"].valore), color=es.BLUE, lw=1.4)
        a2.axvspan(truth["lo"].valore, truth["hi"].valore, color=es.GREENBG, alpha=0.8, zorder=0)
        a2.axvline(ybar, color=es.RED, lw=2.0)
        a2.set_title(f"medie di {n} osservazioni", loc="left", fontsize=9)
        a2.set_xlabel("media campionaria")
        a2.set_yticks([])
        for ax in (a1, a2):
            es.commas(ax, "x")
        fig.subplots_adjust(wspace=0.15)
        es.save(fig, path)

    return Draft(
        dati=pop, parametri=par, tabelle={}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("var_somma"), "b": Quesito("corretta"), "c": Quesito("se"),
                 "d": Quesito("n_obs"), "e": Quesito("c"), "f": Quesito("dentro")},
        attese=[lambda r: r["dentro"] == "no", lambda r: r["se"].valore < sigma / 4, simulazione_coerente],
        margini=[Margin(stat=truth["z"].valore, crit=Z)], figure={"campionaria": figura})


@exercise("e00_08", modulo=0, livello=2,
          tipo=("intervallo-di-confidenza-per-una-proporzione", "test-su-una-proporzione"))
def sondaggio_maggioranza(rng):
    """Build the interval for a proportion and test it against 1/2 with the standard error under H0."""
    n, pi0 = 900, 0.5
    while True:
        x = int(rng.binomial(n, 0.54))
        ph = x / n
        z0 = (ph - pi0) / np.sqrt(pi0 * (1 - pi0) / n)
        zh = (ph - pi0) / np.sqrt(ph * (1 - ph) / n)
        if 2.35 <= z0 <= 3.2 and zh >= 2.3:
            break
    par = {"n": Numero(n, 0), "x": Numero(x, 0), "pi0": Numero(pi0, 2)}

    def answers(dim, succ, p0):
        """Return every answer from the sample size, the number of successes and the value under H0."""
        p = succ / dim
        se = np.sqrt(p * (1 - p) / dim)
        se0 = np.sqrt(p0 * (1 - p0) / dim)
        z = (p - p0) / se0
        return {"se": Numero(se, 4), "lo": Numero(p - Z * se, 3), "hi": Numero(p + Z * se, 3),
                "se0": Numero(se0, 4), "z": Numero(z, 2), "dec": "rifiuta" if z > Z_UNI else "non rifiuta",
                "phat": Numero(p, 3), "z_hat": Numero((p - p0) / se, 2),
                "soglia": Numero(p0 + Z_UNI * se0, 4)}

    def studente(_tabelle):
        """Rebuild the answers from the numbers given in the text."""
        return answers(*(par[k].valore for k in ("n", "x", "pi0")))

    truth = answers(n, x, pi0)
    rng_sim = np.random.default_rng(11)

    def simulazione_coerente(r):
        """Check coverage of the interval, size of the test and the standard error under H0."""
        p_vero = 0.54
        ph_s = rng_sim.binomial(n, p_vero, 100000) / n
        se_s = np.sqrt(ph_s * (1 - ph_s) / n)
        copertura = np.mean(np.abs(ph_s - p_vero) <= Z * se_s)
        ph_0 = rng_sim.binomial(n, pi0, 100000) / n
        z_0 = (ph_0 - pi0) / r["se0"].valore
        return (abs(copertura - 0.95) < 0.01 and abs(np.mean(z_0 > Z_UNI) - 0.05) < 0.01
                and abs(ph_0.std(ddof=1) / r["se0"].valore - 1) < 0.02)

    def figura(path):
        """Draw the interval against pi0 and the null distribution of the sample proportion."""
        es, plt = _stile()
        r = truth
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.7), gridspec_kw={"width_ratios": [1, 1.4]})
        a1.errorbar(r["phat"].valore, 0, xerr=Z * r["se"].valore, fmt="o", color=es.BLUE, capsize=4, lw=2)
        a1.axvline(pi0, color=es.RED, ls="--", lw=1.2)
        a1.set_yticks([])
        a1.set_ylim(-1, 1)
        a1.set_title("IC al 95% e valore sotto $H_0$", loc="left", fontsize=8.5)
        a1.set_xlabel("proporzione")
        g = np.linspace(pi0 - 4 * r["se0"].valore, r["phat"].valore + 2 * r["se0"].valore, 300)
        dens = stats.norm.pdf(g, pi0, r["se0"].valore)
        a2.plot(g, dens, color=es.BLUE, lw=1.4)
        a2.fill_between(g, dens, color=es.BLUEBG)
        zona = g >= r["soglia"].valore
        a2.fill_between(g[zona], dens[zona], color=es.RED, alpha=0.35)
        a2.axvline(r["phat"].valore, color=es.GREEN, lw=2.0)
        a2.set_title("distribuzione di $\\hat\\pi$ sotto $H_0$", loc="left", fontsize=8.5)
        a2.set_xlabel("proporzione campionaria")
        a2.set_yticks([])
        for ax in (a1, a2):
            es.commas(ax, "x")
        fig.subplots_adjust(wspace=0.12)
        es.save(fig, path)

    return Draft(
        dati=None, parametri=par, tabelle={}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("se"), "b": Quesito("lo"), "c": Quesito("hi"), "d": Quesito("se0"),
                 "e": Quesito("z"), "f": Quesito("dec")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["lo"].valore > pi0, simulazione_coerente],
        margini=[Margin(stat=truth["z"].valore, crit=Z_UNI), Margin(stat=truth["z_hat"].valore, crit=Z)],
        figure={"proporzione": figura})


@exercise("e00_09", modulo=0, livello=2,
          tipo=("distribuzione-t-e-piccoli-campioni", "test-unilaterali-e-bilaterali-sulla-media",
                "intervallo-di-confidenza-per-la-media"))
def flaconi_in_laboratorio(rng):
    """Test a mean from four observations with the t quantile and show where the normal one misleads."""
    n, mu0 = 4, 50.0
    qt = round(float(stats.t.ppf(0.975, n - 1)), 3)
    while True:
        v = np.round(rng.normal(52.0, 2.0, n), 1)
        t = (v.mean() - mu0) / (v.std(ddof=1) / np.sqrt(n))
        # Between the two critical values the normal rejects and the t does not.
        if 2.3 <= abs(t) <= 2.62:
            break
    tab = _tabella(["flacone", "contenuto (ml)"], [[f"F{i + 1}", _cella(x, 1)] for i, x in enumerate(v)])
    par = {"mu0": Numero(mu0, 0), "qt": Numero(qt, 3), "n": Numero(n, 0)}

    def answers(valori):
        """Return every answer from the printed contents of the flasks."""
        dim = len(valori)
        media, s = valori.mean(), valori.std(ddof=1)
        se = s / np.sqrt(dim)
        t_obs = (media - mu0) / se
        return {"t": Numero(t_obs, 2), "gdl": Numero(dim - 1, 0),
                "dec_t": "rifiuta" if abs(t_obs) > qt else "non rifiuta",
                "dec_norm": "rifiuta" if abs(t_obs) > Z else "non rifiuta",
                "lo": Numero(media - qt * se, 2), "hi": Numero(media + qt * se, 2),
                "media": Numero(media, 3), "s": Numero(s, 3),
                "se": Numero(se, 3), "t_abs": Numero(abs(t_obs), 2),
                "lo_z": Numero(media - Z * se, 2), "hi_z": Numero(media + Z * se, 2)}

    def studente(_tabelle):
        """Rebuild the answers from the four printed contents."""
        return answers(np.array([r[0] for r in _leggi(tab)]))

    def simulazione_coerente(_risposte):
        """Check on simulated normal samples that the t quantile gives 5% and the normal almost 15%."""
        x = np.random.default_rng(5).normal(0.0, 1.0, (200000, n))
        ts = x.mean(axis=1) / (x.std(axis=1, ddof=1) / np.sqrt(n))
        esatto = 2 * stats.t.sf(Z, n - 1)
        return (abs(np.mean(np.abs(ts) > qt) - 0.05) < 0.004 and abs(np.mean(np.abs(ts) > Z) - esatto) < 0.004
                and 0.14 < esatto < 0.15)

    def figura(path):
        """Draw the normal and t densities with their critical values and the observed t."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.0))
        x = np.linspace(-6, 6, 600)
        ax.plot(x, stats.norm.pdf(x), color=es.BLUE, lw=1.4, label="normale")
        ax.plot(x, stats.t.pdf(x, n - 1), color=es.RED, lw=1.4,
                label=f"$t$ di Student con {n - 1} gradi di libertà")
        ax.axvline(-Z, color=es.BLUE, ls="--", lw=1.0, label="valore critico normale: ±1,96")
        ax.axvline(Z, color=es.BLUE, ls="--", lw=1.0)
        ax.axvline(-qt, color=es.RED, ls="--", lw=1.0, label=f"valore critico $t$: ±{_it(qt, 3)}")
        ax.axvline(qt, color=es.RED, ls="--", lw=1.0)
        ax.axvline(t, color=es.GREEN, lw=2.0, label=f"$t$ osservata = {_it(t)}")
        ax.set_xlabel("valore della statistica")
        ax.set_yticks([])
        ax.set_ylim(0, 0.62)
        es.commas(ax, "x")
        ax.legend(loc="upper left", fontsize=7.5)
        es.save(fig, path)

    truth = answers(v)
    return Draft(
        dati=v, parametri=par, tabelle={"dati": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("t"), "b": Quesito("gdl"), "c": Quesito("dec_t"),
                 "d": Quesito("dec_norm"), "e": Quesito("lo"), "f": Quesito("hi")},
        attese=[lambda r: r["dec_t"] == "non rifiuta", lambda r: r["dec_norm"] == "rifiuta",
                lambda r: r["lo"].valore < mu0 < r["hi"].valore, simulazione_coerente],
        margini=[Margin(stat=t, crit=qt), Margin(stat=t, crit=Z)], figure={"densita": figura})


@exercise("e00_10", modulo=0, livello=2, tipo="confronto-tra-due-medie-campioni-indipendenti")
def tempi_di_risposta(rng):
    """Compare two independent means where the single intervals overlap but the test rejects."""
    while True:
        n1, n2 = (int(k) for k in rng.choice([64, 81, 100], 2))
        s1, s2 = (round(float(k), 1) for k in rng.uniform(7.5, 10.0, 2))
        e1, e2 = s1 / np.sqrt(n1), s2 / np.sqrt(n2)
        # The difference must clear the test by 15% and still sit 15% inside the overlap limit.
        basso, alto = 1.15 * Z * np.hypot(e1, e2), 0.85 * Z * (e1 + e2)
        d = round((basso + alto) / 2, 2)
        if basso <= d <= alto:
            break
    m2 = round(float(rng.uniform(36, 42)), 2)
    m1 = round(m2 + d, 2)
    tab = _tabella(["servizio", "$n$", "media $\\bar y$", "dev. std. $s$"],
                   [["A", _cella(n1, 0), _cella(m1, 2), _cella(s1, 1)],
                    ["B", _cella(n2, 0), _cella(m2, 2), _cella(s2, 1)]])

    def answers(righe):
        """Return every answer from the printed sizes, means and standard deviations."""
        (a, ma, sa), (b, mb, sb) = righe
        ea, eb = sa / np.sqrt(a), sb / np.sqrt(b)
        sed = np.hypot(ea, eb)
        diff = ma - mb
        t_obs = diff / sed
        lo_a, hi_a, lo_b, hi_b = ma - Z * ea, ma + Z * ea, mb - Z * eb, mb + Z * eb
        return {"se_d": Numero(sed, 3), "t": Numero(t_obs, 2),
                "dec": "rifiuta" if abs(t_obs) > Z else "non rifiuta",
                "sovrapposti": "sì" if max(lo_a, lo_b) < min(hi_a, hi_b) else "no",
                "lo": Numero(diff - Z * sed, 2), "hi": Numero(diff + Z * sed, 2),
                "diff": Numero(diff, 2), "n1": Numero(a, 0), "n2": Numero(b, 0),
                "m1": Numero(ma, 2), "m2": Numero(mb, 2), "s1": Numero(sa, 1), "s2": Numero(sb, 1),
                "e1": Numero(ea, 3), "e2": Numero(eb, 3), "lo1": Numero(lo_a, 2),
                "hi1": Numero(hi_a, 2), "lo2": Numero(lo_b, 2), "hi2": Numero(hi_b, 2),
                "lim": Numero(Z * (ea + eb), 2), "z_se": Numero(Z * sed, 2)}

    def studente(_tabelle):
        """Rebuild the answers from the two printed rows."""
        return answers(_leggi(tab))

    def simulazione_coerente(r):
        """Check Var of the difference, the null covariance and the size of the test by simulation."""
        g = np.random.default_rng(3)
        x1, x2 = g.normal(0, s1, (20000, n1)), g.normal(0, s2, (20000, n2))
        mu1, mu2 = x1.mean(axis=1), x2.mean(axis=1)
        sed = np.sqrt(x1.var(axis=1, ddof=1) / n1 + x2.var(axis=1, ddof=1) / n2)
        return (abs(np.var(mu1 - mu2, ddof=1) / r["se_d"].valore ** 2 - 1) < 0.04
                and abs(np.corrcoef(mu1, mu2)[0, 1]) < 0.03
                and abs(np.mean(np.abs(mu1 - mu2) / sed > Z) - 0.05) < 0.01)

    def figura(path):
        """Draw the two single intervals, their overlap, and the interval of the difference."""
        es, plt = _stile()
        r = truth
        fig = plt.figure(figsize=(6.1, 3.7))
        grid = fig.add_gridspec(2, 1, height_ratios=[1.3, 1.0], hspace=0.75)
        ax = fig.add_subplot(grid[0])
        ax.axvspan(max(r["lo1"].valore, r["lo2"].valore), min(r["hi1"].valore, r["hi2"].valore),
                   color=es.AMBER, alpha=0.3, label="parte comune dei due intervalli")
        ax.errorbar(r["m1"].valore, 1, xerr=Z * r["e1"].valore, fmt="o", color=es.BLUE, capsize=4, lw=2)
        ax.errorbar(r["m2"].valore, 0, xerr=Z * r["e2"].valore, fmt="o", color=es.RED, capsize=4, lw=2)
        ax.set_yticks([0, 1], ["servizio B", "servizio A"])
        ax.set_ylim(-0.6, 1.6)
        ax.set_xlabel("tempo medio di risposta, con intervallo al 95% (secondi)")
        es.commas(ax, "x")
        ax.legend(loc="upper left", fontsize=8)
        bx = fig.add_subplot(grid[1])
        bx.errorbar(r["diff"].valore, 0, xerr=Z * r["se_d"].valore, fmt="o", color=es.BLUE, capsize=4, lw=2,
                    label="differenza A − B con intervallo al 95%")
        bx.axvline(0, color=es.RED, ls="--", lw=1.2, label="nessuna differenza ($H_0$)")
        bx.set_yticks([])
        bx.set_ylim(-1, 1)
        bx.set_xlim(-0.6 * r["hi"].valore, 1.15 * r["hi"].valore)
        bx.set_xlabel("differenza fra le medie, A meno B (secondi)")
        es.commas(bx, "x")
        bx.legend(loc="upper left", fontsize=8)
        es.save(fig, path)

    truth = answers([[n1, m1, s1], [n2, m2, s2]])
    return Draft(
        dati=None, parametri={}, tabelle={"gruppi": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("se_d"), "b": Quesito("t"), "c": Quesito("dec"),
                 "d": Quesito("sovrapposti"), "e": Quesito("lo"), "f": Quesito("hi")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["sovrapposti"] == "sì",
                lambda r: r["lo"].valore > 0, simulazione_coerente],
        margini=[Margin(stat=truth["t"].valore, crit=Z),
                 Margin(stat=truth["diff"].valore, crit=truth["lim"].valore)],
        figure={"intervalli": figura})


@exercise("e00_11", modulo=0, livello=2, tipo="confronto-tra-due-proporzioni")
def adesione_alle_offerte(rng):
    """Compare two proportions with the pooled standard error under H0 and the unpooled one for the interval."""
    while True:
        n1, n2 = (int(k) for k in rng.choice([300, 400, 500, 600], 2, replace=False))
        x1, x2 = int(rng.binomial(n1, 0.33)), int(rng.binomial(n2, 0.24))
        p1, p2, pool = x1 / n1, x2 / n2, (x1 + x2) / (n1 + n2)
        z = (p1 - p2) / np.sqrt(pool * (1 - pool) * (1 / n1 + 1 / n2))
        zu = (p1 - p2) / np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
        if 2.4 <= z <= 3.2 and zu >= 2.3:
            break
    tab = _tabella(["offerta", "$n$", "accettazioni $x$"],
                   [["A", _cella(n1, 0), _cella(x1, 0)], ["B", _cella(n2, 0), _cella(x2, 0)]])

    def answers(righe):
        """Return every answer from the printed sizes and counts of the two offers."""
        (a, xa), (b, xb) = righe
        pa, pb, comb = xa / a, xb / b, (xa + xb) / (a + b)
        se0 = np.sqrt(comb * (1 - comb) * (1 / a + 1 / b))
        se_u = np.sqrt(pa * (1 - pa) / a + pb * (1 - pb) / b)
        z_obs = (pa - pb) / se0
        return {"pool": Numero(comb, 4), "se0": Numero(se0, 4), "z": Numero(z_obs, 2),
                "dec": "rifiuta" if abs(z_obs) > Z else "non rifiuta",
                "lo": Numero(pa - pb - Z * se_u, 3), "hi": Numero(pa - pb + Z * se_u, 3),
                "p1": Numero(pa, 4), "p2": Numero(pb, 4), "diff": Numero(pa - pb, 4),
                "se_u": Numero(se_u, 4), "n1": Numero(a, 0), "x1": Numero(xa, 0),
                "n2": Numero(b, 0), "x2": Numero(xb, 0), "zu": Numero((pa - pb) / se_u, 2),
                "se_err": Numero(np.sqrt(comb * (1 - comb) / (a + b)), 4),
                "z_err": Numero((pa - pb) / np.sqrt(comb * (1 - comb) / (a + b)), 2),
                "n_tot": Numero(a + b, 0)}

    def studente(_tabelle):
        """Rebuild the answers from the two printed rows."""
        return answers(_leggi(tab))

    truth = answers([[n1, x1], [n2, x2]])

    def simulazione_coerente(r):
        """Check size of the pooled test, its null standard error and the coverage of the interval."""
        g = np.random.default_rng(13)
        pool_, vero = r["pool"].valore, 0.33 - 0.24
        a1, a2 = g.binomial(n1, pool_, 100000) / n1, g.binomial(n2, pool_, 100000) / n2
        comb = (a1 * n1 + a2 * n2) / (n1 + n2)
        z_s = (a1 - a2) / np.sqrt(comb * (1 - comb) * (1 / n1 + 1 / n2))
        b1, b2 = g.binomial(n1, 0.33, 100000) / n1, g.binomial(n2, 0.24, 100000) / n2
        se_s = np.sqrt(b1 * (1 - b1) / n1 + b2 * (1 - b2) / n2)
        return (abs(np.mean(np.abs(z_s) > Z) - 0.05) < 0.01
                and abs((a1 - a2).std(ddof=1) / r["se0"].valore - 1) < 0.02
                and abs(np.mean(np.abs(b1 - b2 - vero) <= Z * se_s) - 0.95) < 0.01)

    def figura(path):
        """Draw the two proportions with the pooled one, and the null distribution of z."""
        es, plt = _stile()
        r = truth
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1, 1.6]})
        a1.bar([0, 1], [r["p1"].valore, r["p2"].valore], color=[es.BLUE, es.AMBER], width=0.55)
        a1.axhline(r["pool"].valore, color=es.RED, ls="--", lw=1.2, label="proporzione combinata")
        a1.set_xticks([0, 1], ["offerta A", "offerta B"])
        a1.set_ylabel("quota di accettazioni")
        a1.set_ylim(0, r["p1"].valore * 1.6)
        es.commas(a1, "y")
        a1.legend(loc="upper right", fontsize=7)
        es.dist_test("z", stat=r["z"].valore, crit=Z, tail="two", ax=a2, statlabel=f"$z$ = {_it(r['z'].valore)}",
                     critlabel="regione di rifiuto: $|z|$ > 1,96")
        a2.legend(loc="upper left", fontsize=7)
        fig.subplots_adjust(wspace=0.25)
        es.save(fig, path)

    return Draft(
        dati=None, parametri={}, tabelle={"offerte": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("pool"), "b": Quesito("se0"), "c": Quesito("z"), "d": Quesito("dec"),
                 "e": Quesito("lo"), "f": Quesito("hi")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["lo"].valore > 0, simulazione_coerente],
        margini=[Margin(stat=truth["z"].valore, crit=Z), Margin(stat=truth["zu"].valore, crit=Z)],
        figure={"proporzioni": figura})


@exercise("e00_12", modulo=0, livello=3, punti=4,
          tipo=("confronto-per-dati-appaiati", "media-e-varianza-di-una-somma",
                "covarianza-e-sue-proprieta", "correlazione-e-indipendenza"))
def corso_di_formazione(rng):
    """Test the mean of paired differences from summary statistics, with and without the covariance."""
    n = 36
    sd_pop, corr = (6.0, 6.4), 0.9
    cov_pop = [[sd_pop[0] ** 2, corr * sd_pop[0] * sd_pop[1]],
               [corr * sd_pop[0] * sd_pop[1], sd_pop[1] ** 2]]
    while True:
        xy = rng.multivariate_normal([48.0, 49.2], cov_pop, n)
        prima, dopo = xy[:, 0], xy[:, 1]
        mb, ma = round(float(prima.mean()), 1), round(float(dopo.mean()), 1)
        sb, sa = round(float(prima.std(ddof=1)), 2), round(float(dopo.std(ddof=1)), 2)
        cv = round(float(np.cov(prima, dopo)[0, 1]), 2)
        var_d = sb**2 + sa**2 - 2 * cv
        if var_d <= 0:
            continue
        t = (ma - mb) / np.sqrt(var_d / n)
        t_ind = (ma - mb) / np.sqrt((sb**2 + sa**2) / n)
        # Paired test rejects clearly, the independent one clearly does not.
        if 2.3 <= t <= 3.4 and 0.3 <= t_ind <= 1.3:
            break
    tab = _tabella(["", "media", "dev. std."],
                   [["prima", _cella(mb, 1), _cella(sb, 2)], ["dopo", _cella(ma, 1), _cella(sa, 2)]])
    par = {"n": Numero(n, 0), "cov": Numero(cv, 2)}

    def answers(medie, sds, c):
        """Return every answer from the printed means, standard deviations and the covariance."""
        (m_pre, m_post), (s_pre, s_post) = medie, sds
        d = m_post - m_pre
        var = s_pre**2 + s_post**2 - 2 * c
        se, se_ind = np.sqrt(var / n), np.sqrt((s_pre**2 + s_post**2) / n)
        return {"d": Numero(d, 2), "r": Numero(c / (s_pre * s_post), 3),
                "sd_d": Numero(np.sqrt(var), 3), "t": Numero(d / se, 2),
                "dec": "rifiuta" if d / se > Z_UNI else "non rifiuta",
                "t_ind": Numero(d / se_ind, 2),
                "dec_ind": "rifiuta" if d / se_ind > Z_UNI else "non rifiuta",
                "var_d": Numero(var, 3), "se": Numero(se, 3), "se_ind": Numero(se_ind, 3),
                "var_pre": Numero(s_pre**2, 4), "var_post": Numero(s_post**2, 4),
                "somma_var": Numero(s_pre**2 + s_post**2, 3), "m_pre": Numero(m_pre, 1),
                "m_post": Numero(m_post, 1), "s_pre": Numero(s_pre, 2), "s_post": Numero(s_post, 2),
                "due_cov": Numero(2 * c, 2), "rapporto": Numero(se_ind / se, 1)}

    def studente(_tabelle):
        """Rebuild the answers from the printed table and the printed covariance."""
        (m_pre, s_pre), (m_post, s_post) = _leggi(tab)
        return answers((m_pre, m_post), (s_pre, s_post), par["cov"].valore)

    def identita_e_varianza(_risposte):
        """Check the variance identity on the sample and Var of the mean difference by simulation."""
        esatta = abs(np.var(dopo - prima, ddof=1)
                     - (np.var(dopo, ddof=1) + np.var(prima, ddof=1) - 2 * np.cov(prima, dopo)[0, 1])) < 1e-9
        g = np.random.default_rng(17).multivariate_normal([0.0, 0.0], cov_pop, size=(20000, n))
        var_sim = np.var((g[:, :, 1] - g[:, :, 0]).mean(axis=1), ddof=1)
        var_formula = (sd_pop[0] ** 2 + sd_pop[1] ** 2 - 2 * corr * sd_pop[0] * sd_pop[1]) / n
        var_ind = (sd_pop[0] ** 2 + sd_pop[1] ** 2) / n
        return bool(esatta and abs(var_sim / var_formula - 1) < 0.04 and var_ind > 5 * var_formula)

    def figura(path):
        """Draw the paired scatter and the intervals for the mean difference with and without Cov."""
        es, plt = _stile()
        r = truth
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), gridspec_kw={"width_ratios": [1, 1.35]})
        a1.plot(prima, dopo, "o", color=es.BLUE, ms=3.5, alpha=0.7)
        lim = [min(prima.min(), dopo.min()) - 1, max(prima.max(), dopo.max()) + 1]
        a1.plot(lim, lim, color=es.RED, lw=1.2, label="dopo = prima")
        a1.set_xlabel("prima")
        a1.set_ylabel("dopo")
        a1.legend(loc="upper left", fontsize=7.5)
        es.commas(a1)
        d = r["d"].valore
        for y0, errore, colore in ((1, r["se"].valore, es.BLUE), (0, r["se_ind"].valore, es.RED)):
            a2.errorbar(d, y0, xerr=Z_UNI * errore, fmt="o", color=colore, capsize=4, lw=2)
        a2.axvline(0, color=es.GRAY, ls="--", lw=1.0)
        a2.set_yticks([0, 1], ["covarianza\nignorata", "con la\ncovarianza"])
        a2.set_ylim(-0.6, 1.6)
        a2.set_xlabel("differenza media dopo − prima")
        es.commas(a2, "x")
        fig.subplots_adjust(wspace=0.4)
        es.save(fig, path)

    truth = answers((mb, ma), (sb, sa), cv)
    return Draft(
        dati=(prima, dopo), parametri=par, tabelle={"stat": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("d"), "b": Quesito("r"), "c": Quesito("sd_d"), "d": Quesito("t"),
                 "e": Quesito("dec"), "f": Quesito("t_ind"), "g": Quesito("dec_ind")},
        attese=[lambda r: r["dec"] == "rifiuta", lambda r: r["dec_ind"] == "non rifiuta",
                lambda r: r["r"].valore > 0.7, identita_e_varianza],
        margini=[Margin(stat=truth["t"].valore, crit=Z_UNI), Margin(stat=truth["t_ind"].valore, crit=Z_UNI)],
        figure={"appaiati": figura})


@exercise("e00_13", modulo=0, livello=3, punti=4,
          tipo=("valore-atteso-condizionato-e-esogeneita", "probabilita-condizionata-e-indipendenza",
                "correlazione-e-indipendenza", "variabile-casuale-valore-atteso-varianza",
                "covarianza-e-sue-proprieta"))
def errore_e_media_condizionale(rng):
    """Show that a null covariance does not give a null conditional mean, and what a nonzero one costs."""
    xs = np.arange(1.0, 6.0)
    p = np.array([0.10, 0.20, 0.40, 0.20, 0.10])
    c = float(rng.choice([0.4, 0.5, 0.6]))
    d = float(rng.choice([0.3, 0.4, 0.5]))
    # Distinct constants keep the two answers about slopes from coinciding by accident.
    while abs(c - d) < 0.05:
        d = float(rng.choice([0.3, 0.4, 0.5]))
    alpha, beta, xa, xb = 10.0, 3.0, 3.0, 4.0
    # (x-3)^2 has mean 1.2 under p, so the centred square has mean zero and is uncorrelated with X.
    ep = c * ((xs - 3) ** 2 - 1.2)
    eq = d * (xs - 3)
    tab = _tabella(["$x$", "$P(X=x)$", "$E[\\epsilon\\mid X=x]$ modello P", "$E[\\epsilon\\mid X=x]$ modello Q"],
                   [[_cella(x, 0), _cella(q, 2), _cella(a, 2), _cella(b, 2)]
                    for x, q, a, b in zip(xs, p, ep, eq)])
    par = {"alpha": Numero(alpha, 0), "beta": Numero(beta, 0), "xa": Numero(xa, 0), "xb": Numero(xb, 0)}

    def answers(colonne, b_vero, a_vero, x_a, x_b):
        """Return every answer from the printed table and the true coefficients."""
        x, q, e_p, e_q = colonne
        ex = float(x @ q)
        varx = float(((x - ex) ** 2) @ q)
        e_eps_p, e_eps_q = float(q @ e_p), float(q @ e_q)
        exe_p, exe_q = float((x * q) @ e_p), float((x * q) @ e_q)
        cov_p, cov_q = exe_p - ex * e_eps_p, exe_q - ex * e_eps_q
        ia, ib = int(np.argmin(np.abs(x - x_a))), int(np.argmin(np.abs(x - x_b)))
        return {"e_eps_p": Numero(e_eps_p, 2), "cov_p": Numero(cov_p, 2),
                "dec_p": "sì" if np.allclose(e_p, 0, atol=1e-9) else "no",
                "delta": Numero(b_vero + e_p[ib] - e_p[ia], 2), "cov_q": Numero(cov_q, 3),
                "bias_q": Numero(cov_q / varx, 3), "ex": Numero(ex, 1), "varx": Numero(varx, 2),
                "exe_p": Numero(exe_p, 2), "exe_q": Numero(exe_q, 3), "e_eps_q": Numero(e_eps_q, 2),
                "ey_a": Numero(a_vero + b_vero * x_a + e_p[ia], 2),
                "ey_b": Numero(a_vero + b_vero * x_b + e_p[ib], 2),
                "slope_p": Numero(b_vero + cov_p / varx, 2), "slope_q": Numero(b_vero + cov_q / varx, 3),
                **{f"x{i + 1}": Numero(v, 0) for i, v in enumerate(x)},
                **{f"p{i + 1}": Numero(v, 2) for i, v in enumerate(q)},
                **{f"ep{i + 1}": Numero(v, 2) for i, v in enumerate(e_p)}}

    def studente(_tabelle):
        """Rebuild the answers from the printed table."""
        colonne = np.array(_leggi(tab)).T
        return answers(colonne, par["beta"].valore, par["alpha"].valore, par["xa"].valore, par["xb"].valore)

    def simulazione_coerente(_risposte):
        """Check the table and the slopes on a large simulated population."""
        g = np.random.default_rng(23)
        m = 1_000_000
        x = g.choice(xs, size=m, p=p)
        idx = (x - 1).astype(int)

        def pendenza(media_condizionale):
            """Return the sample slope of Y on X when the error has the given conditional mean."""
            y = alpha + beta * x + media_condizionale[idx] + g.normal(0.0, 1.0, m)
            return np.cov(x, y)[0, 1] / np.var(x, ddof=1)

        eps_p = ep[idx] + g.normal(0.0, 1.0, m)
        medie = np.array([eps_p[x == v].mean() for v in xs])
        return bool(abs(pendenza(ep) - beta) < 0.01 and abs(pendenza(eq) - beta - d) < 0.01
                    and np.abs(medie - ep).max() < 0.03 and abs(eps_p.mean()) < 0.01)

    def figura(path):
        """Draw E[Y|X=x] in the two models against the line alpha + beta*x."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9), sharey=True)
        retta = alpha + beta * xs
        for ax, media, colore, nome, pend in (
                (a1, ep, es.BLUE, "modello P", beta + truth["cov_p"].valore / truth["varx"].valore),
                (a2, eq, es.AMBER, "modello Q", beta + truth["bias_q"].valore)):
            ax.plot(xs, retta, color=es.GRAY, ls="--", lw=1.4, label=r"$\alpha+\beta x$", zorder=3)
            ax.plot(xs, retta + media, "o-", color=colore, lw=1.6, ms=5, label=r"$E[Y\mid X=x]$", zorder=4)
            ax.plot(xs, alpha + 3 * beta + pend * (xs - 3), color=es.RED, lw=1.0,
                    label="retta di regressione")
            ax.set_title(nome, loc="left", fontsize=9)
            ax.set_xlabel("$x$")
            es.commas(ax)
            ax.legend(loc="upper left", fontsize=7.5)
        a1.set_ylabel("$Y$")
        fig.subplots_adjust(wspace=0.08)
        es.save(fig, path)

    truth = answers(np.array([xs, p, ep, eq]), beta, alpha, xa, xb)
    return Draft(
        dati=(xs, p, ep, eq), parametri=par, tabelle={"distr": tab}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("e_eps_p"), "b": Quesito("cov_p"), "c": Quesito("dec_p"),
                 "d": Quesito("delta"), "e": Quesito("cov_q"), "f": Quesito("bias_q")},
        attese=[lambda r: r["dec_p"] == "no", lambda r: abs(r["cov_p"].valore) < 1e-9,
                lambda r: abs(r["e_eps_p"].valore) < 1e-9, lambda r: r["cov_q"].valore > 0.2,
                simulazione_coerente],
        figure={"medie": figura})


@exercise("e00_14", modulo=0, livello=3, punti=4,
          tipo=("campionamento-casuale-semplice", "media-campionaria-correttezza-e-errore-standard",
                "media-e-varianza-di-una-somma", "test-unilaterali-e-bilaterali-sulla-media",
                "intervallo-di-confidenza-per-la-media"))
def alunni_della_stessa_classe(rng):
    """Show that correlated observations leave the mean unbiased but inflate its standard error."""
    n, sigma, rho, mu0 = 36, 10.0, 0.10, 60.0
    while True:
        ybar = round(mu0 + float(rng.uniform(2.5, 3.2)) * sigma / np.sqrt(n), 1)
        t_ing = (ybar - mu0) / (sigma / np.sqrt(n))
        t_vero = t_ing / np.sqrt(1 + (n - 1) * rho)
        # Naive test rejects clearly, the correct one clearly does not.
        if t_ing >= 2.4 and t_vero <= 1.5:
            break
    par = {"n": Numero(n, 0), "sigma": Numero(sigma, 0), "rho": Numero(rho, 2),
           "mu0": Numero(mu0, 0), "ybar": Numero(ybar, 1)}

    def answers(dim, sg, r, m0, y):
        """Return every answer from the numbers given in the text."""
        se_ing = sg / np.sqrt(dim)
        fattore_var = 1 + (dim - 1) * r
        var_somma = dim * sg**2 * fattore_var
        se_vero = np.sqrt(var_somma) / dim
        ti, tv = (y - m0) / se_ing, (y - m0) / se_vero
        return {"se_ing": Numero(se_ing, 3), "corretto": "sì", "var_somma": Numero(var_somma, 0),
                "se_vero": Numero(se_vero, 3), "dec_ing": "rifiuta" if abs(ti) > Z else "non rifiuta",
                "dec_vero": "rifiuta" if abs(tv) > Z else "non rifiuta", "t_ing": Numero(ti, 2),
                "t_vero": Numero(tv, 2), "fattore": Numero(se_vero / se_ing, 2),
                "fatt_var": Numero(fattore_var, 2), "neff": Numero(dim / fattore_var, 1),
                "lo": Numero(y - Z * se_vero, 2), "hi": Numero(y + Z * se_vero, 2),
                "lo_ing": Numero(y - Z * se_ing, 2), "hi_ing": Numero(y + Z * se_ing, 2),
                "var_ind": Numero(dim * sg**2, 0), "var_coppie": Numero(r * sg**2, 0),
                "n_coppie": Numero(dim * (dim - 1), 0)}

    def studente(_tabelle):
        """Rebuild the answers from the numbers given in the text."""
        return answers(*(par[k].valore for k in ("n", "sigma", "rho", "mu0", "ybar")))

    truth = answers(n, sigma, rho, mu0, ybar)

    def simulazione_coerente(r):
        """Check mean, variance and rejection rates on equicorrelated samples."""
        g = np.random.default_rng(29)
        m = 100000
        comune = g.normal(0.0, 1.0, (m, 1))
        y = mu0 + sigma * (np.sqrt(rho) * comune + np.sqrt(1 - rho) * g.normal(0.0, 1.0, (m, n)))
        medie = y.mean(axis=1)
        sc = np.abs(medie - mu0)
        return bool(abs(np.cov(y[:, 0], y[:, 1])[0, 1] / sigma**2 - rho) < 0.01
                    and abs(medie.mean() - mu0) < 0.05
                    and abs(medie.var(ddof=1) / r["se_vero"].valore ** 2 - 1) < 0.02
                    and np.mean(sc / r["se_ing"].valore > Z) > 0.30
                    and abs(np.mean(sc / r["se_vero"].valore > Z) - 0.05) < 0.01)

    def figura(path):
        """Draw the distribution of the mean with the naive and the correct standard error."""
        es, plt = _stile()
        r = truth
        fig, ax = plt.subplots(figsize=(6.1, 3.3))
        g = np.linspace(mu0 - 11, mu0 + 11, 500)
        for errore, colore, nome in ((r["se_ing"].valore, es.BLUE, "errore standard ingenuo"),
                                     (r["se_vero"].valore, es.RED, "errore standard con la correlazione")):
            ax.plot(g, stats.norm.pdf(g, mu0, errore), color=colore, lw=1.5, label=f"{nome} ({_it(errore, 2)})")
            for lato in (-1, 1):
                ax.axvline(mu0 + lato * Z * errore, color=colore, ls="--", lw=1.0)
        ax.axvline(ybar, color=es.GREEN, lw=2.0, label=f"media osservata = {_it(ybar, 1)}")
        ax.set_xlabel("media campionaria $\\bar Y$ sotto $H_0$")
        ax.set_yticks([])
        es.commas(ax, "x")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.25), ncol=1, fontsize=7.5)
        es.save(fig, path)

    return Draft(
        dati=None, parametri=par, tabelle={}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("se_ing"), "b": Quesito("corretto"), "c": Quesito("var_somma"),
                 "d": Quesito("se_vero"), "e": Quesito("dec_ing"), "f": Quesito("dec_vero")},
        attese=[lambda r: r["dec_ing"] == "rifiuta", lambda r: r["dec_vero"] == "non rifiuta",
                lambda r: r["lo"].valore < mu0 < r["hi"].valore, simulazione_coerente],
        margini=[Margin(stat=truth["t_ing"].valore, crit=Z), Margin(stat=truth["t_vero"].valore, crit=Z)],
        figure={"densita": figura})
