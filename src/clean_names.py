import pandas as pd

# Load extracted names
with open("results.txt", "r") as file:
    names = file.read().splitlines()

# Remove duplicates and filter names longer than 1 character
cleaned_names = sorted({name for name in names if len(name) > 1})

# Save cleaned names to CSV
df = pd.DataFrame(cleaned_names, columns=["Names"])
df.to_csv("cleaned_names.csv", index=False)

print(f"Cleaned data saved to cleaned_names.csv with {len(cleaned_names)} unique names.")