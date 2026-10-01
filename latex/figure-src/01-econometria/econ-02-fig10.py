import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig10.png")

# Sampling distributions of beta-hat for n = 2, 10, 50, 100 (centre ~3.05).
# Histograms are laid out bin by bin so each bar matches the original.
BLUE, GREEN, RED, TAN = "#1B4469", "#0A7D0A", "#FF0000", "#CBC285"
TAN_EDGE = "#CBC285"

def bars(ax, lefts, heights, width, color, z, edge=TAN_EDGE, lw=0.8):
    ax.bar(lefts, heights, width=width, align="edge", color=color,
           edgecolor=edge, linewidth=lw, zorder=z)

fig, ax = style.figure(figsize=(7.0, 3.3))

DATA = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-02-fig10.csv"),
                     delimiter=",", names=True, dtype=None, encoding="utf-8")
for name, color, z in (("n2", BLUE, 2), ("n10", GREEN, 3), ("n50", RED, 4), ("n100", TAN, 5)):
    d = DATA[DATA["series"] == name]
    if name == "n50":
        d = d[d["height"] > 0]
    # The slide strokes every bar with a tan outline; on n=50's narrow bars it
    # covers most of the fill and leaves only red slivers.
    bars(ax, d["x0"], d["height"], d["x1"] - d["x0"], color, z,
         lw=1.3 if name == "n50" else 0.5)

ax.set_xlim(2, 4)
ax.set_ylim(-0.5, 21)
ax.set_xticks([2, 2.5, 3, 3.5, 4])
ax.set_xticklabels(["2", "2.5", "3", "3.5", "4"])
ax.set_yticks([0, 5, 10, 15, 20])
ax.set_ylabel("Histograms")
ax.grid(axis="y", color=style.LIGHT, linewidth=0.6)
ax.set_axisbelow(True)

ORANGE = "#FF4500"
ann = [("Sample size n=2", (2.30, 2.8), (2.48, 2.2), (2.62, 1.0)),
       ("Sample size n=10", (2.70, 4.9), (2.83, 4.5), (2.95, 2.9)),
       ("Sample size n=50", (3.52, 7.65), (3.33, 6.7), (3.11, 4.1)),
       ("Sample size n=100", (3.42, 19.2), (3.17, 18.5), (3.09, 17.4))]
for t, (tx, ty), (x0, y0), (x1, y1) in ann:
    ax.text(tx, ty, t, ha="center", va="center", fontsize=9, zorder=10)
    ax.plot([x0, x1], [y0, y1], color=ORANGE, lw=1.0, zorder=10,
            solid_capstyle="butt")

lab = {2: BLUE, 10: GREEN, 50: RED, 100: TAN}
h = {n: Patch(fc=c, ec=TAN_EDGE, label=f"n={n}") for n, c in lab.items()}
# ncol=2 fills column by column; reorder so rows read n=2,n=10 / n=50,n=100
ax.legend(handles=[h[2], h[50], h[10], h[100]], ncol=2, loc="upper center",
          bbox_to_anchor=(0.5, -0.12), frameon=True, edgecolor=style.DARK,
          fancybox=False, handlelength=3.5)
style.save(fig, OUT)
