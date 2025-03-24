import requests
import time
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix={}&limit=50"

CACHE = {}  # Cache to store previous API responses and reduce redundant requests

def fetch_suggestions(query):
    """Fetch autocomplete suggestions with caching."""
    if query in CACHE:
        return CACHE[query]

    try:
        response = requests.get(BASE_URL.format(query))
        if response.status_code == 200:
            suggestions = response.json().get("suggestions", [])
            CACHE[query] = suggestions
            return suggestions
        elif response.status_code == 429:  # Handle rate limiting
            print(f"Rate limited. Waiting... (Query: {query})")
            time.sleep(2)
            return fetch_suggestions(query)  # Retry after delay
    except Exception as e:
        print(f"Error fetching '{query}': {e}")
    return []

def extract_names_threaded(prefix, found_names, depth=3):
    """Recursively fetch names using multiple threads."""
    if depth == 0:  # Stop recursion when depth limit is reached
        return
    
    suggestions = fetch_suggestions(prefix)
    
    new_names = [name for name in suggestions if name not in found_names]
    found_names.update(new_names)

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda name: extract_names_threaded(name, found_names, depth - 1), new_names)

if __name__ == "__main__":
    found_names = set()
    extract_names_threaded("a", found_names, depth=5)  # Start search with the prefix 'a'

    # Save results to a file
    with open("names.txt", "w") as f:
        for name in sorted(found_names):
            f.write(name + "\n")

    print(f"Total names extracted: {len(found_names)}")
    print("Results saved to names.txt")
