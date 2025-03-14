import streamlit as st
import pandas as pd
import os


st.header("Exercise 2")




#to filter columns from the dataframe
df = pd.read_excel(os.path.join('utils', 'sampleData.xlsx'))


columns_to_filter = st.segmented_control('Select columns to filter out', df.columns, selection_mode = 'multi')
filtered_df = df.drop(columns=columns_to_filter)

col1, col2 = st.columns([2,1])
with col1:
    # Selectbox to choose house type with 'All' option 
    house_type = st.selectbox('Select house type', ['All'] + list(df['House Type'].unique()))

with col2:
    income = st.selectbox('Select income range', ['All', 'Less than 10000', 'More than or equal to 10000'])

st.write("---")
# Filter dataframe based on selected house type
if house_type != 'All':
    filtered_df = filtered_df[filtered_df['House Type'] == house_type]

# Filter by income: all, less than 10000, more than 10000
if income == 'Less than 10000':
    filtered_df = filtered_df[filtered_df['Income'] < 10000]
elif income == 'More than or equal 10000':
    filtered_df = filtered_df[filtered_df['Income'] >= 10000]

# Display the filtered dataframe
st.dataframe(filtered_df)
