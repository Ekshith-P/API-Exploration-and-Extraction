import pandas as pd

# Step 1: Load extracted names
with open("results.txt", "r") as file:
    names = file.read().splitlines()

# Step 2: Remove duplicates
unique_names = sorted(set(names))

# Step 3: Filter out names shorter than 2 characters (optional)
cleaned_names = [name for name in unique_names if len(name) > 1]

# Step 4: Save as CSV
df = pd.DataFrame(cleaned_names, columns=["Names"])
df.to_csv("cleaned_names.csv", index=False)

print(f"✅ Cleaned data saved to cleaned_names.csv with {len(cleaned_names)} unique names.")
