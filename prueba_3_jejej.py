#$ pip install streamlit --upgrade

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import urllib.request
import base64


st.title('Contaminantes del aire en Lima Metropolitana')

st.markdown("""
	Esta app exploratoria permite visualizar los datos de contaminantes del aire en Lima Metropolitana
	* **Librerías Python:** altair, pandas, streamlit, base64
	* **Base de datos:** [Servicio Nacional de Meteorología e Hidrología del Perú - SENAMHI] (https://www.datosabiertos.gob.pe/dataset/datos-horarios-de-contanimantes-del-aire-en-lima-metropolitana-servicio-nacional-de).
	""")

from PIL import Image
image = Image.open('contaminacion.jpeg')
st.image(image, caption='La contaminación por el parque automotor antiguo es un problema en Lima Metropolitana', use_column_width=True)

st.sidebar.header("Entradas del usuario")
selected_year=st.sidebar.selectbox('Año', list(reversed(range(2010,2021))))

st.header("Dataset SENAMHI")

@st.experimental_memo
def download_data():
   url="http://server01.labs.org.pe:2005/datos_horarios_contaminacion_lima.csv"
   filename="datos_horarios_contaminacion_lima.csv"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('datos_horarios_contaminacion_lima.csv')
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

def load_data(year):
  df = download_data()
	df=df.astype({'ANO':'str'})
	df['PM 10'] = pd.to_numeric(df['PM 10'])
	df['PM 2.5'] = pd.to_numeric(df['PM 2.5'])
	df['SO2'] = pd.to_numeric(df['SO2'])
	df['NO2'] = pd.to_numeric(df['NO2'])
	df['O3'] = pd.to_numeric(df['O3'])
	df['CO'] = pd.to_numeric(df['CO'])
	grouped = df.groupby(df.ANO)
	df_year = grouped.get_group(year)
	return df_year

data_by_year=load_data(str(selected_year))


sorted_unique_district = sorted(data_by_year.ESTACION.unique())
selected_district=st.sidebar.multiselect('Distrito', sorted_unique_district, sorted_unique_district)

unique_contaminant=['PM 10', 'PM 2.5', 'SO2', 'NO2', 'O3', 'CO']
selected_contaminant=st.sidebar.multiselect('Contaminante', unique_contaminant, unique_contaminant)

df_selected=data_by_year[(data_by_year.ESTACION.isin(selected_district))]

def remove_columns(dataset, cols):
	return dataset.drop(cols, axis=1)

cols=np.setdiff1d(unique_contaminant, selected_contaminant)

st.subheader('Mostrar data de distrito(s) y contaminante(s) seleccionado(s)')
data=remove_columns(df_selected, cols)
st.write('Dimensiones: ' + str(data.shape[0]) + ' filas y ' + str(data.shape[1]) + ' columnas')
st.dataframe(data)

#st.text(str(selected_contaminant))

def filedownload(df):
	csv = df.to_csv(index=False)
	b64 = base64.b64encode(csv.encode()).decode()
	href = f'<a href="data:file/csv;base64,{b64}">Descargar archivo CSV</a> (botón derecho y guardar como ".csv")'
	return href

st.markdown(filedownload(df_selected), unsafe_allow_html=True)
	
st.header('Evaluación de distritos por contaminante')	

minYear = st.selectbox('Desde', list(range(2010,2021)))
maxYear = st.selectbox('Hasta', list(reversed(range(2010,2021))))

anios = st.button('Gráfico entre años')

if anios:
	st.header('Gráfico de Contaminantes')
	for cont in unique_contaminant:
		st.subheader(cont)
		tempYear = minYear
		years = ['YEAR']
		for d in load_data(str(2018)).ESTACION.unique():
			years.append(d)
		dataDist = pd.DataFrame(columns=years)
		while tempYear <= maxYear:
			dataYear = load_data(str(tempYear)).groupby('ESTACION')[cont].apply(list)
			row = {'YEAR' : tempYear}
			for key, value in dataYear.items():
				row[key] = np.nansum(value)/len(value)
			dataDist = dataDist.append(row, ignore_index=True)
			tempYear+=1
		data = dataDist.rename(columns = {'YEAR': 'index'}).set_index('index')
		st.line_chart(data)
		
df = download_data()		
		
lsta_conta=['PM 10', 'PM 2.5', 'SO2', 'NO2', 'O3', 'CO']
distrits_names = pd.unique(df["ESTACION"])

st.header('Evaluación de contaminates por distrito')
selec_ditrit = st.selectbox('Evaluación de contaminates por distrito', distrits_names)
st.subheader("Distrito seleccionado:")
st.subheader(str(selec_ditrit))

grouped_g2 = df.groupby(df.ESTACION)
distrito = grouped_g2.get_group(selec_ditrit)
fecha = list(distrito.iloc[0,range(2,5)])
fecha_ini = str(fecha[0])+'/'+str(int(fecha[1]))+'/'+str(int(fecha[2]))

rango = int(list(distrito.shape)[0])
index = pd.date_range(start=fecha_ini, periods=rango, freq='60T')

#df_tempo = pd.DataFrame(index ,columns= ['TIEMPO'])
cont_distrito = distrito.iloc[:,6:].set_index(index)
#series = pd.Series(, index = index) 
#series
fecha_i = index[0]
fecha_f = index[-1]

st.markdown(f"Periodo de muestreo: desde {fecha_i} hasta {fecha_f}") 
st.subheader("Data del monitoreo de contaminates del distrito seleccionado") 
st.dataframe(cont_distrito)

st.subheader("Gráficos interactivos")
st.line_chart(cont_distrito)

sel_year=st.selectbox('Evaluación de contaminantes por año', list(reversed(range(2010,2021))))
data_ano=load_data(str(sel_year))
df_sel=data_ano[data_ano['ESTACION'].isin([selec_ditrit])]

datos=df_sel.groupby(['MES']).agg({"PM 10": 'mean', "PM 2.5": 'mean', "SO2": 'mean', "NO2": 'mean', "O3": 'mean', "CO": 'mean'})
#datos.reset_index(inplace=True)
#c=alt.Chart(datos, title='DISTRITO:'+" "+' '.join(selected_district)).mark_line().encode(x='MES', y='ppm:Q')
data = datos.reset_index().melt('MES')
data.rename(columns={'variable':'contaminante', 'value':'ppm'}, inplace=True)


st.dataframe(data)

contaminantes=['PM 10', 'PM 2.5', 'SO2', 'NO2', 'O3', 'CO']
def getBaseChart():
  #base=alt.Chart(data).mark_line().encode(x='MES',y='ppm',color='contaminante').properties(width=500, height=400)
	base = (alt.Chart(data).encode(x=alt.X("MES:T",axis=alt.Axis(title="Mes")),y=alt.Y("ppm:Q", axis=alt.Axis(title="Concentración (ppm)")),).properties(width=500, height=400))
	return base

def getSelection():
	cont_select = alt.selection_multi(fields=["contaminante"], name="Contaminante")
	cont_color_condition = alt.condition(cont_select, alt.Color("contaminante:N", legend=None), alt.value("lightgrey"))
	return cont_select, cont_color_condition

def createChart():
	cont_select, cont_color_condition = getSelection()
	make_selector = (alt.Chart(data).mark_circle(size=200).encode(y=alt.Y("contaminante:N", axis=alt.Axis(title="Elija contaminante", titleFontSize=15)),color=cont_color_condition,).add_selection(cont_select))
	base = getBaseChart()
	highlight_cont = (base.mark_line(strokeWidth=2).add_selection(cont_select).encode(color=cont_color_condition)).properties(title='DISTRITO:'+" "+' '.join(selec_ditrit))
	return base, make_selector, highlight_cont, cont_select

def createTooltip(base, cont_select):
	nearest = alt.selection(type="single", nearest=True, on="mouseover", fields=["MES"], empty="none")
	selectors = (alt.Chart(data).mark_point().encode(x="MES:T",opacity=alt.value(0)).add_selection(nearest))
	points = base.mark_point(size=5, dy=-10).encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0))).transform_filter(cont_select)

	tooltip_text = base.mark_text(align="left",dx=-60,dy=-15,fontSize=15,fontWeight="bold",lineBreak = "\n",color='white').encode(text=alt.condition(nearest, alt.Text("ppm:Q", format=".2f"), alt.value(" "),),).transform_filter(cont_select)
	rules = (alt.Chart(data).mark_rule(color="white", strokeWidth=1).encode(x="MES:T",).transform_filter(nearest))
	return selectors, rules, points, tooltip_text

base, make_selector, highlight_cont, cont_select  = createChart()
selectors, rules, points, tooltip_text  = createTooltip(base, cont_select)

make_selector | alt.layer(highlight_cont, selectors, points,rules, tooltip_text)


if st.sidebar.button("¿Quiénes somos?"):
	st.header("¿Quiénes somos?")
	st.write("Somos un grupo de estudiantes de V ciclo de Ingeniería de la Universidad Peruano Cayetano Heredia (UPCH). Nos apasiona el procesamiento y visualización de datos medioambientales que puedan ayudar al público general a comprender mejor el problema de la contaminación del aire.")
	
	col1, col2, col3, col4 = st.columns(4)
	image1 = Image.open('03b4fc19-0cf9-4357-8e04-f1e8814ffb96.JPG')
	col1.header("Fergy Aliaga")
	col1.image(image1, use_column_width=True)
	grayscale = image1.convert('LA')
	col2.image(grayscale, use_column_width=True)
	image2 = Image.open('27a9a0fb-c8db-43fa-8b69-cd64f98a01df.JPG')
	col3.header("Juandiego Montero")
	col3.image(image2, use_column_width=True)
	grayscale = image2.convert('LA')
	col4.image(grayscale, use_column_width=True)
	
	col5, col6, col7, col8 = st.columns(4)
	image3 = Image.open('96b31497-069f-4fc1-8796-100ad197e809.JPG')
	col5.header("Fabiola Figueroa")
	col5.image(image3, use_column_width=True)
	grayscale = image3.convert('LA')
	col6.image(grayscale, use_column_width=True)
	image4 = Image.open('IMG_4932.jpg')
	col7.header("Belén Balta")
	col7.image(image4, use_column_width=True)
	grayscale = image4.convert('LA')
	col8.image(grayscale, use_column_width=True)
	
	col9, col10 = st.columns(2)
	image5 = Image.open('f8788697-6bbf-4282-b5a8-edb50b7b9cb3.JPG')
	col9.header("Josmer Cajahuaringa")
	col9.image(image5, use_column_width=True)
	grayscale = image5.convert('LA')
	col10.image(grayscale, use_column_width=True)
