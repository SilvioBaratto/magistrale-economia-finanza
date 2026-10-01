"""ECON 02 figure 7: scatter with heteroskedastic errors around a regression line.

Points are the marker centres recovered from the slide's vector drawing
(data/econ-02-fig07.csv); the line is the one drawn there.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig07.png")
NAVY = "#1F4E79"
LINE = "#9C2F36"

data = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-02-fig07.csv"),
                     delimiter=",", names=True)
x, y = data["x"], data["y"]

fig, ax = style.figure(height_ratio=0.48)
ax.set_axisbelow(True)
ax.grid(axis="y", color="#E6ECEF", lw=0.6)
ax.scatter(x, y, s=22, color=NAVY, linewidths=0, zorder=3)
ax.plot([1, 11], [4.4, 19.5], color=LINE, lw=1.1, label="Regression Line", zorder=2)
ax.set_xlim(-0.1, 11.3)
ax.set_ylim(-0.7, 20.7)
ax.set_xticks([0, 5, 10])
ax.set_yticks([0, 5, 10, 15, 20])
ax.set_xlabel("X")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.27), frameon=True,
          edgecolor=style.DARK, fancybox=False, handlelength=4, borderpad=0.5)
style.save(fig, OUT)
