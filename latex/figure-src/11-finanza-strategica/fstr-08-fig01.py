"""FSTR 08, slide 5: Enterprise Value, Equity Value e Debt (PFN), con E.V. = EBITDA x multiplo."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Ellipse, Polygon, Rectangle

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-08/fig01.png")

ARROW = "#B7CDD5"    # freccia azzurro chiaro della slide (stessa tinta dell'EV in FSTR 07)

# Coordinate nei pixel della slide renderizzata a 150 dpi (1500 x 1125); l'asse y è
# invertito come nell'immagine. S è la scala che porta un pixel della slide a pollici.
S = 0.0038
W = style.WIDTH_IN
CX = 793.5                              # centro orizzontale del disegno nella slide
X0, X1 = CX - W / S / 2, CX + W / S / 2
Y0, Y1 = 205, 1085
H = (Y1 - Y0) * S
FS = 9.5
LW = 0.8

fig, ax = style.figure(figsize=(W, H), constrained_layout=False)
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(X0, X1)
ax.set_ylim(Y1, Y0)

# Rettangolo bianco a tutta tela: impedisce a bbox_inches="tight" di ritagliare la tela,
# così il filtro che scala le immagini tratta questa figura come le altre di FSTR.
ax.add_patch(Rectangle((X0, Y0), X1 - X0, Y1 - Y0, facecolor="white", edgecolor="none", zorder=0))


def box(x0, y0, x1, y1):
    """Disegna un riquadro bianco con bordo scuro tra due angoli opposti (pixel della slide)."""
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="white",
                           edgecolor=style.DARK, linewidth=LW, zorder=1))


def extent(text):
    """Larghezza e centro orizzontale del testo, in pixel della slide."""
    fig.canvas.draw()
    bb = text.get_window_extent(fig.canvas.get_renderer()).transformed(ax.transData.inverted())
    return abs(bb.x1 - bb.x0), (bb.x0 + bb.x1) / 2


def run(parts, gaps, center, y):
    """Dispone in riga più testi con spazi dati in pixel della slide, centrando la riga."""
    texts = [ax.text(0, y, t, fontsize=FS, ha="left", va="center", color="black", zorder=3)
             for t in parts]
    widths = [extent(t)[0] for t in texts]
    x = center - (sum(widths) + sum(gaps)) / 2
    for t, w, g in zip(texts, widths, gaps + [0]):
        t.set_x(x)
        x += w + g
    return texts, widths


def circle(text, y, h, pad):
    """Cerchia in rosso un testo: ellisse centrata sul testo, larga quanto lui più ``pad``, alta ``h``."""
    w, c = extent(text)
    ax.add_patch(Ellipse((c, y), w + pad, h, facecolor="none", edgecolor=style.RED,
                         linewidth=1.3, zorder=4))


# Enterprise Value a sinistra; a destra Equity Value sopra e Debt (PFN) sotto, stessa altezza.
TOP, BOT = 219, 787
box(476, TOP, 814, BOT)
box(837, TOP, 1237, BOT)
ax.plot([837, 1237], [466, 466], color=style.DARK, lw=LW, solid_capstyle="butt", zorder=2)

ax.text(645, 510, "ENTERPRISE\nVALUE (E.V.)", fontsize=FS, ha="center", va="center",
        linespacing=1.55, color="black", zorder=3)
ax.text(1037, 345, "EQUITY VALUE", fontsize=FS, ha="center", va="center", color="black", zorder=3)
(debt, pfn), _ = run(["DEBT", "(PFN)"], [31], 1037, 628)
circle(pfn, 631, 84, 38)

# Formula in basso e freccia che sale verso l'Enterprise Value.
box(350, 966, 967, 1071)
(_, ebitda, _, _), _ = run(["E.V. =", "EBITDA", "×", "multiplo"], [50, 52, 42], 658, 1020)
circle(ebitda, 1020, 78, 30)

ax.add_patch(Polygon([(645, 812), (684, 852), (665, 852), (665, 950), (625, 950),
                      (625, 852), (606, 852)], closed=True, facecolor=ARROW,
                     edgecolor=style.BLUE, linewidth=0.6, joinstyle="miter", zorder=2))

style.save(fig, OUT)
