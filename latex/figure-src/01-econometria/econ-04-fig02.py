"""econ-04 fig02: histograms of chi-square draws, df = 1, 2, 5, 10 (bins recovered from the slide)."""
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import csv

import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-04/fig02.png")

DATA = str(style.REPO / "latex/figure-src/01-econometria/data/econ-04-fig02.csv")
with open(DATA) as fh:
    rows = list(csv.DictReader(fh))
cfg = [
    (1, 0.20, (-0.4, 16.5), np.arange(0, 15.1, 2.5), [0.25, 0.5, 0.75, 1.0], "{:.2f}", (0, 1.12)),
    (2, 0.30, (-1.0, 23.0), [0, 5, 10, 15, 20], [0.1, 0.2, 0.3, 0.4, 0.5], "{:.1f}", (0, 0.52)),
    (5, 0.60, (-2.5, 35.0), [0, 5, 10, 15, 20, 25, 30, 35], [0.05, 0.10, 0.15], "{:.2f}", (0, 0.165)),
    (10, 0.80, (-4.0, 42.0), [0, 10, 20, 30, 40], [0.025, 0.05, 0.075, 0.10], "{:.3f}", (0, 0.118)),
]

fig, axes = style.figure(2, 2, figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.39))
for ax, (df, bw, xlim, xt, yt, fmt, ylim) in zip(axes.ravel(), cfg):
    sel = [r for r in rows if int(r["df"]) == df]
    left = np.array([float(r["left"]) for r in sel])
    dens = np.array([float(r["density"]) for r in sel])
    w = float(sel[0]["right"]) - left[0]
    idx = np.rint((left - left[0]) / w).astype(int)
    heights = np.zeros(idx.max() + 1)
    heights[idx] = dens
    bins = left[0] + w * np.arange(len(heights) + 1)
    centers = bins[:-1] + w / 2
    ax.hist(centers, bins=bins, weights=heights, histtype="step", color="#D62728", linewidth=0.6)
    ax.hist(centers, bins=bins, weights=heights, histtype="bar", fill=False, edgecolor="#D62728", linewidth=0.5)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks(xt)
    ax.set_xticklabels([f"{v:.1f}" if df == 1 else f"{v:g}" for v in xt])
    ax.set_yticks(yt)
    ax.set_yticklabels([fmt.format(v) for v in yt])
    ax.tick_params(labelsize=7, length=2.5)
    ax.set_title(rf"Istogramma di una v.c. $\chi^2_{{{df}}}$", fontsize=8, y=0.86)
fig.get_layout_engine().set(w_pad=0.1, h_pad=0.08)
style.save(fig, OUT)
