import numpy as np
import numbers


class Point:

    def __init__(self, s, x, sEqual=None, xEqual=None):

        self.n = len(x)
        self.compCopyX = x.copy()
        self.compCopyS = s.copy()
        if sEqual is None:
            self.equalCopyS = s.copy()
        else:
            self.equalCopyS = sEqual.copy()

        if xEqual is None:
            self.equalCopyX = np.tile(x.reshape(-1,1), (1, self.n))
        else:
            self.equalCopyX = xEqual.copy()

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.compCopyS + other.compCopyS, self.compCopyX + other.compCopyX,
                         self.equalCopyS + other.equalCopyS, self.equalCopyX + other.equalCopyX)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.compCopyS - other.compCopyS, self.compCopyX - other.compCopyX,
                         self.equalCopyS - other.equalCopyS, self.equalCopyX - other.equalCopyX)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Point(self.compCopyS * other, self.compCopyX * other,
                         self.equalCopyS * other, self.equalCopyX * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)




