import requests
import time

BASE_URL = "https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix={}&limit=10"

def test_api(prefix):
    """Send a request and measure response time"""
    start_time = time.time()
    
    try:
        response = requests.get(BASE_URL.format(prefix))
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            data = response.json().get("suggestions", [])
            print(f"✅ Prefix: '{prefix}' → Found {len(data)} names in {elapsed_time:.2f}s")
        elif response.status_code == 429:
            print(f"⚠️ Rate limited for '{prefix}'. Waiting 2 seconds...")
            time.sleep(2)
            return test_api(prefix)  # Retry
        else:
            print(f"❌ Error {response.status_code} for '{prefix}'")
    except Exception as e:
        print(f"❌ Request failed for '{prefix}': {e}")

if __name__ == "__main__":
    prefixes = ["a", "b", "jo", "ma", "xy"]  # Test different prefixes
    for prefix in prefixes:
        test_api(prefix)
