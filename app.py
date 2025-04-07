import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv("vehicles_us.csv")

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    if "odometer" in df.columns:        
            # crear un histograma
        fig = px.histogram(df, x="odometer", title="Histograma de odómetro")
    else:
        fig = px.histogram(df, x=df.columns[0], title=f"Histograma de {df.columns[0]}")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    if "odometer" in df.columns and "price" in df.columns:        
            # crear un histograma
        fig2 = px.scatter(df, x="odometer", y="price", title="Precio vs Odómetro")
        st.plotly_chart(fig2,use_container_width=True)
    else:
        st.write("Las columnas necesarias para el gráfico no están disponibles")
        