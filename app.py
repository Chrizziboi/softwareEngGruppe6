import sqlite3

from flask import Flask
from backend.users.user import user
from backend.users.admin import admin

app = Flask(__name__)

from flask import Flask, render_template

DATABASE = 'chinook.db'

app = Flask(__name__)

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

user1 = user(userID=int(1), username="user", login=True)
print(user.get_user_info(user1))

admin1 = admin(adminID=int(1), adminname="admin", login=True)
print(admin.get_admin_info(admin1))

