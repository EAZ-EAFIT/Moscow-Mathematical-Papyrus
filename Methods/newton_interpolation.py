import numpy as np
import sympy as sp

def newton_interpolation(x, y, decimals, x_sym=sp.symbols("x")):
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
    coefficients = np.diagonal(matrix)  # Original coefficients
    rounded_coefficients = np.round(coefficients, decimals)  # Rounded coefficients

    # Create the Newton polynomial using original coefficients for the unrounded polynomial
    newton_poly_unrounded = 0
    newton_poly_rounded = 0

    for i in range(n):
        term_unrounded = coefficients[i]
        term_rounded = rounded_coefficients[i]
        for j in range(i):
            term_unrounded *= (x_sym - x[j])
            term_rounded *= (x_sym - x[j])
        newton_poly_unrounded += term_unrounded
        newton_poly_rounded += term_rounded

    # SymPy expressions of the Newton polynomials
    newton_poly_expr_unrounded = sp.expand(newton_poly_unrounded)
    newton_poly_expr_rounded = sp.expand(newton_poly_rounded)

    return matrix, coefficients, rounded_coefficients,newton_poly_unrounded,  newton_poly_expr_unrounded, newton_poly_rounded, newton_poly_expr_rounded
