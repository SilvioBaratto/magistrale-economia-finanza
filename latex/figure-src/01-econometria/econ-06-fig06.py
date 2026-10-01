import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig06.png")

# Values recovered from the slide's vector drawing (bar heights).
_D = np.genfromtxt(str(style.REPO / "latex/figure-src/01-econometria/data/econ-06-fig06.csv"),
                   delimiter=",", names=True)
ACF = _D["acf"]
PACF = _D["pacf"]
BAND = 1.96 / np.sqrt(42)
lags = np.arange(1, 13)

fig, axes = style.figure(2, 1, figsize=(style.WIDTH_IN, style.WIDTH_IN * 0.5))
for ax, vals, name in zip(axes, (ACF, PACF), ("ACF", "PACF")):
    ax.bar(lags, vals, width=0.1, color=style.GP_RED, zorder=3)
    ax.axhline(0, color=style.DARK, lw=0.8, ls=":", zorder=2)
    ax.axhline(BAND, color=style.GP_GREEN, lw=1.0, ls="--", label=r"$\pm$ 1.96/T^0.5")
    ax.axhline(-BAND, color=style.GP_GREEN, lw=1.0, ls="--")
    ax.set_xlim(0, 13)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xticks(range(0, 13, 2))
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticklabels(["−1", "−0.5", "0", "0.5", "1"])
    ax.set_xlabel("Ritardo")
    ax.set_title(f"{name} di linvpc")
    ax.legend(loc="upper right", handlelength=2.6, markerfirst=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(True)
style.save(fig, OUT)
