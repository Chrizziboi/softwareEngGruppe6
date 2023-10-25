import pytest
from backend.users.user import user
from app import user1
from app import admin1
from backend.users.admin import admin


def test_create_user():
    user1 = user(1,"user")

    assert user1.userID == 1
    assert user1.username == "user"




def test_create_admin():
    admin1 = admin(1, "admin")

    assert admin1.adminID == 1
    assert admin1.adminname == "admin"
