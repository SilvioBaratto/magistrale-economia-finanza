"""MA(2) series, data recovered from the slide vector drawing (x in months since 1 Feb)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
import numpy as np

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig11.png")
data = np.loadtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig11.csv"), delimiter=",", skiprows=1)
x, y = data[:, 0], data[:, 1]

fig, ax = style.figure(height_ratio=0.5)
ax.axhline(0, color=style.GREY, lw=0.6, ls=(0, (1, 3)))
ax.plot(x, y, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.set_ylim(-4, 4)
ax.set_yticks(range(-4, 5))
ax.set_xlim(-1.094, 8.41)
months = ["Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott"]
ax.set_xticks(range(9))
ax.set_xticklabels(months)
ax.set_ylabel("ma2")
for s in ("top", "right"):
    ax.spines[s].set_visible(True)
ax.tick_params(axis="x", length=0)
style.save(fig, OUT)
