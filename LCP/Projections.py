import numpy as np
from LCP.Point import Point
from LCP.Instance import Instance


def errorConcur(point: Point):

    concuredPoint = concur(point)
    s = concuredPoint.compCopyS
    x = concuredPoint.compCopyX

    zeros = np.zeros(point.n)
    s = np.maximum(s, zeros)
    x = np.maximum(x, zeros)

    for index in range(point.n):
        if x[index] <= s[index]:
            x[index] = 0
        else:
            s[index] = 0

    return Point(s, x)


def concur(point: Point):


    s = (point.equalCopyS + point.compCopyS)/2
    x = np.zeros(point.n)

    for index in range(point.n):
        x[index] = (point.equalCopyX[index].sum()+point.compCopyX[index])/(point.n+1)

    return Point(s, x)


def divide(point: Point, instance: Instance):

    zeros = np.zeros(point.n)
    compS = np.maximum(point.compCopyS, zeros)
    compX = np.maximum(point.compCopyX, zeros)

    for index in range(point.n):
        if compX[index] <= compS[index]:
            compX[index] = 0
        else:
            compS[index] = 0

    equalX = np.zeros(point.equalCopyX.shape)
    equalS = np.zeros(point.equalCopyS.shape)

    for index in range(point.n):
        gap = np.dot(instance.M[index], point.equalCopyX[:, index])+instance.q[index] - point.equalCopyS[index]
        equalX[:, index] = point.equalCopyX[:, index] - (gap/2)*instance.M[index].transpose()
        equalS[index] = point.equalCopyS[index] + gap/2

    return Point(compS, compX, equalS, equalX)


