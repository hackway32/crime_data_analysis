import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Path to the CSV file containing the most frequent crimes by area
file_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\Cleaned_Crime_Data_from_2020_to_Present.csv'

# Read the dataset
df = pd.read_csv(file_path)

# Selecting features and target variable
X = df[['Vict Age']].values.reshape(-1, 1)  # Feature: Victim Age
y = df['Crm Cd Desc'].astype('category').cat.codes  # Target: Crime type encoded as numerical

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and fitting the linear regression model
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)

# Predicting the test set results
y_pred = linear_regressor.predict(X_test)

# Evaluating the model
print(f"Linear Regression R^2 Score: {linear_regressor.score(X_test, y_test)}")

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import numpy as np

# Logistic regression for binary classification (e.g., predicting 'THEFT' vs 'NON-THEFT')
# Encoding crime type to binary categories for simplicity
df['Crime_Binary'] = df['Crm Cd Desc'].apply(lambda x: 1 if 'THEFT' in x else 0)

# Selecting features and target variable
X = df[['Vict Age', 'Vict Sex']].dropna()
X = pd.get_dummies(X, drop_first=True)  # One-hot encoding for categorical variables
y = df['Crime_Binary'].dropna()

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and fitting the logistic regression model
logistic_regressor = LogisticRegression()
logistic_regressor.fit(X_train, y_train)

# Predicting the test set results
y_pred = logistic_regressor.predict(X_test)

# Evaluating the model
print(classification_report(y_test, y_pred))

import folium
from folium.plugins import HeatMap

# Path to the CSV file containing the most frequent crimes by area
file_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\Cleaned_Crime_Data_from_2020_to_Present.csv'

# Read the dataset
df = pd.read_csv(file_path)

# Initialize the map centered around Los Angeles
map_la = folium.Map(location=[34.0522, -118.2437], zoom_start=10)

# Creating a heatmap
heat_data = [[row['LAT'], row['LON']] for index, row in df.iterrows() if not pd.isnull(row['LAT']) and not pd.isnull(row['LON'])]
HeatMap(heat_data).add_to(map_la)

# Save the map
output_map_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\EDA plots\New_Crime_Heatmap.html'
map_la.save(output_map_path)

print(f"Interactive heatmap saved to {output_map_path}")

