import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig26.png")
CSV = str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig26.csv")
ser = {}
for r in csv.DictReader(open(CSV)):
    ser.setdefault(r["series"], []).append((float(r["x"]), float(r["density"])))
ser = {k: np.array(v) for k, v in ser.items()}

TEAL = "#008080"
fig, ax = style.figure(figsize=(7.2, 3.2))
ax.set_position([0.04, 0.27, 0.94, 0.41])
for k, c in [("df", "red"), ("tn", TEAL), ("dfd", "blue")]:
    ax.plot(ser[k][:, 0], ser[k][:, 1], color=c, lw=1.8, solid_capstyle="round")

ax.set_xlim(-5.6, 5.0)
ax.set_ylim(0, 0.53)
ax.set_xticks(range(-5, 6))
ax.set_yticks([0.2, 0.4])
ax.set_yticklabels([".2", ".4"])
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_visible(True)
ax.set_xticks(np.arange(-5.6, 5.0, 0.2), minor=True)
ax.set_yticks([0.1, 0.3, 0.5], minor=True)
ax.tick_params(axis="x", length=3, pad=4)
ax.tick_params(which="minor", length=1.8, width=0.6)
ax.grid(False)

for xc, h in [(-2.85, 0.125), (-1.95, 0.115), (-1.64, 0.10)]:
    ax.plot([xc, xc], [0, h], color=style.DARK, lw=0.6)

kw = dict(ha="center", va="center", fontsize=9.5, color=style.DARK)
ax.annotate("Valore critico di $\\mathbf{DF\\ con\\ drift}$\n"
            "$Pr_{H_0}(DFd\\!<\\!{-}2.85)\\!=\\!5\\%$",
            xy=(-2.92, 0.075), xytext=(-3.85, 0.215), arrowprops=dict(
                arrowstyle="-", lw=0.5, color=style.DARK, shrinkA=0, shrinkB=0), **kw)
ax.annotate("Valore critico di $\\mathbf{DF}$\n$Pr_{H_0}(DF\\!<\\!{-}1.95)\\!=\\!5\\%$",
            xy=(-2.15, -0.01), xytext=(-3.0, -0.19), annotation_clip=False,
            arrowprops=dict(arrowstyle="-", lw=0.5, color=style.DARK, shrinkA=0, shrinkB=0), **kw)
ax.annotate("Valore critico di $\\mathbf{t}$\n$Pr_{H_0}(t\\!<\\!{-}1.64)\\!=\\!5\\%$",
            xy=(-1.5, -0.02), xytext=(-0.65, -0.19), annotation_clip=False,
            arrowprops=dict(arrowstyle="-", lw=0.5, color=style.DARK, shrinkA=0, shrinkB=0), **kw)

fig.text(0.02, 0.985, "Distribuzione asintotica della statistica $t$ al variare del modello:",
         fontsize=12, fontweight="bold", va="top", ha="left")
for i, s in enumerate([
        "$Se\\ |\\beta_1|\\!<\\!1\\ \\Rightarrow\\ t\\!\\sim\\!N(0,1)$",
        "$Se\\ \\beta_1\\!=\\!1\\ e\\ \\beta_0\\!=\\!0$ la distribuzione è non standard",
        "$Se\\ \\beta_1\\!=\\!1\\ e\\ \\beta_0\\!\\neq\\!0$ la distribuzione è non standard"]):
    fig.text(0.03, 0.865 - i * 0.07, s, fontsize=9.5, style="italic", va="center")
for i, (c, s) in enumerate([
        (TEAL, "$t_{|\\beta_1|<1}$"),
        ("red", "Dickey$-$Fuller ($t_{\\beta_0=0,\\beta_1=1}$)"),
        ("blue", "Dickey$-$Fuller con drift ($t_{\\beta_0\\neq0,\\beta_1=1}$)")]):
    y_ = 0.86 - i * 0.07
    fig.add_artist(Line2D([0.55, 0.585], [y_, y_], color=c, lw=1.8))
    fig.text(0.595, y_, s, fontsize=9.5, va="center")

style.save(fig, OUT)
