"""econ-05 fig03: squared fitted values of price ~ sqrft + lotsize + bdrms (hprice1,
n = 88) against each regressor. The slide plots these values under the axis label
"Squared residuals", so the label is kept as in the original.

Data: Wooldridge hprice1 (the course's hprices.gdt); the three regressors are embedded.
The coefficients are the note's OLS table (price in thousands of dollars).
"""
import sys

import numpy as np
from matplotlib.ticker import FixedLocator

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-05/fig03.png")

ROWS = [(4, 6126, 2438), (3, 9903, 2076), (3, 5200, 1374), (3, 4600, 1448), (4, 6095, 2514), (5, 8566, 2754), (3, 9000, 2067), (3, 6210, 1731), (3, 6000, 1767), (3, 2892, 1890), (4, 6000, 2336), (5, 7047, 2634), (3, 12237, 3375), (3, 6460, 1899), (3, 6519, 2312), (4, 3597, 1760), (4, 5922, 2000), (3, 7123, 1774), (3, 5642, 1376), (4, 8602, 1835), (3, 5494, 2048), (3, 7800, 2124), (3, 6003, 1768), (4, 5218, 1732), (3, 9425, 1440), (3, 6114, 1932), (3, 6710, 1932), (3, 8577, 2106), (7, 8400, 3529), (4, 9773, 2051), (4, 4806, 1573), (4, 15086, 2829), (3, 5763, 1630), (4, 6383, 1840), (4, 9000, 2066), (4, 3500, 1702), (4, 10892, 2750), (5, 15634, 3880), (4, 6400, 1854), (2, 8880, 1421), (3, 6314, 1662), (5, 28231, 3331), (4, 7050, 1656), (3, 5305, 1171), (5, 6637, 2293), (3, 7834, 1764), (3, 1000, 2768), (4, 8112, 3733), (3, 5850, 1536), (4, 6660, 1638), (3, 6637, 1972), (2, 15267, 1478), (3, 5146, 1408), (3, 6017, 1812), (3, 8410, 1722), (4, 5625, 1780), (4, 5600, 1674), (4, 6525, 1850), (3, 6060, 1925), (4, 5539, 2343), (3, 7566, 1567), (4, 5484, 1664), (6, 5348, 1386), (5, 15834, 2617), (4, 8022, 2321), (4, 11966, 2638), (4, 8460, 1915), (4, 15105, 2589), (4, 10859, 2709), (3, 6300, 1587), (3, 11554, 1694), (3, 6000, 1536), (5, 31000, 3662), (3, 4054, 1736), (2, 20700, 2205), (3, 5525, 1502), (4, 92681, 1696), (3, 8178, 2186), (4, 5944, 1928), (3, 18838, 1294), (4, 4315, 1535), (3, 5167, 1980), (4, 7893, 2090), (3, 6056, 1837), (3, 5828, 1715), (3, 6341, 1574), (2, 6362, 1185), (4, 4950, 1774)]
B0, B_SQRFT, B_LOT, B_BDRMS = -21.77031, 0.1227782, 0.0020677, 13.85252

bdrms, lotsize, sqrft = np.array(ROWS, dtype=float).T
sq = (B0 + B_SQRFT * sqrft + B_LOT * lotsize + B_BDRMS * bdrms) ** 2

MARK = "#1A476F"
YTICKS = [0, 100000, 200000, 300000]
panels = [
    (bdrms, "bdrms", [2, 3, 4, 5, 6, 7], (1.8, 7.1)),
    (lotsize, "lotsize", [0, 20000, 40000, 60000, 80000, 100000], (-3000, 103000)),
    (sqrft, "sqrft", [1000, 2000, 3000, 4000], (900, 4080)),
]

fig, axes = style.figure(2, 2, figsize=(5.4, 4.0), constrained_layout=True)
for ax, (x, name, xt, xl) in zip(axes.flat, panels):
    ax.scatter(x, sq, s=22, color=MARK, linewidths=0, zorder=3)
    ax.set_xlim(*xl)
    ax.set_ylim(-18000, 335000)
    ax.xaxis.set_major_locator(FixedLocator(xt))
    ax.yaxis.set_major_locator(FixedLocator(YTICKS))
    ax.set_xlabel(name)
    ax.set_ylabel("Squared residuals")
    ax.grid(axis="y", color=style.LIGHT, linewidth=0.6, zorder=0)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    ax.set_axisbelow(True)
axes[0, 0].set_xlim(1.8, 7.2)
axes.flat[3].set_visible(False)
style.save(fig, OUT)
