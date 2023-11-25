import pytest

class admin:
    def __init__(self, adminID, adminname):
        self.adminID = int(adminID)
        self.adminname = str(adminname)

class user:

    def __init__(self, userID, username): #parameter password for a system that would use password
        self.userID = int(userID)
        self.username = str(username)
        #self.password = str(password)

    def get_user_info(self):
        return f"UserID: {self.userID}, Username: {self.username}."

    def get_username(self):
        return self.username
    def get_userID(self):
        return f"{self.userID}"

    def has_shopping_cart(self, shoppingCart):
        return shoppingCart is not None

def test_create_user():
    user1 = user(1,"user")

    assert user1.userID == 1
    assert user1.username == "user"


def test_create_admin():
    admin1 = admin(1, "admin")

    assert admin1.adminID == 1
    assert admin1.adminname == "admin"



def test_get_userID(userID=1):
    assert userID == 1

