import pandas as pd
import sympy as sp
import numpy as np
from Methods.matrix_helpers import back_substitution

def gauss_total_pivot(A, b):
    n = len(A)
    i = 0
    original_x = np.zeros(n)
    while i < n:

        row_index = np.argmax(np.abs(A[i:, i])) + i
        col_index = np.argmax(np.abs(A[i]))
        if A[row_index][i] == 0 or A[i][col_index] == 0:
            return {"status":"error", "message":"The matrix is singular."}

        swap_row = A[row_index].copy()
        A[i] = A[row_index]
        A[row_index] = swap_row

        swap_b = b[i].copy()
        b[i] = b[row_index]
        b[row_index] = swap_b

        current_value = A[i][i]
        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0
        i += 1
        print("A", A)

    return {"status":"success", "A":A, "b":b}

# Example
A = np.array([[4, 1, 2], [2, 3, 2], [57, 0, 0]], dtype=float)
b = np.array([4, 5, 6], dtype=float)

print("real")

print(np.linalg.solve(A,b))

result = gauss_total_pivot(A, b)

if result["status"] == "error":
    print(result["message"])
else:
    print("A")
    print(result["A"])
    print("b")
    print(result["b"])
    print("Solution ",back_substitution(result["A"], result["b"]))