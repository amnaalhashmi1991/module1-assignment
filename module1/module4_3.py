import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TaskInput(BaseModel):
    # Information for one task.
    title: str
    description: str
    status: str = "pending"


class TwoTasksInput(BaseModel):
    # The API expects exactly two tasks.
    tasks: list[TaskInput]


def create_tasks_table_if_needed():
    # Create the database and table if they do not exist yet.
    with sqlite3.connect("tasks.db") as connection:
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
    # Make sure the request contains exactly two tasks.
    if len(data.tasks) != 2:
        raise HTTPException(
            status_code=400,
            detail="Please send exactly two tasks."
        )

    # Save both tasks in the existing SQLite database.
    with sqlite3.connect("tasks.db") as connection:
        cursor = connection.cursor()
        inserted_ids = []

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


# Ensure the table exists before the API receives requests.
create_tasks_table_if_needed()
