import streamlit as st
import pymongo

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
    no_subjects = int(st.number_input('How Many A Level Subjects Did You Pass In:'))
    for i in range(1, no_subjects + 1):
        # if st.checkbox('Add Subject', key=i):
        st.selectbox('Select Subject Title', options=sorted(subjects), key=range(i, 200))
        st.radio('Select Grade', options=grades, key=range(i, 100))


@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])


client = init_connection()


# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache_data
    return items


items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")
