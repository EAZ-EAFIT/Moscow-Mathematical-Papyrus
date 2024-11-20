import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import definite_matrix_interface, gauss_matrix_result, graph_Ab
from Methods.Gauss_total_pivot import gauss_total_pivot
from Methods.matrix_helpers import back_substitution

def show_gauss_jordan_total_pivot():
    st.header("Gauss-Jordan Elimination with Total Pivoting")

    matrix_A, vector_b = definite_matrix_interface()

    graph_Ab(matrix_A, vector_b)

    result = gauss_total_pivot(matrix_A, vector_b)

    if result["status"] == "error":
        st.error(result["message"])
        return
    else:
        row_echelon = result["A"]
        vector_b = result["b"]

        vector_x = result["x"]
    
    gauss_matrix_result(row_echelon, vector_b, vector_x)
