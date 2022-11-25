#$ pip install streamlit --upgrade

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import urllib.request
import base64
from PIL import Image

st.title('Datos Hidrometereológicos Gobierno Regional Piura')

st.markdown("""Esta pagina web "app" exploratoria permite visualizar a cualquier usuario los datos hidrometereológicos del Gobierno Regional de Piura""")

st.header('Nosotros el Equipo 3 pes profe Tssss!')
st.markdown("""
           Somos un exelente grupo de estudiantes que se encuentra cursando el 5to ciclo de la carrera de Ingeniería Ambiental en la Universidad 
	   Peruana Cayetano Heredia. Como proyecto final del curso “Programación Avanzada”,realizamos esta página en base a los conocimientos 
	   adquiridos en las clases teóricas y prácticas durante del ciclo, junto a la asesoría y enseñansas de nuestros profesores, Fonse <3.
	   """) 
image = Image.open('tenorio el papi.jpg')
st.image(image, caption='Futuros Ingenieros Ambientales', use_column_width=True)

st.header('Agua y saneamiento')
st.markdown("""
	Contiene los datos Hidrometeorológicos del Sistema Hidráulico Mayor a cargo del  Proyecto Especial Chira Piura.
        Este dataset muestra los datos hidrometereológicos registrados de las presas, estaciones hidrológicas e hidrométricas.
        Esta información contiene el nombre de la cuenca, nombre de la estación, medida del caudal a las 007:00 horas, el promedio del caudal a las 
	24:00 horas, el caudal máximo a las 24:00 horas, niveles de presas a las 7:00 horas, nivel máximo de las presas a las 24:00 horas, el volumen 
	de las presas a las 07:00 y precipitaciones.La cuenca es una extensión de terreno en un valle, escurren aguas formando un río atravesando valles 
	y escurriendo en el mar. Una cuenca puede tener varias estaciones hidrometeorológicas.El dato de precipitación es la lluvia acumulada entre las 
	7:00 horas del día anterior y las 7:00 horas de hoy (24 horas), cuando se considera el campo vacío, indica que no se realizaron mediciones.
	""")
st.header('Dato y Medio de Distribución')

st.markdown("""* **Datos Hidrometereológicos Gobierno Regional Piura:** https://www.datosabiertos.gob.pe/dataset/datos-hidrometereol%C3%B3gicos-gobierno-regional-piura/resource/897966b9-f582-4898-83fe""")
st.markdown("""* **Metadatos de los Datos Hidrometereológicos Gobierno Regional Piura:** https://www.datosabiertos.gob.pe/dataset/datos-hidrometereol%C3%B3gicos-gobierno-regional-piura/resource/454e8897-4e25-486e-8291""")
st.markdown("""* **Diccionario de Datos de los Datos Hidrometereológicos Gobierno Regional Piura:** https://www.datosabiertos.gob.pe/dataset/datos-hidrometereol%C3%B3gicos-gobierno-regional-piura/resource/d7437ef6-8950-4c25-bc91""")

st.markdown("""
	* **Para mayor información también puede ingresar a:** http://servicios.regionpiura.gob.pe/datosh
	""")

image = Image.open('Proyecto_Piura.jpg')
st.image(image, caption='Piura: Gobierno regional pone a disposición información hidrometeorológica del sistema hidráulico Chira - Piura', use_column_width=True)

st.header('Datos Hidrometereológicos ')

image = Image.open('crear_mapa.jpg')
st.image(image, caption='  ', use_column_width=True)




###st.sidebar.header("Entradas del usuario")
###selected_prov=st.sidebar.selectbox('Provincia', list(reversed(range(2010,2021))))




st.header("Datos Hidrometereológicos Gobierno Regional Piura")
st.markdown("""Este dataset muestra los datos hidrometereológicos registrados de las presas, estaciones hidrológicas e hidrométricas.""")
@st.experimental_memo
def download_data():
   url="https://www.datosabiertos.gob.pe/sites/default/files/DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv"
   filename="DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv')
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())


st.header('Análisis exploratorio')

# Seleccion del dataset
st.subheader('Seleccionar los datos de las diferentes proviancias de Piura')

opcion_dataset = st.selectbox(
    '¿Qué dataset de las provincias de Piura deseas visualizar?',
    ('Ayabaca', 'Huancabamba','Morropón', 'Paita', 'Piura', 'Sechura', 'Sullana', 'Talara')
    )




