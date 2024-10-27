import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import definite_matrix_interface, calculate_tolerance, iterative_matrix_interface, gauss_matrix_result
from Methods.Gauss_no_pivot import gauss_no_pivot
from Methods.matrix_helpers import back_substitution

def show_gauss_jordan_no_pivot():
    st.header("Gauss-Jordan Elimination without Pivoting")

    matrix_A, vector_b = definite_matrix_interface()

    result = gauss_no_pivot(matrix_A, vector_b)

    if result["status"] == "error":
        st.error(result["message"])
        return
    else:
        row_echelon = result["A"]
        vector_b = result["b"]

        vector_x = back_substitution(row_echelon, vector_b)
    
    gauss_matrix_result(row_echelon, vector_b, vector_x)

