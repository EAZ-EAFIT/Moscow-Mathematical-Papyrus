import pandas as pd
import sympy as sp
import numpy as np

def gauss_no_pivot(A, b):
    n = len(A)
    i = 0
    
    while i < n:
        current_value = A[i][i]
        test_value = current_value
        j = i + 1
        swaps = False
        while j < n and test_value == 0:
            swaps = True
            test_value = A[j][i]
            j += 1
        if test_value == 0:
            return {"status":"error", "message":"The matrix is singular."}
        elif swaps:
            j -= 1
            swap_row = A[i].copy()
            A[i] = A[j]
            A[j] = swap_row

            swap_b = b[i].copy()
            b[i] = b[j]
            b[j] = swap_b
        print("A", A)

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
A = np.array([[0, 1, 0], [0, 3, 2], [1, 0, 0]], dtype=float)
b = np.array([4, 5, 6], dtype=float)
result = gauss_no_pivot(A, b)
if result["status"] == "error":
    print(result["message"])
else:
    print(result["A"], result["b"])