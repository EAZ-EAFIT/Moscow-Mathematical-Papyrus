import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import enter_function, calculate_tolerance
from Methods.Secant import secant

def show_secant():
    st.title("Secant Method")

    x, function_input = enter_function()

    col3, col4 = st.columns(2)
    with col3:
        x0 = st.number_input(
        "First Point (x_0)",
        format="%.4f",
        value = 0.1,
        step = 0.0001,
        help="The first initial guess for the root. It is a value where the function is evaluated."
        )
    with col4:
        x1 = st.number_input(
        "Second Point (x_1)",
        format="%.4f",
        value = 0.2,
        step = 0.0001,
        help="The second initial guess for the root. It should be close to x0 and the function should have different signs at x0 and x1."
        )

    tol, niter, tolerance_type = calculate_tolerance()
    st.markdown(f"**Calculated Tolerance:** {tol:.10f}")
    st.subheader("Function")
    st.latex(f"f({x}) = {sp.latex(sp.sympify(function_input))}")


    x = sp.symbols(f'{x}')
    function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
    result = secant(x0, x1, niter, tol, function, tolerance_type)

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

    st.subheader("Results")

    # Format the dataframe to display the selected number of decimals
    result_display = result.style.format(f"{{:.{decimals}f}}")  # Use f-string to format dynamically

    # Display DataFrame
    st.dataframe(result_display, use_container_width=True)
