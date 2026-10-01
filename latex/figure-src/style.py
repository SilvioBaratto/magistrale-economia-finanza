"""Shared look for the charts regenerated for the dispense.

Charts sit next to text set in Latin Modern with blue Polimi headings, so they
use the same face and colour. Import it before plotting:

    import sys; sys.path.insert(0, "<repo>/latex/figure-src")
    import style
    fig, ax = style.figure()
    ...
    style.save(fig, "<repo>/obsidian/01-Econometria/assets/econ-02/fig03.png")

``save`` writes the PNG that Obsidian shows and, beside it, a vector PDF of the
same name that latex/build.py prefers for the dispense.
"""

import shutil
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib import font_manager

# Scripts locate everything from here, so the repository can live anywhere.
REPO = Path(__file__).resolve().parents[2]
DATASETS = Path(__file__).resolve().parent / "datasets"


def _latin_modern_dir() -> Path:
    """Folder of the Latin Modern OpenType fonts of the local TeX installation."""
    if shutil.which("kpsewhich"):
        hit = subprocess.run(["kpsewhich", "lmroman10-regular.otf"],
                             capture_output=True, text=True).stdout.strip()
        if hit:
            return Path(hit).parent
    return Path("/usr/local/texlive/2025/texmf-dist/fonts/opentype/public/lm")


LM_DIR = _latin_modern_dir()

BLUE = "#5B8999"      # cmyk(0.4, 0.1, 0, 0.4), bluepoli in template/dispensa.latex
DARK = "#2B2B2B"
GREY = "#8C8C8C"
LIGHT = "#D9D9D9"
RED = "#B03A2E"       # for marks the slides draw in red ("quadrati rossi")
PALETTE = [BLUE, DARK, RED, GREY, "#C08A2B"]

# gretl/gnuplot charts in the Econometria slides draw series and correlogram
# bars in pure red, confidence bands in green or blue. Redraws of those charts
# share these values so the family stays uniform across figures.
GP_RED = "#E8000B"
GP_GREEN = "#00B000"
GP_BLUE = "#1F3FD0"
GP_LINEWIDTH = 0.9

# The page shows figures at ~85% of a 160 mm measure, about 5.4 in.
WIDTH_IN = 5.4


def _register_latin_modern() -> None:
    for name in ("regular", "bold", "italic", "bolditalic"):
        path = LM_DIR / f"lmroman10-{name}.otf"
        if path.exists():
            font_manager.fontManager.addfont(str(path))


_register_latin_modern()
plt.rcParams.update({
    "font.family": "Latin Modern Roman",
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.titlesize": 10,
    "axes.labelsize": 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.edgecolor": DARK,
    "axes.labelcolor": DARK,
    "xtick.color": DARK,
    "ytick.color": DARK,
    "axes.prop_cycle": cycler(color=PALETTE),
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "grid.color": LIGHT,
    "grid.linewidth": 0.5,
    "legend.frameon": False,
    "lines.linewidth": 1.4,
    "scatter.marker": "o",
    "axes.formatter.use_locale": False,
    "pdf.fonttype": 42,
})


def figure(nrows=1, ncols=1, height_ratio=0.62, **kwargs):
    """Create a figure sized for the dispensa page.

    Args:
        nrows: Rows of subplots.
        ncols: Columns of subplots.
        height_ratio: Height as a fraction of the page-fitting width.
        **kwargs: Passed on to ``plt.subplots``.

    Returns:
        The ``(fig, axes)`` pair from ``plt.subplots``.
    """
    kwargs.setdefault("figsize", (WIDTH_IN, WIDTH_IN * height_ratio))
    kwargs.setdefault("constrained_layout", True)
    return plt.subplots(nrows, ncols, **kwargs)


def save(fig, path) -> Path:
    """Write the figure as a 300 dpi PNG and as a vector PDF beside it.

    Args:
        fig: The matplotlib figure.
        path: Destination ``.png`` path; the PDF takes the same name.

    Returns:
        The PNG path.
    """
    out = Path(path).with_suffix(".png")
    out.parent.mkdir(parents=True, exist_ok=True)
    for target, dpi in ((out, 300), (out.with_suffix(".pdf"), None)):
        fig.savefig(target, dpi=dpi or "figure", bbox_inches="tight", pad_inches=0.04,
                    facecolor="white")
    plt.close(fig)
    return out
