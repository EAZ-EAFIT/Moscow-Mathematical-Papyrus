import streamlit as st
import sympy as sp
from Methods.spline import linear_spline_interpolation
from interface_blocks import enter_points, graph_with_points

def show_spline():
    st.header("Linear Spline Method")

    x_values, y_values = enter_points(val = 2)

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
    
    piecewise_function_unrounded, piecewise_function_rounded = linear_spline_interpolation(x_values, y_values, decimals)
    
    # Display results
    st.subheader("Results")
    st.write("**Linear Spline Piecewise Function**")
    st.write(f"$P(x) = {sp.latex(piecewise_function_rounded)}$")


    # Graph the interpolation polynomial
    st.subheader("Graph of Spline Interpolation")
    graph_with_points(x_values, y_values, piecewise_function_unrounded)

