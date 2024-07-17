import pandas as pd
import numpy as np

# Function to clean each chunk of the data
def clean_data(df):
    # Convert columns to appropriate data types
    df['Date Rptd'] = pd.to_datetime(df['Date Rptd'], errors='coerce')
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], errors='coerce')
    df['TIME OCC'] = pd.to_numeric(df['TIME OCC'], errors='coerce')
    df['Vict Age'] = pd.to_numeric(df['Vict Age'], errors='coerce')
    df['LAT'] = pd.to_numeric(df['LAT'], errors='coerce')
    df['LON'] = pd.to_numeric(df['LON'], errors='coerce')
    
    # Fill missing values with a placeholder or appropriate values
    df.fillna({
        'TIME OCC': -1,  # Indicate unknown time
        'Vict Age': -1,  # Indicate unknown age
        'Vict Sex': 'Unknown',
        'Vict Descent': 'Unknown',
        'LAT': 0.0,
        'LON': 0.0
    }, inplace=True)
    
    # Remove rows with all NaN values
    df.dropna(how='all', inplace=True)
    
    return df

# Path to the large CSV file
file_path = r'C:\Users\kirk\Desktop\CAPSTONE\Crime_Data_from_2020_to_Present_20240710.csv'

# Initialize an empty DataFrame to concatenate the cleaned chunks
cleaned_data = pd.DataFrame()

# Read and clean the CSV file in chunks
chunksize = 10000
for chunk in pd.read_csv(file_path, chunksize=chunksize):
    cleaned_chunk = clean_data(chunk)
    cleaned_data = pd.concat([cleaned_data, cleaned_chunk], ignore_index=True)

# Save the cleaned data to a new CSV file
cleaned_file_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\Cleaned_Crime_Data_from_2020_to_Present.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
