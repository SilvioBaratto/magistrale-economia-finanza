import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
import pandas as pd
import matplotlib.pyplot as plt

CSV = str(style.DATASETS / "ECON_Dataset_caschool.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-03/fig01.png")

df = pd.read_csv(CSV)
names = ["avg_score", "str", "avginc"]
lims = {"avg_score": (597, 710), "str": (13, 26.5), "avginc": (-1, 61)}
ticks = {"avg_score": [600, 650, 700], "str": [15, 20, 25], "avginc": [0, 20, 40, 60]}
FILL = "#E4ECF0"
NAVY = "#1B4A72"

fig, axes = plt.subplots(3, 3, figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.39),
                         gridspec_kw=dict(hspace=0, wspace=0, left=0.09, right=0.95, top=0.89, bottom=0.10))
for i, yv in enumerate(names):
    for j, xv in enumerate(names):
        ax = axes[i, j]
        for s in ax.spines.values():
            s.set_visible(True); s.set_linewidth(1.2); s.set_color('black')
        ax.set_xlim(lims[xv]); ax.set_ylim(lims[yv])
        ax.set_xticks([]); ax.set_yticks([])
        if i == j:
            ax.set_facecolor(FILL)
            ax.text(0.5, 0.5, yv, transform=ax.transAxes, ha="center", va="center", fontsize=10)
        else:
            ax.scatter(df[xv], df[yv], s=24, color=NAVY, alpha=1.0, linewidths=0)
        if j == 0 or True:
            pass
        # axis labels: columns alternate bottom/top/bottom, rows right/left/right
        if i == 2 and j in (0, 2):
            ax.set_xticks(ticks[xv]); ax.xaxis.set_ticks_position("bottom")
        if i == 0 and j == 1:
            ax.set_xticks(ticks[xv]); ax.xaxis.set_ticks_position("top")
        if j == 0 and i == 1:
            ax.set_yticks(ticks[yv]); ax.yaxis.set_ticks_position("left")
        if j == 2 and i in (0, 2):
            ax.set_yticks(ticks[yv]); ax.yaxis.set_ticks_position("right")
        ax.tick_params(labelsize=8, length=5, width=1.2)
        if i == 0 and j == 1:
            ax.tick_params(labeltop=True, labelbottom=False, top=True, bottom=False)
        if j == 2 and i in (0, 2):
            ax.tick_params(labelright=True, labelleft=False, right=True, left=False)
style.save(fig, OUT)
