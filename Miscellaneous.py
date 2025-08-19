import numpy as np
import pandas as pd
from FindFiles import findFilesWithEnding

# Ax=b vs Ax\leq b
print("Ax\\leq b outerperforms Ax=b")
filenames = findFilesWithEnding("Outputs/Equals", ".npz")
iterationMarks = [1000, 5000, 10000]
counters = [0, 0, 0]
for file in filenames:
    dataEquals = np.load("Outputs/Equals/%s.npz" % file, allow_pickle=True)
    errorsEquals = dataEquals["dr"]
    dataInequality = np.load("Outputs/EqualsAsInequality/%s.npz" % file, allow_pickle=True)
    errorsInequality = dataInequality["dr"]

    for index, num in enumerate(iterationMarks):
        if min(errorsInequality[:num]) <= min(errorsEquals[:num]):
            counters[index] += 1
print(counters)
print("===")

# Ax\leq b Douglas-Rachford outperforms alternating projections
print("Ax\\leq b: DR vs AP")
print("Equals as inequality")
filenames = findFilesWithEnding("Outputs/EqualsAsInequality", ".npz")
iterationMarks = [1000, 5000, 10000]
counters = [0, 0, 0]
for file in filenames:
    data = np.load("Outputs/EqualsAsInequality/%s.npz" % file, allow_pickle=True)
    errorsDR = data["dr"]
    errorsAP = data["ap"]

    for index, num in enumerate(iterationMarks):
        if min(errorsDR[:num]) <= min(errorsAP[:num]):
            counters[index] += 1
print(counters)

print("Linear Programming")
filenames = findFilesWithEnding("Outputs/LP", ".npz")
iterationMarks = [1000, 5000, 10000]
counters = [0, 0, 0]
for file in filenames:
    data = np.load("Outputs/LP/%s.npz" % file, allow_pickle=True)
    errorsDR = data["dr"]
    errorsAP = data["ap"]

    for index, num in enumerate(iterationMarks):
        if min(errorsDR[:num]) <= min(errorsAP[:num]):
            counters[index] += 1
print(counters)
print("===")

# LP - Nesterov vs Douglas-Rachford
print("LP Nesterov outperforms Douglas-Rachford")
filenames = findFilesWithEnding("Outputs/LP", ".npz")
iterationMarks = [5000, 10000]
counter = 0
for file in filenames:
    data = np.load("Outputs/LP/%s.npz" % file, allow_pickle=True)
    errorsNesterov = data["nesterov"]
    errorsDM = data["dr"]

    betterAtAllMarks = True
    for index, num in enumerate(iterationMarks):
        betterAtAllMarks = betterAtAllMarks and min(errorsNesterov[:num]) <= min(errorsDM[:num])
    if betterAtAllMarks:
        counter += 1

print(counter)
print("===")

# LCP - Table
print("LCP - Table")
filenames = findFilesWithEnding("Outputs/LCP", ".npz")
table = []
for file in filenames:
    data = np.load("Outputs/LCP/%s.npz" % file, allow_pickle=True)
    meta = data['meta'].item()
    errorsDM = data["dr"]
    errorsAP = data["ap"]

    table.append([
        meta['name'],
        min((errorsDM[:1000])),
        min((errorsDM[:10000])),
        min((errorsDM[:20000])),
        min(errorsDM),
        min(errorsAP)
    ])
df = pd.DataFrame(table)
latex_str = df.to_latex(index=False, float_format=lambda x: f"{x:.3e}")
print(latex_str)
print("===")

# Sinkhorn-Knopp vs Divide&Concur
print("Sinkorn-Knopp outperforms Divide&Concur ")
filenames = findFilesWithEnding("Outputs/MatrixScaling", ".npz")
iterationMarks = [100, 1000, 10000]
counters = [0, 0, 0]
for file in filenames:
    data = np.load("Outputs/MatrixScaling/%s.npz" % file, allow_pickle=True)
    errorsSinkhorn = data["sinkhorn"]
    errorsDC = data["dc_ap"]

    for index, num in enumerate(iterationMarks):
        if min(errorsSinkhorn[:num]) <= min(errorsDC[:num]):
            counters[index] += 1
print(counters)
print("===")
