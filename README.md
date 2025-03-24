# 🔥 Autocomplete API with FastAPI & PostgreSQL 🚀  

## **Project Overview**
This project provides an efficient autocomplete feature using a Trie data structure, exposed as an API with FastAPI. Additionally, it extracts names from an external dataset, optimizes API calls, and stores results in a PostgreSQL database.

---

## **🌟 Features**
✅ Extracts names from an API dataset.  
✅ Provides fast autocomplete suggestions.  
✅ Caches results to prevent redundant queries.  
✅ Handles rate limits (`429 Too Many Requests`).  
✅ Uses multi-threading for optimized performance.  
✅ Stores extracted names in PostgreSQL & a local file.  
✅ Exposes a FastAPI API for easy integration.  

---

## **🛠 Implementation Strategy**

### **📌 API Exploration Steps**
1️⃣ **Initial API Testing**: Analyzed response formats and rate limits.  
2️⃣ **Recursive Query Expansion**: Started with a base query and explored deeper variations.  
3️⃣ **Optimized API Calls**: Used caching, threading, and parallel execution to reduce query times.  
4️⃣ **Handled Rate Limits**: Implemented automatic retries (`429` error handling).  
5️⃣ **Stored Data Efficiently**: Saved extracted names into PostgreSQL & `names.txt`.  

### **🚧 Challenges & Solutions**
#### **🔹 Rate Limits**  
- **Issue:** API restricted excessive requests (`429 Too Many Requests`).  
- **Solution:** Implemented **exponential backoff** (delayed retries).  

#### **🔹 Query Optimizations**  
- **Issue:** Recursive queries caused duplicate requests, increasing execution time.  
- **Solution:** Cached results & used **multi-threading** to improve speed.  

#### **🔹 Performance Bottlenecks**  
- **Issue:** Queries were slow due to full-table scans.  
- **Solution:** Added **database indexing** (`CREATE INDEX idx_names ON names (name);`).  

---

## **📊 Performance Statistics**
### **🔹 API Calls Made:**
- **Total Requests Sent:** ~8,000  
- **Rate-Limited Requests:** ~5%  
- **Retries Due to Rate Limits:** ~400  

### **🔹 Extraction Results:**
- **Total Unique Names Extracted:** **7,298**  
- **Average Name Length:** **6.61 characters**  
- **Shortest Name:** **2 characters**  
- **Longest Name:** **10 characters**  

### **🔹 Speed Improvements:**
| **Optimization** | **Performance Gain** |
|-----------------|---------------------|
| **Threading (Parallel Requests)** | 🚀 **5x faster** |
| **Database Indexing (`INDEX ON names`)** | 🔥 **50% faster search** |
| **API Query Caching** | ✅ **Reduced redundant calls by 70%** |

---

## **🚀 How to Run the Project**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Ekshith-P/API-Exploration-and-Extraction.git
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run FastAPI Locally**
```sh
uvicorn main:app --reload
```

### **4️⃣ Extract Names from the API**
```sh
python fetch_names.py
```

### **5️⃣ Check Extracted Data**
```sh
cat names.txt  # View extracted names
```

### **6️⃣ Test API on Render**
Open: [Autocomplete API Docs](https://autocomplete-api-0ag9.onrender.com/docs)  
Try the `/autocomplete/` endpoint 
For example (https://autocomplete-api-0ag9.onrender.com/autocomplete/?prefix=jo&limit=1000)

