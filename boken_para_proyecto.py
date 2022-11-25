

import streamlit as st
import pandas as pd
import numpy as np

df_visualizacion=pd.read_csv('TB_UBIGEOS.csv')

df_visualizacion = df_visualizacion.rename(columns={'latitud':'lat', 'longitud':'lon'})
st.map(df_visualizacion[['lat','lon']])

