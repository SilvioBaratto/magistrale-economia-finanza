import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig08.png")

data = np.genfromtxt(
    str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig08.csv"),
    delimiter=",",
    names=True,
)
x = np.round(data["x"])
y = data["y"]

fig, ax = style.figure(height_ratio=0.5)
ax.plot(x, y, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.axhline(0, color=style.DARK, lw=0.8, ls=":")
for s in ("top", "right"):
    ax.spines[s].set_visible(True)
ax.set_xlim(-5, 205)
ax.set_ylim(-4, 4)
ax.set_xticks([0, 50, 100, 150, 200])
ax.set_yticks(range(-4, 5))
ax.set_ylabel("norm")
style.save(fig, OUT)
