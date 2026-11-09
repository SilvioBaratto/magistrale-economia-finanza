"""FSTR 01, slide 30: Corporate Finance Circuit (attivo-impieghi, passivo-fonti, mercato dei capitali)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Ellipse, PathPatch, Polygon, Rectangle
from matplotlib.path import Path as MPath

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-01/fig04.png")

# Geometry read from the vector drawing of slide page 30 (slide points, y pointing down); K
# shrinks the 14 pt slide text to 9.5 pt so the scheme matches the other FSTR figures.
K = 0.68 / 72                    # pollici per punto della slide
W, H = style.WIDTH_IN, 3.15
CX, CY = 404.65, 325.2           # centro del contenuto nella slide
RED, BLUE, DARK = style.RED, style.BLUE, style.DARK
FS, FS_SMALL, FS_BOLD, FS_BOX = 9.5, 8.4, 8.2, 7.4

fig, ax = style.figure(figsize=(W, H), constrained_layout=False)
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(CX - W / K / 2, CX + W / K / 2)
ax.set_ylim(CY + H / K / 2, CY - H / K / 2)
ax.set_aspect("equal")

LW = 0.75 * 0.68 * 1.15
box = dict(facecolor="white", edgecolor=DARK, linewidth=LW, zorder=2)
ax.add_patch(Rectangle((207.63, 216), 89.37, 217, **box))          # attivo: C.I.N.
ax.add_patch(Rectangle((352.75, 216), 85.0, 217, **box))           # passivo: fonti
ax.add_patch(Rectangle((495, 189), 85.0, 42.63, **box))            # impieghi alternativi
ax.add_patch(Ellipse((541.5, 299.25), 102, 76.5, **box))           # mercato dei capitali


def arrow(points, color):
    """Filled arrow polygon given in slide coordinates."""
    ax.add_patch(Polygon(points, closed=True, facecolor=color, edgecolor="none", zorder=4))


arrow([(489.37, 297.03), (450.51, 281.19), (452.77, 275.63), (491.63, 291.47)], RED)
arrow([(451.02, 287.88), (437.75, 272.75), (457.82, 271.21)], RED)
arrow([(491.55, 308.82), (448.68, 335.31), (451.84, 340.42), (494.70, 313.93)], RED)
arrow([(448.08, 328.63), (437.5, 345.75), (457.54, 343.94)], RED)
arrow([(353.25, 316.5), (312, 316.5), (312, 322.5), (353.25, 322.5)], RED)
arrow([(315, 310.5), (297, 319.5), (315, 328.5)], RED)
arrow([(540.37, 256.5), (540.37, 239), (539.62, 239), (539.62, 256.5)], RED)
arrow([(543, 240), (540, 234), (537, 240)], RED)

arrow([(207.88, 312), (189.88, 321), (207.88, 330)], BLUE)
arrow([(192, 319.5), (192, 435), (186, 435), (186, 319.5)], BLUE)
arrow([(198, 432), (189, 450), (180, 432)], BLUE)
arrow([(189, 453), (430.5, 453), (430.5, 447), (189, 447)], BLUE)
arrow([(427.5, 459), (445.5, 450), (427.5, 441)], BLUE)
arrow([(448.22, 451.26), (500.40, 338.87), (494.96, 336.34), (442.78, 448.74)], BLUE)
arrow([(504.58, 344.12), (504, 324), (488.26, 336.54)], BLUE)


def curved(spec):
    """Outlined circular arrow from a flipped-y path (move, line and cubic segments)."""
    verts, codes = [], []
    for op, *pts in spec:
        code = {"M": MPath.MOVETO, "L": MPath.LINETO, "C": MPath.CURVE4}[op]
        for p in pts:
            verts.append((p[0], 540 - p[1]))
            codes.append(code)
    verts.append(verts[0])
    codes.append(MPath.CLOSEPOLY)
    ax.add_patch(PathPatch(MPath(verts, codes), facecolor="white", edgecolor=DARK,
                           linewidth=LW, zorder=3))


curved([("M", (269.69, 266.38)),
        ("C", (269.69, 272.83), (263.5, 278.06), (255.87, 278.06)),
        ("C", (248.24, 278.06), (242.06, 272.83), (242.06, 266.38)),
        ("L", (228.25, 266.38)),
        ("C", (228.25, 279.29), (240.62, 289.75), (255.87, 289.75)),
        ("C", (271.13, 289.75), (283.5, 279.29), (283.5, 266.38)),
        ("L", (290.41, 266.38)), ("L", (276.59, 254.69)), ("L", (262.78, 266.38))])
curved([("M", (242.06, 162.88)),
        ("C", (242.06, 156.42), (248.25, 151.19), (255.87, 151.19)),
        ("C", (263.51, 151.19), (269.69, 156.42), (269.69, 162.88)),
        ("L", (283.5, 162.87)),
        ("C", (283.5, 149.96), (271.13, 139.5), (255.87, 139.5)),
        ("C", (240.62, 139.5), (228.25, 149.96), (228.25, 162.87)),
        ("L", (221.34, 162.88)), ("L", (235.16, 174.56)), ("L", (248.97, 162.88))])


def text(x, y, s, size=FS, color=DARK, weight="normal", ha="center"):
    """Place a label whose vertical centre is at y, in slide coordinates."""
    ax.text(x, y, s, ha=ha, va="center", fontsize=size, color=color, fontweight=weight,
            zorder=5)


text(249.8, 174.0, "ATTIVO-IMPIEGHI", size=FS_BOLD, weight="bold")
text(393.85, 174.0, "PASSIVO-FONTI", size=FS_BOLD, weight="bold")
text(249.7, 198.4, "Attese")
text(393.8, 198.4, "Diritti contingenti")
text(537.5, 202.5, "Impieghi")
text(537.5, 218.7, "alternativi")
text(393.7, 239.5, "CREDITORI", size=FS_BOX, weight="bold")
text(393.7, 263.0, "Debiti")
text(393.7, 287.2, "finanziari")
text(252.4, 316.7, "C.I.N.")
text(252.3, 332.9, "al lavoro")
text(541.5, 291.5, "Mercato")
text(541.5, 307.7, "dei capitali")
text(393.1, 361.1, "AZIONISTI", size=FS_BOX, weight="bold")
text(393.1, 382.7, "Mezzi", size=FS_SMALL)
text(393.1, 406.2, "propri", size=FS_SMALL + 0.8)
for x0, x1, y in ((360.8, 426.6, 245.1), (363.5, 422.6, 366.65)):
    ax.plot([x0, x1], [y, y], color=DARK, lw=0.6, solid_capstyle="butt", zorder=5)

text(510.0, 387.3, "INVESTIMENTI", size=FS_BOLD, color=RED, weight="bold", ha="left")
text(510.0, 421.3, "REMUNERAZIONE", size=FS_BOLD, color=BLUE, weight="bold", ha="left")
text(320.1, 472.1, "FLUSSI DI CASSA GENERATI", size=FS_BOLD, color=BLUE, weight="bold")

fig.add_artist(Rectangle((0, 0), 1, 1, transform=fig.transFigure, facecolor="white",
                         edgecolor="none", zorder=-10))
style.save(fig, OUT)
