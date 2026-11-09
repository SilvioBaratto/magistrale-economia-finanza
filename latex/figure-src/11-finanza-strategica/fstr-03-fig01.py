"""FSTR 03, slide 4-7: enterprise value, equity value e PFN nei tre casi PFN>0, PFN=0, PFN<0."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Rectangle

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-03/fig01.png")

# stessa assegnazione colori di fstr-07 (attivo/EV, PFN, equity)
EV = "#B7CDD5"
PFN = "#D98C82"
EQUITY = "#EBD7A8"
NAME_BOX = "#EDEDED"

# The three cases sit in side-by-side columns with the two firms stacked: the figure stays below
# the template's 0.4 textheight cap, so the print scale is set by the width (0.8 of the line) and
# a 7.6 pt body stays above 7 pt in the PDF. A stacked-rows layout was 5.4 in tall and printed
# at 4.7 pt.
W = 5.4
U = 0.0130           # pollici per milione di euro: le altezze dei blocchi sono in scala
BW = 0.76            # larghezza di un blocco
GAP = 0.05           # spazio tra blocco EV e colonna di destra
GROUP = 2 * BW + GAP
BRACKET = 0.24       # spazio a sinistra della terza colonna per la graffa dell'EV
GAPC = 0.16          # spazio tra le colonne
MARGIN = (W - 3 * GROUP - BRACKET - 2 * GAPC) / 2
X0 = [MARGIN,
      MARGIN + GROUP + GAPC,
      MARGIN + 2 * (GROUP + GAPC) + BRACKET]
FS = 7.6

# (titolo, [(impresa, blocchi)]) con blocchi = (EV o attivo operativo, MK CAP, PFN)
CASES = [
    ("Impresa indebitata,\nPFN > 0",
     [("Impresa Alfa", dict(ev=60, eq=15, pfn=45)),
      ("Impresa Beta", dict(ev=70, eq=15, pfn=55))]),
    ("Impresa non indebitata,\nPFN = 0",
     [("Impresa Gamma", dict(ev=95, eq=95, pfn=0)),
      ("Impresa Delta", dict(ev=74, eq=74, pfn=0))]),
    ("Impresa non indebitata,\nPFN < 0",
     [("Impresa Gamma", dict(ev=95, eq=105, cash=10)),
      ("Impresa Delta", dict(ev=74, eq=84, cash=10))]),
]

TITLE_H, NAME_H, GAP_Y, LEG_H = 0.36, 0.30, 0.08, 0.30
ROWS = 2
row_h = [max(max(firms[r][1]["ev"] + firms[r][1].get("cash", 0), firms[r][1]["eq"])
             for _, firms in CASES) * U for r in range(ROWS)]
H = LEG_H + TITLE_H + sum(h + NAME_H + GAP_Y for h in row_h) - GAP_Y

fig, ax = style.figure(figsize=(W, H), constrained_layout=False)
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def block(x0, ybot, units, color, label, value, above=False):
    """Draw one block whose height is proportional to its value.

    Args:
        x0: Left edge in inches.
        ybot: Bottom edge in inches.
        units: Value in millions of euro; sets the height through ``U``.
        color: Fill colour.
        label: Bold name; shown above the value when the block is tall enough, else beside it.
        value: Amount printed after the euro sign.
        above: Print the one-line label over the block instead of inside it, for blocks too thin
            or too narrow to hold it.
    """
    h = units * U
    ax.add_patch(Rectangle((x0, ybot), BW, h, facecolor=color,
                           edgecolor=style.DARK, linewidth=0.6))
    kw = dict(fontsize=FS, fontweight="bold", ha="center", va="center", color="black")
    if above:
        ax.text(x0 + BW / 2, ybot + h + 0.04, f"{label} €{value}m", **{**kw, "va": "bottom"})
    elif h >= 0.36:
        ax.text(x0 + BW / 2, ybot + h / 2, f"{label}\n€{value}m", linespacing=1.25, **kw)
    else:
        ax.text(x0 + BW / 2, ybot + h / 2 - 0.004, f"{label} €{value}m", **kw)


# legenda: larghezze misurate sul testo reale per centrarla
leg = [(EV, "Enterprise value (assets)"), (EQUITY, "Equity value (MK CAP)"),
       (PFN, "Posizione finanziaria netta (PFN)")]
renderer = fig.canvas.get_renderer()
inch = fig.dpi
widths = []
for _, text in leg:
    probe = ax.text(0, 0, text, fontsize=FS + 0.2)
    widths.append(probe.get_window_extent(renderer).width / inch + 0.16)
    probe.remove()
SEP = 0.2
x = (W - sum(widths) - SEP * (len(leg) - 1)) / 2
yl = H - LEG_H / 2 - 0.02
for (color, text), w in zip(leg, widths):
    ax.add_patch(Rectangle((x, yl - 0.055), 0.11, 0.11, facecolor=color,
                           edgecolor=style.DARK, linewidth=0.6))
    ax.text(x + 0.16, yl, text, fontsize=FS + 0.2, ha="left", va="center", color="black")
    x += w + SEP

top = H - LEG_H
for x0, (title, _) in zip(X0, CASES):
    ax.text(x0 + GROUP / 2, top - TITLE_H / 2, title, fontsize=FS + 0.8, fontweight="bold",
            ha="center", va="center", color=style.DARK, linespacing=1.2)

cursor = top - TITLE_H
for r in range(ROWS):
    ybase = cursor - row_h[r]
    for x0, (_, firms) in zip(X0, CASES):
        name, b = firms[r]
        xr = x0 + BW + GAP
        if "cash" in b:
            # PFN negativa: la cassa è sotto le immobilizzazioni, ma l'EV è solo l'attivo operativo
            block(x0, ybase, b["cash"], PFN, "CASH", b["cash"])
            block(x0, ybase + b["cash"] * U, b["ev"], EV, "FIXED\nASSETS", b["ev"])
            block(xr, ybase, b["eq"], EQUITY, "MK CAP", b["eq"])
            ytop = ybase + (b["cash"] + b["ev"]) * U
            ylo = ybase + b["cash"] * U
            xb = x0 - 0.09
            ax.plot([xb + 0.04, xb, xb, xb + 0.04], [ytop, ytop, ylo, ylo],
                    color=style.DARK, lw=0.8, solid_capstyle="butt")
            ax.text(xb - 0.07, (ylo + ytop) / 2, f"E.V. €{b['ev']}m", rotation=90,
                    fontsize=FS, fontweight="bold", ha="center", va="center", color="black")
        else:
            block(x0, ybase, b["ev"], EV, "E.V.", b["ev"])
            if b["pfn"]:
                block(xr, ybase, b["pfn"], PFN, "PFN", b["pfn"])
                block(xr, ybase + b["pfn"] * U, b["eq"], EQUITY, "MK CAP", b["eq"], above=True)
            else:
                block(xr, ybase, b["eq"], EQUITY, "MK CAP", b["eq"])
        # nome dell'impresa sotto la linea di base comune
        nw, nh = 1.18, 0.19
        ax.add_patch(Rectangle((x0 + GROUP / 2 - nw / 2, ybase - 0.07 - nh), nw, nh,
                               facecolor=NAME_BOX, edgecolor=style.GREY, linewidth=0.6))
        ax.text(x0 + GROUP / 2, ybase - 0.07 - nh / 2 - 0.005, name, fontsize=FS + 0.4,
                fontweight="bold", ha="center", va="center", color="black")
    cursor = ybase - NAME_H - GAP_Y

style.save(fig, OUT)
print(round(W, 2), round(H, 2))
