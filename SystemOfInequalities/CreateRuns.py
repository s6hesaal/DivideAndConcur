import numpy as np
from SystemOfInequalities.AlternatingProjections import simulate as simulate_ap
from SystemOfInequalities.DouglasRachford import simulate as simulate_dr
from SystemOfInequalities.Nesterov import nesterov
from ReadMatrix import readMatFile
from FindFiles import findFilesWithEnding
from SystemOfInequalities.InstanceFromLP import instanceFromMPSFile
import os

def generateEqualsAsInequalityRuns(inputFolder, outputFolder, numIterations):
    os.makedirs(outputFolder, exist_ok=True)
    filenames = findFilesWithEnding(inputFolder, ".mat")

    for file in filenames:

        A = readMatFile("%s/%s.mat" % (inputFolder, file))
        A = np.vstack((A, -A))

        m = len(A)
        n = len(A[0])
        x_sol = np.ones(n)
        x_sol[0] = 10

        b = np.dot(A, x_sol)
        name = file

        m = len(A)
        n = len(A[0])

        print("%s: %dx%d" % (name, m, n))

        starting_x = np.zeros((n, m))
        error_dr = simulate_dr(A, starting_x.copy(), b, numIterations)
        error_nesterov = nesterov(A, starting_x.copy()[:, 0], b, numIterations)
        error_ap = simulate_ap(A, starting_x.copy(), b, numIterations)

        meta = {"m": m, "n": n, "name": name}

        np.savez("{2}/{0}_{1}".format(name, numIterations, outputFolder),
                 ap=error_ap,
                 dr=error_dr,
                 nesterov=error_nesterov,
                 meta=meta)


def generateLPRuns(inputFolder, outputFolder, numIterations):
    os.makedirs(outputFolder, exist_ok=True)
    filenames = findFilesWithEnding(inputFolder, ".mps")

    for file in filenames:

        A, b, name = instanceFromMPSFile("%s/%s.mps" % (inputFolder, file))
        m = len(A)
        n = len(A[0])

        print("%s: %dx%d" % (name, m, n))

        starting_x = np.zeros((n, m))
        error_dr = simulate_dr(A, starting_x.copy(), b, numIterations)
        error_nesterov = nesterov(A, starting_x.copy()[:, 0], b, numIterations)
        error_ap = simulate_ap(A, starting_x.copy(), b, numIterations)

        meta = {"m": m, "n": n, "name": name}

        np.savez("{2}/{0}_{1}".format(name, numIterations, outputFolder),
                 ap=error_ap,
                 dr=error_dr,
                 nesterov=error_nesterov,
                 meta=meta)
