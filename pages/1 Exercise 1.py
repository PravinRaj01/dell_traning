import streamlit as st
import pandas as pd

def popup():
    st.markdown("---")
    #malaysian geomap will be displayed with imports
    st.map(pd.DataFrame({
        'lat': [3.1390],
        'lon': [101.6869],
        'name': ['Kuala Lumpur']
    }))
    st.markdown("---")
    df = pd.read_excel('utils/sampleData.xlsx')
    st.dataframe(df)
    chart_type = st.selectbox("Select a chart type", ['Bar Chart', 'Line Chart', 'Scatter Chart'])
    chart(chart_type)


def chart(chart_type):
    df = pd.read_excel('sampledata.xlsx')

    if chart_type == "Bar Chart":
        return st.bar_chart(df, x="Location", y="Income")
    elif chart_type == "Line Chart":
        return st.line_chart(df, x="Household", y="Income")
    elif chart_type == "Scatter Chart":
        return st.scatter_chart(df, x="Household", y="Income")
    
    

st.header("Welcome to Our Application")
answer = st.selectbox("Kuala Lumpur is located at", [' ', 'Malaysia', 'Thailand', 'UK'])
if answer == 'Malaysia':
    st.success("Correct!")
    
    popup()
elif answer == ' ':
    st.info("Choose an answer.")
else:
    st.error("Incorrect! Try again.")



