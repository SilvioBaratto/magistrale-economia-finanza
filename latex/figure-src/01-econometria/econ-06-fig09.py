import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig09.png")
T = 200
DATA = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig09.csv")
_d = np.genfromtxt(DATA, delimiter=",", names=True)
ACF, PACF = _d["acf"], _d["pacf"]
band = 1.96 / np.sqrt(T)
lags = _d["lag"]

fig, axes = style.figure(2, 1, figsize=(style.WIDTH_IN, 3.0))
for ax, vals, title in zip(axes, (ACF, PACF),
                           ("ACF di norm", "PACF di norm")):
    ax.bar(lags, vals, width=0.2, color=style.GP_RED, zorder=3)
    ax.axhline(0, color=style.DARK, lw=0.8, ls=":", zorder=2)
    ax.axhline(band, color=style.GP_GREEN, lw=0.9, ls="--", label="+- 1.96/T^0.5")
    ax.axhline(-band, color=style.GP_GREEN, lw=0.9, ls="--")
    for sp in ax.spines.values():
        sp.set_visible(True)
    ax.set_xlim(0, 15)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xticks(range(0, 15, 2))
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticklabels(["-1", "-0.5", "0", "0.5", "1"])
    ax.set_xlabel("Ritardo")
    ax.set_title(title)
    ax.legend(loc="upper right", frameon=False, markerfirst=False)
fig.tight_layout()
style.save(fig, OUT)
