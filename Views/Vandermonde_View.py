import streamlit as st
import sympy as sp
from Methods.Vandermonde import vandermonde
from interface_blocks import enter_points, graph_with_points

def show_vandermonde():
    st.header("Vandermonde Method")

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

    coeffs, rounded_coefficients, poly, poly_rounded = vandermonde(x_values, y_values, decimals)

    st.subheader("Results")
    st.write("**Vandermonde Polynomial**")
    st.write(f"$P(x) = {sp.latex(poly_rounded)}$")

    st.subheader("Graph of Vandermonde Interpolation")
    graph_with_points(x_values, y_values, poly)