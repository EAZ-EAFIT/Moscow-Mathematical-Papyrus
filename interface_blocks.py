import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
import plotly.graph_objs as go
import plotly.io as pio
import io

def enter_function(placeholder_variable = "x", placeholder_function = "sin(x)"):
    col1, col2 = st.columns(2)
    with col1:
        x = st.text_input(
        "Enter a Variable Name", 
        value = placeholder_variable,
        help="Enter a variable name to use in the function. Default is 'x'."
        )
    with col2:
        function_input = st.text_input(
            "Enter a function:",
            value = placeholder_function,
            help = "Enter a function in terms of the variable chosen."
            )
    return x, function_input

def calculate_tolerance():
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
    return tol, niter, tolerance_type

def graph(x, function_input):
    
    function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
    st.subheader("Graph")

    col7, col8 = st.columns(2)
    with col7:
        x_min = st.number_input(f"Enter the minimum value for {x}", value=0, step=1)
    with col8:
        x_max = st.number_input(f"Enter the maximum value for {x}", value=10, step=1)


    x_vals = np.linspace(x_min, x_max, 1000)
    y_vals = function(x_vals)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=function_input))

    fig.update_layout(
            title=f"Graph of {function_input}",
            xaxis_title= str(x),
            yaxis_title= f"f({str(x)})",
            showlegend=True,
            margin=dict(l=0, r=0, t=40, b=0),
            hovermode="closest"
    )

    fig.update_xaxes(rangeslider_visible=False)
    fig.update_yaxes(fixedrange=False)

    st.plotly_chart(fig)

    # Download button for the graph
    buf = io.BytesIO()
    pio.write_image(fig, buf, format='svg')
    buf.seek(0)

    st.download_button(
        label="Download Graph as SVG",
        data=buf,
        file_name="newton_raphson_graph.svg",
        mime="image/svg"
    )


def definite_matrix_interface():
    col1 = st.columns(1)[0]
    with col1:
        rows_A = st.number_input("Enter number of rows:", min_value=1, value=3)
        cols_A = rows_A

    col2, col3 = st.columns(2)
    with col2:

        matrix_A = pd.DataFrame(np.zeros((rows_A, cols_A)), columns=[f'x_{i}' for i in range(cols_A)])

        st.write("A matrix:")
        edited_matrix = st.data_editor(matrix_A, num_rows="fixed")

        # Convert the edited matrix to a NumPy array
        matrix_A = edited_matrix.to_numpy()
    with col3:
        rows_b = rows_A
        cols_b = 1
        vector_b = pd.DataFrame(np.zeros((rows_b, cols_b)), columns=[f'b' for i in range(cols_b)])

        st.write("b vector:")
        edited_vector = st.data_editor(vector_b, num_rows="fixed")

        vector_b = edited_vector.to_numpy()

    return matrix_A, vector_b

def iterative_matrix_interface():
    col1 = st.columns(1)[0]
    with col1:
        rows_A = st.number_input("Enter number of rows:", min_value=1, value=3)
        cols_A = rows_A

    col2, col3, col4 = st.columns(3)
    with col2:

        matrix_A = pd.DataFrame(np.zeros((rows_A, cols_A)), columns=[f'x_{i}' for i in range(cols_A)])

        st.write("A matrix:")
        edited_matrix = st.data_editor(matrix_A, num_rows="fixed")

        # Convert the edited matrix to a NumPy array
        matrix_A = edited_matrix.to_numpy()
    with col3:
        rows_b = rows_A
        cols_b = 1
        vector_b = pd.DataFrame(np.zeros((rows_b, cols_b)), columns=[f'b' for i in range(cols_b)])

        st.write("b vector:")
        edited_vector = st.data_editor(vector_b, num_rows="fixed")

        vector_b = edited_vector.to_numpy()
    with col4:
        rows_x0 = rows_A
        cols_x0 = 1
        vector_x0 = pd.DataFrame(np.zeros((rows_x0, cols_x0)), columns=[f'x_{i}' for i in range(cols_x0)])

        st.write("Initial guess vector:")
        edited_vector_x0 = st.data_editor(vector_x0, num_rows="fixed")

        vector_x0 = edited_vector_x0.to_numpy()
    
    calculate_tolerance()

    return matrix_A, vector_b, vector_x0

def enter_points():
    # Use Streamlit's session state to retain current points
    if 'x_values' not in st.session_state:
        st.session_state.x_values = []
    if 'y_values' not in st.session_state:
        st.session_state.y_values = []

    # Get the number of points from user input
    num_points = st.number_input(
        "Enter the number of points:", 
        min_value=1, 
        value=len(st.session_state.x_values) or 1,  # Default to current number of points or 1
        step=1, 
        key="num_points"
    )

    # Create a DataFrame to hold the points
    points_df = pd.DataFrame(np.zeros((2, num_points)), index=['x', 'y'])

    # Fill in existing x and y values if available
    if len(st.session_state.x_values) > 0:
        points_df.iloc[0][:len(st.session_state.x_values)] = st.session_state.x_values
        points_df.iloc[1][:len(st.session_state.y_values)] = st.session_state.y_values
        
        # If the last x value exists, set the next x value to one more
        if len(st.session_state.x_values) < num_points:
            points_df.iloc[0][len(st.session_state.x_values)] = st.session_state.x_values[-1] + 1

    # Allow the user to edit the DataFrame
    edited_points_df = st.data_editor(points_df, num_rows="fixed", key="points_editor", use_container_width=True)

    # Update session state with new values
    st.session_state.x_values = edited_points_df.iloc[0].tolist()
    st.session_state.y_values = edited_points_df.iloc[1].tolist()

    return st.session_state.x_values, st.session_state.y_values

# Function to graph Newton interpolation result
def graph_with_points(x_values, y_values, function, x_symbol = sp.symbols("x")):

    function = sp.lambdify(x_symbol, function, "numpy")

    x_min = min(x_values) - 1
    x_max = max(x_values) + 1
    x_vals = np.linspace(x_min, x_max, 500)
    y_vals = [function(x_val) for x_val in x_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Polynomial P(x)'))
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers', name='Data Points'))


    fig.update_layout(
        title=f"Graph of the Interpolation",
        xaxis_title=str(x_symbol),
        yaxis_title=f"y",
        showlegend=True,
        margin=dict(l=0, r=0, t=40, b=0),
        hovermode="closest"
    )

    st.plotly_chart(fig)

    buf = io.BytesIO()
    pio.write_image(fig, buf, format='svg')
    buf.seek(0)
    st.download_button(
        label="Download Graph as SVG",
        data=buf,
        file_name="interpolation_graph.svg",
        mime="image/svg"
    )

def show_table(result, deci = True, decimals = None):
    if deci:
        decimals = st.slider(
            "Select number of decimals to display on table",
            min_value=1, 
            max_value=10, 
            value=4,
            help="Adjust the number of decimal places for the result table."
        )
    if deci or decimals != None:

        result = result.style.format(f"{{:.{decimals}f}}")

    st.dataframe(result, use_container_width=True)