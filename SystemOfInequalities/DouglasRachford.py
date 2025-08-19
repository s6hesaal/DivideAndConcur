from SystemOfInequalities.ErrorMeasure import l2_error
from SystemOfInequalities.Projections import divide, concur


def step(A, x, b):
    divided_x = divide(A, x, b)
    overshoot = divided_x + (divided_x - x)
    return concur(overshoot) - divided_x + x


def simulate(A, x, b, r):
    errors = []
    for index in range(r):
        x = step(A, x, b)
        errors.append(l2_error(A, x, b))

    return errors


