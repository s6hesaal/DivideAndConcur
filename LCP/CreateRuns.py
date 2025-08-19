import numpy as np
from LCP.AlternatingProjections import simulate as simulateAP
from LCP.DouglasRachford import simulate as simulateDR
from LCP.Instance import Instance
from LCP.Point import Point
from ReadMatrix import readMatFile
from FindFiles import findFilesWithEnding
import os

def generateLCPRuns(inputFolder, outputFolder, numIterations):
    os.makedirs(outputFolder, exist_ok=True)
    filenames = findFilesWithEnding(inputFolder, ".mat")
    for file in filenames:
        print("Start with %s." % file)

        M = readMatFile("%s/%s.mat" % (inputFolder, file))
        m = len(M)
        n = len(M[0])

        if m != n:
            continue

        x_sol = np.ones(n)
        x_sol[0] = 10
        s_sol = np.zeros(n)

        for i in range(1, n):
            if i % 2 == 1:
                continue
            x_sol[i] = 0
            s_sol[i] = 5

        q = s_sol - np.dot(M, x_sol)
        instance = Instance(M, q)
        n = instance.n

        error_ap = simulateAP(Point(np.zeros(n), np.zeros(n)), instance, numIterations)
        error_dr = simulateDR(Point(np.zeros(n), np.zeros(n)), instance, numIterations)

        meta = {"m": m, "n": n, "name": file}

        np.savez("{2}/{0}_{1}".format(file, numIterations, outputFolder),
                 dr=error_dr,
                 ap=error_ap,
                 meta=meta)



