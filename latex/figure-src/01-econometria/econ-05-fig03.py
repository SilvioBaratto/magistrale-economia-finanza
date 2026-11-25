"""econ-05 fig03: squared OLS residuals of price ~ sqrft + lotsize + bdrms (hprice1,
n = 88) against each regressor.

Data: Wooldridge hprice1 (the course's hprices.gdt), embedded as (price, bdrms, lotsize,
sqrft) with price in thousands of dollars. The fit reproduces the note's OLS table and
the auxiliary regression of the squared residuals on the three regressors
(R^2 = 0.160, F = 5.34, p = 0.002).
"""
import sys

import numpy as np
from matplotlib.ticker import FixedLocator

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-05/fig03.png")

ROWS = [
    (300, 4, 6126, 2438), (370, 3, 9903, 2076), (191, 3, 5200, 1374), (195, 3, 4600, 1448),
    (373, 4, 6095, 2514), (466.275, 5, 8566, 2754), (332.5, 3, 9000, 2067),
    (315, 3, 6210, 1731), (206, 3, 6000, 1767), (240, 3, 2892, 1890), (285, 4, 6000, 2336),
    (300, 5, 7047, 2634), (405, 3, 12237, 3375), (212, 3, 6460, 1899), (265, 3, 6519, 2312),
    (227.4, 4, 3597, 1760), (240, 4, 5922, 2000), (285, 3, 7123, 1774), (268, 3, 5642, 1376),
    (310, 4, 8602, 1835), (266, 3, 5494, 2048), (270, 3, 7800, 2124), (225, 3, 6003, 1768),
    (150, 4, 5218, 1732), (247, 3, 9425, 1440), (275, 3, 6114, 1932), (230, 3, 6710, 1932),
    (343, 3, 8577, 2106), (477.5, 7, 8400, 3529), (350, 4, 9773, 2051), (230, 4, 4806, 1573),
    (335, 4, 15086, 2829), (251, 3, 5763, 1630), (235, 4, 6383, 1840), (361, 4, 9000, 2066),
    (190, 4, 3500, 1702), (360, 4, 10892, 2750), (575, 5, 15634, 3880),
    (209.001, 4, 6400, 1854), (225, 2, 8880, 1421), (246, 3, 6314, 1662),
    (713.5, 5, 28231, 3331), (248, 4, 7050, 1656), (230, 3, 5305, 1171), (375, 5, 6637, 2293),
    (265, 3, 7834, 1764), (313, 3, 1000, 2768), (417.5, 4, 8112, 3733), (253, 3, 5850, 1536),
    (315, 4, 6660, 1638), (264, 3, 6637, 1972), (255, 2, 15267, 1478), (210, 3, 5146, 1408),
    (180, 3, 6017, 1812), (250, 3, 8410, 1722), (250, 4, 5625, 1780), (209, 4, 5600, 1674),
    (258, 4, 6525, 1850), (289, 3, 6060, 1925), (316, 4, 5539, 2343), (225, 3, 7566, 1567),
    (266, 4, 5484, 1664), (310, 6, 5348, 1386), (471.25, 5, 15834, 2617), (335, 4, 8022, 2321),
    (495, 4, 11966, 2638), (279.5, 4, 8460, 1915), (380, 4, 15105, 2589),
    (325, 4, 10859, 2709), (220, 3, 6300, 1587), (215, 3, 11554, 1694), (240, 3, 6000, 1536),
    (725, 5, 31000, 3662), (230, 3, 4054, 1736), (306, 2, 20700, 2205), (425, 3, 5525, 1502),
    (318, 4, 92681, 1696), (330, 3, 8178, 2186), (246, 4, 5944, 1928), (225, 3, 18838, 1294),
    (111, 4, 4315, 1535), (268.125, 3, 5167, 1980), (244, 4, 7893, 2090), (295, 3, 6056, 1837),
    (236, 3, 5828, 1715), (202.5, 3, 6341, 1574), (219, 2, 6362, 1185), (242, 4, 4950, 1774),
]

price, bdrms, lotsize, sqrft = np.array(ROWS, dtype=float).T
design = np.column_stack([np.ones_like(price), sqrft, lotsize, bdrms])
coef, *_ = np.linalg.lstsq(design, price, rcond=None)
squared_resid = (price - design @ coef) ** 2

MARK = "#1A476F"
YTICKS = [0, 10000, 20000, 30000, 40000]
YLIM = (-2500, 47000)
panels = [
    (bdrms, "bdrms", [2, 3, 4, 5, 6, 7], (1.8, 7.2)),
    (lotsize, "lotsize", [0, 20000, 40000, 60000, 80000, 100000], (-3000, 103000)),
    (sqrft, "sqrft", [1000, 2000, 3000, 4000], (900, 4080)),
]

fig, axes = style.figure(2, 2, figsize=(5.4, 4.0), constrained_layout=True)
for ax, (x, name, xt, xl) in zip(axes.flat, panels):
    ax.scatter(x, squared_resid, s=22, color=MARK, linewidths=0, zorder=3)
    ax.set_xlim(*xl)
    ax.set_ylim(*YLIM)
    ax.xaxis.set_major_locator(FixedLocator(xt))
    ax.yaxis.set_major_locator(FixedLocator(YTICKS))
    ax.set_xlabel(name)
    ax.set_ylabel("Squared residuals")
    ax.grid(axis="y", color=style.LIGHT, linewidth=0.6, zorder=0)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    ax.set_axisbelow(True)
axes.flat[3].set_visible(False)
style.save(fig, OUT)
