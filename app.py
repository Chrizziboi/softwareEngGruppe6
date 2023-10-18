import sqlite3
from flask import Flask
from backend.users.user import user
from backend.users.admin import admin

app = Flask(__name__)

from flask import Flask, render_template

DATABASE = 'chinook.db'

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE)
    return db

def create_table():
    conn = get_db()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

def register_user(username, password):
    conn = get_db()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def login(username, password):
    conn = get_db()
    cursor = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login(username, password)
        if user:
            session['user'] = user['username']
            return f"Login Successful!\n Welcome {username}!, to a new expedition! <a href='/logout'>Logout</a>".format(user['username'])
        else:
            return 'Login failed! <a href="/index">Try again</a>'
    return render_template('index.html')

@app.route
def change_user():
    session.pop('user', None)
    return "Logged out! <a href='/index'>Login again</a>"

user1 = user(userID=int(1), username="user", password=True)
print(user.get_user_info(user1))

admin1 = admin(adminID=int(1), adminname="admin", login=True)
print(admin.get_admin_info(admin1))

