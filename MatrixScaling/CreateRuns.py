import numpy as np
from ReadMatrix import readMatFile
from MatrixScaling.Algorithms import sinkhorn, DC_AP
from FindFiles import findFilesWithEnding
import os

def generateMatrixScalingRuns(inputFolder, outputFolder, numIterations):
    os.makedirs(outputFolder, exist_ok=True)
    filenames = findFilesWithEnding(inputFolder, ".mat")
    for file in filenames:
        print("Start with %s." % file)

        A = readMatFile("%s/%s.mat" % (inputFolder, file), normaliseRows=False)
        A = np.array(A)
        m = len(A)
        n = len(A[0])
        if m != n:
            continue
        A = abs(A)
        A = A + np.eye(n)

        errors_sinkhorn = sinkhorn(A.copy(), numIterations)
        errors_DC_ap = DC_AP(A.copy(), numIterations)

        meta = {"m": m, "n": n, "name": file}

        np.savez("{2}/{0}_{1}".format(file, numIterations, outputFolder),
                 sinkhorn=errors_sinkhorn,
                 dc_ap=errors_DC_ap,
                 meta=meta)



