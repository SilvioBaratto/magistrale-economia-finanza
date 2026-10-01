import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig21.png")

DATA = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig21.csv")
t, RW = np.loadtxt(DATA, delimiter=",", skiprows=1, unpack=True)
fig, ax = style.figure(height_ratio=0.5)
ax.axhline(0, color=style.DARK, lw=0.8, ls=(0, (1, 2)), zorder=1)
ax.plot(t, RW, color=style.GP_RED, linewidth=style.GP_LINEWIDTH, zorder=3)
ax.set_xlim(-5.4, 256)
ax.set_ylim(-8, 10)
ax.set_xticks(range(0, 251, 50))
ax.set_yticks(range(-8, 11, 2))
ax.set_ylabel("rw")
for s in ("top", "right"):
    ax.spines[s].set_visible(True)
style.save(fig, OUT)
