import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib import font_manager
from matplotlib.patches import Rectangle

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-03/fig02.png")

for n in ("lmmono10-regular", "lmsans10-regular"):
    font_manager.fontManager.addfont(f"{style.LM_DIR}/{n}.otf")

# Layout in the original's pixel space (1650 x 690), y pointing down.
fig, ax = style.figure(height_ratio=690 / 1650, constrained_layout=False)
ax.set_xlim(40, 1620)
ax.set_ylim(670, 20)
ax.axis("off")

boxes = {
    "income": (72, 290, 385, 397),
    "average score": (903, 38, 1582, 166),
    "class size": (945, 540, 1466, 645),
}
for text, (x0, y0, x1, y1) in boxes.items():
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, ec=style.DARK, lw=0.8))
    ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 4, text, family="Latin Modern Mono",
            ha="center", va="center", fontsize=15.5, color=style.DARK)

arrow = dict(arrowstyle="-|>,head_length=0.5,head_width=0.18", color=style.DARK,
             lw=0.8, shrinkA=0, shrinkB=0)
for a, b in (((400, 342), (860, 115)), ((400, 365), (860, 590)), ((1190, 487), (1190, 195))):
    ax.annotate("", xy=b, xytext=a, arrowprops=arrow)

for s, xy in (("(0.7124)", (545, 185)), ("(-0.2322)", (530, 515)), ("(-0.2264)", (1365, 350))):
    ax.text(*xy, s, family="Latin Modern Sans", ha="center", va="center",
            fontsize=12.5, color=style.DARK)

style.save(fig, OUT)
