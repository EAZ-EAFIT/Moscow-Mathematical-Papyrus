import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import enter_function, calculate_tolerance, graph
from Methods.regula_falsi import regula_falsi

def show_regula_falsi():
    st.header("False Position Method")

    x, function_input = enter_function(placeholder_function="x**2 - 4", placeholder_variable="x")

    col3, col4 = st.columns(2)
    with col3:
        a = st.number_input(
        "Initial point of search interval (a)",
        format="%.4f",
        value = 0.1,
        step = 0.0001,
        help="The infimum of the desired search interval [a, b]."
        )
    with col4:
        b = st.number_input(
        "End point of search interval (b)",
        format="%.4f",
        value = 3.0,
        step = 0.0001,
        help="The supremum of the desired search interval [a, b]."
        )

    tol, niter, tolerance_type = calculate_tolerance()
    st.markdown(f"**Calculated Tolerance:** {tol:.10f}")

    x = sp.symbols(f'{x}')
    function = sp.sympify(function_input)

    st.subheader("Function")
    st.latex(f"f({x}) = {sp.latex(function)}")

    function = sp.lambdify(x, sp.sympify(function_input), 'numpy')

    # DO CHECKS ON INPUT INTEGRITY
    # check if derivative is continuous in general

    result = regula_falsi(a, b, niter, tol, tolerance_type, function)

    if result["status"] == "error":
        st.error(result["message"])
        return
    else:
        result = result["table"]

    # Add a slider to choose the number of decimals to display
    decimals = st.slider(
        "Select number of decimals to display on table",
        min_value=1,
        max_value=10,
        value=4,
        help="Adjust the number of decimal places for the result table."
    )
    # Format the dataframe to display the selected number of decimals
    result_display = result.style.format(f"{{:.{decimals}f}}")  # Use f-string to format dynamically

    st.subheader("Results")
    st.dataframe(result_display, use_container_width=True)

    graph(x, function_input)