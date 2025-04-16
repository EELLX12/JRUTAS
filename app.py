import streamlit as st


def main():
    # Título de la aplicación
    st.title("Aplicación Optimización de Rutas Grupo Juyo SAC")
    
    menu = ["CLIENTES", "PEDIDOS", "VEHICULOS", "MACHINE LEARNING", "Conocenos"]
    choice = st.sidebar.selectbox("Menu", menu)
 # Lógica para mostrar el contenido correspondiente basado en la opción seleccionada
    if choice == "CLIENTES":
        st.subheader("Machine Learning")
    elif choice == "PEDIDOS":
        st.subheader("Machine Learning")
    elif choice == "VEHICULOS":
        st.subheader("Machine Learning")
    elif choice == "MACHINE LEARNING":
        st.subheader("Machine Learning")
    else:
        st.subheader("Conocenos") 

if __name__ == "__main__":
    main()