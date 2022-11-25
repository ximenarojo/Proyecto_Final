

import streamlit as st
import pandas as pd
import numpy as np

df_visualizacion=pd.read_csv('TB_UBIGEOS.csv')

st.dataframe(df_visualizacion)

df_anho_freq = pd.DataFrame(df_visualizacion["region"].value_counts())
st.bar_chart(df_anho_freq)

df_visualizacion = df_visualizacion.rename(columns={'latitud':'LAT', 'longitud':'LON'})
st.map(df_visualizacion[['LAT','LON']])


