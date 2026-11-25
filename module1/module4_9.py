import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/tasks/search")
def search_tasks(term: str):
    term = term.strip()

    if not term:
        raise HTTPException(status_code=400, detail="Enter a search term.")

    database_path = Path(__file__).with_name("tasks.db")

    if not database_path.exists():
        raise HTTPException(status_code=404, detail="tasks.db was not found.")

    with sqlite3.connect(database_path) as connection:
        connection.row_factory = sqlite3.Row

        rows = connection.execute("""
            SELECT id, title, description, status, created_at
            FROM tasks
            WHERE description LIKE ?
            ORDER BY CASE
                WHEN description = ? THEN 0
                WHEN description LIKE ? THEN 1
                ELSE 2
            END, id
        """, (f"%{term}%", term, f"{term}%")).fetchall()

        return [dict(row) for row in rows]
