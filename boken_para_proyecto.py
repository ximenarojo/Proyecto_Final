

import streamlit as st
import pandas as pd
import numpy as np

df_mapa = pd.read_csv('DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv')

df_ubigeo = pd.read_csv('TB_UBIGEOS.csv')

@st.experimental_memo

df_ubigeo = df_ubigeo.rename(columns={'LATITUD':'latitud', 'LONGITUD':'longitud'})
st.map(df_ubigeo[['latitud','longitud']])


