import pandas as pd
import sympy as sp
import numpy as np

from Methods.matrix_helpers import back_substitution, forward_substitution

def LU_simple(A):
    n = len(A)
    i = 0

    factors = []
    
    while i < n:
        current_value = A[i][i]
        if current_value == 0:
            return {"status":"error", "message":"The matrix cannot be decomposed without permuting rows."}
        
        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            A[j][i] = 0
            factors.append(factor)
        i += 1

    for factor in factors:
        print(factor)

    return {"status":"success", "U":A, "factor":factors}

def back_substitution(A,b):
    n = len(A)
    x = np.zeros(n)

    for i in range(n-1, -1, -1):

        print("hallo", i, x[i], b[i])

        x[i] = b[i]
        print(i, x[i], b[i])
        for j in range(i+1, n):
            if j != i:
                x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x

def forward_substitution(A,b):
    n = len(A)
    x = np.zeros(n)

    for i in range(0,n):
        x[i] = b[i]
        for j in range(i+1, n):
            if j != i:
                x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x

# Example
A = np.array([[0, 1, 0], [0, 3, 2], [1, 0, 0]], dtype=float)
b = np.array([4, 5, 6], dtype=float)

print("real",np.linalg.solve(A,b))
result = LU_simple(A, b)
if result["status"] == "error":
    print(result["message"])
else:
    print(result["A"], result["b"])
    print("prent",back_substitution(result["A"], result["b"]))