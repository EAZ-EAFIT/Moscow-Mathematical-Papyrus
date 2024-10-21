import streamlit as st
from Views.Graph import show_graph
from Views.Newton_View import show_newton
from Views.Secant_View import show_secant
from Views.Bisection_View import show_bisection
from Views.RegulaFalsi_View import show_regula_falsi
from Views.Incremental_View import show_incremental

# Function definitions for each page
def show_home():
    st.title("Numerical Methods Project")
    st.write("Welcome to the project on numerical methods.")

def show_gradient():
    st.title("Function Graphing")
    st.write("TODO: Add details and implementation for the Gradient method.")

def show_gradient():
    st.title("Gradient Method")
    st.write("TODO: Add details and implementation for the Gradient method.")

def show_newton_multiple_roots():
    st.title("Newton for Multiple Roots")
    st.write("TODO: Add details and implementation for Newton with multiple roots.")

def show_quasi_newton():
    st.title("Quasi-Newton Method")
    st.write("TODO: Add details and implementation for Quasi-Newton method.")

def show_fixed_point():
    st.title("Fixed-Point Method")
    st.write("TODO: Add details and implementation for Fixed-Point method.")

def show_gauss_jordan_no_pivot():
    st.title("Gauss-Jordan without Pivoting")
    st.write("TODO: Add details and implementation for Gauss-Jordan without pivoting.")

def show_gauss_jordan_partial_pivot():
    st.title("Gauss-Jordan with Partial Pivoting")
    st.write("TODO: Add details and implementation for Gauss-Jordan with partial pivoting.")

def show_gauss_jordan_total_pivot():
    st.title("Gauss-Jordan with Total Pivoting")
    st.write("TODO: Add details and implementation for Gauss-Jordan with total pivoting.")

def show_gauss_jordan_fractions():
    st.title("Gauss-Jordan with Fractions")
    st.write("TODO: Add details and implementation for Gauss-Jordan with fractions.")

def show_lu_factorization():
    st.title("LU Factorization")
    st.write("TODO: Add details and implementation for LU Factorization.")

def show_penalty_method():
    st.title("Penalty Method (Internal/External)")
    st.write("TODO: Add details and implementation for Penalty methods.")

def show_kkt():
    st.title("KKT Method")
    st.write("TODO: Add details and implementation for KKT.")

def show_bfgs():
    st.title("BFGS Method")
    st.write("TODO: Add details and implementation for BFGS.")

# Sidebar navigation
st.sidebar.title("Numerical Methods Menu")
option = st.sidebar.selectbox(
    "Choose a method:",
    [
        "Home", "Function Graphing", "Gradient", "Newton", "Newton Multiple Roots", "Quasi-Newton",
        "Secant", "Fixed-Point", "False Position", "Incremental", "Bisection",
        "Gauss-Jordan without Pivoting", "Gauss-Jordan with Partial Pivoting", "Gauss-Jordan with Total Pivoting",
        "Gauss-Jordan with Fractions", "LU Factorization", "Penalty Method (Internal/External)",
        "KKT", "BFGS"
    ]
)

# Page routing
if option == "Home":
    show_home()
if option == "Function Graphing":
    show_graph()
elif option == "Gradient":
    show_gradient()
elif option == "Newton":
    show_newton()
elif option == "Newton Multiple Roots":
    show_newton_multiple_roots()
elif option == "Quasi-Newton":
    show_quasi_newton()
elif option == "Secant":
    show_secant()
elif option == "Fixed-Point":
    show_fixed_point()
elif option == "False Position":
    show_regula_falsi()
elif option == "Incremental":
    show_incremental()
elif option == "Bisection":
    show_bisection()
elif option == "Gauss-Jordan without Pivoting":
    show_gauss_jordan_no_pivot()
elif option == "Gauss-Jordan with Partial Pivoting":
    show_gauss_jordan_partial_pivot()
elif option == "Gauss-Jordan with Total Pivoting":
    show_gauss_jordan_total_pivot()
elif option == "Gauss-Jordan with Fractions":
    show_gauss_jordan_fractions()
elif option == "LU Factorization":
    show_lu_factorization()
elif option == "Penalty Method (Internal/External)":
    show_penalty_method()
elif option == "KKT":
    show_kkt()
elif option == "BFGS":
    show_bfgs()
