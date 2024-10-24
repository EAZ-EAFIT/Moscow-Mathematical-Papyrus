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
    
    pol, pol_rounded, pol_sim, pol_rounded_sim = lagrange(x_values, y_values, decimals)

    # Display results
    st.subheader("Results")
    st.write("**Lagrange Polynomial**")
    st.latex(f"P(x) = {sp.latex(pol_rounded)}")

    st.write("**Newton Polynomial Simplified**")
    st.latex(f"P(x) = {sp.latex(pol_rounded_sim)}")

    # Graph the interpolation polynomial
    st.subheader("Graph of Newton Interpolation")
    graph_with_points(x_values, y_values, pol)
