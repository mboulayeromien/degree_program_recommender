import streamlit as st

st.title('UB Degree Program Recommender')
st.header('DEGREE PROGRAM RECOMMENDATION SYSTEM FOR THE UNIVERSITY OF BUEA')

# Defining system constants and variables
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


from mlxtend.frequent_patterns import association_rules, apriori
import pandas as pd
# from efficient_apriori import apriori

# Load the transaction data as a pandas dataframe
df = pd.read_csv('prepared_alevel_csv.csv')

# Drop unwanted Column
df = df.drop('Target', axis = 1)

# df = df.fillna(0)
# df = df.pivot(index='user_id', columns='item_id', values='rating').fillna(0)

# Convert the dataframe into a binary matrix
df = df.astype('bool')
df[df > 0] =bool(1)

# Apply the Apriori algorithm to find frequent itemsets with minimum support of 0.1
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

# Generate association rules with minimum confidence of 0.5
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)
# frequent_itemsets, rules = apriori(df, output_transaction_ids=True)

# Print the rules
# print(frequent_itemsets)

user_items = set(student_data.keys())
recommendations = {}
for i in range(len(rules)):
    X = set(rules['antecedents'].iloc[i])
    Y = set(rules['consequents'].iloc[i])
    # X = set(rules[i])
    # Y = set(rules[i])
    if X.issubset(user_items) and Y.isdisjoint(user_items):
        recommendations.update({list(Y)[0]: rules['confidence'].iloc[i]*100})
# Print the recommendations
if submit:
    st.subheader('Based on the data you submitted, I recommend you also study...')
    st.write(recommendations)
 
# Getting User feedback   
with st.form('feedback'):
    st.subheader('Give Me Feedback')
    user_satisfaction = st.radio('How satisfied on a scale of 5, are you with the recommendation?', [5, 4, 3, 2, 1])
    send = st.form_submit_button("Send")
    if send:
        pass
            # st.('Thank You!')