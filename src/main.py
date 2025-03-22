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
from src.autocomplete import Autocomplete

app = FastAPI()
trie = Autocomplete()

# Update path to match your actual file
with open("data/results.txt", "r") as file:
    for name in file:
        trie.insert(name.strip())

@app.get("/autocomplete/")
def get_suggestions(prefix: str, limit: int = 5):
    return {"suggestions": trie.search(prefix, limit)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)