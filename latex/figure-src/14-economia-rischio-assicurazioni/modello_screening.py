"""Screening model and plot furniture shared by the figures of ERA chapter 07.

An insurer serves two types of customer, low and high risk, that differ only in their accident
probability. A contract (B, p) pays the indemnity B on a loss for the premium p. The figures draw the
indifference curves of the two types and the zero-profit lines p = pi * B in the (B, p) plane.

The figure scripts import this module by name: Python puts the folder of a running script on sys.path.
"""
import sys
from pathlib import Path
from typing import NamedTuple

import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from scipy.optimize import brentq

# Scripts are run as plain files, so the shared style module is only importable once its folder is
# added by hand.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style  # noqa: E402

# Worked example of the chapter. The teacher's curves are schematic and more bent than the ones these
# values give; both share the structure (high-risk curve steeper, a single crossing).
WEALTH = 10.0
LOSS = 6.0
PI_LOW = 0.15
PI_HIGH = 0.5

# Distance kept from the ends 0 and LOSS of the indemnity range when bracketing a root.
BRACKET_MARGIN = 1e-6
# Upper end of the premium bracket in premium_on_curve, above every premium the figures reach.
PREMIUM_SEARCH_MAX = 1.5

ASSET_DIR = style.REPO / "obsidian/14-Economia-Rischio-Assicurazioni/assets/era-07"

# Font sizes of axis, line and tick labels, and of the symbols that name curves and contracts.
LABEL_SIZE = 10
SYMBOL_SIZE = 11
TICK_LENGTH = 3
CURVE_LINE_WIDTH = 2.0
ZERO_PROFIT_LINE_WIDTH = 1.0
CONTRACT_MARKER_SIZE = 6
COMPACT_MARKER_SIZE = 5.5
# Size and spacing of the multi-line labels written next to a line.
LINE_LABEL_STYLE = dict(fontsize=LABEL_SIZE, linespacing=1.15)
# Thin dashed guide that drops from a contract onto the axes.
GUIDE_LINE_STYLE = dict(color=style.GREY, lw=0.9, ls=(0, (4, 3)), zorder=1)


class SeparatingContract(NamedTuple):
    """Separating equilibrium of the worked example.

    The high-risk type buys full cover at its fair premium (psi_h^c). The low-risk type gets the
    largest indemnity on its own zero-profit line that the high-risk type does not prefer to psi_h^c.

    Attributes:
        u_high_c: Utility of the high-risk type at psi_h^c = (LOSS, PI_HIGH * LOSS).
        b_bar: Indemnity of the low-risk contract psi_l bar.
        p_bar: Premium of psi_l bar, on the line p = PI_LOW * B.
        u_low_bar: Utility of the low-risk type at psi_l bar.
    """

    u_high_c: float
    b_bar: float
    p_bar: float
    u_low_bar: float


def expected_utility(pi, b, p):
    """Return the expected log utility of a type holding the contract (b, p).

    Args:
        pi: Accident probability of the type.
        b: Indemnity paid when the loss occurs.
        p: Premium, paid in both states.

    Returns:
        Expected utility, with the shape of the broadcast arguments.
    """
    return pi * np.log(WEALTH - p - LOSS + b) + (1 - pi) * np.log(WEALTH - p)


def indemnity_on_curve(pi, level, p):
    """Return the indemnity that keeps a type at a given utility for the premium p.

    The inversion is closed form because the utility is logarithmic.

    Args:
        pi: Accident probability of the type.
        level: Utility the indifference curve stands for.
        p: Premium; may be an array.

    Returns:
        Indemnity B on the curve, with the shape of ``p``.
    """
    wealth_no_loss = WEALTH - p
    return np.exp((level - (1 - pi) * np.log(wealth_no_loss)) / pi) - wealth_no_loss + LOSS


def premium_on_curve(pi, level, b):
    """Return the premium at which the indifference curve has the indemnity b.

    Args:
        pi: Accident probability of the type.
        level: Utility the indifference curve stands for.
        b: Indemnity at which the curve is read.

    Returns:
        The premium p in [0, PREMIUM_SEARCH_MAX] with ``indemnity_on_curve(pi, level, p) == b``.

    Raises:
        ValueError: If the curve does not reach b within the search bracket.
    """
    return brentq(lambda p: indemnity_on_curve(pi, level, p) - b, 0.0, PREMIUM_SEARCH_MAX)


def separating_contract() -> SeparatingContract:
    """Solve the separating equilibrium of the worked example.

    Returns:
        The utilities and the low-risk contract that the figures draw.
    """
    u_high_c = expected_utility(PI_HIGH, LOSS, PI_HIGH * LOSS)
    b_bar = brentq(lambda b: expected_utility(PI_HIGH, b, PI_LOW * b) - u_high_c,
                   BRACKET_MARGIN, LOSS - BRACKET_MARGIN)
    p_bar = PI_LOW * b_bar
    return SeparatingContract(u_high_c, b_bar, p_bar, expected_utility(PI_LOW, b_bar, p_bar))


def new_plane(height_ratio: float, xmax: float, ymax: float) -> tuple[Figure, Axes]:
    """Create a figure whose axes show the (B, p) plane from the origin.

    Args:
        height_ratio: Height of the figure as a fraction of its width.
        xmax: Right limit of the B axis.
        ymax: Top limit of the p axis.

    Returns:
        The ``(fig, ax)`` pair.
    """
    fig, ax = style.figure(height_ratio=height_ratio)
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    return fig, ax


def plot_full_cover_line(ax: Axes, end: float) -> None:
    """Draw the dashed line p = B, where the premium equals the indemnity.

    Args:
        ax: Axes of the (B, p) plane.
        end: Value of B and p at which the line stops.
    """
    ax.plot([0, end], [0, end], color=style.GREY, lw=1.2, ls=(0, (5, 3)))


def plot_zero_profit_line(ax: Axes, pi: float, b_end: float, color: str,
                          lw: float = ZERO_PROFIT_LINE_WIDTH) -> None:
    """Draw the zero-profit line p = pi * B of a type.

    Args:
        ax: Axes of the (B, p) plane.
        pi: Accident probability of the type.
        b_end: Indemnity at which the line stops.
        color: Line colour.
        lw: Line width in points.
    """
    ax.plot([0, b_end], [0, pi * b_end], color=color, lw=lw)


def mark_contracts(ax: Axes, b, p, size: float = CONTRACT_MARKER_SIZE, zorder: int = 3) -> None:
    """Mark contracts as dots in the (B, p) plane.

    Args:
        ax: Axes of the (B, p) plane.
        b: Indemnity of each contract.
        p: Premium of each contract.
        size: Marker size in points.
        zorder: Drawing order; raise it where a curve or a region would cover the dot.
    """
    ax.plot(b, p, "o", color=style.DARK, ms=size, zorder=zorder)


def leader_line(shrink_a: float, shrink_b: float) -> dict:
    """Return the arrow properties of a thin line that leads from a label to the point it names.

    Args:
        shrink_a: Gap in points kept at the label end.
        shrink_b: Gap in points kept at the point end.

    Returns:
        Keyword arguments for the ``arrowprops`` of ``Axes.annotate``.
    """
    return dict(arrowstyle="-", color=style.DARK, lw=0.7, shrinkA=shrink_a, shrinkB=shrink_b)


def draw_axes_frame(ax: Axes) -> None:
    """Thicken the left and bottom spines and end them with arrowheads, as the slides do.

    Args:
        ax: Axes of the (B, p) plane.
    """
    for spine in ("left", "bottom"):
        ax.spines[spine].set_linewidth(1.0)
    ax.plot(1, 0, ">", color=style.DARK, ms=5, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^", color=style.DARK, ms=5, transform=ax.get_xaxis_transform(), clip_on=False)


def decorate_axes(ax: Axes) -> None:
    """Give the axes the frame, the B and p names and the 0 of the origin.

    Args:
        ax: Axes of the (B, p) plane, with its own ticks already set.
    """
    ax.annotate("$B$", xy=(1, 0), xycoords="axes fraction", xytext=(0, -6), textcoords="offset points",
                ha="right", va="top", fontsize=LABEL_SIZE)
    ax.annotate("$p$", xy=(0, 1), xycoords="axes fraction", xytext=(8, -2), textcoords="offset points",
                ha="left", va="top", fontsize=LABEL_SIZE)
    draw_axes_frame(ax)
    ax.text(-0.01, -0.02, "0", transform=ax.transAxes, ha="right", va="top", fontsize=LABEL_SIZE)


def save_figure(fig: Figure, name: str) -> Path:
    """Write the figure as PNG and PDF in the assets folder of chapter 07.

    Args:
        fig: The finished figure.
        name: File name without extension, for example ``fig01``.

    Returns:
        The PNG path.
    """
    return style.save(fig, ASSET_DIR / f"{name}.png")
