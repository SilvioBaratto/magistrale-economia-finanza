import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from scipy.stats import gaussian_kde, norm
import style

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-06/fig24.png")
T, R = 500, 20000
rng = np.random.default_rng(24)

# t statistic on the slope of y_t = a + b x_t + u_t with x, y independent random walks
x = rng.standard_normal((R, T)).cumsum(axis=1)
y = rng.standard_normal((R, T)).cumsum(axis=1)
xc = x - x.mean(1, keepdims=True)
yc = y - y.mean(1, keepdims=True)
b = (xc * yc).sum(1) / (xc ** 2).sum(1)
res = yc - b[:, None] * xc
s2 = (res ** 2).sum(1) / (T - 2)
tstat = b / np.sqrt(s2 / (xc ** 2).sum(1))

grid = np.linspace(-85, 92, 6000)
spur = gaussian_kde(tstat, bw_method=0.15)(grid)
# KDE of simulated N(0,1) t statistics, as in the original (peak slightly above the 0.4 tick)
z = np.random.default_rng(26).standard_normal(500)
stand = gaussian_kde(z, bw_method=0.2)(grid)

PINK, CYAN = "#F4B8B4", "#8FE3E3"
fig, ax = style.figure(figsize=(5.4, 5.4))
ax.set_position([0.13, 0.10, 0.50, 0.80])
ax.fill_between(grid, spur, color=PINK, alpha=0.6, lw=0, label="Stat t regressione spuria")
ax.plot(grid, spur, color="black", lw=0.8)
ax.fill_between(grid, stand, color=CYAN, alpha=0.6, lw=0, label="Stat t caso standard - N(0,1)")
ax.plot(grid, stand, color="black", lw=0.8)
ax.set_xlim(-95, 100)
ax.set_ylim(-0.02, 0.44)
ax.set_xticks([-50, 0, 50])
ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
ax.set_xlabel("value")
ax.set_ylabel("density")
ax.set_title("Densità della statistica t")
leg = ax.legend(title="case", loc="center left", bbox_to_anchor=(1.03, 0.5), frameon=False, fontsize=8, title_fontproperties={"weight": "bold"}, alignment="left")
style.save(fig, OUT)
print(tstat.std(), spur.max(), stand.max())
