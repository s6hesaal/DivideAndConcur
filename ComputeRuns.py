from MatrixScaling.CreateRuns import generateMatrixScalingRuns
from LCP.CreateRuns import generateLCPRuns
from SystemOfInequalities.CreateRuns import generateEqualsAsInequalityRuns, generateLPRuns
from SystemOfEquations.CreateRuns import generateEqualsRuns

#print("===MATRIX SCALING ===")
#generateMatrixScalingRuns("Inputs/squareMatrices", "Outputs/MatrixScaling", 10000)

#print("===LINEAR COMPLEMENTARY PROBLEM ===")
#generateLCPRuns("Inputs/squareMatrices", "Outputs/LCP", 100000)

#print("===EQUALS ===")
#generateEqualsRuns("Inputs/sparseMatrices", "Outputs/Equals", 10000)

print("===EQUALS AS INEQUALITY ===")
generateEqualsAsInequalityRuns("Inputs/sparseMatrices", "Outputs/EqualsAsInequality", 10000)

print("===LINEAR PROGRAMMING ===")
generateLPRuns("Inputs/LP", "Outputs/LP", 10000)

