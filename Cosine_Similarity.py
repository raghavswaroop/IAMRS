
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("Dataset\csim.csv") 

# Sample data (you should replace this with your actual data)
# data = {
#     'UserID': [1, 1, 2, 2, 3, 3],
#     'AccessRightID': [101, 102, 101, 103, 102, 104],
# }

#print(data)

df = pd.DataFrame(data)

# # Create a user-item matrix
user_item_matrix = pd.crosstab(df['UserID'], df['AccessRightID'])
print (user_item_matrix)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# user_vector2 = user_item_matrix.loc['P852706'].values.reshape(1, -1)

# print(user_vector2)

#Function to recommend access rights for a user
def recommend_access_rights(user_id, user_item_matrix, user_similarity):
    user_id = str(user_id)  # Ensure user_id is treated as a string
    user_position = np.where(user_item_matrix.index == user_id)[0][0]  # Find the position of the user in the user-item matrix
    sim_scores = user_similarity[user_position]  # Use the user's position as an index
    weighted_access_rights = (user_item_matrix.T.values * sim_scores).T
    recommended_access_rights = weighted_access_rights.sum(axis=0)
    recommended_access_rights = recommended_access_rights * (user_item_matrix.loc[user_id] == 0)
    recommended_access_rights = recommended_access_rights.sort_values(ascending=False)
    return recommended_access_rights

# Example: Recommend access rights for 'userA' (an alphanumeric user ID)
recommended_access_rights = recommend_access_rights('P811141', user_item_matrix, user_similarity)
print(recommended_access_rights)



