import os
import redis
from pathlib import Path

# Redis Cloud connection details
REDIS_HOST = "redis-16337.crce179.ap-south-1-1.ec2.redns.redis-cloud.com"
REDIS_PORT = 16337
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')  # Get this from environment variables

try:
    r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        decode_responses=True,
        ssl=True  # Required for Redis Cloud
    )
    r.ping()
    print("Successfully connected to Redis!")
except Exception as e:
    print(f"Redis connection failed: {str(e)}")
    r = None

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

def load_names_into_redis(file_path):
    project_root = Path(__file__).parent.parent
    full_path = project_root / "data" / file_path
    
    with open(full_path, "r") as file:
        for name in file:
            name = name.strip().lower()
            r.sadd("names", name)

def search_names(prefix, limit=10):
    if r is None:
        return {"error": "Redis connection not available"}
    try:
        all_names = r.smembers("names")
        matches = [name for name in all_names if name.startswith(prefix.lower())][:limit]
        return matches
    except Exception as e:
        return {"error": str(e)}