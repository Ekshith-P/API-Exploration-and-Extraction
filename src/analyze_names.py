import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

# Step 1: Load names from results.txt
with open("results.txt", "r") as file:
    names = file.read().splitlines()

# Step 2: Remove duplicates & sort
unique_names = sorted(set(names))

# Step 3: Analyze Name Lengths
name_lengths = [len(name) for name in unique_names]
avg_length = sum(name_lengths) / len(name_lengths)
min_length = min(name_lengths)
max_length = max(name_lengths)

print(f"✅ Total Unique Names: {len(unique_names)}")
print(f"📏 Average Name Length: {avg_length:.2f}")
print(f"🔹 Shortest Name Length: {min_length}")
print(f"🔹 Longest Name Length: {max_length}")

# Step 4: Find Most Common Prefixes (First 2 Letters)
prefixes = [name[:2] for name in unique_names if len(name) > 1]
prefix_counts = Counter(prefixes)

print("\n🔝 Top 10 Most Common Prefixes:")
for prefix, count in prefix_counts.most_common(10):
    print(f"{prefix}: {count} names")

# Step 5: Plot Histogram of Name Lengths
plt.figure(figsize=(8, 5))
plt.hist(name_lengths, bins=20, edgecolor="black", alpha=0.75)
plt.xlabel("Name Length")
plt.ylabel("Frequency")
plt.title("Distribution of Name Lengths")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Step 6: Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(unique_names))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Extracted Names")
plt.show()
