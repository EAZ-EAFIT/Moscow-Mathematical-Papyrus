import streamlit as st
from interface_blocks import definite_matrix_interface, calculate_tolerance, show_matrix, show_T_and_C, graph_Ab
from Methods.SOR import sor_method  # Asegúrate de que el método SOR esté implementado en el módulo correspondiente

def show_SOR():
    st.header("Successive Over-Relaxation (SOR) Method")

    # Interfaz para definir la matriz, el vector b y otros parámetros iniciales
    matrix_A, vector_b, x_0, norm_value = definite_matrix_interface(x_0="Yes")

    # Parámetros adicionales: tolerancia, iteraciones y tipo de error
    tol, niter, tolerance_type = calculate_tolerance()

    # Factor de relajación ω
    omega = st.number_input("Relaxation Factor (ω):", min_value=0.0, max_value=2.0, step=0.1, value=1.0)

    st.write("Calculated Tolerance: ", tol)

    graph_Ab(matrix_A, vector_b)

    # Ejecutar el método SOR
    X, table, rad_esp, err, T, C = sor_method(matrix_A, vector_b, x_0, tol, niter, omega, norm_value, tolerance_type)

    if err is None:
        st.success("The SOR method has converged successfully.")
        
        # Mostrar los resultados
        st.write(f"**Solution Vector (x)**")
        show_matrix(X, deci=False)
        
        st.write(f"**Solution Table**")
        show_matrix(table)
        
        st.write("Spectral Radius: ", rad_esp)
        show_T_and_C(T, C)
    else:
        st.error(err)
