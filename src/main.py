import os
import uvicorn
from fastapi import FastAPI
from src.autocomplete import search_names, load_names_into_db
from src.autocomplete import api_counter, api_results

app = FastAPI()

# Load names into PostgreSQL if the table is empty
load_names_into_db("data/results.txt")

@app.get("/autocomplete/")
async def get_suggestions(prefix: str = "", limit: int = 5):
    """Return name suggestions based on the provided prefix."""
    return {"suggestions": search_names(prefix, limit)}

@app.get("/metrics/")
async def get_api_metrics():
    """Endpoint to fetch API call and result metrics."""
    return {
        "No. of searches made for v1": api_counter.calls["v1"],
        "No. of searches made for v2": api_counter.calls["v2"],
        "No. of searches made for v3": api_counter.calls["v3"],
        "No. of results in v1": len(api_results.results["v1"]),
        "No. of results in v2": len(api_results.results["v2"]),
        "No. of results in v3": len(api_results.results["v3"]),
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting FastAPI on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
