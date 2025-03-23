import requests
import time
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix={}&limit=50"

CACHE = {}  # ✅ Store previous API responses to avoid redundant requests

def fetch_suggestions(query):
    """Fetch autocomplete suggestions with caching"""
    if query in CACHE:  # ✅ Check if we already queried this prefix
        return CACHE[query]

    try:
        response = requests.get(BASE_URL.format(query))
        if response.status_code == 200:
            suggestions = response.json().get("suggestions", [])
            CACHE[query] = suggestions  # ✅ Store result in cache
            return suggestions
        elif response.status_code == 429:
            print(f"⚠️ Rate limited. Waiting... (Query: {query})")
            time.sleep(2)  
            return fetch_suggestions(query)
    except Exception as e:
        print(f"❌ Error fetching {query}: {e}")
    return []


def extract_names_threaded(prefix, found_names, depth=3):
    """Fetch names in parallel using threads and go deeper"""
    if depth == 0:  # Stop recursion after certain depth
        return
    
    suggestions = fetch_suggestions(prefix)
    
    new_names = [name for name in suggestions if name not in found_names]
    found_names.update(new_names)  

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda name: extract_names_threaded(name, found_names, depth-1), new_names)

if __name__ == "__main__":
    found_names = set()
    extract_names_threaded("a", found_names, depth=5)  # Start with 'a'

    # ✅ Save results to a file
    with open("names.txt", "w") as f:
        for name in sorted(found_names):  # Sort for better readability
            f.write(name + "\n")

    print(f"✅ Total names extracted: {len(found_names)}")
    print("📂 Saved to names.txt!")

