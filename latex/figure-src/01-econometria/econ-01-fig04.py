"""ECON 01, figure 4: monthly returns of a portfolio and of the market, 1961-2006.

The plotted vertices are read from the vector drawing of the original slide
(data/econ-01-fig04.csv), in months since 1960m1.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-01/fig04.png")
NAVY = "#1F4E79"
MAROON = "#8E2F3A"
CSV = str(style.REPO / "latex/figure-src/01-econometria/data/econ-01-fig04.csv")

data = np.genfromtxt(CSV, delimiter=",", names=True, dtype=None, encoding="utf-8")
port = data[data["series"] == "port"]
mkt = data[data["series"] == "mkt"]

fig, ax = style.figure(height_ratio=0.60)
ax.plot(port["month"], port["value"], color=NAVY, lw=0.9, label="Portfolio")
ax.plot(mkt["month"], mkt["value"], color=MAROON, lw=0.9, label="Market")
ax.set_ylim(-40, 40)
ax.set_xlim(-10, 549)
ax.set_yticks([-40, -20, 0, 20, 40])
ax.set_xticks(range(0, 481, 120))
ax.set_xticklabels([f"{y}m1" for y in range(1960, 2001, 10)])
ax.set_xticks([60, 180, 300, 420, 540], minor=True)
ax.tick_params(axis="x", which="minor", length=2, labelbottom=False)
ax.grid(axis="y", color="#E3E3E3", lw=0.6)
ax.set_axisbelow(True)
ax.set_xlabel("time")
ax.set_ylabel("Returns")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=True,
          edgecolor=style.DARK, fancybox=False, handlelength=3)
style.save(fig, OUT)
