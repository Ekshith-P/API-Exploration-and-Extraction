import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the dataset
df = pd.read_csv("cleaned_names.csv")

# Total unique names
print(f"Total unique names: {len(df)}")

# Most common starting letters
starting_letters = df["Names"].str[0]
letter_counts = Counter(starting_letters)
print("\n Top 5 Most Common Starting Letters:")
for letter, count in letter_counts.most_common(5):
    print(f"{letter}: {count} names")

# Most common two-letter prefixes
prefixes = df["Names"].str[:2]
prefix_counts = Counter(prefixes)
print("\n Top 5 Most Common Two-Letter Prefixes:")
for prefix, count in prefix_counts.most_common(5):
    print(f"{prefix}: {count} names")

# Name length distribution
name_lengths = df["Names"].str.len()

plt.figure(figsize=(10, 5))
plt.hist(name_lengths, bins=20, edgecolor="black")
plt.xlabel("Name Length")
plt.ylabel("Frequency")
plt.title("Distribution of Name Lengths")
plt.grid(True)
plt.show()