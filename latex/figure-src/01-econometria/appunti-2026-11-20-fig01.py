"""Appunti ECON 2026-11-20: wage against education, one line per gender, after dropping M.

Rebuilt from the audio, not from a slide. The lecturer draws salary on the vertical axis and
education on the horizontal one. The group M line has slope beta_1 (expected positive) and
intercept alpha. The group F line has the same slope and intercept alpha + beta_3, and sits
below the M line because beta_3 is typically negative. The lines are parallel, so the gap
between the groups is beta_3 at every education level. He gives no numbers for the lines, so
the axes carry no values and the positions are only schematic.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/appunti/figure/2026-11-20-fig01.png")

# Schematic geometry: only the ordering (F below M) and the shared slope come from the audio.
SLOPE = 0.8
INTERCEPT_M = 1.0
INTERCEPT_F = 0.55
X_MAX = 1.0
Y_HEADROOM = 0.3
GAP_ARROW_X = 0.55
GAP_LABEL_OFFSET_X = 0.02
LINE_LABEL_X = 0.97
LINE_LABEL_OFFSET_Y = 0.04
# The F label sits below its line, which rises to the right, so it needs more room than M.
F_LABEL_DROP = 0.2
SLOPE_NOTE_X = 0.03
SLOPE_NOTE_OFFSET_Y = 0.45
SLOPE_NOTE_SIZE = 8.5
LINE_WIDTH = 1.6
ARROW_WIDTH = 0.9

x_values = np.array([0.0, X_MAX])
line_m = INTERCEPT_M + SLOPE * x_values
line_f = INTERCEPT_F + SLOPE * x_values
gap_top = INTERCEPT_M + SLOPE * GAP_ARROW_X
gap_bottom = INTERCEPT_F + SLOPE * GAP_ARROW_X

fig, ax = style.figure(height_ratio=0.55)
ax.plot(x_values, line_m, color=style.BLUE, lw=LINE_WIDTH)
ax.plot(x_values, line_f, color=style.RED, lw=LINE_WIDTH)
ax.text(LINE_LABEL_X, line_m[1] + LINE_LABEL_OFFSET_Y, "gruppo M", color=style.BLUE,
        ha="right", va="bottom")
ax.text(LINE_LABEL_X, line_f[1] - F_LABEL_DROP, "gruppo F", color=style.RED,
        ha="right", va="top")

ax.set_xlim(0, X_MAX)
ax.set_ylim(0, line_m[1] + Y_HEADROOM)
ax.set_xticks([])
ax.set_yticks([INTERCEPT_F, INTERCEPT_M])
ax.set_yticklabels([r"$\alpha + \beta_3$", r"$\alpha$"])
ax.set_xlabel("livello di istruzione")
ax.set_ylabel("salario")

ax.annotate("", xy=(GAP_ARROW_X, gap_bottom), xytext=(GAP_ARROW_X, gap_top),
            arrowprops=dict(arrowstyle="<->", color=style.DARK, lw=ARROW_WIDTH))
ax.text(GAP_ARROW_X + GAP_LABEL_OFFSET_X, (gap_top + gap_bottom) / 2, r"$\beta_3$",
        va="center", color=style.DARK)
ax.text(SLOPE_NOTE_X, line_m[0] + SLOPE_NOTE_OFFSET_Y, r"stessa pendenza $\beta_1$",
        color=style.GREY, fontsize=SLOPE_NOTE_SIZE, ha="left")
style.save(fig, OUT)
print(OUT)
