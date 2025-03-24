import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

# Class to track results for different versions
class APIResults:
    def __init__(self):
        self.results = {"v1": set(), "v2": set(), "v3": set()}

    def add_results(self, version, names):
        if version in self.results:
            self.results[version].update(names)

# Global instance to track results
api_results = APIResults()

# Function to extract names and track results
def extract_names(version, data):
    names = [item["name"] for item in data]  # Adjust based on API response
    api_results.add_results(version, names)  # Track results
    return names

# Load names from results.txt
with open("results.txt", "r") as file:
    names = file.read().splitlines()

# Remove duplicates and sort
unique_names = sorted(set(names))

# Analyze name lengths
name_lengths = [len(name) for name in unique_names]
avg_length = sum(name_lengths) / len(name_lengths)

print(f"Total Unique Names: {len(unique_names)}")
print(f"Average Name Length: {avg_length:.2f}")
print(f"Shortest Name Length: {min(name_lengths)}")
print(f"Longest Name Length: {max(name_lengths)}")

# Find the most common prefixes (first 2 letters)
prefixes = [name[:2] for name in unique_names if len(name) > 1]
prefix_counts = Counter(prefixes)

print("\nTop 10 Most Common Prefixes:")
for prefix, count in prefix_counts.most_common(10):
    print(f"{prefix}: {count} names")

# Plot histogram of name lengths
plt.figure(figsize=(8, 5))
plt.hist(name_lengths, bins=20, edgecolor="black", alpha=0.75)
plt.xlabel("Name Length")
plt.ylabel("Frequency")
plt.title("Distribution of Name Lengths")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(unique_names))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Extracted Names")
plt.show()

# Example usage of extract_names (assuming data is fetched from an API)
# data = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Alice"}]  # Example API response
# version = "v1"
# extracted_names = extract_names(version, data)
# print(f"Extracted Names for {version}: {extracted_names}")
# print(f"Tracked Results: {api_results.results}")