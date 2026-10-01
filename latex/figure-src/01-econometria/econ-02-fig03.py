import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import style

CSV = str(style.DATASETS / "ECON_Dataset_wage.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig03.png")

d = pd.read_csv(CSV)
m = d.groupby("educ").wage.mean()

fig, ax = style.figure(height_ratio=0.5)
ax.scatter(d.educ, d.wage, s=14, color=style.BLUE, zorder=2, linewidths=0)
ax.scatter(m.index, m.values, s=46, marker="s", color=style.RED, zorder=3, linewidths=0)
ax.set_xlim(-0.6, 20)
ax.set_ylim(-0.8, 25.8)
ax.set_xticks(range(0, 21, 5))
ax.set_yticks(range(0, 26, 5))
ax.set_xlabel("educ")
ax.set_ylabel("wage")
ax.grid(axis="y")
ax.set_axisbelow(True)
h = [Line2D([], [], marker="o", ls="", color=style.BLUE, markersize=4),
     Line2D([], [], marker="s", ls="", color=style.RED, markersize=6)]
ax.legend(h, ["wage", "Conditional mean of wage given educ"], loc="upper center",
          bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=True, edgecolor=style.DARK,
          fancybox=False, columnspacing=1.2, handletextpad=0.3)
style.save(fig, OUT)
