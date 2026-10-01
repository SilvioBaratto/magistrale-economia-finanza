"""AR(3) series, T = 250, plotted from the vertices recovered from the slide drawing."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig17.png")
DATA = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig17.csv")

d = np.genfromtxt(DATA, delimiter=",", names=True)

fig, ax = style.figure(figsize=(style.WIDTH_IN, style.WIDTH_IN*0.49))
ax.axhline(0, color=style.DARK, lw=0.7, ls=":", zorder=1)
ax.plot(d["t"], d["ar3"], color=style.GP_RED, linewidth=style.GP_LINEWIDTH, zorder=2)
ax.set_xlim(-6, 255)
ax.set_ylim(-3, 4)
ax.set_xticks(range(0, 251, 50))
ax.set_yticks(range(-3, 5))
ax.set_ylabel("ar3")
for s in ("top", "right"):
    ax.spines[s].set_visible(True)
ax.tick_params(top=False, right=False)
style.save(fig, OUT)
