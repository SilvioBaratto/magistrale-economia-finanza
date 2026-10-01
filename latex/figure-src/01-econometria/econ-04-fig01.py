import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy import stats
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-04/fig01.png")
import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)

d1, d2 = 3, 60
crit = stats.f.ppf(0.95, d1, d2)  # 2.76
xmax = 3.8
xlim = 3.9
# The slide's curve is a schematic F density with a heavier tail than F(3,60);
# F(4,6) matches its peak position and its tail heights at 2.76 and at the right end.
# The slide's curve meets the y-axis at about 20% of its peak, so a sharp
# term is added to the F density to reproduce that steep start.
_peak = stats.f.pdf(np.linspace(1e-3, 4, 4000), 4, 6).max()
def pdf(t):
    return stats.f.pdf(t, 4, 6) + 0.20 * _peak * np.exp(-np.asarray(t) / 0.05)
x = np.linspace(0, xmax, 1600)
y = pdf(x)
ymax = y.max()

fig, ax = style.figure(figsize=(5.4, 4.9))
ax.plot(x, y, color=style.DARK, lw=1.4, zorder=3)

xs = np.linspace(crit, xmax, 200)
ax.fill_between(xs, 0, pdf(xs), facecolor="none",
                edgecolor=style.DARK, hatch="\\\\\\", lw=0, zorder=2)
ax.plot([crit, crit], [0, pdf(crit)], color=style.DARK, lw=1.4, zorder=3)

ax.set_xlim(0, xlim)
ax.set_ylim(0, ymax * 1.02)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_linewidth(1.2)
ax.spines["bottom"].set_linewidth(1.2)
ax.spines["bottom"].set_position(("data", 0))
ax.grid(False)
ax.set_yticks([])
ax.set_xticks([])

# area labels with leader lines
ax.annotate("area = .95", xy=(0.70, ymax * 0.70), xytext=(1.27, ymax * 0.91),
            ha="center", va="center", fontsize=9,
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.9, shrinkA=6, shrinkB=0))
ax.annotate("area = .05", xy=(3.15, pdf(3.15)), xytext=(3.5, ymax * 0.24),
            ha="center", va="center", fontsize=9,
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.9, shrinkA=6, shrinkB=0))

# rejection region arrow below the axis
yb = -ymax * 0.08
ax.annotate("", xy=(xmax + 0.1, yb), xytext=(crit, yb), annotation_clip=False,
            arrowprops=dict(arrowstyle="->", color=style.DARK, lw=1.2))
ax.plot([crit, crit], [0, yb * 1.0], color=style.DARK, lw=1.4, clip_on=False)
ax.text((crit + xmax) / 2 + 0.1, yb * 1.35, "rejection\nregion", ha="center", va="top", fontsize=9)
ax.text(crit, yb * 1.35, "2.76", ha="center", va="top", fontsize=9)
ax.text(0, yb * 1.35, "0", ha="center", va="top", fontsize=9)

ax.text(0, ymax * 1.02 + ymax * 0.02, r"The 5% critical value and rejection region in an $F_{3,60}$ distribution.",
        ha="left", va="bottom", fontsize=9)
style.save(fig, OUT)
