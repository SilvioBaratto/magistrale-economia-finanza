import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-01/fig05.png")

data = np.loadtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-01-fig05.csv"),
                  delimiter=",", skiprows=1)
x, y = data[:, 0], data[:, 1]
xs = np.array([-23.126, 16.020])
ys = np.array([-24.800, 17.601])

fig, ax = style.figure(figsize=(5.4, 3.25))
ax.scatter(x, y, s=38, color="#1A476F", zorder=2, linewidths=0, label="Portfolio Returns")
ax.plot(xs, ys, color="#8C2A2A", lw=1.2, zorder=3, label="Fitted values")
ax.set_xlim(-24, 20)
ax.set_ylim(-40, 40)
ax.set_xticks([-20, -10, 0, 10, 20])
ax.set_yticks([-40, -20, 0, 20, 40])
ax.set_xlabel("Market Portfolio")
ax.set_ylabel("Portfolio Returns")
ax.grid(axis="y", color=style.LIGHT, lw=0.6)
ax.set_axisbelow(True)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=2, frameon=True,
          edgecolor=style.DARK, fancybox=False)
style.save(fig, OUT)
