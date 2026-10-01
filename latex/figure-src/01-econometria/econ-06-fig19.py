"""Deterministic quadratic trend Y_t = a0 + a1 t + a2 t^2 + eps_t (T = 250)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig19.png")

data = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig19.csv"), delimiter=",", names=True)
t = data["t"]
y = data["trend_det"]

fig, ax = style.figure(height_ratio=0.5)
ax.axhline(0, color=style.DARK, lw=0.7, ls=":")
ax.plot(t, y, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.set_xlim(-5, 255)
ax.set_ylim(-20, 140)
ax.set_xticks(range(0, 251, 50))
ax.set_yticks(range(-20, 141, 20))
ax.set_ylabel("trend_det")
for s in ("top", "right"):
    ax.spines[s].set_visible(True)
style.save(fig, OUT)
