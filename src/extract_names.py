import requests
import time

BASE_URL = "http://35.200.185.69:8000/v1/autocomplete?query="
OUTPUT_FILE = "results.txt"

# Store all unique names
found_names = set()

# Rate limit settings
REQUESTS_PER_MINUTE = 100
DELAY = 60 / REQUESTS_PER_MINUTE  # 1 request per second

def fetch_names(query):
    """Fetch names from the API for a given query."""
    try:
        response = requests.get(BASE_URL + query)
        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        elif response.status_code == 429:  # Rate limit exceeded
            print("Rate limit hit! Waiting 60 seconds...")
            time.sleep(60)  # Pause for 1 minute
            return fetch_names(query)  # Retry
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []
    except Exception as e:
        print(f"Request failed: {e}")
        return []

def explore_queries(query_prefix):
    """Recursively find all possible names starting with query_prefix."""
    results = fetch_names(query_prefix)

    if not results:
        return  # No results found

    for name in results:
        if name not in found_names:
            found_names.add(name)
            print(f"Found: {name}")

    # If we got 10 results, there might be more—explore further
    if len(results) == 10:
        for char in "abcdefghijklmnopqrstuvwxyz":
            explore_queries(query_prefix + char)

    # Pause to respect rate limit
    time.sleep(DELAY)

def save_results():
    """Save the extracted names to a file."""
    with open(OUTPUT_FILE, "w") as file:
        for name in sorted(found_names):
            file.write(name + "\n")
    print(f"Results saved to {OUTPUT_FILE}")

# Start the extraction
print("Starting API exploration...")
for char in "abcdefghijklmnopqrstuvwxyz":
    explore_queries(char)

# Save extracted names
save_results()
