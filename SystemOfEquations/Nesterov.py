import math
import numpy as np
from SystemOfEquations.ErrorMeasure import l2_error


def gradient(A, x, b):
    return_value = np.zeros(len(x))
    m = len(A)
    for index in range(m):
        return_value -= (b[index] - np.dot(A[index], x)) * A[index].transpose()
    return return_value


def nesterov(A, x, b, r):
    m = len(A)
    errors = []
    L = m
    alpha = 1
    beta = 0
    y = x.copy()

    for k in range(r):
        prev_x = x.copy()
        x = y - gradient(A, y, b)/L
        if k > 0:
            old_alpha = alpha
            alpha = alpha*(math.sqrt(alpha**2 + 4) - alpha)/2
            beta = old_alpha*(1-old_alpha)/(old_alpha**2+alpha)
        y = x + beta*(x-prev_x)
        errors.append(l2_error(A, x, b))

    return errors
