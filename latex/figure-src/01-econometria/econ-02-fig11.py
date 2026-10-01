import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import pandas as pd
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig11.png")
TAN = "#CFC48A"


DATA = pd.read_csv(str(style.REPO / "latex/figure-src/01-econometria/data/econ-02-fig11.csv"))


def panel(ax, name, n, ymax, yticks):
    d = DATA[DATA.panel == name]
    bars = d[d.kind == "bar"]
    ax.bar(bars.x, bars.y, width=bars.x_right - bars.x, align="edge",
           color=TAN, edgecolor="none")
    curve = d[d.kind == "curve"]
    ax.plot(curve.x, curve.y, color="red", lw=1.2)
    ax.set_xlim(-4.4, 4.4)
    ax.set_ylim(0, ymax)
    ax.set_xticks([-4, -2, 0, 2, 4])
    ax.set_yticks(yticks)
    ax.set_yticklabels([("0" if t == 0 else f"{t:.1f}".lstrip("0")) for t in yticks])
    ax.set_xlabel(f"Sample size n={n}")
    ax.set_ylabel("Density")
    ax.grid(axis="y", color="#E3E3E3", lw=0.6)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


fig, axs = style.figure(1, 2, figsize=(style.WIDTH_IN, 2.1))
panel(axs[0], "left", 2, 0.62, [0, .2, .4, .6])
panel(axs[1], "right", 50, 0.52, [0, .1, .2, .3, .4, .5])
fig.set_layout_engine("tight")
style.save(fig, OUT)
