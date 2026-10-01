import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig05.png")

# Coordinates are read off the original slide in pixels (y grows downward).
X0, X1, YTOP, YBOT = 192, 1150, 70, 497
LINE = lambda x: 398 + (209 - 398) * (x - 192) / (1150 - 192)
PTS = [(310, 349), (468, 275), (519, 375), (738, 370), (773, 378),
       (878, 318), (906, 116), (975, 279)]
XI, YI = 603, 227
XA, YA = 391, 421


def brace(ax, x, y0, y1, w=14, color=None):
    """Right-pointing curly brace spanning y0..y1 with its tip at x + w."""
    ym = (y0 + y1) / 2
    r = min(w, abs(y1 - y0) / 4)
    t = np.linspace(0, np.pi / 2, 20)
    pts = []
    pts += [(x + r - r * np.cos(a), y0 + r * np.sin(a)) for a in t]
    pts += [(x + r, y0 + r), (x + r, ym - r)]
    pts += [(x + r + r * (1 - np.cos(a)), ym - r + r * np.sin(a)) for a in t]
    pts += [(x + r + r * (1 - np.cos(a)), ym + r - r * np.sin(a)) for a in t[::-1]]
    pts += [(x + r, ym + r), (x + r, y1 - r)]
    pts += [(x + r - r * np.cos(a), y1 - r * np.sin(a)) for a in t[::-1]]
    p = np.array(pts)
    ax.plot(p[:, 0], p[:, 1], color=color or style.DARK, lw=1.1, solid_capstyle="round")


fig, ax = style.figure(figsize=(style.WIDTH_IN, style.WIDTH_IN * 545 / 1250))
ax.set_xlim(0, 1250)
ax.set_ylim(545, 0)
ax.axis("off")

ax.plot([123, 1150], [16, 16], color=style.DARK, lw=0.8)
ax.text(152, 31, "Fitted values and residuals.", fontsize=8, va="center", color=style.DARK)

ax.annotate("", xy=(X0, YTOP - 8), xytext=(X0, YBOT),
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=1.3))
ax.plot([X0, 1160], [YBOT, YBOT], color=style.DARK, lw=1.3)
ax.text(176, 76, "$y$", ha="right", va="center", fontsize=9, style="italic")
ax.text(1157, 512, "$x$", ha="center", va="center", fontsize=9)

ax.plot([X0, 1150], [LINE(X0), LINE(1150)], color=style.DARK, lw=1.1)

ax.plot([XI, XI], [YI, YBOT], color=style.DARK, lw=1.2)
ax.plot([XA, XA], [LINE(XA), YBOT], color=style.DARK, lw=1.2)
ax.plot([XA, XA], [LINE(XA), YA], color="white", lw=1.2, ls=(0, (3, 2)))
ax.plot([XA, XA], [LINE(XA), YA], color=style.DARK, lw=0.8, ls=(0, (3, 2)))

px, py = zip(*(PTS + [(XI, YI), (XA, YA)]))
ax.plot(px, py, "o", color=style.DARK, ms=3)

ax.text(XI + 24, YI - 8, "$y_i$", ha="center", va="center", fontsize=9)
ax.text(XA - 28, YA, "$y_1$", ha="center", va="center", fontsize=9)
ax.text(XA, 516, "$x_1$", ha="center", va="center", fontsize=9)
ax.text(XI, 516, "$x_i$", ha="center", va="center", fontsize=9)

brace(ax, XI + 8, YI + 4, LINE(XI) - 2, w=11)
brace(ax, XI + 8, LINE(XI) + 2, YBOT - 2, w=11)
ax.text(648, 266, r"$\hat{\varepsilon}$= residual", ha="left", va="center", fontsize=8.5)
ax.text(645, 406, r"$\hat{y}_i$= Fitted value", ha="left", va="center", fontsize=8.5)

ax.plot([1075, 1100], [236, 219], color=style.DARK, lw=0.8)
ax.text(1008, 266, r"$\hat{y}$ =   $\hat{\alpha}$ + $\hat{\beta}\,x$", ha="left", va="center", fontsize=9)

style.save(fig, OUT)
