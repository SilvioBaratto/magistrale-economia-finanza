"""FSTR 04, slide 14: schema temporale del terminal value (t0..t3, business plan, NOPAT 2028)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Polygon, Rectangle

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-04/fig01.png")

# Coordinate in punti della slide (pagina 720 x 540, asse y verso il basso), lette dai tracciati
# vettoriali del PDF. S porta un punto della slide a pollici: la tela è larga 5,4 pollici.
W = style.WIDTH_IN
X0, X1 = 117.0, 692.0
Y0, Y1 = 183.0, 539.0
S = W / (X1 - X0)
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
    """Disegna un riquadro bianco con bordo scuro tra due angoli opposti (punti della slide)."""
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="white",
                           edgecolor=style.DARK, linewidth=LW, zorder=1))


def line(x, y, text, **kw):
    """Scrive una riga centrata su ``x`` con la linea di base a ``y`` (punti della slide)."""
    return ax.text(x, y, text, fontsize=FS, ha="center", va="baseline", color="black",
                   zorder=3, **kw)


# Asse del tempo: freccia vuota con contorno scuro, dall'origine fino a destra.
ax.add_patch(Polygon([(124.5, 221.14), (682.59, 221.14), (682.59, 218.18), (688.5, 224.10),
                      (682.59, 230.01), (682.59, 227.05), (124.5, 227.05)], closed=True,
                     facecolor="white", edgecolor=style.DARK, linewidth=LW,
                     joinstyle="miter", zorder=2))

# Istanti sopra l'asse. Le slide li posizionano a mano con scarti di qualche punto (e t0 più
# in basso): qui hanno passo uguale e stessa altezza, che è ciò che la scala dei tempi significa.
TICK_W, TICK_Y0, TICK_Y1 = 39.0, 187.4, 214.1
CENTERS = [235.5 + 66.0 * i for i in range(4)]
for i, c in enumerate(CENTERS):
    box(c - TICK_W / 2, TICK_Y0, c + TICK_W / 2, TICK_Y1)
    line(c, 206.2, rf"$t_{i}$")

# t0: bilancio di partenza.
box(120.0, 239.2, 255.0, 304.6)
for y, t in zip((257.9, 277.1, 296.3), ("Bilancio «actual»", "31/12/2025", "(oggi)")):
    line(187.5, y, t, fontweight="bold")

# t1-t3: business plan con tre flussi spuntati, il blocco spunta + etichetta è centrato.
BP_C = 363.0
box(273.02, 241.7, 453.01, 341.25)
line(BP_C, 260.4, "Business Plan:")
labels = ("FCFO 2026", "FCFO 2027", "FCFO 2028")
probe = ax.text(0, 0, labels[0], fontsize=FS)
fig.canvas.draw()
bb = probe.get_window_extent(fig.canvas.get_renderer()).transformed(ax.transData.inverted())
label_w = abs(bb.x1 - bb.x0)
probe.remove()
GAP = 22.6
left = BP_C - (GAP + label_w) / 2
for y, t in zip((279.6, 298.8, 318.0), labels):
    ax.text(left, y, r"$\checkmark$", fontsize=FS + 0.5, ha="left", va="baseline",
            color="black", zorder=3)
    ax.text(left + GAP, y, t, fontsize=FS, ha="left", va="baseline", color="black", zorder=3)

# Terminal value: NOPAT dell'ultimo anno esplicito e rendita da t3 all'infinito.
box(360.0, 365.6, 570.07, 411.7)
line(465.0, 384.3, "Calcolo il NOPAT dell’ultimo")
line(465.0, 403.5, "anno di previsione esplicita…")

box(360.01, 422.1, 453.01, 468.15)
line(406.5, 440.8, "NOPAT", fontweight="bold")
line(406.5, 460.0, "2028", fontweight="bold")

box(459.67, 422.1, 669.74, 468.15)
line(564.7, 440.8, r"Da $t_3$ all’infinito… quindi è il")
line(564.7, 460.0, "Terminal Value")

box(356.53, 508.6, 682.03, 535.3)
line(519.3, 527.4, "Se c’è crescita annua, allora applico (1+g)", fontstyle="italic")

style.save(fig, OUT)
