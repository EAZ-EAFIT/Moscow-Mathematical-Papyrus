import pandas as pd
import sympy as sp
import numpy as np

from matrix_helpers import back_substitution, forward_substitution

def LU_partial(A):
    n = len(A)
    i = 0

    L = np.eye(n)
    P = np.eye(n)

    while i < n:
        swap_index = np.argmax(np.abs(A[i:, i])) + i

        if A[swap_index][i] == 0:
            return {"status":"error", "message":"The matrix cannot be decomposed as it is singular."}

        if swap_index != i:
            swap_row = A[i].copy()
            A[i] = A[swap_index]
            A[swap_index] = swap_row

            P[i][i] = 0
            P[swap_index][swap_index] = 0
            P[swap_index][i] = 1
            P[i][swap_index] = 1


        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            A[j][i] = 0
            L[j][i] = factor
        i += 1

    return {"status":"success", "U":A, "L":L, "P":P}


# ?? REVISAR
def solve_LU_partial(P,L,U,b):
    b = np.inv(P) @ b
    y = forward_substitution(L,b)
    x = back_substitution(U,y)
    return x