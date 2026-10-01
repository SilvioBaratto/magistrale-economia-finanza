import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style
import matplotlib.pyplot as plt

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig25.png")

# Two independent random walks, quarterly 1971:1-2008:2 (150 obs), values taken from the slide.
# Both are stored in left-axis units; Y is read on the right axis (left value - 20).
X = np.array([-0.39,-2.27,-1.89,-3.06,-2.87,-2.36,-3.19,-2.84,-1.54,-1.41,-0.58,0.18,-0.87,-1.79,-1.41,-1.15,-0.36,-0.65,-0.9,-1.82,-2.93,-3.82,-2.68,-2.78,-3.25,-1.09,-1.98,0.31,-0.52,0.24,0.75,-0.2,0.12,1.83,2.15,1.45,1.71,2.53,2.82,3.61,4.57,3.26,1.99,1.07,1.83,2.79,4.38,3.68,2.69,2.44,2.18,1.51,0.02,0.5,1.77,1.77,1.74,1.83,2.47,2.4,3.68,3.52,3.99,4.18,2.88,3.49,4.34,5.77,7.65,9.68,9.87,11.68,12.64,13.02,14.51,14.54,13.5,13.78,14,14.51,16.93,16.04,14.74,14.42,13.81,12.13,10.76,9.46,9.43,9.87,11.37,13.08,13.02,12.32,12.24,12.16,11.94,11.62,12.26,12.38,13.27,13.97,13.15,12.54,12.13,12.54,13.02,12.54,12.86,13.15,12.89,11.72,12.89,13.56,13.15,13.85,13.75,14.13,15.08,14.29,14.8,15.66,16.2,15.97,16.51,17.66,19.09,19.79,22.3,22.04,22.39,21.6,19.85,18.64,18.36,18.07,17.34,17.75,16.83,16.48,15.34,14.35,14.08,13.81,13.72,13.24,12.51,12.99,14.96,14.8])
Y = np.array([20.07,20.17,19.38,20.17,20.42,20.71,21.89,22.27,21.89,20.96,21.5,20.42,20.26,21.5,22.49,21.82,22.01,21.63,20.49,19.76,19.95,19.53,19.41,18.74,18.99,18.58,18.96,17.85,16.83,18.33,19.6,18.39,19.34,19.76,19.85,19.72,19.63,18.58,17.44,16.04,15.02,14.07,13.18,13.02,12.73,13.02,13.62,12.54,12.61,13.05,12.8,12.86,12.57,13.02,13.5,13.85,14.04,13.65,12.99,11.21,9.68,9.68,9.43,9.56,9.97,10.03,9.71,10.25,9.21,8.54,9.21,8.03,7.97,7.3,5.58,6.28,5.14,4.34,3.68,5.07,4.63,4.09,3.9,5.17,5.52,6.44,6.63,6.35,6.12,6.15,4.82,5.55,6.73,6.92,6.19,5.61,6.41,6.95,7.39,6.85,6.5,6.06,5.71,6.85,8,8.32,8.44,8.7,8.03,9.56,8.38,8.54,8.35,8.76,9.17,7.78,6.92,6.47,6.15,6.22,5.39,6.47,7.78,8.09,6.5,7.04,7.43,8.16,8.51,8.7,7.81,6.92,5.46,3.45,2.75,1.48,0.43,-0.39,-0.42,-0.04,-0.46,-1.15,-1,-0.65,-0.01,-0.01,-0.17,0.31,-0.61,-1.22])
t = 1971 + np.arange(len(X)) * 0.25 + 0.2

fig, ax = style.figure(figsize=(7.4, 3.5))
ax.spines["right"].set_visible(True)
ax.plot(t, Y, color=style.GP_RED, lw=style.GP_LINEWIDTH, label="Y (destra)")
ax.plot(t, X, color=style.GP_BLUE, lw=style.GP_LINEWIDTH, ls=(0, (4, 2)), label="X (sinistra)")
ax.axhline(0, color="black", lw=0.8, ls=":")
ax.set_xlim(1970.3, 2009.5)
ax.set_ylim(-5, 25)
ax.set_xticks(range(1975, 2006, 5))
ax.set_yticks(range(-5, 26, 5))
ax2 = ax.twinx()
ax2.set_ylim(-25, 5)
ax2.set_yticks(range(-25, 6, 5))
ax2.spines["right"].set_visible(True)
ax2.spines["top"].set_visible(True)
ax.spines["top"].set_visible(True)
ax.set_xlabel("Tempo")
ax.set_ylabel("Ascisse Y")
ax2.set_ylabel("Ascisse X")
ax.set_title("Grafico dei random walk indipendenti (Y,X)")
leg = ax.legend(loc="upper left", bbox_to_anchor=(0.16, 1.0), markerfirst=False, handlelength=2.6, fontsize=9,
                labelspacing=0.05, borderaxespad=0.15, frameon=False)
for h in leg.get_lines():
    h.set_linewidth(style.GP_LINEWIDTH)
style.save(fig, OUT)
