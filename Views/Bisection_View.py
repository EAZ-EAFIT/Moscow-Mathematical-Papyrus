import streamlit as st
import sympy as sp
from interface_blocks import enter_function, calculate_tolerance, graph
from Methods.Bisection import bisection

def show_bisection():

    st.markdown("""
    The **Bisection Method** is a numerical technique used to find roots of a continuous function  f(x)  
    over a specified interval. It is based on the **Intermediate Value Theorem**, which states that if a continuous 
    function changes sign over an interval [a, b], then there is at least one root in that interval.
    """)

    with st.expander("📘 How the Bisection Method Works"):
        st.markdown("""
        **1. Define the Interval [a, b]:**
        - Choose an interval [a, b] such that.""")
        st.latex(r"""f(a) \cdot f(b) < 0""")
        st.markdown("""
        - This ensures a root exists in the interval.

        **2. Compute the Midpoint:**
        - The midpoint  c  of the interval is computed as:
        """)
        st.latex(r"""
        c = \frac{a + b}{2}
        """)
        st.markdown("""
        **3. Evaluate the Function at the Midpoint:**
        - Check the sign of  f(c) :
          - If  f(c) = 0 ,  c  is the root.
          - If  the following condition is met, the root lies in [a, c]:""")
        st.latex(r"""f(a) \cdot f(c) < 0""")
        st.markdown("""
          - Otherwise, the root lies in [c, b].

        **4. Repeat:**
        - Update the interval to [a, c] or [c, b] and repeat steps 2-3 until the interval is sufficiently small 
          or the function value at  c  is close enough to zero.

        **Convergence:**
        - The Bisection Method guarantees convergence to a root if  f(x)  is continuous on [a, b].
        """)


    try:
        st.header("Bisection Method")

        x, function_input = enter_function(placeholder_function="x**2 - 4", placeholder_variable="x")

        col3, col4 = st.columns(2)
        with col3:
            a = st.number_input(
            "Initial point of search interval (a)",
            format="%.4f",
            value = 0.1,
            step = 0.0001,
            help="The infimum of the desired search interval [a, b]."
            )
        with col4:
            b = st.number_input(
            "End point of search interval (b)",
            format="%.4f",
            value = 3.0,
            step = 0.0001,
            help="The supremum of the desired search interval [a, b]."
            )

        tol, niter, tolerance_type = calculate_tolerance()
        st.markdown(f"**Calculated Tolerance:** {tol:.10f}")

        x = sp.symbols(f'{x}')
        function = sp.sympify(function_input)

        st.subheader("Function")
        st.latex(f"f({x}) = {sp.latex(function)}")

        function = sp.lambdify(x, sp.sympify(function_input), 'numpy')

        # DO CHECKS ON INPUT INTEGRITY
        # check if derivative is continuous in general

        result = bisection(a, b, niter, tol, tolerance_type, function)

        if result["status"] == "error":
            st.error(result["message"])
            return
        else:
            result = result["table"]

        # Add a slider to choose the number of decimals to display
        decimals = st.slider(
            "Select number of decimals to display on table",
            min_value=1,
            max_value=10,
            value=4,
            help="Adjust the number of decimal places for the result table."
        )
        # Format the dataframe to display the selected number of decimals
        result_display = result.style.format(f"{{:.{decimals}f}}")  # Use f-string to format dynamically

        st.subheader("Results")
        st.dataframe(result_display, use_container_width=True)

        mid = result.iloc[-1]['mid']
        st.success(f"Root found at x = {mid:.{decimals}f}: f({mid:.{decimals}f}) = {function(mid):.{decimals}f}")

        graph(x, function_input)
    except Exception as e:
        st.error("Error: Check your inputs ")