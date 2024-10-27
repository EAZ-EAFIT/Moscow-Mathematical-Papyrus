import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import definite_matrix_interface, LU_result
from Methods.PLU_factorization import PLU_factorization, solve_PLU

def show_PLU_factorization():
    st.header("LU Factorization with pivoting")

    matrix_A, vector_b = definite_matrix_interface()

    result = PLU_factorization(matrix_A)

    if result["status"] == "error":
        st.error(result["message"])
        return
    else:
        L = result["L"]
        U = result["U"]
        P = result["P"]

        vector_x = solve_PLU(P, L, U, vector_b)
    
    LU_result(P=P, L=L, U=U, vector_x=vector_x)