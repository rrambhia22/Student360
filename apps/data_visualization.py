import streamlit as st
from PIL import Image

def app():
    with st.sidebar:
        option_list = {'Analysis of Entrance Taken',
        '10th CGPA & Backlog Analysis', '12th CGPA & Backlog Analysis', 'Feature Importance', 'Eligible Count Analysis', 'Active Backlog Analysis',
        'Backlog Analysis', 'Big Data Analytics', 'CGPA Analysis', 'Global Dropout Rate', 'National Dropout Rate', 'KNN Clustering', 'OECD Average',
        'Reasons for Dropping out', 'Relationship between 12th & Backlogs', 'Average 10th CGPA for each 10th Board','Average 12th percentage for each 12th board',
        'Count of Eligible & Not Eligible Students based on Gender','Percentage Analysis (12th & BTech) based on Gender', 'High School Dropout Rate'}

        option = st.selectbox(label = "Select the visualization", options = option_list)


    if option == "Analysis of Entrance Taken":
        st.markdown("Analysis of count of Entrance Exam Taken")
        img = Image.open("Bar Graph.png")
        st.image(img)

    elif option == "10th CGPA & Backlog Analysis":
        st.markdown("Relationship between 10th grade CGPA and Total Backlogs based on Gender")
        img = Image.open("10th&Backlog.png")
        st.image(img)

    elif option == "12th CGPA & Backlog Analysis":
        st.markdown("Relationship between 12th grade CGPA and Total Backlogs based on Gender")
        img = Image.open("12th&Backlog.png")
        st.image(img)

    elif option == "Feature Importance":
        st.markdown("Feature Importance (Based on Random Forest Classifier)")
        img = Image.open("Feature Importance.png")
        st.image(img)

    elif option == "Eligible Count Analysis":
        st.markdown("Eligible Count Analysis in each branch")
        img = Image.open("EligibleCount.png")
        st.image(img)

    elif option == "Active Backlog Analysis":
        st.markdown("Active Backlog Analysis")
        img = Image.open("Active Backlog Analysis.jpeg")
        st.image(img)

    elif option == "Backlog Analysis":
        st.markdown("Backlog Analysis")
        img = Image.open("Backlog Analysis.jpeg")
        st.image(img)

    elif option == "Big Data Analytics":
        st.markdown("Big Data Analytics in Education Market Size")
        img = Image.open("Big Data Analytics.jpeg")
        st.image(img)

    elif option == "CGPA Analysis":
        st.markdown("CGPA Analysis")
        img = Image.open("CGPA Analysis.jpeg")
        st.image(img)

    elif option == "Global Dropout Rate":
        st.markdown("Global Dropout Rate")
        img = Image.open("Global Dropout Rate.jpeg")
        st.image(img)

    elif option == "National Dropout Rate":
        st.markdown("National Dropout Rate")
        img = Image.open("National Dropout Rate.jpeg")
        st.image(img)

    elif option == "KNN Clustering":
        st.markdown("KNN Clustering")
        img = Image.open("KNN Clustering.jpeg")
        st.image(img)

    elif option == "OECD Average":
        st.markdown("Organisation for Economic Co-operation and Development (OECD) Average")
        img = Image.open("OECD Average.jpeg")
        st.image(img)

    elif option == "Reasons for Dropping out":
        st.markdown("Reasons for Dropping out")
        img = Image.open("Reasons for Dropping out.jpeg")
        st.image(img)

    elif option == "Relationship between 12th & Backlogs":
        st.markdown("Relationship between 12th & Backlogs")
        img = Image.open("Relationship between 12th & Backlogs.jpeg")
        st.image(img)

    elif option =="Average 10th CGPA for each 10th Board":
        st.markdown("Average 10th CGPA for each 10th Board")
        img = Image.open("Average 10th CGPA for each 10th Board.png")
        st.image(img)

    elif option =="Average 12th percentage for each 12th board":
        st.markdown("Average 12th percentage for each 12th board")
        img = Image.open("Average 12th percentage for each 12th board.png")
        st.image(img)

    elif option =="Count of Eligible & Not Eligible Students based on Gender":
        st.markdown("Count of Eligible & Not Eligible Students based on Gender")
        img = Image.open("Count of Eligible & Not Eligible Students based on Gender.png")
        st.image(img)

    elif option =="Percentage Analysis (12th & BTech) based on Gender":
        st.markdown("Percentage Analysis (12th & BTech) based on Gender")
        img = Image.open("Percentage Analysis (12th & BTech) based on Gender.png")
        st.image(img)

    elif option =="High School Dropout Rate":
        st.markdown("High School Dropout Rate")
        img = Image.open("High School Dropout Rate.jpeg")
        st.image(img)
        
