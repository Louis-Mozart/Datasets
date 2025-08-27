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
    return {"message": "Welcome to Persona KB. Try /personas or /personas/{id}"}

# Get N random persona descriptions
@app.get("/personas_random")
def get_personas(limit: int = Query(10, le=100)):
    return query_db("SELECT id, description FROM personas ORDER BY RANDOM() LIMIT ?", (limit,))

# Get N persona descriptions not randomly
@app.get("/personas")
def get_personas(limit: int = Query(10, le=100)):
    return query_db("SELECT id, description FROM personas ORDER BY LIMIT ?", (limit,))

# Get one persona description by ID
@app.get("/personas/{persona_id}")
def get_persona(persona_id: int):
    result = query_db("SELECT id, description FROM personas WHERE id=?", (persona_id,))
    if not result:
        return {"error": "Persona not found"}
    return result[0]
