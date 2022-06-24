#deploying the model for testing

import pickle
import streamlit as st

#loading in the model to predict 
pickle_in = open('Student_Classifier.pkl', 'rb')
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



def main():
    html_temp = ""
    st.markdown(html_temp, unsafe_allow_html = True)
    tenthCgpa = st.text_input("10th CGPA")
    percent_12 = st.text_input("12th %")
    activebacklogs = st.text_input("No. of Active Backlogs")
    passivebacklogs = st.text_input("No. of Passive Backlogs")
    gender = st.text_input("Gender")
    internship = st.text_input("Internship")
    branch = st.text_input("Branch")
    category = st.text_input("Category")
    result =""


    if st.button("Predict"):
        result = prediction(tenthCgpa, percent_12, activebacklogs, passivebacklogs, gender, internship, branch, category)
        if result == 0:
            st.success('Student is Eligible')
        else:
            st.success('Student is Not Eligible')



if __name__=='__main__':
    main()