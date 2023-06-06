import streamlit as st
import pandas as pd


url = 'https://drive.google.com/file/d/1WQ5QFkP9S1FfpAxCTxQpzWKEP5lD67uL/view?usp=drive_link'
path = 'https://drive.google.com/drive/u/0/folders/1Hd2HOFknGccrm11VSdDp5N9-ADkboWvZ'+url.split('/')[-2]
st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv(path)
st.dataframe(df)
st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa=pd.DataFrame()
mapa=mapa.dropna()
st.map(mapa.astype(int))
