import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig12.png")

T, NLAGS = 200, 23
data = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig12.csv"),
                     delimiter=",", names=True)
a, p = data["acf"], data["pacf"]
lags = np.arange(1, NLAGS + 1)
band = 1.96 / np.sqrt(T)

fig, axes = style.figure(2, 1, figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.46),
                         constrained_layout=False)
fig.subplots_adjust(hspace=0.95, left=0.1, right=0.98, top=0.92, bottom=0.12)
for ax, vals, title in ((axes[0], a, "ACF di ma2"), (axes[1], p, "PACF di ma2")):
    ax.bar(lags, vals, width=0.12, color=style.GP_RED, zorder=3)
    ax.axhline(0, color=style.DARK, lw=0.6, ls=(0, (1, 4)), zorder=1)
    for s in (band, -band):
        ax.axhline(s, color=style.GP_BLUE, lw=0.7, zorder=2)
    ax.plot([], [], color=style.GP_BLUE, lw=0.7, label="+- 1.96/T^0.5")
    ax.legend(loc="upper right", fontsize=8, handlelength=3, markerfirst=False)
    ax.set_xlim(0, 23.5)
    ax.set_ylim(-1, 1)
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticklabels(["-1", "-0.5", "0", "0.5", "1"])
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.tick_params(top=True, direction="in", labelsize=8)
    for sp in ax.spines.values():
        sp.set_visible(True)
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("Ritardo", fontsize=9)
style.save(fig, OUT)
