"""FSTR 12, slide 6: premio massimo nell'acquisizione (valore stand alone, premio e scalinata delle sinergie)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Polygon, Rectangle

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-12/fig01.png")

PREMIUM = "#EBD7A8"   # premio (giallo nella slide), stessa tinta ocra del patrimonio netto in FSTR 07
STAND_ALONE = style.LIGHT   # blocco del valore stand alone (grigio chiaro nella slide)

# Coordinate nei punti della slide (720 x 540, vettoriale); l'asse y cresce verso il basso come nel
# PDF. S porta un punto della slide a pollici: con 0,0094 le etichette da 9,5 pt corrispondono ai
# 14 pt del corpo della slide.
S = 0.0094
W = style.WIDTH_IN
CX = 449.0                              # centro orizzontale del disegno nella slide
X0, X1 = CX - W / S / 2, CX + W / S / 2
Y0, Y1 = 111.0, 450.0
H = (Y1 - Y0) * S
FS = 9.5
FS_PREMIUM = 8.5
FS_STOP = 12.5
LW_BLOCK = 1.5
LW = 0.8

fig, ax = style.figure(figsize=(W, H), constrained_layout=False)
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(X0, X1)
ax.set_ylim(Y1, Y0)

# Rettangolo bianco a tutta tela: impedisce a bbox_inches="tight" di ritagliare la tela,
# così il filtro che scala le immagini tratta questa figura come le altre di FSTR.
ax.add_patch(Rectangle((X0, Y0), X1 - X0, Y1 - Y0, facecolor="white", edgecolor="none", zorder=0))

# Nella slide blocchi, linee e gradini di uno stesso livello differiscono di circa 1,5 pt per
# imprecisione del disegno: qui coincidono, perché rappresentano lo stesso livello.
Y_TOP = 171.1       # sommità del blocco del premio e del gradino delle sinergie finanziarie
Y_MID = 292.5       # sommità del valore stand alone, base del premio e del gradino fiscale
Y_BOT = 446.6       # base del valore stand alone
X_BLK0, X_BLK1 = 249.1, 339.3

STEPS = [   # (etichetta, x0, x1, y alto, y basso): ogni gradino sta più in alto e più a destra
    ("Sinergie fiscali", 411.9, 574.8, 259.4, Y_MID),
    ("Sinergie operative", 464.6, 627.5, 217.1, 259.4),
    ("Sinergie finanziarie", 486.1, 649.0, Y_TOP, 217.1),
]


def box(x0, y0, x1, y1, facecolor="white", lw=LW):
    """Disegna un riquadro con bordo scuro tra due angoli opposti (punti della slide)."""
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=facecolor,
                           edgecolor=style.DARK, linewidth=lw, joinstyle="miter", zorder=2))


def extent(text):
    """Larghezza e centro orizzontale del testo, in punti della slide."""
    fig.canvas.draw()
    bb = text.get_window_extent(fig.canvas.get_renderer()).transformed(ax.transData.inverted())
    return abs(bb.x1 - bb.x0), (bb.x0 + bb.x1) / 2


def run(parts, center, y, size=FS):
    """Dispone in riga più testi (stile ``(testo, corsivo)``) centrando la riga su ``center``."""
    texts = [ax.text(0, y, t, fontsize=size, fontstyle="italic" if it else "normal", ha="left",
                     va="center", color="black", zorder=4) for t, it in parts]
    widths = [extent(t)[0] for t in texts]
    gap = 0.28 * size / (S * 72)         # spazio tra parole, in punti della slide
    x = center - (sum(widths) + gap * (len(parts) - 1)) / 2
    for t, w in zip(texts, widths):
        t.set_x(x)
        x += w + gap


# Linee tratteggiate che portano i due livelli fino ai gradini, sotto ai riquadri.
for y, x_end in ((Y_MID, STEPS[0][1]), (Y_TOP, STEPS[2][1])):
    ax.plot([X_BLK1, x_end], [y, y], color=style.DARK, lw=1.1, ls=(0, (1.1, 1.1)),
            solid_capstyle="butt", zorder=1)

# Colonna di sinistra: valore stand alone in basso, premio sopra.
box(X_BLK0, Y_MID, X_BLK1, Y_BOT, STAND_ALONE, LW_BLOCK)
box(X_BLK0, Y_TOP, X_BLK1, Y_MID, PREMIUM, LW_BLOCK)
xc = (X_BLK0 + X_BLK1) / 2
ax.text(xc, 372, "Equity\ndel target", fontsize=FS, ha="center", va="center", linespacing=1.25,
        color="black", zorder=4)
ax.text(xc, 233, "Premio\nper\nl’acquisizione", fontsize=FS_PREMIUM, ha="center", va="center",
        linespacing=1.3, color="black", zorder=4)

# Riquadro che nomina il blocco grigio.
box(356.0, 347.4, 518.9, 377.75)
run([("Valore", False), ("stand alone", True)], 437.4, 362.9)

# Scalinata delle tre sinergie.
for label, x0, x1, y0, y1 in STEPS:
    box(x0, y0, x1, y1)
    ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 0.6, label, fontsize=FS, ha="center", va="center",
            color="black", zorder=4)

# Segnale di stop: poligoni della slide, già portati nel sistema di coordinate dei punti della slide.
POLE = [[(382.85, 204.44), (390.56, 204.44), (390.56, 156.04), (382.85, 156.04)],
        [(383.68, 204.44), (389.73, 204.44), (389.73, 156.04), (383.68, 156.04)],
        [(384.5, 204.44), (388.85, 204.44), (388.85, 156.04), (384.5, 156.04)]]
for pts, color in zip(POLE, (style.GREY, style.LIGHT, style.GREY)):
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor=style.DARK, linewidth=0.5,
                         joinstyle="miter", zorder=3))

OCTAGON = [(354.09, 130.88), (374.0, 115.42), (399.41, 115.42), (419.32, 130.88),
           (419.32, 153.17), (399.41, 169.6), (374.0, 169.6), (354.09, 153.17)]
RING = [(358.48, 132.44), (375.71, 119.09), (397.7, 119.09), (414.93, 132.44),
        (414.93, 151.69), (397.7, 165.89), (375.71, 165.89), (358.48, 151.69)]
LETTERS = [   # P, O, S, T con i rispettivi occhielli rossi
    [(400.49, 130.63), (408.3, 130.63), (411.62, 134.25), (411.62, 142.59), (408.3, 146.18),
     (405.04, 146.18), (405.04, 153.38), (400.49, 153.38)],
    [(389.78, 130.63), (395.11, 130.63), (398.42, 134.25), (398.42, 149.76), (395.11, 153.38),
     (389.78, 153.38), (386.47, 150.13), (386.47, 134.25)],
    [(364.64, 130.63), (369.61, 130.63), (372.92, 134.25), (372.92, 138.25), (368.78, 138.25),
     (368.78, 135.3), (365.88, 135.3), (365.88, 140.4), (369.61, 140.4), (372.92, 143.31),
     (372.92, 150.13), (370.02, 153.38), (364.64, 153.38), (361.8, 150.13), (361.8, 146.18),
     (365.88, 146.18), (365.88, 149.04), (368.78, 149.04), (368.78, 143.98), (365.05, 143.98),
     (361.8, 141.12), (361.8, 134.25)],
    [(374.98, 130.63), (385.23, 130.63), (385.23, 135.3), (382.38, 135.3), (382.38, 153.38),
     (377.88, 153.38), (377.88, 135.3), (374.98, 135.3)],
]
HOLES = [[(391.03, 148.7), (393.92, 148.7), (393.92, 135.3), (391.03, 135.3)],
         [(405.04, 141.5), (407.53, 141.5), (407.53, 135.31), (405.04, 135.31)]]

ax.add_patch(Polygon(OCTAGON, closed=True, facecolor=style.RED, edgecolor=style.DARK,
                     linewidth=0.8, joinstyle="miter", zorder=5))
# Filetto bianco interno, con bordo scuro ai due lati come nella slide.
ax.add_patch(Polygon(RING, closed=True, facecolor="none", edgecolor=style.DARK, linewidth=2.6,
                     joinstyle="miter", zorder=5))
ax.add_patch(Polygon(RING, closed=True, facecolor="none", edgecolor="white", linewidth=1.3,
                     joinstyle="miter", zorder=6))
for pts in LETTERS:
    ax.add_patch(Polygon(pts, closed=True, facecolor="white", edgecolor=style.DARK,
                         linewidth=0.5, joinstyle="miter", zorder=7))
for pts in HOLES:
    ax.add_patch(Polygon(pts, closed=True, facecolor=style.RED, edgecolor=style.DARK,
                         linewidth=0.5, joinstyle="miter", zorder=8))

ax.text(425.9, 161.35, "Premio massimo!", fontsize=FS_STOP, fontweight="bold", color=style.BLUE,
        ha="left", va="baseline", zorder=4)

style.save(fig, OUT)
