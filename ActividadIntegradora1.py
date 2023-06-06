import streamlit as st
import pandas as pd

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df = pd.read_csv("./Users/HP Use/Desktop/Streamlit/Police_Department_Incident_Reports__2018_to_Present.csv", low_memory=False)
st.dataframe(df)
st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa=pd.DataFrame()
mapa=mapa.dropna()
st.map(mapa.astype(int))
