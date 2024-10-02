import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objs as go

def show_graph():
    st.title("Interactive Function Grapher")

    col1, col2 = st.columns(2)
    with col1:
        x = st.text_input("Enter a Variable Name", "x")
    with col2:
        function_input = st.text_input("Enter a function:", "sin(x)")

    col3, col4 = st.columns(2)
    with col3:
        x_min = st.number_input(f"Enter the minimum value for {x}", value=0, step=1)
    with col4:
        x_max = st.number_input(f"Enter the maximum value for {x}", value=10, step=1)

    x = sp.symbols(x)

    try:
        function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
        x_vals = np.linspace(x_min, x_max, 1000)
        y_vals = function(x_vals)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=function_input))

        st.subheader("Your Function")
        st.latex(sp.sympify(function_input))

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

    except Exception as e:
        st.error(f"Error: {str(e)}")
