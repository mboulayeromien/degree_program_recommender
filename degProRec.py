import streamlit as st


st.title('UB Degree Program Recommender')
st.header('DEGREE PROGRAM RECOMMENDATION SYSTEM FOR THE UNIVERSITY OF BUEA')
subjects = ['ICT', 'BIOLOGY', 'GEOLOGY', 'HISTORY', 'ECONOMICS', 'GEOGRAPHY', 'MARKETING', 'DATA PROCESSING',
            'BUSINESS MATHEMATICS', 'BUSINESS MANAGEMENT',
            'PHYSICS', 'MATHEMATICS AND MECHANICS', 'CHEMISTRY', 'PHILOSOPHY', 'LITERATURE IN ENGLISH',
            'RELIGIOUS STUDIES', 'PURE MATHEMATICS WITH STATISTICS',
            'FRENCH', 'FOOD SCIENCE AND NUTRITION', 'FURTHER MATHEMATICS', 'PURE MATHEMATICS WITH MECHANICS',
            'COMMERCE AND FINANCE', 'ENGLISH LANGUAGE',
            'COMPUTER SCIENCE', 'ACCOUNTING', 'LAW', 'COMMUNICATION SKILLS', 'SECRETERIAL ADMINISTRATION',
            'ENGINEERING SCIENCE']
grades = ['A', 'B', 'C', 'D', 'E']

students_subjects = []
students_grades = []
with st.form("my_form"):
    submitted = st.form_submit_button("Submit")
    # for i in subjects:
    st.subheader('Advanced Level Subjects')
    no_subjects = int(st.number_input('How Many A Level Subjects Did You Pass In:'))
    for i in range(1, no_subjects + 1):
        # if st.checkbox('Add Subject', key=i):
        st.selectbox('Select Subject Title', options=sorted(subjects), key=range(i, 200))
        st.radio('Select Grade', options=grades, key=range(i, 100))

    st.subheader('Ordinary Level Subjects')
    english = st.write('ENGLISH LANGUAGE')
    english_grade = st.radio('Select Grade', ['A', 'B', 'C'], key='english')
    english = st.write('MATHEMATICS')
    maths_grade = st.radio('Select Grade', ['A', 'B', 'C'], key='english')
