import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="Persona KB API")

DB_PATH = "personas.db"

def query_db(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/")
def root():
    """
    Welcome endpoint describing all available API routes.
    """
    return {
        "message": "Welcome to the Persona KB API!",
        "description": "This API allows you to retrieve persona descriptions from the knowledge base.",
        "endpoints": {
            "/personas_random?limit=N": "Get N random persona descriptions (default 10). Limit max 200000.",
            "/personas?limit=N": "Get N persona descriptions sequentially (ordered by ID). Limit max 200000.",
            "/personas/{id}": "Get the description of a single persona by its ID."
        },
        "examples": {
            "Random personas": "/personas_random?limit=10",
            "Sequential personas": "/personas?limit=10",
            "Single persona by ID": "/personas/42"
        }
    }


# Get N random persona descriptions
@app.get("/personas_random")
def get_personas(limit: int = Query(10, le=200000)):
    return query_db("SELECT id, description FROM personas ORDER BY RANDOM() LIMIT ?", (limit,))

# Get N persona descriptions not randomly
@app.get("/personas")
def get_personas(limit: int = Query(10, le=200000)):
    return query_db("SELECT id, description FROM personas LIMIT ?", (limit,))

# Get one persona description by ID
@app.get("/personas/{persona_id}")
def get_persona(persona_id: int):
    result = query_db("SELECT id, description FROM personas WHERE id=?", (persona_id,))
    if not result:
        return {"error": "Persona not found"}
    return result[0]
