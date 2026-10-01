import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig10.png")

data = np.loadtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig10.csv"), delimiter=",", skiprows=1)
x, y = data[:, 0], data[:, 1]

fig, ax = style.figure(figsize=(5.4, 3.1))
for s in ax.spines.values():
    s.set_visible(True)
    s.set_linewidth(0.6)
ax.axhline(0, color=style.DARK, lw=0.6, ls=(0, (1, 3)))
ax.plot(x, y, color=style.GP_RED, lw=style.GP_LINEWIDTH)
ax.set_xlim(-1.13, 8.43)
ax.set_ylim(-3, 3)
ax.set_yticks(range(-3, 4))
ax.set_yticklabels([str(t).replace("-", "−") for t in range(-3, 4)])
ax.set_xticks(range(9))
ax.set_xticklabels(["Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott"])
ax.set_ylabel("y")
ax.grid(False)
style.save(fig, OUT)
