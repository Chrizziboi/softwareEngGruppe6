from flask import Flask
#from backend.users.admin import admin
from backend.users.user import user
from backend.users.admin import admin


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome to Expedition Planner!'

def user_login():
    pass




if __name__ == '__main__':
    app.run()

user1 = user(userID=int(1), username="user", login=True)
print(user.get_user_info(user1))

admin1 = admin(adminID=int(1), adminname="admin", login=True)
print(admin.get_admin_info(admin1))
