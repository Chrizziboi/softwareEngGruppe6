import pytest


class admin:
    def __init__(self, adminID, adminname):
        self.adminID = int(adminID)
        self.adminname = str(adminname)


class user:

    def __init__(self, userID, username):  # parameter password for a system that would use password
        self.userID = int(userID)
        self.username = str(username)
        # self.password = str(password)

    def get_user_info(self):
        return f"UserID: {self.userID}, Username: {self.username}."

    def get_username(self):
        return self.username

    def get_userID(self):
        return f"{self.userID}"

    def has_shopping_cart(self, shoppingCart):
        return shoppingCart is not None


@pytest.fixture()
def user_fixture():
    return user(1, "user")


@pytest.fixture()
def admin_fixture():
    return admin(1, "admin")


def test_create_user(user_fixture):
    assert user_fixture.userID == 1
    assert user_fixture.username == "user"


def test_create_admin(admin_fixture):
    assert admin_fixture.adminID == 1
    assert admin_fixture.adminname == "admin"
