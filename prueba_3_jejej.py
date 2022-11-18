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
	* **Agua y Saneamiento:** Contiene los datos Hidrometeorológicos del Sistema Hidráulico Mayor a cargo del  Proyecto Especial Chira Piura.
        Este dataset muestra los datos hidrometereológicos registrados de las presas, estaciones hidrológicas e hidrométricas.
        Esta información contiene el nombre de la cuenca, nombre de la estación, medida del caudal a las 007:00 horas, el promedio del caudal a las 
	24:00 horas, el caudal máximo a las 24:00 horas, niveles de presas a las 7:00 horas, nivel máximo de las presas a las 24:00 horas, el volumen 
	de las presas a las 07:00 y precipitaciones.La cuenca es una extensión de terreno en un valle, escurren aguas formando un río atravesando valles 
	y escurriendo en el mar. Una cuenca puede tener varias estaciones hidrometeorológicas.El dato de precipitación es la lluvia acumulada entre las 
	7:00 horas del día anterior y las 7:00 horas de hoy (24 horas), cuando se considera el campo vacío, indica que no se realizaron mediciones.
	* **Para mayor información también puede ingresar a:** http://servicios.regionpiura.gob.pe/datosh""")

from PIL import Image
image = Image.open('Proyecto_Piura.jpg')
st.image(image, caption='La contaminación por el parque automotor antiguo es un problema en Lima Metropolitana', use_column_width=True)

st.sidebar.header("Entradas del usuario")
selected_year=st.sidebar.selectbox('Año', list(reversed(range(2010,2021))))
