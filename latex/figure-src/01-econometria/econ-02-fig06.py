import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig06.png")

# Points read off the slide (per-x clusters); the fitted line is the slide's OLS line.
pts = {
    1: [5.7, 5.4, 5.2, 4.3, 3.9],
    2: [8.6, 7.45, 7.25, 7.0, 6.8, 6.5, 6.25, 5.9, 5.6, 5.3, 5.05, 4.5, 4.2, 3.8],
    3: [9.45, 9.0, 8.6, 8.2, 7.9, 7.6, 7.35, 7.1, 6.8, 6.6, 6.2, 5.85, 5.5],
    4: [11.75, 11.35, 10.4, 10.0, 9.8, 9.5, 9.2, 8.9, 8.4, 8.1, 7.8, 7.5, 6.8, 6.3],
    5: [12.2, 11.9, 11.6, 11.3, 11.0, 10.75, 10.5, 10.3, 10.1, 9.85, 9.6, 9.0, 8.65],
    6: [14.2, 13.4, 13.1, 12.8, 12.2, 12.0, 11.7, 11.5, 10.95, 10.6, 9.7],
    7: [14.9, 14.65, 13.4, 13.1, 12.8, 12.55, 12.1, 11.9],
    8: [14.2, 14.7, 15.0],
    9: [15.1, 18.1],
    11: [19.8],
}
x = np.concatenate([[k] * len(v) for k, v in pts.items()]).astype(float)
y = np.concatenate([v for v in pts.values()])
b, a = 1.48, 3.02

fig, ax = style.figure(figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.43))
ax.scatter(x, y, s=22, color=style.BLUE, zorder=3, linewidths=0)
xs = np.array([1.0, 11.0])
ax.plot(xs, a + b * xs, color=style.RED, lw=1.3, zorder=4, label="Regression Line")
ax.set_xlim(-0.2, 11.7)
ax.set_ylim(3.2, 20.5)
ax.set_xticks([0, 5, 10])
ax.set_yticks([5, 10, 15, 20])
ax.set_xlabel("x", labelpad=-2)
ax.tick_params(axis="both", length=3)
ax.grid(axis="y", color=style.LIGHT, lw=0.5)
ax.set_axisbelow(True)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.24), frameon=True, edgecolor=style.DARK, fancybox=False)
style.save(fig, OUT)
