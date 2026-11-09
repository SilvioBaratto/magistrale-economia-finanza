"""FSTR 03, slide 17: multiplo EBITDA (capitalizzazione / EBITDA) di cinque società alimentari."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/11-Finanza-Strategica/assets/fstr-03/fig02.png")

# capitalizzazione e EBITDA in migliaia di euro, dalla tabella della slide
DATA = [
    ("Conagra Foods Inc.", 17_383_003, 1_391_339),
    ("General Mills Inc.", 35_364_038, 2_999_013),
    ("Kellogg Co.", 24_665_300, 2_319_281),
    ("Marr S.p.A.", 1_269_299, 105_674),
    ("Tyson Foods Inc.", 19_542_863, 2_479_693),
]
names = [n for n, _, _ in DATA]
mult = [cap / ebitda for _, cap, ebitda in DATA]
# la slide riporta la media dei cinque multipli arrotondati a due decimali
mean = round(sum(round(m, 2) for m in mult) / len(mult), 2)


def it(x: float) -> str:
    """Format with two decimals and the decimal comma used by the slide."""
    return f"{x:.2f}".replace(".", ",")


fig, ax = style.figure(height_ratio=0.50)
x = range(len(DATA))
ax.bar(x, mult, width=0.72, color=style.BLUE, zorder=2)

# nella slide le tre linee di griglia cadono a 0, 5 e 10; la scala non è riportata
for y in (5, 10):
    ax.axhline(y, color=style.LIGHT, lw=0.5, zorder=1)
ax.axhline(0, color=style.LIGHT, lw=0.8, zorder=1)
ax.axhline(mean, color=style.DARK, lw=1.0, ls=(0, (4, 2.5)), zorder=3)

for xi, m in zip(x, mult):
    ax.text(xi, m + 0.22, it(m), ha="center", va="bottom", fontsize=8.5,
            fontweight="bold", color="black", zorder=5,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.6))
# la slide mette l'etichetta a sinistra, sopra la prima barra; qui sta sopra la barra più bassa
# (Tyson) per non coprire il tracciato di Conagra
ax.text(len(DATA) - 0.5, mean + 0.2, f"Valore medio: {it(mean)}", ha="right", va="bottom",
        fontsize=8.5, color="black", zorder=5)

ax.set_xlim(-0.5, len(DATA) - 0.5)
ax.set_ylim(0, 14.2)
ax.set_xticks(list(x))
ax.set_xticklabels(names, fontsize=8)
ax.tick_params(axis="x", length=0)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_title("Multiplo EBITDA", loc="left", fontsize=10, fontweight="bold", color=style.DARK)

style.save(fig, OUT)
print([round(m, 4) for m in mult], mean)
