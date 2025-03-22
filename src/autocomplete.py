class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.names = []  # Store names for quick lookup

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, name):
        node = self.root
        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.names.append(name)  # Store names at each node for quick lookup
        node.is_end_of_word = True

    def search(self, prefix, top_n=5):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No suggestions if prefix not found
            node = node.children[char]
        return sorted(set(node.names))[:top_n]  # Return top suggestions

# Load names from file
with open("results.txt", "r") as file:
    extracted_names = [line.strip().lower() for line in file if line.strip()]

# Initialize Trie and insert names
trie = Trie()
for name in extracted_names:
    trie.insert(name.lower())

# Test Autocomplete
prefix = input("Enter a prefix: ").strip().lower()
suggestions = trie.search(prefix)
print(f"Suggestions for '{prefix}': {suggestions}")

import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Test Connection
try:
    r.ping()
    print("✅ Successfully connected to Redis!")
except redis.ConnectionError:
    print("❌ Redis connection failed. Make sure Redis is running.")
def load_names_into_redis(file_path):
    with open(file_path, "r") as file:
        for name in file:
            name = name.strip().lower()  # Normalize names
            r.sadd("names", name)  # Store names in a Redis Set

# Run this once to load the names
load_names_into_redis("results.txt")
print("✅ Names loaded into Redis!")

def search_names(prefix, limit=10):
    all_names = r.smembers("names")  # Fetch all names
    matches = [name for name in all_names if name.startswith(prefix)][:limit]  # Filter by prefix
    return matches

