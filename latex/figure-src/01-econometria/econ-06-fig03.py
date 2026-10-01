"""Binomial tree S0=4 -> S1 -> S2, redrawn from the slide (no probabilities shown there)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig03.png")

fig, ax = style.figure(figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.72))
ax.set_xlim(100, 1080)
ax.set_ylim(860, 70)
ax.axis("off")

def label(x, y, s):
    ax.text(x, y, s, ha="left", va="center", fontsize=10, color=style.DARK)

label(145, 478, r"$S_{\mathrm{0}}\,=\,\mathrm{4}$")
label(415, 293, r"$S_{\mathrm{1}}(\mathit{H})\,=\,\mathrm{8}$")
label(418, 604, r"$S_{\mathrm{1}}(\mathit{T})\,=\,\mathrm{2}$")
label(836, 115, r"$S_{\mathrm{2}}(\mathit{HH})\,=\,\mathrm{16}$")
label(836, 407, r"$S_{\mathrm{2}}(\mathit{HT})\,=\,\mathrm{4}$")
label(836, 514, r"$S_{\mathrm{2}}(\mathit{TH})\,=\,\mathrm{4}$")
label(836, 808, r"$S_{\mathrm{2}}(\mathit{TT})\,=\,\mathrm{1}$")

arrows = [
    ((220, 450), (405, 305)), ((220, 450), (405, 598)),
    ((582, 270), (803, 122)), ((582, 305), (803, 415)),
    ((582, 598), (803, 488)), ((582, 632), (803, 782)),
]
for a, b in arrows:
    ax.annotate("", xy=b, xytext=a,
                arrowprops=dict(arrowstyle="-|>", color=style.DARK, lw=0.9,
                                shrinkA=0, shrinkB=0, mutation_scale=9))
style.save(fig, OUT)
