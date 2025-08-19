import numpy as np
from sklearn.preprocessing import normalize
from MatrixScaling.ErrorMeasure import calculateError


def sinkhorn(A, r):
    errors = [calculateError(A)]

    for i in range(r):
        A = normalize(A, axis=1, norm="l1", copy=False)
        A = normalize(A, axis=0, norm="l1", copy=False)
        errors.append(calculateError(A))

    return errors


def DC_AP(A, r):
    errors = [calculateError(A)]

    for i in range(r):
        rowScaled = normalize(A, axis=1, norm="l1")
        columnScaled = normalize(A, axis=0, norm="l1")
        A = np.sqrt(rowScaled * columnScaled)
        errors.append(calculateError(A))

    return errors

