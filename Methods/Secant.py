import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def secant(x0, x1, niter, tol, function):
    table = []
    
    # Initial setup
    xn = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
    x_prev = x1
    x_prev2 = x0
    err = 100
    iter = 0

    # First iteration (iteration 0)
    row = {
        "x_{n-1}": x0,
        "x_n": x1,
        "f(x_n)": function(x1),
        "Relative Error (%)": None
    }
    table.append(row)

    # Secant method iterations
    while iter < niter and err >= tol:
        # Update xn
        xn = x_prev - function(x_prev) * (x_prev - x_prev2) / (function(x_prev) - function(x_prev2))
        
        # Calculate relative error
        err = abs((xn - x_prev) / xn)
        
        # Append row for current iteration
        row = {
            "x_{n-1}": x_prev,
            "x_n": xn,
            "f(x_n)": function(xn),
            "Relative Error (%)": err
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
        x = st.text_input("Enter a Variable Name", "x")
    with col2:
        function_input = st.text_input("Enter a function:", "sin(x)")

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

    col5, col6 = st.columns(2)
    with col5:
        niter = st.number_input(
        "Number of Iterations",
        value=1000,
        min_value=1,
        step=1,
        help="The maximum number of iterations the algorithm will perform to find the root. Higher values allow for more precision."
    )

    with col6:
        tol = st.number_input(
            "Tolerance (TOL)",
            value=5e-6,
            format="%.10f",
            step = 0.0000000001,
            help="The acceptable error margin for the root. The algorithm will stop if the error is less than this value."
        )

    st.subheader("Function")
    st.latex(sp.sympify(function_input))

    x = sp.symbols(f'{x}')
    function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
    result = secant(x0, x1, niter, tol, function)
        
    st.subheader("Results")
    st.dataframe(result)