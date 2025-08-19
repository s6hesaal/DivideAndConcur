from pulp import LpProblem, lpSum, LpConstraintGE, LpConstraintLE, LpConstraintEQ
import numpy as np


# Optimal values based on NETLIB LP Collection
def nameToBounds(name):
    if name == "ADLITTLE":
        # Optimal value 2.2549496316E+05
        return 2.2549496316E+05, 2.2549496316E+05

    if name == "KB2":
        # Optimal value -1.7499001299E+03
        return  -1.7499001299E+03, -1.7499001299E+03

    if name == "AFIRO":
        # Optimal value -4.6475314286E+02
        return -4.6475314286E+02, -4.6475314286E+02

    if name == "BLEND":
        # Optimal value -3.0812149846E+01
        return -3.0812149846E+01, -3.0812149846E+01

    if name == "BOEING2":
        # Optimal value -3.1501872802E+02
        return -3.1501872802E+02, -3.1501872802E+02

    if name == "ISRAEL":
        # Optimal value -8.9664482186E+05
        return -8.9664482186E+05, -8.9664482186E+05

    if name == "RECIPE":
        # Optimal value -2.6661600000E+02
        return -2.6661600000E+02, -2.6661600000E+02

    if name == "SC105":
        # Optimal value -5.2202061212E+01
        return -5.2202061212E+01, -5.2202061212E+01

    if name == "SC50A":
        # Optimal value -6.4575077059E+01
        return -6.4575077059E+01, -6.4575077059E+01

    if name == "SC50B":
        # Optimal value -7.0000000000E+01
        return -7.0000000000E+01, -7.0000000000E+01

    if name == "SHARE2B":
        # Optimal value -4.1573224074E+02
        return -4.1573224074E+02, -4.1573224074E+02

    if name == "BEACONFD":
        # Opt 3.3592485807E+04
        return 3.3592485807E+04, 3.3592485807E+04


def instanceFromMPSFile(filename):

    status, problem = LpProblem.fromMPS(filename)

    cost_variables = problem.variables()
    objective_row = problem.objective

    # Build new Constraint
    cost_coefficients = []
    for var in cost_variables:
        cost_coefficients.append(objective_row.get(var, 0))
    lower, upper = nameToBounds(problem.name)
    problem += (lpSum(
        cost_coefficients[i] * cost_variables[i] for i in range(len(cost_variables))) >= lower), "CostConstraintLower"

    problem += (lpSum(
        cost_coefficients[i] * cost_variables[i] for i in range(len(cost_variables))) <= upper), "CostConstraintUpper"

    # Formulate as Ax\leq b
    A = []
    b = []
    for constraint in problem.constraints.values():

        row = []
        for var in problem.variables():
            row.append(constraint.get(var, 0))

        if constraint.sense == LpConstraintLE:
            A.append(row)
            b.append(constraint.constant)

        elif constraint.sense == LpConstraintGE:
            A.append([-coef for coef in row])
            b.append(-constraint.constant)

        elif constraint.sense == LpConstraintEQ:
            A.append(row)
            b.append(constraint.constant)
            A.append([-coef for coef in row])
            b.append(-constraint.constant)


    # Normalise rows
    A = np.array(A)
    b = np.array(b)
    for i in range(A.shape[0]):
        norm = np.linalg.norm(A[i, :])
        if norm > 0:
            A[i, :] = A[i, :] / norm
            b[i] = b[i] / norm

    return A, b, problem.name

