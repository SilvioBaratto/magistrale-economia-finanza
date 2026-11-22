"""ERA 04, slide 6: c.d.f.s of X1 = (0, 1/2; 1, 1/2) and X2 = (0, 1/3; 1, 2/3), where F2 lies below F1."""
from modello_cdf import (FIRST_CURVE, LABEL_SIZE, PLATEAU_LABEL_OFFSET, PROBABILITY_AXIS_RANGE, SECOND_CURVE,
                         Lottery, cdf, draw_comparison, fraction_label, fraction_ticks, label_curve, level_guide,
                         name_axes, save_figure, set_up_axes, style)

FIRST = Lottery((0.0, 1.0), (1 / 2, 1 / 2))
SECOND = Lottery((0.0, 1.0), (1 / 3, 2 / 3))

X_RANGE = (-0.5, 1.5)
# The only stretch on which the two c.d.f.s differ.
GAP = (0.0, 1.0)


def main():
    """Render the figure."""
    middle = sum(GAP) / 2
    level_first, level_second = float(cdf(FIRST, middle)), float(cdf(SECOND, middle))

    fig, ax = style.figure()
    set_up_axes(ax, X_RANGE, PROBABILITY_AXIS_RANGE,
                fraction_ticks(GAP), fraction_ticks([0, level_second, level_first, 1]))
    name_axes(ax, "$x$", "$F(x)$")

    height = draw_comparison(ax, FIRST, SECOND, X_RANGE, GAP)
    for level in (level_first, level_second):
        level_guide(ax, level, GAP[0])
    label_curve(ax, (middle, level_first + PLATEAU_LABEL_OFFSET), "$F_1$", FIRST_CURVE)
    label_curve(ax, (middle, level_second - PLATEAU_LABEL_OFFSET), "$F_2$", SECOND_CURVE)
    ax.text(middle, level_second + height / 2, fraction_label(height), ha="center", va="center",
            fontsize=LABEL_SIZE)

    save_figure(fig, "fig01")


if __name__ == "__main__":
    main()
