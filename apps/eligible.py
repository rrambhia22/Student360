#deploying the model for testing

import pickle
import streamlit as st


pickle_in = open('Student_Classifier_EligibilityPrediction.pkl', 'rb')
student_classifier = pickle.load(pickle_in)

def prediction(tenthCgpa, percent_12, activebacklogs, passivebacklogs, gender, internship, branch, category): 

    #gender
    if gender == 'Male':
        gender = 0
    else:
        gender = 1


    #internship
    if internship == 'ADP':
        internship = 0
    elif internship == 'Advanced Auto Parts':
        internship = 1
    elif internship == 'Ematic Solutions':
        internship = 2
    elif internship == 'JPMC Intern':
        internship = 3
    elif internship == 'Morgan Stanley Intern':
        internship = 4
    else:
        internship = 5


    #branch
    if branch == 'AME' :
        branch = 0
    elif branch == 'Civil' :
        branch = 1
    elif branch == 'CSE' :
        branch = 2
    elif branch == 'ECE' :
        branch = 3
    elif branch == 'EEE' :
        branch = 4
    elif branch == 'EIE' :
        branch = 5
    elif branch == 'IT' :
        branch = 6
    else:
        branch = 7


    #category
    if category == 'BC-A':
        category = 0
    elif category == 'BC-B':
        category = 1
    elif category == 'BC-C':
        category = 2
    elif category == 'BC-D':
        category = 3
    elif category == 'BC-E':
        category = 4
    elif category == 'EBC':
        category = 7
    elif category == 'OBC':
        category = 8
    elif category == 'OC':
        category = 9
    elif category == 'SC':
        category = 10
    else:
        category = 11

    tenthCgpa = float(tenthCgpa)
    percent_12 = float(percent_12)
    activebacklogs = int(activebacklogs)
    passivebacklogs = int(passivebacklogs)

    prediction = student_classifier.predict(
        [[tenthCgpa, percent_12, activebacklogs, passivebacklogs, gender, internship, branch, category]])
    return prediction



def clear_text():
    st.session_state["tenthCgpa"] = ""
    st.session_state["percent_12"] = ""
    st.session_state["activebacklogs"] = ""
    st.session_state["passivebacklogs"] = ""
    st.session_state["gender"] = ""
    st.session_state["internship"] = ""
    st.session_state["branch"] = ""
    st.session_state["category"] = ""

    

def app():

    html_temp = '<p style= "color:Black; font-size: 20px;">Eligibility Prediction of Students</p>'
    st.markdown(html_temp, unsafe_allow_html = True)
    tenthCgpa = st.text_input("10th CGPA", key="tenthCgpa")
    percent_12 = st.text_input("12th %", key="percent_12")
    activebacklogs = st.text_input("No. of Active Backlogs", key="activebacklogs")
    passivebacklogs = st.text_input("No. of Passive Backlogs", key="passivebacklogs")
    gender = st.text_input("Gender", key="gender")
    internship = st.text_input("Internship", key="internship")
    branch = st.text_input("Branch", key="branch")
    category = st.text_input("Category", key="category")
    result =""


    if st.button("Predict"):
        result = prediction(tenthCgpa, percent_12, activebacklogs, passivebacklogs, gender, internship, branch, category)
        if result == 0:
            st.success('Student is Eligible')
        else:
            st.success('Student is Not Eligible')


    st.button("Reload", on_click=clear_text)

  
        