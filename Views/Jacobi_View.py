import streamlit as st
from interface_blocks import definite_matrix_interface, calculate_tolerance, show_matrix, show_T_and_C, graph_Ab
from Methods.Jacobi import jacobi_method

def show_Jacobi():
    st.header("Jacobi Method")


    matrix_A, vector_b, x_0, norm_value = definite_matrix_interface(x_0 = "Yes")

    

    tol, niter, tolerance_type = calculate_tolerance()

    st.write("Calculated Tolerance: ", tol)
    
    graph_Ab(matrix_A, vector_b)

    X, table, rad_esp, err, T, C = jacobi_method(matrix_A, vector_b, x_0, tol, niter, norm_value, tolerance_type)


    if err == None:
        st.success("The Jacobi method has converged successfully.")
        # Display the results
        st.write(f"**Solution Vector (x)**")
        show_matrix(X, deci = False)
        st.write(f"**Solution Table**")
        show_matrix(table)
        st.write("Spectral Radius: ", rad_esp)
        show_T_and_C(T, C)
    else:
        st.error(err)


