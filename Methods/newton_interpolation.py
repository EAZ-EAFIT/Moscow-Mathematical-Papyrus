import numpy as np
import sympy as sp

def newton_interpolation(x, y, x_sym):
    n = len(x)
    matrix = np.zeros((n, n))  # Create a square matrix of size len(x)

    # Fill the first column with y values
    for i in range(n):
        matrix[i, 0] = y[i]
    
    # Compute the divided differences
    for col in range(1, n):
        for row in range(col, n):
            matrix[row, col] = (matrix[row, col-1] - matrix[row-1, col-1]) / (x[row] - x[row-col])

    # Newton coefficients (diagonal of the matrix)
    coefficients = np.diagonal(matrix)

    # Create the Newton polynomial
    newton_poly = 0

    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x_sym - x[j])
        newton_poly += term

    # SymPy expression of the Newton polynomial
    newton_poly_expr = sp.expand(newton_poly)

    return matrix, coefficients, newton_poly, newton_poly_expr
