import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import enter_function, calculate_tolerance
from Methods.Newton import get_derivative, newton

def show_newton():
    st.title("Newton-Raphson Method")

    x, function_input = enter_function()

    col3, col4 = st.columns(2)
    with col3:
        x0 = st.number_input(
        "Initial Point (x_0)",
        format="%.4f",
        value = 0.1,
        step = 0.0001,
        help="The first initial guess for the root. It is a value where the function is evaluated."
        )
    with col4:
        print("")

    tol, niter, tolerance_type = calculate_tolerance()
    st.markdown(f"**Calculated Tolerance:** {tol:.10f}")

    x = sp.symbols(f'{x}')
    function = sp.sympify(function_input)
    derivative = get_derivative(function)

    st.subheader("Function")
    st.latex(f"f({x}) = {sp.latex(function)}")
    st.subheader("Derivative")
    st.latex(f"f({x}) = {sp.latex(sp.sympify(derivative))}")

    function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
    derivative = sp.lambdify(x, derivative, 'numpy')
    #check if derivative is continuous at the initial point
    if derivative(x0) == 0:
        st.error("Derivative is not continuous at the initial point. Please choose another point.")
        return
    # check if derivative is continuous in general

    result = newton(x0, niter, tol, tolerance_type, function,  derivative)
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