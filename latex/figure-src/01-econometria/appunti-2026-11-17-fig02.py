"""Appunti ECON 2026-11-17: two-sided test, alpha = 5% split between the two tails.

Rebuilt from the audio, not from a slide. For H0: beta = 1/2 against beta != 1/2 the lecturer
splits alpha in half, alpha/2 in each tail, and with alpha = 5% on a normal reads the two
thresholds as minus and plus 1.96. The alternatives (curves to the left or to the right of the
null) are described only as "not centred", so only the null is drawn.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.stats import norm
import style

OUT = str(style.REPO / "obsidian/01-Econometria/appunti/figure/2026-11-17-fig02.png")

ALPHA = 0.05
THRESHOLD = 1.96
# The lecturer reads rounded values off the normal table, so the check allows for rounding.
TABLE_ROUNDING = 1e-3

AREA_YELLOW = "#E8C547"
X_LIMIT = 4.0
GRID_POINTS = 800
Y_LIMIT = 0.5

# Label heights as fractions of the y limit, so they follow it if it changes.
REJECT_LABEL_Y = 0.9 * Y_LIMIT
ALPHA_NOTE_Y = 0.5 * Y_LIMIT
ARROW_TIP_Y = 0.03 * Y_LIMIT
NULL_LABEL_Y = 0.1 * Y_LIMIT

# Offsets beyond the threshold: the arrow tip must stay inside the shaded tail.
ARROW_TIP_OFFSET = 0.44
ALPHA_NOTE_OFFSET = 0.64
REJECT_LABEL_GAP = 0.1


def decimal_comma(value, digits=2):
    """Format a number with the Italian decimal comma, for plain-text labels."""
    return f"{value:.{digits}f}".replace(".", ",")


def percent_label(share):
    """Format a share as a percentage with a decimal comma that is safe inside mathtext."""
    return f"{share * 100:g}".replace(".", "{,}") + r"\%"


assert abs(2 * norm.sf(THRESHOLD) - ALPHA) < TABLE_ROUNDING

grid = np.linspace(-X_LIMIT, X_LIMIT, GRID_POINTS)
density = norm.pdf(grid)
left_tail = grid <= -THRESHOLD
right_tail = grid >= THRESHOLD
tail_note = rf"$\alpha/2 = {percent_label(ALPHA / 2)}$"

fig, ax = style.figure(height_ratio=0.5)
ax.plot(grid, density, color=style.RED, lw=1.6)
for tail in (left_tail, right_tail):
    ax.fill_between(grid[tail], density[tail], color=AREA_YELLOW, alpha=0.9, linewidth=0)
ax.axvline(-THRESHOLD, color=style.DARK, lw=1.0)
ax.axvline(THRESHOLD, color=style.DARK, lw=1.0)
ax.set_xticks([-THRESHOLD, 0, THRESHOLD])
ax.set_xticklabels([f"-{decimal_comma(THRESHOLD)}", "0", decimal_comma(THRESHOLD)])
ax.set_yticks([])
ax.set_ylim(0, Y_LIMIT)
ax.set_xlim(-X_LIMIT, X_LIMIT)
ax.set_xlabel("t, sotto l'ipotesi nulla")
ax.annotate(tail_note, xy=(THRESHOLD + ARROW_TIP_OFFSET, ARROW_TIP_Y),
            xytext=(THRESHOLD + ALPHA_NOTE_OFFSET, ALPHA_NOTE_Y), ha="left",
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.7))
ax.annotate(tail_note, xy=(-THRESHOLD - ARROW_TIP_OFFSET, ARROW_TIP_Y),
            xytext=(-THRESHOLD - ALPHA_NOTE_OFFSET, ALPHA_NOTE_Y), ha="right",
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.7))
ax.text(0, NULL_LABEL_Y, "non rifiuto\nla nulla", ha="center", va="center", color=style.DARK)
ax.text(-THRESHOLD - REJECT_LABEL_GAP, REJECT_LABEL_Y, "rifiuto", ha="right", color=style.DARK)
ax.text(THRESHOLD + REJECT_LABEL_GAP, REJECT_LABEL_Y, "rifiuto", ha="left", color=style.DARK)
style.save(fig, OUT)
print(OUT)
