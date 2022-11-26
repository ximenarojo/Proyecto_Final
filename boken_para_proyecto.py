

import streamlit as st
import pandas as pd
import numpy as np

df_mapa=pd.read_csv('TB_UBIGEOS.csv')

st.dataframe(df_visualizacion)

df_anho_freq = pd.DataFrame(df_visualizacion["region"].value_counts())
st.bar_chart(df_anho_freq)


df =  df_mapa.rename(columns={'LATITUD':'lat', 'LONGITUD':'lon'})

st.map(df)


