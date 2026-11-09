"""FSTR 07, slide 15: value maps in ottica equity (P/BV su ROE) e assets (EV/CIN su ROI)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Rectangle

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-07/fig02.png")

# Coordinate normalizzate sul riquadro degli assi della slide: le slide 15, 16 e 17
# riusano la stessa nuvola di dieci punti e la stessa retta.
POINTS = [(0.10, 0.32), (0.20, 0.40), (0.33, 0.36), (0.41, 0.67), (0.49, 0.44),
          (0.62, 0.69), (0.70, 0.40), (0.75, 0.72), (0.86, 0.96), (0.93, 0.83)]
LINE = ((0.04, 0.28), (0.99, 0.77))

# Stesse dimensioni di pannello nelle tre figure delle value maps: la tela e' larga
# quanto la pagina, cosi' il testo ha la stessa scala anche con un solo pannello.
W, H = style.WIDTH_IN, 2.55
PANEL_W, PANEL_H = 2.05, 1.95
XLIM, YLIM = (0, 1.09), (0, 1.09)


def draw_panel(ax, left, title, ylabel, xlabel):
    """Disegna uno scatter concettuale (senza scala) con retta di regressione."""
    ax.set_position([left / W, 0.30 / H, PANEL_W / W, PANEL_H / H])
    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.axis("off")
    arrow = dict(arrowstyle="-|>", color=style.DARK, lw=1.2, shrinkA=0, shrinkB=0,
                 mutation_scale=9)
    ax.annotate("", xy=(1.04, 0), xytext=(0, 0), arrowprops=arrow, annotation_clip=False)
    ax.annotate("", xy=(0, 1.04), xytext=(0, 0), arrowprops=arrow, annotation_clip=False)
    (x0, y0), (x1, y1) = LINE
    ax.plot([x0, x1], [y0, y1], color=style.RED, lw=1.4, zorder=3, solid_capstyle="round")
    ax.scatter(*zip(*POINTS), s=62, color=style.BLUE, edgecolors="white", linewidths=0.7,
               zorder=2, clip_on=False)
    ax.text(-0.03, 1.05, ylabel, ha="right", va="top", fontsize=9.5)
    ax.text(1.04, -0.04, xlabel, ha="right", va="top", fontsize=9.5)
    ax.text(0.54, 1.09, title, ha="center", va="bottom", fontsize=10.5, fontweight="bold")


fig, axes = style.figure(ncols=2, figsize=(W, H), constrained_layout=False)
draw_panel(axes[0], 0.55, "Ottica Equity", "P/BV", "ROE")
draw_panel(axes[1], 3.15, "Ottica Assets", "EV/CIN", "ROI")
fig.add_artist(Rectangle((0, 0), 1, 1, transform=fig.transFigure, facecolor="white",
                         edgecolor="none", zorder=-10))
style.save(fig, OUT)
