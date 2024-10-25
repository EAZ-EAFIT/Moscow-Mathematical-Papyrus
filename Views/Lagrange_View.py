import streamlit as st
import pandas as pd
import sympy as sp
from Methods.lagrange import lagrange
from interface_blocks import enter_points, graph_with_points, show_table

def show_lagrange():
    st.header("Lagrange Method")

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
    
    pol_decimal, pol_rounded_decimal, newton_poly_expr_unrounded, newton_poly_expr_rounded = lagrange(x_values, y_values, decimals)

    # Display results
    st.subheader("Results")
    st.write("**Lagrange Polynomial**")
    st.write(f"$P(x) = {sp.latex(pol_rounded_decimal)}$")

    st.write("**Lagrange Polynomial Simplified**")
    st.write(f"$P(x) = {sp.latex(newton_poly_expr_rounded)}$")

    # Graph the interpolation polynomial
    st.subheader("Graph of Lagrange Interpolation")
    graph_with_points(x_values, y_values, pol_decimal)
