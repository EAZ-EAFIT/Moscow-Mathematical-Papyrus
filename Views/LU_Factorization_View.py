import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import definite_matrix_interface, LU_result, graph_Ab
from Methods.LU_factorization import LU_factorization, solve_LU

def show_LU_factorization():
    st.header("LU Factorization without pivoting")

    matrix_A, vector_b = definite_matrix_interface()
    graph_Ab(matrix_A, vector_b)

    result = LU_factorization(matrix_A)

    if result["status"] == "error":
        st.error(result["message"])
        return
    else:
        L = result["L"]
        U = result["U"]

        vector_x = solve_LU(L, U, vector_b)
    

    LU_result(L=L, U=U, vector_x=vector_x)