

import streamlit as st
import pandas as pd
import numpy as np



df_ubigeo = pd.read_csv('TB_UBIGEOS.csv')


df_ubigeo=df_ubigeo.rename(columns={'latitud':'lat', 'longitud':'lon'})
st.map(df_ubigeo[['lat','lon']])


