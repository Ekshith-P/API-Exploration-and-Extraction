import sys
import os

# Get the project root directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.autocomplete import fetch_names, api_counter, api_results 

API_URLS = {
    "v1": "https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix=a&limit=10",
    "v2": "https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix=b&limit=10",
    "v3": "https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix=c&limit=10"
}

for version, url in API_URLS.items():
    print(f"\nFetching names from {version}...")
    try:
        data = fetch_names(version, url)
        print(f"Fetched Data for {version}:", data)
    except Exception as e:
        print(f"⚠️ Error fetching from {version}: {e}")

with open("performance_metrics.txt", "w") as f:
    f.write(f"No. of searches made for v1: {api_counter.calls['v1']}\n")
    f.write(f"No. of searches made for v2: {api_counter.calls['v2']}\n")
    f.write(f"No. of searches made for v3: {api_counter.calls['v3']}\n")
    f.write(f"No. of results in v1: {len(api_results.results['v1'])}\n") 
    f.write(f"No. of results in v2: {len(api_results.results['v2'])}\n")
    f.write(f"No. of results in v3: {len(api_results.results['v3'])}\n")

print("\n Performance metrics saved to performance_metrics.txt")
