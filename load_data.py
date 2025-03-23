import sys
sys.path.append("src")  # Add the 'src' folder to Python's path

from autocomplete import load_names_into_db

load_names_into_db("data/results.txt")
print("Names successfully loaded into the database!")
