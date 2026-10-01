#!/usr/bin/env python3
"""Figure della soluzione dell'appello di Econometria del 17 gennaio 2023.

Dieci figure, una per domanda.  Nessun dato reale e' disponibile per questo
appello (cfr. `_teoria/dati.md`): tutto cio' che si vede e' costruito
analiticamente dall'output di regressione riportato nel testo, oppure letto
sul rendering delle figure gretl del PDF d'esame (le letture sono dichiarate
in didascalia), oppure simulato con seme fissato e dichiarato tale.

    python3 figure/2023-01-17/plots.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import numpy as np, econstyle as es
from scipy import stats
es.use()
OUT = pathlib.Path(__file__).resolve().parent

import matplotlib.pyplot as plt

SEED = 20230117


def it(x, d=4):
    """Numero con la virgola decimale, per le etichette dei grafici."""
    return f"{x:.{d}f}".replace(".", ",")


# =====================================================================
#  Parametri letti dal testo d'esame
# =====================================================================
# --- Esercizio 1 -----------------------------------------------------
ADF_USA, ADF_AUS, ADF_CRIT = -0.686, -0.401, -3.43
EG_STAT, EG_P = -3.779, 0.014
G0, SE_G0 = 0.181332, 0.0784053          # costante dell'ECM
LAM, SE_LAM = -0.144386, 0.0431124       # coefficiente di ecm_1
G1, SE_G1 = 0.557456, 0.101152           # coefficiente di d_usa
T_ECM = 122

# ACF/PACF dei residui dell'ECM, lette sul rendering della Figura 2 (p. 3)
ACF_RES = [-0.033, 0.029, 0.174, -0.096, 0.142, 0.114, 0.047, -0.089,
           0.054, -0.059, -0.036, -0.013, -0.033, -0.008, 0.119, -0.059,
           -0.073, 0.105, -0.151, 0.110]
PACF_RES = [-0.035, 0.028, 0.177, -0.088, 0.131, 0.102, 0.083, -0.158,
            0.040, -0.080, -0.020, -0.095, 0.024, -0.010, 0.181, -0.077,
            -0.033, 0.057, -0.095, 0.059]

# ACF/PACF di Dlog(usa), lette sul rendering della Figura 3 (p. 4)
ACF_DUSA = [0.306, 0.302, 0.151, 0.131, 0.072, 0.046, 0.003, -0.095,
            0.118, 0.102, 0.099, -0.095, -0.030, -0.036, -0.092, 0.036,
            -0.023, 0.033, 0.030, 0.115]
PACF_DUSA = [0.306, 0.230, 0.013, 0.026, 0.000, -0.010, -0.026, -0.122,
             0.204, 0.105, -0.003, -0.217, -0.023, 0.039, -0.089, 0.112,
             0.062, 0.046, -0.023, -0.003]

# --- Esercizio 2 -----------------------------------------------------
# Modello (6): l_scrap = a + b1 grant + b2 hrsemp + b3 h_grant
B = {"const": 0.596425, "grant": -0.275495,
     "hrsemp": -0.00429880, "h_grant": 0.00462819}
SE = {"const": 0.0107498, "grant": 0.0455437,
      "hrsemp": 0.000300004, "h_grant": 0.001724751}
# Modello (9): + l_sales
BL = {"const": 1.69601, "grant": -0.081663, "hrsemp": -0.00477343,
      "h_grant": 0.00250093, "l_sales": -0.0724485}
SEL = {"const": 0.107142, "grant": 0.0210214, "hrsemp": 0.000229862,
       "h_grant": 0.000768435, "l_sales": 0.00719269}
# Modello (10): scrap = a + b1 grant + b2 hrsemp + b3 hrsemp^2
Q = {"const": 1.83671, "grant": -0.403453,
     "hrsemp": -0.00751402, "sq_hrsemp": 0.00113981}
QSE = {"const": 0.0234330, "grant": 0.0714537,
       "hrsemp": 0.0012498, "sq_hrsemp": 0.0009034}
DF2 = 316          # g.d.l. implicati dai p-value dell'output (n ~ 320)

# Figura 4 (p. 6): centri dei 471 marcatori, letti sul grafico vettoriale del
# PDF d'esame.  Prima colonna: valore predetto; seconda: residuo.
F4_POINTS = """
    -5.42 -2.58 -4.55 0.94 -4.30 2.35 -3.67 -0.17 -3.61 0.67 -3.52 -0.66 -3.33 1.76 -3.31 0.23
    -3.30 -2.27 -3.14 1.75 -3.06 0.29 -3.00 0.32 -2.98 -0.74 -2.88 -0.79 -2.78 -0.25 -2.75 -0.07
    -2.71 -0.02 -2.69 6.29 -2.67 0.29 -2.66 -1.75 -2.60 0.47 -2.48 -0.32 -2.37 0.46 -2.34 0.00
    -2.32 -0.28 -2.24 -0.77 -2.23 -0.21 -2.23 1.00 -2.22 -0.62 -2.20 0.41 -2.20 -0.88 -2.12 -1.60
    -2.11 -0.49 -2.10 0.08 -2.09 0.55 -2.02 0.52 -2.02 -0.62 -2.02 -0.06 -2.00 0.49 -1.97 0.28
    -1.89 -0.28 -1.83 0.97 -1.82 -0.36 -1.81 -0.55 -1.79 -0.83 -1.78 -0.18 -1.77 0.84 -1.74 0.25
    -1.72 -0.31 -1.72 0.00 -1.72 0.43 -1.70 0.08 -1.67 -0.03 -1.67 -0.51 -1.67 0.26 -1.64 0.41
    -1.63 0.14 -1.61 -0.72 -1.57 -0.25 -1.56 -0.43 -1.54 -0.26 -1.52 0.12 -1.50 0.03 -1.46 -0.07
    -1.45 -0.06 -1.44 -0.10 -1.42 -0.37 -1.38 0.13 -1.37 0.10 -1.37 -0.30 -1.36 0.11 -1.35 0.16
    -1.34 0.88 -1.26 0.01 -1.26 0.03 -1.23 0.56 -1.22 -0.14 -1.22 -0.35 -1.22 -0.07 -1.19 0.25
    -1.19 0.20 -1.15 0.14 -1.15 0.07 -1.15 0.06 -1.14 -0.17 -1.14 -0.07 -1.10 -0.44 -1.10 -0.03
    -1.10 -0.23 -1.09 -0.14 -1.08 0.18 -1.08 -0.14 -1.08 0.19 -1.07 -0.14 -1.06 -0.38 -1.04 -0.05
    -1.04 -0.22 -1.02 -0.03 -1.02 -0.05 -1.01 0.10 -1.01 0.23 -1.00 -0.11 -1.00 -0.08 -1.00 -0.31
    -0.99 -0.03 -0.98 0.20 -0.94 -0.03 -0.93 0.07 -0.93 -0.03 -0.93 0.07 -0.92 0.03 -0.91 -0.10
    -0.90 0.01 -0.87 0.16 -0.86 -0.10 -0.85 -0.22 -0.83 0.31 -0.83 -0.16 -0.82 -0.25 -0.81 -0.17
    -0.80 -0.09 -0.79 0.13 -0.78 -0.04 -0.72 0.08 -0.71 -0.14 -0.70 0.02 -0.68 0.03 -0.67 -0.06
    -0.66 -0.08 -0.66 -0.10 -0.65 0.03 -0.65 0.05 -0.65 0.06 -0.63 -0.05 -0.62 -0.04 -0.62 -0.11
    -0.61 2.93 -0.60 -0.08 -0.60 -0.05 -0.58 0.04 -0.58 -0.04 -0.57 -0.03 -0.57 -0.15 -0.57 -0.08
    -0.56 0.02 -0.56 0.06 -0.56 0.04 -0.54 0.01 -0.52 -0.11 -0.50 -0.04 -0.48 -0.04 -0.47 -0.12
    -0.47 -0.08 -0.45 -0.05 -0.45 0.03 -0.41 0.02 -0.41 -0.07 -0.39 -0.10 -0.37 0.03 -0.37 -0.02
    -0.35 -0.07 -0.35 -0.05 -0.33 -0.04 -0.33 -0.01 -0.32 0.91 -0.31 -0.00 -0.31 0.00 -0.31 -0.03
    -0.30 -0.00 -0.27 -0.05 -0.26 -0.09 -0.26 -0.07 -0.25 -0.04 -0.24 -0.02 -0.23 -0.06 -0.23 0.03
    -0.22 -0.05 -0.22 -0.02 -0.21 0.01 -0.20 -0.01 -0.20 -0.04 -0.19 -0.07 -0.18 -0.06 -0.16 -0.05
    -0.16 -0.09 -0.16 -0.03 -0.16 -0.03 -0.15 -0.02 -0.14 -0.03 -0.14 -0.03 -0.10 -0.01 -0.10 0.01
    -0.06 -0.06 -0.05 -0.04 -0.04 -0.04 -0.04 -0.06 -0.03 -0.05 -0.03 -0.04 0.01 -0.03 0.01 -0.03
    0.02 -0.04 0.02 -0.05 0.03 -0.04 0.03 -0.03 0.04 -0.05 0.10 -0.06 0.10 -0.04 0.11 -0.04
    0.11 -0.04 0.12 -0.04 0.14 -0.05 0.14 -0.05 0.16 -0.04 0.16 -0.05 0.17 -0.04 0.18 -0.04
    0.19 -0.05 0.21 -0.05 0.21 -0.05 0.22 -0.05 0.22 -0.04 0.24 -0.05 0.24 -0.05 0.25 -0.05
    0.26 -0.05 0.27 -0.05 0.27 -0.05 0.28 -0.05 0.28 -0.05 0.28 -0.05 0.29 -0.05 0.29 -0.05
    0.30 -0.05 0.31 -0.05 0.32 -0.05 0.32 -0.05 0.32 -0.05 0.33 -0.05 0.34 -0.05 0.35 -0.05
    0.35 -0.05 0.36 -0.05 0.36 -0.05 0.37 -0.05 0.37 -0.05 0.38 -0.05 0.38 -0.05 0.38 -0.05
    0.39 -0.05 0.40 -0.05 0.40 -0.05 0.41 -0.05 0.41 -0.05 0.43 -0.05 0.43 -0.05 0.44 -0.05
    0.45 -0.05 0.47 -0.05 0.47 -0.05 0.49 -0.05 0.50 -0.06 0.51 -0.06 0.51 -0.06 0.51 0.95
    0.51 -0.06 0.52 -0.05 0.54 -0.05 0.56 -0.05 0.56 -0.06 0.57 -0.06 0.57 -0.06 0.58 -0.05
    0.58 -0.06 0.60 -0.05 0.61 -0.07 0.62 -0.06 0.62 -0.06 0.62 -0.05 0.63 -0.06 0.63 -0.06
    0.63 -0.07 0.64 -0.07 0.67 -0.07 0.67 -0.06 0.68 -0.04 0.69 -0.06 0.70 -0.07 0.71 -0.08
    0.73 -0.08 0.73 -0.06 0.74 -0.05 0.75 -0.07 0.76 -0.08 0.76 -0.02 0.77 -0.07 0.77 -0.04
    0.79 -0.04 0.82 -0.06 0.82 -0.08 0.83 -0.06 0.89 -0.07 0.90 -0.05 0.90 -0.08 0.90 -0.03
    0.91 -0.08 0.91 -0.03 0.92 -0.03 0.92 -0.05 0.94 -0.07 0.97 -0.08 1.00 -0.03 1.01 -0.08
    1.02 -0.02 1.04 -0.12 1.04 -0.06 1.04 0.97 1.06 -0.07 1.07 -0.06 1.08 0.00 1.08 4.02
    1.09 -0.06 1.16 -0.08 1.18 -0.16 1.18 -0.05 1.19 -0.12 1.20 -0.00 1.20 -0.15 1.21 -0.11
    1.24 -0.05 1.25 -0.08 1.26 -0.20 1.26 -0.17 1.27 -0.16 1.28 -0.12 1.29 -0.01 1.30 -0.08
    1.31 -0.23 1.31 -0.06 1.33 0.02 1.33 -0.04 1.35 -0.14 1.35 -0.11 1.35 0.05 1.35 0.02
    1.38 -0.08 1.39 -0.11 1.40 -0.11 1.41 -0.32 1.41 -0.28 1.42 0.06 1.43 -0.15 1.46 -0.25
    1.46 -0.06 1.47 0.02 1.47 -0.07 1.49 -0.11 1.50 -0.15 1.50 -0.27 1.50 0.02 1.52 -0.09
    1.53 -0.29 1.53 -0.19 1.53 -0.23 1.54 0.00 1.56 -0.26 1.58 -0.23 1.59 -0.13 1.60 0.11
    1.60 -0.02 1.61 -0.06 1.64 -0.06 1.64 -0.24 1.65 0.11 1.66 0.09 1.68 -0.28 1.68 0.08
    1.69 -0.18 1.71 -0.19 1.72 0.22 1.72 -0.20 1.72 -0.01 1.73 -0.38 1.73 -0.22 1.73 -0.22
    1.73 0.14 1.75 0.15 1.76 -0.47 1.80 -0.23 1.84 -0.35 1.84 -0.10 1.86 -0.31 1.88 0.07
    1.89 0.15 1.91 0.13 1.93 0.21 1.95 0.07 1.95 -0.14 1.95 0.06 1.96 -0.15 1.97 -0.44
    1.97 -0.15 1.98 0.25 2.00 -0.25 2.01 0.40 2.09 0.09 2.09 0.21 2.10 -0.09 2.12 -0.29
    2.13 -0.45 2.15 -0.10 2.20 -0.39 2.21 -0.75 2.25 0.38 2.27 0.30 2.27 0.25 2.31 -0.28
    2.32 0.13 2.37 -0.30 2.42 -0.20 2.43 0.00 2.43 -0.05 2.44 0.12 2.46 -0.70 2.49 0.32
    2.52 0.58 2.53 -0.40 2.58 -0.24 2.60 -0.50 2.60 -0.24 2.61 0.27 2.63 0.22 2.65 0.91
    2.69 0.55 2.72 0.39 2.72 0.07 2.74 0.01 2.80 0.16 2.82 0.23 2.87 0.20 2.94 1.61
    2.96 -0.09 2.98 0.37 3.01 -0.33 3.07 -0.71 3.08 -0.77 3.11 0.17 3.14 0.48 3.21 0.34
    3.30 -1.09 3.35 0.39 3.36 0.68 3.39 -0.39 3.41 0.38 3.48 -0.66 3.61 0.24 3.66 -1.41
    3.68 2.33 3.72 0.75 3.76 -2.10 3.81 1.00 3.86 0.70 3.96 0.74 4.06 -0.97 4.10 -0.67
    4.26 -1.45 4.37 1.62 4.38 -1.23 4.41 -1.34 4.42 2.80 4.49 3.22 4.66 -0.65
"""


# =====================================================================
#  Simulazioni (seme fissato) usate dalle figure 1 e 2
# =====================================================================
def df_null(kind, T=122, R=20000, seed=SEED):
    """Distribuzione nulla della t di Dickey-Fuller, per simulazione.

    kind: 'none' (nessuna deterministica) | 'const' | 'trend'.
    """
    rng = np.random.default_rng(seed)
    out = np.empty(R)
    for r in range(R):
        y = np.cumsum(rng.standard_normal(T + 1))
        dy, ylag = np.diff(y), y[:-1]
        n = len(dy)
        if kind == "none":
            X = ylag[:, None]
        elif kind == "const":
            X = np.column_stack([np.ones(n), ylag])
        else:
            X = np.column_stack([np.ones(n), np.arange(1, n + 1), ylag])
        b, *_ = np.linalg.lstsq(X, dy, rcond=None)
        e = dy - X @ b
        s2 = e @ e / (n - X.shape[1])
        V = s2 * np.linalg.inv(X.T @ X)
        out[r] = b[-1] / np.sqrt(V[-1, -1])
    return out


def eg_null(T=122, R=20000, seed=SEED + 1):
    """Distribuzione nulla della statistica di Engle-Granger (2 variabili)."""
    rng = np.random.default_rng(seed)
    out = np.empty(R)
    for r in range(R):
        x = np.cumsum(rng.standard_normal(T))
        y = np.cumsum(rng.standard_normal(T))
        X = np.column_stack([np.ones(T), x])
        b, *_ = np.linalg.lstsq(X, y, rcond=None)
        u = y - X @ b
        du, ul = np.diff(u), u[:-1]
        Z = ul[:, None]
        bb, *_ = np.linalg.lstsq(Z, du, rcond=None)
        e = du - Z @ bb
        s2 = e @ e / (len(du) - 1)
        out[r] = bb[0] / np.sqrt(s2 / (Z.T @ Z)[0, 0])
    return out


def kde(sample, grid, bw=None):
    """Densita' liscia (gaussiana) senza dipendenze extra."""
    s = np.asarray(sample)
    if bw is None:
        bw = 1.06 * s.std() * len(s) ** (-0.2)
    z = (grid[:, None] - s[None, :]) / bw
    return np.exp(-0.5 * z ** 2).sum(axis=1) / (len(s) * bw * np.sqrt(2 * np.pi))


# =====================================================================
#  D1 — quale regressione di Dickey-Fuller
# =====================================================================
def d01():
    rng = np.random.default_rng(SEED)
    # La Figura 1 dell'esame disegna 124 trimestri (1970:1-2000:4): la serie
    # `usa` va da 38,3 a 100,7 e la deviazione standard delle sue differenze
    # prime e' 0,515 punti indice.  Su questi tre numeri e' calibrata la
    # simulazione illustrativa.
    T, Y0, Y1, SD = 124, 38.3, 100.7, 0.515
    t = np.arange(T)
    drift = (Y1 - Y0) / (T - 1)
    rw = Y0 + drift * t + np.cumsum(rng.standard_normal(T) * SD)
    # alternativa trend-stazionaria con lo stesso andamento medio
    ar = np.zeros(T)
    for i in range(1, T):
        ar[i] = 0.75 * ar[i - 1] + rng.standard_normal() * 1.6
    ts = Y0 + drift * t + ar

    fig, axes = plt.subplots(1, 2, figsize=(6.5, 3.05))
    ax = axes[0]
    ax.plot(1970 + t / 4, rw, color=es.BLUE, lw=1.3,
            label="trend stocastico:  I(1) con drift")
    ax.plot(1970 + t / 4, ts, color=es.AMBER, lw=1.3, ls="--",
            label="trend deterministico:  I(0) attorno a una retta")
    ax.plot(1970 + t / 4, Y0 + drift * t, color=es.GRAY, lw=0.9, ls=":")
    ax.set_title("A. Le due ipotesi compatibili con la Figura 1", loc="left")
    ax.set_xlabel("anno")
    ax.set_ylabel("indice del GDP reale")
    # La legenda stava in basso a destra, dove le due serie la attraversano:
    # sale in alto a sinistra, sopra il profilo crescente.
    ax.set_ylim(34, 122)
    ax.legend(loc="upper left", fontsize=7.8, framealpha=1.0)
    es.commas(ax, "y", decimals=0)

    ax = axes[1]
    grid = np.linspace(-6.0, 2.5, 500)
    crit = {}
    specs = [("none", es.GRAY, r"$\Delta y_t=\delta y_{t-1}+u_t$"),
             ("const", es.AMBER, r"$\Delta y_t=\alpha+\delta y_{t-1}+u_t$"),
             ("trend", es.TEAL, r"$\Delta y_t=\alpha+\gamma t+\delta y_{t-1}+u_t$")]
    peak = 0.0
    for kind, col, lab in specs:
        sim = df_null(kind)
        crit[kind] = np.quantile(sim, 0.05)
        dens = kde(sim, grid)
        peak = max(peak, dens.max())
        ax.plot(grid, dens, color=col, lw=1.4, label=lab)
        ax.axvline(crit[kind], color=col, ls=":", lw=1.0, ymax=0.46)
    # Le densita' restano nella meta' bassa: la fascia libera in alto ospita
    # legenda e didascalie, che prima coprivano curve e rette verticali.
    ax.set_ylim(0, peak * 2.25)
    nomi = {"none": "senza deterministica", "const": "con costante",
            "trend": "con costante e trend"}
    for i, (kind, col, _) in enumerate(specs):
        ax.annotate(f"{nomi[kind]}:  " + it(crit[kind], 2),
                    xy=(0.015, 0.74 - 0.08 * i), xycoords="axes fraction",
                    fontsize=8, color=col, ha="left", va="center",
                    fontweight="bold", zorder=6)
    ax.axvline(ADF_CRIT, color=es.RED, lw=1.8, ymax=0.46)
    ax.annotate("critico dato dal testo:  " + it(ADF_CRIT, 2),
                xy=(0.015, 0.50), xycoords="axes fraction",
                ha="left", va="center", fontsize=8, color=es.RED,
                fontweight="bold", zorder=6)
    ax.set_title("B. Densita' nulla e critico al 5% nei tre casi", loc="left")
    ax.set_xlabel("statistica di Dickey-Fuller")
    ax.set_ylabel("densita'")
    ax.set_yticks([])
    ax.set_xlim(-6.0, 2.5)
    ax.legend(loc="upper right", fontsize=7.8, labelspacing=0.3, framealpha=1.0)
    es.commas(ax, "x", decimals=0)

    fig.tight_layout()
    es.save(fig, OUT / "d01-specificazione-df.pdf")
    return crit


# =====================================================================
#  D2 — radici unitarie e cointegrazione
# =====================================================================
def d02():
    fig, axes = plt.subplots(2, 1, figsize=(6.4, 4.5))

    ax = axes[0]
    s = df_null("trend")
    grid = np.linspace(-6.0, 2.5, 600)
    dens = kde(s, grid)
    ax.plot(grid, dens, color=es.BLUE, lw=1.4, label="densita' DF (costante e trend)")
    ax.fill_between(grid, dens, color=es.BLUEBG)
    m = grid <= ADF_CRIT
    ax.fill_between(grid[m], dens[m], color=es.RED, alpha=0.30,
                    label="regione di rifiuto al 5%:  $t<-3{,}43$")
    ax.vlines(ADF_CRIT, 0, 0.72 * dens.max(), color=es.RED, ls="--", lw=1.1)
    for v, lab, dy in [(ADF_USA, "usa  " + it(ADF_USA, 3), 0.86),
                       (ADF_AUS, "aus  " + it(ADF_AUS, 3), 0.62)]:
        ax.vlines(v, 0, dy * dens.max() * 1.04, color=es.GREEN, lw=1.8)
        ax.annotate(lab, xy=(v, dy * dens.max()), xytext=(6, 0),
                    textcoords="offset points", fontsize=8.5, color=es.GREEN,
                    fontweight="bold", va="center", zorder=6, bbox=dict(facecolor="white", alpha=0.92, edgecolor="none", pad=1.3))
    ax.set_title("A. Serie in livello: nessuna delle due statistiche entra nella regione di rifiuto",
                 loc="left")
    ax.set_ylabel("densita'")
    ax.set_yticks([])
    ax.set_xlim(-6.0, 2.5)
    ax.legend(loc="upper left", fontsize=8.4, framealpha=1.0)
    es.commas(ax, "x", decimals=0)

    ax = axes[1]
    s = eg_null()
    grid = np.linspace(-6.5, 1.0, 600)
    dens = kde(s, grid)
    q05 = np.quantile(s, 0.05)
    psim = (s < EG_STAT).mean()
    ax.plot(grid, dens, color=es.BLUE, lw=1.4,
            label="densita' di Engle-Granger (residui, 2 variabili)")
    ax.fill_between(grid, dens, color=es.BLUEBG)
    m = grid <= q05
    ax.fill_between(grid[m], dens[m], color=es.RED, alpha=0.30,
                    label="regione di rifiuto al 5%:  $t<$ " + it(q05, 2))
    m2 = grid <= EG_STAT
    ax.fill_between(grid[m2], dens[m2], color=es.GREEN, alpha=0.45,
                    label="coda oltre la statistica: " + it(100 * psim, 1)
                          + "% simulato, 1,4% dal testo")
    ax.vlines(EG_STAT, 0, 0.60 * dens.max(), color=es.GREEN, lw=2.0)
    ax.annotate("residui:  " + it(EG_STAT, 3), xy=(EG_STAT, 0.55 * dens.max()),
                xytext=(-8, 0), textcoords="offset points", fontsize=8.5,
                color=es.GREEN, fontweight="bold", ha="right", va="center",
                zorder=6, bbox=dict(facecolor="white", alpha=0.92, edgecolor="none", pad=1.3))
    ax.set_title("B. Residui della relazione di lungo periodo: la statistica cade nella regione di rifiuto",
                 loc="left")
    ax.set_xlabel("statistica del test di radice unitaria")
    ax.set_ylabel("densita'")
    ax.set_yticks([])
    ax.set_xlim(-6.5, 1.0)
    ax.legend(loc="upper left", fontsize=8.2, framealpha=1.0)
    es.commas(ax, "x", decimals=0)

    fig.tight_layout()
    es.save(fig, OUT / "d02-cointegrazione.pdf")
    return q05, psim


# =====================================================================
#  D3 — correlogramma dei residui dell'ECM
# =====================================================================
def d03():
    fig, axes = plt.subplots(2, 1, figsize=(6.4, 4.3), sharex=True)
    es.acf_pacf(ACF_RES, PACF_RES, n=T_ECM, axes=axes)
    band = 1.96 / np.sqrt(T_ECM)
    for ax, vals in zip(axes, (ACF_RES, PACF_RES)):
        ax.set_xticks(range(0, 21, 5))
        ax.set_xlim(0.2, 20.8)
        # econstyle etichetta la banda con "$\pm0,177$": dentro mathtext la
        # virgola fra cifre diventa uno spazio, quindi il numero esce dal math.
        hs, ls = ax.get_legend_handles_labels()
        ls = [r"$\pm$" + it(band, 3) if t.startswith("$\\pm") else t for t in ls]
        ax.legend(hs, ls, loc="upper right", fontsize=8.2)
        k = int(np.argmax(np.abs(vals))) + 1
        v = vals[k - 1]
        ax.annotate(f"ritardo {k}: " + it(v, 3),
                    xy=(k, v), xytext=(10, 12 if v > 0 else -16),
                    textcoords="offset points", fontsize=8.4, color=es.AMBER,
                    fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=es.AMBER, lw=0.8))
    axes[0].set_title("Residui dell'ECM: una sola barra su 40 esce dalle bande "
                      + r"$\pm 1{,}96/\sqrt{122}=\pm 0{,}177$", loc="left")
    fig.tight_layout()
    es.save(fig, OUT / "d03-correlogramma-residui.pdf")
    return band


# =====================================================================
#  D4 — assorbimento del disequilibrio
# =====================================================================
def d04():
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.1))
    _, _, tab = es.decay(LAM, horizon=24, targets=(0.5, 0.8), ax=axes[0],
                         title="A. Quota di disequilibrio ancora aperta",
                         ylabel=r"$(1+\hat\lambda)^h$")
    axes[0].set_ylim(0, 1.05)
    axes[0].set_xlabel("trimestri dopo lo shock ($h$)")

    h = np.arange(0, 25)
    z0 = -1.0                                   # disequilibrio iniziale unitario
    z = z0 * (1 + LAM) ** h
    dz = LAM * z0 * (1 + LAM) ** h              # contributo al tasso di crescita
    ax = axes[1]
    ax.axhline(0, color=es.GRAY, lw=0.8)
    ax.plot(h, z, "o-", color=es.BLUE, lw=1.5, ms=3.6,
            label=r"disequilibrio $z_{t+h}$  (parte da $-1$)")
    ax.plot(h, dz, "s--", color=es.GREEN, lw=1.4, ms=3.4,
            label=r"spinta sulla crescita  $\hat\lambda\,z_{t+h-1}>0$")
    ax.annotate("la spinta resta positiva:\nl'Australia cresce di piu'",
                xy=(3, dz[3]), xytext=(5.5, -0.72), textcoords="data",
                fontsize=8, color=es.GREEN, fontweight="bold", zorder=6,
                ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=es.GREEN, lw=0.8))
    ax.set_title("B. Il segno del meccanismo di correzione", loc="left")
    ax.set_xlabel("trimestri dopo lo shock ($h$)")
    ax.set_ylabel("scostamento dall'equilibrio")
    ax.legend(loc="lower right", fontsize=7.6, framealpha=1.0)
    es.commas(ax, "y", decimals=1)

    fig.tight_layout()
    es.save(fig, OUT / "d04-assorbimento-ecm.pdf")
    return tab


# =====================================================================
#  D5 — identificazione ARMA per Dlog(usa)
# =====================================================================
def ar2_from_pacf(p11, p22):
    """Yule-Walker inverso: dai primi due valori della PACF ai phi di un AR(2)."""
    phi2 = p22
    phi1 = p11 * (1 - p22)
    return phi1, phi2


def ar2_acf(phi1, phi2, k):
    r = [1.0, phi1 / (1 - phi2)]
    while len(r) <= k:
        r.append(phi1 * r[-1] + phi2 * r[-2])
    return np.array(r[1:k + 1])


def d05():
    phi1, phi2 = ar2_from_pacf(PACF_DUSA[0], PACF_DUSA[1])
    K = 20
    acf_th = ar2_acf(phi1, phi2, K)
    pacf_th = np.zeros(K)
    pacf_th[0], pacf_th[1] = PACF_DUSA[0], PACF_DUSA[1]

    fig, axes = plt.subplots(2, 1, figsize=(6.4, 4.5), sharex=True)
    es.acf_pacf(ACF_DUSA, PACF_DUSA, n=T_ECM, axes=axes)
    lags = np.arange(1, K + 1)
    axes[0].plot(lags, acf_th, "-", color=es.AMBER, lw=1.4, zorder=6,
                 label=f"ACF teorica di un AR(2) con $\\phi_1=${it(phi1, 3)}, "
                       f"$\\phi_2=${it(phi2, 3)}")
    axes[1].plot(lags, pacf_th, "-", color=es.AMBER, lw=1.4, zorder=6,
                 label="PACF teorica dello stesso AR(2)")
    for ax in axes:
        ax.set_xticks(range(0, 21, 5))
        ax.set_xlim(0.2, 20.8)
        ax.legend(loc="upper right", fontsize=7.4)
    axes[0].annotate("ritardi 1 e 2 fuori banda,\npoi decadimento",
                     xy=(2, ACF_DUSA[1]), xytext=(26, 6),
                     textcoords="offset points", fontsize=8, color=es.RED,
                     fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))
    axes[1].annotate("troncamento dopo il ritardo 2",
                     xy=(3, PACF_DUSA[2]), xytext=(20, 40),
                     textcoords="offset points", fontsize=8, color=es.RED,
                     fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))
    fig.suptitle(r"$\Delta\log(\mathrm{usa}_t)$: ACF e PACF osservate contro l'AR(2) identificato",
                 x=0.01, ha="left", color=es.BLUE, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.965))
    es.save(fig, OUT / "d05-acf-pacf-dusa.pdf")
    return phi1, phi2, acf_th


# =====================================================================
#  D6 — effetto di un'ora in piu' di formazione
# =====================================================================
def d06():
    b2, b3 = B["hrsemp"], B["h_grant"]
    s2, s3 = SE["hrsemp"], SE["h_grant"]
    tot = b2 + b3
    bound = s2 + s3                     # |Cov| <= se2*se3  =>  se(b2+b3) <= s2+s3
    target = np.log(0.99)

    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.0))

    ax = axes[0]
    hrs = np.linspace(0, 40, 200)
    ax.plot(hrs, 100 * b2 * hrs, color=es.BLUE, lw=1.6,
            label="senza finanziamento:  $\\hat\\beta_2=$ " + it(b2, 5))
    ax.plot(hrs, 100 * tot * hrs, color=es.RED, lw=1.6,
            label="con finanziamento:  $\\hat\\beta_2+\\hat\\beta_3=$ " + it(tot, 5))
    ax.plot(hrs, 100 * target * hrs, color=es.GREEN, lw=1.4, ls="--",
            label="obiettivo: $-1\\%$ per ogni ora")
    ax.axhline(0, color=es.GRAY, lw=0.8)
    ax.annotate("effetto stimato positivo", xy=(32, 100 * tot * 32),
                xytext=(-14, 30), textcoords="offset points", fontsize=8,
                color=es.RED, fontweight="bold", ha="right",
                arrowprops=dict(arrowstyle="->", color=es.RED, lw=0.8))
    ax.set_title("A. Variazione cumulata di $\\log(\\mathrm{scrap})$", loc="left")
    ax.set_xlabel("ore di formazione per addetto")
    ax.set_ylabel("variazione attesa (%)")
    ax.legend(loc="lower left", fontsize=7.4)
    es.commas(ax, "both", decimals=0)

    ax = axes[1]
    es.ci_line(tot, tot - 1.96 * bound, tot + 1.96 * bound, h0=target, ax=ax,
               label="intervallo conservativo al 95%", decimals=5,
               xlabel=r"$\beta_2+\beta_3$  (effetto di un'ora, dato il finanziamento)",
               title="B. Intervallo conservativo al 95%")
    ax.annotate("larghezza massima possibile:\n"
                r"errore standard $\leq$ " + it(bound, 5),
                xy=(tot, -0.52), ha="center", va="top", fontsize=7.6, color=es.GRAY)

    fig.tight_layout()
    es.save(fig, OUT / "d06-effetto-ore.pdf")
    return tot, bound, (tot - target) / bound


# =====================================================================
#  D7 — differenza fra l'azienda A e l'azienda B
# =====================================================================
def d07():
    parts = [("grant $=1$", B["grant"]),
             (r"$5\times$ hrsemp", 5 * B["hrsemp"]),
             (r"$5\times$ h_grant", 5 * B["h_grant"])]
    theta = sum(v for _, v in parts)
    bound = SE["grant"] + 5 * SE["hrsemp"] + 5 * SE["h_grant"]
    lo, hi = theta - 1.96 * bound, theta + 1.96 * bound
    pct = lambda v: 100 * (np.exp(v) - 1)

    fig, axes = plt.subplots(1, 2, figsize=(6.8, 3.2))

    ax = axes[0]
    base = 0.0
    for i, (lab, v) in enumerate(parts):
        col = es.BLUE if v < 0 else es.RED
        ax.bar(i, v, bottom=base, color=col, alpha=0.88, width=0.58)
        ax.annotate(it(v, 4), xy=(i, base + v / 2),
                    xytext=(0, 0), textcoords="offset points",
                    ha="center", va="center", fontsize=7.4,
                    color="white" if abs(v) > 0.05 else col,
                    fontweight="bold")
        if abs(v) <= 0.05:
            ax.annotate(it(v, 4), xy=(i, base + v),
                        xytext=(0, 9 if v > 0 else -13), textcoords="offset points",
                        ha="center", fontsize=7.4, color=col, fontweight="bold")
        nxt = base + v
        if i < 2:
            ax.plot([i + 0.29, i + 0.71], [nxt, nxt], color=es.GRAY, lw=0.7, ls=":")
        base = nxt
    ax.bar(3, theta, color=es.TEAL, width=0.58)
    ax.annotate(it(theta, 4), xy=(3, theta / 2), ha="center", va="center",
                fontsize=8, color="white", fontweight="bold")
    ax.axhline(0, color=es.GRAY, lw=0.9)
    ax.set_xticks(range(4))
    ax.set_xticklabels([p[0] for p in parts] + [r"totale $\theta$"], fontsize=7.4)
    ax.set_ylim(-0.33, 0.055)
    ax.set_title(r"A. Scomposizione di $\theta=\beta_1+5\beta_2+5\beta_3$", loc="left")
    ax.set_ylabel(r"contributo a $\Delta\log(\mathrm{scrap})$")
    es.commas(ax, "y", decimals=2)

    ax = axes[1]
    ax.barh([1], [pct(theta)], color=es.TEAL, height=0.34,
            xerr=[[pct(theta) - pct(lo)], [pct(hi) - pct(theta)]],
            error_kw=dict(ecolor=es.GRAY, capsize=4, lw=1.2))
    ax.barh([0], [100 * theta], color=es.BLUE, alpha=0.5, height=0.34)
    ax.axvline(0, color=es.RED, lw=1.5, ls="--")
    ax.annotate(r"$H_0:\ \theta=0$", xy=(0, 1.62), xytext=(-6, 0),
                textcoords="offset points", fontsize=8.5, color=es.RED,
                fontweight="bold", va="center", ha="right")
    ax.annotate("esatta  " + it(pct(theta), 2) + "%", xy=(pct(theta) / 2, 1),
                ha="center", va="center", fontsize=8.5, color="white",
                fontweight="bold")
    ax.annotate("approssimata  " + it(100 * theta, 2) + "%",
                xy=(100 * theta / 2, 0), ha="center", va="center",
                fontsize=8.5, color="white", fontweight="bold")
    ax.annotate("banda: " + it(pct(lo), 1) + "% / " + it(pct(hi), 1) + "%",
                xy=(pct(lo), 1.34), xytext=(0, 0), textcoords="offset points",
                ha="left", va="center", fontsize=7.4, color=es.GRAY)
    ax.set_yticks([0, 1])
    ax.set_yticklabels([r"$100\,\theta$", r"$100(e^{\theta}-1)$"], fontsize=8.5)
    ax.set_ylim(-0.55, 1.95)
    ax.set_xlim(-40, 14)
    ax.set_xlabel("differenza percentuale attesa (A rispetto a B)", fontsize=8.5)
    ax.set_title("B. Conversione in percentuale", loc="left")
    ax.grid(axis="y", visible=False)
    es.commas(ax, "x", decimals=0)

    fig.tight_layout()
    es.save(fig, OUT / "d07-differenza-aziende.pdf")
    return theta, bound, pct(theta)


# =====================================================================
#  D8 — residui contro valori predetti
# =====================================================================
def d08():
    """Nube (valori predetti, residui) della Figura 4, estratta dal PDF d'esame.

    I 471 marcatori della Figura 4 sono disegnati nel PDF come cerchi
    vettoriali: le coordinate qui sotto sono i loro centri, convertiti in
    unita' di grafico con la calibrazione degli assi (tick -4/-2/0/2/4 in
    ascissa, 7...-3 in ordinata).  Non c'e' quindi nessuna simulazione: il
    pannello A e' la Figura 4 ridisegnata.
    """
    P = np.array(F4_POINTS.split(), dtype=float).reshape(-1, 2)
    yhat, res = P[:, 0], P[:, 1]

    # semi-ampiezza misurata: 90esimo percentile di |residuo| in bin di |yhat|
    # larghi 0,5 (i due bin oltre 4,5 contengono 3 punti e sono esclusi)
    centres, halfw, nobs = [], [], []
    for lo in np.arange(0.0, 4.5, 0.5):
        m = (np.abs(yhat) >= lo) & (np.abs(yhat) < lo + 0.5)
        centres.append(lo + 0.25)
        halfw.append(np.quantile(np.abs(res[m]), 0.90))
        nobs.append(int(m.sum()))
    centres, halfw = np.array(centres), np.array(halfw)
    X = np.column_stack([np.ones(len(centres)), centres ** 2])
    coef, *_ = np.linalg.lstsq(X, halfw, rcond=None)
    lab = ("$" + it(coef[0], 3).replace(",", "{,}") + " + "
           + it(coef[1], 3).replace(",", "{,}") + r"\,\hat y^{2}$")

    fig, axes = plt.subplots(1, 2, figsize=(6.7, 3.05))
    ax = axes[0]
    ax.scatter(yhat, res, s=16, facecolors="none", edgecolors=es.TEAL, lw=0.7)
    ax.axhline(0, color=es.GRAY, lw=0.8, ls=":")
    xx = np.linspace(-5.6, 4.8, 300)
    env = coef[0] + coef[1] * xx ** 2
    ax.fill_between(xx, -env, env, color=es.REDBG, alpha=0.6, zorder=0,
                    label="banda al 90%:  " + lab)
    ax.plot(xx, env, color=es.RED, lw=1.0, zorder=1)
    ax.plot(xx, -env, color=es.RED, lw=1.0, zorder=1)
    ax.set_title("A. La nube a clessidra della Figura 4", loc="left")
    ax.set_xlabel("valori predetti")
    ax.set_ylabel("residui")
    ax.set_ylim(-3.3, 6.9)
    ax.legend(loc="upper right", fontsize=7.2, framealpha=1.0)
    es.commas(ax, "both", decimals=0)

    ax = axes[1]
    ax.bar(centres, halfw, width=0.42, color=es.BLUE, alpha=0.8,
           label="semi-ampiezza al 90% (Figura 4)")
    gg = np.linspace(0, 4.5, 200)
    ax.plot(gg, coef[0] + coef[1] * gg ** 2, color=es.RED, lw=1.4, label=lab)
    ax.set_title(r"B. La dispersione cresce come $\hat y^{2}$", loc="left")
    ax.set_xlabel(r"$|\hat y|$")
    ax.set_ylabel("semi-ampiezza dei residui")
    ax.set_ylim(0, 3.35)
    ax.legend(loc="upper left", fontsize=7.0, framealpha=1.0)
    es.commas(ax, "both", decimals=1)

    fig.tight_layout()
    es.save(fig, OUT / "d08-residui-eteroschedasticita.pdf")
    return list(zip(np.round(centres, 2), np.round(halfw, 3), nobs)), coef


# =====================================================================
#  D9 — variabile omessa
# =====================================================================
def d09():
    keys = ["grant", "hrsemp", "h_grant"]
    titoli = {"grant": "grant", "hrsemp": "hrsemp", "h_grant": "h_grant"}
    delta = {k: (B[k] - BL[k]) / BL["l_sales"] for k in keys}

    fig, axes = plt.subplots(1, 4, figsize=(7.0, 3.0))
    for ax, k in zip(axes[:3], keys):
        for i, (bb, ss, col, lab) in enumerate(
                [(B[k], SE[k], es.AMBER, "modello (6)"),
                 (BL[k], SEL[k], es.BLUE, "modello (9)")]):
            ax.errorbar([i], [bb], yerr=[1.96 * ss], fmt="o", ms=6, color=col,
                        capsize=5, lw=1.4, label=lab)
            ax.annotate(it(bb, 5), xy=(i, bb), xytext=(8, 0),
                        textcoords="offset points", fontsize=7.4, color=col,
                        va="center")
        ax.axhline(0, color=es.GRAY, lw=0.8, ls=":")
        ax.annotate("", xy=(1, BL[k]), xytext=(0, B[k]),
                    arrowprops=dict(arrowstyle="->", color=es.RED, lw=1.1, ls="--"))
        ax.set_xlim(-0.6, 1.9)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["(6)", "(9)"])
        ax.set_title(titoli[k], loc="left")
        es.commas(ax, "y")
    axes[0].set_ylabel("stima e intervallo al 95%")
    axes[0].legend(loc="upper left", fontsize=7.0)

    ax = axes[3]
    vals = [delta[k] for k in keys]
    cols = [es.RED if v > 0 else es.BLUE for v in vals]
    ax.bar(range(3), vals, color=cols, width=0.6)
    ax.axhline(0, color=es.GRAY, lw=0.9)
    for i, v in enumerate(vals):
        ax.annotate(it(v, 3), xy=(i, v), xytext=(0, 5 if v > 0 else -13),
                    textcoords="offset points", ha="center", fontsize=7.4,
                    color=cols[i], fontweight="bold")
    ax.set_xticks(range(3))
    ax.set_xticklabels([titoli[k] for k in keys], fontsize=7.4, rotation=20)
    ax.set_title(r"$\hat\delta_j$ implicito", loc="left")
    ax.set_ylabel(r"coefficiente di $X_j$ in $\log(\mathrm{sales})$")
    es.commas(ax, "y", decimals=1)

    fig.suptitle("Confronto fra le due specificazioni e distorsione implicata dall'omissione di "
                 r"$\log(\mathrm{sales})$",
                 x=0.01, ha="left", color=es.BLUE, fontweight="bold", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    es.save(fig, OUT / "d09-variabile-omessa.pdf")
    return delta


# =====================================================================
#  D10 — quadratica in hrsemp
# =====================================================================
def d10():
    b2, b3 = Q["hrsemp"], Q["sq_hrsemp"]
    s3 = QSE["sq_hrsemp"]
    tstat = b3 / s3
    tcrit = stats.t.ppf(0.975, DF2)
    turn = turn_point(b2, b3)

    fig, axes = plt.subplots(1, 2, figsize=(6.8, 3.0))
    _, ax, _ = es.quadratic_effect(b2, b3, xmax=12, xmin=0, ax=axes[0],
                                   varname="hrsemp",
                                   ylabel="effetto marginale su scrap",
                                   title="A. Effetto marginale crescente")
    ax.legend(loc="lower right", fontsize=7.0)
    ax.set_xlabel("hrsemp (ore di formazione per addetto)")
    es.commas(ax, "x", decimals=0)
    es.commas(ax, "y", decimals=3)
    ax.annotate("effetto negativo sotto " + it(turn, 2) + " ore,\npositivo sopra",
                xy=(0.04, 0.80), xycoords="axes fraction", fontsize=7.6,
                color=es.RED, va="top")

    es.dist_test("t", DF2, stat=tstat, crit=tcrit, tail="two", ax=axes[1],
                 pvalue=0.2086,
                 title=r"B. $H_0:\beta_3=0$ contro $H_1:\beta_3\neq0$")
    axes[1].legend(loc="upper left", fontsize=6.9)

    fig.tight_layout()
    es.save(fig, OUT / "d10-quadratica.pdf")
    return turn, tstat, tcrit


def turn_point(b1, b2):
    return -b1 / (2 * b2)


# =====================================================================
if __name__ == "__main__":
    print("figure dell'appello 2023-01-17")
    crit = d01()
    print("   critici DF simulati:", {k: round(v, 3) for k, v in crit.items()})
    q05, psim = d02()
    print(f"   Engle-Granger: critico 5% {q05:.3f}, p-value simulato {psim:.4f}")
    print("   banda correlogramma:", round(d03(), 5))
    print("   orizzonti di assorbimento:", d04())
    phi1, phi2, acf_th = d05()
    print(f"   AR(2) identificato: phi1={phi1:.4f} phi2={phi2:.4f}; "
          f"ACF teorica ai ritardi 1-4: {np.round(acf_th[:4], 4)}")
    tot, bound, tmin = d06()
    print(f"   b2+b3 = {tot:.8f}; se <= {bound:.8f}; t minimo = {tmin:.4f}")
    theta, bt, pct = d07()
    print(f"   theta = {theta:.8f} -> {pct:.3f}% esatto; se <= {bt:.6f}")
    bins, coef = d08()
    print("   semi-ampiezza al 90% per bin di |yhat|:", bins)
    print("   fit  %.4f + %.4f * yhat^2" % (coef[0], coef[1]))
    print("   delta impliciti:", {k: round(v, 4) for k, v in d09().items()})
    tp, ts, tc = d10()
    print(f"   punto di svolta {tp:.4f}; t = {ts:.4f}; critico {tc:.4f}")
