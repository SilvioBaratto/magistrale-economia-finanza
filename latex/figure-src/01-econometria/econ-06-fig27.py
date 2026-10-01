"""Y_t = TD_t + Y*_t: monthly series (200 obs, 2004:11-2021:06), linear trend plus AR(1), data from the slide."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig27.png")
GREEN, ORANGE, PURPLE = "#1B9E77", "#D95F02", "#7570B3"

d = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig27.csv"),
                  delimiter=",", names=True)
x, y, td, ys = d["x"], d["Y"], d["TD"], d["Ystar"]

fig, ax = style.figure(figsize=(style.WIDTH_IN, 2.9))
ax.plot(x, y, color=GREEN, lw=0.9, label="Y")
ax.plot(x, td, color=ORANGE, lw=0.9, label="TD")
ax.plot(x, ys, color=PURPLE, lw=0.9, label="Y*")
ax.axhline(0, color=style.DARK, lw=0.7, ls=":", zorder=0)
ax.set_title("Y_t= TD_t + Y*_t")
ax.set_xlim(2004.4, 2021.8)
ax.set_ylim(-5, 30)
ax.set_xticks(range(2006, 2021, 2))
ax.set_yticks(range(-5, 31, 5))
ax.legend(loc="upper left", frameon=False, handlelength=3, labelspacing=0.1,
          bbox_to_anchor=(0.0, 1.0))
style.save(fig, OUT)
