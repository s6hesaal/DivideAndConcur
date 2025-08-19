import numpy as np
from SystemOfInequalities.Projections import concur


def l2_error(A, x, b):
    zeros = np.zeros(b.shape)
    if x.ndim == 2:
        concured_x = concur(x)
        return np.linalg.norm(np.minimum(np.dot(A, concured_x[:, 0]) - b, zeros), 2)
    else:
        return np.linalg.norm(np.minimum(np.dot(A, x) - b, zeros), 2)



