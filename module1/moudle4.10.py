import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TaskInput(BaseModel):
    title: str
    description: str
    status: str = "pending"


class TwoTasksInput(BaseModel):
    tasks: list[TaskInput]


def create_tasks_table_if_needed():
    database_path = Path(__file__).with_name("tasks.db")

    with sqlite3.connect(database_path) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL DEFAULT 'pending',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.post("/tasks")
def add_two_tasks(data: TwoTasksInput):
    if len(data.tasks) != 2:
        raise HTTPException(
            status_code=400,
            detail="Please send exactly two tasks."
        )

    database_path = Path(__file__).with_name("tasks.db")
    inserted_ids = []

    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()

        for task in data.tasks:
            cursor.execute(
                """
                INSERT INTO tasks (title, description, status)
                VALUES (?, ?, ?)
                """,
                (task.title, task.description, task.status)
            )
            inserted_ids.append(cursor.lastrowid)

        connection.commit()

    return {
        "message": "Two tasks were added.",
        "ids": inserted_ids
    }


@app.get("/tasks")
def get_tasks():
    database_path = Path(__file__).with_name("tasks.db")

    with sqlite3.connect(database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT * FROM tasks ORDER BY id"
        ).fetchall()

        return [dict(row) for row in rows]


create_tasks_table_if_needed()
