import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Task 1: Extract and display Year and DALYs columns for the first 10 rows
print("Task 1: First 10 rows of Year and DALYs data")

first_10_subset = dalys_data.iloc[0:10, [2, 3]]
print(first_10_subset)

max_dalys_idx = first_10_subset['DALYs'].idxmax()
max_year_afghan = first_10_subset.loc[max_dalys_idx, 'Year']
print(f"\nYear with maximum DALYs in Afghanistan's first 10 years: {max_year_afghan}")
# Comment: For the first 10 years of data (Afghanistan's initial records), the year with the maximum DALYs is 1998

# Task 2: Extract all years with DALYs records for Zimbabwe using boolean indexing
print("\nTask 2: Zimbabwe's recorded years")

zimbabwe_mask = dalys_data['Entity'] == 'Zimbabwe'
zimbabwe_years = dalys_data.loc[zimbabwe_mask, 'Year']
print("All recorded years for Zimbabwe:", zimbabwe_years.values)

first_zim_year = zimbabwe_years.min()
last_zim_year = zimbabwe_years.max()
print(f"First recorded year for Zimbabwe: {first_zim_year}")
print(f"Last recorded year for Zimbabwe: {last_zim_year}")
# Comment: For Zimbabwe, the first recorded year of DALYs data is 1990, and the last recorded year is 2019

# Task 3: Analyze 2019 data to find countries with maximum and minimum DALYs
print("\nTask 3: 2019 DALYs country comparison")

year_2019_mask = dalys_data['Year'] == 2019
data_2019 = dalys_data.loc[year_2019_mask, ['Entity', 'DALYs']]

max_dalys_row = data_2019.loc[data_2019['DALYs'].idxmax()]
max_country = max_dalys_row['Entity']
max_dalys_val = max_dalys_row['DALYs']

min_dalys_row = data_2019.loc[data_2019['DALYs'].idxmin()]
min_country = min_dalys_row['Entity']
min_dalys_val = min_dalys_row['DALYs']

print(f"Country with maximum DALYs in 2019: {max_country}, value: {max_dalys_val:.2f}")
print(f"Country with minimum DALYs in 2019: {min_country}, value: {min_dalys_val:.2f}")
# Comment: In 2019, the country with the highest DALYs is Lesotho, and the country with the lowest DALYs is Singapore

# Task 4: Plot DALYs trend over time for the country with maximum DALYs in 2019
print("\nTask 4: Plotting DALYs trend over time")
target_country_data = dalys_data.loc[dalys_data['Entity'] == max_country, :]

plt.figure(figsize=(10, 6))
plt.plot(target_country_data['Year'], target_country_data['DALYs'], 'bo-', linewidth=1.2, markersize=5)
plt.title(f'DALYs Trend Over Time in {max_country} (1990-2019)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('DALYs (per 100,000 population)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()

plot_filename = f'{max_country}_dalys_trend.png'
plt.savefig(plot_filename)
print(f"Trend plot saved as: {plot_filename}")

# Task 5: Custom question analysis - Distribution of DALYs across all countries in 2019
print("\nTask 5: Custom analysis - 2019 DALYs distribution")

plt.figure(figsize= (10, 6))
n, bins, patches = plt.hist(data_2019['DALYs'], bins=15, edgecolor='black', alpha=0.7)
plt.title('Distribution of DALYs Across All Countries in 2019', fontsize=14)
plt.xlabel('DALYs (per 100,000 population)', fontsize=12)
plt.ylabel('Number of Countries', fontsize=12)

mean_dalys = data_2019['DALYs'].mean()
plt.axvline(mean_dalys, color='red', linestyle='--', linewidth=2, label=f'Mean DALYs: {mean_dalys:.2f}')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

dist_plot_filename = '2019_dalys_distribution.png'
plt.savefig(dist_plot_filename)
print(f"Distribution plot saved as: {dist_plot_filename}")

median_dalys = data_2019['DALYs'].median()
print(f"Mean DALYs across all countries in 2019: {mean_dalys:.2f}")
print(f"Median DALYs across all countries in 2019: {median_dalys:.2f}")