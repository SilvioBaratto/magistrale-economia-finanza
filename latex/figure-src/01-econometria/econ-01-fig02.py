import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
import style
import matplotlib.pyplot as plt

CSV = str(style.DATASETS / "ECON_Dataset_caschool.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-01/fig02.png")

df = pd.read_csv(CSV)
names = ["avg_score", "str", "avginc"]
ticks = {"avg_score": [600, 650, 700], "str": [15, 20, 25], "avginc": [0, 20, 40, 60]}
lim = {}
for n in names:
    lo, hi = df[n].min(), df[n].max()
    pad = 0.04 * (hi - lo)
    lim[n] = (lo - pad, hi + pad)

fig, axes = plt.subplots(3, 3, figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.46),
                         gridspec_kw=dict(wspace=0, hspace=0))
SHADE = "#DCE6EC"
for i, yn in enumerate(names):
    for j, xn in enumerate(names):
        ax = axes[i, j]
        for s in ax.spines.values():
            s.set_visible(True)
            s.set_linewidth(0.8)
            s.set_color(style.DARK)
        ax.set_xlim(lim[xn])
        ax.set_ylim(lim[yn])
        ax.set_xticks(ticks[xn])
        ax.set_yticks(ticks[yn])
        if i == j:
            ax.set_facecolor(SHADE)
            ax.text(0.5, 0.5, yn, transform=ax.transAxes, ha="center", va="center", fontsize=9)
        else:
            ax.scatter(df[xn], df[yn], s=13, color="#1A476F", lw=0, alpha=0.95)
        ax.tick_params(length=3, width=0.6, labelsize=8,
                       bottom=False, top=False, left=False, right=False,
                       labelbottom=False, labeltop=False, labelleft=False, labelright=False)
        # alternating axes: x on bottom (row 3) for cols 1,3 / top (row 1) for col 2
        if j % 2 == 0 and i == 2:
            ax.tick_params(axis="x", bottom=True, labelbottom=True)
        if j == 1 and i == 0:
            ax.tick_params(axis="x", top=True, labeltop=True)
        if i == 1 and j == 0:
            ax.tick_params(axis="y", left=True, labelleft=True)
        if j == 2 and i in (0, 2):
            ax.tick_params(axis="y", right=True, labelright=True)
        if i == 2 and j == 2:
            pass
style.save(fig, OUT)
