import sqlite3
from pathlib import Path


def print_rows(title, columns, rows):
    # Print the result title, column names, and rows.
    print(f"\n{title}")
    print(columns)

    if rows:
        for row in rows:
            print(row)
    else:
        print("No rows found.")


def sort_tasks_two_ways():
    # Look for tasks.db next to this Python file.
    database_path = Path(__file__).with_name("tasks.db")

    if not database_path.exists():
        print("tasks.db was not found next to this script.")
        return

    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()

        # Check that the required table exists.
        tables = cursor.execute("""
            SELECT name
            FROM sqlite_schema
            WHERE type = 'table' AND name = 'tasks'
        """).fetchone()

        if tables is None:
            print("The tasks table was not found.")
            return

        # Read the column names.
        columns = [
            row[1]
            for row in cursor.execute("PRAGMA table_info(tasks)").fetchall()
        ]

        # Make sure Exercise 6 added the required column.
        if "missing_field" not in columns:
            print("missing_field is missing. Complete Exercise 6 first.")
            return

        # Approach 1: let SQL sort the rows.
        sql_rows = cursor.execute("""
            SELECT *
            FROM tasks
            ORDER BY missing_field ASC, id ASC
        """).fetchall()

        print_rows("Approach 1: sorted by SQL", columns, sql_rows)

        # Approach 2: fetch rows, then sort them in Python.
        python_rows = cursor.execute("SELECT * FROM tasks").fetchall()
        missing_field_index = columns.index("missing_field")
        id_index = columns.index("id")

        python_rows.sort(
            key=lambda row: (
                row[missing_field_index] is None,
                row[missing_field_index] or "",
                row[id_index]
            )
        )

        print_rows("Approach 2: sorted by Python", columns, python_rows)


if __name__ == "__main__":
    sort_tasks_two_ways()
