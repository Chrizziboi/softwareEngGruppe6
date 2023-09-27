from flask import Flask
#from backend.users.admin import admin
from backend.users.user import user

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome to Expedition Planner!'



if __name__ == '__main__':
    app.run()

user1 = user(userID=int(1), username="bruker")
print(user.get_user_info(user1))