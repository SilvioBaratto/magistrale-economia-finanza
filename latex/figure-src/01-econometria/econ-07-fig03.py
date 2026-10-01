import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import pandas as pd
import style

CSV = str(style.DATASETS / "ECON_Dataset_tassi-USA.csv")
OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-07/fig03.png")

df = pd.read_csv(CSV)
t = 1946 + 11 / 12 + np.arange(len(df)) / 12  # monthly, from 1946:12

fig, ax = style.figure(height_ratio=0.5)
ax.plot(t, df["r3"], color=style.GP_RED, lw=style.GP_LINEWIDTH, label="Tasso a 3 mesi (r3)")
ax.plot(t, df["r60"], color=style.GP_BLUE, lw=style.GP_LINEWIDTH, label="Tasso a 5 anni (r60)")
ax.set_ylim(0, 16)
ax.set_xlim(1945.5, 1991.5)
ax.set_yticks(range(0, 17, 2))
ax.set_xticks(range(1950, 1991, 5))
ax.legend(loc="upper left", bbox_to_anchor=(0.08, 1.0), handlelength=3)
style.save(fig, OUT)
