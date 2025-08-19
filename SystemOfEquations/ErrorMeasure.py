import numpy as np
from SystemOfEquations.Projections import concur


def l2_error(A, x, b):
    if x.ndim == 2:
        concured_x = concur(x)
        return np.linalg.norm(np.dot(A, concured_x[:, 0]) - b, 2)
    else:
        return np.linalg.norm(np.dot(A, x) - b, 2)



