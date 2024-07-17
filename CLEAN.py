import pandas as pd
import os

# Define the file paths
base_path = r'C:\Users\kirk\Desktop\CAPSTONE'
file_names = [
    "Location Type_07-07-2024.csv",
    "Offender Age_07-07-2024.csv",
    "Offender Ethnicity_07-07-2024.csv",
    "Offender Race_07-07-2024.csv",
    "Offender Sex_07-07-2024.csv",
    "Offense linked to another offense_07-07-2024.csv",
    "Rate of Homicide Offenses by Population_07-07-2024.csv",
    "Type of weapon involved by offense_07-07-2024.csv",
    "Victim Age_07-07-2024.csv",
    "Victim Ethnicity_07-07-2024.csv",
    "Victim Race_07-07-2024.csv",
    "Victim Sex_07-07-2024.csv",
    "Victim’s relationship to the offender_07-07-2024.csv"
]

# Function to clean data
def clean_data(file_path, cleaned_file_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Display the initial data
    print(f"Initial DataFrame ({file_path}):\n", df.head())

    # Step 1: Handle missing values
    df_cleaned = df.dropna()  # Option 1: Remove rows with any missing values

    # Step 2: Remove duplicate rows
    df_cleaned = df_cleaned.drop_duplicates()

    # Step 3: Convert data types if necessary (e.g., to numeric)
    for col in df_cleaned.columns:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='ignore')

    # Step 4: Standardize column names
    df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('/', '_').str.replace('(', '').str.replace(')', '')

    # Step 5: Remove unwanted columns (if any)

    # Step 6: Handle outliers (example using IQR method)
    # Apply the quantile calculation only to numeric columns
    numeric_cols = df_cleaned.select_dtypes(include=['number']).columns

    Q1 = df_cleaned[numeric_cols].quantile(0.25)
    Q3 = df_cleaned[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1

    df_cleaned = df_cleaned[~((df_cleaned[numeric_cols] < (Q1 - 1.5 * IQR)) |(df_cleaned[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Display the cleaned data
    print(f"Cleaned DataFrame ({file_path}):\n", df_cleaned.head())

    # Save the cleaned data to a new file
    df_cleaned.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")

# Clean each file
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    cleaned_file_name = "Cleaned_" + file_name
    cleaned_file_path = os.path.join(base_path, cleaned_file_name)
    clean_data(file_path, cleaned_file_path)
