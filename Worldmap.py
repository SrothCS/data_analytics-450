# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Loading the datasets. 
data_file = 'country_data.csv'
df = pd.read_csv(data_file, skiprows=4)
#
# Clean the dataset and focus on the 2020 data
df_2020 = df[['Country Name', 'Country Code', '2020']].dropna() 
df_2020 = df_2020.rename(columns={'2020': 'Poverty Ratio 2020'})

# 1. Histogram: Distribution of Poverty Ratio in 2020
plt.figure(figsize=(10, 6))
sns.histplot(df_2020['Poverty Ratio 2020'], bins=20, kde=True, color='blue')
plt.title('Histogram of Poverty Ratio (2020)')
plt.xlabel('Poverty Ratio (2020)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2. Box Plot: Poverty Ratio in 2020
plt.figure(figsize=(10, 6))
sns.boxplot(df_2020['Poverty Ratio 2020'], color='green')
plt.title('Box Plot of Poverty Ratio (2020)')
plt.grid(True)
plt.show()

# 3. Density Plot: Poverty Ratio in 2020
plt.figure(figsize=(10, 6))
sns.kdeplot(df_2020['Poverty Ratio 2020'], shade=True, color='red')
plt.title('Density Plot of Poverty Ratio (2020)')
plt.grid(True)
plt.show()

# 4. Bar Plot: Count of Countries by Region (from metadata_country)
metadata_country_file = 'data.csv'
metadata_country_df = pd.read_csv(metadata_country_file)

# Merge country metadata to include regions
merged_df = pd.merge(df_2020, metadata_country_df[['Country Code', 'Region']], on='Country Code', how='left')

# Bar plot of countries by region
plt.figure(figsize=(12, 6))
sns.countplot(data=merged_df, x='Region', palette='muted')
plt.title('Bar Plot: Count of Countries by Region')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
