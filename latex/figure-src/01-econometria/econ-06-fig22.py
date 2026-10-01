"""ACF and PACF correlogram of the random walk, values recovered from the slide drawing."""
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style
import pandas as pd

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig22.png")
CSV = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig22.csv")
T = 250

df = pd.read_csv(CSV)
band = 1.96 / np.sqrt(T)
lags = df["lag"].to_numpy()

fig, axes = style.figure(2, 1, height_ratio=0.49)
for ax, vals, name in ((axes[0], df["acf"].to_numpy(), "ACF"),
                       (axes[1], df["pacf"].to_numpy(), "PACF")):
    ax.bar(lags, vals, width=0.12, color=style.GP_RED, zorder=3)
    bc = style.GP_GREEN
    ax.axhline(0, color=style.DARK, lw=0.8, ls=":")
    ax.axhline(band, color=bc, lw=0.9, ls="--", label="+- 1.96/T^0.5")
    ax.axhline(-band, color=bc, lw=0.9, ls="--")
    ax.set_xlim(0, 17)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xticks(range(0, 17, 2))
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticklabels(["-1", "-0.5", "0", "0.5", "1"])
    ax.set_xlabel("Ritardo")
    ax.set_title(f"{name} di rw")
    ax.legend(loc="upper right", markerfirst=False,
              fontsize=8, borderaxespad=0.15, borderpad=0.2)
    for side in ax.spines.values():
        side.set_visible(True)
style.save(fig, OUT)
