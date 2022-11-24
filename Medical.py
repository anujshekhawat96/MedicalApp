import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from sklearn.preprocessing import StandardScaler
import pandas_datareader as data 



import streamlit as st



import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


import requests
import json

import pandas as pd 
from PIL import Image
#image = Image.open('sunrise.jpg')

#st.image(image, caption='Sunrise by the mountains')

def state_data():
    city_list = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai']
    state_selected = st.selectbox("Select a State:", city_list)
    treatment = ['Heart Surgery','Knee Surgery','Liver Transplant','Kidney Transplant','Other Surgeries']
    treatment_selected = st.selectbox("Select a Treatment Looking for:", treatment)
    List_hospital = ['Ganga Ram Hospital', 'LIBS', 'MAX Hospital','Medanta Hospital']
    Price = ['Rs.120000','Rs.300000','Rs.70000','Rs.120000']
    
    if(treatment_selected=='Heart Surgery'):
        lst = [['Ganga Ram Hospital', 'Rs.120000','Dr. John'], ['LIBS', 'Rs.300000','Dr. AS'],
       ['MAX Hospital', 'Rs.70000', 'Dr. FK'], ['Medanta Hospital', 'Rs.100000','Dr. Raun']]
        df_heart = pd.DataFrame(lst, columns =['Hospital Name', 'Cost', 'Doctor Name'])
               
        st.dataframe(df_heart)
    else:
        lst = [['Ortho', 'Rs.75000'], ['Dr Ortho', 'Rs.85000'],
            ['MAX Hospital', 'Rs.35000'], ['ABC Hospital', 'Rs.55000']]
        df_else = pd.DataFrame(lst, columns =['Hospital Name', 'Cost'])   
        st.dataframe(df_else)  

def countryData():
    # Countries
	clist = df['country'].unique()

	country = st.selectbox("Select a country:", clist)

	col1, col2 = st.columns(2)

	fig = px.line(df[df['country'] == country],
		x="year", y="gdpPercap", title="GDP per Capita")
	col1.plotly_chart(fig, use_container_width=True)

	fig = px.line(df[df['country'] == country],
		x="year", y="pop", title="Population Growth")
	col2.plotly_chart(fig, use_container_width=True)



	
	

############################
# App starts here
############################
st.header("Estimate your Medical Bill and Choose as per your Budget")
#countryData()
state_data()
# page = st.sidebar.selectbox('Select page',['Country data','Continent data']) 
# if(page=='Country data'):
# 	countryData()
# else:
# 	continentData()

