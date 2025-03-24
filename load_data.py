import sys
from autocomplete import load_names_into_db

# Ensure 'src' directory is added to the Python path
sys.path.append("src")

try:
    load_names_into_db("data/results.txt")
    print("Names successfully loaded into the database!")
except Exception as e:
    print(f"Error loading names into the database: {e}")
