import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import style
from scipy import stats
from scipy.special import log_expit

OUT = str(style.REPO / "obsidian/01-Econometria/assets/econ-02/fig09.png")

# Schematic skewed sampling densities in the slide's pixel units (x 62..1212, baseline y=518).
# The slide draws them freehand, so there is no underlying dataset: each curve is a smooth analytic
# hump whose parameters were least-squares fitted to the original's outline.
X0, X1, BASE, BETA = 62, 1212, 518, 337
SKY = "#6EC3E6"
CYAN = "#0A9AD6"
GREY = "#808080"
GRID = np.linspace(-300, 1700, 8001)


def unit_peak(f):
    """Return f divided by its maximum, so shapes can be mixed and scaled by peak height."""
    return lambda x: f(x) / f(GRID).max()


def gamma_hump(x0, scale, a, p, cut, cut_width):
    """Generalized-gamma density starting at x0, with a soft Gaussian cut-off on the far tail."""
    return unit_peak(lambda x: stats.gengamma.pdf(x, a / p, p, loc=x0, scale=scale)
                     * stats.norm.sf(x, cut, cut_width))


def plateau_hump(a, wa, na, b, wb, nb, mu, sigma, tau, weight, cut, cut_width):
    """Round-topped core plus a right-skewed exponentially modified Gaussian base.

    The core rises at ``a`` and falls at ``b`` through generalized-logistic edges, giving the
    dome; the base carries the long right tail, and a Gaussian cut-off lets it reach the axis
    where the slide's curve does instead of decaying forever.
    """
    core = unit_peak(lambda x: np.exp(na * log_expit((x - a) / wa) + nb * log_expit((b - x) / wb)))
    base = unit_peak(lambda x: stats.exponnorm.pdf(x, tau / sigma, loc=mu, scale=sigma))
    return unit_peak(lambda x: (core(x) + weight * base(x)) * stats.norm.sf(x, cut, cut_width))


n1 = gamma_hump(61.592, 244.61, 1.6351, 1.1186, 1105.3, 177.66)
n2 = plateau_hump(112.93, 67.846, 6.7495, 364.46, 12.79, 0.11127,
                  275.94, 29.706, 131.43, 0.49741, 720.42, 83.639)
n3 = plateau_hump(305.08, 5.4304, 0.63608, 374.74, 4.6251, 0.15491,
                  296.34, 43.748, 135.39, 0.92562, 580.58, 80.47)

x1 = np.linspace(61.592, X1, 4000)
x2 = np.linspace(90, 830, 3000)
x3 = np.linspace(172, 705, 3000)
h1 = 197.51 * n1(x1)
h2 = 322.23 * n2(x2)
h3 = 500.44 * n3(x3)

AX_H = BASE - 17 + 8
fig, ax = style.figure(figsize=(style.WIDTH_IN, style.WIDTH_IN * (AX_H + 33) / (X1 - X0 + 40)))
ax.plot(x1, h1, color=SKY, lw=1.3, solid_capstyle="butt")
ax.plot(x2, h2, color=GREY, lw=1.6, solid_capstyle="butt")
ax.plot(x3, h3, color=CYAN, lw=1.8, solid_capstyle="butt")


def label(txt, xy, xt):
    """Write txt at xt with a plain leader line ending on the curve point xy."""
    ax.annotate(txt, xy=xy, xytext=xt, ha="left", va="center", fontsize=10,
                arrowprops=dict(arrowstyle="-", color=style.DARK, lw=0.8, shrinkA=0, shrinkB=0))


def hgt(y):
    """Convert a slide pixel row to a height above the baseline."""
    return BASE - y


label(r"$n_3$", (380, hgt(68)), (436, hgt(40)))
label(r"$n_2$", (396, hgt(254)), (458, hgt(222)))
label(r"$n_1$", (678, hgt(466)), (727, hgt(410)))

ax.set_xlim(X0, X1)
ax.set_ylim(0, AX_H)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
for s in ("left", "right", "top"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_visible(True)
ax.spines["bottom"].set_linewidth(1.0)
ax.plot([X0, X0], [0, hgt(55)], color=style.DARK, lw=1.6, solid_capstyle="butt", clip_on=False)
ax.plot([BETA, BETA], [0, 11], color=style.DARK, lw=1.0, solid_capstyle="butt")
ax.text(BETA, -16, r"$\beta_1$", ha="center", va="top")
ax.text(X1 - 4, -16, r"$\hat\beta_1$", ha="right", va="top", fontsize=10)
ax.text(X0 - 14, hgt(52), r"$f_{\hat\beta_1}$", ha="right", va="center")
style.save(fig, OUT)
