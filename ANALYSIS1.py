import pandas as pd

# Path to the cleaned CSV file
file_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\Cleaned_Crime_Data_from_2020_to_Present.csv'

# Read the cleaned dataset
df = pd.read_csv(file_path)

# Group the data by 'AREA NAME' and 'Crm Cd Desc' and count the occurrences
crime_counts = df.groupby(['AREA NAME', 'Crm Cd Desc']).size().reset_index(name='Count')

# Find the most frequent crime in each area
most_frequent_crimes = crime_counts.loc[crime_counts.groupby('AREA NAME')['Count'].idxmax()]

# Sort the results by area name for better readability
most_frequent_crimes = most_frequent_crimes.sort_values(by='AREA NAME')

# Display the results
print(most_frequent_crimes)

# Optionally, save the results to a CSV file
output_file_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\Most_Frequent_Crimes_by_Area.csv'
most_frequent_crimes.to_csv(output_file_path, index=False)

print(f"Results saved to {output_file_path}")
