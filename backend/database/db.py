import os.path
import sqlite3

from flask import Flask, render_template, g


def db_startup():
    abs_path_db = os.path.abspath('chinook.db')
    dir_path_db = os.path.dirname(abs_path_db)
    db_file_path = os.path.join(dir_path_db, 'chinook.db')

    conn = sqlite3.connect(db_file_path)

    abs_path_script = os.path.abspath('schema.sql')
    dir_path_script = os.path.dirname(abs_path_script)
    script_file_path = os.path.join(dir_path_script, 'schema.sql')

    #root_path = os.path.exists(os.path.join(root_directory, 'softwareEngGruppe6'))
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
    return db
'''

'''
def list_items():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return render_template("EXAMPLE")
'''