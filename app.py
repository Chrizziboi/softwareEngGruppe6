import sqlite3

from flask import Flask, render_template
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



user1 = user(userID=int(1), username="user")
print(user.get_user_info(user1))

admin1 = admin(adminID=int(1), adminname="admin")
print(admin.get_admin_info(admin1))

