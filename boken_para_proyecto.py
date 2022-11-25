

import streamlit as st
import pandas as pd
import numpy as np

df_visualizacion=pd.read_csv('TB_UBIGEOS.csv')

st.dataframe(df_visualizacion)

df_actividad_freq = pd.DataFrame(df_visualizacion["provincia"].value_counts())
labels = df_actividad_freq.index.tolist()
sizes = df_actividad_freq["provincia"].tolist()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
startangle=0)
#plt.title('Distribucion de datos segun provincia')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

df_anho_freq = pd.DataFrame(df_visualizacion["region"].value_counts())
st.bar_chart(df_anho_freq)

df_visualizacion = df_visualizacion.rename(columns={'latitud':'lat', 'longitud':'lon'})
st.map(df_visualizacion[['lat','lon']])


