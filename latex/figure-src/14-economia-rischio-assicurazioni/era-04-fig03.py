"""ERA 04, slide 12: p.m.f.s, c.d.f.s and integrated c.d.f.s of X1 = (50, 1/4; 150, 1/4; 200, 1/2) and
X2 = (100, 1/2; 200, 1/2), where F2 dominates F1 at the second order but not at the first."""
import numpy as np

from modello_cdf import (FIRST_CURVE, LABEL_SIZE, PROBABILITY_AXIS_RANGE, SECOND_CURVE, Lottery, cdf,
                         draw_step_cdfs, fraction_ticks, integrated_cdf, label_curve, name_y_axis, save_figure,
                         set_up_axes, shade_between, style)

FIRST = Lottery((50.0, 150.0, 200.0), (1 / 4, 1 / 4, 1 / 2))
SECOND = Lottery((100.0, 200.0), (1 / 2, 1 / 2))
# Lower end a of the support, from which the integrals of the c.d.f.s start.
SUPPORT_START = 50.0

HEIGHT_RATIO = 0.5
X_RANGE = (30.0, 215.0)
X_TICKS = [50, 100, 150, 200]
# Width of a p.m.f. bar; the two bars of a shared value sit side by side, half a width off the value.
BAR_WIDTH = 9.0
BAR_SHIFT = BAR_WIDTH / 2
PMF_AXIS_RANGE = (0.0, 0.62)
PMF_TICKS = [0.0, 1 / 4, 1 / 2]
# Height of a label above the bar or the line it names, in the units of each panel.
PMF_LABEL_OFFSET = 0.05
CDF_LABEL_OFFSET = 0.08
CDF_FIRST_LABEL_X = 100.0
CDF_SECOND_LABEL_X = 125.0
INTEGRAL_AXIS_RANGE = (-3.0, 72.0)
INTEGRAL_TICKS = [0, 25, 50]
INTEGRAL_FIRST_LABEL_XY = (88.0, 22.0)
INTEGRAL_SECOND_LABEL_XY = (178.0, 20.0)


def draw_pmf(ax):
    """Draw the p.m.f.s as bars, the bars of a shared value side by side.

    Args:
        ax: Axes of the first panel.
    """
    for lottery, curve, shift in ((FIRST, FIRST_CURVE, -BAR_SHIFT), (SECOND, SECOND_CURVE, BAR_SHIFT)):
        ax.bar(np.asarray(lottery.values) + shift, lottery.probs, width=BAR_WIDTH, color=curve.color)
    label_curve(ax, (FIRST.values[0] - BAR_SHIFT, FIRST.probs[0] + PMF_LABEL_OFFSET), "$X_1$", FIRST_CURVE)
    label_curve(ax, (SECOND.values[0] + BAR_SHIFT, SECOND.probs[0] + PMF_LABEL_OFFSET), "$X_2$", SECOND_CURVE)
    set_up_axes(ax, X_RANGE, PMF_AXIS_RANGE, (X_TICKS, X_TICKS), fraction_ticks(PMF_TICKS))
    name_y_axis(ax, "$f(x)$")


def draw_cdfs(ax):
    """Draw the step c.d.f.s, which cross.

    Args:
        ax: Axes of the second panel.
    """
    draw_step_cdfs(ax, FIRST, SECOND, X_RANGE)
    first_level = float(cdf(FIRST, FIRST.values[0]))
    second_level = float(cdf(SECOND, SECOND.values[0]))
    label_curve(ax, (CDF_FIRST_LABEL_X, first_level + CDF_LABEL_OFFSET), "$F_1$", FIRST_CURVE)
    label_curve(ax, (CDF_SECOND_LABEL_X, second_level + CDF_LABEL_OFFSET), "$F_2$", SECOND_CURVE)
    levels = [0.0, first_level, second_level, 1.0]
    set_up_axes(ax, X_RANGE, PROBABILITY_AXIS_RANGE, (X_TICKS, X_TICKS), fraction_ticks(levels))
    name_y_axis(ax, "$F(x)$")


def draw_integrals(ax):
    """Draw the integrals of the c.d.f.s from the start of the support, and shade the gap between them.

    Both are piecewise linear with kinks at the values of the lotteries, so the lines through those
    points are exact.

    Args:
        ax: Axes of the third panel.
    """
    knots = np.unique([X_RANGE[0], SUPPORT_START, *FIRST.values, *SECOND.values, X_RANGE[1]])
    upper = integrated_cdf(FIRST, SUPPORT_START, knots)
    lower = integrated_cdf(SECOND, SUPPORT_START, knots)
    shade_between(ax, knots, lower, upper)
    for values, curve in ((upper, FIRST_CURVE), (lower, SECOND_CURVE)):
        ax.plot(knots, values, color=curve.color, lw=curve.line_width, zorder=curve.zorder)
    label_curve(ax, INTEGRAL_FIRST_LABEL_XY, r"$\int F_1$", FIRST_CURVE)
    label_curve(ax, INTEGRAL_SECOND_LABEL_XY, r"$\int F_2$", SECOND_CURVE)
    set_up_axes(ax, X_RANGE, INTEGRAL_AXIS_RANGE, (X_TICKS, X_TICKS), (INTEGRAL_TICKS, INTEGRAL_TICKS))
    name_y_axis(ax, rf"$\int_{{{SUPPORT_START:g}}}^{{x}}F$")


def main():
    """Render the figure."""
    fig, (ax_pmf, ax_cdf, ax_integral) = style.figure(1, 3, height_ratio=HEIGHT_RATIO)
    draw_pmf(ax_pmf)
    draw_cdfs(ax_cdf)
    draw_integrals(ax_integral)
    fig.supxlabel("$x$", fontsize=LABEL_SIZE)
    save_figure(fig, "fig03")


if __name__ == "__main__":
    main()
