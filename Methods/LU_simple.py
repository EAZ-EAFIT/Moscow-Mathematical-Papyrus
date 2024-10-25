import pandas as pd
import sympy as sp
import numpy as np

from matrix_helpers import back_substitution, forward_substitution

def LU_simple(A):
    n = len(A)
    i = 0

    L = np.eye(n)

    while i < n:
        current_value = A[i][i]
        if current_value == 0:
            return {"status":"error", "message":"The matrix cannot be decomposed without permuting rows."}
        
        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            A[j][i] = 0
            L[j][i] = factor
        i += 1

    return {"status":"success", "U":A, "L":L}

def solve_LU_simple(L,U,b):
    y = forward_substitution(L,b)
    x = back_substitution(U,y)
    return x

# Example
A = np.array([[3, 1, 0], [0, 3, 2], [1, 0, 0]], dtype=float)
b = np.array([4, 5, 6], dtype=float)

L, U, P = sp.Matrix(A).LUdecomposition()
L = np.array(L).astype(np.float64)
U = np.array(U).astype(np.float64)
print(U)
print(L)
print(P)
