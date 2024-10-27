import pandas as pd
import sympy as sp
import numpy as np
from Methods.matrix_helpers import back_substitution

def gauss_partial_pivot(A, b):
    n = len(A)
    i = 0
    while i < n:

        swap_index = np.argmax(np.abs(A[i:, i])) + i
        if A[swap_index][i] == 0:
            return {"status":"error", "message":"The matrix is singular."}

        swap_row = A[i].copy()
        A[i] = A[swap_index]
        A[swap_index] = swap_row

        swap_b = b[i].copy()
        b[i] = b[swap_index]
        b[swap_index] = swap_b

        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0
        i += 1
    return {"status":"success", "A":A, "b":b}

# Example
A = np.array([[4, 1, 2], [2, 3, 2], [57, 0, 0]], dtype=float)
b = np.array([4, 5, 6], dtype=float)

print("real")

print(np.linalg.solve(A,b))

result = gauss_partial_pivot(A, b)

if result["status"] == "error":
    print(result["message"])
else:
    print("A")
    print(result["A"])
    print("b")
    print(result["b"])
    print("Solution ",back_substitution(result["A"], result["b"]))