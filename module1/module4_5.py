import sqlite3
import time
from pathlib import Path


def temporarily_change_and_restore_task():
    # Use the database file next to this Python script.
    database_path = Path(__file__).with_name("tasks.db")

    # Read one existing task and save its original values.
    with sqlite3.connect(database_path) as connection:
        task = connection.execute(
            "SELECT id, title, status FROM tasks ORDER BY id LIMIT 1"
        ).fetchone()

    if task is None:
        print("No tasks found. Add a task using Exercise 3 first.")
        return

    task_id, original_title, original_status = task

    # Change the task, save the change, and close the connection
    # so the database viewer can show the updated values.
    with sqlite3.connect(database_path) as connection:
        connection.execute(
            """
            UPDATE tasks
            SET title = ?, status = ?
            WHERE id = ?
            """,
            ("TEMPORARY DEMO - " + original_title, "temporary", task_id)
        )
        connection.commit()

    print("Task changed. You have 15 seconds to view it in your SQLite viewer.")

    try:
        # Pause so you can see the temporary values.
        time.sleep(15)
    finally:
        # Restore the original values, even if the script is interrupted.
        with sqlite3.connect(database_path) as connection:
            connection.execute(
                """
                UPDATE tasks
                SET title = ?, status = ?
                WHERE id = ?
                """,
                (original_title, original_status, task_id)
            )
            connection.commit()

        print("The original task values have been restored.")


if __name__ == "__main__":
    temporarily_change_and_restore_task()
