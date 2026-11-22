"""Machina triangle and plot furniture shared by the figures of ERA chapter 02.

With three prizes x1 < x2 < x3 a lottery is the probability triple (p1, p2, p3). Since p2 = 1 - p1 - p3 it
is the point (p1, p3) of the triangle T = {p1 >= 0, p3 >= 0, p1 + p3 <= 1}. The figures draw T with p1 on
the horizontal axis and p3 on the vertical one, in true scale: the slopes quoted in the chapter (10 for the
Allais segments, 1/2 for the indifference lines) are read in these coordinates.

The figure scripts import this module by name: Python puts the folder of a running script on sys.path.
"""
import math
import sys
from pathlib import Path
from typing import Sequence

from matplotlib.axes import Axes
from matplotlib.colors import to_rgba
from matplotlib.figure import Figure
from matplotlib.patches import Polygon

# Scripts are run as plain files, so the shared style module is only importable once its folder is
# added by hand.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import style  # noqa: E402

Point = tuple[float, float]

# Degenerate lotteries: the prize x1, x2 or x3 with certainty.
VERTEX_L1: Point = (1.0, 0.0)
VERTEX_L2: Point = (0.0, 0.0)
VERTEX_L3: Point = (0.0, 1.0)
VERTICES = (VERTEX_L1, VERTEX_L2, VERTEX_L3)

# Tolerance on the sum of the three probabilities of a lottery.
PROBABILITY_TOLERANCE = 1e-9

ASSET_DIR = style.REPO / "obsidian/14-Economia-Rischio-Assicurazioni/assets/era-02"

HEIGHT_RATIO = 0.70
# The window leaves room on the right for the p1 axis name and the labels of the vertices, and above for
# the p3 axis name.
X_LIMITS = (-0.22, 1.45)
Y_LIMITS = (-0.17, 1.22)
# The axes run past the vertices L1 and L3, so the arrowheads sit outside the triangle.
AXIS_END_X = 1.22
AXIS_END_Y = 1.12

LABEL_SIZE = 10
OUTLINE_WIDTH = 1.0
ARROW_HEAD_SIZE = 9
# Arrow with a filled head, shared by the axes and by the arrow of growing utility.
ARROW_PROPS = dict(arrowstyle="-|>", color=style.DARK, lw=OUTLINE_WIDTH, mutation_scale=ARROW_HEAD_SIZE,
                   shrinkA=0, shrinkB=0)
# Line spacing of the two-line labels.
LINE_SPACING = 1.15
# Offset in points of the axis names from the arrow tips: p1 to the right, p3 above.
AXIS_NAME_P1_OFFSET = (5, 0)
AXIS_NAME_P3_OFFSET = (0, 4)
VERTEX_MARKER_SIZE = 3.5
POINT_MARKER_SIZE = 5.5
FILL_ALPHA = 0.08
FILL_Z_ORDER = 0
POINT_Z_ORDER = 4

# Offset in points, alignment and anchor of the label of each vertex, in the order of VERTICES. The
# labels stay outside the triangle: L1 below right, L2 below, L3 above right.
VERTEX_LABEL_PLACEMENT = (
    dict(xytext=(5, -6), ha="left", va="top"),
    dict(xytext=(0, -6), ha="center", va="top"),
    dict(xytext=(7, 3), ha="left", va="bottom"),
)


def lottery_point(probabilities: Sequence[float]) -> Point:
    """Return the point of the triangle that represents a lottery on three prizes.

    Args:
        probabilities: Probabilities ``(p1, p2, p3)`` of the prizes x1 < x2 < x3.

    Returns:
        The coordinates ``(p1, p3)``.

    Raises:
        ValueError: If there are not three probabilities, one is negative or they do not sum to 1.
    """
    if len(probabilities) != 3:
        raise ValueError(f"A lottery on three prizes needs three probabilities, got {len(probabilities)}")
    if min(probabilities) < 0 or not math.isclose(sum(probabilities), 1.0, abs_tol=PROBABILITY_TOLERANCE):
        raise ValueError(f"Not a probability vector: {tuple(probabilities)}")
    return probabilities[0], probabilities[2]


def compound_lottery(alpha: float, point_a: Point, point_b: Point) -> Point:
    """Return the compound lottery alpha * L^a + (1 - alpha) * L^b.

    Args:
        alpha: Weight of L^a, between 0 and 1.
        point_a: Coordinates ``(p1, p3)`` of L^a.
        point_b: Coordinates ``(p1, p3)`` of L^b.

    Returns:
        The point of the segment from L^a to L^b whose distance from L^b is ``alpha`` times the length
        of the segment.
    """
    return tuple(alpha * a + (1 - alpha) * b for a, b in zip(point_a, point_b))


def segment_slope(start: Point, end: Point) -> float:
    """Return the slope dp3/dp1 of the segment between two lotteries.

    Args:
        start: First lottery ``(p1, p3)``.
        end: Second lottery ``(p1, p3)``, with a different p1.

    Returns:
        The slope of the segment in the (p1, p3) plane.
    """
    return (end[1] - start[1]) / (end[0] - start[0])


def indifference_slope(u1: float, u2: float, u3: float) -> float:
    """Return the slope of the indifference lines of an expected-utility maximiser.

    The expected utility is U = u2 + p1 * (u1 - u2) + p3 * (u3 - u2), so U is constant along the lines
    of slope (u2 - u1) / (u3 - u2) and grows with p3 and falls with p1.

    Args:
        u1: Utility of the lowest prize.
        u2: Utility of the middle prize.
        u3: Utility of the highest prize, above u2 and above u1.

    Returns:
        The slope dp3/dp1 of the indifference lines.
    """
    return (u2 - u1) / (u3 - u2)


def new_triangle_plane() -> tuple[Figure, Axes]:
    """Create a figure for the triangle: true scale, no frame, room for the labels around it.

    Returns:
        The ``(fig, ax)`` pair.
    """
    fig, ax = style.figure(height_ratio=HEIGHT_RATIO)
    ax.set_xlim(*X_LIMITS)
    ax.set_ylim(*Y_LIMITS)
    # With equal scale a direction perpendicular on the screen is perpendicular in (p1, p3), which the
    # arrow of growing utility relies on.
    ax.set_aspect("equal", adjustable="box")
    ax.set_axis_off()
    return fig, ax


def draw_triangle(ax: Axes) -> Polygon:
    """Draw the triangle T as a lightly filled outline with a dot on each vertex.

    Args:
        ax: Axes of the (p1, p3) plane.

    Returns:
        The triangle patch, which a caller can use as clip path to keep lines inside T.
    """
    triangle = Polygon(VERTICES, closed=True, facecolor=to_rgba(style.BLUE, FILL_ALPHA),
                       edgecolor=style.DARK, linewidth=OUTLINE_WIDTH, zorder=FILL_Z_ORDER)
    ax.add_patch(triangle)
    mark_points(ax, VERTICES, VERTEX_MARKER_SIZE)
    return triangle


def draw_axes(ax: Axes) -> None:
    """Draw the p1 and p3 axes from the origin, with arrowheads and names.

    Args:
        ax: Axes of the (p1, p3) plane.
    """
    for end in ((AXIS_END_X, 0.0), (0.0, AXIS_END_Y)):
        ax.annotate("", xy=end, xytext=VERTEX_L2, arrowprops=ARROW_PROPS)
    ax.annotate(r"$\pi_1$", xy=(AXIS_END_X, 0.0), xytext=AXIS_NAME_P1_OFFSET, textcoords="offset points",
                ha="left", va="center", fontsize=LABEL_SIZE)
    ax.annotate(r"$\pi_3$", xy=(0.0, AXIS_END_Y), xytext=AXIS_NAME_P3_OFFSET, textcoords="offset points",
                ha="center", va="bottom", fontsize=LABEL_SIZE)


def label_vertices(ax: Axes, labels: Sequence[str]) -> None:
    """Write a label next to each vertex, outside the triangle.

    Args:
        ax: Axes of the (p1, p3) plane.
        labels: Texts for L1, L2 and L3, in this order; two-line texts are allowed.
    """
    for vertex, text, placement in zip(VERTICES, labels, VERTEX_LABEL_PLACEMENT):
        ax.annotate(text, xy=vertex, textcoords="offset points", fontsize=LABEL_SIZE,
                    linespacing=LINE_SPACING, **placement)


def mark_points(ax: Axes, points: Sequence[Point], size: float = POINT_MARKER_SIZE) -> None:
    """Mark lotteries as dots.

    Args:
        ax: Axes of the (p1, p3) plane.
        points: Coordinates ``(p1, p3)`` of the lotteries.
        size: Marker size in points.
    """
    xs, ys = zip(*points)
    ax.plot(xs, ys, "o", color=style.DARK, ms=size, zorder=POINT_Z_ORDER)


def save_figure(fig: Figure, name: str) -> Path:
    """Write the figure as PNG and PDF in the assets folder of chapter 02.

    Args:
        fig: The finished figure.
        name: File name without extension, for example ``fig01``.

    Returns:
        The PNG path.
    """
    return style.save(fig, ASSET_DIR / f"{name}.png")
