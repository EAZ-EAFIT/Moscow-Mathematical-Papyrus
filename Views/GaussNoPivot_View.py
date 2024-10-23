import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import definite_matrix_interface, calculate_tolerance, iterative_matrix_interface
from Methods.Gauss_no_pivot import gauss_no_pivot

def show_gauss_jordan_no_pivot():
    st.title("Gauss-Jordan Elimination without Pivoting")

    matrix_A, vector_b = definite_matrix_interface()

    result = gauss_no_pivot(matrix_A, vector_b)

    if result["status"] == "error":
        st.error(result["message"])
        return
    else:
        vector_x = result["vector"]
    
    st.subheader("Results")
    st.write("The solution vector is:")
    st.write(vector_x)
