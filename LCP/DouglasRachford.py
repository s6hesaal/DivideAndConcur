from LCP.Point import Point
from LCP.Instance import Instance
from LCP.Projections import divide, concur
from LCP.ErrorMeasures import calculateError


def step(point: Point, instance):
    divided = divide(point, instance)
    overshoot = divided + (divided - point)
    return concur(overshoot) - divided + point


def simulate(start: Point, instance: Instance, numSteps):
    errors = [calculateError(start, instance)]

    for index in range(numSteps):
        start = step(start, instance)
        errors.append(calculateError(start, instance))

    return errors
