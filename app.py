import streamlit as st
from pedidos import cargapedidos

def main():
    # Título de la aplicación
    st.title("Aplicación Optimización de Rutas Grupo Juyo SAC")
    
    menu = ["CLIENTES", "PEDIDOS", "VEHICULOS", "MACHINE LEARNING", "Conocenos"]
    choice = st.sidebar.selectbox("Menu", menu)
 # Lógica para mostrar el contenido correspondiente basado en la opción seleccionada
    if choice == "CLIENTES":
        st.subheader("MIS CLIENTES")
    elif choice == "PEDIDOS":
        cargapedidos()
    elif choice == "VEHICULOS":
        st.subheader("VEHICULOS")
    elif choice == "MACHINE LEARNING":
        st.subheader("Machine Learning")
    else:
        st.subheader("Conocenos") 

if __name__ == "__main__":
    main()