import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-07/fig04.png")

t = np.arange(0, 9)
a05 = -1.0 * 0.5 ** t
a1 = np.where(t == 0, -2.0, 0.0)
a2 = -3.0 * (-0.5) ** t

fig, ax = style.figure(height_ratio=0.42)
ax.axhline(0, color=style.GREY, lw=0.6, zorder=1)
ax.plot(t, a05, color="#D62728", lw=1.6, label=r"$\alpha_y$=0.5", zorder=2)
ax.plot(t, a1, color="#1F3FD0", lw=1.6, label=r"$\alpha_y$=1", zorder=3)
ax.plot(t, a2, color="#1F8A8A", lw=1.6, label=r"$\alpha_y$=2", zorder=2)
ax.set_xlim(0, 10)
ax.set_ylim(-3, 1.6)
ax.set_xticks(range(0, 11))
ax.set_yticks(np.arange(-3, 1.6, 0.5))
ax.set_yticklabels([f"{v:.1f}" for v in np.arange(-3, 1.6, 0.5)])
ax.set_xlabel("tempo", style="italic")
ax.set_ylabel(r"$E[Y_t - Y_{t-1}\,|\,passato]$")
ax.set_title(r"Andamento di $E[\Delta Y_t\,|\,passato]$ per diversi valori di $\alpha_y$",
             fontweight="bold", y=-0.4, fontsize=9)
ax.legend(loc="upper right", frameon=True, edgecolor=style.DARK, fancybox=False,
          handlelength=2.2, fontsize=8, borderpad=0.3, labelspacing=0.2, bbox_to_anchor=(0.94, 1.0))
style.save(fig, OUT)
