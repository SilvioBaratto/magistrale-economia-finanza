import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import pandas as pd
import style

CSV = str(style.DATASETS / "ECON_Dataset_caschool.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-01/fig01.png")

df = pd.read_csv(CSV)
x, y = df["str"].to_numpy(), df["avg_score"].to_numpy()
b, a = np.polyfit(x, y, 1)
xs = np.array([x.min(), x.max()])

fig, ax = style.figure(height_ratio=0.44)
ax.scatter(x, y, s=14, color="#1A476F", linewidths=0, label="avg_score")
ax.plot(xs, a + b * xs, color="#8B2A2A", lw=1.0, label="Fitted values")
ax.set_xlabel("Average Class Size (str)")
ax.set_ylabel("Average Score (ave_score)", fontsize=8.5)
ax.set_xticks([15, 20, 25])
ax.set_yticks(range(600, 701, 20))
ax.set_ylim(598, 710)
ax.grid(axis="y")
ax.set_axisbelow(True)
fig.legend(loc="outside lower center", ncol=2, frameon=True,
          edgecolor=style.DARK, fancybox=False)
style.save(fig, OUT)
print(len(df), x.min(), x.max(), y.min(), y.max(), a, b)
