import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def secant(x0, x1, niter, tol, function, tolerance_type):
    table = []
    
    # Initial setup
    xn = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
    x_prev = x1
    x_prev2 = x0
    err = 100
    iter = 0

    Error = "Relative Error" if tolerance_type == "Significant Figures" else "Absolute Error"

    # First iteration (iteration 0)
    row = {
        "x_{n-1}": x0,
        "x_n": x1,
        "f(x_n)": function(x1),
        f"{Error}": None
    }
    table.append(row)

    # Secant method iterations
    while iter < niter and err >= tol:
        # Update xn
        xn = x_prev - function(x_prev) * (x_prev - x_prev2) / (function(x_prev) - function(x_prev2))
        
        # Calculate error based on tolerance type
        if tolerance_type == "Significant Figures":
            # Calculate relative error
            err = abs((xn - x_prev) / xn)
        elif tolerance_type == "Correct Decimals":
            # Calculate absolute error
            err = abs(xn - x_prev)

        # Append row for current iteration
        row = {
            "x_{n-1}": x_prev,
            "x_n": xn,
            "f(x_n)": function(xn),
            f"{Error}": err
        }
        table.append(row)

        iter += 1
        x_prev2 = x_prev
        x_prev = xn

    # Convert table to DataFrame and return
    df = pd.DataFrame(table)
    return df


def show_secant():
    st.title("Secant Method")

    col1, col2 = st.columns(2)
    with col1:
        x = st.text_input(
        "Enter a Variable Name", 
        value = "x",
        help="Enter a variable name to use in the function. Default is 'x'."
        )
    with col2:
        function_input = st.text_input(
            "Enter a function:",
            value = "sin(x)",
            help = "Enter a function in terms of the variable chosen."
            )

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

    col5, col6, col7 = st.columns(3)
    with col5:
        # Ask whether the user wants to use significant figures or decimal places
        tolerance_type = st.radio(
            "Tolerance Type",
            ("Correct Decimals", "Significant Figures"),
            help="Choose whether you want to set the tolerance based on significant figures or correct decimal places."
        )

    with col6:
        # Ask for the number of significant figures or correct decimals
        if tolerance_type == "Significant Figures":
            num_figures = st.number_input(
                "Number of Significant Figures",
                value=5,
                min_value=1,
                step=1,
                help="The number of significant figures to use for tolerance calculation."
            )
            # Calculate tolerance based on significant figures
            tol = 5 * 10 ** (-num_figures)

        elif tolerance_type == "Correct Decimals":
            num_decimals = st.number_input(
                "Number of Correct Decimals",
                value=6,
                min_value=1,
                step=1,
                help="The number of correct decimals to use for tolerance calculation."
            )
            # Calculate tolerance based on correct decimals
            tol = 0.5 * 10 ** (-num_decimals)

    with col7:
        niter = st.number_input(
        "Number of Iterations",
        value=1000,
        min_value=1,
        step=1,
        help="The maximum number of iterations the algorithm will perform to find the root. Higher values allow for more precision."
    )
    st.markdown(f"**Calculated Tolerance:** {tol:.10f}")
    st.subheader("Function")
    st.latex(f"f({x}) = {sp.latex(sp.sympify(function_input))}")


    x = sp.symbols(f'{x}')
    function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
    result = secant(x0, x1, niter, tol, function, tolerance_type)

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
    

show_secant()
