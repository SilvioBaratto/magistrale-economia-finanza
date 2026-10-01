import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style
from matplotlib.ticker import FixedLocator

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-07/fig02.png")

# The quarterly 1955-2001 spread (R1yr - R90) is not in the course datasets
# (tassi-USA is monthly and has a different range), so the values were read
# off the slide chart at each quarter.
SPREAD = [
    0.20, 0.36, 0.30, 0.15, 0.09, 0.16, 0.24, 0.54, 0.47, 0.52, 0.73, 0.33,
    0.31, 0.39, 1.06, 1.04, 0.91, 0.84, 1.02, 0.93, 0.70, 0.16, 0.14, 0.75,
    0.83, 1.24, 1.33, 0.70, 0.74, 0.39, 0.34, 0.07, 0.06, 0.16, 0.21, 0.25,
    0.36, 0.36, 0.32, 0.36, 0.01, -0.04, 0.01, 0.32, 0.37, 0.02, 0.10, -0.15,
    -0.21, 0.15, 1.29, 1.40, 0.90, -0.16, -0.44, -0.08, -0.17, -1.74, -1.44, -1.03,
    -1.02, -0.21, 0.24, 0.10, 0.18, 0.42, 0.20, -0.02, 0.86, 0.50, 0.45, 0.30,
    -0.12, -0.72, -2.19, -2.57, -1.98, -2.75, -3.06, -2.07, 0.34, 1.15, 1.36, 1.29,
    1.13, 1.10, 0.61, 0.34, 0.75, 0.52, 0.47, 0.46, 0.54, 0.51, 0.30, 0.25,
    0.23, -0.15, -0.98, -1.30, -1.11, -2.39, 0.29, -2.14, -2.48, -2.65, -1.65, 0.01,
    0.11, -0.71, 0.83, -0.15, 0.11, 0.36, 0.84, 0.51, 0.50, 0.97, 0.42, 0.81,
    0.92, 0.38, 0.01, -0.29, -0.36, -0.27, -0.21, -0.47, -0.33, 0.15, 0.29, 0.32,
    0.14, 0.13, 0.03, 0.06, -0.12, -0.84, -0.98, -0.83, -0.07, 0.03, -0.36, -0.44,
    0.14, 0.38, 0.25, 0.05, 0.37, 0.45, 0.16, 0.52, 0.38, 0.38, 0.37, 0.51,
    0.65, 1.19, 1.11, 1.42, 1.05, -0.08, -0.17, -0.27, -0.25, 0.43, 0.47, 0.20,
    0.37, 0.33, 0.01, -0.02, -0.21, -0.09, -0.44, -0.47, -0.02, 0.12, 0.07, 0.38,
    0.51, -0.13, -0.44, -0.52, -0.98, -0.66, -0.09, 0.10
]
t = 1955.0 + 0.25 * np.arange(len(SPREAD))

fig, ax = style.figure(height_ratio=0.34)
ax.plot(t, SPREAD, color=style.GP_RED, linewidth=style.GP_LINEWIDTH)
ax.axhline(0, color=style.DARK, lw=0.7, ls=":")
ax.set_xlim(1953.8, 2002.9)
ax.set_ylim(-3.5, 1.5)
ax.set_xticks(range(1955, 2001, 5))
ax.set_yticks(np.arange(-3.5, 1.51, 0.5))
ax.set_yticklabels([("%g" % y) for y in np.arange(-3.5, 1.51, 0.5)])
ax.set_ylabel("spread (R1yr-R90)")
style.save(fig, OUT)
