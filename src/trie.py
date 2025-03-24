import os
import uvicorn
from fastapi import FastAPI
from src.autocomplete import search_names, load_names_into_db

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        """Return all words in the Trie starting with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        """Perform a depth-first search to find all words from the current node."""
        if node.is_end_of_word:
            results.append(prefix)

        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, results)

app = FastAPI()

# Load names into PostgreSQL if the table is empty
load_names_into_db("data/results.txt")

@app.get("/autocomplete/")
async def get_suggestions(prefix: str = "", limit: int = 5):
    """Return name suggestions based on the provided prefix."""
    return {"suggestions": search_names(prefix, limit)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting FastAPI on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
