import streamlit as st

st.set_page_config(page_title="Home Page", layout="wide")

st.title("Welcome to the Cabbage Merchant's Muti-Media Page!!!") 
st.write("Please use the sidebar on the left to navigate between the pages!")

cabbage_image = ("https://static.vecteezy.com/system/resources/previews/006/562/329/non_2x/cabbage-illustration-in-cartoon-style-vector.jpg")

#Home Page Required Info
def home_page():
    st.header("Alexandria Thompson: CS 1301 - Ronnie Howard ")
    st.write('---')
    st.write("**ABOUT THE CABBAGE MERCHANT**: This page is an introduction to the cabbage merchant and his journey selling his cabbages throughout the Earth Kingdom.")
    st.write("**SELLING CABBAGES**: This page is for the Cabbage Merchant to try and spread the influence of his cabbages farther than his small cart. Please visit so that you can support his buisness and have some cabbage!")
    st.write('---')
    st.write("Please enjoy the following large image of a cabbage!")
    st.write('---')
    st.image(cabbage_image, width=800)
home_page()
