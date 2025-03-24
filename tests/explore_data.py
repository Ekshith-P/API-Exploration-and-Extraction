import os
import uvicorn
from fastapi import FastAPI
from collections import Counter
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

def analyze_data(file_path="names.txt"):
    """Analyze extracted names from the file."""
    with open(file_path, "r") as file:
        names = [line.strip() for line in file]

    total_names = len(names)
    avg_length = sum(len(name) for name in names) / total_names
    min_length = min(len(name) for name in names)
    max_length = max(len(name) for name in names)

    prefixes = [name[:2] for name in names if len(name) > 1]
    prefix_counts = Counter(prefixes).most_common(10)

    print(f"Total Unique Names: {total_names}")
    print(f"Average Name Length: {avg_length:.2f}")
    print(f"Shortest Name Length: {min_length}")
    print(f"Longest Name Length: {max_length}")
    print("\nTop 10 Most Common Prefixes:")
    for prefix, count in prefix_counts:
        print(f"{prefix}: {count} names")

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
    analyze_data("data/results.txt")
    uvicorn.run(app, host="0.0.0.0", port=port)
