"""Appunti FSTR 2026-11-20: the lecturer's "house" example, enterprise value against PFN.

Rebuilt from the audio, not the slide: the lecturer's own sketch is not in the slides.
Numbers stated aloud: enterprise value 100 in every case; accounting assets 60 (cases A and B);
case A PFN 45 so the transfer is 55; case B no debt and no cash so the transfer is 100; case C
cash of 10 inside the company so the transfer is 110.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/appunti/figure/2026-11-20-fig01.png")

ENTERPRISE_VALUE = 100
ACCOUNTING_ASSETS = 60
DEBT_CASE_A = 45
CASH_CASE_C = 10
Y_AXIS_TOP = 125
BAR_WIDTH = 0.6
EDGE_WIDTH = 0.8
LABEL_SIZE = 8
X_MARGIN = 0.6
LABEL_GAP = 0.05
TOTAL_LABEL_OFFSET = 4
LIGHT_BLUE = "#A9C2CC"
# White text on the dark fills, dark text on the light ones.
DARK_FILLS = (style.BLUE, style.DARK, style.GREY)

fig, axes = style.figure(ncols=3, height_ratio=0.62, sharey=True)


def draw_bar(ax, x_position, bottom, height, color, label):
    """Draw one stacked segment with its label centred inside.

    Args:
        ax: Axes to draw on.
        x_position: Horizontal centre of the bar.
        bottom: Value where the segment starts.
        height: Value spanned by the segment.
        color: Fill colour; the label turns white on dark fills.
        label: Text centred in the segment.
    """
    ax.bar(x_position, height, bottom=bottom, width=BAR_WIDTH, color=color,
           edgecolor=style.DARK, linewidth=EDGE_WIDTH)
    ax.text(x_position, bottom + height / 2, label, ha="center", va="center",
            fontsize=LABEL_SIZE, color="white" if color in DARK_FILLS else style.DARK)


case_a, case_b, case_c = axes

draw_bar(case_a, 0, 0, ACCOUNTING_ASSETS, style.LIGHT, str(ACCOUNTING_ASSETS))
draw_bar(case_a, 1, 0, DEBT_CASE_A, style.GREY, f"PFN\n{DEBT_CASE_A}")
draw_bar(case_a, 1, DEBT_CASE_A, ENTERPRISE_VALUE - DEBT_CASE_A, style.BLUE,
         f"Bonifico\n{ENTERPRISE_VALUE - DEBT_CASE_A}")
case_a.set_title("Caso A: PFN positiva")

draw_bar(case_b, 0, 0, ACCOUNTING_ASSETS, style.LIGHT, str(ACCOUNTING_ASSETS))
draw_bar(case_b, 1, 0, ENTERPRISE_VALUE, style.BLUE, f"Bonifico\n{ENTERPRISE_VALUE}")
case_b.set_title("Caso B: PFN nulla")

draw_bar(case_c, 1, 0, ENTERPRISE_VALUE, style.BLUE, str(ENTERPRISE_VALUE))
draw_bar(case_c, 1, ENTERPRISE_VALUE, CASH_CASE_C, LIGHT_BLUE, "")
# The cash segment is too thin to hold its label, so it sits beside the bar.
case_c.text(1 - BAR_WIDTH / 2 - LABEL_GAP, ENTERPRISE_VALUE + CASH_CASE_C / 2,
            f"Cassa {CASH_CASE_C}", ha="right", va="center", fontsize=LABEL_SIZE,
            color=style.DARK)
case_c.text(1, ENTERPRISE_VALUE + CASH_CASE_C + TOTAL_LABEL_OFFSET,
            f"Bonifico {ENTERPRISE_VALUE + CASH_CASE_C}", ha="center", va="bottom",
            fontsize=LABEL_SIZE, color=style.DARK)
case_c.set_title("Caso C: cassa")

for ax in (case_a, case_b):
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Attivo\ncontabile", "Enterprise\nvalue"])
case_c.set_xticks([1])
case_c.set_xticklabels(["Enterprise\nvalue"])
for ax in axes:
    ax.set_xlim(-X_MARGIN, 1 + X_MARGIN)
    ax.set_ylim(0, Y_AXIS_TOP)
case_a.set_ylabel("Valore")

style.save(fig, OUT)
