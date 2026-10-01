import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig20.png")
DATA = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig20.csv")

t, rw = np.loadtxt(DATA, delimiter=",", skiprows=1, unpack=True)

fig, ax = style.figure(figsize=(5.4, 2.7))
ax.axhline(0, color=style.DARK, lw=0.7, ls=":")
ax.plot(t, rw, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.set_xlim(-5, 255)
ax.set_ylim(-14, 6)
ax.set_xticks(range(0, 251, 50))
ax.set_yticks(range(-14, 7, 2))
ax.set_ylabel("rw")
style.save(fig, OUT)
