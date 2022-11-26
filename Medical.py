import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from sklearn.preprocessing import StandardScaler
import pandas_datareader as data 

import streamlit as st

from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


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




	
	

############################
# App starts here
############################
from PIL import Image
image = Image.open('medicalimage.jpg')

st.image(image, caption='Pay Right')
st.header("Team Bremner")
st.subheader("Check Price for Treatment")

#state_data()

##Beautification of APP
city_list = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai']
country_list=['India','Bangladesh','Pakistan','Nepal','Srilanka']
country_selected = st.selectbox("Select a Country",country_list)
state_selected = st.selectbox("Select a State:", city_list)
treatment = ['Heart Surgery','Knee Surgery','Liver Transplant','Kidney Transplant','Other Surgeries']
treatment_selected = st.selectbox("Select a Treatment Looking for:", treatment)

lst = [['Ganga Ram Hospital', '340 Vasant Kunj','Rs.120000','Dr. John','100','45','55'], ['LIBS', '244 Karol Bagh','Rs.300000','Dr. AS','150','100','50'],
       ['MAX Hospital', '33 South Ext','Rs.70000', 'Dr. FK','200','190','10'], ['Medanta Hospital', '44 Gurgaon Road','Rs.100000','Dr. Raun','500','250','250']]
df_heart = pd.DataFrame(lst, columns =['Hospital Name', 'Address','Cost', 'Doctor Name','Total Number of Beds','Occupied','Vacant'])

if(treatment_selected=='Heart Surgery'):

    gb = GridOptionsBuilder.from_dataframe(df_heart)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
    df_heart,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme = 'streamlit', #Add theme color to the table
    enable_enterprise_modules=True,
    height=300, 
    width='100%',
    reload_data=True
                 )
   
else:
   
    lst2 = [['George Hospital', '44 Vasant Kunj','Rs.150,000','Dr KP','1000','770','230'], ['Transplant Hospital', '33 Rk Puram','Rs.185,000','Dr SP','600','480','120'],
            ['Healthline Hospital', '552 Karolbagh','Rs.235000','Dr Thomas','500','200','300'], ['ABC Hospital', '340 Dwarka','Rs.155000','Dr XY','400','300','100']]
   
    df_else = pd.DataFrame(lst2, columns =['Hospital Name', 'Address','Cost', 'Doctor Name','Total Number of Beds','Occupied','Vacant'])  
        
    gb1 = GridOptionsBuilder.from_dataframe(df_else)
    
    gb1.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb1.configure_side_bar() #Add a sidebar
    gb1.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb1.build()

    grid_response = AgGrid(
    df_else,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme = 'streamlit', #Add theme color to the table
    enable_enterprise_modules=True,
    height=300, 
    width='100%',
    reload_data=True
                 )





if st.button('Submit Request'):
    st.write('Thank you for Submitting your Request!!')
else:
    st.write('')
