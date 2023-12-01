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
student_data = {}

with st.form("my_form"):
    st.subheader('Advanced Level Subjects')
    no_subjects = int(st.number_input('How Many A Level Subjects Did You Pass In:'))
    for i in range(1, no_subjects + 1):
                if no_subjects < 2 or no_subjects > 5 or no_subjects < 0:
                    st.write('You should a minimum of 2 and a maximum of 5 subjects')
                else:
                    a_subjects = st.selectbox('Select Subject Title', options=sorted(alevel_subjects), key=range(i, 200))
                    a_grades = st.radio('Select Grade', options=alevel_grades, key=range(i, 100))
                    student_data.update({a_subjects:a_grades})
    st.subheader('Ordinary Level Subjects')
    
             
    no_subjects = int(st.number_input('How Many O Level Subjects Did You Pass In:'))
    for i in range(1, no_subjects + 1):
                if no_subjects < 4 or no_subjects > 11 or no_subjects < 0:
                    st.write('You should a minimum of 4 and a maximum of 11 subjects')
                else:
                    o_subjects = st.selectbox('Select Subject Title', sorted(olevel_subjects), key=range(i, 12))
                    o_grades = st.radio('Select Grade', olevel_grades, key=range(i, 45))
                    student_data.update({o_subjects:o_grades})
                        
    st.form_submit_button("Submit")
# import pandas as pd
# df = pd.DataFrame()
# student_df = pd.DataFrame(student_data.items())

if st.checkbox('Show Student Data'):
    st.write(student_data)

st.subheader('Based on the data you submitted, I recommend this to you!')
st.write('Still Working On It...')
st.write('Kindly Take a moment to rate my services to you')

user_satisfaction = st.radio('How satisfied on a scale of 5, are you with the recommendation? '['1', '2', '3', '4','5'].reverse())

   

    
# for i in subjects:
#     if i == students_subjects:
        
