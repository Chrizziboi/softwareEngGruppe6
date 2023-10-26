import sqlite3

from flask import Flask, render_template, redirect, url_for, request
from backend.users.user import user
from backend.users.admin import admin
from backend.json import *
from backend.database.db import db_startup

app = Flask(__name__)

DATABASE = 'chinook.db'

db_startup()

user1 = user(userID=int(1), username="user")
print(user.get_user_info(user1))

admin1 = admin(adminID=int(1), adminname="admin")
print(admin.get_admin_info(admin1))

def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user-page')
def userpage():
    user1 = user(userID=1, username="user")
    return render_template('user-page.html', user=user1)

@app.route("/user-info")
def user_info():

    return render_template('user-info.html', user=user1)

def admin_info():
    admin1 = admin(adminID=1, adminname="admin")
    return render_template('admin-info.html', admin=admin1)

@app.route('/admin-page')
def adminpage():
    admin1 = admin(adminID=1, adminname="admin")
    return render_template('admin-page.html', admin=admin1)

@app.route("/add_item", methods=["POST"])
def add_item():
    name = request.form["name"]
    if name:
        conn = get_db()
        conn.execute("INSERT INTO items (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
    return redirect(url_for("list_items"))

def login():
    pass
def create_table():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    conn.close()

def list_items():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return render_template("EXAMPLE")

if __name__ == '__main__':
    app.run(debug=True)


