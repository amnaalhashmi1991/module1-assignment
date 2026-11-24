import sqlite3


def create_tasks_table():
    # Open or create the database file.
    connection = sqlite3.connect("tasks.db")

    # Create the tasks table if it does not already exist.
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Save the table, then check and print its column names.
    connection.commit()
    columns = connection.execute("PRAGMA table_info(tasks)").fetchall()
    print("Columns:", [column[1] for column in columns])

    # Close the database connection.
    connection.close()


if __name__ == "__main__":
    create_tasks_table()
    print("Database and tasks table are ready.")
