"""FSTR 02, slide 4: schema Assets / Equity / Debts e formula del WACC."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Rectangle, Polygon, PathPatch
from matplotlib.path import Path as MPath

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-02/fig01.png")

BLOCK = "#EFC58F"   # arancione della slide, schiarito per stare accanto alla palette
ARROW = "#C08A2B"   # ambra della palette
BRACE = style.BLUE

# Geometria in punti della slide, origine nell'angolo in alto a sinistra di ASSETS, y verso il basso.
XMIN, XMAX = -112.0, 458.0
YMIN, YMAX = -3.0, 336.0
W = 5.3
K = W / (XMAX - XMIN)
H = (YMAX - YMIN) * K


def X(x):
    """Converte un'ascissa in punti della slide nelle coordinate (pollici) degli assi."""
    return (x - XMIN) * K


def Y(y):
    """Converte un'ordinata in punti della slide (verso il basso) nelle coordinate degli assi."""
    return (YMAX - y) * K


fig, ax = style.figure(figsize=(W, H), constrained_layout=False)
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# blocchi: ASSETS a tutta altezza, EQUITY (40%) sopra DEBTS (60%)
HT, WA, WR, SPLIT = 197.0, 170.0, 169.0, 78.0


def block(x0, y0, x1, y1, label):
    """Disegna un riquadro con la sua etichetta centrata; gli estremi sono in punti della slide."""
    ax.add_patch(Rectangle((X(x0), Y(y1)), (x1 - x0) * K, (y1 - y0) * K,
                           facecolor=BLOCK, edgecolor=style.DARK, linewidth=0.6))
    ax.text(X((x0 + x1) / 2), Y((y0 + y1) / 2), label, fontweight="bold",
            fontsize=9, ha="center", va="center", color="black")


block(0, 0, WA, HT, "ASSETS")
block(WA, 0, WA + WR, SPLIT, "EQUITY")
block(WA, SPLIT, WA + WR, HT, "DEBTS")


def brace(x_end, x_body, x_tip, y0, y1):
    """Graffa che parte dal lato dei blocchi (x_end) e punta verso x_tip."""
    s = 1.0 if x_body > x_end else -1.0
    r = abs(x_body - x_end)
    ym = (y0 + y1) / 2
    pts = [
        (x_end, y0),
        (x_end + s * 0.55 * r, y0), (x_body, y0 + 1.8), (x_body, y0 + 4.0),
        (x_body, ym - 4.0),
        (x_body, ym - 1.8), (x_body + 0.55 * (x_tip - x_body), ym), (x_tip, ym),
        (x_body + 0.55 * (x_tip - x_body), ym), (x_body, ym + 1.8), (x_body, ym + 4.0),
        (x_body, y1 - 4.0),
        (x_body, y1 - 1.8), (x_end + s * 0.55 * r, y1), (x_end, y1),
    ]
    codes = [MPath.MOVETO,
             MPath.CURVE4, MPath.CURVE4, MPath.CURVE4,
             MPath.LINETO,
             MPath.CURVE4, MPath.CURVE4, MPath.CURVE4,
             MPath.CURVE4, MPath.CURVE4, MPath.CURVE4,
             MPath.LINETO,
             MPath.CURVE4, MPath.CURVE4, MPath.CURVE4]
    path = MPath([(X(x), Y(y)) for x, y in pts], codes)
    ax.add_patch(PathPatch(path, facecolor="none", edgecolor=BRACE, linewidth=1.3,
                           capstyle="round"))


# WACC sull'intero attivo; r_E sull'equity; r_D sul debito
brace(-12.0, -36.0, -60.0, 0, HT)
brace(WA + WR + 13.0, WA + WR + 38.0, WA + WR + 63.0, 1.0, SPLIT - 1.5)
brace(WA + WR + 13.0, WA + WR + 38.0, WA + WR + 63.0, SPLIT + 1.5, HT - 1.0)
ax.text(X(-68), Y(HT / 2), "WACC", fontsize=10.5, ha="right", va="center")
ax.text(X(WA + WR + 78), Y(SPLIT / 2), "$r_E$", fontsize=11, ha="left", va="center")
ax.text(X(WA + WR + 78), Y((SPLIT + HT) / 2), "$r_D$", fontsize=11, ha="left", va="center")

# formula composta a pezzi, così da conoscere la posizione di r_E e r_D(1 - t_c)
FF = 13.0
BASE = Y(247.0)
pieces = [
    r"$\mathit{WACC}\;=$",
    r"$r_E$",
    r"$\dfrac{E}{E+D}$",
    r"$+$",
    r"$r_D(1-t_c)$",
    r"$\dfrac{D}{E+D}$",
]
GAP = 0.07
renderer = fig.canvas.get_renderer()
texts, widths = [], []
for s in pieces:
    t = ax.text(0, BASE, s, fontsize=FF, ha="left", va="baseline")
    widths.append(t.get_window_extent(renderer).width / fig.dpi)
    texts.append(t)
total = sum(widths) + GAP * (len(pieces) - 1)
x = X(WA) - total / 2
centers = []
for t, w in zip(texts, widths):
    t.set_x(x)
    centers.append(x + w / 2)
    x += w + GAP

# frecce verso l'origine dei due tassi
HEAD_W, STEM_W, HEAD_H, ARROW_H = 31.0, 15.5, 15.5, 40.0
TOP = 266.0
for cx, label in ((centers[1], "CAPM"), (centers[4], "Tasso prestiti")):
    hw, sw = HEAD_W * K / 2, STEM_W * K / 2
    yt, yh, yb = Y(TOP), Y(TOP + ARROW_H - HEAD_H), Y(TOP + ARROW_H)
    ax.add_patch(Polygon([(cx - sw, yt), (cx + sw, yt), (cx + sw, yh), (cx + hw, yh),
                          (cx, yb), (cx - hw, yh), (cx - sw, yh)],
                         closed=True, facecolor=ARROW, edgecolor="none"))
    ax.text(cx, Y(TOP + ARROW_H + 16), label, fontsize=10, ha="center", va="center")

style.save(fig, OUT)
