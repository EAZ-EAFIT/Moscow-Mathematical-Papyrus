import streamlit as st
import sympy as sp
from secant import secant

# Function definitions for each page
def show_home():
    st.title("Numerical Methods Project")
    st.write("Welcome to the project on numerical methods.")

def show_gradient():
    st.title("Gradient Method")
    st.write("TODO: Add details and implementation for the Gradient method.")

def show_newton():
    st.title("Newton Method")
    st.write("TODO: Add details and implementation for the Newton method.")

def show_newton_multiple_roots():
    st.title("Newton for Multiple Roots")
    st.write("TODO: Add details and implementation for Newton with multiple roots.")

def show_quasi_newton():
    st.title("Quasi-Newton Method")
    st.write("TODO: Add details and implementation for Quasi-Newton method.")

def show_secant():
    st.title("Secant Method")

    # Input parameters
    function_input = st.text_input("Enter the function of x", 
                                value="-2 ** (-x) + x * (-1 + x) - x ** (2/3) - 2")
    x0 = st.number_input("First Point (x0)", value=0.663)
    x1 = st.number_input("Second Point (x1)", value=0.664)
    niter = st.number_input("Number of Iterations", value=1000, step=1)
    tol = st.number_input("Tolerance (TOL)", value=5e-6, format="%.6f")

    x = sp.symbols('x')
    try:
        function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
    except Exception as e:
        st.error(f"Error in function input: {e}")

    if function_input:
        # Run the secant method
        result = secant(x0, x1, niter, tol, function)
        
        # Display the results in a pretty table
        st.subheader("Results")
        st.dataframe(result)

        # Print the results in console (for debugging, not usually needed in Streamlit)
        print(result)
    else:
        st.error("Please enter a valid function.")

def show_fixed_point():
    st.title("Fixed-Point Method")
    st.write("TODO: Add details and implementation for Fixed-Point method.")

def show_false_position():
    st.title("False Position Method")
    st.write("TODO: Add details and implementation for False Position method.")

def show_incremental():
    st.title("Incremental Method")
    st.write("TODO: Add details and implementation for Incremental method.")

def show_bisection():
    st.title("Bisection Method")
    st.write("TODO: Add details and implementation for Bisection method.")

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
        "Home", "Gradient", "Newton", "Newton Multiple Roots", "Quasi-Newton",
        "Secant", "Fixed-Point", "False Position", "Incremental", "Bisection",
        "Gauss-Jordan without Pivoting", "Gauss-Jordan with Partial Pivoting", "Gauss-Jordan with Total Pivoting",
        "Gauss-Jordan with Fractions", "LU Factorization", "Penalty Method (Internal/External)",
        "KKT", "BFGS"
    ]
)

# Page routing
if option == "Home":
    show_home()
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
    show_false_position()
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
