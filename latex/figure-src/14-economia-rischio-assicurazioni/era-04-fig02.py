"""ERA 04, slide 9: c.d.f.s of the income change of a member of a community of N = 1 and N = 2 agents."""
from modello_cdf import (FIRST_CURVE, PLATEAU_LABEL_OFFSET, PROBABILITY_AXIS_RANGE, SECOND_CURVE, Lottery,
                         draw_comparison, label_curve, level_guide, name_axes, save_figure, set_up_axes, style)

# Shock B with probability p; the loss is split equally, so a member bears B / N.
SHOCK = 1.0
PROBABILITY = 0.3
FIRST = Lottery((-SHOCK, 0.0), (PROBABILITY, 1 - PROBABILITY))
SECOND = Lottery((-SHOCK / 2, 0.0), (PROBABILITY, 1 - PROBABILITY))

X_RANGE = (-1.3, 0.4)
# The only stretch on which the two c.d.f.s differ.
GAP = (-SHOCK, -SHOCK / 2)


def main():
    """Render the figure."""
    middle = sum(GAP) / 2

    fig, ax = style.figure()
    set_up_axes(ax, X_RANGE, PROBABILITY_AXIS_RANGE,
                ([-SHOCK, -SHOCK / 2, 0], ["$-B$", "$-B/2$", "$0$"]),
                ([0, PROBABILITY, 1], ["$0$", "$p$", "$1$"]))
    name_axes(ax, "$x$", "$F(x)$")

    draw_comparison(ax, FIRST, SECOND, X_RANGE, GAP)
    level_guide(ax, PROBABILITY, GAP[0])
    label_curve(ax, (middle, PROBABILITY + PLATEAU_LABEL_OFFSET), "$F_1$", FIRST_CURVE)
    label_curve(ax, (middle, PLATEAU_LABEL_OFFSET), "$F_2$", SECOND_CURVE)

    save_figure(fig, "fig02")


if __name__ == "__main__":
    main()
