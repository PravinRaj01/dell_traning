import streamlit as st

def add_selectbox():  # This function is defined in the next section
    return st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )