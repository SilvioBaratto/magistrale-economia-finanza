"""FSTR 11, slide 13: valore unitario di acquisizione delle azioni al variare della quota acquistata."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style
from matplotlib.patches import Rectangle

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-11/fig01.png")

W_BASE = 2.0          # (W_S + W_DIV) / N, per share
W_IND_OVER_N = 0.65   # W_IND / N
SHARES = [1.00, 0.75, 0.51]
LABELS = ["2,65", "2,867", "3,275"]
BASE_VALUE = 1.8
X_END = 2.81          # right end of the axes in category units, as on the slide


def w(alpha):
    """Unit acquisition value for a stake alpha."""
    return W_BASE + W_IND_OVER_N / np.asarray(alpha)


# The x axis is categorical (equidistant 100%, 75%, 51%): between categories alpha is a
# quadratic through the three stakes, so the curve is the exact w(alpha) at the three
# points and smooth and convex in between.
coef = np.polyfit([0, 1, 2], SHARES, 2)
xs = np.linspace(0, 2, 200)
curve = w(np.polyval(coef, xs))
values = w(SHARES)
assert [f"{v:.3f}".rstrip("0").replace(".", ",") for v in values] == LABELS, values

# The page shows figures at 0.8 of the line width, so the canvas keeps the full 5.4 in
# of the other FSTR figures and the text keeps the same scale.
W, H = style.WIDTH_IN, 2.74
AX_LEFT, AX_BOTTOM, AX_W, AX_H = 0.62, 0.52, 4.2, 2.1

fig, ax = style.figure(figsize=(W, H), constrained_layout=False)
ax.set_position([AX_LEFT / W, AX_BOTTOM / H, AX_W / W, AX_H / H])
ax.set_xlim(0, X_END)
ax.set_ylim(1.6, 3.6)
ax.spines["left"].set_linewidth(0.8)
ax.spines["bottom"].set_linewidth(0.8)

ax.plot([0, X_END], [BASE_VALUE] * 2, color=style.DARK, lw=0.9, ls=(0, (3.5, 2.5)), zorder=2)
ax.text(X_END, BASE_VALUE + 0.03, "valore base", ha="right", va="bottom", fontsize=9.5)

ax.plot(xs, curve, color=style.BLUE, lw=1.1, zorder=3)
ax.plot([0, 1, 2], values, ls="none", marker="s", ms=4.6, color=style.BLUE, mec="none",
        zorder=4, clip_on=False)

ax.annotate(LABELS[0], (0, values[0]), xytext=(-7, 0), textcoords="offset points",
            ha="right", va="center", fontsize=9, fontweight="bold", color=style.BLUE)
for x, v, lab in zip((1, 2), values[1:], LABELS[1:]):
    ax.annotate(lab, (x, v), xytext=(0, -6), textcoords="offset points", ha="center",
                va="top", fontsize=9, fontweight="bold", color=style.BLUE)
ax.annotate("$w$", (2, values[2]), xytext=(6, 3), textcoords="offset points", ha="left",
            va="center", fontsize=10, color=style.BLUE)

ax.text(0.40, 3.58, "valore unitario\ndi acquisizione\ndelle azioni $(w)$", ha="center",
        va="top", fontsize=9.5, linespacing=1.3)

ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["100%", "75%", "51%"], fontsize=9.5)
ax.set_yticks([1.6, 1.8, 2.0, 2.4, 2.8, 3.2, 3.6])
ax.set_yticklabels(["1,6", "1,8", "2,0", "2,4", "2,8", "3,2", "3,6"], fontsize=9.5)
ax.tick_params(axis="both", length=4, width=0.8, pad=4)
ax.annotate("% del capitale\nacquistata", (X_END, 1.6), xytext=(0, -8),
            textcoords="offset points", ha="center", va="top", fontsize=9.5, linespacing=1.3,
            annotation_clip=False)

fig.add_artist(Rectangle((0, 0), 1, 1, transform=fig.transFigure, facecolor="white",
                         edgecolor="none", zorder=-10))
style.save(fig, OUT)
print([round(float(v), 4) for v in values])
