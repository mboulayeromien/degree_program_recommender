import streamlit as st

st.title('UB Degree Program Recommender')
st.header('DEGREE PROGRAM RECOMMENDATION SYSTEM FOR THE UNIVERSITY OF BUEA')

# Defining system constants and variables
alevel_subjects = ['ICT', 'BIOLOGY', 'GEOLOGY', 'HISTORY', 'ECONOMICS', 'GEOGRAPHY', 'MARKETING', 'DATA PROCESSING',
            'BUSINESS MATHEMATICS', 'BUSINESS MANAGEMENT', 'PHYSICS', 'MATHEMATICS AND MECHANICS', 'CHEMISTRY', 'PHILOSOPHY', 'LITERATURE IN ENGLISH',
            'RELIGIOUS STUDIES', 'PURE MATHEMATICS WITH STATISTICS','FRENCH', 'FOOD SCIENCE AND NUTRITION', 'FURTHER MATHEMATICS',
            'COMMERCE AND FINANCE', 'ENGLISH LANGUAGE', 'COMPUTER SCIENCE', 'ACCOUNTING', 'LAW', 'COMMUNICATION SKILLS', 'SECRETERIAL ADMINISTRATION',
            'ENGINEERING SCIENCE']
olevel_subjects = ['O MATHEMATICS', 'O BIOLOGY', 'O GEOLOGY', 'O HISTORY', 'O ECONOMICS', 'O GEOGRAPHY', 'O MARKETING', 'O DATA PROCESSING',
            'O BUSINESS MATHEMATICS', 'O BUSINESS MANAGEMENT', 'O PHYSICS', 'O CHEMISTRY', 'O LOGIC', 'O LITERATURE IN ENGLISH',
            'O RELIGIOUS STUDIES', 'O ADDITIONAL MATHEMATICS', 'O FRENCH', 'O FOOD SCIENCE AND NUTRITION', 'O COMMERCE AND FINANCE', 'O ENGLISH LANGUAGE',
            'O COMPUTER SCIENCE', 'O ACCOUNTING', 'O LAW', 'O COMMUNICATION SKILLS', 'O SECRETERIAL ADMINISTRATION', 'O ENGINEERING SCIENCE']
alevel_grades = ['A', 'B', 'C', 'D', 'E']
olevel_grades = ['A', 'B', 'C']

a_subjects = []
a_grades = []
o_subjects = []
o_grades = []

# Form design
with st.form("data_collection_form"):
    student_data = {}
    # Collect A Level subjects from student
    st.subheader('Advanced Level Subjects')
    no_subjects = int(st.number_input('How Many A Level Subjects Did You Pass In:'))
    if no_subjects < 2 or no_subjects > 5 or no_subjects < 0:
        st.warning('You should enter a minimum of 2 and a maximum of 5 subjects')
    else:   
        for i in range(1, no_subjects + 1):
            a_subjects = st.selectbox('Select Subject Title', options=sorted(alevel_subjects), key=range(i, 200))
            a_grades = st.radio('Select Grade', options=alevel_grades, key=range(i, 100))
            student_data.update({a_subjects:a_grades})
   
    # Collect O Level subjects from student
    st.subheader('Ordinary Level Subjects')      
    no_subjects = int(st.number_input('How Many O Level Subjects Did You Pass In:'))
    if no_subjects < 4 or no_subjects > 11 or no_subjects < 0:
        st.warning('You should enter a minimum of 4 and a maximum of 11 subjects')
    else:
        for i in range(1, no_subjects + 1):     
            o_subjects = st.selectbox('Select Subject Title', sorted(olevel_subjects), key=range(i, 12))
            o_grades = st.radio('Select Grade', olevel_grades, key=range(i, 45))
            student_data.update({o_subjects:o_grades})
    if st.checkbox('Show My Data'):
        st.write(student_data)
                        
    submit = st.form_submit_button("Submit")
    