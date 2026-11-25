"""Appunti ECON 2026-11-17: one-sided test on the right, threshold at alpha = 5%.

Rebuilt from the audio, not from a slide. The lecturer draws the density of the t statistic
under the null (the "curva rossa", N(0,1)), shades the area beyond the threshold as alpha
("area gialla") and reads the thresholds off the normal table: 1.64 for alpha = 5%, 1.96 for
alpha = 2.5%. The alternative curve is described only as "shifted to the right" with no
amount, so it is not drawn.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.stats import norm
import style

OUT = str(style.REPO / "obsidian/01-Econometria/appunti/figure/2026-11-17-fig01.png")

ALPHA = 0.05
ALPHA_SECOND = 0.025
THRESHOLD_ALPHA = 1.64
THRESHOLD_ALPHA_SECOND = 1.96
# The lecturer reads rounded values off the normal table, so the check allows for rounding.
TABLE_ROUNDING = 1e-3

AREA_YELLOW = "#E8C547"
X_LIMIT = 4.0
GRID_POINTS = 800
Y_LIMIT = 0.5

# Label heights as fractions of the y limit, so they follow it if it changes.
ZONE_LABEL_Y = 0.9 * Y_LIMIT
SECOND_THRESHOLD_LABEL_Y = 0.72 * Y_LIMIT
ALPHA_NOTE_Y = 0.5 * Y_LIMIT
ARROW_TIP_Y = 0.06 * Y_LIMIT

# Offsets from the threshold: the arrow tip must stay inside the shaded tail.
ARROW_TIP_OFFSET = 0.56
ALPHA_NOTE_OFFSET = 1.06
ZONE_LABEL_GAP = 0.1
SECOND_THRESHOLD_LABEL_GAP = 0.08


def decimal_comma(value, digits=2):
    """Format a number with the Italian decimal comma, for plain-text labels."""
    return f"{value:.{digits}f}".replace(".", ",")


def percent_label(share):
    """Format a share as a percentage with a decimal comma that is safe inside mathtext."""
    return f"{share * 100:g}".replace(".", "{,}") + r"\%"


assert abs(norm.sf(THRESHOLD_ALPHA) - ALPHA) < TABLE_ROUNDING
assert abs(norm.sf(THRESHOLD_ALPHA_SECOND) - ALPHA_SECOND) < TABLE_ROUNDING

grid = np.linspace(-X_LIMIT, X_LIMIT, GRID_POINTS)
density = norm.pdf(grid)
tail = grid >= THRESHOLD_ALPHA

fig, ax = style.figure(height_ratio=0.5)
ax.plot(grid, density, color=style.RED, lw=1.6)
ax.fill_between(grid[tail], density[tail], color=AREA_YELLOW, alpha=0.9, linewidth=0)
ax.axvline(THRESHOLD_ALPHA, color=style.DARK, lw=1.0)
ax.axvline(THRESHOLD_ALPHA_SECOND, color=style.GREY, lw=0.9, ls="--")
ax.set_xticks([0, THRESHOLD_ALPHA])
ax.set_xticklabels(["0", decimal_comma(THRESHOLD_ALPHA)])
ax.set_ylim(0, Y_LIMIT)
ax.set_yticks([])
ax.set_xlim(-X_LIMIT, X_LIMIT)
ax.set_xlabel("t, sotto l'ipotesi nulla")
ax.annotate(rf"$\alpha = {percent_label(ALPHA)}$",
            xy=(THRESHOLD_ALPHA + ARROW_TIP_OFFSET, ARROW_TIP_Y),
            xytext=(THRESHOLD_ALPHA + ALPHA_NOTE_OFFSET, ALPHA_NOTE_Y), ha="left",
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.7))
ax.text(THRESHOLD_ALPHA - ZONE_LABEL_GAP, ZONE_LABEL_Y, "non rifiuto la nulla", ha="right",
        color=style.DARK)
ax.text(THRESHOLD_ALPHA + ZONE_LABEL_GAP, ZONE_LABEL_Y, "rifiuto la nulla", ha="left",
        color=style.DARK)
ax.text(THRESHOLD_ALPHA_SECOND + SECOND_THRESHOLD_LABEL_GAP, SECOND_THRESHOLD_LABEL_Y,
        rf"{decimal_comma(THRESHOLD_ALPHA_SECOND)}: soglia per "
        rf"$\alpha = {percent_label(ALPHA_SECOND)}$",
        ha="left", color=style.GREY, fontsize=8.5)
style.save(fig, OUT)
print(OUT)
