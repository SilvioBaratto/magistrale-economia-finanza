"""econ-06 fig15: ar11 series (t=4..200), data recovered from the slide vector drawing."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig15.png")

data = np.loadtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig15.csv"), delimiter=",", skiprows=1)
t, y = data[:, 0], data[:, 1]

fig, ax = style.figure(height_ratio=0.5)
ax.axhline(0, color=style.GREY, lw=0.8, ls=":")
ax.plot(t, y, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.set_xlim(-5, 205)
ax.set_ylim(-5, 5)
ax.set_xticks([0, 50, 100, 150, 200])
ax.set_yticks(range(-5, 6))
ax.set_ylabel("ar11")
ax.spines["top"].set_visible(True)
ax.spines["right"].set_visible(True)
style.save(fig, OUT)
print(y.min(), y.max(), y.std())
