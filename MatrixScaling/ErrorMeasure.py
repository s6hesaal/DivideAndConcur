import math


def calculateError(A):
    rowError = 0
    for rowIndex in range(len(A)):
        rowError += (A[rowIndex].sum()-1) ** 2

    columnError = 0
    for columnIndex in range(len(A[0])):
        columnError += (A[:, columnIndex].sum() - 1) **2

    return math.sqrt(rowError) + math.sqrt(columnError)