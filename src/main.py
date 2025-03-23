from fastapi import FastAPI
from src.autocomplete import search_names, load_names_into_db

app = FastAPI()

# Load names from results.txt into Neon PostgreSQL
load_names_into_db("data/results.txt")

@app.get("/")
async def root():
    return {"message": "Welcome to the Autocomplete API"}

@app.get("/autocomplete/")
async def get_suggestions(prefix: str = "", limit: int = 5):
    """Fetch name suggestions from the database"""
    return {"suggestions": search_names(prefix, limit)}



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
# from fastapi import FastAPI
# from src.autocomplete import Autocomplete, search_names, load_names_into_redis

# app = FastAPI(
#     title="Name Autocomplete API",
#     description="An API for name autocompletion using Redis",
#     version="1.0.0"
# )

# load_names_into_redis()

# @app.get("/")
# async def root():
#     """Welcome endpoint for the API"""
#     return {"message": "Welcome to the Autocomplete API"}

# @app.get("/autocomplete/")
# async def get_suggestions(prefix: str = "", limit: int = 5):
#     """Get name suggestions using query parameters"""
#     try:
#         suggestions = search_names(prefix.lower(), limit)
#         return {"suggestions": list(suggestions)}
#     except Exception as e:
#         return {"error": str(e)}

# @app.get("/autocomplete/{prefix}")
# async def get_suggestions_path(prefix: str, limit: int = 5):
#     """Get name suggestions using path parameters"""
#     try:
#         suggestions = search_names(prefix.lower(), limit)
#         return {"suggestions": list(suggestions)}
#     except Exception as e:
#         return {"error": str(e)}

# from fastapi import FastAPI
# from src.autocomplete import search_names, load_names_into_db

# app = FastAPI()

# # Load names into SQL database
# load_names_into_db("data/results.txt")

# @app.get("/autocomplete/")
# async def get_suggestions(prefix: str = "", limit: int = 5):
#     return {"suggestions": search_names(prefix, limit)}
