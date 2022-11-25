import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from sklearn.preprocessing import StandardScaler
import pandas_datareader as data 



import streamlit as st
from st_aggrid import AgGrid


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
    country_list=['India','Bangladesh','Pakistan','Nepal','Srilanka']
    country_selected = st.selectbox("Select a Country",country_list)
    state_selected = st.selectbox("Select a State:", city_list)
    
    treatment = ['Heart Surgery','Knee Surgery','Liver Transplant','Kidney Transplant','Other Surgeries']
    treatment_selected = st.selectbox("Select a Treatment Looking for:", treatment)
    List_hospital = ['Ganga Ram Hospital', 'LIBS', 'MAX Hospital','Medanta Hospital']
    Price = ['Rs.120000','Rs.300000','Rs.70000','Rs.120000']
    
    if(treatment_selected=='Heart Surgery'):
        lst = [['Ganga Ram Hospital', 'Rs.120000','Dr. John','100','45','55'], ['LIBS', 'Rs.300000','Dr. AS','150','100','50'],
       ['MAX Hospital', 'Rs.70000', 'Dr. FK','200','190','10'], ['Medanta Hospital', 'Rs.100000','Dr. Raun','500','250','250']]
        df_heart = pd.DataFrame(lst, columns =['Hospital Name', 'Cost', 'Doctor Name','Total Number of Beds','Occupied','Vacant'])
               
        
        AgGrid(df_heart)
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
st.header("Team Bremner")
st.subheader("Estimate your Medical Bill and Choose as per your Budget")
#countryData()
state_data()
# page = st.sidebar.selectbox('Select page',['Country data','Continent data']) 
# if(page=='Country data'):
# 	countryData()
# else:
# 	continentData()

