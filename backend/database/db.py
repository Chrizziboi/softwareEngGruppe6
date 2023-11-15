import os.path
import sqlite3

from flask import Flask, render_template, g


def db_startup():
    abs_path_db = os.path.dirname('chinook.db')
    db_file_path = os.path.join(abs_path_db, 'chinook.db')

    conn = sqlite3.connect(db_file_path)

    abs_path_script = os.path.dirname('schema.sql')
    script_file_path = os.path.join(abs_path_script, 'schema.sql')

    cur = conn.cursor()
    cur.execute("SELECT * FROM peristorage")
    #table_exists = cur.fetchone()

    with open(script_file_path) as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('chinook.db', check_same_thread=False)
    return g.db

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

'''def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect('chinook.db', check_same_thread=False)
    return db'''


def list_items():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return render_template("EXAMPLE")
