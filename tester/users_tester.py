import pytest

class admin:
    def __init__(self, adminID, adminname):
        self.adminID = int(adminID)
        self.adminname = str(adminname)

class user:

    def __init__(self, userID, username):
        self.userID = int(userID)
        self.username = str(username)

def test_create_user():
    user1 = user(1,"user")

    assert user1.userID == 1
    assert user1.username == "user"




def test_create_admin():
    admin1 = admin(1, "admin")

    assert admin1.adminID == 1
    assert admin1.adminname == "admin"
