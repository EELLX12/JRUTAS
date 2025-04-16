import streamlit as st 
import pandas as pd

def cargapedidos():
    st.subheader("Pedidos")
    try:
        df = pd.read_csv("data/pedidos.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.error("No se encontró el archivo 'data/pedidos.csv")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    cargapedidos()