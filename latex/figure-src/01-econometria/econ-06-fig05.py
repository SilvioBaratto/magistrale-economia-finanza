"""ECON 06 fig. 5: ACF and PACF correlogram of the series ar3."""
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style
from matplotlib.lines import Line2D

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig05.png")
T = 250

data = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig05.csv"),
                     delimiter=",", names=True)
vals = {"ACF": data["acf"], "PACF": data["pacf"]}
band = 1.96 / np.sqrt(T)
lags = data["lag"]

fig, axes = style.figure(2, 1, figsize=(6.0, 3.0), constrained_layout=False)
for ax, (name, v) in zip(axes, vals.items()):
    ax.bar(lags, v, width=0.09, color=style.GP_RED, zorder=3)
    ax.axhline(0, color="black", lw=0.8, ls=":", zorder=2)
    band_color = style.GP_GREEN
    for s in (1, -1):
        ax.axhline(s * band, color=band_color, lw=0.8, ls=(0, (4, 2)), zorder=1)
    ax.set_xlim(0, 15)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xticks(range(0, 15, 2))
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticklabels(["-1", "-0.5", "0", "0.5", "1"])
    ax.set_title(f"{name} di ar3", fontsize=9.5)
    ax.set_xlabel("Ritardo")
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    ax.legend([Line2D([], [], color=style.GP_GREEN, lw=0.8, ls=(0, (4, 2)))], ["+- 1.96/T^0.5"],
              loc="upper right", markerfirst=False, handlelength=3, fontsize=8.5, bbox_to_anchor=(1, 1.0))
fig.subplots_adjust(hspace=0.85, left=0.08, right=0.98, top=0.91, bottom=0.13)
style.save(fig, OUT)
