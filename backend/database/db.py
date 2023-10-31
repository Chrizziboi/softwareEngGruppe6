import os.path
import sqlite3


def db_startup():
    abs_path_db = os.path.dirname('chinook.db')
    db_file_path = os.path.join(abs_path_db, 'chinook.db')

    conn = sqlite3.connect(db_file_path)

    abs_path_script = os.path.dirname('schema.sql')
    script_file_path = os.path.join(abs_path_script, 'schema.sql')

    with open(script_file_path) as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    cur.execute("INSERT INTO peristorage (title, content) VALUES (?, ?)",
                ('PERSISTENT1', 'STORAGE1')
                )

    cur.execute("INSERT INTO peristorage (title, content) VALUES (?, ?)",
                ('PERSISTENT2', 'STORAGE2')
                )

    conn.commit()
    conn.close()

