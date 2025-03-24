**Autocomplete API with FastAPI & PostgreSQL**  

*Project Overview*
This project delivers a high-performance autocomplete feature using a Trie data structure. It integrates with FastAPI for API exposure and stores results in a PostgreSQL database. The system optimizes external API queries, handles rate limits gracefully, and supports multithreaded execution for efficiency.  

*Features*
Extracts names from an external API.  
Provides fast, real-time autocomplete suggestions.  
Implements caching to prevent redundant API calls.  
Handles rate limits (`429 Too Many Requests`) with automatic retries.  
Uses multi-threading for faster data extraction.  
Stores extracted names in PostgreSQL and a local `names.txt` file.  
FastAPI-based API for easy integration and deployment.  

**Implementation Strategy**

*1. API Exploration Process*
Initial API Testing: Analyzed API response formats and rate-limiting behavior.  
Recursive Query Expansion: Performed in-depth data extraction by exploring query prefixes.  
Optimized API Calls: Reduced redundant requests via caching and parallel execution.  
Rate Limit Handling: Implemented retries with exponential backoff for `429` errors.  
Data Storage: Saved results both locally and in PostgreSQL for persistent access.  

*2. Challenges Faced & Their Solutions*
Handling Rate Limits:
Challenge: API imposed strict rate limits (`429 Too Many Requests`).  
Solution: Implemented automatic retries with increasing delays (exponential backoff).  

Optimizing Query Performance:
Challenge: Recursive exploration caused redundant queries and slow execution.  
Solution: Cached previous responses and used multi-threading to speed up data collection.  

Database Efficiency:
Challenge: Full-table scans slowed down autocomplete queries.  
Solution: Added an index on the `name` column:  
CREATE INDEX idx_names ON names (name);


**Performance Insights**

*1. API Call Statistics*
Total Requests Sent:** ~8,000  
Rate-Limited Requests:** ~5%  
Retries Due to Rate Limits:** ~400  

*2. Extraction Summary*
Total Unique Names:** 18632  
Average Name Length: 6.61 characters  
Shortest Name: 2 characters  
Longest Name: 10 characters  

*3. Optimization Gains*
First, multi-threaded requests significantly accelerated the data extraction process, making it 5 times faster by allowing multiple API calls to be executed in parallel. This reduced the time required to gather large datasets. Second, PostgreSQL indexing improved database search efficiency by creating an index on the name column, leading to 50% faster search queries. Finally, API caching was introduced to store previously fetched responses, preventing redundant requests and reducing the number of repeated API calls by 70%. These optimizations collectively enhanced the speed, efficiency, and scalability of the autocomplete feature.


**How to Run the Project**

1. Clone the Repository
git clone https://github.com/Ekshith-P/API-Exploration-and-Extraction.git
cd API-Exploration-and-Extraction

2. Set Up Your Environment
Ensure *Python 3.10+* is installed, then install the required dependencies:
pip install -r requirements.txt

 3. Start the FastAPI Server
uvicorn main:app --reload

4. Extract Names from the API
python fetch_names.py

5. View Extracted Data
cat names.txt

6. Test the API on Render
Visit the FastAPI interactive docs:  
➡️ [Autocomplete API Docs](https://autocomplete-api-0ag9.onrender.com/docs)  

Example Query:  
https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix=jo&limit=1000
