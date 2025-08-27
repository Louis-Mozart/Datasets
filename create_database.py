import json
import sqlite3
from pathlib import Path

FOLDER = Path("personas-json/results")    
DB_PATH = "personas.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS personas")    
cur.execute("""
CREATE TABLE personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT
)
""")

for json_file in FOLDER.glob("*.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    desc = data.get("description")
    if desc:  
        cur.execute("INSERT INTO personas (description) VALUES (?)", (desc,))

conn.commit()
conn.close()

print("✅ Database built successfully")
