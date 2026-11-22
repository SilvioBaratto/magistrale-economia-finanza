"""ERA 02, slide 20: the Allais options in the Machina triangle, with the indifference lines of an
expected-utility maximiser."""
import math

import numpy as np

from modello_triangolo import (ARROW_PROPS, LABEL_SIZE, LINE_SPACING, draw_axes, draw_triangle,
                               indifference_slope, label_vertices, lottery_point, mark_points,
                               new_triangle_plane, save_figure, segment_slope, style)

# Probabilities of (nothing, 1 million, 5 million), from the table of the chapter.
OPTIONS = {
    "1A": (0.00, 1.00, 0.00),
    "1B": (0.01, 0.89, 0.10),
    "2A": (0.89, 0.11, 0.00),
    "2B": (0.90, 0.00, 0.10),
}
# Utilities u(0), u(1 million), u(5 million) used to draw the indifference lines: the example of the chapter.
UTILITIES = (0.0, 1.0, 3.0)
# Slopes the chapter states for the segments 1A-1B and 2A-2B and for the indifference lines.
CHAPTER_SEGMENT_SLOPE = 10.0
CHAPTER_INDIFFERENCE_SLOPE = 0.5

VERTEX_TEXTS = ("$L_1$\n(0 certo)", "1A = $L_2$\n(1 mln certo)", "$L_3$\n(5 mln certi)")
SEGMENT_WIDTH = 2.4
INDIFFERENCE_WIDTH = 1.1
LINES_LABEL_TEXT = "rette di\nindifferenza"
LINES_LABEL_XY = (0.70, 0.365)

# Offset in points, horizontal and vertical alignment of the label of each option. 1A has none: it is the
# vertex L2 and takes its name from the vertex label. The others stay clear of the lines and the axes.
OPTION_LABELS = {
    "1B": dict(xytext=(-6, 0), ha="right", va="center"),
    "2A": dict(xytext=(0, -6), ha="center", va="top"),
    "2B": dict(xytext=(7, 5), ha="left", va="bottom"),
}

# Start, length (in plane units) and appearance of the arrow of growing utility, drawn in the empty
# corner above the highest line.
ARROW_START = (0.24, 0.30)
ARROW_LENGTH = 0.30
ARROW_LABEL_OFFSET = (8, 0)


def option_points() -> dict:
    """Return the point of the triangle of each Allais option.

    Returns:
        Map from the option name to its coordinates ``(p1, p3)``.
    """
    return {name: lottery_point(probabilities) for name, probabilities in OPTIONS.items()}


def check_chapter_geometry(points: dict, slope_of_lines: float) -> None:
    """Check that the points and the utilities reproduce the slopes the chapter states.

    Args:
        points: Coordinates of the four options, as returned by ``option_points``.
        slope_of_lines: Slope of the indifference lines drawn.

    Raises:
        ValueError: If a segment is not parallel to the other, or a slope differs from the chapter.
    """
    first = segment_slope(points["1A"], points["1B"])
    second = segment_slope(points["2A"], points["2B"])
    if not (math.isclose(first, CHAPTER_SEGMENT_SLOPE) and math.isclose(second, CHAPTER_SEGMENT_SLOPE)):
        raise ValueError(f"Segment slopes {first}, {second} differ from {CHAPTER_SEGMENT_SLOPE}")
    if not math.isclose(slope_of_lines, CHAPTER_INDIFFERENCE_SLOPE):
        raise ValueError(f"Indifference slope {slope_of_lines} differs from {CHAPTER_INDIFFERENCE_SLOPE}")


def draw_indifference_lines(ax, triangle, points, slope):
    """Draw the indifference line through each option, cut at the sides of the triangle.

    Args:
        ax: Axes of the (p1, p3) plane.
        triangle: Triangle patch used as clip path.
        points: Coordinates of the four options.
        slope: Common slope of the lines.
    """
    for point in points.values():
        line = ax.axline(point, slope=slope, color=style.BLUE, lw=INDIFFERENCE_WIDTH)
        line.set_clip_path(triangle)


def draw_utility_arrow(ax, slope):
    """Draw the arrow of growing utility, perpendicular to the indifference lines.

    Utility is U = u2 + p1 (u1 - u2) + p3 (u3 - u2); its gradient (u1 - u2, u3 - u2) is perpendicular to
    the lines, and the plane has equal scale, so the arrow looks perpendicular too. It points up and left.

    Args:
        ax: Axes of the (p1, p3) plane.
        slope: Slope of the indifference lines.
    """
    direction = np.array([-slope, 1.0]) / np.hypot(slope, 1.0)
    end = np.array(ARROW_START) + ARROW_LENGTH * direction
    ax.annotate("", xy=end, xytext=ARROW_START, arrowprops=ARROW_PROPS)
    middle = (np.array(ARROW_START) + end) / 2
    ax.annotate("utilità\ncrescente", xy=middle, xytext=ARROW_LABEL_OFFSET, textcoords="offset points",
                ha="left", va="center", fontsize=LABEL_SIZE,
                linespacing=LINE_SPACING)


def main():
    """Render the figure."""
    points = option_points()
    slope = indifference_slope(*UTILITIES)
    check_chapter_geometry(points, slope)

    fig, ax = new_triangle_plane()
    triangle = draw_triangle(ax)
    draw_indifference_lines(ax, triangle, points, slope)
    draw_axes(ax)
    label_vertices(ax, VERTEX_TEXTS)

    for start, end in (("1A", "1B"), ("2A", "2B")):
        ax.plot(*zip(points[start], points[end]), color=style.DARK, lw=SEGMENT_WIDTH, solid_capstyle="round")
    mark_points(ax, list(points.values()))
    for name, placement in OPTION_LABELS.items():
        ax.annotate(name, xy=points[name], textcoords="offset points", fontsize=LABEL_SIZE, **placement)

    draw_utility_arrow(ax, slope)
    ax.text(*LINES_LABEL_XY, LINES_LABEL_TEXT, ha="left", va="center", color=style.BLUE, fontsize=LABEL_SIZE,
            linespacing=LINE_SPACING)

    save_figure(fig, "fig02")


if __name__ == "__main__":
    main()
