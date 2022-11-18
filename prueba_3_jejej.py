#$ pip install streamlit --upgrade

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import urllib.request
import base64
from PIL import Image

st.title('Datos Hidrometereológicos Gobierno Regional Piura')

st.markdown("""
	Esta pagina web "app" exploratoria permite visualizar a cualquier usuario los datos hidrometereológicos del Gobierno Regional de Piura
	* **Agua y Saneamiento** : como lo siguiente
	asda
	* **Para mayor información también puede ingresar a** : http://servicios.regionpiura.gob.pe/datosh
	""")

from PIL import Image
image = Image.open('Proyecto_Piura.jpg')
st.image(image, caption='La contaminación por el parque automotor antiguo es un problema en Lima Metropolitana', use_column_width=True)

st.sidebar.header("Entradas del usuario")
selected_year=st.sidebar.selectbox('Año', list(reversed(range(2010,2021))))
