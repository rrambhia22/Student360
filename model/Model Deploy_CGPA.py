#deploying the model for testing

import pickle
import streamlit as st

#loading in the model to predict 
pickle_in = open('Student_Classifier.pkl', 'rb')
student_classifier = pickle.load(pickle_in)
  

def prediction(tenthCgpa, percent_12, branch, gender, category, entrancetaken, seattype, rankofentrance): 

    #gender
    if gender == 'Male':
        gender = 0
    else:
        gender = 1


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


    #seat
    if seattype == 'B-CAT':
        seattype = 0
    elif seattype == 'E-CET':
        seattype = 1
    elif seattype == 'EAMCET':
        seattype = 2
    else:
        seattype = 3


    #entrance taken
    if entrancetaken == 'AP-EAMCET':
        entrancetaken = 0
    elif entrancetaken == 'B-CAT' :
        entrancetaken = 1
    elif entrancetaken == 'BOI' :
        entrancetaken = 2
    elif entrancetaken == "Didn't perform well" :
        entrancetaken = 3
    elif entrancetaken == 'E-CET' :
        entrancetaken = 4
    elif entrancetaken == 'EAMCET' :
        entrancetaken = 5
    elif entrancetaken == 'IP' :
        entrancetaken = 6
    elif entrancetaken == 'IPE' :
        entrancetaken = 7
    elif entrancetaken == 'IPE GRADE' :
        entrancetaken = 8
    elif entrancetaken == 'JEE' :
        entrancetaken = 9
    elif entrancetaken == 'JEE-2' :
        entrancetaken = 10
    elif entrancetaken == 'Management' :
        entrancetaken = 11
    elif entrancetaken == 'NDA' :
        entrancetaken = 12
    elif entrancetaken == 'NRI' :
        entrancetaken = 13
    elif entrancetaken == 'No Exam/No Rank' :
        entrancetaken = 14
    elif entrancetaken == 'No Rank' :
        entrancetaken = 15
    elif entrancetaken == 'Other' :
        entrancetaken = 16
    elif entrancetaken == 'SAT' :
        entrancetaken = 17
    elif entrancetaken == 'Sports' :
        entrancetaken = 18
    elif entrancetaken == 'Spot' :
        entrancetaken = 19
    elif entrancetaken == 'Spot Evaluation' :
        entrancetaken = 20
    elif entrancetaken == 'Spot admission' :
        entrancetaken = 21
    elif entrancetaken == 'Spot counciling' :
        entrancetaken = 22
    else:
        entrancetaken = 23


    tenthCgpa = float(tenthCgpa)
    percent_12 = float(percent_12)

   
    prediction = student_classifier.predict(
        [[tenthCgpa, percent_12, branch, gender, category, entrancetaken, seattype, rankofentrance]])
    return prediction



def main():
    html_temp = ""
    st.markdown(html_temp, unsafe_allow_html = True)
    tenthCgpa = st.text_input("10th CGPA")
    percent_12 = st.text_input("12th %")
    entrancetaken = st.text_input("Entrance Taken")
    rankofentrance = st.text_input("Rank of Entrance Test")
    seattype = st.text_input("Seat Type")
    branch = st.text_input("Branch")
    gender = st.text_input("Gender")
    category = st.text_input("Category")
    result =""


    if st.button("Predict"):
        result = prediction(tenthCgpa, percent_12, branch, gender, category, entrancetaken, seattype, rankofentrance)
        st.write(f"CGPA of the Student is: {result}")

        if (result<=6.5):
            st.write("Student is Not Eligible")
        else:
            st.write("Student is Eligible")



if __name__=='__main__':
    main()