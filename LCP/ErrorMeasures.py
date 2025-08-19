import numpy as np
from LCP.Point import Point
from LCP.Instance import Instance
from LCP.Projections import errorConcur


def calculateError(point: Point, instance: Instance):
    errorPoint = errorConcur(point)
    return np.linalg.norm(np.dot(instance.M, errorPoint.equalCopyX[:, 0]) + instance.q - errorPoint.equalCopyS)
