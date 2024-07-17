import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the CSV file containing the most frequent crimes by area
file_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\Most_Frequent_Crimes_by_Area.csv'

# Read the dataset
df = pd.read_csv(file_path)

# Pivot the data for stacked bar plot
pivot_df = df.pivot(index='AREA NAME', columns='Crm Cd Desc', values='Count').fillna(0)

# Set the plot size
plt.figure(figsize=(14, 8))

# Create a stacked bar plot
pivot_df.plot(kind='bar', stacked=True, colormap='tab20', figsize=(14, 8))

# Set the title and labels
plt.title('Most Frequent Crimes by Area')
plt.xlabel('Area Name')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate area names for better readability
plt.legend(title='Crime Description', bbox_to_anchor=(1.05, 1), loc='upper left')

# Save the plot to a file
output_plot_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\EDA plots\Most_Frequent_Crimes_by_Area_Stacked.png'
plt.tight_layout()
plt.savefig(output_plot_path)
print(f"Stacked bar plot saved to {output_plot_path}")

# Set the plot size
plt.figure(figsize=(14, 8))

# Create a heatmap
sns.heatmap(pivot_df, annot=True, fmt='g', cmap='viridis')

# Set the title and labels
plt.title('Heatmap of Most Frequent Crimes by Area')
plt.xlabel('Crime Description')
plt.ylabel('Area Name')

# Save the plot to a file
output_plot_path = r'C:\Users\kirk\Desktop\CAPSTONE\CLEANED\EDA plots\Most_Frequent_Crimes_by_Area_Heatmap.png'
plt.tight_layout()
plt.savefig(output_plot_path)
print(f"Heatmap saved to {output_plot_path}")

# Show the plot
plt.show()

