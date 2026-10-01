import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
import style

CSV = str(style.DATASETS / "ECON_Dataset_wage.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig04.png")
GREEN = "#4F6F1F"

d = pd.read_csv(CSV)
m = d.groupby("educ").wage.mean()
b, a = np.polyfit(d.educ, d.wage, 1)
xs = np.array([d.educ.min(), d.educ.max()])

fig, ax = style.figure(height_ratio=0.42)
ax.scatter(d.educ, d.wage, s=14, color=style.BLUE, zorder=2, linewidths=0)
ax.scatter(m.index, m.values, s=46, marker="s", color=style.RED, zorder=3, linewidths=0)
ax.plot(xs, a + b * xs, color=GREEN, lw=1.2, zorder=4)
ax.set_xlim(-0.6, 20)
ax.set_ylim(-1.5, 22.5)
ax.set_xticks(range(0, 21, 5))
ax.set_yticks(range(0, 21, 5))
ax.set_xlabel("educ")
ax.grid(axis="y")
ax.set_axisbelow(True)
h = [Line2D([], [], marker="o", ls="", color=style.BLUE, markersize=4),
     Line2D([], [], marker="s", ls="", color=style.RED, markersize=6),
     Line2D([], [], color=GREEN, lw=1.2)]
ax.legend([h[0], h[2], h[1]], ["wage", "Fitted values", "conditional mean"], loc="upper center",
          bbox_to_anchor=(0.5, -0.27), ncol=2, frameon=True, edgecolor=style.DARK,
          fancybox=False, columnspacing=1.2, handletextpad=0.3)
style.save(fig, OUT)
print(a, b, len(d))
