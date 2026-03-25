# Import library for creating plots
import matplotlib.pyplot as plt

# Given heart rate data
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# Calculate total number of patients and mean heart rate
total_patients = len(heart_rates)
mean_hr = sum(heart_rates) / total_patients

# Print total patients and mean heart rate
print("Heart Rate Analysis")
print(f"Total patients: {total_patients}, Mean heart rate: {mean_hr:.2f} bpm")

# Classify heart rates into three categories
low = 0
normal = 0
high = 0

for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1

# Print counts for each category
print(f"Low (<60 bpm): {low}")
print(f"Normal (60-120 bpm): {normal}")
print(f"High (>120 bpm): {high}")

# Find the largest category
category_counts = {"Low": low, "Normal": normal, "High": high}
largest_category = max(category_counts, key=category_counts.get)
print(f"The largest category is: {largest_category}")

# Create a well-labelled pie chart
plt.figure(figsize=(6, 6))
plt.pie([low, normal, high],
        labels=["Low (<60 bpm)", "Normal (60-120 bpm)", "High (>120 bpm)"],
        autopct="%1.1f%%")
plt.title("Heart Rate Category Distribution")

# Show the pie chart
plt.show()