# from fastapi import FastAPI
# from typing import List
# from trie import Trie

# app = FastAPI()

# # Initialize Trie
# trie = Trie()

# # Load names from file
# with open("results.txt", "r") as file:
#     extracted_names = [line.strip().lower() for line in file if line.strip()]

# # Insert names into Trie
# for name in extracted_names:
#     trie.insert(name)

# @app.get("/autocomplete/{prefix}", response_model=List[str])
# def autocomplete(prefix: str):
#     """Returns a list of names that start with the given prefix."""
#     return trie.search(prefix)
from fastapi import FastAPI
from src.autocomplete import Autocomplete, search_names

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Autocomplete API"}

@app.get("/autocomplete/")
async def get_suggestions(prefix: str = "", limit: int = 5):
    try:
        suggestions = search_names(prefix.lower(), limit)
        return {"suggestions": list(suggestions)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/autocomplete/{prefix}")
async def get_suggestions_path(prefix: str, limit: int = 5):
    try:
        suggestions = search_names(prefix.lower(), limit)
        return {"suggestions": list(suggestions)}
    except Exception as e:
        return {"error": str(e)}