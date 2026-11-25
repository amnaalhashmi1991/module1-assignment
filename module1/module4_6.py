import sqlite3
import random
import string
from pathlib import Path


def add_and_fill_missing_field():
    database_path = Path(__file__).with_name("tasks.db")

    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()

        # 
        columns = [row[1] for row in cursor.execute(
            "PRAGMA table_info(tasks)"
        ).fetchall()]

      
        task_ids = cursor.execute(
            "SELECT id FROM tasks"
        ).fetchall()

        for (task_id,) in task_ids:
          
            random_character = random.choice(string.ascii_letters)

           

        connection.commit()

    print("The column was added and tasks were updated.")


if __name__ == "__main__":
    add_and_fill_missing_field()
