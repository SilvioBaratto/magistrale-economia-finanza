"""ERA 07, slide 26: cream skimming, region R between psi'' and psi_l (bar) on the low-risk zero-profit line."""
from typing import NamedTuple

import numpy as np
from scipy.optimize import brentq

from modello_screening import (COMPACT_MARKER_SIZE, CURVE_LINE_WIDTH, LABEL_SIZE, LINE_LABEL_STYLE, PI_HIGH,
                               PI_LOW, SYMBOL_SIZE, decorate_axes, expected_utility, indemnity_on_curve,
                               leader_line, mark_contracts, new_plane, plot_full_cover_line,
                               plot_zero_profit_line, save_figure, separating_contract, style)

# Same parameters as Figure 3. With them the region R is a thin sliver on the full plane
# (psi_h^c = (6, 3)), so the plot is an enlargement of the window B in [0, XMAX], p in [0, P_TOP] around
# psi_l bar; the headroom up to YMAX only holds the labels of the lines.
HEIGHT_RATIO = 0.66
XMAX, YMAX = 3.2, 0.84
P_TOP = 0.58

# psi'' and psi' lie on the low-risk zero-profit line at these multiples of the B of psi_l bar.
PSI_LEFT_SHARE = 0.5
PSI_RIGHT_SHARE = 1.5
# The premium grid reaches well above the plotted window so that np.interp can invert both curves
# all the way to their crossing.
GRID_TOP = 1.6
GRID_SAMPLES = 4000
REGION_SAMPLES = 600
# Upper end of the B bracket in which the two curves cross.
CROSSING_SEARCH_MAX = 3.0
# Premium at which the low-risk curve u_l'' stops.
LOW_CURVE_P_END = 0.42
# B at which the label of the low-risk zero-profit line sits, just below the line.
LOW_LINE_LABEL_B = 2.2
REGION_LABEL_XY = (0.8, 0.035)


class Geometry(NamedTuple):
    """Contracts and curves that bound the region of cream skimming.

    Attributes:
        b_left: Indemnity of psi''.
        p_left: Premium of psi''.
        b_right: Indemnity of psi'.
        p_right: Premium of psi'.
        p_grid: Premiums at which both curves are sampled, increasing.
        b_high_c: Indemnity of the high-risk curve u_h^c at each premium of the grid.
        b_low_left: Indemnity of the low-risk curve u_l'' through psi'' at each premium of the grid.
    """

    b_left: float
    p_left: float
    b_right: float
    p_right: float
    p_grid: np.ndarray
    b_high_c: np.ndarray
    b_low_left: np.ndarray


def build_geometry(contract) -> Geometry:
    """Place psi'' and psi' around psi_l bar and sample the two curves that bound the region.

    Args:
        contract: The separating equilibrium of Figure 3.

    Returns:
        The two contracts and the sampled curves.
    """
    b_left = PSI_LEFT_SHARE * contract.b_bar
    b_right = PSI_RIGHT_SHARE * contract.b_bar
    p_left = PI_LOW * b_left
    p_right = PI_LOW * b_right
    u_low_left = expected_utility(PI_LOW, b_left, p_left)
    p_grid = np.linspace(0, GRID_TOP, GRID_SAMPLES)
    return Geometry(b_left, p_left, b_right, p_right, p_grid,
                    indemnity_on_curve(PI_HIGH, contract.u_high_c, p_grid),
                    indemnity_on_curve(PI_LOW, u_low_left, p_grid))


def shade_region(ax, contract, geo):
    """Shade the region R: above the low-risk line, below u_l'', above and left of u_h^c.

    Left of u_h^c the high-risk type is worse off than at psi_h^c.

    Args:
        ax: Axes of the (B, p) plane.
        contract: The separating equilibrium of Figure 3.
        geo: Contracts and curves that bound the region.
    """
    b_cross = brentq(lambda b: np.interp(b, geo.b_low_left, geo.p_grid) - np.interp(b, geo.b_high_c, geo.p_grid),
                     contract.b_bar, CROSSING_SEARCH_MAX)
    b_fill = np.linspace(geo.b_left, b_cross, REGION_SAMPLES)
    upper = np.interp(b_fill, geo.b_low_left, geo.p_grid)
    lower = np.maximum(PI_LOW * b_fill, np.interp(b_fill, geo.b_high_c, geo.p_grid))
    ax.fill_between(b_fill, lower, upper, where=upper > lower, color=style.LIGHT, lw=0, zorder=1)


def draw_reference_lines(ax):
    """Draw the line p = B and the zero-profit lines of the two types, with their labels.

    Args:
        ax: Axes of the (B, p) plane.
    """
    plot_full_cover_line(ax, P_TOP)
    ax.text(P_TOP - 0.05, P_TOP + 0.01, "$p=B$", ha="right", va="bottom", fontsize=LABEL_SIZE)
    plot_zero_profit_line(ax, PI_HIGH, P_TOP / PI_HIGH, style.DARK)
    plot_zero_profit_line(ax, PI_LOW, XMAX, style.BLUE)
    ax.text(P_TOP / PI_HIGH + 0.1, P_TOP + 0.04, "retta di profitto nullo\ndell’alto rischio", ha="center",
            va="bottom", **LINE_LABEL_STYLE)
    ax.text(XMAX - 0.02, PI_LOW * LOW_LINE_LABEL_B - 0.05, "retta di profitto nullo\ndel basso rischio", ha="right",
            va="top", color=style.BLUE, **LINE_LABEL_STYLE)


def draw_indifference_curves(ax, geo):
    """Draw the visible parts of u_h^c and u_l'' with their labels.

    Args:
        ax: Axes of the (B, p) plane.
        geo: Contracts and curves that bound the region.
    """
    visible_high = geo.p_grid <= P_TOP
    ax.plot(geo.b_high_c[visible_high], geo.p_grid[visible_high], color=style.DARK, lw=CURVE_LINE_WIDTH)
    ax.text(geo.b_high_c[visible_high][-1] + 0.07, P_TOP + 0.02, "$u_h^c$\nverso $\\psi_h^c$", ha="left",
            va="center", **LINE_LABEL_STYLE)

    visible_low = geo.p_grid <= LOW_CURVE_P_END
    ax.plot(geo.b_low_left[visible_low], geo.p_grid[visible_low], color=style.BLUE, lw=CURVE_LINE_WIDTH)
    ax.text(geo.b_low_left[visible_low][-1] + 0.06, LOW_CURVE_P_END, "$u_l''$", ha="left", va="center",
            color=style.BLUE, fontsize=SYMBOL_SIZE)


def draw_contracts(ax, contract, geo):
    """Mark psi'', psi_l (bar) and psi' on the low-risk line and name them.

    Args:
        ax: Axes of the (B, p) plane.
        contract: The separating equilibrium of Figure 3.
        geo: Contracts and curves that bound the region.
    """
    mark_contracts(ax, [geo.b_left, contract.b_bar, geo.b_right], [geo.p_left, contract.p_bar, geo.p_right],
                   size=COMPACT_MARKER_SIZE, zorder=4)
    label_region(ax, contract, geo)
    ax.annotate("$\\psi''$", xy=(geo.b_left, geo.p_left), xytext=(-5, 5), textcoords="offset points",
                ha="right", va="bottom", fontsize=SYMBOL_SIZE)
    ax.annotate("$\\overline{\\psi}_l$", xy=(contract.b_bar, contract.p_bar), xytext=(4, -5),
                textcoords="offset points", ha="left", va="top", fontsize=SYMBOL_SIZE)
    ax.annotate("$\\psi'$", xy=(geo.b_right, geo.p_right), xytext=(4, -5), textcoords="offset points",
                ha="left", va="top", fontsize=SYMBOL_SIZE)


def label_region(ax, contract, geo):
    """Name the shaded region with a label that points into it.

    Args:
        ax: Axes of the (B, p) plane.
        contract: The separating equilibrium of Figure 3.
        geo: Contracts and curves that bound the region.
    """
    b_label = 0.5 * (geo.b_left + contract.b_bar) + 0.1
    p_label = 0.5 * (PI_LOW * b_label + np.interp(b_label, geo.b_low_left, geo.p_grid))
    ax.annotate(r"$\mathcal{R}$", xy=(b_label, p_label), xytext=REGION_LABEL_XY, ha="center", va="center",
                fontsize=SYMBOL_SIZE, arrowprops=leader_line(shrink_a=7, shrink_b=0))


def main():
    """Render the figure."""
    contract = separating_contract()
    geo = build_geometry(contract)
    fig, ax = new_plane(HEIGHT_RATIO, XMAX, YMAX)

    shade_region(ax, contract, geo)
    draw_reference_lines(ax)
    draw_indifference_curves(ax, geo)
    draw_contracts(ax, contract, geo)

    ax.set(xticks=[], yticks=[])
    decorate_axes(ax)

    save_figure(fig, "fig04")


if __name__ == "__main__":
    main()
