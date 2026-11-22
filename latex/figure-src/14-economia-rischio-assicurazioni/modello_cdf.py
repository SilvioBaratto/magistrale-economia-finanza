"""Step c.d.f. model and plot furniture shared by the figures of ERA chapter 04.

A finite lottery is a list of values with their probabilities. Its c.d.f. is a right-continuous step
function, and the integral of the c.d.f. that the second-order condition compares is piecewise linear, so
both are computed exactly from the atoms and never by numerical quadrature.

The figure scripts import this module by name: Python puts the folder of a running script on sys.path.
"""
import sys
from fractions import Fraction
from pathlib import Path
from typing import NamedTuple

import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# Scripts are run as plain files, so the shared style module is only importable once its folder is
# added by hand.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style  # noqa: E402

ASSET_DIR = style.REPO / "obsidian/14-Economia-Rischio-Assicurazioni/assets/era-04"

# Font sizes of tick labels, and of the symbols that name axes and curves; the larger size keeps
# the subscripts and limits of those symbols above 7 pt once the figure is scaled to the page.
LABEL_SIZE = 10
SYMBOL_SIZE = 11
TICK_LENGTH = 3
OPEN_MARKER_EDGE_WIDTH = 1.0
# Vertical room kept below 0 and above 1, so that a c.d.f. equal to 0 or 1 does not run along a spine.
PROBABILITY_AXIS_RANGE = (-0.05, 1.05)
GAP_SHADE_ALPHA = 0.18
# The shaded gap between two c.d.f.s is drawn under the curves.
SHADE_Z_ORDER = 1
# Offset in points of the axis names: the x name below the right end of its axis, the y name above the top.
X_AXIS_NAME_OFFSET = (0, -6)
Y_AXIS_NAME_OFFSET = (0, 4)
# Distance of the label of a plateau from the plateau, in probability units.
PLATEAU_LABEL_OFFSET = 0.07
# Largest denominator that fraction_label accepts for a probability read off the model.
MAX_DENOMINATOR = 12
# Thin dotted guide that carries a level from an axis to the point it belongs to.
GUIDE_LINE_STYLE = dict(color=style.GREY, lw=0.9, ls=(0, (1, 2.5)), zorder=1)


class Lottery(NamedTuple):
    """A finite lottery.

    Attributes:
        values: Outcomes in increasing order.
        probs: Probability of each outcome; they add up to 1.
    """

    values: tuple[float, ...]
    probs: tuple[float, ...]


class CurveStyle(NamedTuple):
    """How a curve and its jump markers are drawn.

    Attributes:
        color: Line and marker colour.
        line_width: Line width in points.
        marker_size: Size in points of the dots at the jumps.
        zorder: Drawing order of the line; its dots sit half a step above.
    """

    color: str
    line_width: float
    marker_size: float
    zorder: float


# Where two curves coincide (the c.d.f.s outside the stretch on which they differ) the second one is
# drawn thinner on top of the first, so that both stay visible.
FIRST_CURVE = CurveStyle(style.DARK, 3.2, 6.0, 2)
SECOND_CURVE = CurveStyle(style.BLUE, 1.5, 3.6, 3)


def cdf(lottery: Lottery, x):
    """Return the c.d.f. of a lottery.

    Args:
        lottery: The lottery.
        x: Point or array of points.

    Returns:
        P(X <= x), with the shape of ``x``; the function is continuous from the right.
    """
    reached = np.asarray(x, dtype=float)[..., None] >= np.asarray(lottery.values)
    return np.sum(np.asarray(lottery.probs) * reached, axis=-1)


def integrated_cdf(lottery: Lottery, lower: float, x):
    """Return the integral of the c.d.f. from ``lower`` to ``x``.

    An atom of mass m at v adds m to the c.d.f. from v on, so it adds m * (x - max(v, lower)) to the
    integral once x has passed it.

    Args:
        lottery: The lottery.
        lower: Lower limit of the integral, not above the smallest value of the lottery.
        x: Point or array of points; below ``lower`` the integral is 0.

    Returns:
        The integral, with the shape of ``x``.
    """
    start = np.maximum(np.asarray(lottery.values), lower)
    run = np.maximum(np.asarray(x, dtype=float)[..., None] - start, 0.0)
    return np.sum(np.asarray(lottery.probs) * run, axis=-1)


def draw_step_cdf(ax: Axes, lottery: Lottery, x_range: tuple[float, float], curve: CurveStyle) -> None:
    """Draw the c.d.f. of a lottery as steps with a dot at each jump.

    The dot is filled on the level the function takes at the jump and open on the level it leaves, which
    shows that the c.d.f. is continuous from the right.

    Args:
        ax: Axes to draw on.
        lottery: The lottery.
        x_range: Left and right ends of the drawn stretch.
        curve: Colour, widths and drawing order.
    """
    knots = np.concatenate([[x_range[0]], lottery.values, [x_range[1]]])
    levels = np.concatenate([[0.0], np.cumsum(lottery.probs)])
    ax.hlines(levels, knots[:-1], knots[1:], color=curve.color, lw=curve.line_width, zorder=curve.zorder)
    dots = dict(ms=curve.marker_size, zorder=curve.zorder + 0.5)
    ax.plot(lottery.values, levels[1:], "o", color=curve.color, **dots)
    ax.plot(lottery.values, levels[:-1], "o", mfc="white", mec=curve.color, mew=OPEN_MARKER_EDGE_WIDTH,
            **dots)


def draw_step_cdfs(ax: Axes, first: Lottery, second: Lottery, x_range: tuple[float, float]) -> None:
    """Draw the step c.d.f.s of two lotteries, the first one under the second.

    Args:
        ax: Axes to draw on.
        first: Lottery drawn in the first style.
        second: Lottery drawn in the second style.
        x_range: Left and right ends of the drawn stretch.
    """
    draw_step_cdf(ax, first, x_range, FIRST_CURVE)
    draw_step_cdf(ax, second, x_range, SECOND_CURVE)


def shade_between(ax: Axes, x, lower, upper) -> None:
    """Shade the region between two curves that are linear between the points ``x``.

    Args:
        ax: Axes to draw on.
        x: Abscissas where either curve changes slope.
        lower: Ordinates of the lower curve at ``x``.
        upper: Ordinates of the upper curve at ``x``.
    """
    ax.fill_between(x, lower, upper, color=style.BLUE, alpha=GAP_SHADE_ALPHA, lw=0, zorder=SHADE_Z_ORDER)


def shade_cdf_gap(ax: Axes, first: Lottery, second: Lottery, x_start: float, x_end: float) -> float:
    """Shade the region between two c.d.f.s over a stretch where each is constant.

    Args:
        ax: Axes to draw on.
        first: Lottery whose c.d.f. is the upper one on the stretch.
        second: Lottery whose c.d.f. is the lower one on the stretch.
        x_start: Left end of the stretch.
        x_end: Right end of the stretch.

    Returns:
        The height of the shaded region.
    """
    middle = (x_start + x_end) / 2
    upper, lower = float(cdf(first, middle)), float(cdf(second, middle))
    shade_between(ax, [x_start, x_end], [lower, lower], [upper, upper])
    return upper - lower


def draw_comparison(ax: Axes, first: Lottery, second: Lottery, x_range: tuple[float, float],
                    gap: tuple[float, float]) -> float:
    """Draw two step c.d.f.s and shade the region between them over one stretch.

    Args:
        ax: Axes to draw on.
        first: Lottery whose c.d.f. is the upper one on ``gap``.
        second: Lottery whose c.d.f. is the lower one on ``gap``.
        x_range: Left and right ends of the drawn stretch.
        gap: Stretch on which both c.d.f.s are constant and differ.

    Returns:
        The height of the shaded region.
    """
    height = shade_cdf_gap(ax, first, second, *gap)
    draw_step_cdfs(ax, first, second, x_range)
    return height


def fraction_label(value: float) -> str:
    """Write a probability as a fraction, so a tick shows the value the model computed.

    The slash form keeps the digits at the size of the other labels; a stacked fraction would set them
    in script size, too small once the figure is scaled to the page.

    Args:
        value: Probability whose denominator is at most ``MAX_DENOMINATOR``.

    Returns:
        A mathtext string such as ``$1/3$``, or ``$1$`` for a whole number.
    """
    exact = Fraction(value).limit_denominator(MAX_DENOMINATOR)
    if exact.denominator == 1:
        return f"${exact.numerator}$"
    return f"${exact.numerator}/{exact.denominator}$"


def fraction_ticks(values) -> tuple[list[float], list[str]]:
    """Return tick positions with their fraction labels, in the form ``set_up_axes`` takes.

    Args:
        values: Tick positions that are probabilities.

    Returns:
        The positions and, for each, its ``fraction_label``.
    """
    return list(values), [fraction_label(value) for value in values]


def level_guide(ax: Axes, level: float, x_end: float) -> None:
    """Draw a dotted guide from the vertical axis to ``x_end`` at the given level.

    Args:
        ax: Axes to draw on, with its x limits already set.
        level: Ordinate of the guide.
        x_end: Abscissa where the guide stops.
    """
    ax.hlines(level, ax.get_xlim()[0], x_end, **GUIDE_LINE_STYLE)


def label_curve(ax: Axes, xy: tuple[float, float], text: str, curve: CurveStyle) -> None:
    """Write the symbol of a curve in the colour of the curve.

    Args:
        ax: Axes to draw on.
        xy: Centre of the label in data coordinates.
        text: Label, a mathtext string.
        curve: Style whose colour the label takes.
    """
    ax.text(*xy, text, color=curve.color, ha="center", va="center", fontsize=SYMBOL_SIZE)


def set_up_axes(ax: Axes, xlim, ylim, xticks, yticks) -> None:
    """Set limits and labelled ticks.

    Args:
        ax: Axes to set up.
        xlim: Left and right limits.
        ylim: Bottom and top limits.
        xticks: ``(positions, labels)`` of the x ticks.
        yticks: ``(positions, labels)`` of the y ticks.
    """
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks(*xticks)
    ax.set_yticks(*yticks)
    ax.tick_params(length=TICK_LENGTH, labelsize=LABEL_SIZE)


def name_y_axis(ax: Axes, name: str) -> None:
    """Write the name of the vertical axis above its top end.

    Args:
        ax: Axes to name.
        name: Name of the axis, a mathtext string.
    """
    ax.annotate(name, xy=(0, 1), xycoords="axes fraction", xytext=Y_AXIS_NAME_OFFSET,
                textcoords="offset points", ha="left", va="bottom", fontsize=SYMBOL_SIZE)


def name_axes(ax: Axes, x_name: str, y_name: str) -> None:
    """Write the name of each axis at its far end.

    Args:
        ax: Axes to name.
        x_name: Name of the horizontal axis, a mathtext string; it sits below the right end.
        y_name: Name of the vertical axis, a mathtext string; it sits above the top end.
    """
    ax.annotate(x_name, xy=(1, 0), xycoords="axes fraction", xytext=X_AXIS_NAME_OFFSET,
                textcoords="offset points", ha="right", va="top", fontsize=SYMBOL_SIZE)
    name_y_axis(ax, y_name)


def save_figure(fig: Figure, name: str) -> Path:
    """Write the figure as PNG and PDF in the assets folder of chapter 04.

    Args:
        fig: The finished figure.
        name: File name without extension, for example ``fig01``.

    Returns:
        The PNG path.
    """
    return style.save(fig, ASSET_DIR / f"{name}.png")
