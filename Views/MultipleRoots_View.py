import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
from interface_blocks import enter_function, calculate_tolerance, graph, show_table
from Methods.MultipleRoots import multiple_roots

def show_multiple_roots():
    st.header("Multiple Roots Method")
    
    # Entrada de función y variable
    x, function_input = enter_function()

    col3 = st.columns(1)[0]
    with col3:
        x0 = st.number_input(
            "Initial Point (x_0)",
            format="%.4f",
            value=1.0,
            step=0.0001,
            help="Initial guess for the root. The method requires an initial value close to the actual root."
        )

    # Calcular tolerancia
    tol, niter, tolerance_type = calculate_tolerance()
    st.markdown(f"**Calculated Tolerance:** {tol:.10f}")
    st.subheader("Function")
    st.latex(f"f({x}) = {sp.latex(sp.sympify(function_input))}")
    
    # Preparar función, derivadas y método
    x = sp.symbols(f'{x}')
    function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
    df = sp.lambdify(x, sp.diff(sp.sympify(function_input), x), 'numpy')
    d2f = sp.lambdify(x, sp.diff(sp.diff(sp.sympify(function_input), x), x), 'numpy')
    
    result = multiple_roots(x0, niter, tol, function, df, d2f, tolerance_type)
    
    # Mostrar resultados o errores
    if result["status"] == "error":
        st.error(result["message"])
    else:
        show_table(result["table"])
    
    # Gráfica de la función
    graph(x, function_input)
 