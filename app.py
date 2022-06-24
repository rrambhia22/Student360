import streamlit as st
from multiapp import MultiPage
from apps import home, cgpa, eligible, data_visualization, dashboard
from PIL import  Image
import numpy as np

# Create an instance of the app 
app = MultiPage()


display = Image.open('SiliconValley.png')
display = np.array(display)
st.set_page_config(page_title='Student Risk Analysis')
st.image(display, width = 500)
original_title = '<p style= "color:Black; font-size: 40px;">Student Risk Analysis</p>'
st.markdown(original_title, unsafe_allow_html=True)

hide_menu_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_menu_style, unsafe_allow_html=True)
    

# Add all your applications (pages) here
app.add_app("Home", home.app)
app.add_app("Data Visualization", data_visualization.app)
app.add_app("Tableau Dashboards", dashboard.app)
app.add_app("Eligibility Prediction", eligible.app)
app.add_app("CGPA Prediction", cgpa.app)

# The main app
app.run()