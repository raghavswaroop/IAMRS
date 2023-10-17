

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load your dataset, which includes the new feature
data = pd.read_csv("your_data.csv")  # Replace with your dataset file

# Assuming your dataset has columns: "user", "item", "rating", "office", "application_count"

# Feature Engineering: You can use the "application_count" as an additional feature
# X = data[["user", "item", "office", "application_count"]]
X = data[["Applications", "Assignments", "office", "application_count"]]
y = data["rating"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training: You can use a machine learning model like Random Forest for recommendation
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model (you can use different metrics based on your problem)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Now, you can use the trained model to make recommendations
# Given a user, item, office, and application_count, you can predict a rating

# For example:
user_id = "User123"
item_id = "Item456"
office_id = "Office789"
application_count = 10  # Update with the actual application count

prediction = model.predict([[user_id, item_id, office_id, application_count]])
print(f"Predicted Rating for User {user_id}, Item {item_id}: {prediction[0]}")
