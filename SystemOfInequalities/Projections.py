import numpy as np


def divide(A, x, b):
    return_x = np.zeros(x.shape)
    m = len(b)
    for index in range(m):
        return_x[:, index] = x[:, index] + max((b[index]-np.dot(A[index], x[:, index])), 0)*A[index].transpose()
    return return_x


def concur(x):
    n = len(x)
    m = len(x[0])
    return_x = np.zeros(x.shape)
    for index in range(n):
        return_x[index] = x[index].sum()/m

    return return_x
