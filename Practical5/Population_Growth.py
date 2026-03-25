# Import library for creating plots
import matplotlib.pyplot as plt

# Population data (millions) for 2020 and 2024
pop_data = {
    "UK": {"2020": 66.7, "2024": 69.2},
    "China": {"2020": 1426, "2024": 1410},
    "Italy": {"2020": 59.4, "2024": 58.9},
    "Brazil": {"2020": 208.6, "2024": 212.0},
    "USA": {"2020": 331.6, "2024": 340.1}
}

# Calculate percentage population change for each country
growth_rates = {}
for country, data in pop_data.items():
    pop20 = data["2020"]
    pop24 = data["2024"]
    change = (pop24 - pop20) / pop20 * 100
    growth_rates[country] = change
   
# Sort growth rates in descending order (largest increase to largest decrease)
sorted_rates = sorted(growth_rates.items(), key=lambda x: x[1], reverse=True)

print("Population Changes (Descending Order)")
for country, rate in sorted_rates:
    print(f"{country}: {rate:.2f}%")

# Identify country with largest increase and largest decrease
max_inc_country = sorted_rates[0][0]
max_dec_country = sorted_rates[-1][0]

print(f"\nCountry with largest population increase: {max_inc_country}")
print(f"Country with largest population decrease: {max_dec_country}")

# Create a well-labelled bar chart
countries = list(growth_rates.keys())
rates = list(growth_rates.values())

plt.figure(figsize=(8, 4))
plt.bar(countries, rates, color='orange')
plt.title("Population Percentage Change (2020-2024)")
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()