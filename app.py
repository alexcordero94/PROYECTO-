import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') 
hist_button = st.button('Construir histograma')
        
if hist_button: 
           
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            
            fig = px.histogram(car_data, x="Unnamed: 6")
        
          
            st.plotly_chart(fig, use_container_width=True)

import streamlit as st


build_histogram = st.checkbox('Construir un histograma')

if build_histogram: 
    st.write('Construir un histograma para la columna odómetro')



