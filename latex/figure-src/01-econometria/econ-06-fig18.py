"""ACF and PACF of the AR(3) series ar3 (T = 250), values extracted from the slide vector drawing."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig18.png")
T, NLAG = 250, 36
D = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig18.csv"),
                  delimiter=",", names=True)
a, p = D["acf"], D["pacf"]
lags = D["lag"]
band = 1.96 / np.sqrt(T)

fig, axes = style.figure(2, 1, figsize=(style.WIDTH_IN, style.WIDTH_IN / 1.5))
fig.get_layout_engine().set(h_pad=0.08, hspace=0.10)
for ax, v, name in ((axes[0], a, "ACF di ar3"), (axes[1], p, "PACF di ar3")):
    ax.bar(lags, v, width=0.15, color=style.GP_RED, zorder=3)
    ax.axhline(0, color="black", lw=0.6, ls=":", zorder=2)
    for s in (band, -band):
        ax.axhline(s, color=style.GP_GREEN, lw=0.8, ls=(0, (6, 3)), zorder=1)
    ax.plot([], [], color=style.GP_GREEN, lw=0.8, ls=(0, (6, 3)), label="+- 1.96/T^0.5")
    ax.set_xlim(0, 37)
    ax.set_ylim(-1.05, 1.05)
    ax.set_xticks(range(0, 36, 5))
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticklabels(["-1", "-0.5", "0", "0.5", "1"])
    ax.set_title(name)
    ax.set_xlabel("Ritardo", labelpad=1)
    ax.legend(loc="upper right", borderaxespad=0.3, handlelength=3, markerfirst=False, frameon=False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(True)
style.save(fig, OUT)
