# Import the library for creating plots
import matplotlib.pyplot as plt

# Create a dictionary with 5 genes and their expression values
gene_dict = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}

# Print the original dictionary
print("Original gene expression dictionary")
print(gene_dict)

# Add the new gene MYC to the dictionary
gene_dict["MYC"] = 11.6

# Print the updated dictionary
print("Dictionary after adding MYC")
print(gene_dict)

# Prepare data for bar chart
genes = list(gene_dict.keys())
values = list(gene_dict.values())

# Create a labeled bar chart
plt.bar(genes, values)
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Value")
plt.xticks(rotation=45)
plt.tight_layout()

# Check a specific gene
gene_of_interest = "TP53"

print(f"Result for gene: {gene_of_interest}")
if gene_of_interest in gene_dict:
    print(f"Expression value: {gene_dict[gene_of_interest]}")
else:
    print("Error: This gene is not in the dataset.")

 # Calculate and print the average expression
average = sum(values) / len(values)
print(f"Average gene expression")
print(f"Average value: {average:.2f}")

# Show the plot
plt.show()