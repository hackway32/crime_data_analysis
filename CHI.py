import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Function to create a full list for crime severity
def generate_crime_severity_list(df_length):
    base_list = ['Low', 'Medium', 'High', 'Unknown', 'Low']
    multiplier = df_length // len(base_list)
    remainder = df_length % len(base_list)
    return base_list * multiplier + base_list[:remainder]

# Load cleaned data
base_path = r'C:\Users\kirk\Desktop\CAPSTONE'
file_name = "Location Type_07-07-2024.csv"
file_path = os.path.join(base_path, file_name)

# Ensure the file path is correct and load the data
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    df = pd.read_csv(file_path)
    
    # Generate crime severity list
    df_length = len(df)
    df['crime_severity'] = generate_crime_severity_list(df_length)

    # Create a contingency table
    contingency_table = pd.crosstab(df['key'], df['crime_severity'])

    # Perform chi-square test
    chi2, p, dof, ex = chi2_contingency(contingency_table)
    print(f"Chi-square test statistic: {chi2}")
    print(f"P-value: {p}")

    # Interpret the p-value
    if p < 0.05:
        print("Reject the null hypothesis: There is a significant association between location type and crime severity.")
    else:
        print("Fail to reject the null hypothesis: No significant association between location type and crime severity.")
    
    # Plot bar chart
    plt.figure(figsize=(12, 8))
    sns.barplot(x='key', y='value', data=df)
    plt.xticks(rotation=90)
    plt.title('Crime Count by Location Type')
    plt.xlabel('Location Type')
    plt.ylabel('Count')
    
    # Save the plot
    plot_dir = os.path.join(base_path, 'EDA plots')
    os.makedirs(plot_dir, exist_ok=True)
    plt.savefig(os.path.join(plot_dir, 'Crime_Count_by_Location_Type.png'))
    plt.show()
