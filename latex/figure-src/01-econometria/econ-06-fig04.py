"""Fig. 4 of ECON 06: scatterplots of an AR(3) series against its lags (points recovered from the slide)."""
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig04.png")
DATA = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig04.csv")

# Coordinates are in slide plot-frame units; the frame spans exactly [0, XMAX] x [0, YMAX].
XMAX, YMAX = 136.099522, 107.101804
pts = np.genfromtxt(DATA, delimiter=",", names=True)

lags = [(1, "ar3_1"), (2, "ar3_2"), (3, "ar3_3"), (10, "ar3_10")]
# The slide's frames are 468 x 241 px, with a gap between the columns of about
# a third of a frame's width.
FRAME_ASPECT = 241 / 468
fig, axes = style.figure(2, 2, figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.6))
fig.get_layout_engine().set(wspace=0.2, hspace=0.06)
for ax, (j, name) in zip(axes.flat, lags):
    sel = pts[pts["lag"] == j]
    # Unclipped: four points sit exactly on the frame and the original draws them whole.
    ax.scatter(sel["x"], sel["y"], marker="+", s=16, linewidths=0.7, color=style.GP_RED, zorder=2, clip_on=False)
    ax.set_box_aspect(FRAME_ASPECT)
    ax.set_xlim(0, XMAX)
    ax.set_ylim(0, YMAX)
    ax.set_xlabel(name)
    ax.set_ylabel("ar3")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(True)
        s.set_linewidth(0.8)
style.save(fig, OUT)
