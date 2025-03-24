import requests
import time

BASE_URL = "http://35.200.185.69:8000/v1/autocomplete?query="
OUTPUT_FILE = "results.txt"

# Store all unique names
found_names = set()

# Rate limit settings
REQUESTS_PER_MINUTE = 100
DELAY = 60 / REQUESTS_PER_MINUTE

def fetch_names(query):
    """Fetch names from the API for a given query."""
    try:
        response = requests.get(BASE_URL + query)
        if response.status_code == 200:
            return response.json().get("results", [])
        if response.status_code == 429:
            print("Rate limit hit! Waiting 60 seconds...")
            time.sleep(60)
            return fetch_names(query)
        print(f"Error {response.status_code}: {response.text}")
        return []
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

def explore_queries(prefix):
    """Recursively find all names starting with the given prefix."""
    results = fetch_names(prefix)

    if not results:
        return

    for name in results:
        if name not in found_names:
            found_names.add(name)
            print(f"Found: {name}")

    # Explore further if 10 results were found (indicating more possibilities)
    if len(results) == 10:
        for char in "abcdefghijklmnopqrstuvwxyz":
            explore_queries(prefix + char)

    time.sleep(DELAY)

def save_results():
    """Save the extracted names to a file."""
    with open(OUTPUT_FILE, "w") as file:
        file.write("\n".join(sorted(found_names)))
    print(f"Results saved to {OUTPUT_FILE}")

# Start the extraction
print("Starting API exploration...")
for char in "abcdefghijklmnopqrstuvwxyz":
    explore_queries(char)

save_results()