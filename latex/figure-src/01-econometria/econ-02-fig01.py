import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
import style

CSV = str(style.DATASETS / "ECON_Dataset_wage.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig01.png")

d = pd.read_csv(CSV)
fig, ax = style.figure(height_ratio=0.34)
ax.scatter(d.educ, d.wage, s=14, color=style.BLUE, edgecolor="none", clip_on=False, zorder=3)
ax.set_xlim(-0.5, 20)
ax.set_ylim(-0.7, 25.5)
ax.set_xticks([0, 5, 10, 15, 20])
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.set_xlabel("educ")
ax.set_ylabel("wage")
ax.grid(axis="y", zorder=0)
ax.set_axisbelow(True)
style.save(fig, OUT)
