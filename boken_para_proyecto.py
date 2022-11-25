

import streamlit as st
import pandas as pd
import numpy as np

df_visualizacion=pd.read_csv('TB_UBIGEOS.csv')

st.dataframe(df_visualizacion)

