"""FSTR 07, slide 4: raccordo tra dati di bilancio e valutazione (goodwill)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style
from matplotlib.patches import Rectangle

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-07/fig01.png")

ASSET = "#B7CDD5"    # attivo / enterprise value (verde nella slide)
PFN = "#D98C82"      # posizione finanziaria netta (rosso-arancio nella slide)
EQUITY = "#EBD7A8"   # patrimonio netto / equity value (giallo nella slide)

W, H = 5.3, 3.05
fig, ax = style.figure(figsize=(W, H), constrained_layout=False)
ax.set_position([0, 0, 1, 1])
ax.axis("off")
# x in pollici, y in unità di valore (100 = attivo di bilancio, 150 = EV)
ax.set_xlim(0, W)
ax.set_ylim(-38, 224)

COL = 0.86
A0 = 0.05                      # inizio colonna Attivo
P0 = A0 + COL                  # inizio colonna Passivo
RB = P0 + COL                  # bordo destro del blocco di bilancio
E0 = 3.05                      # inizio colonna Enterprise Value
Q0 = E0 + COL                  # inizio colonna PFN / Equity Value
RV = Q0 + COL                  # bordo destro del blocco di valutazione
FS = 7.3


def bar(x0, y0, y1, color):
    ax.add_patch(Rectangle((x0, y0), COL, y1 - y0, facecolor=color,
                           edgecolor=style.DARK, linewidth=0.6))


# bilancio: attivo 100; passivo = PFN 40 (alto) + patrimonio netto 60 (basso)
bar(A0, 0, 100, ASSET)
bar(P0, 60, 100, PFN)
bar(P0, 0, 60, EQUITY)
# valutazione: EV 150; PFN 40 (alto) + equity value 110 (basso)
bar(E0, 0, 150, ASSET)
bar(Q0, 110, 150, PFN)
bar(Q0, 0, 110, EQUITY)

ctr = lambda x0: x0 + COL / 2
bold = dict(fontweight="bold", fontsize=FS, ha="center", va="center", color="black")
ax.text(ctr(A0), 72, "CCN", **bold)
ax.text(ctr(A0), 30, "ATTIVO\nFISSO", linespacing=1.15, **bold)
ax.text(ctr(P0), 80, "PFN", **bold)
ax.text(ctr(P0), 30, "PATRIMONIO\nNETTO", linespacing=1.15, **bold)
ax.text(ctr(E0), 112, "ENTERPRISE\nVALUE", linespacing=1.15, **bold)
ax.text(ctr(Q0), 130, "PFN", **bold)
ax.text(ctr(Q0), 55, "EQUITY\nVALUE", linespacing=1.15, **bold)

# importi a destra delle colonne del passivo
val = dict(fontweight="bold", fontsize=FS, ha="left", va="center", color="black")
ax.text(RB + 0.04, 80, "40", **val)
ax.text(RB + 0.04, 30, "60", **val)
ax.text(RV + 0.04, 130, "40", **val)
ax.text(RV + 0.04, 55, "110", **val)

# intestazioni a tabella
T1, T2, T3 = 221, 186, 167
for x0, x1 in ((A0, RB), (E0, RV)):
    for y in (T1, T3):
        ax.plot([x0, x1], [y, y], color=style.DARK, lw=1.1, solid_capstyle="butt")
ax.plot([A0, RB], [T2, T2], color=style.DARK, lw=0.8, solid_capstyle="butt")
ax.text((A0 + RB) / 2, (T1 + T2) / 2, "DATI DI BILANCIO\n(STATO PATR.)",
        linespacing=1.15, **bold)
ax.text(ctr(A0), (T2 + T3) / 2, "Attivo", **bold)
ax.text(ctr(P0), (T2 + T3) / 2, "Passivo", **bold)
ax.text((E0 + RV) / 2, (T1 + T3) / 2, "VALUTAZIONE", **bold)

# totali
for x0, label in ((A0, "100"), (P0, "100"), (E0, "150"), (Q0, "150")):
    ax.text(ctr(x0), -17, label, **bold)
for x0, x1 in ((A0, RB), (E0, RV)):
    ax.plot([x0, x1], [-33, -33], color=style.DARK, lw=1.1, solid_capstyle="butt")

# goodwill: differenza tra la sommità del blocco di valutazione e quella dell'attivo
for y in (100, 150):
    ax.plot([RB, E0], [y, y], color=style.RED, lw=1.1, ls=(0, (3.5, 2.5)))
xa = RB + 0.52
ax.annotate("", xy=(xa, 150), xytext=(xa, 100),
            arrowprops=dict(arrowstyle="<|-|>", color=style.RED, lw=1.1,
                            shrinkA=0, shrinkB=0, mutation_scale=9))
ax.text(xa + 0.09, 125, "Goodwill", fontsize=7.8, fontstyle="italic", fontweight="bold",
        color=style.GREY, ha="left", va="center")

style.save(fig, OUT)
