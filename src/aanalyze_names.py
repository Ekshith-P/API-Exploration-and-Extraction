import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Load cleaned names
df = pd.read_csv("cleaned_names.csv")

# Step 2: Basic statistics
total_names = len(df)
print(f"✅ Total unique names: {total_names}")

# Step 3: Find the most common starting letters
starting_letters = df["Names"].str[0]  # Get the first letter of each name
letter_counts = Counter(starting_letters)
print("\n🔹 Top 5 Most Common Starting Letters:")
for letter, count in letter_counts.most_common(5):
    print(f"{letter}: {count} names")

# Step 4: Find most common two-letter prefixes
prefixes = df["Names"].str[:2]  # Get first two letters
prefix_counts = Counter(prefixes)
print("\n🔹 Top 5 Most Common Two-Letter Prefixes:")
for prefix, count in prefix_counts.most_common(5):
    print(f"{prefix}: {count} names")

# Step 5: Name Length Distribution
df["Length"] = df["Names"].str.len()

# Plot histogram for name length distribution
plt.figure(figsize=(10, 5))
plt.hist(df["Length"], bins=20, edgecolor="black")
plt.xlabel("Name Length")
plt.ylabel("Frequency")
plt.title("Distribution of Name Lengths")
plt.grid(True)
plt.show()
