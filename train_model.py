import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import NearestNeighbors
import pickle

# Load transaction data
with open('transactions.json', 'r') as f:
    transactions = json.load(f)

# Prepare data for training
data = []
for transaction in transactions:
    for item in transaction.values():
        product = item['product']
        quantity = item['quantity']
        data.append((product['name'], transaction['user'], quantity))

# Convert data to a DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=['product', 'user', 'quantity'])

# Create a pivot table
pivot_table = df.pivot_table(index='user', columns='product', values='quantity', fill_value=0)

# Split the data into training and test sets
train_data, test_data = train_test_split(pivot_table, test_size=0.2, random_state=42)

# Train the model
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(train_data)

# Evaluate the model
def get_rmse(model, test_data):
    test_users = test_data.index
    test_products = test_data.columns
    predictions = []
    actuals = []
    for user in test_users:
        distances, indices = model.kneighbors([test_data.loc[user]], n_neighbors=5)
        for idx in indices[0]:
            if idx < len(train_data):
                predictions.append(train_data.iloc[idx].mean())
                actuals.append(test_data.loc[user].mean())
    return mean_squared_error(actuals, predictions, squared=False)

rmse = get_rmse(model, test_data)
print(f"RMSE: {rmse}")

# Save the model
with open('recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)
