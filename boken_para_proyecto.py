

import streamlit as st
import pandas as pd
import numpy as np

df_mapa = pd.read_csv('DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv')

df_ubigeo = pd.read_csv('TB_UBIGEOS.csv')


df = df.rename(columns={'latitud':'lat', 'longitud':'lon'})
st.map(df[['lat','lon']])


