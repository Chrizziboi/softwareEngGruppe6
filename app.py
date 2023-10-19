import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from backend.users.user import user
from backend.users.admin import admin

app = Flask(__name__)





from flask import Flask, render_template

DATABASE = 'chinook.db'

def user_login():
    pass

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = login(username)
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
