import sqlite3
from pathlib import Path


def search_tasks(search_text):
    term = str(search_text).strip()

    if not term:
        return []

    database_path = Path(__file__).with_name("tasks.db")

    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, title, description, status, created_at
            FROM tasks
            WHERE description LIKE ?
            ORDER BY CASE
                WHEN description = ? THEN 0
                WHEN description LIKE ? THEN 1
                ELSE 2
            END, id
        """, (f"%{term}%", term, f"{term}%"))

        return cursor.fetchall()


if __name__ == "__main__":
    search_text = input("Search task descriptions:database ")
    results = search_tasks(search_text)

    if results:
        for row in results:
            print(row)
    else:
        print("No matching tasks found.")
