"""Appunti FSTR 2026-11-24: weight of the terminal value on the enterprise value.

Rebuilt from the audio, not the slide: the lecturer shows the picture on screen and describes it
with the numbers of an example. Numbers stated aloud: enterprise value 10 million; the four years
of business plan give 1 million of cash flows; the discounted terminal value gives 9 million.
The lecturer calls the terminal-value region "la zona arancione".
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/appunti/figure/2026-11-24-fig01.png")

BUSINESS_PLAN_MILLIONS = 1
TERMINAL_VALUE_MILLIONS = 9
ENTERPRISE_VALUE_MILLIONS = BUSINESS_PLAN_MILLIONS + TERMINAL_VALUE_MILLIONS
Y_AXIS_TOP = 11.5
BAR_WIDTH = 0.5
EDGE_WIDTH = 0.8
LABEL_SIZE = 9
TOTAL_LABEL_OFFSET = 0.3
ORANGE = style.PALETTE[4]

fig, ax = style.figure(height_ratio=0.55)

ax.bar(0, BUSINESS_PLAN_MILLIONS, width=BAR_WIDTH, color=style.BLUE,
       edgecolor=style.DARK, linewidth=EDGE_WIDTH)
ax.bar(0, TERMINAL_VALUE_MILLIONS, bottom=BUSINESS_PLAN_MILLIONS, width=BAR_WIDTH, color=ORANGE,
       edgecolor=style.DARK, linewidth=EDGE_WIDTH)

# The business-plan slice is too thin to hold its label, so it sits beside the bar.
ax.text(BAR_WIDTH / 2 + 0.05, BUSINESS_PLAN_MILLIONS / 2,
        f"Business plan (quattro anni): {BUSINESS_PLAN_MILLIONS}", ha="left", va="center",
        fontsize=LABEL_SIZE, color=style.DARK)
ax.text(0, BUSINESS_PLAN_MILLIONS + TERMINAL_VALUE_MILLIONS / 2,
        f"Terminal value\nattualizzato\n{TERMINAL_VALUE_MILLIONS}", ha="center", va="center",
        fontsize=LABEL_SIZE, color="white")
ax.text(0, ENTERPRISE_VALUE_MILLIONS + TOTAL_LABEL_OFFSET,
        f"Enterprise value: {ENTERPRISE_VALUE_MILLIONS}", ha="center", va="bottom",
        fontsize=LABEL_SIZE, color=style.DARK)

ax.set_xlim(-0.6, 1.9)
ax.set_ylim(0, Y_AXIS_TOP)
ax.set_xticks([])
ax.set_ylabel("Milioni")

style.save(fig, OUT)
