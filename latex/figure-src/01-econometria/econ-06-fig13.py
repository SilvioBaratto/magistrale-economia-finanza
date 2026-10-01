import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig13.png")

data = np.loadtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig13.csv"), delimiter=",", skiprows=1)
t, p = data[:, 0], data[:, 1]

fig, ax = style.figure(figsize=(style.WIDTH_IN * 1.3, style.WIDTH_IN * 1.3 / 2.15))
ax.plot(t, p, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.set_xlim(0, 12600); ax.set_ylim(1.04, 1.24)
ax.set_xticks(range(0, 12001, 2000))
ax.set_yticks(np.arange(1.04, 1.241, 0.02))
ax.set_yticklabels([f"{v:g}" for v in np.round(np.arange(1.04, 1.241, 0.02), 2)])
for s in ax.spines.values():
    s.set_visible(True)
ax.tick_params(direction="out", top=False, right=False)
for mk in (ax.twinx, ax.twiny):
    a2 = mk(); a2.set_xlim(ax.get_xlim()); a2.set_ylim(ax.get_ylim())
    a2.set_xticks(ax.get_xticks()); a2.set_yticks(ax.get_yticks())
    a2.tick_params(direction="in", labeltop=False, labelright=False, labelbottom=False, labelleft=False, bottom=False, left=False, top=True, right=True)
    a2.grid(False)
    for sp in a2.spines.values(): sp.set_visible(False)
ax.grid(False)
ax.set_ylabel("prezzo dell'asset")
style.save(fig, OUT)
