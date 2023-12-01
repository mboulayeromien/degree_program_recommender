import streamlit as st


st.title('UB Degree Program Recommender')
st.header('DEGREE PROGRAM RECOMMENDATION SYSTEM FOR THE UNIVERSITY OF BUEA')
alevel_subjects = ['ICT', 'BIOLOGY', 'GEOLOGY', 'HISTORY', 'ECONOMICS', 'GEOGRAPHY', 'MARKETING', 'DATA PROCESSING',
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
student_data = {}
olevel = ['O ENGLISH LANGUAGE', 'O MATHEMATICS', 'O BIOLOGY', 'O GEOLOGY', 'O HISTORY', 'O ECONOMICS', 'O GEOGRAPHY', 'O MARKETING', 'O DATA PROCESSING',
            'O BUSINESS MATHEMATICS', 'O BUSINESS MANAGEMENT', 'O PHYSICS', 'O CHEMISTRY', 'O LOGIC', 'O LITERATURE IN ENGLISH',
            'O RELIGIOUS STUDIES', 'O ADDITIONAL MATHEMATICS', 'O FRENCH', 'O FOOD SCIENCE AND NUTRITION', 'O COMMERCE AND FINANCE', 'O ENGLISH LANGUAGE',
            'O COMPUTER SCIENCE', 'O ACCOUNTING', 'O LAW', 'O COMMUNICATION SKILLS', 'O SECRETERIAL ADMINISTRATION', 'O ENGINEERING SCIENCE']]
with st.form("my_form"):
    st.subheader('Advanced Level Subjects')
    no_subjects = int(st.number_input('How Many A Level Subjects Did You Pass In:'))
    for i in range(1, no_subjects + 1):
                if no_subjects < 2 or no_subjects > 5 or no_subjects < 0:
                    st.warn('You should a minimum of 2 and a maximum of 5 subjects')
                else:
                    students_subjects = st.selectbox('Select Subject Title', options=sorted(subjects), key=range(i, 200))
                    students_grades = st.radio('Select Grade', options=grades, key=range(i, 100))
                    student_data.update({students_subjects:students_grades})
    st.subheader('Ordinary Level Subjects')
    
             
    no_subjects = int(st.number_input('How Many O Level Subjects Did You Pass In:'))
    for i in range(1, no_subjects + 1):
            if no_subjects < 4 or no_subjects > 11 or no_subjects < 0:
                    st.warn('You should a minimum of 4 and a maximum of 11 subjects')
            else:
                    olevel_sub = st.selectbox('Select Subject Title', olevel, key=range(i, 10))
                    olevel_grade = st.radio('Select Grade', ['A', 'B', 'C'], key=range(i, 30) )
                    student_data.update({olevel_sub:olevel_grade})
    st.form_submit_button("Submit")

   
import pandas as pd
final_subjects = subjects.extend(olevel)
# final_data = dict(final_subjects, )
df = pd.DataFrame()
student_df = pd.DataFrame(student_data.items())

if st.checkbox('Show Student Data'):
    st.write(student_df)
    
# for i in subjects:
#     if i == students_subjects:
        
