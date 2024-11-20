import streamlit as st
import sympy as sp
import numpy as np
from Methods.Spline_quadratic import quadratic_spline_interpolation
from interface_blocks import enter_points, graph_with_points

def show_quadratic_spline():
    st.header("Quadratic Spline Method")

    # Input points (minimum 3 points required for quadratic spline)
    x_values, y_values = enter_points(val=3)

    # Input validation
    if len(x_values) != len(set(x_values)):
        st.error("Error: The points entered have an x-repeated value, which makes it impossible to be represented as a function.")
        return
    
    if len(x_values) < 3:
        st.error("Error: At least 3 points are required for quadratic spline interpolation.")
        return

    try:
        # Sort points by x-values
        points = sorted(zip(x_values, y_values))
        x_values, y_values = zip(*points)
        x_values = list(x_values)
        y_values = list(y_values)

        # Slider for decimal precision
        decimals = st.slider(
            "Select number of decimals to display",
            min_value=1, 
            max_value=10, 
            value=4,
            help="Adjust the number of decimal places for the result."
        )

        # Perform quadratic spline interpolation
        try:
            piecewise_function_unrounded, piecewise_function_rounded = quadratic_spline_interpolation(
                x_values, 
                y_values, 
                decimals=decimals
            )

            # Display results
            st.subheader("Results")
            st.write("**Quadratic Spline Piecewise Function**")
            st.latex(sp.latex(piecewise_function_rounded))

            # Convert the symbolic function to a numerical function
            spline_function = sp.lambdify(sp.symbols('x'), piecewise_function_unrounded)

            # Generate numerical values for plotting
            x_plot = np.linspace(min(x_values), max(x_values), 500)
            try:
                # Graph the interpolation
                st.subheader("Graph of Spline Interpolation")
                graph_with_points(x_values, y_values, piecewise_function_unrounded)

            except Exception as e:
                st.error(f"Error calculating function values: {str(e)}")

        except ValueError as e:
            st.error(f"Error during interpolation: {str(e)}")

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")