from collections import Counter

def analyze_data(file_path="names.txt"):
    """Analyze extracted names from the file"""
    with open(file_path, "r") as file:
        names = [line.strip() for line in file]

    total_names = len(names)
    avg_length = sum(len(name) for name in names) / total_names
    min_length = min(len(name) for name in names)
    max_length = max(len(name) for name in names)

    # Find most common name prefixes (first 2 letters)
    prefixes = [name[:2] for name in names if len(name) > 1]
    prefix_counts = Counter(prefixes).most_common(10)

    print(f"✅ Total Unique Names: {total_names}")
    print(f"📏 Average Name Length: {avg_length:.2f}")
    print(f"🔹 Shortest Name Length: {min_length}")
    print(f"🔹 Longest Name Length: {max_length}")
    print("\n🔝 Top 10 Most Common Prefixes:")
    for prefix, count in prefix_counts:
        print(f"{prefix}: {count} names")

if __name__ == "__main__":
    analyze_data()
