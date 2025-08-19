from SystemOfInequalities.ErrorMeasure import l2_error
from SystemOfInequalities.Projections import divide, concur

def step(A, x, b):
    x = divide(A, x, b)
    x = concur(x)
    return x

def simulate(A, x, b, r):
    errors = []
    for index in range(r):
        x = step(A, x, b)
        errors.append(l2_error(A, x, b))

    return errors
