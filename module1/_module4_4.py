import sqlite3
from pathlib import Path


def view_database_tables():
    # Find tasks.db in the same folder as this Python file.
    database_path = Path(__file__).with_name("tasks.db")

    # Stop with a helpful message if the database file is missing.
    if not database_path.exists():
        print("tasks.db was not found. Run your Module 4 Exercise 2 first.")
        return

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        # List the user-created tables in this database.
        tables = cursor.execute("""
            SELECT name
            FROM sqlite_schema
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
            ORDER BY name
        """).fetchall()

        if not tables:
            print("There are no tables in this database.")
            return

        print("Tables in the database:")
        for (table_name,) in tables:
            print("-", table_name)

        # Show the column names and rows in the tasks table.
        if any(table_name == "tasks" for (table_name,) in tables):
            cursor.execute("SELECT * FROM tasks ORDER BY id")
            rows = cursor.fetchall()
            column_names = [column[0] for column in cursor.description]

            print("\nColumns:", column_names)

            if rows:
                print("Rows:")
                for row in rows:
                    print(row)
            else:
                print("The tasks table is empty. Add tasks in Exercise 3.")

    finally:
        connection.close()


if __name__ == "__main__":
    view_database_tables()
