import streamlit as st

def app():
    original_title1 = '<p style= "color:Black; font-size: 20px;">Student Risk Analysis deals with analyzing the student performance based on the various external factors to determine the student dropout rate and predict the CGPA of the students.</p>'
    original_title2 = '<p style= "color:Black; font-size: 20px;">The exploration and analysis of student dataset helps to predict the possible dropouts and determine the significant factors affecting the eligibility of students to complete the course.</p>'
    st.markdown(original_title1, unsafe_allow_html=True)
    st.markdown(original_title2, unsafe_allow_html=True)
    #st.markdown("Student Risk Analysis deals with analyzing the student performance based on the various external factors to determine the student dropout rate and predict the CGPA of the students.")
