# Import the libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the transaction data as a pandas dataframe
df = pd.read_csv('transaction_data.csv')

# Convert the dataframe into a binary matrix
df = df.pivot(index='user_id', columns='item_id', values='rating').fillna(0)
df[df > 0] = 1

# Apply the Apriori algorithm to find frequent itemsets with minimum support of 0.1
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

# Generate association rules with minimum confidence of 0.5
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)

# Print the rules
print(rules)

# Make recommendations for user 1
user_id = 1
user_items = set(df.columns[df.loc[user_id] == 1])
recommendations = []
for i in range(len(rules)):
    X = set(rules['antecedents'].iloc[i])
    Y = set(rules['consequents'].iloc[i])
    if X.issubset(user_items) and Y.isdisjoint(user_items):
        recommendations.append((list(Y)[0], rules['confidence'].iloc[i]))

# Sort the recommendations by confidence
recommendations.sort(key=lambda x: x[1], reverse=True)

# Print the recommendations
print('Recommendations for user {}:'.format(user_id))
for item, confidence in recommendations:
    print('Item {}, confidence {:.2f}'.format(item, confidence))
