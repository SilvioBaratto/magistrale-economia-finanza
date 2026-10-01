"""econ-06 fig 7: monthly returns (%) of the S&P 500 and Boeing, 1996-2006.

Neither series is in the course datasets (exelon.csv has Exelon, not Boeing), so
the 130 monthly values were digitised from the slide plot (about 0.1 pp
resolution) and redrawn here.
"""
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig07.png")

SP500 = [0.7, 0.9, 1.3, 2.2, 0.5, -4.7, 2.4, 5.3, 2.6, 7.0, -2.0, 6.0, -0.2, -4.4, 5.6, 5.6, 4.4, 7.5, -5.8, 5.1, -3.5, 4.4, 1.5, 1.1, 6.8, 5.1, 0.5, -2.0, 4.0, -0.2, -15.7, 6.4, 7.7, 5.8, 5.5, 4.3, -3.3, 3.9, 3.7, -2.5, 5.2, -3.3, -0.6, -2.8, 6.0, 2.0, 5.6, -5.2, -2.5, 9.1, -3.1, -2.4, 2.2, -1.6, 5.9, -5.6, -0.4, -8.2, 0.7, 3.3, -9.6, -7.0, 7.4, 0.5, -2.5, -1.0, -6.7, -8.5, 2.8, 7.1, 0.5, -1.6, -2.0, 3.4, -6.2, -0.8, -7.5, -8.2, 0.5, -11.6, 8.2, 5.9, -6.2, -2.7, -1.8, 0.5, 7.7, 5.6, 1.1, 1.7, 1.7, -1.2, 5.5, 1.0, 4.8, 1.7, 1.3, -1.6, -1.6, 1.3, 1.8, -3.3, 0.3, 1.0, 1.4, 3.7, 3.3, -2.5, 1.8, -1.7, -2.0, 3.0, -0.1, 3.6, -1.0, 0.6, -1.7, 3.4, -0.1, 2.5, 0.1, 1.1, 1.0, -3.1, 0.1, 0.5, 2.1, 2.5, 3.0, 0.2]
BOEING = [4.9, 6.6, -5.2, 4.1, 2.2, 1.7, 2.6, 4.4, 1.1, 4.8, 7.0, -0.4, -4.8, -3.3, -0.6, 6.8, 0.7, 10.0, -7.0, -0.2, -12.6, 10.5, -8.0, -3.9, 13.2, -4.0, -4.0, -4.6, -6.5, -12.6, -22.2, 10.4, 8.9, 8.3, -21.8, 6.0, 3.7, -4.6, 17.8, 3.9, 3.6, 3.3, 0.7, -5.9, 7.5, -12.2, 3.2, 7.0, -18.1, 2.6, 4.9, -1.0, 5.9, 15.5, 9.6, 18.4, 4.5, 2.6, -3.5, -11.9, 6.3, -10.8, 10.4, 3.3, -12.3, 5.1, -8.8, -42.4, -0.9, 8.2, 10.1, 5.3, 11.9, 6.3, -7.8, -4.7, 5.3, -8.5, -10.9, -8.2, -13.4, 14.0, -3.3, -4.2, -13.2, -10.3, 9.0, 12.3, 11.3, -3.3, 12.7, -8.5, 11.5, 0.5, 9.1, -0.9, 4.0, -5.4, 4.5, 7.0, 10.9, -0.6, 3.2, -1.6, -3.5, 7.5, -3.5, -2.5, 8.6, 6.6, 2.0, 7.7, 2.8, 0.1, 1.8, 1.5, -5.0, 5.8, 3.3, -2.5, 6.7, 7.0, 6.7, -0.2, -1.4, -5.5, -3.3, 5.3, 1.4, 6.4]

t = 1996 + (1 + np.arange(len(SP500))) / 12
fig, ax = style.figure(height_ratio=0.5)
ax.axhline(0, color=style.DARK, lw=0.8, ls=(0, (1, 2)))
ax.plot(t, SP500, color=style.GP_RED, lw=style.GP_LINEWIDTH, label="Sp500")
ax.plot(t, BOEING, color=style.GP_GREEN, lw=style.GP_LINEWIDTH, ls=(0, (4, 1.5)), label="Boeing")
ax.set_xlim(1995.85, 2007.15)
ax.set_ylim(-50, 20)
ax.set_xticks(range(1996, 2007, 2))
ax.set_yticks(range(-50, 21, 10))
for s in ("top", "right"):
    ax.spines[s].set_visible(True)
ax.legend(loc="upper left", bbox_to_anchor=(0.0, 1.0), handlelength=2.5, frameon=False, fontsize=8, borderaxespad=0.3, labelspacing=0.2)
style.save(fig, OUT)
