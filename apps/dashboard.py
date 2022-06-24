import streamlit as st
from PIL import Image

def app():
    with st.sidebar:
        option_list = {'Dashboard 1 Analysis', 'Dashboard 2 Analysis', 'Dashboard 3 Analysis', 'Dashboard 4 Analysis', 'Dashboard 5 Analysis'}

        option = st.selectbox(label = "Select the dashboard", options = option_list)

    
    if option == "Dashboard 1 Analysis":
        st.markdown("Student Risk Analysis - Dashboard 1")
        img = Image.open("D1.png")
        st.image(img)

    elif option == "Dashboard 2 Analysis":
        st.markdown("Student Risk Analysis - Dashboard 2")
        img = Image.open("D2.png")
        st.image(img)

    elif option == "Dashboard 3 Analysis":
        st.markdown("Student Risk Analysis - Dashboard 3")
        img = Image.open("D3.png")
        st.image(img)

    elif option == "Dashboard 4 Analysis":
        st.markdown("Student Risk Analysis - Dashboard 4")
        img = Image.open("D4.png")
        st.image(img)

    elif option == "Dashboard 5 Analysis":
        st.markdown("Student Risk Analysis - Dashboard 5")
        img = Image.open("D5.jpeg")
        st.image(img)