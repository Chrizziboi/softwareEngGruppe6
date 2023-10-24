import sqlite3

from flask import Flask, render_template, redirect, url_for, request
from backend.users.user import user
from backend.users.admin import admin

app = Flask(__name__)

DATABASE = 'chinook.db'

def user_login():
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user-page')
def userpage():
    return render_template('user-page.html')

@app.route('/admin-page')
def adminpage():
    return render_template('admin-page.html')

if __name__ == '__main__':
    app.run(debug=True)

def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE)
    return db

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
    return render_template("items.html")

#@app.route("/add_item", methods=["POST"])
def add_item():
    name = request.form["name"]
    if name:
        conn = get_db()
        conn.execute("INSERT INTO items (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
    return redirect(url_for("list_items"))

user1 = user(userID=int(1), username="user")
print(user.get_user_info(user1))

admin1 = admin(adminID=int(1), adminname="admin")
print(admin.get_admin_info(admin1))

