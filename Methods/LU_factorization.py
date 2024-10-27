import pandas as pd
import sympy as sp
import numpy as np

from .matrix_helpers import back_substitution, forward_substitution

def LU_factorization(A):
    A = A.copy().astype(float)
    n = len(A)
    i = 0

    L = np.eye(n)

    while i < n:
        current_value = A[i][i]
        if current_value == 0:
            return {"status":"error", "message":"The matrix cannot be decomposed without permuting rows or is singular."}

        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            A[j][i] = 0
            L[j][i] = factor
        i += 1
    return {"status":"success", "U":A, "L":L}

def solve_LU(L,U,b):
    y = forward_substitution(L,b)
    x = back_substitution(U,y)
    return x

# A = np.array([[2.0, 4.0, 2.0], [4.0, -10.0, 2.0], [1.0, 2.0, 4.0]])
# b = np.array([5.0, -8.0, 13.0])

# print("real")
# print(np.linalg.solve(A, b))

# result = LU_factorization(A)
# print("U:")
# print(result["U"])
# print("L:")
# print(result["L"])
# print(result["L"]@result["U"])
# print("x:")
# print(solve_LU(result["L"], result["U"], b))
