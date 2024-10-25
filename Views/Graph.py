import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from interface_blocks import graph

def show_graph():
    st.title("Interactive Function Grapher")
    col1, col2 = st.columns(2)
    with col1:
        x = st.text_input("Enter a Variable Name", "x")
    with col2:
        function_input = st.text_input("Enter a function:", "sin(x)")
    col3, col4 = st.columns(2)
    
    x = sp.symbols(x)
    try:

        st.subheader("Your Function")
        st.latex(sp.sympify(function_input))
        
        graph(x, function_input)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
