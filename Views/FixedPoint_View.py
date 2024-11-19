import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
from interface_blocks import enter_function, calculate_tolerance, graph

def show_fixed_point():
    st.header("Fixed-Point Iteration Method")

    # Function and variable input
    x, function_input = enter_function(placeholder_function="cos(x)", placeholder_variable="x")

    # Initial guess input
    x0 = st.number_input(
        "Initial guess (x₀)",
        format="%.4f",
        value=0.5,
        step=0.0001,
        help="Provide the initial guess for the root."
    )

    # Tolerance and iteration settings
    tol, niter, tolerance_type = calculate_tolerance()
    st.markdown(f"**Calculated Tolerance:** {tol:.10f}")

    # Parse function and variable
    x_symbol = sp.symbols(f'{x}')
    function = sp.sympify(function_input)

    # Display the function in LaTeX
    st.subheader("Function")
    st.latex(f"g({x_symbol}) = {sp.latex(function)}")

    # Lambdify the function for numerical evaluations
    g = sp.lambdify(x_symbol, function, "numpy")

    # Fixed-Point Iteration Algorithm
    st.subheader("Results")
    table_data = {"Iteration": [], "xₙ": [], "Error": []}
    x_prev = x0
    converged = False

    for i in range(1, niter + 1):
        x_next = g(x_prev)
        error = abs(x_next - x_prev)

        # Append iteration data
        table_data["Iteration"].append(i)
        table_data["xₙ"].append(x_next)
        table_data["Error"].append(error)

        # Check for convergence
        if error < tol:
            converged = True
            break

        x_prev = x_next

    # Display results table
    result_df = pd.DataFrame(table_data)
    decimals = st.slider(
        "Select number of decimals to display on table",
        min_value=1,
        max_value=10,
        value=4,
        help="Adjust the number of decimal places for the result table."
    )
    result_display = result_df.style.format(f"{{:.{decimals}f}}")
    st.dataframe(result_display, use_container_width=True)

    if converged:
        st.success(f"The method converged to {x_next:.{decimals}f} after {i} iterations.")
    else:
        st.warning("The method did not converge within the maximum number of iterations.")

    # Graph the function
    graph(x_symbol, function_input)
