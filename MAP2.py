import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('Cleaned_Crime_Data_from_2020_to_Present.csv')

# Ensure the demographic columns are in the correct format
df['Vict Age'] = pd.to_numeric(df['Vict Age'], errors='coerce')
df['Vict Sex'] = df['Vict Sex'].astype('category')
df['Vict Descent'] = df['Vict Descent'].astype('category')

# Clean the data
# Remove negative ages and ages that are likely outliers (e.g., > 120)
df = df[(df['Vict Age'] >= 0) & (df['Vict Age'] <= 120)]

# Summary statistics
print(df[['Vict Age', 'Vict Sex', 'Vict Descent']].describe())

# Bar plot for crime counts by gender
plt.figure(figsize=(10, 6))
sns.countplot(x='Vict Sex', data=df, order=df['Vict Sex'].value_counts().index)
plt.title('Crime Counts by Gender')
plt.show()

# Bar plot for crime counts by descent
plt.figure(figsize=(10, 6))
sns.countplot(x='Vict Descent', data=df, order=df['Vict Descent'].value_counts().index)
plt.title('Crime Counts by Descent')
plt.show()

# Histogram for age distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Vict Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution of Crime Victims')
plt.show()

# Chi-square test for independence between gender and crime type
contingency_table = pd.crosstab(df['Vict Sex'], df['Crm Cd Desc'])
chi2, p, dof, ex = chi2_contingency(contingency_table)
print(f'Chi-square Test: chi2 = {chi2}, p-value = {p}')

# Interactive map using Folium
import folium
from folium.plugins import HeatMap

# Create a base map
map_la = folium.Map(location=[34.0522, -118.2437], zoom_start=10)

# Add crime data points
heat_data = [[row['LAT'], row['LON']] for index, row in df.iterrows() if pd.notnull(row['LAT']) and pd.notnull(row['LON'])]
HeatMap(heat_data).add_to(map_la)

# Save the map
map_la.save('crime_heatmap.html')
