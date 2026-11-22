"""ERA 07, slide 20: indifference curves of the two types, which cross once in the (B, p) plane."""
import numpy as np

from modello_screening import (COMPACT_MARKER_SIZE, CURVE_LINE_WIDTH, GUIDE_LINE_STYLE, LABEL_SIZE, PI_HIGH,
                               PI_LOW, TICK_LENGTH, draw_axes_frame, expected_utility, indemnity_on_curve,
                               mark_contracts, new_plane, premium_on_curve, save_figure, style)

B_CROSS, P_CROSS = 2.0, 0.6     # contract (B', p') where the two curves cross
B_REDUCED = 1.2                 # reduced indemnity B''

HEIGHT_RATIO = 0.66
XMAX, YMAX = 6.4, 1.62
CURVE_SAMPLES = 300
# The curves stop short of the axes, as in the slide.
LOW_CURVE_P_RANGE = (0.18, 1.2)
HIGH_CURVE_P_RANGE = (0.03, 1.5)
# Premium at which the utility arrow of each type leaves its curve.
LOW_ARROW_P = 0.95
HIGH_ARROW_P = 1.30
ARROW_LENGTH_PT = 40
ARROW_GAP_PT = 5
DIRECTION_LABEL_XY = (4.55, 0.30)


def utility_arrow(ax, curve, scale, at_p):
    """Draw the arrow that leaves a curve toward higher utility, down and to the right.

    Args:
        ax: Axes of the (B, p) plane.
        curve: The ``(b, p)`` arrays of the curve; the arrow starts at the sample closest to ``at_p``.
        scale: Display units per data unit along ``(x, y)``, so the arrow is perpendicular to the
            curve as the eye sees it and not in data coordinates.
        at_p: Premium at which the arrow leaves the curve.
    """
    b_curve, p_curve = curve
    sx, sy = scale
    i = int(np.argmin(np.abs(p_curve - at_p)))
    tangent = np.array([(b_curve[i + 1] - b_curve[i - 1]) * sx, (p_curve[i + 1] - p_curve[i - 1]) * sy])
    normal = np.array([tangent[1], -tangent[0]]) / np.hypot(*tangent)
    start = np.array([b_curve[i] * sx, p_curve[i] * sy]) + ARROW_GAP_PT * normal
    end = start + ARROW_LENGTH_PT * normal
    ax.annotate("", xy=(end[0] / sx, end[1] / sy), xytext=(start[0] / sx, start[1] / sy),
                arrowprops=dict(arrowstyle="-|>", color=style.DARK, lw=1.0, mutation_scale=9))


def draw_guides(ax, p_low_reduced, p_high_reduced):
    """Draw the dashed guides and the dots of the three contracts that the ticks name.

    Args:
        ax: Axes of the (B, p) plane.
        p_low_reduced: Premium p_l'' of the low-risk curve at B''.
        p_high_reduced: Premium p_h'' of the high-risk curve at B''.
    """
    ax.plot([0, B_CROSS], [P_CROSS, P_CROSS], **GUIDE_LINE_STYLE)
    ax.plot([0, B_REDUCED], [p_low_reduced, p_low_reduced], **GUIDE_LINE_STYLE)
    ax.plot([0, B_REDUCED], [p_high_reduced, p_high_reduced], **GUIDE_LINE_STYLE)
    ax.plot([B_CROSS, B_CROSS], [0, P_CROSS], **GUIDE_LINE_STYLE)
    ax.plot([B_REDUCED, B_REDUCED], [0, p_low_reduced], **GUIDE_LINE_STYLE)
    mark_contracts(ax, [B_CROSS, B_REDUCED, B_REDUCED], [P_CROSS, p_low_reduced, p_high_reduced],
                   size=COMPACT_MARKER_SIZE)
    ax.set_xticks([B_REDUCED, B_CROSS], ["$B''$", "$B'$"])
    ax.set_yticks([p_high_reduced, p_low_reduced, P_CROSS], ["$p_h''$", "$p_l''$", "$p'$"])
    ax.tick_params(length=TICK_LENGTH, labelsize=LABEL_SIZE)
    ax.set_xlabel("$B$", loc="right", labelpad=-6)
    ax.set_ylabel("$p$", loc="top", rotation=0, labelpad=-8)


def display_scale(fig, ax):
    """Return the display units per data unit of the axes along x and y.

    Args:
        fig: Figure that owns the axes.
        ax: Axes whose limits start at the origin.

    Returns:
        The ``(sx, sy)`` pair, read after drawing because constrained layout settles the box then.
    """
    fig.canvas.draw()
    box = ax.get_window_extent()
    return box.width / ax.get_xlim()[1], box.height / ax.get_ylim()[1]


def main():
    """Render the figure."""
    level_low = expected_utility(PI_LOW, B_CROSS, P_CROSS)
    level_high = expected_utility(PI_HIGH, B_CROSS, P_CROSS)
    p_low_reduced = premium_on_curve(PI_LOW, level_low, B_REDUCED)
    p_high_reduced = premium_on_curve(PI_HIGH, level_high, B_REDUCED)

    p_low = np.linspace(*LOW_CURVE_P_RANGE, CURVE_SAMPLES)
    p_high = np.linspace(*HIGH_CURVE_P_RANGE, CURVE_SAMPLES)
    b_low = indemnity_on_curve(PI_LOW, level_low, p_low)
    b_high = indemnity_on_curve(PI_HIGH, level_high, p_high)

    fig, ax = new_plane(HEIGHT_RATIO, XMAX, YMAX)
    ax.plot(b_low, p_low, color=style.BLUE, lw=CURVE_LINE_WIDTH, solid_capstyle="round")
    ax.plot(b_high, p_high, color=style.DARK, lw=CURVE_LINE_WIDTH, solid_capstyle="round")
    draw_guides(ax, p_low_reduced, p_high_reduced)
    draw_axes_frame(ax)

    ax.text(b_high[-1] + 0.1, p_high[-1], r"$u_h=\mathrm{costante}$", ha="left", va="center", color=style.DARK,
            fontsize=LABEL_SIZE)
    ax.text(b_low[-1] + 0.1, p_low[-1], r"$u_l=\mathrm{costante}$", ha="left", va="center", color=style.BLUE,
            fontsize=LABEL_SIZE)

    scale = display_scale(fig, ax)
    utility_arrow(ax, (b_high, p_high), scale, HIGH_ARROW_P)
    utility_arrow(ax, (b_low, p_low), scale, LOW_ARROW_P)
    ax.text(*DIRECTION_LABEL_XY, "direzione di\nutilità crescente", ha="center", va="center", fontsize=LABEL_SIZE)

    save_figure(fig, "fig01")


if __name__ == "__main__":
    main()
