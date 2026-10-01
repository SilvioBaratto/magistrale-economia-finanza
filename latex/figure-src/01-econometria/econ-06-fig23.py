"""Random walk with drift Y_t = 0.5 + Y_{t-1} + eps_t, T = 250 (original data recovered from the slide vector drawing)."""
import sys

import numpy as np

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig23.png")

data = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig23.csv"), delimiter=",", names=True)
x, y = data["x"], data["rw"]

fig, ax = style.figure(height_ratio=0.5)
ax.axhline(0, color=style.DARK, lw=0.8, ls=":")
ax.plot(x, y, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.set_xlim(-5, 255)
ax.set_ylim(-20, 140)
ax.set_xticks(range(0, 251, 50))
ax.set_yticks(range(-20, 141, 20))
ax.set_ylabel("rw", rotation=90)
style.save(fig, OUT)
