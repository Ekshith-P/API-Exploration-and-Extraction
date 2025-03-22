import os
from pathlib import Path
import redis

REDIS_HOST = os.getenv('REDIS_HOST', 'redis-16337.crce179.ap-south-1-1.ec2.redns.redis-cloud.com')
REDIS_PORT = int(os.getenv('REDIS_PORT', 16337))
REDIS_PASSWORD = os.getenv('Bittu39', None)

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

try:
    r.ping()
    print("Successfully connected to Redis!")
except redis.ConnectionError:
    print("Redis connection failed")

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.names = []

class Autocomplete:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, name):
        node = self.root
        name = name.lower()
        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.names.append(name)
        node.is_end_of_word = True

    def search(self, prefix, top_n=5):
        prefix = prefix.lower()
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return sorted(set(node.names))[:top_n]

# Initialize Redis connection
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def load_names_into_redis(file_path):
    project_root = Path(__file__).parent.parent
    full_path = project_root / "data" / file_path
    
    with open(full_path, "r") as file:
        for name in file:
            name = name.strip().lower()
            r.sadd("names", name)

def search_names(prefix, limit=10):
    all_names = r.smembers("names")
    matches = [name for name in all_names if name.startswith(prefix)][:limit]
    return matches

# Remove or comment out the test code
# with open(PROJECT_ROOT / "data" / "results.txt", "r") as file:
#     extracted_names = [line.strip().lower() for line in file if line.strip()]
# trie = Trie()  # This was causing the error
# for name in extracted_names:
#     trie.insert(name.lower())