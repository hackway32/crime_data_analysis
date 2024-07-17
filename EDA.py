import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file paths
base_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED'
file_names = [
    "Cleaned_Location Type_07-07-2024.csv",
    "Cleaned_Offender Age_07-07-2024.csv",
    "Cleaned_Offender Ethnicity_07-07-2024.csv",
    "Cleaned_Offender Race_07-07-2024.csv",
    "Cleaned_Offender Sex_07-07-2024.csv",
    "Cleaned_Offense linked to another offense_07-07-2024.csv",
    "Cleaned_Rate of Homicide Offenses by Population_07-07-2024.csv",
    "Cleaned_Type of weapon involved by offense_07-07-2024.csv",
    "Cleaned_Victim Age_07-07-2024.csv",
    "Cleaned_Victim Ethnicity_07-07-2024.csv",
    "Cleaned_Victim Race_07-07-2024.csv",
    "Cleaned_Victim Sex_07-07-2024.csv",
    "Cleaned_Victim’s relationship to the offender_07-07-2024.csv"
]

# Directory to save plots
output_dir = os.path.join(base_path, "EDA plots")
os.makedirs(output_dir, exist_ok=True)

# Load all CSV files into a dictionary of DataFrames
data_frames = {}
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    df = pd.read_csv(file_path)
    data_frames[file_name] = df

# Function to save plot
def save_plot(file_name, plot_func, *args, **kwargs):
    plot_func(*args, **kwargs)
    plt.savefig(os.path.join(output_dir, f"{file_name}.png"))
    plt.close()

# Function to plot a bar graph
def plot_bar(df, title, x_label, y_label):
    plt.figure(figsize=(12, 7))
    sns.barplot(x=x_label, y=y_label, data=df)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

# Function to plot a pie chart
def plot_pie(df, title):
    plt.figure(figsize=(12, 7))
    plt.pie(df['value'], labels=df['key'], autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.tight_layout()

# Function to clean up file names for better readability
def clean_file_name(file_name):
    name = os.path.splitext(file_name)[0]
    name = name.replace("07-07-2024", "").replace("_", " ").replace("’", "'").strip()
    return name

# Determine the optimal visualization based on the CSV file name
def determine_visualization(file_name, df):
    title = clean_file_name(file_name)
    if 'Rate' in file_name:
        save_plot(title, plot_pie, df, title)
    else:
        # Attempt to find the right columns for plotting
        if 'key' in df.columns and 'value' in df.columns:
            save_plot(title, plot_bar, df, title, 'key', 'value')
        elif 'Category' in df.columns and 'Count' in df.columns:
            save_plot(title, plot_bar, df, title, 'Category', 'Count')
        elif df.columns.size == 2:
            save_plot(title, plot_bar, df, title, df.columns[0], df.columns[1])
        else:
            print(f"Could not determine columns to plot for {file_name}")

# Display a summary of each DataFrame and generate appropriate plots
for file_name, df in data_frames.items():
    print(f"Summary of {file_name}:\n")
    print(df.info())
    print(df.describe())
    print("\n")
    
    # Determine and generate the optimal visualization
    determine_visualization(file_name, df)
