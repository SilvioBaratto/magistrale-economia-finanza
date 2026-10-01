"""ACF and PACF of an AR(1) series (T = 200), gretl ar11 correlogram; bar heights extracted from the slide vector drawing."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig16.png")
T = 200
DATA = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig16.csv"),
                     delimiter=",", names=True)
a = DATA["acf"]
p = DATA["pacf"]
lags = DATA["lag"]
band = 1.96 / np.sqrt(T)

fig, axes = style.figure(2, 1, figsize=(style.WIDTH_IN, 3.0))
for ax, vals, title, up, lo in ((axes[0], a, "ACF di ar11", style.GP_GREEN, style.GP_GREEN),
                                (axes[1], p, "PACF di ar11", style.GP_GREEN, style.GP_GREEN)):
    ax.bar(lags, vals, width=0.1, color=style.GP_RED, zorder=3)
    ax.axhline(0, color="black", lw=0.9, ls=":", zorder=2)
    ax.axhline(band, color=up, lw=0.9, ls=(0, (4, 2)))
    ax.axhline(-band, color=lo, lw=0.9, ls=(0, (4, 2)))
    ax.set_xlim(0, 14.8)
    ax.set_ylim(-1.1, 1.1)
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticklabels(["-1", "-0.5", "0", "0.5", "1"])
    ax.set_xticks(range(0, 15, 2))
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("Ritardo", labelpad=1)
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    ax.plot([], [], color=up, lw=0.9, ls=(0, (4, 2)), label="+- 1.96/T^0.5")
    ax.legend(loc="upper right", frameon=False, fontsize=8.5, handlelength=3, markerfirst=False)
style.save(fig, OUT)
