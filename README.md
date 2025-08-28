
# Persona Knowledge Base API

This project provides a lightweight **Persona Knowledge Base (KB)** built with **FastAPI** and **SQLite**.  
It enables you to query persona descriptions stored in a local database, making it easy to retrieve and utilize them in experiments, chatbots, or other applications.


## Features
- Store all personas from a folder into a single SQLite database (`personas.db`).
- REST API to:
  - Fetch N random persona descriptions.
  - Fetch N persona descriptions in order.
  - Fetch a persona description by ID.
- Easy deployment anywhere with FastAPI + Uvicorn.

---

## Installation

Clone the repository:
```bash
git clone https://github.com/Louis-Mozart/Datasets/.git && cd Datasets
````

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows

pip install -r requirements.txt
```


## Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

By default, the server runs on `http://127.0.0.1:8000`.

---

## API Endpoints

### Root

```http
GET /
```

Returns a welcome message and available endpoints.

---

### Get Random Personas

```http
GET /personas_random?limit=10
```

Returns up to 10 random persona descriptions.
**Parameters**:

* `limit` (int, optional): number of personas (default = 10, max = 100).

---

### Get Ordered Personas

```http
GET /personas?limit=10
```

Returns the first 10 persona descriptions in order.

---

### Get Persona by ID

```http
GET /personas/{id}
```

Returns the persona with the given ID.
Example:

```http
GET /personas/5
```

---

## Usage Examples

### 1. Using Python (`requests`)

You can query the API directly from Python:

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Get 5 random personas
resp = requests.get(f"{BASE_URL}/personas_random?limit=5")
print(resp.json())

# Get first 3 personas in order
resp = requests.get(f"{BASE_URL}/personas?limit=3")
print(resp.json())

# Get persona with ID 7
resp = requests.get(f"{BASE_URL}/personas/7")
print(resp.json())
```

---

### 2. Using Browser or cURL

Fetch random personas (10 by default):

```bash
curl http://127.0.0.1:8000/personas_random
```

Fetch first 5 personas:

```bash
curl "http://127.0.0.1:8000/personas?limit=5"
```

Fetch persona with ID 2:

```bash
curl http://127.0.0.1:8000/personas/2
```



## Note on Data

The personas included in this KB are sourced from **HuggingFace datasets**.
Ensure that you check the license of the dataset you are using before deploying this API publicly.

