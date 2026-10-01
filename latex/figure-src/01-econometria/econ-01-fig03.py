import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib import font_manager
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-01/fig03.png")
for f in ("lmmono10-regular.otf", "lmsans10-regular.otf"):
    font_manager.fontManager.addfont(str(style.LM_DIR / f))

fig, ax = style.figure(figsize=(style.WIDTH_IN, style.WIDTH_IN * 330 / 830))
ax.set_xlim(0, 830)
ax.set_ylim(330, 0)
ax.axis("off")

def box(x0, y0, x1, y1, text):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, ec="black", lw=1.0))
    ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 2, text, family="Latin Modern Mono",
            ha="center", va="center", fontsize=15, color="black")

box(27, 145, 186, 195, "income")
box(441, 25, 780, 80, "average score")
box(464, 265, 722, 318, "class size")

def arrow(p, q):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(
        arrowstyle="-|>,head_width=0.18,head_length=0.45", color="black", lw=0.9,
        shrinkA=0, shrinkB=0))

arrow((190, 168), (422, 58))
arrow((190, 178), (422, 292))
arrow((587, 240), (587, 98))

kw = dict(family="Latin Modern Sans", fontsize=13, ha="center", va="center", color="black")
ax.text(262, 90, "(0.7124)", **kw)
ax.text(255, 255, "(-0.2322)", **kw)
ax.text(675, 172, "(-0.2264)", **kw)
style.save(fig, OUT)
