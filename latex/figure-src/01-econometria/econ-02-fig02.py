import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
import math
import numpy as np
import pandas as pd

D = str(style.DATASETS / "ECON_Dataset_wage.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig02.png")

df = pd.read_csv(D)
levels = sorted(df.educ.unique())
data = [df.loc[df.educ == e, "wage"].values for e in levels]



def stata_pct(x, p):
    """Stata's percentile definition, used by its graph box (differs from numpy's)."""
    x = np.sort(x)
    k = len(x) * p
    if abs(k - round(k)) < 1e-9:
        k = int(round(k))
        return (x[k - 1] + x[min(k, len(x) - 1)]) / 2
    return x[math.ceil(k) - 1]


def stats(x):
    q1, med, q3 = (stata_pct(x, p) for p in (0.25, 0.5, 0.75))
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    inside = x[(x >= lo) & (x <= hi)]
    return dict(q1=q1, med=med, q3=q3, whislo=inside.min(), whishi=inside.max(),
                fliers=x[(x < lo) | (x > hi)])


fig, ax = style.figure(height_ratio=0.5)
ax.bxp(
    [stats(x) for x in data], positions=range(len(levels)), widths=0.6, patch_artist=True,
    boxprops=dict(facecolor="#9AB0C4", edgecolor="#1A476F", linewidth=1.2),
    medianprops=dict(color="#1A476F", linewidth=0.9),
    whiskerprops=dict(color="#1A476F", linewidth=1.2),
    capprops=dict(color="#1A476F", linewidth=1.2),
    flierprops=dict(marker="o", markerfacecolor="#1A476F", markeredgecolor="#1A476F", markersize=4),
)
ax.set_xticks(range(len(levels)))
ax.set_xticklabels([str(int(e)) for e in levels])
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.set_ylim(-1, 26)
ax.grid(axis="y")
ax.set_axisbelow(True)
ax.set_xlabel("educ")
ax.set_ylabel("wage")
style.save(fig, OUT)
