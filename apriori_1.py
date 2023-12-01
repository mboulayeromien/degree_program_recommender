import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

# Load the movie ratings dataset
data = pd.read_csv('movie_ratings.csv')

# Convert ratings into binary values (1 for liked and 0 for disliked)
data['liked'] = data['rating'] >= 3

# Convert the dataset into a transaction list
transactions = []
for user in data['user'].unique():
    transactions.append(data[data['user'] == user]['movie'].tolist())

# Generate frequent itemsets
frequent_itemsets = apriori(transactions, min_support=0.01, use_colnames=True)

# Generate association rules
association_rules = association_rules(frequent_itemsets, metric="confidence", min_confidence=0.5)

# Convert association rules into a dataframe
association_rules_df = association_rules.sort_values('confidence', ascending=False)

# Function to recommend movies
def recommend_movies(user, movies_to_recommend):
    liked_movies = data[data['user'] == user]['movie'].tolist()
    recommendations = []
    for rule in association_rules_df:
        if rule['antecedent'].issubset(liked_movies):
            recommendations.append(rule['consequent'][0])

    recommendations = list(set(recommendations) - set(liked_movies))
    recommendations = recommendations[:movies_to_recommend]
    return recommendations

# Example usage
user = 1
movies_to_recommend = 3
recommendations = recommend_movies(user, movies_to_recommend)
print("Recommendations for user", user, ":", recommendations)
