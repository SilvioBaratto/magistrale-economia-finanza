"""FSTR 02, slide 25: schemi del beta unlevered con PFN positiva e PFN negativa."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Rectangle, FancyBboxPatch

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-02/fig02.png")

BLOCK = "#EFC58F"   # arancione della slide, schiarito per stare accanto alla palette
BOX = "#1C1C1C"     # riquadro nero delle intestazioni

# Geometria in punti della slide, y verso il basso.
XMIN, XMAX = 117.0, 700.0
YMIN, YMAX = 112.0, 496.0
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


def block(x0, y0, x1, y1, label):
    """Disegna un riquadro con la sua etichetta centrata; gli estremi sono in punti della slide."""
    ax.add_patch(Rectangle((X(x0), Y(y1)), (x1 - x0) * K, (y1 - y0) * K,
                           facecolor=BLOCK, edgecolor=style.DARK, linewidth=0.6))
    ax.text(X((x0 + x1) / 2), Y((y0 + y1) / 2), label, fontweight="bold",
            fontsize=8.5, ha="center", va="center", color="black")


def header(x0, x1, y0, y1, text):
    """Disegna il riquadro nero ad angoli arrotondati con il testo bianco su tre righe."""
    r = 17.3 * K
    ax.add_patch(FancyBboxPatch((X(x0) + r, Y(y1) + r), (x1 - x0) * K - 2 * r, (y1 - y0) * K - 2 * r,
                                boxstyle=f"round,pad={r},rounding_size={r}",
                                facecolor=BOX, edgecolor="none"))
    ax.text(X((x0 + x1) / 2), Y((y0 + y1) / 2), text, color="white", fontsize=10.5,
            ha="center", va="center", linespacing=1.25)


header(122.0, 390.0, 114.0, 217.5, "SE LA POSIZIONE\nFINANZIARIA NETTA\nÈ POSITIVA:")
header(413.0, 696.0, 114.0, 217.5, "SE LA POSIZIONE\nFINANZIARIA NETTA È\nNEGATIVA:")

# PFN positiva: ASSETS a tutta altezza; EQUITY (40%) sopra DEBTS (60%)
T, B = 228.5, 354.0
SPLIT = T + 0.40 * (B - T)
block(138.0, T, 246.0, B, "ASSETS")
block(247.0, T, 366.4, SPLIT, "EQUITY")
block(247.0, SPLIT, 366.4, B, "DEBTS")

# PFN negativa: ASSETS (73%) sopra CASH (27%); EQUITY alto quanto la somma dei due
T2, B2 = 227.5, 351.0
SPLIT2 = T2 + 0.73 * (B2 - T2)
block(438.4, T2, 554.1, SPLIT2, "ASSETS")
block(438.4, SPLIT2, 554.1, B2, "CASH")
block(557.5, T2, 678.0, B2, "EQUITY")

FF = 12.5
ax.text(X(252.0), Y(407.0), r"$\beta_U=\dfrac{\beta_L}{1+\dfrac{\mathit{PFN}}{E}(1-t_c)}$",
        fontsize=FF, ha="center", va="baseline")
ax.text(X(556.0), Y(407.0), r"$\beta_U=\beta_L\,\dfrac{E}{E+\mathit{PFN}}$",
        fontsize=FF, ha="center", va="baseline")

ax.text(X(119.0), Y(487.0), "Il Beta del debito è implicitamente considerato pari a zero",
        fontsize=9.5, ha="left", va="center")

style.save(fig, OUT)
