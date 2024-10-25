import streamlit as st
import pandas as pd
import sympy as sp
from Methods.newton_interpolation import newton_interpolation
from interface_blocks import enter_points, graph_with_points, show_table

def show_newton_divided_diff():
    st.header("Newton Interpolation Method")

    x_values, y_values = enter_points()

    # Check for repeated x values
    if len(x_values) != len(set(x_values)):
        st.error("Error: The points entered have an x-repeated value, which makes it impossible to be represented as a function.")
        return  # Stop further execution if there are repeated x values
    
    decimals = st.slider(
            "Select number of decimals to display",
            min_value=1, 
            max_value=10, 
            value=4,
            help="Adjust the number of decimal places for the result table."
        )
    
    matrix, coefficients, rounded_coefficients,newton_poly_unrounded,  newton_poly_expr_unrounded, newton_poly_rounded, newton_poly_expr_rounded = newton_interpolation(x_values, y_values, decimals)

    # Display results
    st.subheader("Results")
    st.write("**Divided Differences Table** The Coefficients of the Newton Interpolation Polynomial are displayed on the Diagonal.")
    show_table(pd.DataFrame(matrix), deci= False, decimals = decimals)

    st.write("**Newton Polynomial**")
    st.latex(f"P(x) = {sp.latex(newton_poly_rounded)}")

    st.write("**Newton Polynomial Simplified**")
    st.latex(f"P(x) = {sp.latex(newton_poly_expr_rounded)}")

    # Graph the interpolation polynomial
    st.subheader("Graph of Newton Interpolation")
    graph_with_points(x_values, y_values, newton_poly_expr_unrounded)
