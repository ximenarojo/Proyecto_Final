

import streamlit as st
import pandas as pd
import numpy as np



df_ubigeO=pd.read_csv('TB_UBIGEOS.csv')



st.map(df_ubigeo)


