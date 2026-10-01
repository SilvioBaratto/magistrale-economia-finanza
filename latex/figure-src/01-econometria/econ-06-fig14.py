"""ACF and PACF of Roll-model returns (MA(1), T = 12316), values read from the slide."""
import sys

import numpy as np

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

CSV = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig14.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig14.png")

T, NLAG = 12316, 40
data = np.genfromtxt(CSV, delimiter=",", names=True)
vals = {"ACF": data["acf"], "PACF": data["pacf"]}
# The slide strokes bars with square caps (half stroke width = 0.625 path units, 30.598 units
# per 0.4 of data), so every bar overshoots both ends by this much and zero bars stay visible.
CAP = 0.625 * 0.4 / 30.598
band = 1.96 / np.sqrt(T)
lags = np.arange(1, NLAG + 1)

fig, axes = style.figure(2, 1, figsize=(9.6, 3.4), sharex=False)
for ax, (name, v) in zip(axes, vals.items()):
    lo = np.minimum(v, 0) - CAP
    hi = np.maximum(v, 0) + CAP
    ax.bar(lags, hi - lo, bottom=lo, width=0.22, color=style.GP_RED, zorder=3)
    for s in (band, -band):
        ax.axhline(s, color=style.GP_BLUE, lw=0.8, zorder=2)
    ax.axhline(0, color=style.GP_BLUE, lw=0.6, ls=":", zorder=1)
    ax.set_xlim(0, 41)
    ax.set_ylim(-0.58, 0.58)
    ax.set_xticks(range(0, 41, 5))
    ax.set_yticks([-0.4, -0.2, 0, 0.2, 0.4])
    ax.set_yticklabels(["-0.4", "-0.2", "0", "0.2", "0.4"])
    ax.set_title(f"{name} di rendimenti", fontsize=10)
    ax.set_xlabel("Ritardo", labelpad=1)
    ax.tick_params(labelsize=8)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(True)
    ax.plot([], [], color=style.GP_BLUE, lw=0.8, label=r"+- 1.96/T^0.5")
    ax.legend(loc="upper right", handlelength=2.2, markerfirst=False, borderaxespad=0.3, fontsize=8)
style.save(fig, OUT)
