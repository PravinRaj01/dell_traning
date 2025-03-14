import streamlit as st
from utils import add_selectbox



# Save this function in a separate file, e.g., `utils.py`
# Then, you can import it in other pages like this:
# from utils import add_selectbox

add_selectbox()


st.header("Welcome to Our Application")
st.subheader("Our Mission")
st.caption("Our mission is to empower individuals through education and technology. We believe in the power of knowledge and strive to make learning accessible to everyone.")

 
st.markdown("*Streamlit* is **really** ***cool***.") 
st.markdown(''' :red[Streamlit] :orange[ is]:green[ fun] ''')
st.markdown("Here's a bouquet &mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("Success")
st.warning("Warning")
st.info("Information")
st.error("Error")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True) 