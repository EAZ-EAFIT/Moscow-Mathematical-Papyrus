import streamlit as st

# Import necessary views for each method
from Views.Graph import show_graph
from Views.Newton_View import show_newton
from Views.Secant_View import show_secant
from Views.Bisection_View import show_bisection
from Views.RegulaFalsi_View import show_regula_falsi
from Views.Incremental_View import show_incremental
from Views.GaussNoPivot_View import show_gauss_jordan_no_pivot
from Views.GaussPartialPivot_View import show_gauss_jordan_partial_pivot
from Views.GaussTotalPivot_View import show_gauss_jordan_total_pivot
from Views.LU_Factorization_View import show_lu_factorization
from Views.Vandermonde_View import show_vandermonde
from Views.NewtonDividedDiff_View import show_newton_divided_diff
from Views.Lagrange_View import show_lagrange
from Views.Spline_View import show_spline

# Initialize session state if not already initialized
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function definitions for each page
def show_home():
    st.title("Numerical Methods Project")
    st.write("Welcome to the project on numerical methods. Choose a category from the sidebar.")

# Sidebar navigation and categories with buttons for each method
st.sidebar.title("Numerical Methods Menu")

# Button for "Function Graphing"
if st.sidebar.button("Show Graph"):
    st.session_state.page = "graph"

# Buttons for "Finding Roots"
if st.sidebar.button("Finding Roots"):
    st.session_state.page = "roots"

# Buttons for "Solving Systems of Equations"
if st.sidebar.button("Solving Systems of Equations"):
    st.session_state.page = "systems"

# Buttons for "Interpolation Methods"
if st.sidebar.button("Interpolation Methods"):
    st.session_state.page = "interpolation"

# Render the page based on session state
if st.session_state.page == "home":
    show_home()

elif st.session_state.page == "graph":
    show_graph()

elif st.session_state.page == "roots":
    st.title("Finding Roots of Polynomials")
    
    # Dropdown to select root-finding method
    root_method = st.selectbox(
        "Select a root-finding method",
        ["Newton", "Secant", "Bisection", "False Position", "Incremental Search"]
    )
    
    # Display the corresponding method content based on the dropdown selection
    if root_method == "Newton":
        show_newton()
    elif root_method == "Secant":
        show_secant()
    elif root_method == "Bisection":
        show_bisection()
    elif root_method == "False Position":
        show_regula_falsi()
    elif root_method == "Incremental Search":
        show_incremental()

elif st.session_state.page == "systems":
    st.title("Solving Systems of Equations")
    
    # Dropdown to select a system-solving method
    system_method = st.selectbox(
        "Select a system-solving method",
        ["Gauss-Jordan without Pivoting", "Gauss-Jordan with Partial Pivoting", "Gauss-Jordan with Total Pivoting", "LU Factorization"]
    )
    
    # Display the corresponding method content based on the dropdown selection
    if system_method == "Gauss-Jordan without Pivoting":
        show_gauss_jordan_no_pivot()
    elif system_method == "Gauss-Jordan with Partial Pivoting":
        show_gauss_jordan_partial_pivot()
    elif system_method == "Gauss-Jordan with Total Pivoting":
        show_gauss_jordan_total_pivot()
    elif system_method == "LU Factorization":
        show_lu_factorization()

elif st.session_state.page == "interpolation":
    st.title("Interpolation Methods")
    # Dropdown to select interpolation method
    interpolation_method = st.selectbox(
        "Select an interpolation method",
        ["Vandermonde Matrix", "Newton Divided Difference", "Lagrange Interpolation", "Spline Interpolation (Linear, Square, Cubic)"]
    )
    
    # Display the corresponding method content based on the dropdown selection
    if interpolation_method == "Vandermonde Matrix":
        show_vandermonde()
    elif interpolation_method == "Newton Divided Difference":
        show_newton_divided_diff()
    elif interpolation_method == "Lagrange Interpolation":
        show_lagrange()
    elif interpolation_method == "Spline Interpolation (Linear, Square, Cubic)":
        show_spline()

