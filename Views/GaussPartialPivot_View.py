import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import definite_matrix_interface, calculate_tolerance, iterative_matrix_interface
from Methods.Gauss_partial_pivot import gauss_partial_pivot
from Methods.matrix_helpers import back_substitution


def show_gauss_jordan_partial_pivot():
    st.header("Gauss-Jordan Elimination with partial Pivoting")

    matrix_A, vector_b = definite_matrix_interface()

    result = gauss_partial_pivot(matrix_A, vector_b)

    if result["status"] == "error":
        st.error(result["message"])
        return
    else:
        eliminated_matrix = result["A"]
        vector_b = result["b"]

        vector_x = back_substitution(eliminated_matrix, vector_b)

    decimals = st.slider(
            "Select number of decimals to display",
            min_value=1, 
            max_value=10, 
            value=4,
            help="Adjust the number of decimal places in the result."
        )
    
    col1, col2, col3 = st.columns(3)

    with col1:
        eliminated_matrix = sp.Matrix(eliminated_matrix)
        st.subheader("Eliminated Matrix")
        st.latex(sp.latex(eliminated_matrix))
    with col2:
        vector_b = sp.Matrix(vector_b)
        st.subheader("Vector b")
        st.latex(sp.latex(vector_b))
    with col3:
        vector_x = sp.Matrix(vector_x)
        st.subheader("Result")
        st.latex(sp.latex(vector_x))