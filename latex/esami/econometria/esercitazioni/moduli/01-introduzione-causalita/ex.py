"""Module 01 - introduction and causality: causal criteria, data types, sources of estimation problems."""

import numpy as np
import statsmodels.api as sm

from esercitazioni.lib import figs
from esercitazioni.lib.bank import Draft, Margin, Numero, Quesito, exercise
from esercitazioni.lib.gretl import ols_table

TITOLO = "Introduzione e causalità"

# Normal quantile the exam texts fix for a two-sided test at 5%.
Z = 1.96

# Judging an association from row percentages alone needs a convention; the exercise
# keeps its gap well clear of it so the answer never depends on the exact cut.
SOGLIA_ASSOCIAZIONE = 5.0

_NOMI_TIPO = {"cross": "cross section", "serie": "serie storica", "panel": "panel",
              "ripetute": "cross section ripetuta"}


def _fit(y, columns, stats=("n", "r2", "ssr")):
    """Fit OLS of ``y`` on a constant and the named columns; return the result and its table."""
    names = list(columns)
    X = sm.add_constant(np.column_stack([columns[k] for k in names]))
    res = sm.OLS(y, X).fit()
    return res, ols_table(res, labels=["const", *names], stats=stats)


def _decide(t):
    """Return the two-sided decision at 5% for a t ratio, in the words of the exam."""
    return "rifiuta" if abs(t) > Z else "non rifiuta"


def _stile():
    """Install the house plotting style and return ``(econstyle, pyplot)``."""
    es = figs.use_style()
    import matplotlib.pyplot as plt

    return es, plt


def _righe(tab):
    """Return the numeric cells of each labelled row of a printed table, by row label."""
    out = {}
    for line in tab.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.startswith("|") or not cells[0]:
            continue
        try:
            out[cells[0]] = [float(c.replace(",", ".")) for c in cells[1:]]
        except ValueError:
            continue
    return out


def _intervalli(ax, es, voci, xlabel, riferimento=None, ancora=-0.45):
    """Draw one 95% interval per entry of ``voci`` = (height, coefficient, se, label, colour)."""
    for altezza, coef, err, etichetta, colore in voci:
        ax.errorbar(coef, altezza, xerr=Z * err, fmt="o", color=colore, capsize=4, label=etichetta)
    if riferimento is not None:
        ax.axvline(riferimento[0], color=es.GRAY, ls="--", lw=1.0, label=riferimento[1])
    ax.set_yticks([])
    ax.set_ylim(-0.6, max(v[0] for v in voci) + 0.6)
    ax.set_xlabel(xlabel)
    es.commas(ax, "x")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, ancora), ncol=1)


def _retta(ax, x, res, colore, etichetta=None, ls="-"):
    """Draw the fitted line of a simple regression ``res`` over the range of ``x``."""
    g = np.linspace(x.min(), x.max(), 50)
    ax.plot(g, res.params[0] + res.params[1] * g, color=colore, lw=1.6, ls=ls, label=etichetta)


@exercise("e01_01", modulo=1, livello=1, tipo="causalita-criteri-e-confutazione")
def palestra_assenze(rng):
    """Read the row percentages of a contingency table and apply the three causal criteria."""
    n_si, n_no = int(rng.integers(300, 501)), int(rng.integers(500, 701))
    ass_si, ass_no = int(rng.binomial(n_si, 0.20)), int(rng.binomial(n_no, 0.34))
    n = n_si + n_no
    tab = "\n".join([
        "| | assenza: sì | assenza: no | totale |",
        "|---|---|---|---|",
        f"| iscritti | {ass_si} | {n_si - ass_si} | {n_si} |",
        f"| non iscritti | {ass_no} | {n_no - ass_no} | {n_no} |",
        f"| totale | {ass_si + ass_no} | {n - ass_si - ass_no} | {n} |"])

    def answers(righe):
        """Return every answer from the printed counts of enrolled and non-enrolled employees."""
        s, o = righe["iscritti"], righe["non iscritti"]
        p_si, p_no = 100 * s[0] / s[2], 100 * o[0] / o[2]
        return {"k_si": Numero(s[0], 0), "n_si": Numero(s[2], 0), "k_no": Numero(o[0], 0),
                "n_no": Numero(o[2], 0), "p_si": Numero(p_si, 1), "p_no": Numero(p_no, 1),
                "diff": Numero(p_si - p_no, 1),
                "assoc": "sì" if abs(p_si - p_no) > SOGLIA_ASSOCIAZIONE else "no",
                "ordine": "no", "causa": "no"}

    def studente(tabelle):
        """Rebuild the answers from the printed contingency table, not from the counts drawn."""
        return answers(_righe(tab))

    def figura(path):
        """Draw the two row percentages side by side with their gap."""
        es, plt = _stile()
        p_si, p_no = 100 * ass_si / n_si, 100 * ass_no / n_no
        fig, ax = plt.subplots(figsize=(6.1, 2.4))
        ax.barh([1, 0], [p_si, p_no], color=[es.BLUE, es.RED], height=0.55)
        for y, v in ((1, p_si), (0, p_no)):
            ax.annotate(f"{v:.1f}%".replace(".", ","), xy=(v, y), xytext=(5, 0),
                        textcoords="offset points", va="center", fontsize=9, fontweight="bold")
        ax.annotate("", xy=(p_si, 0.5), xytext=(p_no, 0.5),
                    arrowprops={"arrowstyle": "<->", "color": es.GRAY, "lw": 1.0})
        ax.text((p_si + p_no) / 2, 0.58, f"differenza {p_si - p_no:.1f} punti".replace(".", ","),
                ha="center", va="bottom", fontsize=8.5, color=es.GRAY)
        ax.set_yticks([1, 0], ["iscritti", "non iscritti"])
        ax.set_xlim(0, 1.3 * max(p_si, p_no))
        ax.set_xlabel("percentuale di dipendenti con almeno un'assenza")
        es.commas(ax, "x")
        es.save(fig, path)

    return Draft(
        dati=None, parametri={"n": Numero(n, 0)}, tabelle={"cont": tab},
        risposte=answers(_righe(tab)), studente=studente,
        quesiti={"a": Quesito("p_si"), "b": Quesito("p_no"), "c": Quesito("diff"),
                 "d": Quesito("assoc"), "e": Quesito("ordine"), "f": Quesito("causa")},
        attese=[lambda r: r["diff"].valore < -10, lambda r: r["assoc"] == "sì"],
        margini=[Margin(stat=ass_si / n_si * 100 - ass_no / n_no * 100, crit=SOGLIA_ASSOCIAZIONE)],
        figure={"percentuali": figura})


def _tabella_dati(variabile, righe):
    """Print a long-format dataset: one row per (subject, period) with one measured variable."""
    corpo = [f"| {s} | {p} | {v} |" for s, p, v in righe]
    return "\n".join([f"| soggetto | periodo | {variabile} |", "|---|---|---|", *corpo])


def _coppie(tab):
    """Read back the (subject, period) pairs of a table printed by :func:`_tabella_dati`."""
    out = []
    for line in tab.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) == 3 and cells[1] not in ("periodo", "---"):
            out.append((cells[0], cells[1]))
    return out


def _tipo_dati(coppie):
    """Classify (subject, period) pairs as cross section, time series, panel or repeated cross sections.

    A panel needs the same subjects in more than one period; subjects that appear
    once in each of several periods are repeated cross sections, not a panel.
    """
    soggetti = {s for s, _ in coppie}
    if len({p for _, p in coppie}) == 1:
        return "cross"
    if len(soggetti) == 1:
        return "serie"
    ripetuti = all(sum(1 for s2, _ in coppie if s2 == s) > 1 for s in soggetti)
    return "panel" if ripetuti else "ripetute"


@exercise("e01_02", modulo=1, livello=1, tipo="tipi-di-dato-e-cause-di-problemi")
def tipi_di_dato(rng):
    """Recognise cross section, time series and panel from the structure of printed datasets."""
    n_imp, n_anni = int(rng.integers(120, 401)), int(rng.integers(5, 13))

    def fmt(v):
        """Format a value with one decimal and a decimal comma, as in the printed tables."""
        return f"{v:.1f}".replace(".", ",")

    fatt = rng.uniform(2.5, 40.0, 5)
    prezzo = 60.0 + np.cumsum(rng.normal(0.0, 1.5, 6))
    inv = rng.uniform(1.0, 9.0, (3, 3))
    case = rng.uniform(55.0, 140.0, 6)
    mesi = ["gen", "feb", "mar", "apr", "mag", "giu"]
    tab_a = _tabella_dati("fatturato", [(f"impresa {i + 1}", "2023", fmt(v)) for i, v in enumerate(fatt)])
    tab_b = _tabella_dati("prezzo", [("titolo", f"{m} 2024", fmt(v)) for m, v in zip(mesi, prezzo)])
    tab_c = _tabella_dati("investimenti", [(f"impresa {i + 1}", str(2019 + j), fmt(inv[i, j]))
                                           for i in range(3) for j in range(3)])
    tab_d = _tabella_dati("prezzo", [(f"casa {i + 1}", "1978" if i < 3 else "1981", fmt(v))
                                     for i, v in enumerate(case)])
    tabelle = {"a": tab_a, "b": tab_b, "c": tab_c, "d": tab_d}

    def answers(coppie):
        """Return every answer from the (subject, period) pairs of the four printed datasets."""
        tipi = {k: _tipo_dati(v) for k, v in coppie.items()}
        una_impresa = [c for c in coppie["c"] if c[0] == coppie["c"][0][0]]
        return {"a": "sì" if tipi["a"] == "serie" else "no", "b": "sì" if tipi["b"] == "serie" else "no",
                "c": "sì" if tipi["c"] == "panel" else "no", "d": "sì" if tipi["d"] == "panel" else "no",
                "oss": Numero(float(n_imp * n_anni), 0),
                "f": "sì" if _tipo_dati(una_impresa) == "panel" else "no",
                "tipo_a": _NOMI_TIPO[tipi["a"]], "tipo_b": _NOMI_TIPO[tipi["b"]],
                "tipo_c": _NOMI_TIPO[tipi["c"]], "tipo_d": _NOMI_TIPO[tipi["d"]],
                "tipo_f": _NOMI_TIPO[_tipo_dati(una_impresa)]}

    def studente(_lette):
        """Rebuild the answers from the printed datasets, reading subjects and periods."""
        return answers({k: _coppie(tabelle[k]) for k in tabelle})

    def figura(path):
        """Draw each dataset as a grid of subjects by periods: which cells are observed."""
        es, plt = _stile()
        fig, assi = plt.subplots(1, 4, figsize=(6.1, 2.5), sharey=True)
        titoli = {"a": "A", "b": "B", "c": "C", "d": "D"}
        for ax, (k, tab) in zip(assi, tabelle.items()):
            cp = _coppie(tab)
            soggetti = list(dict.fromkeys(s for s, _ in cp))
            periodi = list(dict.fromkeys(p for _, p in cp))
            ax.scatter([periodi.index(p) for _, p in cp], [soggetti.index(s) for s, _ in cp],
                       marker="s", s=55, color=es.BLUE)
            ax.set_xlim(-0.7, max(len(periodi) - 1, 1) + 0.7)
            ax.set_xticks([])
            ax.set_title(f"{titoli[k]}: {_NOMI_TIPO[_tipo_dati(cp)]}", fontsize=8.5)
            ax.set_xlabel("periodi")
        assi[0].set_ylim(5.6, -0.7)
        assi[0].set_yticks([])
        assi[0].set_ylabel("soggetti")
        fig.subplots_adjust(wspace=0.15)
        es.save(fig, path)

    def tipi_attesi(r):
        """Check that the four datasets are the four different structures they were built to be."""
        return [r["tipo_a"], r["tipo_b"], r["tipo_c"], r["tipo_d"]] == [
            "cross section", "serie storica", "panel", "cross section ripetuta"]

    coppie = {k: _coppie(v) for k, v in tabelle.items()}
    return Draft(
        dati=None, parametri={"N": Numero(n_imp, 0), "T": Numero(n_anni, 0)}, tabelle=tabelle,
        risposte=answers(coppie), studente=studente,
        quesiti={"a": Quesito("a"), "b": Quesito("b"), "c": Quesito("c"), "d": Quesito("d"),
                 "e": Quesito("oss"), "f": Quesito("f")},
        attese=[tipi_attesi, lambda r: r["f"] == "no"], figure={"griglie": figura})


@exercise("e01_03", modulo=1, livello=2,
          tipo=("causalita-criteri-e-confutazione", "tipi-di-dato-e-cause-di-problemi"))
def polizia_reati(rng):
    """Show that the association is symmetric, so it cannot give the direction of the link."""
    n, dpol = 120, 0.5
    reati = rng.normal(40.0, 10.0, n)
    poli = 2.0 + 0.04 * (reati - 40.0) + rng.normal(0.0, 0.3, n)
    ra, taba = _fit(reati, {"poliziotti": poli})
    rb, tabb = _fit(poli, {"reati": reati})

    def answers(a, b, r2a, r2b):
        """Return every answer from the printed rows of the two regressions and their R-squared."""
        simmetrici = abs(a["t"] - b["t"]) < 1e-9 and abs(r2a - r2b) < 1e-9
        return {"decA": _decide(a["t"]), "effA": Numero(dpol * a["coef"], 1), "decB": _decide(b["t"]),
                "simm": "sì" if simmetrici else "no", "dir": "no",
                "bA": Numero(a["coef"], 3), "bB": Numero(b["coef"], 4), "tA": Numero(a["t"], 2),
                "tB": Numero(b["t"], 2), "r2": Numero(r2a, 4),
                "prod": Numero(a["coef"] * b["coef"], 4), "inv": Numero(1 / a["coef"], 4)}

    def studente(tabelle):
        """Rebuild the answers from the two printed regressions."""
        return answers(tabelle["A"].rows["poliziotti"], tabelle["B"].rows["reati"],
                       tabelle["A"].stats["r2"], tabelle["B"].stats["r2"])

    def identita(_risposte):
        """Check the exact symmetry: same t and R-squared, slopes whose product is the R-squared."""
        r = np.corrcoef(poli, reati)[0, 1]
        return (abs(ra.tvalues[1] - rb.tvalues[1]) < 1e-9 and abs(ra.rsquared - rb.rsquared) < 1e-12
                and abs(ra.params[1] * rb.params[1] - ra.rsquared) < 1e-12
                and abs(ra.tvalues[1] - r * np.sqrt((n - 2) / (1 - r**2))) < 1e-9)

    def figura(path):
        """Draw the same cloud of cities twice, with the roles of the axes swapped."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 2.9))
        a1.plot(poli, reati, "o", color=es.GRAY, ms=3, alpha=0.55)
        _retta(a1, poli, ra, es.BLUE)
        a1.set_xlabel("poliziotti")
        a1.set_ylabel("reati")
        a1.set_title("reati su poliziotti", fontsize=9)
        a2.plot(reati, poli, "o", color=es.GRAY, ms=3, alpha=0.55)
        _retta(a2, reati, rb, es.RED)
        a2.set_xlabel("reati")
        a2.set_ylabel("poliziotti")
        a2.set_title("poliziotti su reati", fontsize=9)
        for ax, res in ((a1, ra), (a2, rb)):
            es.commas(ax)
            ax.text(0.04, 0.95, f"$t$ = {res.tvalues[1]:.2f}\n$R^2$ = {res.rsquared:.3f}".replace(".", ","),
                    transform=ax.transAxes, va="top", fontsize=8.5)
        fig.subplots_adjust(wspace=0.32)
        es.save(fig, path)

    truth = answers(dict(zip(("coef", "se", "t"), (ra.params[1], ra.bse[1], ra.tvalues[1]))),
                    dict(zip(("coef", "se", "t"), (rb.params[1], rb.bse[1], rb.tvalues[1]))),
                    ra.rsquared, rb.rsquared)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "dpol": Numero(dpol, 1)},
        tabelle={"A": taba, "B": tabb}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("decA"), "b": Quesito("effA"), "c": Quesito("decB"),
                 "d": Quesito("simm"), "e": Quesito("dir")},
        attese=[lambda r: r["decA"] == "rifiuta", lambda r: r["decB"] == "rifiuta",
                lambda r: r["bA"].valore > 5, lambda r: r["simm"] == "sì",
                lambda r: abs(r["inv"].valore - r["bB"].valore) > 0.01, identita],
        margini=[Margin(stat=ra.tvalues[1], crit=Z)], figure={"nuvola": figura})


@exercise("e01_04", modulo=1, livello=2, tipo="tipi-di-dato-e-cause-di-problemi")
def spesa_riportata(rng):
    """Show that a regressor measured with error biases the slope and that more data does not cure it."""
    n, grande, beta, sd_vera, sd_err = 200, 20000, 1.5, 40.0, 30.0

    def campione(m):
        """Draw ``m`` households: true weekly spending, reported spending and monthly spending."""
        vera = rng.normal(150.0, sd_vera, m)
        riportata = vera + rng.normal(0.0, sd_err, m)
        return vera, riportata, 120.0 + beta * vera + rng.normal(0.0, 30.0, m)

    vera, rip, y = campione(n)
    vera_g, rip_g, y_g = campione(grande)
    r_vera, tab_vera = _fit(y, {"spesa_vera": vera})
    r_rip, tab_rip = _fit(y, {"spesa_rip": rip})
    r_gr, tab_gr = _fit(y_g, {"spesa_rip": rip_g}, stats=("n", "r2"))
    medie = [vera.mean(), rip.mean()]
    sd = [vera.std(ddof=1), rip.std(ddof=1)]
    desc = "\n".join(["| variabile | media | deviazione standard |", "|---|---|---|",
                      *(f"| {nome} | {m:.3f} | {s:.3f} |".replace(".", ",")
                        for nome, m, s in zip(("spesa_vera", "spesa_rip"), medie, sd))])

    def answers(mv, mr, bv, br, bg, sg, sdv, sdr):
        """Return every answer from the printed means, deviations and slopes and the large-sample se."""
        t_g = (bg - beta) / sg
        return {"mv": Numero(mv, 3), "mr": Numero(mr, 3), "sd_v": Numero(sdv, 3),
                "sd_r": Numero(sdr, 3), "dm": Numero(100 * (mr - mv) / mv, 2), "r_pic": Numero(br / bv, 2),
                "r_gr": Numero(bg / beta, 2), "dec": _decide(t_g),
                "elimina": "sì" if abs(t_g) < Z else "no", "t_g": Numero(t_g, 1),
                "b_vera": Numero(bv, 4), "b_rip": Numero(br, 4), "b_gr": Numero(bg, 4),
                "s_gr": Numero(sg, 5)}

    def studente(tabelle):
        """Rebuild the answers from the printed means and the three printed regressions."""
        m = _righe(desc)
        return answers(m["spesa_vera"][0], m["spesa_rip"][0], tabelle["vera"].rows["spesa_vera"]["coef"],
                       tabelle["rip"].rows["spesa_rip"]["coef"], tabelle["grande"].rows["spesa_rip"]["coef"],
                       tabelle["grande"].rows["spesa_rip"]["se"], m["spesa_vera"][1], m["spesa_rip"][1])

    def limite_coerente(r):
        """Check that the large-sample slope sits at the attenuated value and the small one close to it."""
        fattore = sd_vera**2 / (sd_vera**2 + sd_err**2)
        return (abs(r["r_gr"].valore - fattore) < 0.03 and abs(r["r_pic"].valore - fattore) < 0.15
                and abs(r["r_pic"].valore - r["r_gr"].valore) < 0.15)

    def figura(path):
        """Draw the clouds with the two lines, and the intervals of the slope against the true value."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 3.1), gridspec_kw={"width_ratios": [1.15, 1]})
        k = slice(0, 100)
        a1.plot(vera[k], y[k], "o", color=es.GRAY, ms=3, alpha=0.6, label="spesa vera")
        a1.plot(rip[k], y[k], "o", color=es.RED, ms=3, alpha=0.5, label="spesa riportata")
        _retta(a1, np.concatenate([vera, rip]), r_vera, es.BLUE, "retta con la spesa vera")
        _retta(a1, np.concatenate([vera, rip]), r_rip, es.RED, "retta con la spesa riportata")
        a1.set_xlabel("spesa settimanale al supermercato")
        a1.set_ylabel("spesa mensile non alimentare")
        es.commas(a1)
        a1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), fontsize=8)
        _intervalli(a2, es, [(2, r_vera.params[1], r_vera.bse[1], "spesa vera, campione piccolo", es.BLUE),
                             (1, r_rip.params[1], r_rip.bse[1], "riportata, campione piccolo", es.RED),
                             (0, r_gr.params[1], r_gr.bse[1], "riportata, campione grande", es.AMBER)],
                    "pendenza, con intervallo al 95%", riferimento=(beta, "valore usato nei dati"),
                    ancora=-0.3)
        fig.subplots_adjust(wspace=0.3)
        es.save(fig, path)

    truth = answers(medie[0], medie[1], r_vera.params[1], r_rip.params[1], r_gr.params[1], r_gr.bse[1],
                    sd[0], sd[1])
    return Draft(
        dati=None,
        parametri={"n": Numero(n, 0), "grande": Numero(grande, 0), "beta": Numero(beta, 1)},
        tabelle={"desc": desc, "vera": tab_vera, "rip": tab_rip, "grande": tab_gr},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("dm"), "b": Quesito("r_pic"), "c": Quesito("r_gr"),
                 "d": Quesito("dec"), "e": Quesito("elimina")},
        attese=[lambda r: abs(r["dm"].valore) < 3, lambda r: r["r_pic"].valore < 0.85,
                lambda r: r["dec"] == "rifiuta", lambda r: r["elimina"] == "no", limite_coerente],
        margini=[Margin(stat=truth["t_g"].valore, crit=Z)], figure={"errore": figura})


@exercise("e01_05", modulo=1, livello=3, punti=4,
          tipo=("causalita-criteri-e-confutazione", "tipi-di-dato-e-cause-di-problemi"))
def gelati_incidenti(rng):
    """Show a spurious association induced by a common cause and refute the naive causal reading."""
    n, dg, dt = 250, 2.0, 3.0
    temp = rng.normal(27.0, 2.0, n)
    gel = 4.0 + 0.5 * (temp - 27.0) + rng.normal(0.0, 0.6, n)
    inc = 10.0 + 1.2 * (temp - 27.0) + rng.normal(0.0, 1.3, n)
    r1, tab1 = _fit(inc, {"gelati": gel})
    r2, tab2 = _fit(inc, {"gelati": gel, "temperatura": temp})
    ra, taba = _fit(gel, {"temperatura": temp})

    def answers(m1, m2, aux):
        """Return every answer from the printed rows of the two models and the auxiliary regression."""
        t_naive = (m2["gelati"]["coef"] - m1["gelati"]["coef"]) / m2["gelati"]["se"]
        return {"dec1": _decide(m1["gelati"]["t"]), "eff1": Numero(dg * m1["gelati"]["coef"], 2),
                "dec2": _decide(m2["gelati"]["t"]), "effT": Numero(dt * m2["temperatura"]["coef"], 2),
                "decT": _decide(aux["temperatura"]["t"]), "naive": _decide(t_naive),
                "t_naive": Numero(t_naive, 1), "t1": Numero(m1["gelati"]["t"], 2),
                "t2": Numero(m2["gelati"]["t"], 2), "tT": Numero(aux["temperatura"]["t"], 2),
                "b1": Numero(m1["gelati"]["coef"], 4), "b2": Numero(m2["gelati"]["coef"], 4),
                "s2": Numero(m2["gelati"]["se"], 5), "bT": Numero(m2["temperatura"]["coef"], 4),
                "dT": Numero(aux["temperatura"]["coef"], 4)}

    def righe(res, nomi):
        """Return the rows of a fit as the dictionaries the table parser would give."""
        return {nome: {"coef": res.params[i + 1], "se": res.bse[i + 1], "t": res.tvalues[i + 1]}
                for i, nome in enumerate(nomi)}

    def studente(tabelle):
        """Rebuild the answers from the three printed tables."""
        return answers(tabelle["m1"].rows, tabelle["m2"].rows, tabelle["aux"].rows)

    def residuo_parziale(_risposte):
        """Check that the slope of ``inc`` net of the temperature effect on ``gel`` is the Model 2 slope."""
        netto = inc - r2.params[2] * (temp - temp.mean())
        return abs(sm.OLS(netto, sm.add_constant(gel)).fit().params[1] - r2.params[1]) < 1e-9

    def figura(path):
        """Draw the raw cloud with the Model 1 line and the cloud net of temperature with the Model 2 line."""
        es, plt = _stile()
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.1, 3.0), sharey=True)
        a1.plot(gel, inc, "o", color=es.GRAY, ms=3, alpha=0.55)
        _retta(a1, gel, r1, es.RED)
        a1.set_title("senza controllo (Modello 1)", fontsize=9)
        netto = inc - r2.params[2] * (temp - temp.mean())
        a2.plot(gel, netto, "o", color=es.GRAY, ms=3, alpha=0.55)
        _retta(a2, gel, sm.OLS(netto, sm.add_constant(gel)).fit(), es.BLUE)
        a2.set_title("al netto della temperatura (Modello 2)", fontsize=9)
        for ax in (a1, a2):
            ax.set_xlabel("gelati")
            es.commas(ax)
        a1.set_ylabel("incidenti")
        a2.set_ylabel("")
        fig.subplots_adjust(wspace=0.08)
        es.save(fig, path)

    truth = answers(righe(r1, ["gelati"]), righe(r2, ["gelati", "temperatura"]),
                    righe(ra, ["temperatura"]))
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "dg": Numero(dg, 0), "dt": Numero(dt, 0)},
        tabelle={"m1": tab1, "m2": tab2, "aux": taba}, risposte=truth, studente=studente,
        quesiti={"a": Quesito("dec1"), "b": Quesito("eff1"), "c": Quesito("dec2"),
                 "d": Quesito("effT"), "e": Quesito("decT"), "f": Quesito("naive")},
        attese=[lambda r: r["dec1"] == "rifiuta", lambda r: r["dec2"] == "non rifiuta",
                lambda r: r["decT"] == "rifiuta", lambda r: r["naive"] == "rifiuta",
                lambda r: r["eff1"].valore > 2, lambda r: r["effT"].valore > 2, residuo_parziale],
        margini=[Margin(stat=r1.tvalues[1], crit=Z), Margin(stat=r2.tvalues[1], crit=Z),
                 Margin(stat=ra.tvalues[1], crit=Z), Margin(stat=r2.tvalues[2], crit=Z),
                 Margin(stat=truth["t_naive"].valore, crit=Z)],
        figure={"controllo": figura})


@exercise("e01_06", modulo=1, livello=3, punti=4,
          tipo=("causalita-criteri-e-confutazione", "tipi-di-dato-e-cause-di-problemi"))
def capm_fondo(rng):
    """Validate the CAPM on a fund: test the intercept and the slope, and read the idiosyncratic risk."""
    n, dm = 240, 3.0
    mercato = rng.normal(0.6, 4.4, n)
    fondo = 0.10 + 1.12 * mercato + rng.normal(0.0, 2.4, n)
    res, tab = _fit(fondo, {"mercato": mercato})

    def answers(const, mkt, n_oss, ssr):
        """Return every answer from the printed rows of ``const`` and ``mercato`` and the SSR line."""
        t_beta = (mkt["coef"] - 1.0) / mkt["se"]
        return {"serie": "sì", "decA": _decide(const["t"]), "prova": "no", "decB": _decide(t_beta),
                "eff": Numero(dm * mkt["coef"], 2), "sigma": Numero(np.sqrt(ssr / (n_oss - 2)), 3),
                "ssr": Numero(ssr, 2), "a": Numero(const["coef"], 4), "ta": Numero(const["t"], 2),
                "t0": Numero(mkt["t"], 2), "b": Numero(mkt["coef"], 4), "sb": Numero(mkt["se"], 5),
                "tb": Numero(t_beta, 2), "ic_lo": Numero(mkt["coef"] - Z * mkt["se"], 3),
                "ic_hi": Numero(mkt["coef"] + Z * mkt["se"], 3)}

    def studente(tabelle):
        """Rebuild the answers from the printed regression and its statistics line."""
        t = tabelle["ols"]
        return answers(t.rows["const"], t.rows["mercato"], t.stats["n"], t.stats["ssr"])

    def scomposizione(_risposte):
        """Check Var(R) = beta^2 Var(Rm) + sigma^2 as an exact identity of the sample moments."""
        s2 = np.var(fondo, ddof=1)
        return abs(s2 - (res.params[1] ** 2 * np.var(mercato, ddof=1) + res.ssr / (n - 1))) < 1e-9

    def figura(path):
        """Draw the cloud, the fitted line and the slope-one line of a fund that only mirrors the market."""
        es, plt = _stile()
        fig, ax = plt.subplots(figsize=(6.1, 3.2))
        ax.plot(mercato, fondo, "o", color=es.GRAY, ms=3, alpha=0.55)
        g = np.linspace(mercato.min(), mercato.max(), 50)
        ax.plot(g, res.params[0] + res.params[1] * g, color=es.BLUE, lw=1.6,
                label=f"retta stimata, pendenza {res.params[1]:.3f}".replace(".", ","))
        ax.plot(g, g, color=es.RED, ls="--", lw=1.2, label="retta di pendenza 1")
        ax.set_xlabel("extra-rendimento del mercato (%)")
        ax.set_ylabel("extra-rendimento del fondo (%)")
        es.commas(ax)
        ax.legend(loc="upper left")
        es.save(fig, path)

    def riga(i):
        """Return row ``i`` of the fit as the dictionary the table parser would give."""
        return {"coef": res.params[i], "se": res.bse[i], "t": res.tvalues[i]}

    truth = answers(riga(0), riga(1), n, res.ssr)
    return Draft(
        dati=None, parametri={"n": Numero(n, 0), "dm": Numero(dm, 0)}, tabelle={"ols": tab},
        risposte=truth, studente=studente,
        quesiti={"a": Quesito("serie"), "b": Quesito("decA"), "c": Quesito("prova"),
                 "d": Quesito("decB"), "e": Quesito("eff"), "f": Quesito("sigma")},
        attese=[lambda r: r["decA"] == "non rifiuta", lambda r: r["decB"] == "rifiuta",
                lambda r: r["b"].valore > 1, lambda r: 1 < r["sigma"].valore < 5, scomposizione],
        margini=[Margin(stat=res.tvalues[0], crit=Z), Margin(stat=truth["tb"].valore, crit=Z)],
        figure={"capm": figura})
