"""Figure 8 of ECON 02: population line E[wage|educ] against the OLS fit.

Schematic redraw in the pixel frame of the slide: the fitted line is the
wage-on-educ regression (-.9048 + .5413 educ); the dashed population line is
drawn as in the original, flatter and crossing it near the left.
"""
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig08.png")

fig, ax = style.figure(height_ratio=0.46)
ax.set_xlim(27, 1160)
ax.set_ylim(537, 10)
ax.set_xticks([])
ax.set_yticks([])

C = style.BLUE
ax.plot([27, 1045], [391, 100], color=C, lw=1.5, solid_capstyle="butt")
ax.plot([32, 1043], [334, 228], color=C, lw=1.5, dashes=(7, 3.5))

ax.annotate("", xy=(840, 155), xytext=(770, 97),
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.8, shrinkA=0, shrinkB=0))
ax.annotate("", xy=(908, 245), xytext=(975, 303),
            arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.8, shrinkA=0, shrinkB=0))

ax.text(766, 72, r"$\hat{E}[wage\,|\,educ\,]\,{=}\,\mathrm{{-}{.}9048\,{+}\,{.}5413}\ educ$", ha="center", va="center",
        fontsize=9.5, color=style.DARK)
ax.text(955, 345, r"$E[wage\,|\,educ]\,{=}\,a\,{+}\,b\ educ$", ha="center", va="center",
        fontsize=9.5, color=style.DARK)
ax.text(36, 28, "wage", fontstyle="italic", ha="left", va="center", fontsize=9.5, color=style.DARK)
ax.text(1155, 521, "educ", fontstyle="italic", ha="right", va="center", fontsize=9.5, color=style.DARK)

style.save(fig, OUT)
